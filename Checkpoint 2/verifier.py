"""Independent verifier: report + saved evidence only; no access to analyst prompts."""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
import re
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False), encoding="utf-8")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe_file(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Evidence path escapes the saved run.")
    return path


def seal_evidence(root):
    root = Path(root)
    paths = [root / "catalog.json", root / "quarter_observations.json"]
    paths += list(root.glob("*/facts.json")) + list(root.glob("*/*.txt"))
    if (root / "market_input.json").exists():
        paths += [root / "market_input.json"] + list((root / "market_data").glob("*.csv"))
    hashes = {p.relative_to(root).as_posix(): digest(p) for p in paths if p.is_file()}
    write_json(root / "evidence_manifest.json", hashes)


def check_evidence(root):
    root = Path(root)
    for relative, expected in read_json(root / "evidence_manifest.json").items():
        if digest(safe_file(root, relative)) != expected:
            raise ValueError(f"Saved evidence SHA-256 mismatch: {relative}")


def normalized(value):
    return re.sub(r"\s+", " ", value).strip()


def rounded(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


# The report's complete numeric records live in fenced JSON. They are visibly
# rendered as claim cards, not hidden in a sidecar that could disagree with prose.
CLAIM_BLOCK = re.compile(r"```claim\s*\n(.*?)\n```", re.S)


def clean_prose(text):
    text=re.sub(r"\[\[[^\]]+\]\]","",text)
    text=re.sub(r"\[source:\s*[^\]]+\]","",text)
    text=re.sub(r"\b(?:10-[KQ]|8-K|Exhibit 99\.1)\b","",text,flags=re.I)
    return text


def has_unstructured_quantity(text):
    text=clean_prose(text)
    if re.search(r"\d",text):return True
    words=r"(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)"
    return bool(re.search(r"\b"+words+r"(?:[\s\-\u2010-\u2014]+"+words+r"){0,5}[\s\-\u2010-\u2014]+(?:percent|dollars|basis points|weeks|months|years)\b",text,re.I))


def claim_block(claim):
    return "```claim\n" + json.dumps(claim, ensure_ascii=False, allow_nan=False) + "\n```"


def extract_claims(report):
    claims = []
    for match in CLAIM_BLOCK.finditer(report):
        claim = json.loads(match.group(1))
        required = {"id", "text", "value", "unit", "source", "period", "definition", "inputs"}
        if not required.issubset(claim):
            raise ValueError("Malformed quantitative claim in compiled report.")
        claims.append(claim)
    if len({c["id"] for c in claims}) != len(claims):
        raise ValueError("Duplicate claim IDs in compiled report.")
    return claims


def evaluate(key, catalog, root, visiting=None):
    """Recompute with a fixed formula registry; never eval model expressions."""
    visiting = set() if visiting is None else set(visiting)
    if key in visiting:
        raise ValueError("Cyclic calculation source.")
    visiting.add(key)
    entry = catalog[key]
    kind = entry["kind"]
    if kind == "fact":
        saved = read_json(safe_file(root, entry["facts_file"]))[entry["metric"]]
        for field in ("tag", "start", "end", "unit", "accession", "value", "line", "dimensions", "context"):
            if entry[field] != saved[field]:
                raise ValueError(f"Fact context differs from saved XBRL facts: {key} {field}")
        lines = safe_file(root, saved["file"]).read_text(encoding="utf-8").splitlines()
        if normalized(lines[saved["line"] - 1]) != normalized(saved["source_text"]):
            raise ValueError("Quoted fact row is absent from the saved filing.")
        return float(saved["value"])
    if kind == "quarter":
        saved = read_json(Path(root) / "quarter_observations.json")
        obs = saved["observations"][entry["metric"]]
        if obs["value"] != entry["value"] or saved["accession"] != entry["accession"]:
            raise ValueError("Quarter observation differs from saved extraction.")
        if saved["period_end"] != entry["quarter_end"]:
            raise ValueError("Quarter-end context mismatch.")
        lines = safe_file(root, saved["file"]).read_text(encoding="utf-8").splitlines()
        if normalized(lines[obs["line"] - 1]) != normalized(entry["quote"]):
            raise ValueError("Quarter source line is absent.")
        cells = [float(c.strip().replace(",", "").replace("$", ""))
                 for c in lines[obs["line"] - 1].split("|")
                 if re.fullmatch(r"\s*\$?\s*[\d,]+(?:\.\d+)?\s*", c)]
        if cells[entry["column_index"]] * entry["scale"] != obs["value"]:
            raise ValueError("Quarter value does not match its exact statement column.")
        return float(obs["value"])
    if kind == "price":
        receipt = read_json(Path(root) / "market_input.json")
        if digest(safe_file(root, receipt["data_file"])) != receipt["sha256"]:
            raise ValueError("Market receipt data hash differs.")
        if receipt["trade_date"] != entry["period"] or receipt["close_usd"] != entry["value"]:
            raise ValueError("Market date/value differs from receipt.")
        return float(receipt["close_usd"])
    if kind == "line":
        lines = safe_file(root, entry["file"]).read_text(encoding="utf-8").splitlines()
        if normalized(entry["quote"]) not in normalized(lines[entry["line"] - 1]):
            raise ValueError("Source quotation is absent from its line.")
        return float(entry["value"])
    vals = [evaluate(k, catalog, root, visiting) for k in entry["inputs"]]
    formulas = {
        "growth": lambda a, b: (a / b - 1) * 100,
        "margin": lambda a, b: a / b * 100,
        "roe": lambda n, b, e: n / ((b + e) / 2) * 100,
        "de": lambda a, b, e: (a + b) / e,
        "fcf": lambda a, b: a - b,
        "pe": lambda p, e: p / e,
    }
    return formulas[entry["formula"]](*vals)


def citation(entry, catalog):
    if entry["kind"] == "ratio":
        return entry["arithmetic"] + "; " + "; ".join(citation(catalog[k], catalog) for k in entry["inputs"])
    if entry["kind"] == "price":
        return f"market_input.json; {entry['period']}; {entry['definition']}"
    return (f"{entry['file']} L{entry['line']}; {entry.get('tag', 'statement column')}; "
            f"{entry['period']}; {entry['accession']}; {entry.get('quote', entry.get('source_text', ''))}")


def canonical_claim(claim, key, catalog, root):
    entry = catalog[key]
    result = deepcopy(claim)
    result.update(value=float(evaluate(key, catalog, root)), source=key,
                  unit=entry["unit"], period=entry["period"], definition=entry["definition"],
                  inputs=[{"source": k, "value": evaluate(k, catalog, root)} for k in entry.get("inputs", [])])
    if "quote" in result:
        result["quote"]=entry.get("source_text",entry.get("quote",""))
    return result


def verify_report(report, catalog, root, semantic_call=None):
    """semantic_call receives no paths to prompts and no role/node outputs."""
    claims = extract_claims(report)
    marks = []
    for claim in claims:
        key = claim["source"]
        mark, reason, replacement = "correct", "Exact source context and rounded value match.", None
        if key not in catalog:
            mark, reason = "unsupported", "No saved source for this number."
        else:
            entry = catalog[key]
            expected = evaluate(key, catalog, root)
            if any(claim[f] != entry[f] for f in ("period", "definition", "unit")):
                mark, reason = "unsupported", "The period, definition or unit differs from the saved evidence."
            elif rounded(claim["value"]) != rounded(expected):
                mark, reason = "wrong", "Report value differs from independently recomputed evidence."
            if "quote" in claim and normalized(claim["quote"])!=normalized(entry.get("source_text",entry.get("quote",""))):
                mark,reason="wrong","The report's quoted source line differs from the saved filing line."
            quoted_inputs = claim["inputs"]
            if entry["kind"] == "ratio":
                actual = {i["source"]: i["value"] for i in quoted_inputs}
                if set(actual) != set(entry["inputs"]) or any(
                        rounded(actual[k]) != rounded(evaluate(k, catalog, root)) for k in entry["inputs"] if k in actual):
                    mark, reason = "unsupported", "The ratio's quoted inputs differ from the saved source inputs."
            if mark != "correct":
                replacement = canonical_claim(claim, key, catalog, root)
        marks.append({"id": claim["id"], "mark": mark, "reason": reason,
                      "reported": claim["value"], "corrected": replacement["value"] if replacement else None,
                      "replacement": replacement,
                      "evidence": citation(catalog[key], catalog) if key in catalog else "No source",
                      "semantic_status": "not_run"})
    # Numerical prose outside the claim format cannot silently evade verification.
    body = "\n".join(report.splitlines()[2:])
    body = CLAIM_BLOCK.sub("", body)
    body = re.sub(r"<!-- thesis-start -->.*?<!-- thesis-end -->", "", body, flags=re.S)
    for index, line in enumerate(body.splitlines()):
        if has_unstructured_quantity(line):
            marks.append({"id": f"UNSOURCED-{index}", "mark": "unsupported",
                          "reason": "Number outside the required sourced claim format.",
                          "reported": line, "corrected": None, "replacement": None,
                          "evidence": "No auditable claim record", "semantic_status": "not_run"})
    if semantic_call:
        keys={c["source"] for c in claims if c["source"] in catalog}
        def include_inputs(key):
            for child in catalog[key].get("inputs",[]):
                if child not in keys:
                    keys.add(child);include_inputs(child)
        for key in list(keys):include_inputs(key)
        used_catalog={k:catalog[k] for k in sorted(keys)}
        files = {e["file"] for e in used_catalog.values() if "file" in e}
        # Give the model the saved lines with surrounding headers/definitions,
        # rather than resending several entire annual filings beyond its context.
        excerpts = {}
        for filename in sorted(files):
            lines = safe_file(root, filename).read_text(encoding="utf-8").splitlines()
            wanted = set()
            for entry in used_catalog.values():
                if entry.get("file") == filename:
                    wanted.update(range(max(1, entry["line"] - 8), min(len(lines), entry["line"] + 8) + 1))
            excerpts[filename] = "\n".join(f"L{n}: {lines[n-1]}" for n in sorted(wanted))
        fields={"kind","value","unit","period","definition","tag","start","end","accession","file","line","context","dimensions","inputs","arithmetic","formula","column_index","scale"}
        facts={k:{f:v for f,v in e.items() if f in fields} for k,e in used_catalog.items()}
        payload = {"task": "Check every numerical claim's meaning, period and definition; skip the marked subjective thesis. Saved XBRL facts are authoritative for their exact context. Return one verdict per claim ID; code failures cannot be approved away.",
                   "context": {"report": report, "saved_facts": facts,
                               "filing_texts": excerpts,
                               "code_marks": [{k:m[k] for k in ("id","mark","reason")} for m in marks]},
                   "expected_output": "One semantic verdict for each sourced claim ID; correction source or empty string."}
        results = semantic_call(payload)
        verdicts = {v["id"]: v for v in results["verdicts"]}
        # A proposed numerical correction must itself exist in saved evidence.
        # Give the Verifier one bounded opportunity to resolve a scale mistake.
        by_claim={c["id"]:c for c in claims}
        def numeric_disputes(values):
            disputed=[]
            for item in marks:
                v=values.get(item["id"])
                if item["mark"]=="correct" and v and v["mark"]=="wrong" and item["id"] in by_claim:
                    key=v["correction_source"]
                    if key not in catalog or rounded(evaluate(key,catalog,root))==rounded(by_claim[item["id"]]["value"]):
                        disputed.append(item["id"])
            return disputed
        disputed=numeric_disputes(verdicts)
        if disputed:
            retry=deepcopy(payload)
            retry["task"]+=" Your prior wrong-value verdicts for "+", ".join(disputed)+" contradict the saved normalized values: USD values must not be rescaled to printed millions/thousands. Recheck once and return all claim IDs. Use unsupported for a genuine meaning/definition mismatch; do not invent numeric magnitudes."
            results=semantic_call(retry)
            verdicts={v["id"]:v for v in results["verdicts"]}
            if numeric_disputes(verdicts):
                raise ValueError("Semantic numeric corrections remain inconsistent with saved facts after the bounded recheck.")
        sourced_ids={c["id"] for c in claims}
        all_ids={m["id"] for m in marks}
        if not sourced_ids.issubset(verdicts) or not set(verdicts).issubset(all_ids) or len(verdicts)!=len(results["verdicts"]):
            raise ValueError("Semantic verifier omitted, duplicated or invented a claim ID.")
        by_id = {c["id"]: c for c in claims}
        for item in marks:
            if item["id"] not in verdicts or item["id"] not in by_id:
                continue
            v = verdicts[item["id"]]
            item["semantic_status"] = "completed"
            if v["mark"] != "correct":
                item.update(mark=v["mark"], reason=v["reason"])
                new_key = v["correction_source"]
                item["replacement"] = canonical_claim(by_id[item["id"]], new_key, catalog, root) if new_key in catalog else None
                if item["replacement"]:
                    item["replacement"]["text"] = "Corrected sourced metric: " + new_key
                item["corrected"] = item["replacement"]["value"] if item["replacement"] else None
                item["evidence"] = citation(catalog[new_key], catalog) if new_key in catalog else item["evidence"]
    replacements = {m["id"]: m["replacement"] for m in marks if m["mark"] != "correct"}
    corrected = CLAIM_BLOCK.sub(lambda m: claim_block(replacements.get(json.loads(m[1])["id"]) or json.loads(m[1])), report)
    rows = ["| Claim | Mark | Reported | Corrected | Evidence / reason |", "|---|---|---:|---:|---|"]
    for item in marks:
        clean = lambda s: str(s).replace("|", "/").replace("\n", " ")
        rows.append("| " + " | ".join(clean(v) for v in [item["id"], item["mark"], item["reported"],
                    item["corrected"] if item["corrected"] is not None else "", item["reason"] + " " + item["evidence"]]) + " |")
    status = "LIVE semantic check completed" if semantic_call else "CODE ONLY; semantic model check NOT RUN"
    lines = corrected.splitlines()
    verified = "\n".join([lines[0], "", "> Verifier: " + status + ". Marks refer to the original report. Human review pending.", ""]
                          + rows + ["", *lines[1:]])
    return {"marks": marks, "verified_report": verified, "semantic_status": "completed" if semantic_call else "not_run",
            "errors": sum(m["mark"] in {"wrong", "unsupported"} for m in marks),
            "unresolved_errors":sum(m["mark"] in {"wrong","unsupported"} and m["replacement"] is None for m in marks),
            "claim_count": len(claims)}
