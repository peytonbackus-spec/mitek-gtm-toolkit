# 🟩 Strategy and Ops Track

**Posting:** manages "data systems and processes governing the sales pipeline lifecycle", combining GTM operations, analytics and engineering. Full requirement map: [gtm_strategy_ops/README.md](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/README.md).

## What's in the track

| Area | Artifact | Type |
|---|---|---|
| Opportunity lifecycle | [Stage definitions & exit criteria](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/opportunity_lifecycle/stage-definitions.md) | 📐 |
| Pipeline analytics | [Pipeline report](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/pipeline_analytics/pipeline_report.py) · [SQL](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/pipeline_analytics/sql/pipeline_coverage.sql) · [dashboard spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/pipeline_analytics/dashboard-spec.md) | ▶️ + 📐 |
| Forecasting | [Forecast cadence](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/forecasting/forecast-cadence.md) · [accuracy & bias](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/forecasting/forecast_accuracy.py) | 📐 + ▶️ |
| Deal risk | [Risk signals + AI commentary](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/ai_deal_risk/deal_risk.py) with prompts and evals | ▶️ |
| Renewals | [Renewal process](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/renewals/renewal-process.md) · [health signals](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/renewals/renewal_signals.py) · [closed-lost](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/renewals/closed_lost_analysis.py) | 📐 + ▶️ |
| Partners | [Partner-sourced opportunity workflow](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/partner_ops/partner-sourced-opportunity-workflow.md) | 📐 |
| Sales leadership | [VP of Sales brief, scorecard, industries, stage velocity, deal board, all-hands](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/sales_leadership/README.md) | ▶️ |
| Sales planning | [Capacity, quota, territory, pipeline distribution](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/sales_planning/README.md) · [CRM request intake](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/sales_planning/crm-request-intake.md) | ▶️ + 📐 |
| Clari | [Configuration & Salesforce integration spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/clari_admin/clari-configuration-spec.md) | 📐 |

## Design in one paragraph

Stages are defined by buyer outcomes, not seller activity, and Mitek's two long poles, technical validation and bank security review, each get their own gate. Deal risk is decided by explainable rules and *explained* by AI, never the other way round, and every suggestion (including any forecast-category change) goes through human review. Forecast accuracy is measured at weeks 4, 8 and 12 by region, so bias shows up as a pattern you can coach rather than a one-off miss. Renewals are forecast separately from new business, and check renewals are weighted for volume decline because management has said check is in structural decline.

## Clari, honestly

The forecasting method (win-rate-based coverage, deal-risk scoring, forecast inputs) is my experience. Clari as a tool is researched from public documentation: the role-hierarchy roll-up, the formula-field limitation, CRM Score, and the Dec 2025 Clari–Salesloft merger. The [spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/clari_admin/clari-configuration-spec.md) says so on the first line.

## Handoff in

Receives SQLs from the [[GTM Engineer Track]] at lead conversion, plus partner deal registrations and expansion signals from renewals.
