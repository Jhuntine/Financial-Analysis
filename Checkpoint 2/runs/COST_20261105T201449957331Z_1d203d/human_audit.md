# Checkpoint 2 human audit - COSTCO WHOLESALE CORP /NEW

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
| 1 | Total revenue, latest fiscal year | 303,154,000,000 USD | | | COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| 2 | Revenue growth versus the prior year | 10.14% | | | (303,154,000,000 / 275,235,000,000 - 1) * 100; COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093; COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-09-02 to 2025-08-31; 0000909832-26-000093 |
| 3 | Operating income and operating margin | 11,685,000,000 USD; 3.85% | | | 11,685,000,000 / 303,154,000,000 * 100; COST/10-K.txt L723; us-gaap:OperatingIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| 4 | Net income attributable to the company | 9,226,000,000 USD | | | COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| 5 | Diluted earnings per share, GAAP | 20.76 USD/shares; listed common stock | | | COST/10-K.txt L734; us-gaap:EarningsPerShareDiluted; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| 6 | Return on average equity | 28.40% | | | 9,226,000,000 / ((29,164,000,000 + 35,803,000,000) / 2) * 100; COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; COST/10-K.txt L796; us-gaap:StockholdersEquity; instant to 2025-08-31; 0000909832-26-000093; COST/10-K.txt L796; us-gaap:StockholdersEquity; instant to 2026-08-30; 0000909832-26-000093 |
| 7 | Debt to equity | 0.17x | | | (3,914,000,000 + 2,248,000,000) / 35,803,000,000; COST/10-K.txt L783; us-gaap:LongTermDebtNoncurrent; instant to 2026-08-30; 0000909832-26-000093; COST/10-K.txt L779; us-gaap:LongTermDebtCurrent; instant to 2026-08-30; 0000909832-26-000093; COST/10-K.txt L796; us-gaap:StockholdersEquity; instant to 2026-08-30; 0000909832-26-000093 |
| 8 | Free cash flow | 9,382,000,000 USD | | | 15,817,000,000 - 6,435,000,000; COST/10-K.txt L850; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2025-09-01 to 2026-08-30; 0000909832-26-000093; COST/10-K.txt L852; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| 9 | The latest quarter's revenue | 95,723,000,000 USD | | | COST/earnings_release.txt L48; First quarter column; 16 weeks ended 2026-08-30; Total revenue; source in millions; 0000909832-26-000084 |
| 10 | The quarter's growth versus the same quarter last year | 11.10% | | | (95,723,000,000 / 86,156,000,000 - 1) * 100; COST/earnings_release.txt L48; First quarter column; 16 weeks ended 2026-08-30; Total revenue; source in millions; 0000909832-26-000084; COST/earnings_release.txt L48; Second quarter column; corresponding quarter ended 2025-08-31; Total revenue; source in millions; 0000909832-26-000084 |
| 11 | The quarter's diluted EPS, GAAP | 6.75 USD/shares; listed common stock | | | COST/earnings_release.txt L64; First quarter column; GAAP diluted EPS; 16 weeks ended 2026-08-30; listed common stock; no separate class dimension; 0000909832-26-000084 |

## Every other Financial Analyst number

| Claim | Report said / formula | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|
| Input: revenue | 303,154,000,000.00 USD | | | COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| Input: operating_income | 11,685,000,000.00 USD | | | COST/10-K.txt L723; us-gaap:OperatingIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| Input: net_income | 9,226,000,000.00 USD | | | COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| Input: diluted_eps | 20.76 USD/shares | | | COST/10-K.txt L734; us-gaap:EarningsPerShareDiluted; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| Input: equity | 35,803,000,000.00 USD | | | COST/10-K.txt L796; us-gaap:StockholdersEquity; instant to 2026-08-30; 0000909832-26-000093 |
| Input: long_term_debt | 3,914,000,000.00 USD | | | COST/10-K.txt L783; us-gaap:LongTermDebtNoncurrent; instant to 2026-08-30; 0000909832-26-000093 |
| Input: current_debt | 2,248,000,000.00 USD | | | COST/10-K.txt L779; us-gaap:LongTermDebtCurrent; instant to 2026-08-30; 0000909832-26-000093 |
| Input: operating_cash_flow | 15,817,000,000.00 USD | | | COST/10-K.txt L850; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| Input: capex | 6,435,000,000.00 USD | | | COST/10-K.txt L852; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; 2025-09-01 to 2026-08-30; 0000909832-26-000093 |
| Input: prior_revenue | 275,235,000,000.00 USD | | | COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-09-02 to 2025-08-31; 0000909832-26-000093 |
| Input: prior_equity | 29,164,000,000.00 USD | | | COST/10-K.txt L796; us-gaap:StockholdersEquity; instant to 2025-08-31; 0000909832-26-000093 |
| WMT revenue | 713,163,000,000 USD | | | WMT/10-K.txt L826; us-gaap:Revenues; 2025-02-01 to 2026-01-31; 0000104169-26-000055 |
| WMT operating_income | 29,825,000,000 USD | | | WMT/10-K.txt L830; us-gaap:OperatingIncomeLoss; 2025-02-01 to 2026-01-31; 0000104169-26-000055 |
| WMT GAAP operating margin | 4.18%; 29,825,000,000 / 713,163,000,000 * 100 | | | WMT/ratios.json; own annual fiscal period |
| TGT revenue | 104,780,000,000 USD | | | TGT/10-K.txt L1123; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-02-02 to 2026-01-31; 0000027419-26-000016 |
| TGT operating_income | 5,117,000,000 USD | | | TGT/10-K.txt L1127; us-gaap:OperatingIncomeLoss; 2025-02-02 to 2026-01-31; 0000027419-26-000016 |
| TGT GAAP operating margin | 4.88%; 5,117,000,000 / 104,780,000,000 * 100 | | | TGT/ratios.json; own annual fiscal period |
| BJ revenue | 21,457,274,000 USD | | | BJ/10-K.txt L991; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-02-02 to 2026-01-31; 0001531152-26-000007 |
| BJ operating_income | 816,604,000 USD | | | BJ/10-K.txt L995; us-gaap:OperatingIncomeLoss; 2025-02-02 to 2026-01-31; 0001531152-26-000007 |
| BJ GAAP operating margin | 3.81%; 816,604,000 / 21,457,274,000 * 100 | | | BJ/ratios.json; own annual fiscal period |
| Ratio: revenue_growth | 10.14 %; (303,154,000,000 / 275,235,000,000 - 1) * 100 | | | COST/ratios.json and cited fact inputs |
| Ratio: operating_margin | 3.85 %; 11,685,000,000 / 303,154,000,000 * 100 | | | COST/ratios.json and cited fact inputs |
| Ratio: return_on_average_equity | 28.40 %; 9,226,000,000 / ((29,164,000,000 + 35,803,000,000) / 2) * 100 | | | COST/ratios.json and cited fact inputs |
| Ratio: debt_to_equity | 0.17 x; (3,914,000,000 + 2,248,000,000) / 35,803,000,000 | | | COST/ratios.json and cited fact inputs |
| Ratio: free_cash_flow | 9,382,000,000.00 USD; 15,817,000,000 - 6,435,000,000 | | | COST/ratios.json and cited fact inputs |
| Ratio: price_earnings | 43.18 x; 896.48 / 20.76 | | | COST/ratios.json and cited fact inputs |
| Dated market price | 896.48 USD on 2026-09-24 | | | market_input.json; WRDS Compustat comp.secd.prccd; primary U.S. security; dated security ticker COST; 2026-09-24 |
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

## Analyst Insight checks

| Claim | Report said | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|
| Insight: Costco's return on average equity of [[COST.ratio.return_on_average_equity]] highlights its efficiency in turning shareholders' capital into earnings, a core component of intrinsic valuation. | 28.40 % | | | 9,226,000,000 / ((29,164,000,000 + 35,803,000,000) / 2) * 100; COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; NET INCOME / $ / 9,226 / / / $ / 8,099 / / / $ / 7,367 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2025-08-31; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2026-08-30; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
| Insight: Return on average equity demonstrates strong profitability relative to shareholders' capital. | 28.40 % | | | 9,226,000,000 / ((29,164,000,000 + 35,803,000,000) / 2) * 100; COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; NET INCOME / $ / 9,226 / / / $ / 8,099 / / / $ / 7,367 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2025-08-31; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2026-08-30; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
| Insight: The modest debt‑to‑equity ratio reflects a conservative capital structure. | 0.17 x | | | (3,914,000,000 + 2,248,000,000) / 35,803,000,000; COST/10-K.txt L783; us-gaap:LongTermDebtNoncurrent; 2026-08-30; 0000909832-26-000093; Long-term debt, excluding current portion / 3,914 / / / 5,713 /; COST/10-K.txt L779; us-gaap:LongTermDebtCurrent; 2026-08-30; 0000909832-26-000093; Current portion of long-term debt / 2,248 / / / 75 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2026-08-30; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
