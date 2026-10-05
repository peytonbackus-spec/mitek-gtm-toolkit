# Gaps & Placeholders

This page separates three things: what is **real experience**, what is **demonstrated in this repo** (built on synthetic data), and what is **still a gap**. It exists so nothing here overclaims.

## 1. Experience vs demonstration, by requirement

| Requirement (role) | Real experience | Demonstrated here | Gap / action |
|---|---|---|---|
| Salesforce automation, data model, governance (🟪) | ✅ Validation rules, Flows, fields, layouts, reports | Object model, Flow spec, DQ rules | — |
| Lead routing + scoring (🟦) | ✅ Built at Planful and Certa | Scoring, calibration, routing engine | — |
| Lead lifecycle + SDR process design (🟦) | ✅ SDR leadership at Planful (12) and Certa (5) | Lifecycle spec, SLA monitor, capacity model | — |
| AI-enabled workflows (🟪) | ✅ Certa AI Systems & GTM Engineering; consulting practice | 3 AI workflows with evals, PII guard, HITL | `[CONFIRM]` one production AI workflow + measured result to cite |
| Clay (🟦) | ✅ | Waterfall spec | — |
| Salesloft / sales engagement (🟦 required) | `[CONFIRM]` | Cadence architecture spec | Haven't built auto-enrollment; spec says so |
| Nooks, Lusha, Qualified, Sales Nav (🟦 preferred) | `[CONFIRM]` | Config specs | Confirm hands-on vs evaluated |
| **Clari, hands-on (🟩 required, "ideally Clari")** | `[CONFIRM]` | Clari config spec, forecast cadence, accuracy measurement | **Largest likely gap for the Strategy & Ops role.** If it's limited, lead with forecast process and accuracy measurement, which are tool-agnostic, and show the spec. |
| Clari Copilot / conversation intelligence (🟩 preferred) | `[CONFIRM]` | Tracker and EB-detection design | Confirm |
| Forecasting cadence ownership (🟩) | `[CONFIRM]`: ran forecasts as SDR leader / GTM eng? | Cadence + accuracy/bias script | Be specific about what was owned vs contributed to |
| Renewals / retention ops (🟩) | `[CONFIRM]`: Certa scope included CS | Renewal process + health model | Confirm depth |
| SQL / BI / warehouse (preferred, both) | `[CONFIRM]` | Semantic layer + role SQL, runnable | Confirm depth |
| 4+ years in GTM/Revenue Ops or technical GTM (both) | `[CONFIRM: count years]` | — | Frame SDR leadership + builder work + Certa GTM engineering as one continuous technical-GTM arc |
| Enterprise ABM in fintech or cybersecurity (🟦 preferred) | Partial: Certa is third-party-risk (security/risk buyers) | — | `[CONFIRM]` account examples |

## 2. What's synthetic or assumed in this repo

| Item | Status | Replace with |
|---|---|---|
| `sample_data/*` (accounts, leads, opps, renewals, forecast snapshots) | Synthetic, seeded | Mitek Salesforce / Clari data (read-only) in week 1 |
| Segment and persona weights | `[ASSUME]` | Back-test on Mitek closed-won (calibration script does this) |
| ACV ranges, cycle lengths, quota | `[ASSUME]`, illustrative | Mitek actuals |
| Stage design and max days | `[ASSUME]` | Validate with sales leadership |
| Health weights and expected churn by band | `[ASSUME]` | Calibrate on 4 quarters of renewals |
| Competitor names | Placeholder labels | Mitek's actual competitive set |
| SDR / AE names | Fictional | — |
| AI model | Deterministic mock by default | Live mode exists (`GTM_LLM_MODE=anthropic`); vendor and retention terms need Mitek security approval |

## 3. Before this repo is shared with anyone

- [ ] Fill every `[CONFIRM]` in this file and in [`about/builder-experience.md`](about/builder-experience.md), or delete the row.
- [ ] Re-check the company-brief figures against Mitek's latest 10-Q / press release.
- [ ] Decide which role the conversation is about and lead with that track's README.
- [ ] Repo stays **private** until there's a reason to share it.
