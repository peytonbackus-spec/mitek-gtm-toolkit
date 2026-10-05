# Clari Configuration & Salesforce Integration Spec

![Strategy & Ops](https://img.shields.io/badge/role-GTM%20Strategy%20%26%20Ops-2DA44E)

> **Posting:** "Administer Clari platform and optimize Salesforce integration" · "Establish data quality monitoring across Salesforce and Clari" · *Preferred:* "Clari Copilot or conversation intelligence experience"

This is a design spec: how I'd set Clari up so it reads clean Salesforce data and gives the forecast one source of truth. It's based on Clari's public documentation and community material (sources at the bottom), not on hands-on Clari administration. The forecasting method underneath (win-rate-based coverage, deal-risk scoring, accuracy measurement) is work I've done; the Clari-specific mechanics are researched.

## Platform context: Clari and Salesloft are one company now

Clari and Salesloft completed their merger on **Dec 3, 2025**. Clari Forecast and Inspect now sit in the same platform as Salesloft Cadence, Deals, Conversation Intelligence, Rhythm and Analytics, on what the company calls a unified revenue data layer synced with Salesforce.

What this means at Mitek, where both tools are in the stack:

- **The two roles share a vendor.** Salesloft (🟦 GTM Engineer) and Clari (🟩 Strategy & Ops) increasingly read the same data. A cadence change or an activity-logging gap shows up in forecast signals, so the roles need one activity-capture standard (see the 🟪 [stack map](../../shared_core/context/gtm-stack-map.md)).
- **Two conversation-intelligence products may now overlap:** Clari Copilot and Salesloft Conversation Intelligence. Week-one question: which one does Mitek actually record calls in? `[VERIFY]`
- **Integration risk drops.** Engagement activity and forecast data should line up with less custom plumbing than two separate vendors would need.

## Modules and what each is for at Mitek

| Module | What it does | Mitek use |
|---|---|---|
| **Forecast** | Roll-up forecasting: reps submit calls, managers roll up, with categories, waterfall (movement and slippage) views and historical trending | Weekly forecast calls; week 4/8/12 accuracy |
| **Inspect** | Pipeline inspection and deal risk: changes, CRM Score, engagement, next steps | Manager deal reviews; complements [`deal_risk.py`](../ai_deal_risk/deal_risk.py) |
| **Copilot** | Call recording, transcription, trackers, summaries | Deal-risk themes; economic-buyer evidence |
| **Activity capture** | Email and calendar sync into the deal timeline | Feeds engagement signals; this is what makes "No activity in 30d" trustworthy |

## Hierarchy: the constraint to design around

Clari's forecast rolls up along the **Salesforce role hierarchy**. That's the only roll-up path. It works well for the people view (AE → manager → VP → CRO), but it has consequences:

| Need | Solved in Clari natively? | How I'd handle it |
|---|---|---|
| AE → regional manager → VP (NA, EMEA, APAC/LATAM) → CRO | ✅ Yes | Keep the Salesforce role hierarchy clean and current. A rep in the wrong role puts their pipeline in the wrong roll-up. |
| New business vs renewals | ✅ Separate forecast tabs filtered by `Type` | Two tabs: New Business (New Logo + Expansion) and Renewals |
| Check vs Fraud & Identity (Mitek's two reported segments) | ⚠️ Filtered tabs work, but managers still get one roll-up per tab | Product-line tabs for visibility; the official product-line forecast for Finance comes from the warehouse, built off Clari snapshots + `Product_Line__c` |
| Partner-sourced pipeline across all managers | ⚠️ Cuts across the hierarchy | Partner view in the warehouse / BI layer ([pipeline report](../pipeline_analytics/pipeline_report.py) `source` dimension), not as a Clari roll-up |

Seyler's newly unified GTM org (sales, channel, CS, SE, PS) makes this matter more. Channel and renewals now report into the same CRO as direct sales, so the hierarchy has to be designed on purpose.

## Categories

- Pipeline / Best Case / Commit / Closed / Omitted, mapped 1:1 to Salesforce `ForecastCategoryName`. No Clari-only category: if a category exists in only one system, the two systems will disagree.
- Commit rules follow the [stage definitions](../opportunity_lifecycle/stage-definitions.md). A Commit in stage 1–2 is flagged (DQ rule O05).
- Rep calls vs manager overrides are both kept. The gap between them, over time, is one of the inputs to the [bias analysis](../forecasting/forecast_accuracy.py).

## Salesforce field rules for Clari

| Rule | Why |
|---|---|
| **No formula fields as Clari inputs.** Mirror anything Clari needs (e.g. days in stage, risk level) into a real field stamped by Flow. | Clari can't consume Salesforce formula fields directly. This is the most-cited admin pain point. The 🟪 [object model](../../shared_core/data_model/salesforce-object-model.md) already uses Flow-stamped fields for this reason. |
| Validation rules live in Salesforce only, never duplicated as Clari logic | Rules in two places drift |
| Keep Clari-synced field count lean, and every field has an owner | API limits and sync lag grow with field count |
| Picklist values mirrored in `config/mitek.yaml` | Code, Salesforce and Clari share one definition |

## Sync & data quality

| Check | Frequency | Action |
|---|---|---|
| Clari ↔ Salesforce totals by forecast category (count and $) | Weekly, before the Wednesday call | Investigate any gap > 0.5%; usually sync lag or a field-mapping change |
| Opportunities with Clari activity but no Salesforce activity | Weekly | Activity-capture gaps (email/calendar sync, unlicensed users) |
| Role-hierarchy changes vs forecast roll-up | On every org change | Reps moved in HR but not in Salesforce roles roll up to the wrong manager |
| Snapshot export to warehouse | Every Friday | Feeds [`forecast_accuracy.py`](../forecasting/forecast_accuracy.py) and the product-line / partner views above |
| Users owning opportunities without Clari access | Monthly | Licence / provisioning hygiene |

## Deal inspection: how the repo's deal-risk model fits with Clari's

Clari's documented deal-inspection approach has four parts: what changed (7/14/30-day views), win likelihood (**CRM Score**, a confidence score for closing as won), engagement and relationships (AI summary from email and meetings), and next steps (Smart CRM Suggestions that update methodology fields from call transcripts).

[`deal_risk.py`](../ai_deal_risk/deal_risk.py) doesn't replace this. It adds what Clari's native score doesn't make explicit:

| Clari native | Repo deal-risk model | Combined use |
|---|---|---|
| CRM Score (a probability; how it's derived isn't visible to users) | Named, explainable rules ("security review not started at stage 4+") | Use CRM Score as one input; the rules explain *why* in language a manager can act on |
| Generic engagement signals | Mitek-specific gates: technical validation (POC) and bank security review | Mitek's long poles get first-class signals |
| Smart CRM Suggestions from transcripts | HITL policy: AI may *suggest* `Economic_Buyer_Engaged__c`, never set it | Same idea; the repo makes the review step explicit |

## Copilot (conversation intelligence)

- Trackers for Mitek's deal-risk themes: *security review, POC / pilot, competitor names (e.g. Jumio, Onfido), budget, deepfake / injection, consortium*. Tracker hits write to the deal timeline.
- **Economic-buyer detection:** a meeting with a contact whose persona is an economic buyer (from the 🟪 [persona model](../../shared_core/context/icp-and-personas.md)) can *suggest* `Economic_Buyer_Engaged__c = true` for AE confirmation. It's never set automatically.
- Competitor tracker hits feed the competitive component of the [renewal health model](../renewals/renewal_signals.py).
- My conversation-intelligence experience is Gong: qualification validation and objection-trend tracking. Same category, same uses.

## AI outputs into Clari

Deal-risk commentary from [`deal_risk.py`](../ai_deal_risk/deal_risk.py) posts to the Clari deal note **only after HITL acceptance**. The note is labelled `[AI-assisted · reviewed by <manager>]`, so nobody mistakes it for the AE's own words.

## Week-one questions

1. Which conversation-intelligence tool records calls today: Clari Copilot, Salesloft Conversation Intelligence, or both?
2. Are renewals already a separate forecast tab?
3. Does the Salesforce role hierarchy match the new unified GTM org under the CRO?
4. Who administers Clari today, and how many Salesforce formula fields are being worked around?

## Sources

- [Clari and Salesloft complete merger (Dec 3, 2025)](https://www.salesloft.com/company/newsroom/clari-salesloft-merger)
- [Salesloft platform overview (Clari Forecast, Inspect, Cadence, CI, unified data layer)](https://www.salesloft.com/platform-overview)
- [Clari community: the 4-point deal inspection](https://community.clari.com/best-practices-learnings-wins-tips-70/transform-your-deal-reviews-the-all-new-4-point-deal-inspection-2287)
- [Forecasting outside the Salesforce role hierarchy (Weflow, a competitor; on the role-hierarchy roll-up constraint)](https://www.weflow.ai/blog/forecasting-outside-salesforce-role-hierarchy-clari)
- [Clari feature analysis (Oliv, a competitor; on modules and the formula-field admin pitfall)](https://www.oliv.ai/blog/clari-features)
