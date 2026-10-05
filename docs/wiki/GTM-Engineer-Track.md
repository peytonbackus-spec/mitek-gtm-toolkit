# 🟦 GTM Engineer Track

**Posting:** owns "the data, AI workflows, systems and operating processes that drive demand generation through qualified pipeline development." Full requirement map: [gtm_engineer/README.md](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/README.md).

## What's in the track

| Area | Artifact | Type |
|---|---|---|
| Lead lifecycle | [Lifecycle spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_lifecycle/lead-lifecycle-spec.md) (statuses, SLAs, SQL standard) · [SLA monitor](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_lifecycle/lifecycle_sla.py) | 📐 + ▶️ |
| Scoring | [Fit × intent scoring](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_scoring/score_leads.py) · [calibration](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_scoring/calibrate_scoring.py) | ▶️ |
| Routing | [Routing engine R1–R7](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_routing/route_leads.py) · [Salesforce Flow spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/lead_routing/salesforce-routing-flow-spec.md) | ▶️ + 📐 |
| AI research | [Account research brief](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/ai_research/account_research.py) with prompt, evals and review queue | ▶️ |
| Platforms | [Clay + Lusha waterfall](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/platform_admin/clay-enrichment-waterfall.md) · [Salesloft, Nooks, Qualified, Sales Nav](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/platform_admin/salesloft-nooks-qualified-salesnav.md) | 📐 |
| Analytics | [Funnel report](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/funnel_analytics/funnel_report.py) · [SQL](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/funnel_analytics/sql/lead_funnel.sql) · [dashboard spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/funnel_analytics/dashboard-spec.md) | ▶️ + 📐 |
| Capacity | [SDR capacity model](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/sdr_capacity/capacity_model.py) | ▶️ |

## Design in one paragraph

Leads are scored on two separate axes, fit and intent, so a quiet Top-25 bank fraud leader and an over-active student don't blend into the same number. Routing is an ordered rule list (R1–R7) where the order *is* the GTM policy, and every lead carries the rule and reason that routed it. Existing customers go to their account owner (the cross-sell play), partner referrals go to the partner manager, and only net-new MQLs reach the SDR pool. The AI research brief runs after routing, never writes to the CRM without review, and has an eval set that fails CI if a prompt change breaks the contract.

## Tool experience for this role

Hands-on: Salesforce, Clay, Lusha, Nooks, Sales Navigator, Outreach, Gong, Drift, Chili Piper. Same category, different vendor: Salesloft (Outreach), Qualified (Drift + Chili Piper). See [builder-experience](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/about/builder-experience.md).

## Handoff

The track ends at lead conversion. The opportunity is created at stage 1 with `Originating_Lead__c` set, and ownership passes to the [[Strategy and Ops Track]].
