"""Create live submission evidence and a portable manifest; never fill human marks."""
import argparse
from datetime import date
from pathlib import Path

from team import (BASE,previous_config,read_json,write_json,run_team,seed_run,verify_only)
from verifier import check_evidence,digest,extract_claims


class PreparationError(ValueError):
    """A completed stage failed the submission checks; retain its evidence."""


def relative(path):
    return Path(path).resolve().relative_to(BASE).as_posix()


def validate_live(folder):
    folder=Path(folder)
    summary=read_json(folder/"summary.json")
    verification=read_json(folder/"verification.json")
    check_evidence(folder)
    problems=[]
    if summary.get("mode")!="live":problems.append("run did not use live models")
    if not summary["manager_approved"]:
        review=read_json(folder/"manager_review.json")
        problems.extend(f"{f['role']}: {f['issue']}" for f in review["failures"])
        if not review["failures"]:problems.append("Manager did not approve")
    if verification["semantic_status"]!="completed":problems.append("semantic verification incomplete")
    if verification.get("unresolved_errors",verification["errors"]):
        problems.extend(f"{m['id']} ({m['mark']}): {m['reason']}" for m in verification["marks"]
                        if m["mark"]!="correct" and m.get("corrected") is None)
    if problems:
        raise PreparationError(f"Run needs revision: {folder.name}\n"+"\n".join(dict.fromkeys(problems)))
    return summary,verification


def require_current_roles(folder):
    for role in (BASE/"roles").glob("*.md"):
        saved=Path(folder)/"roles"/role.name
        if not saved.exists() or digest(saved)!=digest(role):
            raise PreparationError("Role instructions changed since "+Path(folder).name+
                                   ". Use --refresh to generate reports with the current personas.")


def completed_verification(source):
    """Resume only a genuine completed check of this exact report and evidence."""
    source=Path(source).resolve()
    for folder in sorted((BASE/"runs").glob("*_verify_only"),reverse=True):
        try:
            summary=read_json(folder/"summary.json")
            if summary.get("mode")!="verify_only" or Path(summary["source_run"]).resolve()!=source:
                continue
            result=read_json(folder/"verification.json")
            if result["semantic_status"]!="completed":continue
            if digest(folder/"report.md")!=digest(source/"report.md"):continue
            if digest(folder/"catalog.json")!=digest(source/"catalog.json"):continue
            if read_json(folder/"evidence_manifest.json")!=read_json(source/"evidence_manifest.json"):continue
            check_evidence(folder)
            integrity=read_json(folder/"report_integrity.json")
            if any(digest(folder/name)!=integrity[key] for name,key in (
                ("report.md","original_report_sha256"),("verified_report.md","verified_report_sha256"),
                ("catalog.json","catalog_sha256"))):continue
            saved_role=folder/"roles/verifier.md"
            if not saved_role.exists() or digest(saved_role)!=digest(BASE/"roles/verifier.md"):continue
            outputs=list((folder/"nodes").glob("verifier*_output.json"))
            if not outputs or any(read_json(p).get("metadata",{}).get("mode")!="live" or
                                  not read_json(p).get("metadata",{}).get("response_id") for p in outputs):continue
            return {"run_dir":str(folder),**result}
        except (OSError,ValueError,KeyError,TypeError):
            # Incomplete attempts remain in history and are never selected.
            continue
    return None


def completed_seed(baseline,mutation):
    baseline=Path(baseline)
    for seeded in sorted((BASE/"runs").glob("*_"+mutation),reverse=True):
        try:
            change=read_json(seeded/"mutation.json")
            if (change["kind"]!=mutation or change["source_run"]!=baseline.name or
                change["source_report_sha256"]!=digest(baseline/"report.md")):continue
            checked=completed_verification(seeded)
            if checked:return seeded,checked
        except (OSError,ValueError,KeyError,TypeError):
            continue
    return None


def config_from_snapshot(folder):
    return {**read_json(Path(folder)/"configuration.json"),"source_run":str(Path(folder).resolve()),
            "offline":True,"model_provider":"purdue","model":"gpt-oss:120b"}


def attach_partner(manifest,partner,reporting_month=None):
    partner=Path(partner).resolve()
    validate_live(partner)
    quarter=read_json(partner/"quarter_observations.json")
    config=read_json(partner/"run_config.json")
    required=reporting_month if reporting_month is not None else config["as_of"][:7]
    try:
        if len(required)!=7 or date.fromisoformat(required+"-01").strftime("%Y-%m")!=required:
            raise ValueError
    except (TypeError,ValueError):
        raise PreparationError("Reporting month must use YYYY-MM, for example 2026-11.")
    if quarter["release_date"][:7]!=required:
        raise PreparationError(
            f"Partner report was not attached: {config['ticker']} released earnings on {quarter['release_date']}, "
            f"but the required reporting month is {required}.\n"
            f"This run's information cutoff is {config['as_of']}. "
            +("The reporting month defaulted to that cutoff month. " if reporting_month is None else "")
            +"Lab 5 requires your partner's choice to have reported in the assignment month. "
            "Use a company that meets that requirement. If your instructor means a different month, "
            "specify that actual month with --reporting-month YYYY-MM; keep the run's dates unchanged.")
    manifest["partner_run"]=relative(partner)
    manifest["partner_reporting_month"]=required


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument("--refresh",action="store_true",help="Make new live baseline, repeat and primary-company runs after role edits")
    mode.add_argument("--resume",action="store_true",help="Reuse completed stages and retry an unsuccessful primary run (the default)")
    parser.add_argument("--partner-run",type=Path,help="Attach the actual partner-selected run produced from the page")
    parser.add_argument("--reporting-month",help="Assignment's required earnings-release month, YYYY-MM; defaults to the partner run's cutoff month")
    args=parser.parse_args()
    if args.reporting_month and not args.partner_run:
        parser.error("--reporting-month applies only with --partner-run")
    if args.partner_run and not args.refresh and (BASE/"submission_manifest.json").exists():
        manifest=read_json(BASE/"submission_manifest.json")
        attach_partner(manifest,args.partner_run,args.reporting_month)
        write_json(BASE/"submission_manifest.json",manifest)
        from submission_index import write_submission_index
        write_submission_index(BASE)
        print("Attached the selected partner run; existing live evidence preserved.")
        return
    data=BASE/read_json(BASE/"costco_data_pointer.json")["run_dir"]
    print("[1/8] Costco baseline"+(" - new run" if args.refresh else " - resume if completed"),flush=True)
    if args.refresh or not (BASE/"costco_live_pointer.json").exists():
        baseline=Path(run_team(config_from_snapshot(data))["run_dir"])
    else:baseline=BASE/read_json(BASE/"costco_live_pointer.json")["run_dir"]
    validate_live(baseline)
    require_current_roles(baseline)
    write_json(BASE/"costco_live_pointer.json",{"run_dir":relative(baseline)})
    print("Accepted:",baseline.name,flush=True)
    print("[2/8] Costco repeat - same fixed graph, separate report",flush=True)
    if (BASE/"costco_repeat_pointer.json").exists() and not args.refresh:
        saved=read_json(BASE/"costco_repeat_pointer.json")
        repeat=BASE/saved["run_dir"] if saved.get("baseline_source")==relative(baseline) else None
    else:repeat=None
    if repeat is None:
        repeat=Path(run_team(config_from_snapshot(data))["run_dir"])
    validate_live(repeat)
    require_current_roles(repeat)
    write_json(BASE/"costco_repeat_pointer.json",{"run_dir":relative(repeat),"baseline_source":relative(baseline)})
    print("Accepted:",repeat.name,flush=True)
    if read_json(baseline/"node_order.json")!=read_json(repeat/"node_order.json"):
        raise ValueError("Repeated baseline changed node order.")
    baseline_hash=digest(baseline/"report.md")
    demonstrations={}
    for step,mutation in enumerate(("eps_plus_one","growth_plus_four","wrong_quarter","ambiguous_roe"),3):
        print(f"[{step}/8] Verification demonstration: {mutation}",flush=True)
        saved=completed_seed(baseline,mutation) if not args.refresh else None
        if saved:
            seeded,checked=saved
            print("Reusing completed verification:",Path(checked["run_dir"]).name,flush=True)
        else:
            seeded=seed_run(baseline,mutation)
            checked=verify_only(seeded)
        changed=read_json(seeded/"mutation.json")["claim_id"]
        verdict=next(m for m in checked["marks"] if m["id"]==changed)
        if verdict["mark"] not in {"wrong","unsupported"} or verdict["corrected"] is None:
            raise ValueError("Verifier missed a planted error.")
        demonstrations[mutation]={"seeded_run":relative(seeded),"verified_run":relative(checked["run_dir"]),
                                  "claim_id":changed,"reported":verdict["reported"],"mark":verdict["mark"],
                                  "corrected":verdict["corrected"],"baseline_report_sha256":baseline_hash}
    print("[7/8] Clean baseline - check for false positives",flush=True)
    clean=completed_verification(baseline) if not args.refresh else None
    if clean:print("Reusing completed verification:",Path(clean["run_dir"]).name,flush=True)
    else:clean=verify_only(baseline)
    if clean["errors"]!=0:raise ValueError("Clean baseline produced a false-positive verification finding.")
    if digest(baseline/"report.md")!=baseline_hash:raise ValueError("Original baseline was modified.")
    print("[8/8] Visa primary report",flush=True)
    primary=None
    if not args.refresh and (BASE/"visa_live_pointer.json").exists():
        candidate=BASE/read_json(BASE/"visa_live_pointer.json")["run_dir"]
        try:
            validate_live(candidate)
            require_current_roles(candidate)
            primary=candidate
            print("Reusing completed live run:",primary.name,flush=True)
        except PreparationError as exc:
            print(str(exc)+"\nStarting a new Visa run; earlier files are retained.",flush=True)
    if primary is None:
        primary=Path(run_team({**previous_config(),"model_provider":"purdue","model":"gpt-oss:120b"})["run_dir"])
    validate_live(primary)
    write_json(BASE/"visa_live_pointer.json",{"run_dir":relative(primary)})
    manifest={"schema_version":2,"framework":"LangGraph","model_provider":"Purdue GenAI Studio","model":"gpt-oss:120b",
              "primary_ticker":"V","primary_run":relative(primary),"baseline_ticker":"COST","baseline_run":relative(baseline),
              "baseline_repeat_run":relative(repeat),"clean_verification_run":relative(clean["run_dir"]),
              "seeded_tests":demonstrations,"partner_run":None,
              "human_personas":"pending student writing","human_audit":"pending","partner_checks":"pending"}
    if args.partner_run:
        attach_partner(manifest,args.partner_run,args.reporting_month)
    manifest["source_hashes"]={p.relative_to(BASE).as_posix():digest(p) for p in [
        BASE/"team.py",BASE/"verifier.py",BASE/"data_tools.py",BASE/"market_adapter.py",BASE/"app.py",
        BASE/"submission_support.py",BASE/"prepare_submission.py",BASE/"build_notebook.py",
        BASE/"human_review.py",
        BASE/"submission_index.py",
        *sorted((BASE/"roles").glob("*.md"))]}
    write_json(BASE/"submission_manifest.json",manifest)
    from submission_index import write_submission_index
    write_submission_index(BASE)
    write_json(BASE/"latest_run.json",{"run_dir":relative(primary)})
    print("Submission evidence prepared:",BASE/"submission_manifest.json",flush=True)


if __name__=="__main__":
    try:
        main()
    except PreparationError as exc:
        raise SystemExit(str(exc)+"\nNo submission manifest or index was updated by this unsuccessful command. "
                         "Resume report preparation with --resume after fixing report findings; "
                         "a partner-date mismatch requires a qualifying partner report or the correct assignment month.")
