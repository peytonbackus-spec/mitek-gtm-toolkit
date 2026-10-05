# 🟪 Shared Core: supports BOTH roles

![Shared](https://img.shields.io/badge/supports-BOTH%20roles-7B61FF) ![GTM Engineer](https://img.shields.io/badge/GTM%20Engineer-✓-1F6FEB) ![Strategy & Ops](https://img.shields.io/badge/GTM%20Strategy%20%26%20Ops-✓-2DA44E)

The two Mitek postings overlap on about 40% of their requirements: Salesforce data modeling, data-quality monitoring, dashboard architecture, AI workflow design and governance, and cross-functional leadership. That overlap lives here, built once. Each role track builds on it.

| Folder | What it is | Posting language it answers |
|---|---|---|
| [`context/`](context/) | [Company brief](context/mitek-company-brief.md), [ICP & personas](context/icp-and-personas.md), [stack map](context/gtm-stack-map.md) | "Operationalize ICP segmentation" · "analytical views segmented by region, product, source, owner" |
| [`data_model/`](data_model/) | [Salesforce object & field model](data_model/salesforce-object-model.md), including the Lead→Opportunity handoff boundary | "Translate GTM policies into Salesforce configurations" · "Own Salesforce opportunity lifecycle configuration" · "data modeling" |
| [`data_quality/`](data_quality/) | [`dq_monitor.py`](data_quality/dq_monitor.py): 16 rules across Lead and Opportunity, with an owner and pass rate per rule | "Data-quality monitoring and reconciliation" · "data quality monitoring across Salesforce and Clari" |
| [`ai_governance/`](ai_governance/) | [AI workflow standard](ai_governance/README.md), [PII guard](ai_governance/pii_guard.py), [LLM client](ai_governance/llm_client.py), [eval harness](ai_governance/eval_harness.py), [HITL policy](ai_governance/hitl.py) | "Define prompts, outputs, evaluation criteria and HITL controls" · "governance for data security and responsible AI use" |
| [`metrics/`](metrics/) | [Metric definitions](metrics/metric-definitions.md), [semantic-layer SQL](metrics/sql/semantic_layer.sql), [SQL runner](metrics/run_sql.py) | "Data modeling and dashboard architecture" · "SQL, BI tools, warehouse-based reporting" |

```bash
python -m shared_core.data_quality.dq_monitor            # rule pass rates + failing records
python -m shared_core.metrics.run_sql                    # build the semantic layer on sample data
```
