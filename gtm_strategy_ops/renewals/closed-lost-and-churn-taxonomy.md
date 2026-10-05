# Closed-Lost & Churn Taxonomy

![Strategy & Ops](https://img.shields.io/badge/role-GTM%20Strategy%20%26%20Ops-2DA44E)

> **Posting:** "Capture closed-lost and churn insights for actionable analysis"

One picklist for new-business losses and one for churn. Each value has an owner who acts on it. Values are mirrored in [`config/mitek.yaml`](../../config/mitek.yaml) so the code and Salesforce can't drift.

## New business: `Closed_Lost_Reason__c` (required on Closed Lost)

| Value | Use when | Required detail | Fix owner |
|---|---|---|---|
| Price | Chose a cheaper option or no budget at our price | Competitor or alternative price, if known | Sales leadership |
| Lost to Competitor | Signed with a named vendor | `Competitor__c` required | Product Marketing |
| No Decision / Status Quo | Project stopped; stayed with the current process | Last stage reached | Sales |
| Build In-House | Building internally | — | Product |
| Security / Compliance Blocker | Failed the security review, data residency or regulator concern | Specific blocker | Security / Legal |
| Integration Effort | Couldn't resource the integration (core, mobile app, onboarding flow) | System involved | Solutions Engineering |
| Timing / Budget | Real need, wrong quarter or fiscal year | Re-engage date (auto-creates a task) | Marketing nurture |
| Champion Left | Champion or sponsor departed mid-cycle | — | Sales ops (multi-threading standard) |

## Churn and downgrade: `Churn_Reason__c` (required on lost renewal or downsell)

| Value | Notes | Signal that predicted it (validate quarterly) |
|---|---|---|
| Volume decline | Fewer checks or verifications. Structural for check. | `volume_trend` component |
| Consolidated vendor | Moved to a platform bundle (core provider, IDV suite) | `competitive` component |
| M&A | Acquired; acquirer's vendor won | News signal |
| Product gap | Needed a capability we lack | Clari Copilot mentions |
| Service / support | Sev-1 history, implementation issues | `support` component |
| Price at renewal | Pushback on uplift or commit | — |
| Business closure | — | — |

## Review loop

- **Monthly:** [`closed_lost_analysis.py`](closed_lost_analysis.py) output reviewed with Sales and Product Marketing leaders. Each top reason gets an owner and a dated action.
- **Quarterly:** check the [renewal health model](renewal_signals.py) against what actually churned. Did the drivers we weighted predict the churn reasons we got? Re-weight if not.
- **Data quality:** blank reasons are tracked in the [DQ monitor](../../shared_core/data_quality/dq_monitor.py) (rule O03). An "Other" value is deliberately not allowed.
