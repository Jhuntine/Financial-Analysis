Mastercard Inc; annual source: 0001141391-26-000013
Annual-only technical test; no partner review or full agent run claimed.

```claim
{"id": "A000", "text": "fact.revenue", "value": 32791000000.0, "source": "MA.fact.revenue", "unit": "USD", "period": "2025-01-01 to 2025-12-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "A001", "text": "fact.operating_income", "value": 18897000000.0, "source": "MA.fact.operating_income", "unit": "USD", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "A002", "text": "fact.net_income", "value": 14968000000.0, "source": "MA.fact.net_income", "unit": "USD", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP consolidated net income; use the equity scope identified in the source tag.", "inputs": []}
```

```claim
{"id": "A003", "text": "fact.diluted_eps", "value": 16.52, "source": "MA.fact.diluted_eps", "unit": "USD/shares", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP diluted EPS for the listed common share class; consolidated fact if unambiguous.", "inputs": []}
```

```claim
{"id": "A004", "text": "fact.equity", "value": 7737000000.0, "source": "MA.fact.equity", "unit": "USD", "period": "2025-12-31", "definition": "Reported consolidated stockholders' equity; scope is identified by the selected tag.", "inputs": []}
```

```claim
{"id": "A005", "text": "fact.long_term_debt", "value": 18251000000.0, "source": "MA.fact.long_term_debt", "unit": "USD", "period": "2025-12-31", "definition": "Carrying amount of long-term debt excluding its current portion; excludes operating leases.", "inputs": []}
```

```claim
{"id": "A006", "text": "fact.current_debt", "value": 749000000.0, "source": "MA.fact.current_debt", "unit": "USD", "period": "2025-12-31", "definition": "Current portion of long-term debt; excludes unrelated short-term borrowings.", "inputs": []}
```

```claim
{"id": "A007", "text": "fact.operating_cash_flow", "value": 17648000000.0, "source": "MA.fact.operating_cash_flow", "unit": "USD", "period": "2025-01-01 to 2025-12-31", "definition": "Reported net cash provided by operating activities.", "inputs": []}
```

```claim
{"id": "A008", "text": "fact.capex", "value": 489000000.0, "source": "MA.fact.capex", "unit": "USD", "period": "2025-01-01 to 2025-12-31", "definition": "Cash purchases of property/equipment (and technology if the reported row includes it); positive outflow.", "inputs": []}
```

```claim
{"id": "A009", "text": "fact.prior_revenue", "value": 28167000000.0, "source": "MA.fact.prior_revenue", "unit": "USD", "period": "2024-01-01 to 2024-12-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "A010", "text": "fact.prior_equity", "value": 6485000000.0, "source": "MA.fact.prior_equity", "unit": "USD", "period": "2024-12-31", "definition": "Reported consolidated stockholders' equity; scope is identified by the selected tag.", "inputs": []}
```

```claim
{"id": "A011", "text": "ratio.revenue_growth", "value": 16.4163737707246, "source": "MA.ratio.revenue_growth", "unit": "%", "period": "2025-01-01 to 2025-12-31", "definition": "Same-definition annual revenue / prior annual revenue minus one, percent.", "inputs": [{"source": "MA.fact.revenue", "value": 32791000000.0}, {"source": "MA.fact.prior_revenue", "value": 28167000000.0}]}
```

```claim
{"id": "A012", "text": "ratio.operating_margin", "value": 57.62861760849013, "source": "MA.ratio.operating_margin", "unit": "%", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "MA.fact.operating_income", "value": 18897000000.0}, {"source": "MA.fact.revenue", "value": 32791000000.0}]}
```

```claim
{"id": "A013", "text": "ratio.return_on_average_equity", "value": 210.49078891857684, "source": "MA.ratio.return_on_average_equity", "unit": "%", "period": "2025-01-01 to 2025-12-31", "definition": "GAAP net income / average beginning and ending reported equity, percent.", "inputs": [{"source": "MA.fact.net_income", "value": 14968000000.0}, {"source": "MA.fact.prior_equity", "value": 6485000000.0}, {"source": "MA.fact.equity", "value": 7737000000.0}]}
```

```claim
{"id": "A014", "text": "ratio.debt_to_equity", "value": 2.455732195941579, "source": "MA.ratio.debt_to_equity", "unit": "x", "period": "2025-01-01 to 2025-12-31", "definition": "Long-term debt including its current portion / ending reported equity.", "inputs": [{"source": "MA.fact.long_term_debt", "value": 18251000000.0}, {"source": "MA.fact.current_debt", "value": 749000000.0}, {"source": "MA.fact.equity", "value": 7737000000.0}]}
```

```claim
{"id": "A015", "text": "ratio.free_cash_flow", "value": 17159000000.0, "source": "MA.ratio.free_cash_flow", "unit": "USD", "period": "2025-01-01 to 2025-12-31", "definition": "Operating cash flow less reported property, equipment and technology purchases as applicable.", "inputs": [{"source": "MA.fact.operating_cash_flow", "value": 17648000000.0}, {"source": "MA.fact.capex", "value": 489000000.0}]}
```

