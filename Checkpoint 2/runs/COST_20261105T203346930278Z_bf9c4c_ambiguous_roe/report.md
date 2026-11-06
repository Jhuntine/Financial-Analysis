COSTCO WHOLESALE CORP /NEW (COST); filings read: COST 10-K 0000909832-26-000093; COST 10-Q 0000909832-26-000051; COST earnings 0000909832-26-000084; WMT 10-K 0000104169-26-000055; TGT 10-K 0000027419-26-000016; BJ 10-K 0001531152-26-000007
Run UTC: 2026-11-05T20:28:12.527505+00:00; mode=live; manager_approved=True; human review pending.

> Live agent draft; human approval pending.

## Overview

Costco operates membership warehouses and e‑commerce sites that focus on low prices for a limited selection of nationally‑branded and private‑label products, driving high sales volumes and rapid inventory turnover. This model leverages volume purchasing, efficient distribution and reduced handling in no‑frills, self‑service facilities, allowing profitability at lower gross margins than most retailers. The company emphasizes employee career development, competitive compensation and a high full‑time employee ratio, contributing to a notably high retention rate. However, the firm acknowledges risks in executing its growth strategy, including market expansion and acquisition integration, as well as the need to protect personal and business information against evolving privacy and security threats.

## Market Positioning and Growth Outlook

Costco’s low‑price, high‑volume approach creates strong member loyalty and pricing authority, supporting consistent sales growth across the United States, Canada and other international markets. The ability to sell inventory before payment, combined with early‑payment discounts, enhances cash efficiency. Employee retention and productivity further reinforce operational resilience. While the company reported revenue growth for the fiscal year, it also faces competitive pressures that may require pricing adjustments or promotional investments, potentially impacting gross margins. Ongoing litigation and regulatory exposures present additional uncertainty.

## Valuation Insights

Costco delivers a modest operating margin that, while lower than peers, is supported by a high return on average equity, indicating efficient use of capital. Its debt‑to‑equity ratio remains low, reflecting a conservative financing profile. Free cash flow after capex is sizable, underscoring strong cash generation, and the annual‑filing price‑to‑earnings multiple is elevated relative to the broader market, suggesting a premium valuation. These elements together point to a financially robust business with disciplined capital structure and cash conversion.

### Financial Analyst evidence

```claim
{"id": "C001", "text": "fact.revenue", "value": 303154000000.0, "unit": "USD", "source": "COST.fact.revenue", "period": "2025-09-01 to 2026-08-30", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C002", "text": "fact.operating income", "value": 11685000000.0, "unit": "USD", "source": "COST.fact.operating_income", "period": "2025-09-01 to 2026-08-30", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C003", "text": "fact.net income", "value": 9226000000.0, "unit": "USD", "source": "COST.fact.net_income", "period": "2025-09-01 to 2026-08-30", "definition": "GAAP consolidated net income; use the equity scope identified in the source tag.", "inputs": []}
```

```claim
{"id": "C004", "text": "fact.diluted eps", "value": 20.76, "unit": "USD/shares", "source": "COST.fact.diluted_eps", "period": "2025-09-01 to 2026-08-30", "definition": "GAAP diluted EPS for the listed common share class; consolidated fact if unambiguous.", "inputs": []}
```

```claim
{"id": "C005", "text": "fact.equity", "value": 35803000000.0, "unit": "USD", "source": "COST.fact.equity", "period": "2026-08-30", "definition": "Reported consolidated stockholders' equity; scope is identified by the selected tag.", "inputs": []}
```

```claim
{"id": "C006", "text": "fact.long term debt", "value": 3914000000.0, "unit": "USD", "source": "COST.fact.long_term_debt", "period": "2026-08-30", "definition": "Carrying amount of long-term debt excluding its current portion; excludes operating leases.", "inputs": []}
```

```claim
{"id": "C007", "text": "fact.current debt", "value": 2248000000.0, "unit": "USD", "source": "COST.fact.current_debt", "period": "2026-08-30", "definition": "Current portion of long-term debt; excludes unrelated short-term borrowings.", "inputs": []}
```

```claim
{"id": "C008", "text": "fact.operating cash flow", "value": 15817000000.0, "unit": "USD", "source": "COST.fact.operating_cash_flow", "period": "2025-09-01 to 2026-08-30", "definition": "Reported net cash provided by operating activities.", "inputs": []}
```

```claim
{"id": "C009", "text": "fact.capex", "value": 6435000000.0, "unit": "USD", "source": "COST.fact.capex", "period": "2025-09-01 to 2026-08-30", "definition": "Cash purchases of property/equipment (and technology if the reported row includes it); positive outflow.", "inputs": []}
```

```claim
{"id": "C010", "text": "fact.prior revenue", "value": 275235000000.0, "unit": "USD", "source": "COST.fact.prior_revenue", "period": "2024-09-02 to 2025-08-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C011", "text": "fact.prior equity", "value": 29164000000.0, "unit": "USD", "source": "COST.fact.prior_equity", "period": "2025-08-31", "definition": "Reported consolidated stockholders' equity; scope is identified by the selected tag.", "inputs": []}
```

```claim
{"id": "C012", "text": "ratio.revenue growth", "value": 10.143695387577889, "unit": "%", "source": "COST.ratio.revenue_growth", "period": "2025-09-01 to 2026-08-30", "definition": "Same-definition annual revenue / prior annual revenue minus one, percent.", "inputs": [{"source": "COST.fact.revenue", "value": 303154000000.0}, {"source": "COST.fact.prior_revenue", "value": 275235000000.0}]}
```

```claim
{"id": "C013", "text": "ratio.operating margin", "value": 3.8544766026507977, "unit": "%", "source": "COST.ratio.operating_margin", "period": "2025-09-01 to 2026-08-30", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "COST.fact.operating_income", "value": 11685000000.0}, {"source": "COST.fact.revenue", "value": 303154000000.0}]}
```

```claim
{"id": "C014", "text": "ratio.return on average equity", "value": 28.402111841396398, "unit": "%", "source": "COST.ratio.return_on_average_equity", "period": "2025-09-01 to 2026-08-30", "definition": "Return on equity; denominator unspecified.", "inputs": [{"source": "COST.fact.net_income", "value": 9226000000.0}, {"source": "COST.fact.prior_equity", "value": 29164000000.0}, {"source": "COST.fact.equity", "value": 35803000000.0}]}
```

```claim
{"id": "C015", "text": "ratio.debt to equity", "value": 0.17210848252939698, "unit": "x", "source": "COST.ratio.debt_to_equity", "period": "2025-09-01 to 2026-08-30", "definition": "Long-term debt including its current portion / ending reported equity.", "inputs": [{"source": "COST.fact.long_term_debt", "value": 3914000000.0}, {"source": "COST.fact.current_debt", "value": 2248000000.0}, {"source": "COST.fact.equity", "value": 35803000000.0}]}
```

```claim
{"id": "C016", "text": "ratio.free cash flow", "value": 9382000000.0, "unit": "USD", "source": "COST.ratio.free_cash_flow", "period": "2025-09-01 to 2026-08-30", "definition": "Operating cash flow less reported property, equipment and technology purchases as applicable.", "inputs": [{"source": "COST.fact.operating_cash_flow", "value": 15817000000.0}, {"source": "COST.fact.capex", "value": 6435000000.0}]}
```

```claim
{"id": "C017", "text": "ratio.price earnings", "value": 43.18304431599229, "unit": "x", "source": "COST.ratio.price_earnings", "period": "2025-09-01 to 2026-08-30", "definition": "Dated close / latest filed annual GAAP diluted EPS; annual-filing multiple, not current TTM.", "inputs": [{"source": "COST.price", "value": 896.48}, {"source": "COST.fact.diluted_eps", "value": 20.76}]}
```

```claim
{"id": "C018", "text": "fact.revenue", "value": 713163000000.0, "unit": "USD", "source": "WMT.fact.revenue", "period": "2025-02-01 to 2026-01-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C019", "text": "fact.operating income", "value": 29825000000.0, "unit": "USD", "source": "WMT.fact.operating_income", "period": "2025-02-01 to 2026-01-31", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C020", "text": "ratio.operating margin", "value": 4.182073382943311, "unit": "%", "source": "WMT.ratio.operating_margin", "period": "2025-02-01 to 2026-01-31", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "WMT.fact.operating_income", "value": 29825000000.0}, {"source": "WMT.fact.revenue", "value": 713163000000.0}]}
```

```claim
{"id": "C021", "text": "fact.revenue", "value": 104780000000.0, "unit": "USD", "source": "TGT.fact.revenue", "period": "2025-02-02 to 2026-01-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C022", "text": "fact.operating income", "value": 5117000000.0, "unit": "USD", "source": "TGT.fact.operating_income", "period": "2025-02-02 to 2026-01-31", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C023", "text": "ratio.operating margin", "value": 4.8835655659477, "unit": "%", "source": "TGT.ratio.operating_margin", "period": "2025-02-02 to 2026-01-31", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "TGT.fact.operating_income", "value": 5117000000.0}, {"source": "TGT.fact.revenue", "value": 104780000000.0}]}
```

```claim
{"id": "C024", "text": "fact.revenue", "value": 21457274000.0, "unit": "USD", "source": "BJ.fact.revenue", "period": "2025-02-02 to 2026-01-31", "definition": "Consolidated reported revenue; the source row names any net/gross convention.", "inputs": []}
```

```claim
{"id": "C025", "text": "fact.operating income", "value": 816604000.0, "unit": "USD", "source": "BJ.fact.operating_income", "period": "2025-02-02 to 2026-01-31", "definition": "GAAP consolidated operating income, including litigation and other reported operating costs.", "inputs": []}
```

```claim
{"id": "C026", "text": "ratio.operating margin", "value": 3.8057210808791457, "unit": "%", "source": "BJ.ratio.operating_margin", "period": "2025-02-02 to 2026-01-31", "definition": "GAAP operating income / consolidated reported revenue, percent.", "inputs": [{"source": "BJ.fact.operating_income", "value": 816604000.0}, {"source": "BJ.fact.revenue", "value": 21457274000.0}]}
```

```claim
{"id": "C027", "text": "price", "value": 896.48, "unit": "USD/shares", "source": "COST.price", "period": "2026-09-24", "definition": "WRDS Compustat comp.secd.prccd; primary U.S. security; dated security ticker COST; 2026-09-24", "inputs": []}
```

```claim
{"id": "C028", "text": "quarter.quarter net revenue", "value": 95723000000.0, "unit": "USD", "source": "COST.quarter.quarter_net_revenue", "period": "16 weeks ended 2026-08-30", "definition": "First quarter column; 16 weeks ended 2026-08-30; Total revenue; source in millions", "inputs": []}
```

```claim
{"id": "C029", "text": "quarter.prior quarter net revenue", "value": 86156000000.0, "unit": "USD", "source": "COST.quarter.prior_quarter_net_revenue", "period": "corresponding quarter ended 2025-08-31", "definition": "Second quarter column; corresponding quarter ended 2025-08-31; Total revenue; source in millions", "inputs": []}
```

```claim
{"id": "C030", "text": "quarter.quarter gaap diluted eps", "value": 6.75, "unit": "USD/shares", "source": "COST.quarter.quarter_gaap_diluted_eps", "period": "16 weeks ended 2026-08-30", "definition": "First quarter column; GAAP diluted EPS; 16 weeks ended 2026-08-30; listed common stock; no separate class dimension", "inputs": []}
```

```claim
{"id": "C031", "text": "quarter.annual release gaap diluted eps", "value": 20.76, "unit": "USD/shares", "source": "COST.quarter.annual_release_gaap_diluted_eps", "period": "full fiscal year ended 2026-08-30", "definition": "Third numeric column; full fiscal year ended 2026-08-30; GAAP diluted EPS; listed common stock; no separate class dimension", "inputs": []}
```

```claim
{"id": "C032", "text": "quarter.revenue growth", "value": 11.104275964529453, "unit": "%", "source": "COST.quarter.revenue_growth", "period": "2026-08-30", "definition": "Current quarter revenue / same quarter prior-year revenue minus one, nominal percent.", "inputs": [{"source": "COST.quarter.quarter_net_revenue", "value": 95723000000.0}, {"source": "COST.quarter.prior_quarter_net_revenue", "value": 86156000000.0}]}
```

```claim
{"id": "I033", "text": "Insight: Free cash flow comfortably exceeds capital expenditures, highlighting robust cash generation.", "value": 9382000000.0, "unit": "USD", "source": "COST.ratio.free_cash_flow", "period": "2025-09-01 to 2026-08-30", "definition": "Operating cash flow less reported property, equipment and technology purchases as applicable.", "inputs": [{"source": "COST.fact.operating_cash_flow", "value": 15817000000.0}, {"source": "COST.fact.capex", "value": 6435000000.0}]}
```

## Future Developments and Strategic Recommendations

To sustain its competitive edge, Costco should continue investing in cyber‑security infrastructure to mitigate sophisticated threats and protect member data. Maintaining strong employee development programs will preserve the high retention rate that underpins operational efficiency. Cautious expansion into new markets and careful integration of acquisitions are advised to avoid adverse financial impacts. Ongoing monitoring of legal proceedings and regulatory changes will be essential to manage potential liabilities.

```claim
{"id": "I034", "text": "Insight: Costco's return on average equity was strong", "value": 28.402111841396398, "unit": "%", "source": "COST.ratio.return_on_average_equity", "period": "2025-09-01 to 2026-08-30", "definition": "GAAP net income / average beginning and ending reported equity, percent.", "inputs": [{"source": "COST.fact.net_income", "value": 9226000000.0}, {"source": "COST.fact.prior_equity", "value": 29164000000.0}, {"source": "COST.fact.equity", "value": 35803000000.0}]}
```

## Investment Recommendation

<!-- thesis-start -->
Buy. Costco’s business model shows durable membership‑driven revenue and strong cash efficiency. The high return on average equity of [[COST.ratio.return_on_average_equity]] indicates efficient capital use, while the low leverage profile reduces financial risk. Although competitive pressures and litigation exposure are noted, the combination of operational resilience and robust profitability supports an investment‑positive stance.
<!-- thesis-end -->

```claim
{"id": "D035", "text": "Advisor deciding metric, quoted from the analyst output", "value": 28.402111841396398, "unit": "%", "source": "COST.ratio.return_on_average_equity", "period": "2025-09-01 to 2026-08-30", "definition": "GAAP net income / average beginning and ending reported equity, percent.", "inputs": [{"source": "COST.fact.net_income", "value": 9226000000.0}, {"source": "COST.fact.prior_equity", "value": 29164000000.0}, {"source": "COST.fact.equity", "value": 35803000000.0}]}
```

```claim
{"id": "I036", "text": "Insight: The firm maintains a low leverage profile with a debt‑to‑equity ratio of [[COST.ratio.debt_to_equity]]", "value": 0.17210848252939698, "unit": "x", "source": "COST.ratio.debt_to_equity", "period": "2025-09-01 to 2026-08-30", "definition": "Long-term debt including its current portion / ending reported equity.", "inputs": [{"source": "COST.fact.long_term_debt", "value": 3914000000.0}, {"source": "COST.fact.current_debt", "value": 2248000000.0}, {"source": "COST.fact.equity", "value": 35803000000.0}]}
```

### Review record

Human findings, both partner checks and student persona authorship remain pending.
