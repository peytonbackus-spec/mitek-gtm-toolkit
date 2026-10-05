# Gaps & Placeholders

This page separates three things: what is **real experience**, what is **demonstrated in this repo** (built on synthetic data), and what is **still a gap**. It exists so nothing here overclaims.

## 1. Experience vs demonstration, by requirement

Sources for the "Real experience" column: my resume (Sept 2026 version) and things I've said directly. Last updated Oct 5, 2026.

| Requirement (role) | Real experience | Demonstrated here | Gap / action |
|---|---|---|---|
| Salesforce automation, data model, governance (🟪) | ✅ Validation rules, Flows, fields, layouts, reports; CRM hygiene standards at Planful | Object model, Flow spec, DQ rules | — |
| Lead routing + scoring (🟦) | ✅ Built at Planful and Certa | Scoring, calibration, routing engine | — |
| Lead lifecycle + SDR process design (🟦) | ✅ SDR leadership at Planful (12) and Certa (5); qualification-based BDR→AE handoff; ramp framework | Lifecycle spec, SLA monitor, capacity model | — |
| AI-enabled workflows (🟪) | ✅ Certa: Clay signal-driven prospecting, security/RFP automation, AI-assisted account planning | 3 AI workflows with evals, PII guard, HITL | Confirmed builds with results in [builder-experience](about/builder-experience.md#ai-and-automation-work-ive-built): ~80% of pipeline from signal-based prospecting; win rate ~10% → ~15%; RFP turnaround 1.5–3 weeks → under 2 days |
| Clay (🟦) | ✅ Daily use; signal enrichment at Certa; consulting stack | Waterfall spec | — |
| Hands-on sales engagement platform (🟦 **required**) | ✅ **Outreach**: built the sequencing infrastructure at Certa, daily use | Salesloft cadence architecture spec | Haven't used Salesloft; frame Outreach → Salesloft as same category. Haven't built auto-enrollment; spec says so. |
| Nooks, Lusha (🟦 preferred) | ✅ Used both | Config specs | — |
| Qualified (🟦 preferred) | 🔁 Used Drift and Chili Piper, which between them cover what Qualified does (website chat, account ID, routing, booking) | Config spec | Frame as same category; Drift is now part of the Salesloft/Clari family |
| Sales Navigator (🟦 preferred) | ✅ Used it | Config spec | — |
| **Clari, hands-on (🟩 required, "ideally Clari")** | Not on resume. Adjacent: win-rate-based coverage and capacity forecasting (Certa, Planful); deal-risk and pipeline-health scoring (Certa). | Clari config spec (rebuilt from Clari's public docs: role-hierarchy roll-up, formula-field limits, CRM Score, Salesloft merger), forecast cadence, accuracy measurement | **Still the largest gap for Strategy & Ops.** Lead with forecasting *methodology* (which is real) and the spec. If you've used Clari at all, even as a viewer, `[CONFIRM]`. |
| Conversation intelligence / Clari Copilot (🟩 preferred) | ✅ **Gong**: qualification validation and objection-trend analysis fed back into messaging | Tracker and EB-detection design | Same category, different vendor |
| Deal-risk detection (🟩) | ✅ Deal-risk and pipeline-health scoring calibrated to Certa's ~10% win rate | `deal_risk.py` + evals | — |
| Forecasting cadence ownership (🟩) | Partial: I supplied inputs to forecast calls (win-rate-based coverage and capacity forecasts at Certa and Planful); I didn't run the call | Cadence + accuracy/bias script | Frame it as "built the inputs, now ready to own the cadence". The repo's cadence design shows how I'd run it. |
| Renewals / retention ops (🟩) | ✅ Customer health scoring built; Certa GTM-engineering scope covered Customer Success; the SDR target spanned expansion and renewal motions | Renewal process + health model | `[CONFIRM]` one detail to cite: inputs used, or what the score drove |
| Funnel analytics + reporting (both) | ✅ Full-funnel instrumentation at Certa (engagement tracking, SQL attribution, conversion analytics, weekly leadership reporting); performance dashboards at Planful | Funnel report, pipeline report, SQL | — |
| SQL / BI / warehouse (preferred, both) | 🔁 I read and understand SQL and write it AI-assisted | Semantic layer + role SQL, runnable | Good enough for a take-home. Say "AI-assisted" if asked; don't claim live whiteboard SQL. |
| 4+ years in GTM/Revenue Ops or technical GTM (both) | ~4 yrs 9 mo in B2B SaaS revenue orgs (Jan 2022 – now), with systems ownership growing throughout; plus 2+ yrs at TD Bank | — | Meets the bar. Frame it as one continuous arc: SDR → manager who built the systems → GTM engineering. |
| Enterprise ABM in fintech or cybersecurity (🟦 preferred) | Partial: Certa sells third-party-risk management to risk and security buyers; enterprise account planning and multithreading | — | `[CONFIRM]` specific ABM plays or accounts |
| Banking domain (useful for Mitek, not in posting) | ✅ Personal Banking Specialist, TD Bank (2019–2021) | — | Use as context, not as a fraud/IDV claim |

## 2. What's synthetic or assumed in this repo

| Item | Status | Replace with |
|---|---|---|
| `sample_data/*` (accounts, leads, opps, renewals, forecast snapshots) | Synthetic, seeded | Mitek Salesforce / Clari data (read-only) in week 1 |
| Segment and persona weights | `[ASSUME]` | Back-test on Mitek closed-won (calibration script does this) |
| ACV ranges, cycle lengths, quota | `[ASSUME]`, illustrative | Mitek actuals |
| Stage design and max days | `[ASSUME]` | Validate with sales leadership |
| Health weights and expected churn by band | `[ASSUME]` | Calibrate on 4 quarters of renewals |
| Competitor names | Placeholder labels in data; Jumio and Onfido are publicly compared against Mitek (see VARIABLES.md) | Mitek's actual competitive set from win/loss data |
| SDR / AE names | Fictional | — |
| AI model | Deterministic mock by default | Live mode exists (`GTM_LLM_MODE=anthropic`); vendor and retention terms need Mitek security approval |

## 3. Before this repo is shared with anyone

- [ ] Fill every `[CONFIRM]` in this file and in [`about/builder-experience.md`](about/builder-experience.md), or delete the row.
- [x] Re-check the company-brief figures against Mitek's latest press release (done Oct 5, 2026: Q3 FY26 figures verified against the 8-K exhibit; three items remain from call coverage only).
- [ ] Decide which role the conversation is about and lead with that track's README.
- [ ] Repo stays **private** until there's a reason to share it.
