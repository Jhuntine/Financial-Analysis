VISA INC. (V); filings read: V 10-K 0001403161-25-000089; V 10-Q 0001403161-26-000104; V earnings 0001403161-26-000126; MA 10-K 0001141391-26-000013; PYPL 10-K 0001633917-26-000024
Run UTC: 2026-11-05T19:42:29.536148+00:00; mode=offline_fixture; manager_approved=True; human review pending.

> Offline software fixture: analyst prose is scaffolding; no model calls were made.

## Overview

The filing states "Visa is one of the world’s leaders" [source:K:L151]. This recorded disclosure frames the operating model; the fixture adds no forecast.

## Market Positioning and Growth Outlook

The filing states "The global payments industry continues to undergo" [source:K:L382]. Growth should be evaluated alongside the disclosed competitive risks.

## Valuation Insights

Read GAAP margins, average-equity returns, debt including current maturities and cash generation using the explicit definitions below. The annual-filing P/E uses a dated close and an older filed earnings denominator. It is not a current TTM multiple. Peer fiscal calendars, revenue definitions and business models differ. Quarter and annual-release columns are kept separate.

### Financial Analyst evidence

```claim
{"id": "C001", "text": "fact.revenue", "value": 40000000000.0, "unit": "USD", "source": "V.fact.revenue", "period": "2024-10-01 to 2025-09-30", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C002", "text": "fact.operating income", "value": 23994000000.0, "unit": "USD", "source": "V.fact.operating_income", "period": "2024-10-01 to 2025-09-30", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C003", "text": "fact.net income", "value": 20058000000.0, "unit": "USD", "source": "V.fact.net_income", "period": "2024-10-01 to 2025-09-30", "definition": "GAAP consolidated net income; use the equity scope identified in the source tag.", "inputs": []}
```

```claim
{"id": "C004", "text": "fact.diluted eps", "value": 11.2, "unit": "USD/shares", "source": "V.fact.diluted_eps", "period": "2024-10-01 to 2025-09-30", "definition": "GAAP diluted EPS for the listed common share class; consolidated fact if unambiguous.", "inputs": []}
```

```claim
{"id": "C005", "text": "fact.equity", "value": 37909000000.0, "unit": "USD", "source": "V.fact.equity", "period": "2025-09-30", "definition": "Reported consolidated stockholders' equity; scope is identified by the selected tag.", "inputs": []}
```

```claim
{"id": "C006", "text": "fact.long term debt", "value": 19602000000.0, "unit": "USD", "source": "V.fact.long_term_debt", "period": "2025-09-30", "definition": "Carrying amount of long-term debt excluding its current portion; excludes operating leases.", "inputs": []}
```

```claim
{"id": "C007", "text": "fact.current debt", "value": 5569000000.0, "unit": "USD", "source": "V.fact.current_debt", "period": "2025-09-30", "definition": "Current portion of long-term debt; excludes unrelated short-term borrowings.", "inputs": []}
```

```claim
{"id": "C008", "text": "fact.operating cash flow", "value": 23059000000.0, "unit": "USD", "source": "V.fact.operating_cash_flow", "period": "2024-10-01 to 2025-09-30", "definition": "Reported net cash provided by operating activities.", "inputs": []}
```

```claim
{"id": "C009", "text": "fact.capex", "value": 1482000000.0, "unit": "USD", "source": "V.fact.capex", "period": "2024-10-01 to 2025-09-30", "definition": "Cash purchases of property/equipment (and technology if the reported row includes it); positive outflow.", "inputs": []}
```

```claim
{"id": "C010", "text": "fact.prior revenue", "value": 35926000000.0, "unit": "USD", "source": "V.fact.prior_revenue", "period": "2023-10-01 to 2024-09-30", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C011", "text": "fact.prior equity", "value": 39137000000.0, "unit": "USD", "source": "V.fact.prior_equity", "period": "2024-09-30", "definition": "Reported consolidated stockholders' equity; scope is identified by the selected tag.", "inputs": []}
```

```claim
{"id": "C012", "text": "ratio.revenue growth", "value": 11.339976618604908, "unit": "%", "source": "V.ratio.revenue_growth", "period": "2024-10-01 to 2025-09-30", "definition": "Same-definition annual revenue / prior annual revenue minus one, percent.", "inputs": [{"source": "V.fact.revenue", "value": 40000000000.0}, {"source": "V.fact.prior_revenue", "value": 35926000000.0}]}
```

```claim
{"id": "C013", "text": "ratio.operating margin", "value": 59.985, "unit": "%", "source": "V.ratio.operating_margin", "period": "2024-10-01 to 2025-09-30", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "V.fact.operating_income", "value": 23994000000.0}, {"source": "V.fact.revenue", "value": 40000000000.0}]}
```

```claim
{"id": "C014", "text": "ratio.return on average equity", "value": 52.06759598162137, "unit": "%", "source": "V.ratio.return_on_average_equity", "period": "2024-10-01 to 2025-09-30", "definition": "GAAP net income / average beginning and ending reported equity, percent.", "inputs": [{"source": "V.fact.net_income", "value": 20058000000.0}, {"source": "V.fact.prior_equity", "value": 39137000000.0}, {"source": "V.fact.equity", "value": 37909000000.0}]}
```

```claim
{"id": "C015", "text": "ratio.debt to equity", "value": 0.6639848057189586, "unit": "x", "source": "V.ratio.debt_to_equity", "period": "2024-10-01 to 2025-09-30", "definition": "Long-term debt including its current portion / ending reported equity.", "inputs": [{"source": "V.fact.long_term_debt", "value": 19602000000.0}, {"source": "V.fact.current_debt", "value": 5569000000.0}, {"source": "V.fact.equity", "value": 37909000000.0}]}
```

```claim
{"id": "C016", "text": "ratio.free cash flow", "value": 21577000000.0, "unit": "USD", "source": "V.ratio.free_cash_flow", "period": "2024-10-01 to 2025-09-30", "definition": "Operating cash flow less reported property, equipment and technology purchases as applicable.", "inputs": [{"source": "V.fact.operating_cash_flow", "value": 23059000000.0}, {"source": "V.fact.capex", "value": 1482000000.0}]}
```

```claim
{"id": "C017", "text": "ratio.price earnings", "value": 39.39803921568628, "unit": "x", "source": "V.ratio.price_earnings", "period": "2024-10-01 to 2025-09-30", "definition": "Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.", "inputs": [{"source": "V.price", "value": 401.86}, {"source": "V.fact.diluted_eps", "value": 10.2}]}
```

```claim
{"id": "C018", "text": "fact.revenue", "value": 32791000000.0, "unit": "USD", "source": "MA.fact.revenue", "period": "2025-01-01 to 2025-12-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C019", "text": "fact.operating income", "value": 18897000000.0, "unit": "USD", "source": "MA.fact.operating_income", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C020", "text": "ratio.operating margin", "value": 57.62861760849013, "unit": "%", "source": "MA.ratio.operating_margin", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "MA.fact.operating_income", "value": 18897000000.0}, {"source": "MA.fact.revenue", "value": 32791000000.0}]}
```

```claim
{"id": "C021", "text": "fact.revenue", "value": 33172000000.0, "unit": "USD", "source": "PYPL.fact.revenue", "period": "2025-01-01 to 2025-12-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C022", "text": "fact.operating income", "value": 6065000000.0, "unit": "USD", "source": "PYPL.fact.operating_income", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C023", "text": "ratio.operating margin", "value": 18.28349210177258, "unit": "%", "source": "PYPL.ratio.operating_margin", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "PYPL.fact.operating_income", "value": 6065000000.0}, {"source": "PYPL.fact.revenue", "value": 33172000000.0}]}
```

```claim
{"id": "C024", "text": "price", "value": 401.86, "unit": "USD/shares", "source": "V.price", "period": "2026-10-27", "definition": "LSEG Historical Pricing; V.N; TRDPRC_1; daily close; 2026-10-27; unadjusted", "inputs": []}
```

```claim
{"id": "C025", "text": "quarter.quarter net revenue", "value": 12139000000.0, "unit": "USD", "source": "V.quarter.quarter_net_revenue", "period": "three months ended 2026-09-30", "definition": "First quarter column; three months ended 2026-09-30; source in millions", "inputs": []}
```

```claim
{"id": "C026", "text": "quarter.prior quarter net revenue", "value": 10724000000.0, "unit": "USD", "source": "V.quarter.prior_quarter_net_revenue", "period": "same quarter of prior year relative to 2026-09-30", "definition": "Second quarter column; same quarter of prior year; source in millions", "inputs": []}
```

```claim
{"id": "C027", "text": "quarter.quarter gaap diluted eps", "value": 3.19, "unit": "USD/shares", "source": "V.quarter.quarter_gaap_diluted_eps", "period": "three months ended 2026-09-30", "definition": "First quarter column, GAAP diluted EPS; us-gaap:CommonClassAMember", "inputs": []}
```

```claim
{"id": "C028", "text": "quarter.annual release gaap diluted eps", "value": 12.32, "unit": "USD/shares", "source": "V.quarter.annual_release_gaap_diluted_eps", "period": "twelve months ended 2026-09-30", "definition": "Third numeric column; twelve months ended 2026-09-30; us-gaap:CommonClassAMember", "inputs": []}
```

```claim
{"id": "C029", "text": "quarter.revenue growth", "value": 13.194703468854897, "unit": "%", "source": "V.quarter.revenue_growth", "period": "2026-09-30", "definition": "Current quarter revenue / same quarter prior-year revenue minus one, nominal percent.", "inputs": [{"source": "V.quarter.quarter_net_revenue", "value": 12139000000.0}, {"source": "V.quarter.prior_quarter_net_revenue", "value": 10724000000.0}]}
```

```claim
{"id": "I030", "text": "Insight: Cash remaining after the disclosed capital outflow is a separate constraint on the earnings narrative.", "value": 21577000000.0, "unit": "USD", "source": "V.ratio.free_cash_flow", "period": "2024-10-01 to 2025-09-30", "definition": "Operating cash flow less reported property, equipment and technology purchases as applicable.", "inputs": [{"source": "V.fact.operating_cash_flow", "value": 23059000000.0}, {"source": "V.fact.capex", "value": 1482000000.0}]}
```

## Future Developments and Strategic Recommendations

The filing states "Visa’s strategy is to accelerate revenue growth" [source:K:L214]. Monitor whether subsequent disclosures support the stated strategy; this is an interpretation for human review.

```claim
{"id": "I031", "text": "Insight: Historical operating economics provide a separate test of the growth narrative.", "value": 59.985, "unit": "%", "source": "V.ratio.operating_margin", "period": "2024-10-01 to 2025-09-30", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "V.fact.operating_income", "value": 23994000000.0}, {"source": "V.fact.revenue", "value": 40000000000.0}]}
```

## Investment Recommendation

<!-- thesis-start -->
Hold. Hold is the inherited demonstration judgment pending a current valuation and human review. The live advisor must synthesize only the two analyst outputs and choose its own deciding metric.
<!-- thesis-end -->

```claim
{"id": "D032", "text": "Advisor deciding metric, quoted from the analyst output", "value": 39.39803921568628, "unit": "x", "source": "V.ratio.price_earnings", "period": "2024-10-01 to 2025-09-30", "definition": "Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.", "inputs": [{"source": "V.price", "value": 401.86}, {"source": "V.fact.diluted_eps", "value": 10.2}]}
```

```claim
{"id": "I033", "text": "Insight: The valuation uses the filed annual earnings base, so its denominator deserves separate review.", "value": 39.39803921568628, "unit": "x", "source": "V.ratio.price_earnings", "period": "2024-10-01 to 2025-09-30", "definition": "Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.", "inputs": [{"source": "V.price", "value": 401.86}, {"source": "V.fact.diluted_eps", "value": 10.2}]}
```

### Review record

Human findings, both partner checks and student persona authorship remain pending.
