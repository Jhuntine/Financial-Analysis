# Checkpoint 2 - equity research agent team

**Grading entry point: [Submission/README.md](Submission/README.md).** It links the three descriptively named audit files, their matching reports and the required seeded-error proof. The notebook's saved outputs can be read directly.

Open **[Visa_Checkpoint_2.ipynb](Visa_Checkpoint_2.ipynb)** and Run All. The notebook
contains the model, five-part report, financial evidence, fixed graph, recorded
live provider outputs, mandatory verification and planted-error results.

Run All executes new live model calls, including the mandatory semantic Verifier.
The saved notebook outputs can be read without credentials. The underlying filing
and price data replay their recorded snapshots to keep evidence periods fixed.
Each new run saves a separate evidence folder. Test fixtures are not used as the
submission model.

**Start with [SUBMISSION_INDEX.md](SUBMISSION_INDEX.md).** It links the selected
baseline audit, matching reports and the required seeded-error Verifier marks.
The machine-readable selection is [submission_manifest.json](submission_manifest.json).
It includes the Costco baseline and repeat, Visa, four planted-error checks and
a clean-report verification. A partner-selected run is attached separately when
that actual selection and full run have been completed.

## Required seeded-error evidence

Open [the selected seeded-error proof](SUBMISSION_INDEX.md#required-seeded-error-proof).
It links the planted EPS report, the Verifier's marks and corrected report, and
the detailed machine records. Human audit worksheets are listed separately in
that same index. Earlier development worksheets are retained as run history.

## Install and run

From the repository root:

```powershell
python -m pip install -r "Checkpoint 2/requirements.txt"
python -m streamlit run "Checkpoint 2/app.py"
```

After writing the three student personas, generate the selected submission evidence:

```powershell
python "Checkpoint 2/prepare_submission.py" --refresh
```

Preparation labels eight stages: Costco baseline, Costco repeat, four planted-error
checks, a clean-report check and Visa. Repeated node names belong to these separate
runs. If preparation stops, fix the saved findings and use `--resume` to retain
completed reports and exact matching live verification results. A failed report
is never accepted as a successful primary report; the submission index updates
only after all required preparation stages pass.

Attach the actual partner-selected report with `--partner-run "Checkpoint 2/runs/RUN_FOLDER"`.
The release must fall in the assignment's reporting month, which defaults to the
run's cutoff month. If the instructor's assigned month differs, add
`--reporting-month YYYY-MM`; this records that month without changing the report's
information cutoff. The notebook selects its primary example automatically and
does not require `--partner-run`.

The page accepts ticker, optional peers, cutoff and price settings, prints the
nodes as they start, and displays/downloads the verified report. Select new SEC
retrieval for a new company. New runs use live model calls and cannot skip the
Verifier.

Exact baseline command:

```powershell
python "Checkpoint 2/team.py" COST --peers WMT,TGT,BJ --as-of 2026-11-05 --market-provider wrds --price-date 2026-09-24 --model-provider purdue
```

Replace the ticker, peers and dates for another company. The price is optional.
A manual close uses `--price`, `--price-date` and `--price-source`; it remains
labelled as user supplied. A retrieved WRDS close uses the dated security ticker
and primary U.S. issue, with a saved CSV and SHA-256 receipt. LSEG is also
supported with `--market-provider lseg --ric ... --price-date ...` when its
Workspace connection is available. No unavailable price is replaced silently.

Verify only a saved run:

```powershell
python "Checkpoint 2/team.py" --verify-only "Checkpoint 2/runs/RUN_FOLDER"
```

Replace `RUN_FOLDER` with the actual saved folder. Verify-only runs the independent
Verifier and creates a fresh output folder; it does not rerun an analyst. There
is no code-only or verifier-skip CLI option.

## Model provider and credentials

Purdue GenAI Studio is configured through `PURDUE_GENAI_API_KEY` in the private
root `.env`; the default model is `gpt-oss:120b`. The backend uses the official
OpenAI Python SDK with Purdue's documented chat-completions endpoint and a
validated JSON schema. `--model-provider openai` uses `API_KEY` or
`OPENAI_API_KEY`, and `OPENAI_MODEL` defaults to `gpt-4o`.

SEC retrieval uses `SEC_USER_AGENT`. WRDS uses `WRDS_USERNAME` and
`WRDS_PASSWORD`; LSEG uses `LSEG_APP_KEY`. Reading saved notebook outputs needs no credentials; execution requires the
selected model provider key. Credentials are never copied into runs.

## Process and saved evidence

`team.py` fixes the LangGraph edges: tools, Research Analyst, Financial Analyst,
Investment Advisor, Strategy Manager, three bounded revision slots, Manager
final check and Verifier. No model selects the next node. Each role may make at
most two calls. Empty revision slots make no call. Manager rejection after the
allowed revision is recorded as failed review rather than a successful report.

Each model input is JSON containing task, permitted context and expected output.
`roles/` contains separate instruction files, copied into every run. The Advisor
receives only the two analyst outputs and their exposed numbers. The Verifier
receives only the compiled report, saved numerical evidence, filing excerpts and
code marks; it never receives the other roles' instructions.

`data_tools.py` extends the seven tools from Checkpoint 1 for fiscal-week release
headers, same-definition total revenue and GAAP diluted-EPS columns. It separates
Costco's total revenue from net sales and its 16-week quarter from the full year.
`market_adapter.py` supplies the corrected read-only WRDS lookup.

The compiled report contains explicit numerical claim records. The verifier checks
the actual report records, their quoted inputs, source contexts and arithmetic;
it also rejects numerical prose outside that source contract. Live semantic
verification checks whether a source supports the claim's meaning and period.
`verified_report_readable.md` is generated from the checked records. Its marks
table follows the original filings line, and corrections retain real evidence.

Every run uses a new ticker/UTC-time/unique-suffix folder. It retains raw SEC
responses, filing texts, facts, prices, graph, node inputs/outputs, original and
verified reports, detailed marks and an evidence hash manifest. Earlier runs are
never overwritten. Seeded tests change only report copies, including a false
EPS quotation; the genuine filing evidence remains unchanged.

## Validation and regeneration

```powershell
python -m unittest discover -s "Checkpoint 2/tests" -v
python "Checkpoint 2/prepare_submission.py" --refresh
```

The refresh command makes new live baseline/repeat/primary runs and new live
verification demonstrations, then updates the manifest. Use it after changing
student persona instructions. `--partner-run "Checkpoint 2/runs/RUN_FOLDER"`
attaches the actual partner-selected full run without replacing existing evidence.

The three analyst role files remain labelled reference instructions until the
student replaces them with their own six-part personas. Human factual marks,
partner selection/checks and final submission are separate requirements. The
complete human workflow is in
[Checkpoint_2_Human_Workflow.md](../Checkpoint_2_Human_Workflow.md).

## References

[Lab 4](../Instructions/Lab%204.pdf), [Lab 5](../Instructions/Lab%205.pdf),
[Week 3](../Instructions/Week%203.pdf), [Report Audit](../Instructions/Report%20Audit.pdf).

[LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api),
[Purdue GenAI Studio API](https://docs.rcac.purdue.edu/services/genai/api/),
[official OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).
