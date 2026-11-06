# Checkpoint 2 human audit - COST

**Human reviewer / date:** ____________________
**Report file and version reviewed:** ____________________
**Generated verified report SHA-256:** 0d53514ab252108a871b93efb5c7add287da7e08ecb2ff1deb1e407f26ce2e06
**Errors (wrong + unsupported):** ____   **Missing claims:** ____
**Decision (approve or return for revision):** ____________________

Fill Filing says and Mark only after opening the cited filing. Automatic marks are not human findings. Repeated occurrences are listed by claim ID so they can all be checked.

Marks: Correct; Wrong; Unsupported; Missing; Not in filings. Record the filing's correct figure and the necessary correction for a non-correct claim.

## Eleven core claims

| Claim | Report said | Occurrences | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|---|
| 1 Total annual revenue | 303,154,000,000.00 USD (COST.fact.revenue) | C017 |  |  | COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Total revenue / 303,154 / / / 275,235 / / / 254,453 / |
| 2 Annual revenue growth | 10.14 % (COST.ratio.revenue_growth) | C001, C005, C006, C028 |  |  | (303,154,000,000 / 275,235,000,000 - 1) * 100; COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Total revenue / 303,154 / / / 275,235 / / / 254,453 /; COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-09-02 to 2025-08-31; 0000909832-26-000093; Total revenue / 303,154 / / / 275,235 / / / 254,453 / |
| 3 Operating income and margin | 3.85 % (COST.ratio.operating_margin); 11,685,000,000.00 USD (COST.fact.operating_income) | C002, C007, C008, C018, C029 |  |  | COST/10-K.txt L723; us-gaap:OperatingIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Operating income / 11,685 / / / 10,383 / / / 9,285 /; 11,685,000,000 / 303,154,000,000 * 100; COST/10-K.txt L723; us-gaap:OperatingIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Operating income / 11,685 / / / 10,383 / / / 9,285 /; COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Total revenue / 303,154 / / / 275,235 / / / 254,453 / |
| 4 Net income attributable to company | 9,226,000,000.00 USD (COST.fact.net_income) | C019 |  |  | COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; NET INCOME / $ / 9,226 / / / $ / 8,099 / / / $ / 7,367 / |
| 5 Annual GAAP diluted EPS | 20.76 USD/shares (COST.fact.diluted_eps) | C020 |  |  | COST/10-K.txt L734; us-gaap:EarningsPerShareDiluted; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Diluted / $ / 20.76 / / / $ / 18.21 / / / $ / 16.56 / |
| 6 Return on average equity | 28.40 % (COST.ratio.return_on_average_equity) | C009, C010, C030, I050, D051 |  |  | 9,226,000,000 / ((29,164,000,000 + 35,803,000,000) / 2) * 100; COST/10-K.txt L731; us-gaap:NetIncomeLoss; 2025-09-01 to 2026-08-30; 0000909832-26-000093; NET INCOME / $ / 9,226 / / / $ / 8,099 / / / $ / 7,367 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2025-08-31; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2026-08-30; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
| 7 Debt/equity including current portion | 0.17 x (COST.ratio.debt_to_equity) | C004, C011, C012, C031, I049, I052 |  |  | (3,914,000,000 + 2,248,000,000) / 35,803,000,000; COST/10-K.txt L783; us-gaap:LongTermDebtNoncurrent; 2026-08-30; 0000909832-26-000093; Long-term debt, excluding current portion / 3,914 / / / 5,713 /; COST/10-K.txt L779; us-gaap:LongTermDebtCurrent; 2026-08-30; 0000909832-26-000093; Current portion of long-term debt / 2,248 / / / 75 /; COST/10-K.txt L796; us-gaap:StockholdersEquity; 2026-08-30; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
| 8 Free cash flow | 9,382,000,000.00 USD (COST.ratio.free_cash_flow) | C003, C013, C014, C032 |  |  | 15,817,000,000 - 6,435,000,000; COST/10-K.txt L850; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Net cash provided by operating activities / 15,817 / / / 13,335 / / / 11,339 /; COST/10-K.txt L852; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Additions to property and equipment / ( 6,435 ) / / / ( 5,498 ) / / / ( 4,710 ) / |
| 9 Latest quarter revenue | 95,723,000,000.00 USD (COST.quarter.quarter_net_revenue) | C044 |  |  | COST/earnings_release.txt L48; statement column; 16 weeks ended 2026-08-30; 0000909832-26-000084; Total revenue / 95,723 / / / 86,156 / / / 303,154 / / / 275,235 / |
| 10 Latest quarter nominal growth | 11.10 % (COST.quarter.revenue_growth) | C048 |  |  | (95,723,000,000 / 86,156,000,000 - 1) * 100; COST/earnings_release.txt L48; statement column; 16 weeks ended 2026-08-30; 0000909832-26-000084; Total revenue / 95,723 / / / 86,156 / / / 303,154 / / / 275,235 /; COST/earnings_release.txt L48; statement column; corresponding quarter ended 2025-08-31; 0000909832-26-000084; Total revenue / 95,723 / / / 86,156 / / / 303,154 / / / 275,235 / |
| 11 Latest quarter GAAP diluted EPS | 6.75 USD/shares (COST.quarter.quarter_gaap_diluted_eps) | C046 |  |  | COST/earnings_release.txt L64; statement column; 16 weeks ended 2026-08-30; 0000909832-26-000084; Diluted / $ / 6.75 / / / $ / 5.87 / / / $ / 20.76 / / / $ / 18.21 / |

## Other numerical claims

| Claim/source | Report said | Occurrences | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|---|
| COST.ratio.price_earnings | 43.18 x (COST.ratio.price_earnings) | C015, C016, C033 |  |  | 896.48 / 20.76; market_input.json; 2026-09-24; WRDS Compustat comp.secd.prccd; primary U.S. security; dated security ticker COST; 2026-09-24; COST/10-K.txt L734; us-gaap:EarningsPerShareDiluted; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Diluted / $ / 20.76 / / / $ / 18.21 / / / $ / 16.56 / |
| COST.fact.equity | 35,803,000,000.00 USD (COST.fact.equity) | C021 |  |  | COST/10-K.txt L796; us-gaap:StockholdersEquity; 2026-08-30; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
| COST.fact.long_term_debt | 3,914,000,000.00 USD (COST.fact.long_term_debt) | C022 |  |  | COST/10-K.txt L783; us-gaap:LongTermDebtNoncurrent; 2026-08-30; 0000909832-26-000093; Long-term debt, excluding current portion / 3,914 / / / 5,713 / |
| COST.fact.current_debt | 2,248,000,000.00 USD (COST.fact.current_debt) | C023 |  |  | COST/10-K.txt L779; us-gaap:LongTermDebtCurrent; 2026-08-30; 0000909832-26-000093; Current portion of long-term debt / 2,248 / / / 75 / |
| COST.fact.operating_cash_flow | 15,817,000,000.00 USD (COST.fact.operating_cash_flow) | C024 |  |  | COST/10-K.txt L850; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Net cash provided by operating activities / 15,817 / / / 13,335 / / / 11,339 / |
| COST.fact.capex | 6,435,000,000.00 USD (COST.fact.capex) | C025 |  |  | COST/10-K.txt L852; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; 2025-09-01 to 2026-08-30; 0000909832-26-000093; Additions to property and equipment / ( 6,435 ) / / / ( 5,498 ) / / / ( 4,710 ) / |
| COST.fact.prior_revenue | 275,235,000,000.00 USD (COST.fact.prior_revenue) | C026 |  |  | COST/10-K.txt L719; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-09-02 to 2025-08-31; 0000909832-26-000093; Total revenue / 303,154 / / / 275,235 / / / 254,453 / |
| COST.fact.prior_equity | 29,164,000,000.00 USD (COST.fact.prior_equity) | C027 |  |  | COST/10-K.txt L796; us-gaap:StockholdersEquity; 2025-08-31; 0000909832-26-000093; TOTAL EQUITY / 35,803 / / / 29,164 / |
| WMT.fact.revenue | 713,163,000,000.00 USD (WMT.fact.revenue) | C034 |  |  | WMT/10-K.txt L826; us-gaap:Revenues; 2025-02-01 to 2026-01-31; 0000104169-26-000055; Total revenues / / 713,163 / / / 680,985 / / / 648,125 / |
| WMT.fact.operating_income | 29,825,000,000.00 USD (WMT.fact.operating_income) | C035 |  |  | WMT/10-K.txt L830; us-gaap:OperatingIncomeLoss; 2025-02-01 to 2026-01-31; 0000104169-26-000055; Operating income / / 29,825 / / / 29,348 / / / 27,012 / |
| WMT.ratio.operating_margin | 4.18 % (WMT.ratio.operating_margin) | C036 |  |  | 29,825,000,000 / 713,163,000,000 * 100; WMT/10-K.txt L830; us-gaap:OperatingIncomeLoss; 2025-02-01 to 2026-01-31; 0000104169-26-000055; Operating income / / 29,825 / / / 29,348 / / / 27,012 /; WMT/10-K.txt L826; us-gaap:Revenues; 2025-02-01 to 2026-01-31; 0000104169-26-000055; Total revenues / / 713,163 / / / 680,985 / / / 648,125 / |
| TGT.fact.revenue | 104,780,000,000.00 USD (TGT.fact.revenue) | C037 |  |  | TGT/10-K.txt L1123; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-02-02 to 2026-01-31; 0000027419-26-000016; Net sales / $ / 104,780 / / $ / 106,566 / / $ / 107,412 / |
| TGT.fact.operating_income | 5,117,000,000.00 USD (TGT.fact.operating_income) | C038 |  |  | TGT/10-K.txt L1127; us-gaap:OperatingIncomeLoss; 2025-02-02 to 2026-01-31; 0000027419-26-000016; Operating income / 5,117 / / 5,566 / / 5,707 / |
| TGT.ratio.operating_margin | 4.88 % (TGT.ratio.operating_margin) | C039 |  |  | 5,117,000,000 / 104,780,000,000 * 100; TGT/10-K.txt L1127; us-gaap:OperatingIncomeLoss; 2025-02-02 to 2026-01-31; 0000027419-26-000016; Operating income / 5,117 / / 5,566 / / 5,707 /; TGT/10-K.txt L1123; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-02-02 to 2026-01-31; 0000027419-26-000016; Net sales / $ / 104,780 / / $ / 106,566 / / $ / 107,412 / |
| BJ.fact.revenue | 21,457,274,000.00 USD (BJ.fact.revenue) | C040 |  |  | BJ/10-K.txt L991; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-02-02 to 2026-01-31; 0001531152-26-000007; Total revenues / 21,457,274 / / / 20,501,804 / / / 19,968,689 / |
| BJ.fact.operating_income | 816,604,000.00 USD (BJ.fact.operating_income) | C041 |  |  | BJ/10-K.txt L995; us-gaap:OperatingIncomeLoss; 2025-02-02 to 2026-01-31; 0001531152-26-000007; Operating income / 816,604 / / / 772,206 / / / 800,419 / |
| BJ.ratio.operating_margin | 3.81 % (BJ.ratio.operating_margin) | C042 |  |  | 816,604,000 / 21,457,274,000 * 100; BJ/10-K.txt L995; us-gaap:OperatingIncomeLoss; 2025-02-02 to 2026-01-31; 0001531152-26-000007; Operating income / 816,604 / / / 772,206 / / / 800,419 /; BJ/10-K.txt L991; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2025-02-02 to 2026-01-31; 0001531152-26-000007; Total revenues / 21,457,274 / / / 20,501,804 / / / 19,968,689 / |
| COST.price | 896.48 USD/shares (COST.price) | C043 |  |  | market_input.json; 2026-09-24; WRDS Compustat comp.secd.prccd; primary U.S. security; dated security ticker COST; 2026-09-24 |
| COST.quarter.prior_quarter_net_revenue | 86,156,000,000.00 USD (COST.quarter.prior_quarter_net_revenue) | C045 |  |  | COST/earnings_release.txt L48; statement column; corresponding quarter ended 2025-08-31; 0000909832-26-000084; Total revenue / 95,723 / / / 86,156 / / / 303,154 / / / 275,235 / |
| COST.quarter.annual_release_gaap_diluted_eps | 20.76 USD/shares (COST.quarter.annual_release_gaap_diluted_eps) | C047 |  |  | COST/earnings_release.txt L64; statement column; full fiscal year ended 2026-08-30; 0000909832-26-000084; Diluted / $ / 6.75 / / / $ / 5.87 / / / $ / 20.76 / / / $ / 18.21 / |

## Three Insight checks

| Insight | Numerical claim/source | Source checked by human | Adds to headline? Human explanation |
|---|---|---|---|
| Insight: The modest leverage ratio provides financial flexibility for future strategic initiatives. | I049 / COST.ratio.debt_to_equity | | |
| Insight: A high return on average equity signals that the company generates strong earnings relative to the capital invested by shareholders, underscoring the durability of its profit generation | I050 / COST.ratio.return_on_average_equity | | |
| Insight: The modest leverage ratio indicates ample financial flexibility for future growth initiatives. | I052 / COST.ratio.debt_to_equity | | |

## Report and partner checks

**Five required report parts present / human mark:** ____________________
**Buy/Hold/Sell names a reported metric using checked numbers / human mark:** ____________________

**Partner name / selected ticker / selection date:** ____________________
**Partner claim one / filing value / mark / source:** ____________________
**Partner claim two / filing value / mark / source:** ____________________
**Partner's Insight citation checked / finding:** ____________________

## Corrections and recheck

**Claim / responsible role / correction / new report version / recheck:** ____________________

Keep the original findings. Review the corrected version before recording approval. No human mark or authorship is supplied by this worksheet.
