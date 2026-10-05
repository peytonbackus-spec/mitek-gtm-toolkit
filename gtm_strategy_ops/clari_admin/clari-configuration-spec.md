# Clari Configuration & Salesforce Integration Spec

![Strategy & Ops](https://img.shields.io/badge/role-GTM%20Strategy%20%26%20Ops-2DA44E)

> **Posting:** "Administer Clari platform and optimize Salesforce integration" · "Establish data quality monitoring across Salesforce and Clari" · *Preferred:* "Clari Copilot or conversation intelligence experience"

This is a design spec: how I'd set Clari up so it reads clean Salesforce data and gives the forecast one source of truth.

## Forecast types

| Forecast | Measure | Population | Why separate |
|---|---|---|---|
| **New Business** | Amount | Type ∈ {New Logo, Expansion} | Core growth number |
| **Renewals** | ARR | Type = Renewal | Large check renewals would otherwise hide new-business misses |
| **By Product Line** | Amount | Split by `Product_Line__c` | Mitek reports Check vs Fraud & Identity separately |
| **Partner** | Amount | `Source__c = Partner` | Channel visibility |

## Hierarchy & categories

- The forecast hierarchy mirrors the Salesforce role hierarchy: AE → regional manager → VP (NA, EMEA, APAC/LATAM) → CRO.
- Categories: Pipeline / Best Case / Commit / Closed / Omitted, mapped 1:1 to Salesforce `ForecastCategoryName`. There's no Clari-only category; if a category exists in only one system, the two systems will disagree.
- Commit rules follow the [stage definitions](../opportunity_lifecycle/stage-definitions.md). A Commit in stage 1–2 is flagged (DQ rule O05).

## Sync & data quality

| Check | Frequency | Action |
|---|---|---|
| Clari ↔ Salesforce field mapping drift (stage, category, amount, close date) | Weekly | Reconcile counts and $ by category; investigate any gap > 0.5% |
| Opportunities with Clari activity but no Salesforce activity | Weekly | Activity capture gaps (email/calendar sync) |
| Snapshot export to warehouse | Every Friday | Feeds [`forecast_accuracy.py`](../forecasting/forecast_accuracy.py) |
| Users without Clari access but owning opportunities | Monthly | Licence / provisioning hygiene |

## Clari Copilot (conversation intelligence)

- Trackers for Mitek's deal-risk themes: *security review, POC / pilot, competitor names, budget, deepfake / injection, consortium*. Tracker hits write to the deal timeline.
- **Economic buyer detection:** a meeting with a contact whose persona is an economic buyer (from the 🟪 [persona model](../../shared_core/context/icp-and-personas.md)) can *suggest* `Economic_Buyer_Engaged__c = true` for AE confirmation. It's never set automatically.
- Competitor tracker hits feed the competitive component of the [renewal health model](../renewals/renewal_signals.py).

## AI outputs into Clari

Deal-risk commentary from [`deal_risk.py`](../ai_deal_risk/deal_risk.py) posts to the Clari deal note **only after HITL acceptance**. The note is labelled `[AI-assisted · reviewed by <manager>]`, so nobody mistakes it for the AE's own words.
