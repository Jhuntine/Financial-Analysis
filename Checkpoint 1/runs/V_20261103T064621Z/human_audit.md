# Checkpoint 1 human audit - VISA INC.

Source: [instructor's Report Audit.pdf](../../../Instructions/Report%20Audit.pdf), pages 1-3. The eleven categories and their order below follow that file.

**Errors (wrong + unsupported): not yet counted. Missing claims: not yet counted.**
**Human auditor / date:** ____________________
**Report reviewed / version:** ____________________
**Partner's first claim / mark:** ____________________
**Partner's second claim / mark:** ____________________

The Report said and Where columns are prepared from the draft's data. A human must fill Filing says and Mark after opening the actual filing and checking period, units, share class and definition. A prepared source reference is not an audit mark.

- **Correct:** the rounded number agrees with the filing; computed inputs are present and the arithmetic holds.
- **Wrong:** the same period and definition appear in the filing, but the report's value differs. Record the filing's value.
- **Unsupported:** the supplied figure is absent, guessed, or represents a different period or definition.
- **Missing:** the required claim is absent. Adjusted EPS alone does not satisfy either required GAAP diluted EPS claim.
- **Not in filings:** neither the filings nor the report gives the figure. This contributes to neither count; an invented figure is unsupported.

Count wrong plus unsupported as errors and missing separately. For any non-correct claim, name the role and correction. Review the exact filings listed on the report's first line.

## The eleven core claims

| # | Claim | Report said | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|---|
| 1 | Total revenue, latest fiscal year | 40,000,000,000 USD | | | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| 2 | Revenue growth versus the prior year | 11.34% | | | (40,000,000,000 / 35,926,000,000 - 1) * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089 |
| 3 | Operating income and operating margin | 23,994,000,000 USD; 59.99% | | | 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| 4 | Net income attributable to the company | 20,058,000,000 USD | | | V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| 5 | Diluted earnings per share, GAAP | 10.20 USD/shares; listed Class A | | | V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| 6 | Return on average equity | 52.07% | | | 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2024-09-30; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2025-09-30; 0001403161-25-000089 |
| 7 | Debt to equity | 0.66x | | | (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; instant to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; instant to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2025-09-30; 0001403161-25-000089 |
| 8 | Free cash flow | 21,577,000,000 USD | | | 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| 9 | The latest quarter's revenue | 12,139,000,000 USD | | | V/earnings_release.txt L212; First quarter column; three months ended 2026-09-30; source in millions; 0001403161-26-000126 |
| 10 | The quarter's growth versus the same quarter last year | 13.19% | | | (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; First quarter column; three months ended 2026-09-30; source in millions; 0001403161-26-000126; V/earnings_release.txt L212; Second quarter column; same quarter of prior year; source in millions; 0001403161-26-000126 |
| 11 | The quarter's diluted EPS, GAAP | 3.19 USD/shares; listed Class A | | | V/earnings_release.txt L250; First quarter column, GAAP diluted EPS; us-gaap:CommonClassAMember; 0001403161-26-000126 |

## Every other Financial Analyst number

| Claim | Report said / formula | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|
| Input: revenue | 40,000,000,000.00 USD | | | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| Input: operating_income | 23,994,000,000.00 USD | | | V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| Input: net_income | 20,058,000,000.00 USD | | | V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| Input: diluted_eps | 10.20 USD/shares | | | V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| Input: equity | 37,909,000,000.00 USD | | | V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2025-09-30; 0001403161-25-000089 |
| Input: long_term_debt | 19,602,000,000.00 USD | | | V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; instant to 2025-09-30; 0001403161-25-000089 |
| Input: current_debt | 5,569,000,000.00 USD | | | V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; instant to 2025-09-30; 0001403161-25-000089 |
| Input: operating_cash_flow | 23,059,000,000.00 USD | | | V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| Input: capex | 1,482,000,000.00 USD | | | V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089 |
| Input: prior_revenue | 35,926,000,000.00 USD | | | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089 |
| Input: prior_equity | 39,137,000,000.00 USD | | | V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; instant to 2024-09-30; 0001403161-25-000089 |
| MA revenue | 32,791,000,000 USD | | | MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013 |
| MA operating_income | 18,897,000,000 USD | | | MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013 |
| MA GAAP operating margin | 57.63%; 18,897,000,000 / 32,791,000,000 * 100 | | | MA/ratios.json; own annual fiscal period |
| PYPL revenue | 33,172,000,000 USD | | | PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024 |
| PYPL operating_income | 6,065,000,000 USD | | | PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024 |
| PYPL GAAP operating margin | 18.28%; 6,065,000,000 / 33,172,000,000 * 100 | | | PYPL/ratios.json; own annual fiscal period |
| Ratio: revenue_growth | 11.34 %; (40,000,000,000 / 35,926,000,000 - 1) * 100 | | | V/ratios.json and cited fact inputs |
| Ratio: operating_margin | 59.99 %; 23,994,000,000 / 40,000,000,000 * 100 | | | V/ratios.json and cited fact inputs |
| Ratio: return_on_average_equity | 52.07 %; 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100 | | | V/ratios.json and cited fact inputs |
| Ratio: debt_to_equity | 0.66 x; (19,602,000,000 + 5,569,000,000) / 37,909,000,000 | | | V/ratios.json and cited fact inputs |
| Ratio: free_cash_flow | 21,577,000,000.00 USD; 23,059,000,000 - 1,482,000,000 | | | V/ratios.json and cited fact inputs |
| Ratio: price_earnings | 39.40 x; 401.86 / 10.20 | | | V/ratios.json and cited fact inputs |
| Dated market price | 401.86 USD on 2026-10-27 | | | market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted |
| Newer full-year GAAP EPS, if stated | See the full-year column, not the quarter column | | | quarter_observations.json; release EPS row and period headers |
| Other dates, amounts and period labels in Financial Analyst text | Inspect every remaining numerical statement | | | Report source register and original filing headers |

## Report checks

| Check | Report said | Filing says / evidence (human) | Mark (human) | Where |
|---|---|---|---|---|
| Template | Overview; Market Positioning and Growth Outlook; Valuation Insights; Future Developments and Strategic Recommendations; Investment Recommendation | | | The five report headings |
| Recommendation | Buy, Hold or Sell; names a number stated in this report; thesis uses numbers the human audit marked correct | | | Investment Recommendation and the marked core/other-number rows |

## Corrections and decision

**Claim / role / correction / recheck:** ____________________
**Decision (approve draft or return for revision):** ____________________
**Reviewer name / date / report version:** ____________________

A model or code check must not fill these fields. If a correction changes the report, review that version before signing. See [the human sign-off explanation](human_signoff.md).
