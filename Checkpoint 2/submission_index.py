"""Generate the human-readable index from the selected evidence manifest."""
from pathlib import Path
import json


def write_submission_index(base=None):
    base=Path(base or Path(__file__).resolve().parent)
    manifest=json.loads((base/"submission_manifest.json").read_text(encoding="utf-8"))
    baseline=manifest["baseline_run"]
    primary=manifest["primary_run"]
    repeat=manifest["baseline_repeat_run"]
    eps=manifest["seeded_tests"]["eps_plus_one"]
    lines=["# Checkpoint 2 submission index","",
           "This is the starting page for the selected submission evidence. It is generated from `submission_manifest.json`; the run folders below identify the exact report versions.","",
           "## Start here: baseline human audit","",
           f"**Costco baseline audit:** [human_audit.md]({baseline}/human_audit.md).", "",
           f"Review it alongside [the matching Costco report]({baseline}/verified_report_readable.md) and [its filing texts]({baseline}/COST/).", "",
           f"Selected baseline folder: `{baseline}`.","",
           "This worksheet is for the selected Costco report. Worksheets in other run folders belong to those other versions; they are not additional copies of this review task.","",
           "## Required seeded-error proof","",
           "The Checkpoint 2 checkout instruction requests the automated Verifier's marks on a deliberately corrupted report. The following files provide that proof:","",
           f"1. [Planted EPS report]({eps['seeded_run']}/report.md).",
           f"2. **[Verifier marks and corrected report]({eps['verified_run']}/verified_report_readable.md).**",
           f"3. [Detailed machine verification records]({eps['verified_run']}/verification.json).","",
           f"The planted annual diluted EPS is **${eps['reported']:.2f}**. Claim **{eps['claim_id']}** is marked **{eps['mark']}** and corrected to **${eps['corrected']:.2f}**, with the annual-filing evidence beside it. The genuine filing remains unchanged.","",
           "These automated marks are separate from the student's manual audit findings.","",
           "## Agent team and notebook","",
           "- [Executed notebook](Visa_Checkpoint_2.ipynb)",
           "- [Agent graph and orchestration](team.py)",
           "- [Independent verifier](verifier.py)",
           "- [Role instruction files](roles/)",
           "- [Local user interface](app.py)",
           "- [Setup and run commands](README.md)","",
           "## Selected report and audit files","",
           "| Purpose | Selected report | Matching human worksheet | How to use it |",
           "|---|---|---|---|",
           f"| Costco baseline | [Report]({baseline}/verified_report_readable.md) | **[Baseline audit]({baseline}/human_audit.md)** | Start the baseline review here. |",
           f"| Visa primary example | [Report]({primary}/verified_report_readable.md) | [Visa audit]({primary}/human_audit.md) | This worksheet checks Visa's report, not Costco's. Review it if including the Visa report in the hand-in. |",
           f"| Repeated Costco run | [Report]({repeat}/verified_report_readable.md) | Not an additional baseline assignment | Evidence that a second run uses the same node order and a new folder. |"]
    partner=manifest.get("partner_run")
    if partner:
        lines.append(f"| Partner-selected company | [Report]({partner}/verified_report_readable.md) | [Partner-company audit]({partner}/human_audit.md) | Complete the actual partner-company review and two partner checks. |")
    else:
        lines += ["| Partner-selected company | Not yet recorded | Created with that company's full run | Record the actual partner selection and run; the Visa example does not establish that selection. |"]
    lines += ["", "## Other selected verification tests","",
              "| Test | Planted report | Verifier marks |","|---|---|---|"]
    for name,test in manifest["seeded_tests"].items():
        lines.append(f"| {name} | [Report]({test['seeded_run']}/report.md) | [Marks and corrections]({test['verified_run']}/verified_report_readable.md) |")
    clean=manifest["clean_verification_run"]
    lines += [f"| Clean baseline | Original baseline report above | [Clean-report verification]({clean}/verified_report_readable.md) |","",
              "## Why there are other run folders","",
              "The lab requires separate saved runs rather than overwriting earlier evidence. The repository retains development attempts, repeated runs, planted-error copies and verification-only runs. Each full report run prepares its own blank human worksheet. That history explains the repeated filenames.","",
              "Use the selected links on this page. Choosing the newest timestamp or another file with the same basename can pair an audit with the wrong report. Older development worksheets do not all need to be filled in.","",
              "When new evidence is selected, the preparation command and notebook update this index. Keep human findings with the exact run/version reviewed. The detailed human workflow is [here](../Checkpoint_2_Human_Workflow.md).", ""]
    package=manifest.get("submission_package",{})
    entries=package.get("audits",[])
    if len(entries)==3 and all(manifest.get(e["selection_key"])==e["source_run"] for e in entries):
        front=["## Designated submission audits","",
               "**[Open the three clearly named submission folders](Submission/README.md).** These are the designated hand-in audits; the original run directories retain generation history.","",
               "| Purpose | Named audit | Matching report |","|---|---|---|"]
        for entry in entries:
            front.append(f"| {entry['label']} | [{entry['audit_file']}]({entry['audit']}) | [Report]({entry['report']}) |")
        front.append("")
        lines[4:4]=front
        # All selected-audit navigation points to the three designated copies.
        # Original run IDs remain in the text and manifest as provenance.
        for entry in entries:
            lines=[line.replace("("+entry["source_run"]+"/human_audit.md)","("+entry["audit"]+")")
                        .replace("("+entry["source_run"]+"/","("+entry["folder"]+"/") for line in lines]
        selected=next(e for e in entries if e["selection_key"]=="baseline_run")
        lines=[line.replace(f"Selected baseline folder: `{baseline}`.",
                            f"Designated baseline folder: `{selected['folder']}`. Original generation: `{baseline}`.") for line in lines]
    target=base/"SUBMISSION_INDEX.md"
    target.write_text("\n".join(lines),encoding="utf-8")
    return target
