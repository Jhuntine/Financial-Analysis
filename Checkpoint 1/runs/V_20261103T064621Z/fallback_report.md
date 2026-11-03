VISA INC. (NYSE: V); filings read: V 10-K 0001403161-25-000089; V 10-Q 0001403161-26-000104; V earnings 0001403161-26-000126; MA 10-K 0001141391-26-000013; PYPL 10-K 0001633917-26-000024
fallback; run time (UTC): 2026-11-03T07:35:07.016502+00:00; assistant synthesis using the saved filings; price retrieved directly from LSEG; four live model-provider calls were not run because no model API key was configured.

## Overview

**Research Analyst.** Visa connects participants in electronic payments through its transaction network. Its filing describes a "single connection point" and states "We do not issue cards"; this distinguishes the network's operating model from a card issuer's lending business. [K1, K2] The annual data below cover the fiscal year ended September 30, 2025. The quarterly update covers the three months ended September 30, 2026 and comes from the October earnings release. [K3, E1]

## Market Positioning and Growth Outlook

**Research Analyst.** The annual filing names "Mastercard" among the competing payment networks. [K4] The latest quarterly filing attributes volume support to "consumer spending" and "digital commerce" while identifying incentives as an offset to growth. [Q1] The annual MD&A also identifies "higher client incentives" as an offset to revenue growth. [K5] My inference is that transaction demand and incentive discipline should be assessed together; growth in payment activity alone does not establish stronger economics.

For the latest fiscal quarter, net revenue was **$12.139 billion**, and Class A GAAP diluted EPS was **$3.19**. The corresponding prior-year quarter revenue was **$10.724 billion**; nominal revenue growth calculated in Python is **13.19%**: `(12,139,000,000 / 10,724,000,000 - 1) * 100`. The release rounds this to 13%. [E1, E2] These are quarterly figures, rather than year-to-date or full-year results. The release also supplies non-GAAP EPS; the report uses the GAAP Class A measure. [E2, E3]

## Valuation Insights

**Financial Analyst.** The annual analysis uses the latest available 10-K, for fiscal 2025, even though a newer full-year earnings release is available. Revenue is the consolidated **net revenue after client incentives** shown in that filing. Operating margin is GAAP operating income divided by this net revenue; it includes reported litigation costs. [K3] It is not a gross margin on gross payment volume.

Debt-to-equity includes both the current and noncurrent carrying amounts of long-term debt. ROE uses beginning and ending reported stockholders' equity. Free cash flow deducts the filing's purchases of property, equipment and technology from operating cash flow; it is this desk's stated definition, not a substituted management-adjusted measure. Source tags and source lines are printed beside every input below.

The price input is LSEG's unadjusted daily close, **$401.86 on October 27, 2026**, immediately before the earnings 8-K's **16:05:22 Eastern** acceptance. [P1, F1] The required annual-filing P/E is **39.40x**, calculated as `401.86 / 10.20` using fiscal 2025 GAAP diluted EPS. **This is an annual-filing P/E with an older denominator; it is not a current trailing-twelve-month multiple.** The release separately reports newer annual Class A GAAP diluted EPS of **$12.32**, in a different column from the quarter. [E2] Do not mix the two bases or annualize a single quarter.

### Financial Analyst: annual statement facts

USD unless stated otherwise. Each row is from the selected annual filing.

| Metric | Value | Source, tag and period |
|---|---:|---|
| revenue (USD) | 40,000,000,000 | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| operating_income (USD) | 23,994,000,000 | V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| net_income (USD) | 20,058,000,000 | V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| diluted_eps (USD/shares) | 10.20 | V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| equity (USD) | 37,909,000,000 | V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2025-09-30; 0001403161-25-000089 |
| long_term_debt (USD) | 19,602,000,000 | V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; instant to 2025-09-30; 0001403161-25-000089 |
| current_debt (USD) | 5,569,000,000 | V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; instant to 2025-09-30; 0001403161-25-000089 |
| operating_cash_flow (USD) | 23,059,000,000 | V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| capex (USD) | 1,482,000,000 | V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| prior_revenue (USD) | 35,926,000,000 | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089 |
| prior_equity (USD) | 39,137,000,000 | V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2024-09-30; 0001403161-25-000089 |

### Calculated ratios

| Metric | Value | Arithmetic and source inputs |
|---|---:|---|
| revenue_growth | 11.34 % | (40,000,000,000 / 35,926,000,000 - 1) * 100 = 11.34; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089 |
| operating_margin | 59.99 % | 23,994,000,000 / 40,000,000,000 * 100 = 59.99; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| return_on_average_equity | 52.07 % | 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100 = 52.07; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2024-09-30; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2025-09-30; 0001403161-25-000089 |
| debt_to_equity | 0.66 x | (19,602,000,000 + 5,569,000,000) / 37,909,000,000 = 0.66; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; instant to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; instant to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2025-09-30; 0001403161-25-000089 |
| free_cash_flow | 21,577,000,000.00 USD | 23,059,000,000 - 1,482,000,000 = 21,577,000,000.00; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| price_earnings | 39.40 x | 401.86 / 10.20 = 39.40; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; supplied close 2026-10-27, LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted |

### Peer operating margins

GAAP operating income / reported consolidated revenue. Fiscal calendars and business mixes differ.

| Ticker | Fiscal end | Revenue (USD) | Operating income (USD) | Margin | Sources |
|---|---|---:|---:|---:|---|
| V | 2025-09-30 | 40,000,000,000 | 23,994,000,000 | 59.99% | 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| MA | 2025-12-31 | 32,791,000,000 | 18,897,000,000 | 57.63% | 18,897,000,000 / 32,791,000,000 * 100; MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013 |
| PYPL | 2025-12-31 | 33,172,000,000 | 6,065,000,000 | 18.28% | 6,065,000,000 / 33,172,000,000 * 100; PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024 |

### Latest earnings-release quarter

| Claim | Value | Source and period |
|---|---:|---|
| quarter_net_revenue | 12,139,000,000.00 USD | V/earnings_release.txt L212; First quarter column; three months ended 2026-09-30; source in millions; 0001403161-26-000126 |
| quarter_gaap_diluted_eps | 3.19 USD/shares | V/earnings_release.txt L250; First quarter column, GAAP diluted EPS; us-gaap:CommonClassAMember; 0001403161-26-000126 |
| Quarter revenue growth versus same quarter last year | 13.19% | (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; quarter ended 2026-09-30; 0001403161-26-000126 |

The peer calculation uses each issuer's latest annual filing as of the run date. The same GAAP formula is applied to reported consolidated revenue, but different fiscal calendars, revenue recognition and product mixes limit direct economic comparability. Mastercard is a network comparator; PayPal's wallet and processing model differs. Peer ratios do not establish a peer valuation multiple. PayPal's current-debt fact is dimensional; the unreviewed aggregate is left unavailable, and no PayPal debt-to-equity ratio is calculated. See `PYPL/unavailable_facts.json` and the debt note at `PYPL/10-K.txt` L2942-L2947.

## Future Developments and Strategic Recommendations

**Research Analyst.** Visa identifies "value-added services" as a strategic growth area. [K6] The release describes the proposed BioCatch acquisition as "subject to customary closing conditions"; completion remains conditional. [E4] The quarterly filing also discusses the UK interchange litigation and the finding that certain "interchange rates restrict competition". [Q2] These are reported developments, not a prediction of their outcome.

My inference is to monitor service adoption, incentive discipline, acquisition execution and legal costs before extrapolating historical margins. I would first revise the Financial Analyst's instructions if a draft mixed share classes or annual periods: the correct source tag can still produce a misleading valuation when its context is wrong.

## Investment Recommendation

**Investment Advisor. Hold.** The thesis combines a profitable payment-network model with continued demand for digital commerce, while incentive competition, legal matters and acquisition execution remain material considerations. The deciding number in this educational recommendation is the **39.40x annual-filing P/E** (`$401.86 / $10.20`; [P1] and fiscal 2025 Class A diluted EPS at `V/10-K.txt` L1590, tag `us-gaap:EarningsPerShareDiluted`, Class A context, accession `0001403161-25-000089`). I would retain Hold pending a valuation built on the newer earnings base and a completed human audit. The observed multiple alone does not establish fair value, and this report supplies no unsupported target price or earnings forecast. This judgment uses only the Research Analyst and Financial Analyst material above.

**Strategy Manager.** All five requested sections are present. Quantitative tables and formulas were generated in Python from saved filing evidence. This fallback is not represented as four completed provider API calls. Human marks and partner checks remain pending in `human_audit.md`.

### Source register

- K1: `V/10-K.txt` L153; proprietary transaction network and connection model.
- K2: `V/10-K.txt` L209; card issuance and credit risk distinction.
- K3: `V/10-K.txt` L1556-L1590; annual operating statement and Class A diluted EPS; individual balance-sheet and cash-flow references are in the tables.
- K4: `V/10-K.txt` L385; named payment-network competitors.
- K5: `V/10-K.txt` L839; annual MD&A revenue drivers and incentive offset.
- K6: `V/10-K.txt` L214; growth strategy.
- Annual filing, accession `0001403161-25-000089`: https://www.sec.gov/Archives/edgar/data/1403161/000140316125000089/v-20250930.htm
- Q1: `V/10-Q.txt` L1402; quarterly MD&A transaction-volume discussion.
- Q2: `V/10-Q.txt` L1180; UK interchange litigation.
- Quarterly filing, accession `0001403161-26-000104`: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000104/v-20260630.htm
- E1: `V/earnings_release.txt` L203-L205 and L212; period headers, units and consolidated net revenue.
- E2: `V/earnings_release.txt` L249-L250; diluted EPS heading and Class A row, quarter and full-year columns.
- E3: `V/earnings_release.txt` L24-L26; separately labelled GAAP and non-GAAP EPS.
- E4: `V/earnings_release.txt` L68; conditional BioCatch transaction.
- Earnings release, accession `0001403161-26-000126`, Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000126/q42026earningsrelease.htm
- F1: 8-K index, accession `0001403161-26-000126`: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000126/0001403161-26-000126-index.html
- P1: `market_input.json` and `market_data/lseg_close.csv`; LSEG Historical Pricing, instrument `V.N`, field `TRDPRC_1`, adjustments `unadjusted`, trade date `2026-10-27`. Retrieved `2026-11-03T07:29:18.573577+00:00`; the receipt records the exact request and SHA-256 hash of the saved observation. Documentation: https://developers.lseg.com/en/api-catalog/lseg-data-platform/lseg-data-library-for-python/tutorials/access-tutorials/tutorial-4-get_history

Human audit status: **not completed**. Automated extraction and calculations do not constitute the lab's human sign-off.

### Human sign-off

The [human sign-off learning section](human_signoff.md) answers Lab 3's three
questions from the provided Anthropic Open Source.pdf (pages 1-2) and original
README. The [human audit worksheet](human_audit.md) now follows Report Audit.pdf's
exact eleven core claims, then the other Financial Analyst numbers, template
and recommendation checks. The review record includes error/missing counts,
two partner checks, the reviewed version, reviewer/date and a decision.

This report remains an educational draft pending human verification. The
learning explanation is complete; human findings and approval are not claimed.
