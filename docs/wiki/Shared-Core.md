# 🟪 Shared Core

About 40% of the two postings overlap: Salesforce data modeling, data-quality monitoring, dashboard architecture, AI workflow design and governance, and cross-functional process work. That overlap is built once in [`shared_core/`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/README.md) and both tracks build on it.

| Piece | What it gives both roles |
|---|---|
| [Salesforce object model](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/data_model/salesforce-object-model.md) | One owner per field, and the exact boundary between the roles (lead conversion) |
| [Data-quality monitor](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/data_quality/dq_monitor.py) | 16 rules with pass rates; lead rules route to 🟦, opportunity rules to 🟩 |
| [Metric definitions](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/metrics/metric-definitions.md) + [semantic-layer SQL](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/metrics/sql/semantic_layer.sql) | One definition per metric, so lead-side and opportunity-side numbers reconcile |
| [AI governance](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/README.md) | PII guard, LLM client, eval harness, human-review policy. See [[AI Governance]]. |
| [Company brief](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/context/mitek-company-brief.md), [ICP & personas](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/context/icp-and-personas.md), [stack map](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/context/gtm-stack-map.md) | Shared Mitek context. See [[Mitek Context]]. |
| [`config/mitek.yaml`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/config/mitek.yaml) | Every Mitek-specific value in one file; scripts read it, nothing is hardcoded |

**Why it matters:** if the GTM Engineer's "conversion rate" and the Strategy & Ops "conversion rate" are computed differently, the first leadership meeting becomes a debate about whose number is right. The tests check that the Python reports and the SQL return identical numbers.
