# Checkpoint 1 - Visa

Open [Visa_Checkpoint_1.ipynb](Visa_Checkpoint_1.ipynb) in Jupyter or VS Code and
run all cells. It includes saved outputs and replays the public SEC snapshot
offline by default. The company, peers, cutoff, instrument and price date are notebook
parameters. [desk.py](desk.py) implements the reusable seven steps and four roles.

The recorded run is [runs/V_20261103T064621Z](runs/V_20261103T064621Z):

- [Five-part fallback report](runs/V_20261103T064621Z/fallback_report.md)
- [Human sign-off learning answers and review record](runs/V_20261103T064621Z/human_signoff.md)
- [Human audit worksheet following the supplied checklist](runs/V_20261103T064621Z/human_audit.md)
- `snapshot.json`, individual facts and ratios, tag-selection logs, quarterly
  source observations, price provenance, and peer results
- Saved 10-K, 10-Q and Exhibit 99.1 text, plus peers' annual texts
- `raw/`: compressed public SEC responses with retrieval times and SHA-256 hashes
- `market_input.json` and `market_data/lseg_close.csv`: the actual LSEG observation,
  request parameters, retrieval time and a SHA-256 hash for offline verification

As of November 3, 2026, the selected Visa 10-K covers fiscal 2025, the 10-Q
covers June 2026, and the October 27 release covers the September 2026 quarter
and fiscal year. The notebook keeps those periods and the Class A EPS context
separate. Peers are Mastercard and PayPal; both report annual periods ending
December 2025. All margins use reported GAAP operating income / consolidated
reported revenue, with fiscal-calendar and business-model differences noted.

Install dependencies from the repository root:

```powershell
python -m pip install -r "Checkpoint 1/requirements.txt"
```

To fetch a new snapshot:

```powershell
python "Checkpoint 1/desk.py" V --peers MA,PYPL --market-provider lseg --ric V.N --price-date 2026-10-27 --as-of 2026-11-03
```

The price was retrieved directly through LSEG Historical Pricing: `V.N`,
`TRDPRC_1`, daily, `adjustments="unadjusted"`, October 27, 2026. LSEG returned
**$401.86**. Workspace must be running and signed in for a new request, with
`LSEG_APP_KEY` loaded from the private `.env`. The default notebook replays and
verifies the recorded LSEG receipt, so another live connection is not required.
The annual-filing P/E uses fiscal 2025 Class A diluted EPS and is labelled accordingly.

For WRDS instead, use `--market-provider wrds` and omit `--ric`. This retrieves
the primary U.S. issue's daily `comp.secd.prccd` through the WRDS PostgreSQL
service using `WRDS_USERNAME` and `WRDS_PASSWORD` from `.env`. That route needs
database network access and the relevant subscription. Neither provider silently
falls back to another public quote or relabels a manually supplied price.

To replay the exact saved run:

```powershell
python "Checkpoint 1/desk.py" V --peers MA,PYPL --market-provider lseg --ric V.N --price-date 2026-10-27 --as-of 2026-11-03 --offline --run-dir "Checkpoint 1/runs/V_20261103T064621Z"
```

Append `--step 4` to print only that step (its prerequisites are computed
silently). Change ticker, peers, cutoff and price together for another company.
An offline run can only use URLs already recorded in that run.

For the live four-role workflow, add `API_KEY` or `OPENAI_API_KEY` to the private
repository-root `.env`, optionally set `OPENAI_MODEL` (default `gpt-4o`), and
append `--roles` to the full run command. In the notebook, set
`RUN_MODEL_ROLES = True`. Each role uses a separate official-SDK call, receives a
JSON task/context/output contract, and saves its hand-offs. The manager can send
a failing part back once; a second failed review prevents final compilation.
The advisor receives only the two analysts' outputs and their computed tables.

No model-provider API key was present when this artifact was created, so the
saved report is explicitly labelled as the **course-permitted fallback**. Live
provider calls have not been run. The SDK orchestration is checked with mocked
responses; the SEC extraction and notebook are checked on the saved real data.

Run the regression checks:

```powershell
python -m unittest discover -s "Checkpoint 1/tests" -v
```

The notebook's human sign-off section answers all three Lab 3 learning questions
using [Anthropic Open Source.pdf](../Instructions/Anthropic%20Open%20Source.pdf),
pages 1-2, and [Anthropic's original README](https://github.com/anthropics/financial-services).
It explains professional review, the boundary on consequential actions, and the
difference between the Strategy Manager's structural review and human approval.

The audit worksheet follows [Report Audit.pdf](../Instructions/Report%20Audit.pdf),
pages 1-3: the exact eleven core claims in order, all other Financial Analyst
numbers, and the template/recommendation rows. It includes the five marking
categories, separate error/missing counts, two partner checks and a review record.
The lab reserves the findings, marks and signature for humans; these remain
blank. Complete them, review and commit the deliverables, push, and submit a
**commit permalink** through Brightspace.

The repository `.gitignore` excludes `.env`, environment overrides, Python
bytecode and Jupyter checkpoints; `.env.example` contains placeholders only.
