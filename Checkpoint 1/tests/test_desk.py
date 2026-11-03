"""Offline source/period regressions and mocked SDK orchestration; no paid calls."""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from desk import Desk, SECClient, TEMPLATE, read_json, run_roles, core_audit_claims


class DeskTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="checkpoint1-tests-")
        cls.run_dir = Path(cls.temp.name) / "run"
        recorded = BASE / read_json(BASE / "latest_run.json")["run_dir"]
        shutil.copytree(recorded / "raw", cls.run_dir / "raw")
        shutil.copytree(recorded / "market_data", cls.run_dir / "market_data")
        shutil.copy2(recorded / "market_input.json", cls.run_dir / "market_input.json")
        config = read_json(recorded / "configuration.json")
        cls.desk = Desk(**config, run_dir=cls.run_dir, offline=True)
        with contextlib.redirect_stdout(io.StringIO()):
            cls.desk.run()

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_latest_annual_and_class_a_eps(self):
        f = self.desk.facts["V"]
        self.assertEqual(f["revenue"]["end"], "2025-09-30")
        self.assertEqual(f["revenue"]["value"], 40_000_000_000)
        self.assertEqual(f["diluted_eps"]["value"], 10.20)
        self.assertEqual(f["diluted_eps"]["dimensions"],
                         {"us-gaap:StatementClassOfStockAxis": "us-gaap:CommonClassAMember"})
        self.assertIn("inline XBRL", f["diluted_eps"]["method"])
        self.assertEqual(f["capex"]["value"], 1_482_000_000)
        self.assertEqual(f["current_debt"]["value"], 5_569_000_000)

    def test_all_saved_fact_lines_and_periods(self):
        for ticker, facts in self.desk.facts.items():
            filing = self.desk.filings[ticker]["10-K"]
            for key, fact in facts.items():
                with self.subTest(ticker=ticker, metric=key):
                    lines = (self.run_dir / fact["file"]).read_text(encoding="utf-8").splitlines()
                    self.assertEqual(lines[fact["line"] - 1], fact["source_text"])
                    self.assertEqual(fact["accession"], filing["accession"])
                    if not key.startswith("prior_"):
                        self.assertEqual(fact["end"], filing["report_date"])

    def test_old_revenue_tag_does_not_replace_current_definition(self):
        original = self.desk.sec.json
        data_url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001403161.json"
        data = copy.deepcopy(original(data_url))
        current = data["facts"]["us-gaap"]["RevenueFromContractWithCustomerExcludingAssessedTax"]
        old = [r for r in current["units"]["USD"]
               if r["end"] == "2024-09-30" and r.get("accn") == "0001403161-25-000089"]
        # A higher-priority candidate holds only the old fiscal year. The
        # comparative must retain the selected latest-year revenue definition.
        data["facts"]["us-gaap"]["Revenues"] = {"units": {"USD": old}}
        with patch.object(self.desk.sec, "json", side_effect=lambda url: data if url == data_url else original(url)):
            f = self.desk.annual_facts("V")
        self.assertEqual(f["revenue"]["value"], 40_000_000_000)
        self.assertEqual(f["prior_revenue"]["value"], 35_926_000_000)
        self.assertEqual(f["revenue"]["tag"], f["prior_revenue"]["tag"])

    def test_earnings_quarter_is_not_event_date_or_service_volume_lag(self):
        self.assertEqual(self.desk.quarter["period_end"], "2026-09-30")
        self.assertEqual(self.desk.quarter["release_date"], "2026-10-27")
        self.assertIn("2.02", self.desk.filings["V"]["earnings"]["items"])
        self.assertTrue(self.desk.filings["V"]["earnings"]["release_url"].endswith("q42026earningsrelease.htm"))
        self.assertEqual(self.desk.quarter["observations"]["quarter_gaap_diluted_eps"]["value"], 3.19)
        self.assertAlmostEqual(self.desk.quarter["revenue_growth"]["value"], (12139 / 10724 - 1) * 100)

    def test_exact_eleven_audit_categories_and_blank_human_marks(self):
        claims = core_audit_claims(self.desk)
        self.assertEqual([c["id"] for c in claims], list(range(1, 12)))
        self.assertEqual([c["claim"] for c in claims], [
            "Total revenue, latest fiscal year", "Revenue growth versus the prior year",
            "Operating income and operating margin", "Net income attributable to the company",
            "Diluted earnings per share, GAAP", "Return on average equity", "Debt to equity",
            "Free cash flow", "The latest quarter's revenue",
            "The quarter's growth versus the same quarter last year", "The quarter's diluted EPS, GAAP"])
        text = (self.run_dir / "human_audit.md").read_text(encoding="utf-8")
        import re
        rows = [line for line in text.splitlines() if re.match(r"^\| \d+ \|", line)]
        self.assertEqual(len(rows), 11)
        for row in rows:
            cells = row.split("|")
            self.assertEqual(cells[4].strip(), "")
            self.assertEqual(cells[5].strip(), "")
        signoff = (self.run_dir / "human_signoff.md").read_text(encoding="utf-8")
        self.assertIn("Anthropic Open Source.pdf", signoff)
        self.assertIn("pending human review", signoff)

    def test_provider_price_receipt_replays_the_real_observation(self):
        from market_data import get_market_close
        receipt = get_market_close("V", "2026-10-27", self.run_dir, provider="lseg", offline=True)
        self.assertEqual(receipt["provider"], "LSEG")
        self.assertEqual(receipt["instrument"], "V.N")
        self.assertEqual(receipt["field"], "TRDPRC_1")
        self.assertEqual(receipt["adjustments"], "unadjusted")
        self.assertEqual(receipt["close_usd"], 401.86)
        with self.assertRaisesRegex(ValueError, "different ticker or trade date"):
            get_market_close("V", "2026-10-26", self.run_dir, provider="lseg", offline=True)
        with self.assertRaisesRegex(ValueError, "requested RIC"):
            get_market_close("V", "2026-10-27", self.run_dir, provider="lseg", ric="MA.N", offline=True)

    def test_lseg_sdk_request_and_receipt_integrity(self):
        from market_data import get_market_close
        import pandas as pd
        frame = pd.DataFrame({"TRDPRC_1": [401.86]}, index=pd.to_datetime(["2026-10-27"]))
        with tempfile.TemporaryDirectory(prefix="checkpoint1-lseg-") as directory:
            with patch("lseg.data.open_session") as opened, patch("lseg.data.close_session"), \
                 patch("lseg.data.get_history", return_value=frame) as history, \
                 patch.dict(os.environ, {"LSEG_APP_KEY": "test-only-app-key"}):
                receipt = get_market_close("V", "2026-10-27", directory, "lseg", "V.N")
            opened.assert_called_once_with(name="desktop.workspace", app_key="test-only-app-key")
            history.assert_called_once_with(universe="V.N", fields=["TRDPRC_1"], interval="1D",
                                           start="2026-10-27", end="2026-10-27", adjustments="unadjusted")
            record_text = (Path(directory) / "market_input.json").read_text(encoding="utf-8")
            self.assertNotIn("test-only-app-key", record_text)
            (Path(directory) / receipt["data_file"]).write_text("modified", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                get_market_close("V", "2026-10-27", directory, "lseg", offline=True)

    def test_ratios_and_missing_peer_debt(self):
        r = self.desk.ratios["V"]
        self.assertAlmostEqual(r["operating_margin"]["value"], 59.985)
        self.assertAlmostEqual(r["return_on_average_equity"]["value"], 52.06759598162137)
        self.assertAlmostEqual(r["debt_to_equity"]["value"], (19_602 + 5_569) / 37_909)
        self.assertEqual(r["free_cash_flow"]["value"], 21_577_000_000)
        self.assertAlmostEqual(r["price_earnings"]["value"], 401.86 / 10.20)
        self.assertNotIn("current_debt", self.desk.facts["PYPL"])
        self.assertNotIn("debt_to_equity", self.desk.ratios["PYPL"])
        self.assertIn("current_debt", read_json(self.run_dir / "PYPL/unavailable_facts.json"))

    def test_offline_cache_missing_and_corrupt_responses_fail(self):
        with tempfile.TemporaryDirectory(prefix="checkpoint1-cache-") as directory:
            client = SECClient(directory, offline=True)
            with self.assertRaises(FileNotFoundError):
                client.get("https://data.sec.gov/not-recorded.json")
            content_path = Path(directory) / "raw/bad.gz"
            import gzip
            content_path.write_bytes(gzip.compress(b"changed response"))
            client.manifest["https://data.sec.gov/corrupt.json"] = {"file": "bad.gz", "sha256": "wrong"}
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                client.get("https://data.sec.gov/corrupt.json")

    def _mock_roles(self, reject=False):
        calls = []
        drafts = {
            "Research Analyst": {"sections": [{"title": TEMPLATE[i], "markdown": "Qualitative inference."} for i in [0, 1, 3]],
                                 "recommendation": "", "decision_metric": ""},
            "Financial Analyst": {"sections": [{"title": TEMPLATE[2], "markdown": "Reported margin: {{ratio:operating_margin}}."}],
                                  "recommendation": "", "decision_metric": ""},
            "Investment Advisor": {"sections": [{"title": TEMPLATE[4], "markdown": "Hold. Deciding metric: {{ratio:price_earnings}}."}],
                                   "recommendation": "Hold", "decision_metric": "price_earnings"},
        }
        class Responses:
            def create(inner, **kwargs):
                payload = json.loads(kwargs["input"])
                if kwargs["text"]["format"]["name"] == "review":
                    role = "Strategy Manager"
                    result = {"approved": not reject, "failures": [{"role": "Financial Analyst", "issue": "Repair the share-class explanation."}] if reject else []}
                elif "qualitative" in payload["task"]:
                    role = "Research Analyst"
                    result = drafts[role]
                elif "quantitative" in payload["task"]:
                    role = "Financial Analyst"
                    result = drafts[role]
                else:
                    role = "Investment Advisor"
                    result = drafts[role]
                calls.append((role, payload))
                return SimpleNamespace(status="completed", output_text=json.dumps(result),
                                       id=f"mock-response-{len(calls)}", usage=None)
        return SimpleNamespace(responses=Responses()), calls

    def test_four_distinct_calls_and_advisor_context_boundary(self):
        client, calls = self._mock_roles()
        with tempfile.TemporaryDirectory(prefix="checkpoint1-roles-") as directory:
            output = Path(directory)
            with patch.object(self.desk, "run_dir", output), patch("openai.OpenAI", return_value=client), \
                 patch.dict(os.environ, {"API_KEY": "mock-only-key"}), contextlib.redirect_stdout(io.StringIO()):
                path = run_roles(self.desk)
            self.assertTrue(path.exists())
            self.assertEqual([r for r, _ in calls], ["Research Analyst", "Financial Analyst", "Investment Advisor", "Strategy Manager"])
            advisor_context = calls[2][1]["context"]
            self.assertEqual(set(advisor_context), {"research", "financial", "decision_metrics"})
            self.assertIn("computed_tables", advisor_context["financial"])
            self.assertNotIn("{{", advisor_context["financial"]["sections"][0]["markdown"])
            result = path.read_text(encoding="utf-8")
            self.assertEqual([line[3:] for line in result.splitlines() if line.startswith("## ")], TEMPLATE)
            self.assertNotIn("mock-only-key", result)

    def test_one_revision_then_no_report_when_manager_still_rejects(self):
        client, calls = self._mock_roles(reject=True)
        with tempfile.TemporaryDirectory(prefix="checkpoint1-reject-") as directory:
            output = Path(directory)
            with patch.object(self.desk, "run_dir", output), patch("openai.OpenAI", return_value=client), \
                 patch.dict(os.environ, {"API_KEY": "mock-only-key"}), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(RuntimeError, "after one revision"):
                    run_roles(self.desk)
            self.assertFalse((output / "report.md").exists())
            self.assertTrue((output / "model_roles/unresolved_review.json").exists())
            self.assertEqual([r for r, _ in calls].count("Financial Analyst"), 2)
            self.assertEqual([r for r, _ in calls].count("Strategy Manager"), 2)

    def test_missing_model_key_fails_without_calling_provider(self):
        with patch.dict(os.environ, {"API_KEY": "", "OPENAI_API_KEY": ""}), patch("openai.OpenAI") as constructor:
            with self.assertRaisesRegex(RuntimeError, "No model API key"):
                run_roles(self.desk)
            constructor.assert_not_called()


if __name__ == "__main__":
    unittest.main()
