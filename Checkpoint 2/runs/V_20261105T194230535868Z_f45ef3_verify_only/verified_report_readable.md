VISA INC. (V); filings read: V 10-K 0001403161-25-000089; V 10-Q 0001403161-26-000104; V earnings 0001403161-26-000126; MA 10-K 0001141391-26-000013; PYPL 10-K 0001633917-26-000024

> Verifier: CODE ONLY; semantic model check NOT RUN. Marks refer to the original report. Human review pending.

| Claim | Mark | Reported | Corrected | Evidence / reason |
|---|---|---:|---:|---|
| C001 | correct | 40000000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C002 | correct | 23994000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 / |
| C003 | correct | 20058000000.0 |  | Exact source context and rounded value match. V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / / |
| C004 | correct | 10.2 |  | Exact source context and rounded value match. V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| C005 | correct | 37909000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C006 | correct | 19602000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 / |
| C007 | correct | 5569000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — / |
| C008 | correct | 23059000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 / |
| C009 | correct | 1482000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| C010 | correct | 35926000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C011 | correct | 39137000000.0 |  | Exact source context and rounded value match. V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C012 | correct | 11.339976618604908 |  | Exact source context and rounded value match. (40,000,000,000 / 35,926,000,000 - 1) * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2023-10-01 to 2024-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C013 | correct | 59.985 |  | Exact source context and rounded value match. 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| C014 | correct | 52.06759598162137 |  | Exact source context and rounded value match. 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net income / $ / 20,058 / / / / / / / / / / /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2024-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C015 | correct | 0.6639848057189586 |  | Exact source context and rounded value match. (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 2025-09-30; 0001403161-25-000089; Long-term debt / 19,602 / / / 20,836 /; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 2025-09-30; 0001403161-25-000089; Current maturities of debt / 5,569 / / / — /; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 2025-09-30; 0001403161-25-000089; Total equity / 37,909 / / / 39,137 / |
| C016 | correct | 21577000000.0 |  | Exact source context and rounded value match. 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 /; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| C017 | correct | 39.39803921568628 |  | Exact source context and rounded value match. 401.86 / 10.20; market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| C018 | correct | 32791000000.0 |  | Exact source context and rounded value match. MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Net Revenue / / $ / 32,791 / / / $ / 28,167 / / / $ / 25,098 / |
| C019 | correct | 18897000000.0 |  | Exact source context and rounded value match. MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Operating income / / 18,897 / / / 15,582 / / / 14,008 / |
| C020 | correct | 57.62861760849013 |  | Exact source context and rounded value match. 18,897,000,000 / 32,791,000,000 * 100; MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Operating income / / 18,897 / / / 15,582 / / / 14,008 /; MA/10-K.txt L1779; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001141391-26-000013; Net Revenue / / $ / 32,791 / / / $ / 28,167 / / / $ / 25,098 / |
| C021 | correct | 33172000000.0 |  | Exact source context and rounded value match. PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Net revenues / $ / 33,172 / / / $ / 31,797 / / / $ / 29,771 / |
| C022 | correct | 6065000000.0 |  | Exact source context and rounded value match. PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Operating income / 6,065 / / / 5,325 / / / 5,028 / |
| C023 | correct | 18.28349210177258 |  | Exact source context and rounded value match. 6,065,000,000 / 33,172,000,000 * 100; PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Operating income / 6,065 / / / 5,325 / / / 5,028 /; PYPL/10-K.txt L1212; us-gaap:Revenues; 2025-01-01 to 2025-12-31; 0001633917-26-000024; Net revenues / $ / 33,172 / / / $ / 31,797 / / / $ / 29,771 / |
| C024 | correct | 401.86 |  | Exact source context and rounded value match. market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted |
| C025 | correct | 12139000000.0 |  | Exact source context and rounded value match. V/earnings_release.txt L212; statement column; three months ended 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| C026 | correct | 10724000000.0 |  | Exact source context and rounded value match. V/earnings_release.txt L212; statement column; same quarter of prior year relative to 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| C027 | correct | 3.19 |  | Exact source context and rounded value match. V/earnings_release.txt L250; statement column; three months ended 2026-09-30; 0001403161-26-000126; Class A common stock / $ / 3.19 / / / $ / 2.62 / / / $ / 12.32 / / / $ / 10.20 / |
| C028 | correct | 12.32 |  | Exact source context and rounded value match. V/earnings_release.txt L250; statement column; twelve months ended 2026-09-30; 0001403161-26-000126; Class A common stock / $ / 3.19 / / / $ / 2.62 / / / $ / 12.32 / / / $ / 10.20 / |
| C029 | correct | 13.194703468854897 |  | Exact source context and rounded value match. (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; statement column; three months ended 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 /; V/earnings_release.txt L212; statement column; same quarter of prior year relative to 2026-09-30; 0001403161-26-000126; Net revenue / $ / 12,139 / / / $ / 10,724 / / / $ / 45,903 / / / $ / 40,000 / |
| I030 | correct | 21577000000.0 |  | Exact source context and rounded value match. 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net cash provided by (used in) operating activities / 23,059 / / / 19,950 / / / 20,755 /; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Purchases of property, equipment and technology / ( 1,482 ) / / / ( 1,257 ) / / / ( 1,059 ) / |
| I031 | correct | 59.985 |  | Exact source context and rounded value match. 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Operating income / 23,994 / / / 23,595 / / / 21,000 /; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Net revenue / $ / 40,000 / / / $ / 35,926 / / / $ / 32,653 / |
| D032 | correct | 39.39803921568628 |  | Exact source context and rounded value match. 401.86 / 10.20; market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |
| I033 | correct | 39.39803921568628 |  | Exact source context and rounded value match. 401.86 / 10.20; market_input.json; 2026-10-27; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 2024-10-01 to 2025-09-30; 0001403161-25-000089; Class A common stock / $ / 10.20 / / / $ / 9.73 / / / $ / 8.28 / |

Run UTC: 2026-11-05T19:42:29.536148+00:00; mode=offline_fixture; manager_approved=True; human review pending.

> Offline software fixture: analyst prose is scaffolding; no model calls were made.

## Overview

The filing states "Visa is one of the world’s leaders" [source:K:L151]. This recorded disclosure frames the operating model; the fixture adds no forecast.

## Market Positioning and Growth Outlook

The filing states "The global payments industry continues to undergo" [source:K:L382]. Growth should be evaluated alongside the disclosed competitive risks.

## Valuation Insights

Read GAAP margins, average-equity returns, debt including current maturities and cash generation using the explicit definitions below. The annual-filing P/E uses a dated close and an older filed earnings denominator. It is not a current TTM multiple. Peer fiscal calendars, revenue definitions and business models differ. Quarter and annual-release columns are kept separate.

### Financial Analyst evidence

**fact.revenue** [C001]: **40,000,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Consolidated reported revenue; the source row names any net/gross convention..

<small>Source: V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089</small>

**fact.operating income** [C002]: **23,994,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP consolidated operating income, including litigation and other reported operating costs..

<small>Source: V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089</small>

**fact.net income** [C003]: **20,058,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP consolidated net income; use the equity scope identified in the source tag..

<small>Source: V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089</small>

**fact.diluted eps** [C004]: **10.20 USD/shares**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP diluted EPS for the listed common share class; consolidated fact if unambiguous..

<small>Source: V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089</small>

**fact.equity** [C005]: **37,909,000,000.00 USD**. Period: 2025-09-30. Definition: Reported consolidated stockholders' equity; scope is identified by the selected tag..

<small>Source: V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089</small>

**fact.long term debt** [C006]: **19,602,000,000.00 USD**. Period: 2025-09-30. Definition: Carrying amount of long-term debt excluding its current portion; excludes operating leases..

<small>Source: V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 0001403161-25-000089</small>

**fact.current debt** [C007]: **5,569,000,000.00 USD**. Period: 2025-09-30. Definition: Current portion of long-term debt; excludes unrelated short-term borrowings..

<small>Source: V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 0001403161-25-000089</small>

**fact.operating cash flow** [C008]: **23,059,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Reported net cash provided by operating activities..

<small>Source: V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089</small>

**fact.capex** [C009]: **1,482,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Cash purchases of property/equipment (and technology if the reported row includes it); positive outflow..

<small>Source: V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089</small>

**fact.prior revenue** [C010]: **35,926,000,000.00 USD**. Period: 2023-10-01 to 2024-09-30. Definition: Consolidated reported revenue; the source row names any net/gross convention..

<small>Source: V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089</small>

**fact.prior equity** [C011]: **39,137,000,000.00 USD**. Period: 2024-09-30. Definition: Reported consolidated stockholders' equity; scope is identified by the selected tag..

<small>Source: V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089</small>

**ratio.revenue growth** [C012]: **11.34 %**. Period: 2024-10-01 to 2025-09-30. Definition: Same-definition annual revenue / prior annual revenue minus one, percent.; inputs: V.fact.revenue=40,000,000,000.00, V.fact.prior_revenue=35,926,000,000.00.

<small>Source: (40,000,000,000 / 35,926,000,000 - 1) * 100; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089</small>

**ratio.operating margin** [C013]: **59.98 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: V.fact.operating_income=23,994,000,000.00, V.fact.revenue=40,000,000,000.00.

<small>Source: 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089</small>

**ratio.return on average equity** [C014]: **52.07 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP net income / average beginning and ending reported equity, percent.; inputs: V.fact.net_income=20,058,000,000.00, V.fact.prior_equity=39,137,000,000.00, V.fact.equity=37,909,000,000.00.

<small>Source: 20,058,000,000 / ((39,137,000,000 + 37,909,000,000) / 2) * 100; V/10-K.txt L2877; us-gaap:NetIncomeLoss; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089</small>

**ratio.debt to equity** [C015]: **0.66 x**. Period: 2024-10-01 to 2025-09-30. Definition: Long-term debt including its current portion / ending reported equity.; inputs: V.fact.long_term_debt=19,602,000,000.00, V.fact.current_debt=5,569,000,000.00, V.fact.equity=37,909,000,000.00.

<small>Source: (19,602,000,000 + 5,569,000,000) / 37,909,000,000; V/10-K.txt L1516; us-gaap:LongTermDebtNoncurrent; 0001403161-25-000089; V/10-K.txt L1513; us-gaap:LongTermDebtCurrent; 0001403161-25-000089; V/10-K.txt L1539; us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; 0001403161-25-000089</small>

**ratio.free cash flow** [C016]: **21,577,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Operating cash flow less reported property, equipment and technology purchases as applicable.; inputs: V.fact.operating_cash_flow=23,059,000,000.00, V.fact.capex=1,482,000,000.00.

<small>Source: 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089</small>

**ratio.price earnings** [C017]: **39.40 x**. Period: 2024-10-01 to 2025-09-30. Definition: Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.; inputs: V.price=401.86, V.fact.diluted_eps=10.20.

<small>Source: 401.86 / 10.20; market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089</small>

**fact.revenue** [C018]: **32,791,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: Consolidated reported revenue; the source row names any net/gross convention..

<small>Source: MA/10-K.txt L1779; us-gaap:Revenues; 0001141391-26-000013</small>

**fact.operating income** [C019]: **18,897,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP consolidated operating income, including litigation and other reported operating costs..

<small>Source: MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 0001141391-26-000013</small>

**ratio.operating margin** [C020]: **57.63 %**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: MA.fact.operating_income=18,897,000,000.00, MA.fact.revenue=32,791,000,000.00.

<small>Source: 18,897,000,000 / 32,791,000,000 * 100; MA/10-K.txt L1786; us-gaap:OperatingIncomeLoss; 0001141391-26-000013; MA/10-K.txt L1779; us-gaap:Revenues; 0001141391-26-000013</small>

**fact.revenue** [C021]: **33,172,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: Consolidated reported revenue; the source row names any net/gross convention..

<small>Source: PYPL/10-K.txt L1212; us-gaap:Revenues; 0001633917-26-000024</small>

**fact.operating income** [C022]: **6,065,000,000.00 USD**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP consolidated operating income, including litigation and other reported operating costs..

<small>Source: PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 0001633917-26-000024</small>

**ratio.operating margin** [C023]: **18.28 %**. Period: 2025-01-01 to 2025-12-31. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: PYPL.fact.operating_income=6,065,000,000.00, PYPL.fact.revenue=33,172,000,000.00.

<small>Source: 6,065,000,000 / 33,172,000,000 * 100; PYPL/10-K.txt L1222; us-gaap:OperatingIncomeLoss; 0001633917-26-000024; PYPL/10-K.txt L1212; us-gaap:Revenues; 0001633917-26-000024</small>

**price** [C024]: **401.86 USD/shares**. Period: 2026-10-27. Definition: LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted.

<small>Source: market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted</small>

**quarter.quarter net revenue** [C025]: **12,139,000,000.00 USD**. Period: three months ended 2026-09-30. Definition: First quarter column; three months ended 2026-09-30; source in millions.

<small>Source: V/earnings_release.txt L212; statement column; 0001403161-26-000126</small>

**quarter.prior quarter net revenue** [C026]: **10,724,000,000.00 USD**. Period: same quarter of prior year relative to 2026-09-30. Definition: Second quarter column; same quarter of prior year; source in millions.

<small>Source: V/earnings_release.txt L212; statement column; 0001403161-26-000126</small>

**quarter.quarter gaap diluted eps** [C027]: **3.19 USD/shares**. Period: three months ended 2026-09-30. Definition: First quarter column, GAAP diluted EPS; us-gaap:CommonClassAMember.

<small>Source: V/earnings_release.txt L250; statement column; 0001403161-26-000126</small>

**quarter.annual release gaap diluted eps** [C028]: **12.32 USD/shares**. Period: twelve months ended 2026-09-30. Definition: Third numeric column; twelve months ended 2026-09-30; us-gaap:CommonClassAMember.

<small>Source: V/earnings_release.txt L250; statement column; 0001403161-26-000126</small>

**quarter.revenue growth** [C029]: **13.19 %**. Period: 2026-09-30. Definition: Current quarter revenue / same quarter prior-year revenue minus one, nominal percent.; inputs: V.quarter.quarter_net_revenue=12,139,000,000.00, V.quarter.prior_quarter_net_revenue=10,724,000,000.00.

<small>Source: (12,139,000,000 / 10,724,000,000 - 1) * 100; V/earnings_release.txt L212; statement column; 0001403161-26-000126; V/earnings_release.txt L212; statement column; 0001403161-26-000126</small>

**Insight: Cash remaining after the disclosed capital outflow is a separate constraint on the earnings narrative.** [I030]: **21,577,000,000.00 USD**. Period: 2024-10-01 to 2025-09-30. Definition: Operating cash flow less reported property, equipment and technology purchases as applicable.; inputs: V.fact.operating_cash_flow=23,059,000,000.00, V.fact.capex=1,482,000,000.00.

<small>Source: 23,059,000,000 - 1,482,000,000; V/10-K.txt L1775; us-gaap:NetCashProvidedByUsedInOperatingActivities; 0001403161-25-000089; V/10-K.txt L1777; us-gaap:PaymentsToAcquireProductiveAssets; 0001403161-25-000089</small>

## Future Developments and Strategic Recommendations

The filing states "Visa’s strategy is to accelerate revenue growth" [source:K:L214]. Monitor whether subsequent disclosures support the stated strategy; this is an interpretation for human review.

**Insight: Historical operating economics provide a separate test of the growth narrative.** [I031]: **59.98 %**. Period: 2024-10-01 to 2025-09-30. Definition: GAAP operating income / consolidated reported revenue, percent.; inputs: V.fact.operating_income=23,994,000,000.00, V.fact.revenue=40,000,000,000.00.

<small>Source: 23,994,000,000 / 40,000,000,000 * 100; V/10-K.txt L1567; us-gaap:OperatingIncomeLoss; 0001403161-25-000089; V/10-K.txt L1556; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; 0001403161-25-000089</small>

## Investment Recommendation

<!-- thesis-start -->
Hold. Hold is the inherited demonstration judgment pending a current valuation and human review. The live advisor must synthesize only the two analyst outputs and choose its own deciding metric.
<!-- thesis-end -->

**Advisor deciding metric, quoted from the analyst output** [D032]: **39.40 x**. Period: 2024-10-01 to 2025-09-30. Definition: Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.; inputs: V.price=401.86, V.fact.diluted_eps=10.20.

<small>Source: 401.86 / 10.20; market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089</small>

**Insight: The valuation uses the filed annual earnings base, so its denominator deserves separate review.** [I033]: **39.40 x**. Period: 2024-10-01 to 2025-09-30. Definition: Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.; inputs: V.price=401.86, V.fact.diluted_eps=10.20.

<small>Source: 401.86 / 10.20; market_input.json; LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted; V/10-K.txt L1590; us-gaap:EarningsPerShareDiluted; 0001403161-25-000089</small>

### Review record

Human findings, both partner checks and student persona authorship remain pending.