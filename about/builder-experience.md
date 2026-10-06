# Where My Builder Experience Comes From

## The short version

I came to GTM engineering from the SDR-leadership side. I built routing, scoring, coverage models and enrichment because my teams needed them. Certa then made that the job: AI Systems & GTM Engineering, owning GTM systems and process across the full revenue lifecycle (SDR, AE and Customer Success).

## Timeline

| Dates | Role | Company | What I built / owned |
|---|---|---|---|
| Feb 2026 – Aug 2026 | AI Systems & GTM Engineering | Certa.ai (third-party risk management; Series B) | Signal-driven prospecting with Clay across technographic, firmographic and intent data. Deal-risk and pipeline-health scoring calibrated to the real new-business win rate. Automation for security/RFP processing and sequence optimization. Gong-based qualification checks and objection tracking. AI-assisted account planning. Full-funnel instrumentation (engagement tracking, SQL attribution, conversion analytics) feeding weekly leadership reporting. |
| Apr 2025 – Feb 2026 | Head of Sales Development & Operations | Certa.ai | Five direct SDRs; cross-functional oversight of Sales Ops and AEs. SDR playbook including sequencing infrastructure in Outreach. Pipeline coverage targets and capacity forecasting built on actual win rate. Ramp framework. Qualification-based BDR→AE handoff. |
| Sep 2022 – Apr 2025 | Manager, Sales Development | Planful (FP&A SaaS) | Team grew to 12 SDRs including Team Leads. Performance dashboards and win-rate-based pipeline forecasting models. Salesforce CRM hygiene standards, outbound workflow improvements and qualification frameworks. Lead routing logic and account prioritization/scoring. |
| Jan 2022 – Sep 2022 | SDR | Planful | Promoted to manager within ten months |
| Sep 2019 – Dec 2021 | Personal Banking Specialist | TD Bank | Client portfolios; cross-sell and retention targets |

## CRM and systems build experience

| Platform | Built / used |
|---|---|
| **Salesforce** | Validation rules, Flows, custom fields and page layouts, pipeline reports and dashboards, CRM hygiene standards; deal-risk and pipeline-health scoring surfaced to reps and leadership |
| **HubSpot** | Custom properties and objects, lifecycle and routing workflows, lead scoring, dashboards |
| **Clay** | Signal-driven enrichment across technographic, firmographic and intent data; enrichment waterfalls |
| **Outreach** | Sequencing infrastructure for the SDR playbook (day-to-day user) |
| **Gong** | Qualification validation, objection-trend tracking fed back into messaging and sequencing (day-to-day user) |
| **n8n** | Workflow orchestration between GTM systems |

**Not built yet:** automated sequence enrollment (rules that auto-enroll leads into cadences). The [engagement-layer spec](../gtm_engineer/platform_admin/salesloft-nooks-qualified-salesnav.md) describes how I would pilot it safely.

## Results from this work

- Signal-based prospecting with Clay produced about 80% of pipeline at Certa.
- Deal-risk and pipeline-health scoring took the win rate on closed deals from about 10% to about 15%.
- Security questionnaire and RFP automation cut turnaround from 1.5–3 weeks to under 2 days, with human review kept where verification matters.

## Mapping to Mitek's stack

| Mitek tool | My closest hands-on experience | Transfer |
|---|---|---|
| Salesforce | Direct (above) | Same tool |
| Clay | Direct | Same tool |
| Salesloft | Outreach: built sequencing infrastructure, daily use | Same category, different vendor |
| Clari (forecasting) | Win-rate-based coverage and capacity forecasting; deal-risk scoring. I have not administered Clari; the Clari spec in this repo is written from Clari's public documentation. | Forecasting methodology is direct; the tool is new |
| Clari Copilot | Gong: qualification and objection analysis | Same category, different vendor |
| Nooks, Lusha, Sales Navigator | Direct | Same tools |
| Qualified | Drift and Chili Piper | Same category, different vendors |
| SQL / warehouse | I read SQL and write it with AI assistance (the SQL in this repo was built that way) | Comfortable for analysis and take-home work |

## Why this background is relevant to Mitek

- **Risk and security buyers.** Certa sells third-party-risk management, so its deals run through the same vendor-risk and security reviews Mitek's do. That is why the opportunity stages in this repo give security review its own gate.
- **Banking exposure.** Two years at TD as a Personal Banking Specialist. Banks are Mitek's core buyers.
- **Deal-risk and coverage models are already my work.** The [deal-risk model](../gtm_strategy_ops/ai_deal_risk/deal_risk.py) in this repo is a cleaner, Mitek-shaped version of what I built at Certa.
