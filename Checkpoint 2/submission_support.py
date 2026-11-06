"""Load selected evidence and execute the live submission model."""
from pathlib import Path
import re

from team import BASE,RecordedBackend,read_json,run_team,verify_only,core_groups
from verifier import digest,check_evidence,extract_claims,evaluate,CLAIM_BLOCK,rounded


def load_manifest():
    manifest=read_json(BASE/"submission_manifest.json")
    for relative,expected in manifest["source_hashes"].items():
        if digest(BASE/relative)!=expected:
            raise ValueError("Submission source changed after evidence generation: "+relative)
    return manifest


def run_selected_model(source):
    source=Path(source)
    config={**read_json(source/"configuration.json"),"offline":True,"source_run":str(source.resolve()),
            "model_provider":read_json(source/"run_config.json").get("model_provider","purdue"),
            "model":read_json(source/"run_config.json").get("model","gpt-oss:120b")}
    result=run_team(config)
    if not result["manager_approved"]:raise ValueError("Manager review failed.")
    verification=read_json(Path(result["run_dir"])/"verification.json")
    if verification["semantic_status"]!="completed" or verification.get("unresolved_errors",0):
        raise ValueError("Verification is incomplete or unresolved.")
    return result


def narrative_view(report,catalog,run_dir):
    """Render the five model sections with the exact checked token values."""
    run_dir=Path(run_dir)
    result=[]
    for title,body in re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)",report,flags=re.M|re.S):
        text=CLAIM_BLOCK.sub("",body).split("### Financial Analyst evidence")[0].split("### Review record")[0]
        def number(match):
            key=match[1]
            if key not in catalog:return match[0]
            entry=catalog[key]
            return f"**{rounded(evaluate(key,catalog,run_dir)):,.2f} {entry['unit']}** [source: {key}]"
        text=re.sub(r"\[\[([^\]]+)\]\]",number,text)
        result.extend(["## "+title,text.strip()])
    return "\n\n".join(result)


def core_coverage(ticker,report,catalog,run_dir):
    sources={c["source"] for c in extract_claims(report)}
    rows=[]
    for group,keys in core_groups(ticker).items():
        rows.append({"Core claim":group,"Covered":set(keys)<=sources,
                     "Value":"; ".join(f"{rounded(evaluate(k,catalog,run_dir)):,.2f} {catalog[k]['unit']}" for k in keys),
                     "Period":"; ".join(dict.fromkeys(catalog[k]["period"] for k in keys)),
                     "Source keys":"; ".join(keys)})
    return rows
