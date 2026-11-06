# Checkpoint 2: do these steps in order

You submit **one GitHub commit link** to Brightspace. You do not upload every report or worksheet individually.

Do steps 1-4 first to generate the reports you will submit. Then do the human reviews. Running the model again creates new folders, so avoid generating more reports while you are reviewing a selected version.

Open `C:\Users\josep\orca\Financial-Analysis` as your folder in VS Code. Edit Markdown files in the text editor; use the preview when you only want to read them. Keep using this same project folder for the commands below.

## 1. Finish your three persona files - EDIT

Open these three files:

1. [Research Analyst](Checkpoint%202/roles/research_analyst.md)
2. [Financial Analyst](Checkpoint%202/roles/financial_analyst.md)
3. [Investment Advisor](Checkpoint%202/roles/investment_advisor.md)

Write each persona yourself under the six parts already provided: identity, how it reads a company, permitted inputs, criteria it scores, what would change its view, and output. Require a sourced final Insight beyond the earnings headline. Keep company names out of these reusable instructions. Identify yourself and the date after completing your own writing.

Leave `strategy_manager.md` and `verifier.md` unchanged unless you are fixing a specific implementation problem. Lab 5 reserves the three analyst personas for your own writing.

**Done when:** the three analyst files contain your actual instructions rather than reference/starter text.

## 2. Regenerate the reports and error tests - RUN

Open PowerShell and run:

```powershell
Set-Location "C:\Users\josep\orca\Financial-Analysis"
python "Checkpoint 2/prepare_submission.py" --refresh
```

This generates a new Costco baseline, a second Costco run, the Visa example and the verification tests using your current personas. Wait for the success message saying the submission evidence was prepared. If it stops with an error, resolve that before reviewing or submitting the failed run.

The repeated agent names are expected: there are three full report runs (Costco, Costco repeat and Visa), four planted-error Verifier checks, and one clean-report Verifier check. The command labels these as eight stages. A revision-slot label can appear even when that slot needs no model call.

If a stage fails, keep the saved folders. After fixing the reported cause, resume without regenerating the completed stages:

```powershell
python "Checkpoint 2/prepare_submission.py" --resume
```

Resume checks that completed reports use your current role files and that reused verification evidence matches the exact source report. Use `--refresh` again when you deliberately want new reports after changing the personas.

This command updates the [Submission Index](Checkpoint%202/SUBMISSION_INDEX.md). **After refreshing, use the index links rather than old folder names from our conversation.**

If Python reports a missing package, install the project's requirements in the same Python environment and retry:

```powershell
python -m pip install -r "Checkpoint 2/requirements.txt"
```

## 3. Run and save the notebook - RUN AND SAVE

Open [Visa_Checkpoint_2.ipynb](Checkpoint%202/Visa_Checkpoint_2.ipynb), select your Python kernel, and choose **Run All**. Wait until every cell finishes without an error, then save the notebook.

This makes a live Visa run and saves its outputs in the notebook. It updates the index's selected Visa report. A working `PURDUE_GENAI_API_KEY` must be in your private root `.env`. Do not place keys in the notebook.

**Done when:** the notebook shows the report, verification results and passing checks, and has been saved with those outputs.

The `--partner-run` command belongs to step 4. You do not use it to register the notebook's Visa run. Running the notebook already selects its Visa example automatically.

## 4. Generate your partner's actual company report - RUN

Ask your partner to choose the company required by the assignment, including its reporting-month requirement. Record their name and choice.

Lab 5 says a U.S. company that "reported this month." Use the month your instructor means for this assignment. The **earnings-release date**, rather than the quarter-end date, must fall in that month. The information cutoff is a separate date: it controls which information the model may use and must be on or after the release. For example, Visa's October 27, 2026 release meets an October reporting-month requirement, but does not meet a November reporting-month requirement even if you run the model in November.

Start the page:

```powershell
python -m streamlit run "Checkpoint 2/app.py"
```

Your partner uses the page to enter their ticker, optional peers, cutoff and price settings. Select **New SEC retrieval** and the working model provider, then press **Run research team**. Wait for a completed report with Manager approval and completed semantic verification. Do not use another company's saved snapshot.

The page shows a run folder name next to **Saved run**. Copy that name. After the report finishes saving, return to PowerShell and press **Ctrl+C** to stop the page server. Then attach that actual run to the submission:

```powershell
python "Checkpoint 2/prepare_submission.py" --partner-run "Checkpoint 2/runs/ACTUAL_RUN_FOLDER"
```

Replace `ACTUAL_RUN_FOLDER` with the exact folder name shown on the page. The index will then include a partner-company row.

By default, attachment treats the run's information-cutoff month as the required reporting month. If your instructor specifies another assignment month, state that actual month explicitly. For example, **only if October 2026 is the assigned month**:

```powershell
python "Checkpoint 2/prepare_submission.py" --partner-run "Checkpoint 2/runs/ACTUAL_RUN_FOLDER" --reporting-month "2026-10"
```

This preserves the run's original dates. Do not choose a reporting month merely to make a rejected company pass. If the required month is November, your partner needs a company with a November release available by the chosen cutoff. A month mismatch does not require rerunning the notebook, the Costco baseline or the planted-error tests.

**Done when:** the partner-company report appears in the Submission Index. The Visa example does not establish that your partner selected a company.

## 5. Open the Submission Index - READ

Open [SUBMISSION_INDEX.md](Checkpoint%202/SUBMISSION_INDEX.md).

From now on, use only its selected links for your review:

- **Costco baseline:** the reference report and worksheet.
- **Visa primary example:** the report shown in your notebook and its worksheet.
- **Partner-selected company:** your partner's actual report and worksheet.

You do not need to fill the worksheets from every older development, repeat or test folder. The repeated Costco report supplies process evidence; it is not another baseline review assignment.

## 6. Review the Costco baseline - READ THE EVIDENCE, EDIT THE WORKSHEET

At the top of the index, open the selected Costco **human_audit.md**. Open the matching **verified_report_readable.md** beside it.

Work through the worksheet one row at a time:

1. Read the report's claim in **Report said**.
2. Read **Where** to identify the source file and line. `L719`, for example, means line 719 of the saved text.
3. Open that source and inspect the number, its column header, units, period and definition.
4. Type what you found into **Filing says (human)**.
5. Type your judgment into **Mark (human)**.
6. Continue to the next row.

In VS Code, open the cited text file, press **Ctrl+G**, and enter the line number without the `L`. Also read nearby headings so that you check the correct year or quarter and the stated units. In the worksheet's Markdown table, type into the empty cells between the `|` characters without removing the separators. For **Filing says**, record the value, units and period you actually verified; for **Mark**, enter your judgment from the list below.

Use these files as the worksheet directs:

| File in this selected run | What you do with it |
|---|---|
| `verified_report_readable.md` | Read the report you are checking. |
| `COST/10-K.txt` | Check annual claims and their source inputs. |
| `COST/earnings_release.txt` | Check quarterly claims, GAAP EPS and the quarter/full-year column distinction. |
| `COST/10-Q.txt` | Check cited quarterly business developments and disclosures. |
| Peer folders such as `WMT/10-K.txt` | Check each peer against its own filing. |
| `market_input.json` and its price CSV | Check the price, instrument, date and source used for valuation. Read these files; do not edit them. |
| `human_audit.md` | Fill your findings, marks, counts, name, date and review decision. |

For Costco, distinguish total revenue from net sales and the 16-week quarter from the full year. For ratios, verify the quoted inputs and redo the arithmetic. You can use a calculator.

Use these marks:

- **Correct:** right value, period, units and definition; arithmetic holds.
- **Wrong:** the same claim exists for that period and definition, but its value differs.
- **Unsupported:** the number lacks support or represents another period or definition.
- **Missing:** a required claim is absent. Adjusted EPS alone does not satisfy required GAAP EPS.
- **Not in filings:** neither the filings nor the report supplies the figure; an invented report figure is unsupported instead.

Check the eleven core claims, the other numerical claims, the three Insights, and the template/recommendation rows. Record **wrong + unsupported** as errors and count **missing** separately. Do not assume the human counts are zero merely because the automated checks passed.

If you find an error, record it and the needed correction. Have the problem corrected and review the new selected version before approving it. Preserve the original findings.

**Done when:** the selected Costco worksheet has your actual findings, marks, counts and reviewer details, with a decision based on the review.

## 7. Review the other selected reports - REPEAT THE SAME CHECK

Use the index to open the Visa report's matching worksheet and your partner-company report's matching worksheet. Apply the same row-by-row process from step 6 to the reports you include in the hand-in.

Do not use Costco's worksheet to review Visa or another company. Each completed worksheet stays in the same folder as the exact report it checks. Older historical worksheets can remain blank.

## 8. Record your partner's checks - EDIT THE SELECTED PARTNER REPORT

Your partner independently checks two core claims against their company's filings. Record their actual findings in that run's `human_audit.md` partner fields. Have them open at least one Insight citation and verify its evidence as well.

For the requirement that the two marks appear at the top of the report, add a short human-review note near the top of that run's **verified_report_readable.md**, preserving the first filings line and the automated Verifier table. Include the partner's name/date, the two claim names, their actual marks and filing references.

You may add human review notes to this readable report. Keep its financial claims unchanged. Leave the machine originals, `report.md` and `verified_report.md`, unchanged. This does not require making another report copy.

**Done when:** the partner's two checks are recorded in the worksheet and visible near the top of the selected readable report.

## 9. Inspect the seeded-error proof - READ ONLY

In the index, open **Required seeded-error proof**:

1. Read the planted EPS report.
2. Read the linked **Verifier marks and corrected report**.
3. Open the cited annual-filing line and confirm that the Verifier restored the filing's value.

The deliberately wrong EPS and its automatic **wrong** mark are expected in this test. They demonstrate that the Verifier caught the planted error. Do not edit the planted report or its machine marks to make the test look clean.

Review the other test results and clean-report check linked from the index. Ask your partner to check the seeded EPS result against the actual filing line.

**Done when:** the saved test proof is present and you can explain why its mark and correction are justified. The automated proof does not replace your manual audit.

## 10. Commit, push and submit one link - SUBMIT

Before uploading, confirm that the personas are your own, the notebook is saved with outputs, the selected worksheets and partner notes are complete, and the index points to the intended reports. Complete the classroom/team requirements from the lab as well.

In PowerShell, stage the work:

```powershell
git add .
git diff --cached --name-only -- .env
```

The second command must print nothing. Review the staged files; keep your private `.env` out of the commit.

Then save a commit and upload it:

```powershell
git commit -m "Complete checkpoint 2 agent team and seeded-error verification"
git push origin main
```

After the push succeeds, create and copy the exact link:

```powershell
$submissionCommit = (git rev-parse HEAD).Trim()
$submissionLink = "https://github.com/Jhuntine/Financial-Analysis/commit/$submissionCommit"
$submissionLink
$submissionLink | Set-Clipboard
```

Open the printed URL and confirm that the committed repository contains the notebook and Submission Index, with working links to the seeded-error marks. Ensure your instructor can access the repository.

Paste that URL into Brightspace > Checkpoint 2, submit it by the course deadline, and check the submission confirmation. If you make later changes, create and push a new commit and update the submitted link.

## Everything else

Leave the implementation files (`team.py`, `verifier.py`, `data_tools.py` and related code), generated JSON/CSV evidence, raw caches and historical run folders as supplied unless fixing a specific problem. They are included in the repository; you do not manually complete each one.

This procedure follows [Lab 4](Instructions/Lab%204.pdf), [Lab 5](Instructions/Lab%205.pdf), [Week 3](Instructions/Week%203.pdf) and [Report Audit](Instructions/Report%20Audit.pdf). Your instructor's actual grading instructions and deadline remain authoritative.
