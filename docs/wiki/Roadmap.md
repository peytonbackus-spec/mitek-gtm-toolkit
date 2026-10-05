# Roadmap

What I'd build next, once there's real Mitek data and access. Ordered by when it would happen.

## First 30 days (baseline before building)

- Point the [DQ monitor](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/data_quality/dq_monitor.py) at a read-only Salesforce export; first pass-rate baseline
- Back-test the current lead score with the [calibration method](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_scoring/calibrate_scoring.py) on 12 months of outcomes
- Compute week 4/8/12 forecast accuracy and bias from 4 quarters of Clari snapshots
- Replace every `[ASSUME]` in [`config/mitek.yaml`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/config/mitek.yaml) with Mitek actuals

## Days 31–90

| 🟦 GTM Engineer | 🟩 Strategy & Ops |
|---|---|
| Routing v2 in Salesforce Flow, replay-tested against the last 200 MQLs | Stage exit criteria as validation rules |
| Re-weighted two-axis scoring | Separate Clari forecast tabs: new business / renewals |
| Lusha spend limited to B+ fit economic buyers | Deal-risk flags in shadow mode, then shown before manager calls |
| AI research brief: shadow → assisted | Renewal health v1 for the T-180 window |

## Later

- Swap the SQLite runner for the real warehouse (Snowflake/BigQuery) with dbt models built from the semantic layer
- Live LLM mode once vendor and retention terms are approved by security
- Calibrate renewal health weights and expected churn rates on actual outcomes
- Partner portal / deal registration integration once the Fiserv data path is known
