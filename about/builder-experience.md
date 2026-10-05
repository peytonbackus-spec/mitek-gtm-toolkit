# Where My Builder Experience Comes From

> Context: when I reached out about these roles, Nathan asked where my hands-on builder experience came from and what CRM building I've done. This is the long-form answer. Every line comes from my resume (Sept 2026 version) or things I've said directly. Items marked `[CONFIRM]` are still open.

## The short version

I came to GTM engineering from the SDR-leadership side. I built routing, scoring, coverage models and enrichment because my teams needed them. Certa then made that the job: AI Systems & GTM Engineering, owning GTM systems and process across the full revenue lifecycle (SDR, AE and Customer Success).

## Timeline

| Dates | Role | Company | What I built / owned |
|---|---|---|---|
| Sep 2026 – present | Founder, independent GTM consultant | AI-native GTM consulting practice | GTM audits, pipeline-engine retainers and RevOps sprints for B2B SaaS. Delivery stack: Clay, HubSpot, n8n, Apollo. I set up and run client CRM and automation environments end to end. |
| Feb 2026 – Aug 2026 | AI Systems & GTM Engineering | Certa.ai (third-party risk management; Series B) | Signal-driven prospecting with Clay across technographic, firmographic and intent data. **Deal-risk and pipeline-health scoring calibrated to Certa's ~10% new-business win rate.** Automation for security/RFP processing and sequence optimization. Gong-based qualification checks and objection tracking. AI-assisted account planning. Full-funnel instrumentation (engagement tracking, SQL attribution, conversion analytics) feeding weekly leadership reporting. |
| Apr 2025 – Feb 2026 | Head of Sales Development & Global SDR Operations | Certa.ai | 5 direct SDRs; cross-functional oversight of 9 Sales Ops and 8 AEs; $3.5M target driven by ~45 qualified meetings/week across net-new, expansion and renewal. Wrote the SDR playbook v1 including **sequencing infrastructure in Outreach**. **Pipeline coverage targets and capacity forecasting built on actual win rate.** Ramp framework. Qualification-based BDR→AE handoff. |
| Oct 2022 – Apr 2025 | Manager, Sales Development | Planful (FP&A SaaS) | Team grew to 12 SDRs including Team Leads; ~28 qualified meetings/week. ~120% average attainment against an ~8% win rate. **Performance dashboards and win-rate-based pipeline forecasting models.** **Salesforce CRM hygiene standards**, outbound workflow improvements and qualification frameworks. Lead routing logic and account prioritization/scoring. |
| Jan 2022 – Oct 2022 | SDR | Planful | Top performer; promoted to manager within 10 months |
| Sep 2019 – Dec 2021 | Personal Banking Specialist | TD Bank | Client portfolios; cross-sell and retention targets |

Never missed target, as an IC or as a manager.

## CRM and systems build experience

| Platform | Built / used |
|---|---|
| **Salesforce** | Validation rules, Flows, custom fields and page layouts, pipeline reports and dashboards, CRM hygiene standards; deal-risk / pipeline-health scoring surfaced to reps and leadership |
| **HubSpot** | Custom properties and objects, lifecycle and routing workflows, lead scoring, dashboards |
| **Clay** | Signal-driven enrichment across technographic, firmographic and intent data; enrichment waterfalls |
| **Outreach** | Sequencing infrastructure for the SDR playbook (day-to-day user) |
| **Gong** | Qualification validation, objection-trend tracking fed back into messaging and sequencing (day-to-day user) |
| **n8n** | Workflow orchestration between GTM systems |

**What I haven't built:** automated sequence enrollment (rules that auto-enroll leads into cadences). The [Salesloft spec](../gtm_engineer/platform_admin/salesloft-nooks-qualified-salesnav.md) says so and describes how I'd pilot it safely.

## AI and automation work I've built

All confirmed. Numbers marked `[#]` are still to add; an approximate number beats none.

| # | What | Where | Production or proof of concept | Result |
|---|---|---|---|---|
| 1 | Clay signal-based prospecting (technographic, firmographic, intent signals → personalized sequences) | Certa | Production | `[#]` share of the ~45 meetings/week it sourced, or reply-rate lift |
| 2 | Deal-risk and pipeline-health scoring tied to the real ~10% win rate | Certa | Production | `[#]` slipped deals it caught, or the coverage target it replaced (3–4x benchmark → real number) |
| 3 | Security questionnaire / RFP processing automation | Certa | Production | `[#]` hours saved per RFP or turnaround time |
| 4 | Outbound sequence optimization automation | Certa | Production | `[#]` reply or meeting-rate lift |
| 5 | AI-assisted account planning and executive value models | Certa | Production | `[#]` contacts per opportunity or handoff acceptance |
| 6 | Gong objection tracking fed back into messaging, sequencing and system logic | Certa | Production | `[#]` a messaging change and what moved |
| 7 | GTM prompt and agent library (~53 Claude agents: ICP, scoring, sequences, forecast rollup, renewals…) | Personal toolkit repo | In daily use | `[#]` a task it cut from hours to minutes |
| 8 | Speed-to-lead MCP server enforcing an inbound response SLA | `bd-leadership` repo | Proof of concept | — |
| 9 | Free GTM tech-stack evaluator with Claude-generated audit reports | Live on Vercel | Production (public tool) | `[#]` reports generated |
| 10 | Customer health scoring | `[CONFIRM: where]` | Production | `[#]` what it drove (renewals flagged early, CS prioritization) |

## Mapping to Mitek's stack

| Mitek tool | My closest hands-on experience | Transfer |
|---|---|---|
| Salesforce | Direct (above) | ✅ Same tool |
| Clay | Direct | ✅ Same tool |
| **Salesloft** | **Outreach**: built sequencing infrastructure, daily use | 🔁 Same category, different vendor. Cadence architecture, enrollment and activity sync concepts carry over directly. |
| **Clari** (forecasting) | Win-rate-based coverage and capacity forecasting models that fed leadership's forecast calls; deal-risk and pipeline-health scoring at Certa; customer health scoring | 🔁 Forecast *methodology* is direct; Clari as a tool is `[CONFIRM: any hands-on use?]` |
| **Clari Copilot** | **Gong**: qualification and objection analysis | 🔁 Same category (conversation intelligence) |
| Nooks | Direct: I've used it | ✅ Same tool |
| Lusha | Direct: I've used it (Apollo in my consulting stack too) | ✅ Same tool |
| Qualified | **Drift** (its closest competitor) and **Chili Piper** (routing + meeting booking) | 🔁 Same category, different vendor. Drift covers the chat and account-ID side, Chili Piper the routing and booking side. |
| LinkedIn Sales Navigator | Direct: I've used it | ✅ Same tool |
| SQL / warehouse | I read and understand SQL and write it with AI assistance (the SQL in this repo was built that way) | 🔁 Comfortable for take-home and analysis work; I don't claim live whiteboard SQL |

## Why my background is relevant to Mitek specifically

- **Risk and security buyers.** Certa sells third-party-risk management, so its deals run through the same vendor-risk and security reviews Mitek's do. That's why the opportunity stages in this repo give **security review** its own gate, and why I built security/RFP automation at Certa.
- **I've worked inside a bank.** Two years at TD as a Personal Banking Specialist. Banks are Mitek's core buyers, so I've worked on the buyer's side of the table. `[CONFIRM: anything specific from TD on deposits, fraud or ID checks worth mentioning?]`
- **Deal-risk and coverage models are already my work.** The Strategy & Ops posting asks for deal-risk detection and forecast-accuracy measurement. I built deal-risk and pipeline-health scoring calibrated to real win rates at Certa. The [deal-risk model](../gtm_strategy_ops/ai_deal_risk/deal_risk.py) in this repo is a cleaner, Mitek-shaped version of that idea.
- The GTM Engineer posting prefers "enterprise account-based motion experience in fintech or cybersecurity". Certa (risk/security) is the closest overlap. `[CONFIRM: specific ABM accounts or plays I can talk to]`
