# Checkpoint 2 human audit - V

**Human reviewer / date:** ____________________
**Report file and version reviewed:** ____________________
**Generated verified report SHA-256:** fd481132cdfe5f0b254343e5eca4edcaa9524ddb69cf29fc95cd61f1ce21a286
**Errors (wrong + unsupported):** ____   **Missing claims:** ____
**Decision (approve or return for revision):** ____________________

Fill Filing says and Mark only after opening the cited filing. Automatic marks are not human findings. Repeated occurrences are listed by claim ID so they can all be checked.

Marks: Correct; Wrong; Unsupported; Missing; Not in filings. Record the filing's correct figure and the necessary correction for a non-correct claim.

## Eleven core claims

| Claim | Report said | Occurrences | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|---|
| 1 Total annual revenue | 40,000,000,000.00 USD (V.fact.revenue) | C001, C010 |  |  | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| 2 Annual revenue growth | 11.34 % (V.ratio.revenue_growth) | C021 |  |  | (40,000,000,000 / 35,926,000,000 - 1) * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| 3 Operating income and margin | 59.98 % (V.ratio.operating_margin); 23,994,000,000.00 USD (V.fact.operating_income) | C005, C011, C022, C040, I046 |  |  | V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| 4 Net income attributable to company | 20,058,000,000.00 USD (V.fact.net_income) | C012 |  |  | V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / / |
| 5 Annual GAAP diluted EPS | 10.20 USD/shares (V.fact.diluted_eps) | C002, C013 |  |  | V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| 6 Return on average equity | 52.07 % (V.ratio.return_on_average_equity) | C006, C023, C043, I044 |  |  | 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| 7 Debt/equity including current portion | 0.66 x (V.ratio.debt_to_equity) | C007, C024, I039, C042 |  |  | (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 /; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| 8 Free cash flow | 21,577,000,000.00 USD (V.ratio.free_cash_flow) | C008, C025, C041 |  |  | 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 /; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| 9 Latest quarter revenue | 12,139,000,000.00 USD (V.quarter.quarter_net_revenue) | C034 |  |  | V/earnings_release.txt L212; statement column; three months ended 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| 10 Latest quarter nominal growth | 13.19 % (V.quarter.revenue_growth) | C038 |  |  | (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; statement column; three months ended 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 /; V/earnings_release.txt L212; statement column; corresponding quarter ended 2025-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| 11 Latest quarter GAAP diluted EPS | 3.19 USD/shares (V.quarter.quarter_gaap_diluted_eps) | C036 |  |  | V/earnings_release.txt L250; statement column; three months ended 2026-09-30; 0001403161-26-000126; Class A common stock / $ / 3.19 / / / $ / 2.62 / / / $ / 12.32 / / / $ / 10.20 / |

## Other numerical claims

| Claim/source | Report said | Occurrences | Filing says (human) | Mark (human) | Where |
|---|---|---|---|---|---|
| V.fact.capex | 1,482,000,000.00 USD (V.fact.capex) | C003, C018 |  |  | V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| V.price | 401.86 USD/shares (V.price) | C004, C033 |  |  | market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted |
| V.ratio.price_earnings | 39.40 x (V.ratio.price_earnings) | C009, C026, D045 |  |  | 401.86 / 10.20; market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| V.fact.equity | 37,909,000,000.00 USD (V.fact.equity) | C014 |  |  | V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| V.fact.long_term_debt | 19,602,000,000.00 USD (V.fact.long_term_debt) | C015 |  |  | V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 / |
| V.fact.current_debt | 5,569,000,000.00 USD (V.fact.current_debt) | C016 |  |  | V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — / |
| V.fact.operating_cash_flow | 23,059,000,000.00 USD (V.fact.operating_cash_flow) | C017 |  |  | V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 / |
| V.fact.prior_revenue | 35,926,000,000.00 USD (V.fact.prior_revenue) | C019 |  |  | V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| V.fact.prior_equity | 39,137,000,000.00 USD (V.fact.prior_equity) | C020 |  |  | V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| MA.fact.revenue | 32,791,000,000.00 USD (MA.fact.revenue) | C027 |  |  | MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Net Revenue / / $ / 32,791 / / / $ / 28,167 / / / $ / 25,098 / |
| MA.fact.operating_income | 18,897,000,000.00 USD (MA.fact.operating_income) | C028 |  |  | MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Operating income / / 18,897 / / / 15,582 / / / 14,008 / |
| MA.ratio.operating_margin | 57.63 % (MA.ratio.operating_margin) | C029 |  |  | 18,897,000,000 / 32,791,000,000 * 100; MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Operating income / / 18,897 / / / 15,582 / / / 14,008 /; MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Net Revenue / / $ / 32,791 / / / $ / 28,167 / / / $ / 25,098 / |
| PYPL.fact.revenue | 33,172,000,000.00 USD (PYPL.fact.revenue) | C030 |  |  | PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Net revenues / $ / 33,172 / / / $ / 31,797 / / / $ / 29,771 / |
| PYPL.fact.operating_income | 6,065,000,000.00 USD (PYPL.fact.operating_income) | C031 |  |  | PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Operating income / 6,065 / / / 5,325 / / / 5,028 / |
| PYPL.ratio.operating_margin | 18.28 % (PYPL.ratio.operating_margin) | C032 |  |  | 6,065,000,000 / 33,172,000,000 * 100; PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Operating income / 6,065 / / / 5,325 / / / 5,028 /; PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Net revenues / $ / 33,172 / / / $ / 31,797 / / / $ / 29,771 / |
| V.quarter.prior_quarter_net_revenue | 10,724,000,000.00 USD (V.quarter.prior_quarter_net_revenue) | C035 |  |  | V/earnings_release.txt L212; statement column; corresponding quarter ended 2025-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| V.quarter.annual_release_gaap_diluted_eps | 12.32 USD/shares (V.quarter.annual_release_gaap_diluted_eps) | C037 |  |  | V/earnings_release.txt L250; statement column; full fiscal year ended 2026-09-30; 0001403161-26-000126; Class A common stock / $ / 3.19 / / / $ / 2.62 / / / $ / 12.32 / / / $ / 10.20 / |

## Three Insight checks

| Insight | Numerical claim/source | Source checked by human | Adds to headline? Human explanation |
|---|---|---|---|
| Insight: The leverage level indicated by the debt‑to‑equity ratio is a key gauge of balance‑sheet risk. | I039 / V.ratio.debt_to_equity | | |
| Insight: Return on average equity indicates robust profitability and effective capital deployment. | I044 / V.ratio.return_on_average_equity | | |
| Insight: Operating margin of [[V.ratio.operating_margin]] percent underscores cost efficiency. | I046 / V.ratio.operating_margin | | |

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
