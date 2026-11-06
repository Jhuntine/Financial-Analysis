"""Build the checkpoint 2 submission notebook; no conversational review content."""
from pathlib import Path
import textwrap
import nbformat as nbf
BASE=Path(__file__).resolve().parent
cells=[]
def md(s):cells.append(nbf.v4.new_markdown_cell(textwrap.dedent(s).strip()))
def code(s):cells.append(nbf.v4.new_code_cell(textwrap.dedent(s).strip()))

md("""
# Checkpoint 2 - Equity Research Agent Team

**FIN 67110 | LangGraph | Purdue GenAI Studio | Primary company: Visa**

A fixed graph runs seven filing-data tools, three analyst roles, a Strategy
Manager and an independent Verifier. Each analyst has one bounded revision slot.
The report preserves its source filings, calculation inputs, model handoffs,
original claims, verification marks and corrections.

The saved outputs contain actual provider responses. Run All executes the live
graph, including a new model call in the Verifier. Filing data and the dated
price replay the saved source snapshot so that the evidence periods stay fixed.
Every run saves a new evidence folder; previous runs remain available.
""")
md("""
## Configuration

Install from the repository root:

```powershell
python -m pip install -r "Checkpoint 2/requirements.txt"
```

The selected model is `gpt-oss:120b` on Purdue GenAI Studio. Run All requires
`PURDUE_GENAI_API_KEY` in the private root `.env`; reading the saved notebook
outputs requires no credentials. Source legend: K = annual filing, Q = quarterly filing,
E = earnings release, and L = one-based line in the saved text.
""")
code("""
from pathlib import Path
import sys
import json
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from IPython.display import display, Markdown
cwd=Path.cwd().resolve()
CHECKPOINT=next((p for p in (cwd,cwd/'Checkpoint 2') if (p/'submission_support.py').is_file()),None)
if CHECKPOINT is None:raise FileNotFoundError('Open from the repository root or Checkpoint 2 folder.')
sys.path.insert(0,str(CHECKPOINT))
from submission_support import load_manifest,run_selected_model,narrative_view,core_coverage
from team import read_json,core_groups
from verifier import extract_claims,citation,evaluate,digest,rounded
manifest=load_manifest()
PRIMARY=CHECKPOINT/manifest['primary_run']
BASELINE=CHECKPOINT/manifest['baseline_run']
REPEATED=CHECKPOINT/manifest['baseline_repeat_run']
pd.set_option('display.max_colwidth',100)
pd.set_option('display.max_columns',10)
print('Framework:',manifest['framework'])
print('Provider:',manifest['model_provider'],'| Model:',manifest['model'])
print('Execution: live model roles and mandatory live semantic verification')
""")
md("""
## Fixed graph and bounded revision

Code fixes node order, state boundaries, one revision per analyst and the final
Verifier. Research receives filing excerpts; Finance receives facts and computed
metrics; the Advisor receives only the two analyst outputs and their exposed
numbers. The Manager checks the five parts and three Insights. The Verifier
receives the compiled report and saved evidence, without analyst instructions.
""")
code("""
fig,ax=plt.subplots(figsize=(13,4.4))
ax.set(xlim=(-0.3,12.8),ylim=(0,4.4));ax.axis('off')
labels=['Seven data tools','Research Analyst','Financial Analyst','Investment Advisor','Strategy Manager',
        'Research repair slot','Financial repair slot','Advisor repair slot','Manager final check','Verifier']
positions=[(0,3),(2.6,3),(5.2,3),(7.8,3),(10.4,3),(10.4,0.7),(7.8,0.7),(5.2,0.7),(2.6,0.7),(0,0.7)]
for i,(label,(x,y)) in enumerate(zip(labels,positions)):
    color='#087f8c' if i==9 else '#c17c21' if 5<=i<=7 else '#17365d'
    ax.add_patch(FancyBboxPatch((x,y),2,0.9,boxstyle='round,pad=0.1',facecolor=color,edgecolor='none'))
    ax.text(x+1,y+0.45,label.replace(' repair ','\\nrepair ').replace(' final ','\\nfinal '),ha='center',va='center',color='white',fontsize=10)
    if i:
        px,py=positions[i-1]
        start,end=((px+1,py-0.05),(x+1,y+1.05)) if i==5 else (((px+2.12,py+0.45),(x-0.12,y+0.45)) if i<5 else ((px-0.12,py+0.45),(x+2.12,y+0.45)))
        ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color='#64748b',lw=1.8))
ax.text(6.3,2.25,'Fixed edges; unused revision slots make no model call',ha='center',fontsize=12,color='#334155')
fig.tight_layout();plt.show()
display(Markdown('[Saved graph]('+manifest['primary_run']+'/graph.mmd)'))
""")
md("""
## Primary company run

The tools resolve the ticker, select and identify filings, save line-addressable
text, extract same-period annual facts, calculate ratios, read the correct
quarterly columns and calculate peers on the same margin definition. A dated
market receipt records the price observation separately from the filings.
""")
code("""
result=run_selected_model(PRIMARY)
RUN=Path(result['run_dir'])
catalog=read_json(RUN/'catalog.json')
report=(RUN/'report.md').read_text(encoding='utf-8')
verification=read_json(RUN/'verification.json')
claims=extract_claims(report)
manifest['primary_run']=RUN.relative_to(CHECKPOINT).as_posix()
from verifier import write_json
write_json(CHECKPOINT/'submission_manifest.json',manifest)
write_json(CHECKPOINT/'latest_run.json',{'run_dir':manifest['primary_run']})
from submission_index import write_submission_index
write_submission_index(CHECKPOINT)
display(pd.DataFrame([{'Ticker':manifest['primary_ticker'],'Execution':result['summary']['mode'],
    'Manager approved':result['manager_approved'],'Verifier ran':result['summary']['verifier_ran'],
    'Numerical claims':verification['claim_count'],'Original findings':verification['errors'],
    'Unresolved':verification.get('unresolved_errors',0),'Semantic check':verification['semantic_status']}]))
display(pd.DataFrame({'Node':result['trace']}))
display(Markdown('[Selected live report]('+manifest['primary_run']+'/verified_report_readable.md) | '
                 '[Original report]('+manifest['primary_run']+'/report.md) | '
                 '[Provider call metadata]('+manifest['primary_run']+'/call_counts.json)'))
""")
md("""
## Core financial claims

Ratios use code-calculated inputs and explicit definitions. Annual and quarterly
periods remain separate. The annual-filing P/E uses the recorded close divided
by the selected annual GAAP diluted EPS; it is labelled separately from a current
TTM valuation. Peer fiscal periods and business mixes can differ.

Each source key resolves to exact filing lines, tags, periods and accessions in the run's `catalog.json`. The linked full report prints those citations beside each figure.
""")
code("""
coverage=pd.DataFrame(core_coverage(manifest['primary_ticker'],report,catalog,RUN))
assert len(coverage)==11 and coverage['Covered'].all()
display(coverage)
peer_rows=[]
for ticker in read_json(RUN/'configuration.json')['peers']+[manifest['primary_ticker']]:
    rev=catalog[ticker+'.fact.revenue'];op=catalog[ticker+'.fact.operating_income'];margin=catalog[ticker+'.ratio.operating_margin']
    peer_rows.append({'Ticker':ticker,'Fiscal end':rev['end'],'Reported revenue (USD)':rev['value'],
                     'GAAP operating income (USD)':op['value'],'GAAP operating margin (%)':margin['value'],
                     'Revenue label':rev['source_text'].split('|')[0]})
display(pd.DataFrame(peer_rows))
""")
md("""
## Five-part research report
""")
code("""
display(Markdown(narrative_view(report,catalog,RUN)))
insights=[c for c in claims if c['text'].startswith('Insight:')]
assert len(insights)==3
for claim in insights:
    display(Markdown('**'+claim['text']+'** '+f"{rounded(claim['value']):,.2f} {claim['unit']}"))
    display(Markdown('Source: '+citation(catalog[claim['source']],catalog).replace('|',' / ')))
""")
md("""
## Independent verification marks

Code checks saved facts and their XBRL contexts, source lines, fiscal-quarter
columns, units, price receipts and ratio arithmetic. The separate model check
examines whether the evidence supports each claim's period and definition.
Original marks and corrections remain saved. The Advisor's subjective thesis is
excluded; its deciding metric and separate Insight are checked.
""")
code("""
marks=pd.DataFrame(verification['marks'])
display(marks[['id','mark','reported','corrected','reason','semantic_status']])
assert verification['semantic_status']=='completed'
assert verification.get('unresolved_errors',0)==0
print('Verified source observations:',len(catalog))
print('Original marks:',marks['mark'].value_counts().to_dict())
""")
md("""
## Costco baseline and repeated-run evidence

The baseline uses its own annual filing and the release's 16-week quarter.
Quarterly total revenue includes membership fees; net sales and the full-year
columns are not substituted. Both selected baseline runs made actual provider
calls and saved separate evidence folders.
""")
code("""
baseline_summary=read_json(BASELINE/'summary.json');repeat_summary=read_json(REPEATED/'summary.json')
baseline_verification=read_json(BASELINE/'verification.json')
baseline_report=(BASELINE/'report.md').read_text(encoding='utf-8')
baseline_catalog=read_json(BASELINE/'catalog.json')
assert baseline_summary['mode']==repeat_summary['mode']=='live'
assert baseline_summary['manager_approved'] and repeat_summary['manager_approved']
assert read_json(BASELINE/'node_order.json')==read_json(REPEATED/'node_order.json')
assert BASELINE!=REPEATED
for folder in (BASELINE,REPEATED):assert all(n<=2 for n in read_json(folder/'call_counts.json').values())
display(pd.DataFrame([{'Run':p.name,**read_json(p/'call_counts.json')} for p in (BASELINE,REPEATED)]))
display(pd.DataFrame(core_coverage('COST',baseline_report,baseline_catalog,BASELINE)))
quarter=read_json(BASELINE/'quarter_observations.json')
print('Quarter duration:',quarter['quarter_duration'],'| End:',quarter['period_end'],'| Release:',quarter['release_date'])
display(Markdown('[Baseline report]('+manifest['baseline_run']+'/verified_report_readable.md) | '
                 '[Second baseline report]('+manifest['baseline_repeat_run']+'/verified_report_readable.md)'))
""")
md("""
## Seeded errors, invented growth and clean report

Each planted report is a separate copy. The saved filing evidence is unchanged.
Verify-only runs the Verifier without rerunning the analysts. The EPS test also
alters the report's quoted source line; the genuine filing remains unchanged.
""")
code("""
original_hash=digest(BASELINE/'report.md')
test_rows=[]
for name,record in manifest['seeded_tests'].items():
    checked=read_json(CHECKPOINT/record['verified_run']/'verification.json')
    assert read_json(CHECKPOINT/record['verified_run']/'node_order.json')==['Verifier']
    assert checked['semantic_status']=='completed'
    mark=next(m for m in checked['marks'] if m['id']==record['claim_id'])
    assert mark['mark'] in {'wrong','unsupported'} and mark['corrected'] is not None
    test_rows.append({'Test':name,'Reported':mark['reported'],'Mark':mark['mark'],'Correction':mark['corrected'],
                      'Semantic check':checked['semantic_status']})
    display(Markdown(name+': [planted report]('+record['seeded_run']+'/report.md) | '
                     '[saved live verifier marks]('+record['verified_run']+'/verified_report_readable.md)'))
clean=read_json(CHECKPOINT/manifest['clean_verification_run']/'verification.json')
assert clean['errors']==0 and digest(BASELINE/'report.md')==original_hash
assert clean['semantic_status']=='completed'
display(pd.DataFrame(test_rows))
print('Clean report:',clean['claim_count'],'numerical claims; no verification findings.')
""")
md("""
## General company interface

The same graph accepts another ticker, optional peers and a dated price. The
local page displays node progress and the verified report. The selected partner
run, when recorded in the manifest, uses the same interface and graph.

```powershell
python -m streamlit run "Checkpoint 2/app.py"
```

```powershell
python "Checkpoint 2/team.py" COST --peers WMT,TGT,BJ --as-of 2026-11-05 --market-provider wrds --price-date 2026-09-24 --model-provider purdue
```

Verify a saved run with `python "Checkpoint 2/team.py" --verify-only "Checkpoint 2/runs/RUN_FOLDER"`.
There is no verifier-skip option.
""")
code("""
if manifest.get('partner_run'):
    partner=CHECKPOINT/manifest['partner_run']
    display(pd.DataFrame([read_json(partner/'summary.json')]))
    display(Markdown('[Partner-company verified report]('+manifest['partner_run']+'/verified_report_readable.md)'))
else:
    print('Partner-selected run: not yet recorded in the submission manifest.')
checks=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(CHECKPOINT/'tests'),'-v'],
                      cwd=CHECKPOINT.parent,capture_output=True,text=True)
if checks.returncode:print(checks.stdout+checks.stderr)
assert checks.returncode==0
print('Regression suite:',checks.stderr.strip().splitlines()[-3:])
""")
md("""
## References

[Lab 4](../Instructions/Lab%204.pdf), [Lab 5](../Instructions/Lab%205.pdf),
[Week 3](../Instructions/Week%203.pdf), and [Report Audit](../Instructions/Report%20Audit.pdf).

[LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api),
[Purdue GenAI Studio API](https://docs.rcac.purdue.edu/services/genai/api/),
[official OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).
""")
nb=nbf.v4.new_notebook(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.13'}})
nbf.validate(nb);nbf.write(nb,BASE/'Visa_Checkpoint_2.ipynb')
print('Built',len(cells),'submission cells')
