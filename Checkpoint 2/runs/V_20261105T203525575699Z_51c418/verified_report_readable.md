VISA INC. (V); filings read: V 10-K 0001403161-25-000089; V 10-Q 0001403161-26-000104; V earnings 0001403161-26-000126; MA 10-K 0001141391-26-000013; PYPL 10-K 0001633917-26-000024

> Verifier: LIVE semantic check completed. Marks refer to the original report. Human review pending.

| Claim | Mark | Reported | Corrected | Evidence / reason |
|---|---|---:|---:|---|
| C001 | correct | 59.985 |  | Exact source context and rounded value match. 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C002 | correct | 52.06759598162137 |  | Exact source context and rounded value match. 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C003 | correct | 0.6639848057189586 |  | Exact source context and rounded value match. (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 /; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C004 | wrong | 21577000000.0 | 21577000000.0 | Claim value 21577000000 differs from source fact value 21577000 (saved XBRL). 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 /; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| C005 | correct | 39.39803921568628 |  | Exact source context and rounded value match. 401.86 / 10.20; market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| C006 | correct | 40000000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C007 | correct | 10.2 |  | Exact source context and rounded value match. V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| C008 | correct | 1482000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| C009 | correct | 40000000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C010 | correct | 23994000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 / |
| C011 | correct | 20058000000.0 |  | Exact source context and rounded value match. V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / / |
| C012 | correct | 10.2 |  | Exact source context and rounded value match. V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| C013 | correct | 37909000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C014 | correct | 19602000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 / |
| C015 | correct | 5569000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — / |
| C016 | correct | 23059000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 / |
| C017 | correct | 1482000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| C018 | correct | 35926000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C019 | correct | 39137000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C020 | correct | 11.339976618604908 |  | Exact source context and rounded value match. (40,000,000,000 / 35,926,000,000 - 1) * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C021 | correct | 59.985 |  | Exact source context and rounded value match. 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C022 | correct | 52.06759598162137 |  | Exact source context and rounded value match. 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C023 | correct | 0.6639848057189586 |  | Exact source context and rounded value match. (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 /; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C024 | wrong | 21577000000.0 |  | Claim value 21577000000 differs from source fact value 21577000 (saved XBRL). 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 /; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| C025 | correct | 39.39803921568628 |  | Exact source context and rounded value match. 401.86 / 10.20; market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| C026 | correct | 32791000000.0 |  | Exact source context and rounded value match. MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Net Revenue / / $ / 32,791 / / / $ / 28,167 / / / $ / 25,098 / |
| C027 | correct | 18897000000.0 |  | Exact source context and rounded value match. MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Operating income / / 18,897 / / / 15,582 / / / 14,008 / |
| C028 | correct | 57.62861760849013 |  | Exact source context and rounded value match. 18,897,000,000 / 32,791,000,000 * 100; MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Operating income / / 18,897 / / / 15,582 / / / 14,008 /; MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Net Revenue / / $ / 32,791 / / / $ / 28,167 / / / $ / 25,098 / |
| C029 | correct | 33172000000.0 |  | Exact source context and rounded value match. PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Net revenues / $ / 33,172 / / / $ / 31,797 / / / $ / 29,771 / |
| C030 | correct | 6065000000.0 |  | Exact source context and rounded value match. PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Operating income / 6,065 / / / 5,325 / / / 5,028 / |
| C031 | correct | 18.28349210177258 |  | Exact source context and rounded value match. 6,065,000,000 / 33,172,000,000 * 100; PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Operating income / 6,065 / / / 5,325 / / / 5,028 /; PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Net revenues / $ / 33,172 / / / $ / 31,797 / / / $ / 29,771 / |
| C032 | correct | 401.86 |  | Exact source context and rounded value match. market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted |
| C033 | correct | 12139000000.0 |  | Exact source context and rounded value match. V/earnings_release.txt L212; statement column; three months ended 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| C034 | correct | 10724000000.0 |  | Exact source context and rounded value match. V/earnings_release.txt L212; statement column; corresponding quarter ended 2025-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| C035 | correct | 3.19 |  | Exact source context and rounded value match. V/earnings_release.txt L250; statement column; three months ended 2026-09-30; 0001403161-26-000126; Class A common stock / $ / 3.19 / / / $ / 2.62 / / / $ / 12.32 / / / $ / 10.20 / |
| C036 | correct | 12.32 |  | Exact source context and rounded value match. V/earnings_release.txt L250; statement column; full fiscal year ended 2026-09-30; 0001403161-26-000126; Class A common stock / $ / 3.19 / / / $ / 2.62 / / / $ / 12.32 / / / $ / 10.20 / |
| C037 | correct | 13.194703468854897 |  | Exact source context and rounded value match. (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; statement column; three months ended 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 /; V/earnings_release.txt L212; statement column; corresponding quarter ended 2025-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| I038 | wrong | 21577000000.0 | 21577000000.0 | Insight value 21577000000 differs from source fact value 21577000 (saved XBRL). 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 /; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| I039 | correct | 52.06759598162137 |  | Exact source context and rounded value match. 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| D040 | correct | 52.06759598162137 |  | Exact source context and rounded value match. 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| I041 | correct | 59.985 |  | Exact source context and rounded value match. 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |

Run UTC: 2026-11-05T20:37:56.293044+00:00; mode=live; manager_approved=True; human review pending.

> Live agent draft; human approval pending.

## Overview

Visa operates a global payments network that connects consumers, issuers, acquirers and merchants through a four‑party model, providing authorization, clearing and settlement services. The company emphasizes secure, reliable and efficient money movement and does not issue cards or set rates for account holders. [source:K:L151] [source:Q:L1253]

## Market Positioning and Growth Outlook

Visa’s growth strategy focuses on expanding consumer payments, commercial and money‑movement solutions, and value‑added services. It invests in token technology, cross‑border capabilities and digital commerce tools to capture volume from evolving consumer habits. The firm reports that revenue growth is driven by higher processed transactions, cross‑border volume and overall payments volume, while client incentives partially offset that growth. [source:K:L839] [source:K:L220] The competitive landscape includes emerging entrants leveraging blockchain, stablecoins and new network models, as well as regulatory shifts that may create local alternatives. Visa acknowledges that interchange fee structures and litigation can influence transaction volumes. [source:K:L382] [source:K:L441] Regulatory developments in the United Kingdom have prompted Visa to seek appellate review of decisions affecting interchange practices. [source:Q:L1180] These dynamics suggest that while Visa benefits from a strong network effect, it must navigate incentive pressures and competitive innovation to sustain its market share.

## Valuation Insights

Operating margin is (see sourced claim for V.ratio.operating_margin) percent, reflecting strong profitability relative to revenue. Return on average equity stands at (see sourced claim for V.ratio.return_on_average_equity) percent, indicating efficient use of shareholders’ capital. Debt to equity, including the current portion, is (see sourced claim for V.ratio.debt_to_equity) times, showing a moderate leverage profile. Free cash flow amounts to (see sourced claim for V.ratio.free_cash_flow) dollars, underscoring robust cash generation after capital expenditures. The price‑earnings multiple based on the latest filed annual diluted EPS is (see sourced claim for V.ratio.price_earnings) times, providing a valuation gauge against earnings. Total revenue for the fiscal year is (see sourced claim for V.fact.revenue) dollars, and GAAP diluted EPS is (see sourced claim for V.fact.diluted_eps) dollars per share, both reported under GAAP conventions for the common Class A share class. Capital expenditures of (see sourced claim for V.fact.capex) dollars represent cash outlays for property, equipment and technology.

**Referenced quantitative evidence** [C001]: **59.98 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: V.fact.operating_income=23,994,000,000.00, V.fact.revenue=40,000,000,000.00.

> Source: 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

**Referenced quantitative evidence** [C002]: **52.07 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP net income / average beginning and ending reported equity, percent.; inputs: V.fact.net_income=20,058,000,000.00, V.fact.prior_equity=39,137,000,000.00, V.fact.equity=37,909,000,000.00.

> Source: 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**Referenced quantitative evidence** [C003]: **0.66 x**. Period: 2024-10-01 to 2025-09-30. Definition: Long-term debt including its current portion / ending reported equity.; inputs: V.fact.long_term_debt=19,602,000,000.00, V.fact.current_debt=5,569,000,000.00, V.fact.equity=37,909,000,000.00.

> Source: (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 0001403161-25-000089; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**Corrected sourced metric: V.ratio.free_cash_flow** [C004]: **21,577,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Operating cash flow less reported property, equipment and technology purchases as applicable.; inputs: V.fact.operating_cash_flow=23,059,000,000.00, V.fact.capex=1,482,000,000.00.

> Source: 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089

**Referenced quantitative evidence** [C005]: **39.40 x**. Period: 2024-10-01 to 2025-09-30. Definition: Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.; inputs: V.price=401.86, V.fact.diluted_eps=10.20.

> Source: 401.86 / 10.20; market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089

**Referenced quantitative evidence** [C006]: **40,000,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Consolidated reported revenue; the source row names any net/gross convention..

> Source: V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

**Referenced quantitative evidence** [C007]: **10.20 USD/shares**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP diluted EPS for the listed common share class; consolidated fact if unambiguous..

> Source: V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089

**Referenced quantitative evidence** [C008]: **1,482,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Cash purchases of property/equipment (and technology if the reported row includes it); positive outflow..

> Source: V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089

### Financial Analyst evidence

**fact.revenue** [C009]: **40,000,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Consolidated reported revenue; the source row names any net/gross convention..

> Source: V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

**fact.operating income** [C010]: **23,994,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP consolidated operating income, including litigation and other reported operating costs..

> Source: V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089

**fact.net income** [C011]: **20,058,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP consolidated net income; use the equity scope identified in the source tag..

> Source: V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089

**fact.diluted eps** [C012]: **10.20 USD/shares**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP diluted EPS for the listed common share class; consolidated fact if unambiguous..

> Source: V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089

**fact.equity** [C013]: **37,909,000,000.00 USD**. Period: 2025-09-30. Definition: Reported consolidated stockholders' equity; scope is identified by the selected tag..

> Source: V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**fact.long term debt** [C014]: **19,602,000,000.00 USD**. Period: 2025-09-30. Definition: Carrying amount of long-term debt excluding its current portion; excludes operating leases..

> Source: V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 0001403161-25-000089

**fact.current debt** [C015]: **5,569,000,000.00 USD**. Period: 2025-09-30. Definition: Current portion of long-term debt; excludes unrelated short-term borrowings..

> Source: V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 0001403161-25-000089

**fact.operating cash flow** [C016]: **23,059,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Reported net cash provided by operating activities..

> Source: V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089

**fact.capex** [C017]: **1,482,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Cash purchases of property/equipment (and technology if the reported row includes it); positive outflow..

> Source: V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089

**fact.prior revenue** [C018]: **35,926,000,000.00 USD**. Period: 2023-10-01 to 2024-09-30. Definition: Consolidated reported revenue; the source row names any net/gross convention..

> Source: V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

**fact.prior equity** [C019]: **39,137,000,000.00 USD**. Period: 2024-09-30. Definition: Reported consolidated stockholders' equity; scope is identified by the selected tag..

> Source: V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**ratio.revenue growth** [C020]: **11.34 %**. Period: 2024-10-01 to 2025-09-30. Definition: Same-definition annual revenue / prior annual revenue minus one, percent.; inputs: V.fact.revenue=40,000,000,000.00, V.fact.prior_revenue=35,926,000,000.00.

> Source: (40,000,000,000 / 35,926,000,000 - 1) * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

**ratio.operating margin** [C021]: **59.98 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: V.fact.operating_income=23,994,000,000.00, V.fact.revenue=40,000,000,000.00.

> Source: 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

**ratio.return on average equity** [C022]: **52.07 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP net income / average beginning and ending reported equity, percent.; inputs: V.fact.net_income=20,058,000,000.00, V.fact.prior_equity=39,137,000,000.00, V.fact.equity=37,909,000,000.00.

> Source: 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**ratio.debt to equity** [C023]: **0.66 x**. Period: 2024-10-01 to 2025-09-30. Definition: Long-term debt including its current portion / ending reported equity.; inputs: V.fact.long_term_debt=19,602,000,000.00, V.fact.current_debt=5,569,000,000.00, V.fact.equity=37,909,000,000.00.

> Source: (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 0001403161-25-000089; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**ratio.free cash flow** [C024]: **21,577,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Operating cash flow less reported property, equipment and technology purchases as applicable.; inputs: V.fact.operating_cash_flow=23,059,000,000.00, V.fact.capex=1,482,000,000.00.

> Source: 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089

**ratio.price earnings** [C025]: **39.40 x**. Period: 2024-10-01 to 2025-09-30. Definition: Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.; inputs: V.price=401.86, V.fact.diluted_eps=10.20.

> Source: 401.86 / 10.20; market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089

**fact.revenue** [C026]: **32,791,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: Consolidated reported revenue; the source row names any net/gross convention..

> Source: MA/10-K.txt L1779; us-gaap:Revenues; 0001141391-26-000013

**fact.operating income** [C027]: **18,897,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP consolidated operating income, including litigation and other reported operating costs..

> Source: MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 0001141391-26-000013

**ratio.operating margin** [C028]: **57.63 %**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: MA.fact.operating_income=18,897,000,000.00, MA.fact.revenue=32,791,000,000.00.

> Source: 18,897,000,000 / 32,791,000,000 * 100; MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 0001141391-26-000013; MA/10-K.txt L1779; us-gaap:Revenues; 0001141391-26-000013

**fact.revenue** [C029]: **33,172,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: Consolidated reported revenue; the source row names any net/gross convention..

> Source: PYPL/10-K.txt L1212; us-gaap:Revenues; 0001633917-26-000024

**fact.operating income** [C030]: **6,065,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP consolidated operating income, including litigation and other reported operating costs..

> Source: PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 0001633917-26-000024

**ratio.operating margin** [C031]: **18.28 %**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: PYPL.fact.operating_income=6,065,000,000.00, PYPL.fact.revenue=33,172,000,000.00.

> Source: 6,065,000,000 / 33,172,000,000 * 100; PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 0001633917-26-000024; PYPL/10-K.txt L1212; us-gaap:Revenues; 0001633917-26-000024

**price** [C032]: **401.86 USD/shares**. Period: 2026-10-27. Definition: LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted.

> Source: market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted

**quarter.quarter net revenue** [C033]: **12,139,000,000.00 USD**. Period: three months ended 2026-09-30. Definition: First quarter column; three months ended 2026-09-30; Net revenue; source in millions.

> Source: V/earnings_release.txt L212; statement column; 0001403161-26-000126

**quarter.prior quarter net revenue** [C034]: **10,724,000,000.00 USD**. Period: corresponding quarter ended 2025-09-30. Definition: Second quarter column; corresponding quarter ended 2025-09-30; Net revenue; source in millions.

> Source: V/earnings_release.txt L212; statement column; 0001403161-26-000126

**quarter.quarter gaap diluted eps** [C035]: **3.19 USD/shares**. Period: three months ended 2026-09-30. Definition: First quarter column; GAAP diluted EPS; three months ended 2026-09-30; us-gaap:CommonClassAMember.

> Source: V/earnings_release.txt L250; statement column; 0001403161-26-000126

**quarter.annual release gaap diluted eps** [C036]: **12.32 USD/shares**. Period: full fiscal year ended 2026-09-30. Definition: Third numeric column; full fiscal year ended 2026-09-30; GAAP diluted EPS; us-gaap:CommonClassAMember.

> Source: V/earnings_release.txt L250; statement column; 0001403161-26-000126

**quarter.revenue growth** [C037]: **13.19 %**. Period: 2026-09-30. Definition: Current quarter revenue / same quarter prior-year revenue minus one, nominal percent.; inputs: V.quarter.quarter_net_revenue=12,139,000,000.00, V.quarter.prior_quarter_net_revenue=10,724,000,000.00.

> Source: (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; statement column; 0001403161-26-000126; V/earnings_release.txt L212; statement column; 0001403161-26-000126

**Corrected sourced metric: V.ratio.free_cash_flow** [I038]: **21,577,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Operating cash flow less reported property, equipment and technology purchases as applicable.; inputs: V.fact.operating_cash_flow=23,059,000,000.00, V.fact.capex=1,482,000,000.00.

> Source: 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089

## Future Developments and Strategic Recommendations

Visa plans to deepen its fraud‑prevention capabilities through the acquisition of BioCatch, a behavioral‑first fraud intelligence firm, which is expected to close in the next fiscal year. [source:E:L68] Ongoing investments in the Visa Acceptance Platform, including cloud‑based solutions such as Cybersource and Authorize.net, aim to enhance omnichannel commerce and reduce merchant fraud costs. [source:K:L309] The company also highlights the importance of managing client incentives and monitoring litigation provisions, which can materially affect earnings. [source:Q:L1444] Strategic focus should remain on expanding digital and tokenized payment offerings, strengthening cross‑border services, and proactively addressing regulatory and competitive pressures to protect revenue streams.

**Insight: Visa delivers a high return on equity, indicating strong profitability relative to its capital base.** [I039]: **52.07 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP net income / average beginning and ending reported equity, percent.; inputs: V.fact.net_income=20,058,000,000.00, V.fact.prior_equity=39,137,000,000.00, V.fact.equity=37,909,000,000.00.

> Source: 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

## Investment Recommendation

<!-- thesis-start -->
Buy. Visa’s durable network position and strong cash generation support a positive stance, but regulatory scrutiny and emerging competitive threats warrant vigilance. The high return on equity underscores efficient capital use, while moderate leverage and robust free cash flow provide financial flexibility. Continued investment in digital and tokenized services is essential to sustain growth amid evolving market dynamics.
<!-- thesis-end -->

**Advisor deciding metric, quoted from the analyst output** [D040]: **52.07 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP net income / average beginning and ending reported equity, percent.; inputs: V.fact.net_income=20,058,000,000.00, V.fact.prior_equity=39,137,000,000.00, V.fact.equity=37,909,000,000.00.

> Source: 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089

**Insight: Operating margin is high, reflecting strong profitability relative to revenue.** [I041]: **59.98 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: V.fact.operating_income=23,994,000,000.00, V.fact.revenue=40,000,000,000.00.

> Source: 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089

### Review record

Human findings, both partner checks and student persona authorship remain pending.