# Role Map: Both Postings, Side by Side

The two Mitek postings share a template. Both have Analytics, AI & Automation, a domain section and Cross-Functional Leadership, and both pay $130K–$150K. They split the revenue lifecycle at the lead→opportunity handoff. This page lines them up theme by theme and shows where each requirement is answered.

**Legend:** 🟦 GTM Engineer only · 🟩 GTM Strategy & Ops only · 🟪 both (built once in `shared_core/`) · ▶️ runnable · 📐 spec

## At a glance

| Only 🟦 GTM Engineer | 🟪 Both | Only 🟩 Strategy & Ops |
|---|---|---|
| Lead capture, enrichment, scoring, routing, disqualification | Salesforce data modeling + automation | Opportunity lifecycle + stage standards |
| Qualification standards (Mktg / SDR / AE) | Data-quality monitoring & reconciliation | Forecast cadence, categories, accuracy |
| Clay, Lusha, Nooks, Qualified, Sales Nav admin | Dashboard architecture + data modeling | Clari admin + Salesforce integration |
| SDR capacity + performance | AI workflows: prompts, outputs, evals, HITL | Renewal processes + churn insights |
| Account penetration, early-pipeline outlook | AI governance, data security | Partner-sourced opportunity workflow |
| ICP segmentation + target-account strategy | Measuring realized AI gains | Closed-lost analysis |
| | Requirements gathering, process design, cross-functional partnership | Clari Copilot (preferred) |
| | SQL / BI / warehouse (preferred) · GTM app development (preferred) | |

---

## Theme 1: Analytics & reporting infrastructure

| 🟦 GTM Engineer asks | 🟩 Strategy & Ops asks | Answered by |
|---|---|---|
| Foundational analytics for lead-to-opp conversion | Commercial data models + dashboard architecture, pipeline-to-renewal | 🟪 [semantic layer SQL](shared_core/metrics/sql/semantic_layer.sql) ▶️ · 🟪 [metric definitions](shared_core/metrics/metric-definitions.md) |
| Dashboards: volume, conversion velocity, pipeline value, account penetration | Reporting: pipeline coverage, conversion, forecast accuracy, retention | 🟦 [funnel report](gtm_engineer/funnel_analytics/funnel_report.py) ▶️ + [spec](gtm_engineer/funnel_analytics/dashboard-spec.md) · 🟩 [pipeline report](gtm_strategy_ops/pipeline_analytics/pipeline_report.py) ▶️ + [spec](gtm_strategy_ops/pipeline_analytics/dashboard-spec.md) |
| Cohort and trend analysis on lead-scoring and routing performance | Analytical views by region, product, source, owner | 🟦 [calibrate_scoring.py](gtm_engineer/lead_scoring/calibrate_scoring.py) ▶️ · 🟩 `open_pipeline_by()` / `win_rates_by()` ▶️ |
| Data-quality monitoring and reconciliation | Data-quality monitoring across Salesforce and Clari | 🟪 [dq_monitor.py](shared_core/data_quality/dq_monitor.py) ▶️ (lead rules → 🟦, opp rules → 🟩) · 🟩 [Clari sync checks](gtm_strategy_ops/clari_admin/clari-configuration-spec.md) 📐 |
| Early-pipeline outlooks and performance narratives | Decision-focused pipeline and forecast narratives | 🟦 `early_pipeline_outlook()` + `narrative()` ▶️ · 🟩 `pipeline_report.narrative()` + [forecast commentary](gtm_strategy_ops/ai_deal_risk/prompts/forecast_commentary.md) ▶️ |

## Theme 2: AI & automation

| 🟦 GTM Engineer asks | 🟩 Strategy & Ops asks | Answered by |
|---|---|---|
| Production AI workflows for account research, enrichment, qualification, routing | Production AI workflows for deal-risk detection, forecast commentary, renewal signals | 🟦 [account_research.py](gtm_engineer/ai_research/account_research.py) ▶️ · 🟩 [deal_risk.py](gtm_strategy_ops/ai_deal_risk/deal_risk.py) ▶️ · 🟩 [renewal_signals.py](gtm_strategy_ops/renewals/renewal_signals.py) ▶️ |
| Connect AI to GTM systems via low-code tools and APIs | Integrate AI with Salesforce, Clari via low-code tools | 🟪 [LLM client](shared_core/ai_governance/llm_client.py) ▶️ · 🟦 [Clay waterfall](gtm_engineer/platform_admin/clay-enrichment-waterfall.md) 📐 · 🟩 [Clari AI outputs](gtm_strategy_ops/clari_admin/clari-configuration-spec.md#ai-outputs-into-clari) 📐 |
| Define prompts, outputs, evaluation criteria, HITL controls | Define prompts, outputs, governance standards | 🟪 [AI workflow standard](shared_core/ai_governance/README.md) · [eval harness](shared_core/ai_governance/eval_harness.py) ▶️ · [HITL](shared_core/ai_governance/hitl.py) ▶️ · prompt evals in CI |
| Governance for data security and responsible AI | (governance standards, above) | 🟪 [PII guard](shared_core/ai_governance/pii_guard.py) ▶️ + audit log |
| Measure realized gains in conversion, speed, capacity | Measure impact on forecast accuracy and seller capacity | 🟪 [impact table](shared_core/ai_governance/README.md#measuring-realized-gains) 📐 · 🟩 [forecast impact design](gtm_strategy_ops/forecasting/forecast-cadence.md#measuring-the-ai-workflows-effect-on-the-forecast) 📐 |

## Theme 3: The domain each role owns

| 🟦 Lead lifecycle & operations | 🟩 Pipeline & forecasting management | Answered by |
|---|---|---|
| Own lead capture, enrichment, scoring, routing, disqualification | Own Salesforce opportunity lifecycle config + DQ standards | 🟦 [lifecycle spec](gtm_engineer/lead_lifecycle/lead-lifecycle-spec.md), [score](gtm_engineer/lead_scoring/score_leads.py) ▶️, [route](gtm_engineer/lead_routing/route_leads.py) ▶️ · 🟩 [stage definitions](gtm_strategy_ops/opportunity_lifecycle/stage-definitions.md) 📐 |
| Translate GTM policies into Salesforce configurations | Manage forecasting cadence, categories, accuracy measurement | 🟦 [routing Flow spec](gtm_engineer/lead_routing/salesforce-routing-flow-spec.md) 📐 · 🟩 [cadence](gtm_strategy_ops/forecasting/forecast-cadence.md) 📐 + [accuracy](gtm_strategy_ops/forecasting/forecast_accuracy.py) ▶️ |
| Improve scoring using conversion outcomes and fit signals | Administer Clari; optimize Salesforce integration | 🟦 [calibration](gtm_engineer/lead_scoring/calibrate_scoring.py) ▶️ · 🟩 [Clari spec](gtm_strategy_ops/clari_admin/clari-configuration-spec.md) 📐 |
| Qualification standards across Marketing, SDRs, AEs | Partner with sales leadership on execution discipline | 🟦 [SQL standard](gtm_engineer/lead_lifecycle/lead-lifecycle-spec.md#qualification-standard-for-sql-shared-by-marketing-sdr-and-ae) 📐 · 🟩 [stage aging + hygiene by owner](gtm_strategy_ops/pipeline_analytics/pipeline_report.py) ▶️ |
| **Platform admin:** Salesforce, Salesloft, Lusha, Clay, Nooks, Qualified, Sales Nav | **Operations:** renewal processes, partner-sourced workflows | 🟦 [Clay + Lusha](gtm_engineer/platform_admin/clay-enrichment-waterfall.md), [engagement layer](gtm_engineer/platform_admin/salesloft-nooks-qualified-salesnav.md) 📐 · 🟩 [renewals](gtm_strategy_ops/renewals/renewal-process.md), [partners](gtm_strategy_ops/partner_ops/partner-sourced-opportunity-workflow.md) 📐 |
| Operationalize ICP segmentation + target-account strategies | Capture closed-lost and churn insights | 🟪 [ICP & personas](shared_core/context/icp-and-personas.md) + [config](config/mitek.yaml) · 🟩 [closed-lost](gtm_strategy_ops/renewals/closed_lost_analysis.py) ▶️ + [taxonomy](gtm_strategy_ops/renewals/closed-lost-and-churn-taxonomy.md) |
| Partner with SDR leadership on capacity and performance | (n/a) | 🟦 [capacity model](gtm_engineer/sdr_capacity/capacity_model.py) ▶️ · [SLA monitor](gtm_engineer/lead_lifecycle/lifecycle_sla.py) ▶️ |

## Theme 4: Cross-functional leadership

| 🟦 asks | 🟩 asks | Answered by |
|---|---|---|
| Operational partner to Marketing, Sales, GTM Systems | Operational partner to sales, finance, customer success | 🟦 [first 90 days](gtm_engineer/first-90-days.md) · 🟩 [first 90 days](gtm_strategy_ops/first-90-days.md) |
| Requirements gathering, process design, solution configuration | Requirements gathering, process design, adoption measurement | 🟪 [object model](shared_core/data_model/salesforce-object-model.md): one owner per field |
| Alignment on data standards and service levels | Influence senior leaders with quantitative analysis | 🟪 [metric definitions](shared_core/metrics/metric-definitions.md) · 🟦 [SLA monitor](gtm_engineer/lead_lifecycle/lifecycle_sla.py) · 🟩 [forecast bias](gtm_strategy_ops/forecasting/forecast_accuracy.py) |

## Theme 5: Qualifications

| 🟦 Required / preferred | 🟩 Required / preferred | Evidence |
|---|---|---|
| 4+ yrs GTM Ops / RevOps / technical GTM | 4+ yrs GTM/Revenue/Sales Ops or technical GTM, B2B SaaS | [about/builder-experience.md](about/builder-experience.md) |
| Strong Salesforce (automation, data governance) | Strong Salesforce (data modeling, automation) | Experience + 🟪 [object model](shared_core/data_model/salesforce-object-model.md) |
| AI-enabled workflows; prompt design, testing, monitoring | AI workflows; prompt engineering and testing | Both tracks' AI workflows, evals in CI |
| Hands-on sales engagement platform | Hands-on forecasting platform, ideally Clari | See [gaps](GAPS_AND_PLACEHOLDERS.md) |
| Lead lifecycle + SDR process design | Influence senior cross-functional leaders | SDR leadership background |
| *Pref:* Lusha, Clay, Nooks, Qualified, Sales Nav | *Pref:* Clari Copilot / conversation intelligence | See [gaps](GAPS_AND_PLACEHOLDERS.md) |
| *Pref:* SQL, BI, warehouse | *Pref:* SQL, BI, warehouse | ▶️ SQL in both tracks |
| *Pref:* GTM app / agent development | *Pref:* GTM app / internal tool development | This repo |
| *Pref:* enterprise ABM in fintech or cybersecurity | *Pref:* Salesloft, Lusha, Sales Nav familiarity | Certa.ai (third-party risk management) |
