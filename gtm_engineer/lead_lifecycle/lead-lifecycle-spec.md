# Lead Lifecycle Specification

![GTM Engineer](https://img.shields.io/badge/role-GTM%20Engineer-1F6FEB)

> **Posting:** "Own lead capture, enrichment, scoring, routing and disqualification processes" · "Define qualification standards across Marketing, SDRs and Account Executives" · "Drive alignment on data standards and service levels"

This is the contract between Marketing, SDRs and AEs. Each status has an entry rule, an owner, an SLA and an exit rule. Salesforce enforces the entry rules (validation rules plus record-triggered Flows). [`lifecycle_sla.py`](lifecycle_sla.py) measures the SLAs.

```mermaid
stateDiagram-v2
    [*] --> New: form / Qualified / list import / partner referral
    New --> Enriching: Clay waterfall triggered
    Enriching --> MQL: grade in MQL set OR hand-raise
    Enriching --> Disqualified: non-ICP (auto, reason required)
    Enriching --> Nurture: below threshold
    MQL --> SAL: SDR accepts (≤4h SLA)
    MQL --> Disqualified: SDR rejects (reason required)
    SAL --> Working: first touch (≤1h for demo / chat)
    Working --> SQL: discovery meeting held + qualification met
    Working --> Recycled: 14 days with no SQL
    SQL --> Converted: AE accepts → Opportunity created
    Recycled --> MQL: new intent after 90-day cool-off
    Nurture --> MQL: intent crosses threshold
```

| Status | Entry rule | Owner | SLA | Exit |
|---|---|---|---|---|
| **New** | Record created from any source; `Lead_Source` required | Marketing Ops | Enrichment starts in <5 min | → Enriching |
| **Enriching** | Clay waterfall running (see [waterfall spec](../platform_admin/clay-enrichment-waterfall.md)) | GTM Engineering (system) | <15 min | Scored → MQL / Nurture / Disqualified |
| **MQL** | `Lead_Grade__c` ∈ {A1, A2, B1, A3, B2} **or** demo request / Qualified chat in the last 14 days with fit ≥ C | SDR (routed) | Accept or reject within **4 business hours** | → SAL or Disqualified |
| **SAL** | SDR accepted; `Product_Interest__c` required | SDR | First touch ≤ **1 hour** for hand-raisers, same day otherwise | → Working |
| **Working** | Cadence active in Salesloft | SDR | **14 days** to reach SQL | → SQL or Recycled |
| **SQL** | Meeting held **and** qualification standard met (below) | SDR → AE | AE accepts within 2 business days | → Converted |
| **Converted** | Opportunity created at Stage 1; `Originating_Lead__c` stamped | AE | — | Hand-off to [opportunity lifecycle](../../gtm_strategy_ops/opportunity_lifecycle/stage-definitions.md) 🟩 |
| **Recycled** | No SQL in window or "not now" | Marketing | 90-day cool-off | → MQL on new intent |
| **Disqualified** | `Disqualify_Reason__c` required | SDR / system | — | Feeds [scoring calibration](../lead_scoring/calibrate_scoring.py) |

## Qualification standard for SQL (shared by Marketing, SDR and AE)

An SQL needs **all four**. Each one is a field, so it can be reported on:

1. **Fit:** ICP segment (not `other`) and fit grade A–B.
2. **Use case:** a named fraud, identity or deposit problem in one of Mitek's two product lines (`Product_Interest__c`).
3. **Persona:** a meeting held with an economic buyer or champion persona (see [personas](../../shared_core/context/icp-and-personas.md)).
4. **Timing or trigger:** a known initiative, vendor contract end, regulatory driver or loss event, recorded in `SQL_Trigger__c`.

AEs can reject an SQL within 2 days with a reason. Rejection rate by SDR and by source shows up in the weekly funnel report. That's how "qualified" stays a shared standard instead of an argument.

## Disqualification reasons (picklist, required)

`Not ICP` · `Competitor` · `Student/Job Seeker` · `Existing Open Opp` · `No Fraud/IDV Use Case` · `Bad Data` · `Duplicate`

Required because calibration depends on them. If 30% of A-grade leads are disqualified as "No Fraud/IDV Use Case", the fit model is wrong and the weights need to change.
