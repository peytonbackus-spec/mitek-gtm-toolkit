# Clay + Lusha Enrichment Waterfall

![GTM Engineer](https://img.shields.io/badge/role-GTM%20Engineer-1F6FEB)

> **Posting:** "Administer and optimize Clay, Lusha… LinkedIn Sales Navigator" · "Design production-ready AI workflows for account research, enrichment…" · "Connect AI capabilities to GTM systems via low-code tools and APIs"

The table that turns a raw lead into a routable, scorable record within 15 minutes of creation.

## Table: `Inbound Lead Enrichment` (triggered by Salesforce webhook on Lead create)

| # | Column | Provider / method | Runs when | Writes to Salesforce |
|---|---|---|---|---|
| 1 | Normalize domain | Formula (strip www, map personal domains to blank) | always | — |
| 2 | Account match | Salesforce lookup by domain → fuzzy name | domain present | `Matched_Account__c` |
| 3 | Firmographics | Clay company enrichment | no matched account, or account fields empty | `Segment__c`, `NumberOfEmployees`, `Region__c` |
| 4 | **Bank assets** | FDIC / NCUA public data by institution name | segment is a bank or credit union | `Total_Assets__c` (sizes banks properly; employees mislead) |
| 5 | Segment classifier | Clay AI column: classify into the 9 segment keys, with a confidence output | 3 returned an industry | `Segment__c` if confidence ≥ 0.8, otherwise flag |
| 6 | Title → persona | Clay AI column: map title to the 9 persona keys (prompt pinned, eval'd on 50 labelled titles) | title present | `Persona__c` |
| 7 | Email verify | Clay native verification | email present | `Email_Status__c` |
| 8 | Contact data | **Lusha** (direct dial + verified email) | persona is an economic buyer or champion **and** fit ≥ B | `Phone`, `MobilePhone` |
| 9 | Fallback contact | Second provider in the waterfall | Lusha miss | same fields |
| 10 | Signals | Job postings (fraud and identity roles), news (fraud loss, consent order), Sales Nav job change | ICP segment | `Intent_Signals_clay__c` |
| 11 | Score + route | HTTP column → scoring service ([`score_leads.py`](../lead_scoring/score_leads.py)) | 1–10 done | `Fit_Score__c`, `Intent_Score__c`, `Lead_Grade__c` |

## Cost guardrails

- **Lusha runs only on leads worth calling** (step 8 condition). Spending phone credits on D-grade leads is the most common avoidable waterfall cost.
- **Empty-field-only writes.** Clay never overwrites a rep-entered value. Conflicts go to a `_clay` suffixed field for review.
- **Credit budget per lead source**, reviewed monthly against pipeline per lead from the [funnel report](../funnel_analytics/funnel_report.py). A source with low pipeline per lead gets a cheaper waterfall.

## Quality checks (weekly)

| Check | Target |
|---|---|
| Segment classifier agreement with AE-corrected segment | ≥ 90% |
| Persona mapping accuracy on the labelled set | ≥ 92% |
| Lusha direct-dial connect rate (from Nooks outcomes) | Track per segment; drop the provider for any segment below the fallback |
| Leads stuck in Enriching > 15 min | 0 |
