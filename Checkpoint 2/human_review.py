"""Prepare an unmarked review worksheet from the actual submitted report."""
from pathlib import Path
from verifier import read_json,extract_claims,citation,digest,rounded


def prepare_blank_audit(run_dir):
    from team import core_groups
    run_dir=Path(run_dir)
    report=(run_dir/"verified_report.md").read_text(encoding="utf-8")
    claims=extract_claims(report)
    catalog=read_json(run_dir/"catalog.json")
    config=read_json(run_dir/"run_config.json")
    def clean(v):return str(v).replace("|","/").replace("\n"," ")
    def observed(keys):
        selected=[c for c in claims if c["source"] in keys]
        return "; ".join(dict.fromkeys(f"{rounded(c['value']):,.2f} {c['unit']} ({c['source']})" for c in selected)),", ".join(c["id"] for c in selected)
    def where(keys):return "; ".join(citation(catalog[k],catalog) for k in keys if k in catalog)
    lines=[f"# Checkpoint 2 human audit - {config['ticker']}","",
           "**Human reviewer / date:** ____________________",
           "**Report file and version reviewed:** ____________________",
           f"**Generated verified report SHA-256:** {digest(run_dir/'verified_report.md')}",
           "**Errors (wrong + unsupported):** ____   **Missing claims:** ____",
           "**Decision (approve or return for revision):** ____________________","",
           "Fill Filing says and Mark only after opening the cited filing. Automatic marks are not human findings. Repeated occurrences are listed by claim ID so they can all be checked.","",
           "Marks: Correct; Wrong; Unsupported; Missing; Not in filings. Record the filing's correct figure and the necessary correction for a non-correct claim.","",
           "## Eleven core claims","","| Claim | Report said | Occurrences | Filing says (human) | Mark (human) | Where |","|---|---|---|---|---|---|"]
    core=set()
    for group,keys in core_groups(config["ticker"]).items():
        core.update(keys);values,ids=observed(keys)
        lines.append("| "+" | ".join(clean(v) for v in [group,values or "Not stated",ids,"","",where(keys)])+" |")
    lines += ["","## Other numerical claims","","| Claim/source | Report said | Occurrences | Filing says (human) | Mark (human) | Where |","|---|---|---|---|---|---|"]
    for key in dict.fromkeys(c["source"] for c in claims if c["source"] not in core):
        values,ids=observed([key])
        lines.append("| "+" | ".join(clean(v) for v in [key,values,ids,"","",where([key])])+" |")
    lines += ["","## Three Insight checks","","| Insight | Numerical claim/source | Source checked by human | Adds to headline? Human explanation |","|---|---|---|---|"]
    for c in claims:
        if c["text"].startswith("Insight:"):
            lines.append(f"| {clean(c['text'])} | {clean(c['id']+' / '+c['source'])} | | |")
    lines += ["","## Report and partner checks","",
              "**Five required report parts present / human mark:** ____________________",
              "**Buy/Hold/Sell names a reported metric using checked numbers / human mark:** ____________________","",
              "**Partner name / selected ticker / selection date:** ____________________",
              "**Partner claim one / filing value / mark / source:** ____________________",
              "**Partner claim two / filing value / mark / source:** ____________________",
              "**Partner's Insight citation checked / finding:** ____________________","",
              "## Corrections and recheck","",
              "**Claim / responsible role / correction / new report version / recheck:** ____________________","",
              "Keep the original findings. Review the corrected version before recording approval. No human mark or authorship is supplied by this worksheet.",""]
    (run_dir/"human_audit.md").write_text("\n".join(lines),encoding="utf-8")
