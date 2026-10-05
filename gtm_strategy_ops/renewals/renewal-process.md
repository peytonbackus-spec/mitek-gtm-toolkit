# Renewal Process

![Strategy & Ops](https://img.shields.io/badge/role-GTM%20Strategy%20%26%20Ops-2DA44E)

> **Posting:** "Design renewal processes and partner-sourced opportunity workflows" · "Capture closed-lost and churn insights for actionable analysis" · "Serve as operational partner to sales, finance and customer success"

## Timeline (anchored to renewal date, T)

| When | Step | Owner | System |
|---|---|---|---|
| **T-180** | Renewal opportunity auto-created (`Type = Renewal`, amount = current ARR, stage 1) | System (Flow on contract) | Salesforce |
| **T-180** | Health score computed ([`renewal_signals.py`](renewal_signals.py)); band written to the opportunity | RevOps | Warehouse → Salesforce |
| **T-150** | **At Risk:** AI renewal brief → CS + AE review → escalation plan. **Healthy with expansion signal:** create a linked Expansion opportunity. | CSM + AE | Salesforce, Slack |
| **T-120** | Usage review with the customer. For check customers, review volume trends against their channel mix. | CSM | — |
| **T-90** | Commercial proposal. Renewal forecast category set (Commit only with a verbal yes). | AE | Clari |
| **T-60** | Security and legal paperwork started. Banks need this lead time. | AE + Legal | — |
| **T-30** | Signature target. Escalate to the VP if unsigned. | AE | — |
| **T+0** | Closed Won / Closed Lost; **churn reason required** ([taxonomy](closed-lost-and-churn-taxonomy.md)) | AE | Salesforce |

## Forecasting renewals

- Renewals are forecast **separately** from new business in Clari (a separate forecast type), so a large check renewal can't mask a new-logo miss, or the reverse.
- Forecast GRR = 1 − Σ(ARR × expected churn by health band). Expected churn rates per band are calibrated quarterly against actual outcomes.
- Track gross and net retention by **product line**. Check and identity carry very different risk profiles.

## Health model inputs (aggregated only, no transaction data)

| Component | Weight | Source |
|---|---|---|
| Volume trend (90d) | 30% | Usage telemetry (transaction / check counts) |
| Utilization of committed volume | 20% | Billing |
| Sev-1 tickets (90d) | 15% | Support system |
| Exec sponsor active | 20% | CSM-maintained field |
| Competitive signal | 15% | Clari Copilot mentions, AE flag |
