"""Meaningful offline regressions: adversarial claims, graph bounds and isolation."""
import contextlib
from copy import deepcopy
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from team import (Draft, FixtureBackend, LiveBackend, ROLES, core_groups, previous_config,
                  run_team, seed_run, verify_only)
from verifier import (canonical_claim, claim_block, digest, extract_claims, read_json, verify_report)


class TeamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="checkpoint2-tests-")
        cls.parent = Path(cls.temp.name)
        cls.config = previous_config()
        with contextlib.redirect_stdout(io.StringIO()):
            cls.result = run_team(cls.config, FixtureBackend(), cls.parent)
        cls.run_dir = Path(cls.result["run_dir"])
        cls.catalog = read_json(cls.run_dir / "catalog.json")
        cls.report = (cls.run_dir / "report.md").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_report_notebook_and_audit_use_the_verifiers_decimal_rounding(self):
        from team import readable_report
        from submission_support import core_coverage,narrative_view
        from human_review import prepare_blank_audit
        margin=self.catalog['V.ratio.operating_margin']['value']
        self.assertEqual(margin,59.985)
        rendered=readable_report(self.report,self.catalog)
        self.assertIn('59.99 %',rendered)
        self.assertNotIn('59.98 %',rendered)
        coverage=core_coverage('V',self.report,self.catalog,self.run_dir)
        self.assertTrue(any('59.99 %' in row['Value'] for row in coverage))
        token_report=self.report+'\n## Rounding test\nMargin [[V.ratio.operating_margin]].\n'
        self.assertIn('59.99 %',narrative_view(token_report,self.catalog,self.run_dir))
        narrative=narrative_view(self.report,self.catalog,self.run_dir)
        self.assertEqual(sum(line.startswith('## ') for line in narrative.splitlines()),5)
        self.assertNotIn('```claim',narrative)
        prepare_blank_audit(self.run_dir)
        audit=(self.run_dir/'human_audit.md').read_text(encoding='utf-8')
        self.assertIn('59.99 %',audit)
        self.assertNotIn('59.98 %',audit)

    def test_clean_claims_core_coverage_and_mandatory_verifier(self):
        v = read_json(self.run_dir / "verification.json")
        self.assertEqual(v["errors"], 0)
        self.assertEqual(v["semantic_status"], "not_run")
        self.assertEqual(self.result["trace"][-1], "Verifier")
        sources = {c["source"] for c in extract_claims(self.report)}
        self.assertEqual(len(core_groups(self.config["ticker"])), 11)
        self.assertTrue(all(set(keys) <= sources for keys in core_groups(self.config["ticker"]).values()))
        self.assertEqual(sum(c["text"].startswith("Insight:") for c in extract_claims(self.report)), 3)

    def test_seeded_eps_growth_period_and_definition_corrected(self):
        for mutation in ("eps_plus_one", "growth_plus_four", "wrong_quarter", "ambiguous_roe"):
            with self.subTest(mutation=mutation), contextlib.redirect_stdout(io.StringIO()):
                seed = seed_run(self.run_dir, mutation, self.parent)
                before = digest(seed / "report.md")
                checked = verify_only(seed, backend=FixtureBackend(), output_parent=self.parent)
                claim_id = read_json(seed / "mutation.json")["claim_id"]
                mark = next(m for m in checked["marks"] if m["id"] == claim_id)
                self.assertIn(mark["mark"], {"wrong", "unsupported"})
                self.assertIsNotNone(mark["corrected"])
                self.assertEqual(digest(seed / "report.md"), before)
                self.assertEqual(read_json(Path(checked["run_dir"]) / "node_order.json"), ["Verifier"])
                self.assertEqual(read_json(seed / "evidence_manifest.json"), read_json(self.run_dir / "evidence_manifest.json"))
                corrected = next(c for c in extract_claims(checked["verified_report"]) if c["id"] == claim_id)
                self.assertAlmostEqual(corrected["value"], mark["corrected"])

    def test_unsourced_number_and_unknown_source_are_unsupported(self):
        v = verify_report(self.report + "\nInvented market share is 999%.\n", self.catalog, self.run_dir)
        self.assertTrue(any(m["id"].startswith("UNSOURCED") and m["mark"] == "unsupported" for m in v["marks"]))
        c = deepcopy(extract_claims(self.report)[0])
        c.update(id="UNKNOWN", source="not.saved", value=99)
        v = verify_report(self.report + "\n" + claim_block(c), self.catalog, self.run_dir)
        self.assertEqual(next(m for m in v["marks"] if m["id"] == "UNKNOWN")["mark"], "unsupported")

    def test_ratio_inputs_are_checked_not_only_result(self):
        c = next(c for c in extract_claims(self.report) if c["inputs"])
        changed = deepcopy(c)
        changed["inputs"][0]["value"] += 1_000_000
        v = verify_report(self.report.replace(claim_block(c), claim_block(changed)), self.catalog, self.run_dir)
        self.assertEqual(next(m for m in v["marks"] if m["id"] == c["id"])["mark"], "unsupported")

    def test_semantic_boundary_and_code_failure_cannot_be_overruled(self):
        c = extract_claims(self.report)[0]
        changed = deepcopy(c)
        changed["value"] += 1
        report = self.report.replace(claim_block(c), claim_block(changed))
        calls = []
        def semantic(payload):
            calls.append(payload)
            return {"verdicts": [{"id": c["id"], "mark": "correct", "reason": "mocked semantic agreement",
                                  "correction_source": ""} for c in extract_claims(report)]}
        v = verify_report(report, self.catalog, self.run_dir, semantic)
        self.assertEqual(set(calls[0]["context"]), {"report", "saved_facts", "filing_texts", "code_marks"})
        self.assertEqual(next(m for m in v["marks"] if m["id"] == c["id"])["mark"], "wrong")
        self.assertEqual(v["semantic_status"], "completed")

    def test_source_tamper_is_rejected(self):
        with contextlib.redirect_stdout(io.StringIO()):
            seed = seed_run(self.run_dir, "eps_plus_one", self.parent)
            fact_file = seed / self.config["ticker"] / "facts.json"
            fact_file.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                verify_only(seed, backend=FixtureBackend(), output_parent=self.parent)

    def test_fixed_graph_retry_bound_and_advisor_context(self):
        class RejectOnce(FixtureBackend):
            def __init__(self):
                self.calls = []
                self.reviews = 0
            def call(self, role, payload, schema):
                self.calls.append((role, payload))
                if role == "Strategy Manager":
                    self.reviews += 1
                    return {"approved": self.reviews > 1, "failures": [{"role": ROLES[1], "issue": "Clarify definition."}] if self.reviews == 1 else []}, {"mode": "mock"}
                return super().call(role, payload, schema)
        backend = RejectOnce()
        with contextlib.redirect_stdout(io.StringIO()):
            result = run_team(self.config, backend, self.parent)
        self.assertEqual(result["trace"], self.result["trace"])
        counts = read_json(Path(result["run_dir"]) / "call_counts.json")
        self.assertTrue(all(n <= 2 for n in counts.values()))
        self.assertEqual(counts[ROLES[1]], 2)
        self.assertEqual(counts[ROLES[2]], 2)
        advisor_calls = [p for r, p in backend.calls if r == ROLES[2]]
        self.assertTrue(all("filing_excerpts" not in p["context"] for p in advisor_calls))
        self.assertEqual(set(advisor_calls[0]["context"]["analyst_outputs"]), set(ROLES[:2]))

    def test_missing_insight_retries_then_manager_failure_is_saved(self):
        class MissingInsight(FixtureBackend):
            def call(self, role, payload, schema):
                result, meta = super().call(role, payload, schema)
                if role == ROLES[0]:
                    result["insight"]["text"] = ""
                return result, meta
        with contextlib.redirect_stdout(io.StringIO()):
            result = run_team(self.config, MissingInsight(), self.parent)
        self.assertFalse(result["manager_approved"])
        self.assertEqual(result["trace"][-1], "Verifier")
        self.assertEqual(read_json(Path(result["run_dir"]) / "call_counts.json")[ROLES[0]], 2)

    def test_unknown_peer_metric_has_specific_repair_and_cannot_be_approved(self):
        class UnknownPeer(FixtureBackend):
            def __init__(self,repair):
                self.repair=repair
                self.feedback=[]
            def call(self,role,payload,schema):
                result,meta=super().call(role,payload,schema)
                if role==ROLES[1]:
                    self.feedback=payload["context"].get("repair_once",[])
                    self.asserted_keys=payload["context"]["available_source_keys"]
                    if not self.feedback or not self.repair:
                        result["sections"][0]["text"]+=" Peer leverage is [[PYPL.ratio.debt_to_equity]]."
                return result,meta
        for repair in (False,True):
            backend=UnknownPeer(repair)
            with self.subTest(repair=repair),contextlib.redirect_stdout(io.StringIO()):
                result=run_team(self.config,backend,self.parent)
            self.assertNotIn("PYPL.ratio.debt_to_equity",backend.asserted_keys)
            self.assertTrue(any("PYPL.ratio.debt_to_equity" in issue and "Remove" in issue for issue in backend.feedback))
            self.assertEqual(result["manager_approved"],repair)
            self.assertLessEqual(read_json(Path(result["run_dir"])/"call_counts.json")[ROLES[1]],2)

    def test_resume_requires_exact_report_live_verification_and_unchanged_evidence(self):
        from prepare_submission import completed_verification
        class MockVerifier(FixtureBackend):
            mode="live"
            def call(self,role,payload,schema):
                return {"verdicts":[{"id":c["id"],"mark":"correct","reason":"Unit-test semantic result",
                                      "correction_source":""} for c in extract_claims(payload["context"]["report"])]}, {
                                      "mode":"live","response_id":"unit-test-only"}
        with contextlib.redirect_stdout(io.StringIO()):
            checked=verify_only(self.run_dir,MockVerifier(),self.parent)
        target=Path(checked["run_dir"])
        # The lookup's root is isolated; roles are copied only for this test.
        resume_root=self.parent/"resume-root"
        resume_root.mkdir()
        (resume_root/"runs").mkdir()
        shutil.copytree(BASE/"roles",resume_root/"roles")
        cached=resume_root/"runs"/target.name
        shutil.copytree(target,cached)
        with patch("prepare_submission.BASE",resume_root):
            self.assertIsNotNone(completed_verification(self.run_dir))
            report=cached/"report.md"
            report.write_text(report.read_text(encoding="utf-8")+"\nChanged report\n",encoding="utf-8")
            self.assertIsNone(completed_verification(self.run_dir))
            shutil.copy2(target/"report.md",report)
            evidence=cached/next(iter(read_json(cached/"evidence_manifest.json")))
            original=evidence.read_bytes()
            evidence.write_bytes(original+b"\nChanged evidence\n")
            self.assertIsNone(completed_verification(self.run_dir))
            evidence.write_bytes(original)
            output=next((cached/"nodes").glob("verifier*_output.json"))
            data=read_json(output)
            data["metadata"]["mode"]="mock"
            output.write_text(json.dumps(data),encoding="utf-8")
            self.assertIsNone(completed_verification(self.run_dir))

    def test_advisor_label_without_metric_justification_cannot_be_approved(self):
        class BareRecommendation(FixtureBackend):
            def call(self,role,payload,schema):
                result,meta=super().call(role,payload,schema)
                if role==ROLES[2]:result["sections"][0]["text"]="Hold"
                return result,meta
        with contextlib.redirect_stdout(io.StringIO()):
            result=run_team(self.config,BareRecommendation(),self.parent)
        self.assertFalse(result["manager_approved"])
        self.assertEqual(result["trace"][-1],"Verifier")
        review=read_json(Path(result["run_dir"])/"manager_review.json")
        self.assertTrue(any("recommendation label alone" in f["issue"] for f in review["failures"]))

    def test_advisor_separate_insight_may_use_another_supported_metric(self):
        class DifferentInsight(FixtureBackend):
            def call(self,role,payload,schema):
                result,meta=super().call(role,payload,schema)
                if role==ROLES[2]:
                    catalog=payload["context"]["catalog"]
                    key=next(k for k in catalog if k!=result["decision_source"] and ".ratio." in k)
                    result["insight"]={"text":"Historical profitability provides separate evidence.",
                                       "source":key,"value":catalog[key]["value"]}
                return result,meta
        with contextlib.redirect_stdout(io.StringIO()):
            result=run_team(self.config,DifferentInsight(),self.parent)
        self.assertTrue(result["manager_approved"])

    def test_changed_offline_ticker_is_rejected_and_key_missing_is_explicit(self):
        config = {**self.config, "ticker": "MA"}
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaisesRegex(ValueError, "differs from source snapshot"):
            run_team(config, FixtureBackend(), self.parent)
        with patch.dict(os.environ, {"API_KEY": "", "OPENAI_API_KEY": ""}), patch("team.load_dotenv"):
            with self.assertRaisesRegex(RuntimeError, "No model API key"):
                LiveBackend()

    def test_full_live_contract_with_mocked_responses_includes_verifier(self):
        class MockLive(FixtureBackend):
            mode = "live"
            def call(self, role, payload, schema):
                if role == "Verifier":
                    claims = extract_claims(payload["context"]["report"])
                    return {"verdicts": [{"id": c["id"], "mark": "correct", "reason": "Mock semantic result",
                                          "correction_source": ""} for c in claims]}, {"mode": "mock"}
                return super().call(role, payload, schema)
        with contextlib.redirect_stdout(io.StringIO()):
            result = run_team(self.config, MockLive(), self.parent)
        counts = read_json(Path(result["run_dir"]) / "call_counts.json")
        self.assertEqual(counts["Verifier"], 1)
        self.assertEqual(read_json(Path(result["run_dir"]) / "verification.json")["semantic_status"], "completed")

    def test_secondary_issuer_uses_its_own_facts(self):
        from team import annual_smoke
        result = annual_smoke("MA", self.config["source_run"], self.parent)
        self.assertEqual(result["errors"], 0)
        self.assertTrue(all(key.startswith("MA.") for key in result["catalog"]))
        self.assertEqual(result["catalog"]["MA.fact.revenue"]["end"], "2025-12-31")
        self.assertFalse(read_json(Path(result["run_dir"]) / "summary.json")["partner_run"])

    def test_fiscal_week_quarter_uses_total_revenue_and_eps_not_sales_or_annual_eps(self):
        from data_tools import CourseDesk
        from team import build_tools
        pointer=read_json(BASE/"costco_data_pointer.json")
        source=BASE/pointer["run_dir"]
        config={**read_json(source/"configuration.json"),"offline":True,"source_run":str(source)}
        target=self.parent/"fiscal-week-data";target.mkdir()
        with contextlib.redirect_stdout(io.StringIO()):
            desk,catalog=build_tools(config,target)
        quarter=read_json(target/"quarter_observations.json")
        self.assertEqual(quarter["quarter_duration"],"16 weeks")
        self.assertEqual(quarter["period_end"],"2026-08-30")
        self.assertEqual(quarter["observations"]["quarter_net_revenue"]["value"],95_723_000_000)
        self.assertNotEqual(quarter["observations"]["quarter_net_revenue"]["value"],93_873_000_000)
        self.assertEqual(quarter["observations"]["quarter_gaap_diluted_eps"]["value"],6.75)
        self.assertEqual(quarter["observations"]["annual_release_gaap_diluted_eps"]["value"],20.76)
        self.assertAlmostEqual(quarter["calculated_quarter_revenue_growth"]["value"],(95_723/86_156-1)*100)
        self.assertEqual(catalog["COST.price"]["value"],896.48)

    def test_numerical_words_do_not_evade_verification(self):
        v=verify_report(self.report+"\nWages were thirty-three dollars.\n",self.catalog,self.run_dir)
        self.assertTrue(any(m["id"].startswith("UNSOURCED") for m in v["marks"]))

    def test_recorded_backend_rejects_fixture_provenance(self):
        from team import RecordedBackend
        with self.assertRaisesRegex(ValueError,"fixture or mock"):
            RecordedBackend(self.run_dir)

    def test_public_cli_has_no_verifier_skip_switch(self):
        import subprocess
        p=subprocess.run([sys.executable,str(BASE/"team.py"),"--help"],capture_output=True,text=True)
        self.assertEqual(p.returncode,0)
        self.assertIn("--verify-only",p.stdout)
        self.assertNotIn("--code-only",p.stdout)
        self.assertNotIn("--offline-fixture",p.stdout)

    def test_approved_manager_none_placeholders_are_not_failures(self):
        class EmptyPlaceholder(FixtureBackend):
            def call(self,role,payload,schema):
                if role=="Strategy Manager":
                    return {"approved":True,"failures":[{"role":ROLES[0],"issue":"none"}]},{"mode":"mock"}
                return super().call(role,payload,schema)
        with contextlib.redirect_stdout(io.StringIO()):
            result=run_team(self.config,EmptyPlaceholder(),self.parent)
        self.assertTrue(result["manager_approved"])
        self.assertEqual(read_json(Path(result["run_dir"])/"call_counts.json")["Strategy Manager"],1)

    def test_semantic_scale_error_gets_one_evidence_based_recheck(self):
        calls=[]
        first_id=extract_claims(self.report)[0]["id"]
        def semantic(payload):
            calls.append(payload)
            return {"verdicts":[{"id":c["id"],"mark":"wrong" if len(calls)==1 and c["id"]==first_id else "correct",
                                 "reason":"Mock scale confusion" if len(calls)==1 else "Normalized source agrees",
                                 "correction_source":""} for c in extract_claims(self.report)]}
        checked=verify_report(self.report,self.catalog,self.run_dir,semantic)
        self.assertEqual(len(calls),2)
        self.assertEqual(checked["errors"],0)

    def test_unresolved_semantic_scale_conflict_stops_after_two_calls(self):
        calls=[]
        def semantic(payload):
            calls.append(payload)
            return {"verdicts":[{"id":c["id"],"mark":"wrong","reason":"Invented numeric scale","correction_source":""}
                                 for c in extract_claims(self.report)]}
        with self.assertRaisesRegex(ValueError,"bounded recheck"):
            verify_report(self.report,self.catalog,self.run_dir,semantic)
        self.assertEqual(len(calls),2)


if __name__ == "__main__":
    unittest.main()
