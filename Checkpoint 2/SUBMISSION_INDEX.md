# Checkpoint 2 submission index

This is the starting page for the selected submission evidence. It is generated from `submission_manifest.json`; the run folders below identify the exact report versions.

## Designated submission audits

**[Open the three clearly named submission folders](Submission/README.md).** These are the designated hand-in audits; the original run directories retain generation history.

| Purpose | Named audit | Matching report |
|---|---|---|
| Costco baseline | [COSTCO_Baseline_Human_Audit.md](Submission/01_COSTCO_Baseline/COSTCO_Baseline_Human_Audit.md) | [Report](Submission/01_COSTCO_Baseline/verified_report_readable.md) |
| Visa notebook example | [VISA_Notebook_Human_Audit.md](Submission/02_VISA_Notebook_Example/VISA_Notebook_Human_Audit.md) | [Report](Submission/02_VISA_Notebook_Example/verified_report_readable.md) |
| Visa partner selection | [VISA_Partner_Human_Audit.md](Submission/03_VISA_Partner_Selected_Company/VISA_Partner_Human_Audit.md) | [Report](Submission/03_VISA_Partner_Selected_Company/verified_report_readable.md) |

## Start here: baseline human audit

**Costco baseline audit:** [human_audit.md](Submission/01_COSTCO_Baseline/COSTCO_Baseline_Human_Audit.md).

Review it alongside [the matching Costco report](Submission/01_COSTCO_Baseline/verified_report_readable.md) and [its filing texts](Submission/01_COSTCO_Baseline/COST/).

Designated baseline folder: `Submission/01_COSTCO_Baseline`. Original generation: `runs/COST_20261105T231700361085Z_ec30bc`.

This worksheet is for the selected Costco report. Worksheets in other run folders belong to those other versions; they are not additional copies of this review task.

## Required seeded-error proof

The Checkpoint 2 checkout instruction requests the automated Verifier's marks on a deliberately corrupted report. The following files provide that proof:

1. [Planted EPS report](runs/COST_20261105T232111498131Z_7d807f_eps_plus_one/report.md).
2. **[Verifier marks and corrected report](runs/COST_20261105T232111512941Z_540bc4_verify_only/verified_report_readable.md).**
3. [Detailed machine verification records](runs/COST_20261105T232111512941Z_540bc4_verify_only/verification.json).

The planted annual diluted EPS is **$21.76**. Claim **C011** is marked **wrong** and corrected to **$20.76**, with the annual-filing evidence beside it. The genuine filing remains unchanged.

These automated marks are separate from the student's manual audit findings.

## Agent team and notebook

- [Executed notebook](Visa_Checkpoint_2.ipynb)
- [Agent graph and orchestration](team.py)
- [Independent verifier](verifier.py)
- [Role instruction files](roles/)
- [Local user interface](app.py)
- [Setup and run commands](README.md)

## Selected report and audit files

| Purpose | Selected report | Matching human worksheet | How to use it |
|---|---|---|---|
| Costco baseline | [Report](Submission/01_COSTCO_Baseline/verified_report_readable.md) | **[Baseline audit](Submission/01_COSTCO_Baseline/COSTCO_Baseline_Human_Audit.md)** | Start the baseline review here. |
| Visa primary example | [Report](Submission/02_VISA_Notebook_Example/verified_report_readable.md) | [Visa audit](Submission/02_VISA_Notebook_Example/VISA_Notebook_Human_Audit.md) | This worksheet checks Visa's report, not Costco's. Review it if including the Visa report in the hand-in. |
| Repeated Costco run | [Report](runs/COST_20261105T231903165410Z_096a9f/verified_report_readable.md) | Not an additional baseline assignment | Evidence that a second run uses the same node order and a new folder. |
| Partner-selected company | [Report](Submission/03_VISA_Partner_Selected_Company/verified_report_readable.md) | [Partner-company audit](Submission/03_VISA_Partner_Selected_Company/VISA_Partner_Human_Audit.md) | Complete the actual partner-company review and two partner checks. |

## Other selected verification tests

| Test | Planted report | Verifier marks |
|---|---|---|
| eps_plus_one | [Report](runs/COST_20261105T232111498131Z_7d807f_eps_plus_one/report.md) | [Marks and corrections](runs/COST_20261105T232111512941Z_540bc4_verify_only/verified_report_readable.md) |
| growth_plus_four | [Report](runs/COST_20261105T232203334402Z_3c1381_growth_plus_four/report.md) | [Marks and corrections](runs/COST_20261105T232203351372Z_b63b6a_verify_only/verified_report_readable.md) |
| wrong_quarter | [Report](runs/COST_20261105T232247531759Z_7bc07b_wrong_quarter/report.md) | [Marks and corrections](runs/COST_20261105T232247545988Z_580401_verify_only/verified_report_readable.md) |
| ambiguous_roe | [Report](runs/COST_20261105T232327063931Z_cfb63a_ambiguous_roe/report.md) | [Marks and corrections](runs/COST_20261105T232327080872Z_12b533_verify_only/verified_report_readable.md) |
| Clean baseline | Original baseline report above | [Clean-report verification](runs/COST_20261105T232410133110Z_582adc_verify_only/verified_report_readable.md) |

## Why there are other run folders

The lab requires separate saved runs rather than overwriting earlier evidence. The repository retains development attempts, repeated runs, planted-error copies and verification-only runs. Each full report run prepares its own blank human worksheet. That history explains the repeated filenames.

Use the selected links on this page. Choosing the newest timestamp or another file with the same basename can pair an audit with the wrong report. Older development worksheets do not all need to be filled in.

When new evidence is selected, the preparation command and notebook update this index. Keep human findings with the exact run/version reviewed. The detailed human workflow is [here](../Checkpoint_2_Human_Workflow.md).
