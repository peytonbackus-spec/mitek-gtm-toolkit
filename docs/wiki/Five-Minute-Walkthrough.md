# Five Minute Walkthrough

The order to walk through this work, with one point to make at each stop. It works whether the repo is on screen or you're just talking through the approach (the repo stays private until there's a reason to share it). Pick the track that matches the conversation and spend most of the time there.

| Min | Open | Point to make |
|---|---|---|
| 0:00 | [README](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/README.md), the colour-coded diagram | "Two roles split at lead conversion. Blue owns everything up to an accepted opportunity, green owns everything after. Purple is what both need, built once." |
| 0:45 | [ROLE_MAP.md](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/ROLE_MAP.md) | "Every line of both postings maps to a file. Nothing here is generic filler." |
| 1:30 | Track README: [🟦](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/README.md) or [🟩](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/README.md) | Walk the requirement → artifact table for the role being discussed |
| 2:30 | One runnable script (see below) | Run it live or show the output. Explain one finding it surfaces. |
| 3:30 | [AI workflow standard](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/README.md) | "Every AI workflow has a versioned prompt, a JSON contract, a PII guard, an eval set in CI and a human-review policy. At an identity-verification company, the data boundary isn't optional." |
| 4:15 | [First 90 days](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/first-90-days.md) / [🟩](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/first-90-days.md) | "Measure before building. Here's what I'd baseline in month one and the questions I'd ask in week one." |

## Best script to show, by role

| Role | Script | The finding to point at |
|---|---|---|
| 🟦 | `calibrate_scoring` | It checks whether the lead score actually predicts conversion and flags mis-weighted segments, the "improve scoring using conversion outcomes" line in the posting |
| 🟦 | `funnel_report` | The auto-written narrative and the early-pipeline outlook |
| 🟩 | `deal_risk` | Explainable risk signals (security review, technical validation) → AI commentary → human review queue |
| 🟩 | `forecast_accuracy` | Week 4/8/12 accuracy and the regional bias pattern |

## Real results to connect it to

These are from my work, not the repo (details in [builder-experience](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/about/builder-experience.md)):

- Signal-based prospecting at Certa produced **~80% of pipeline**.
- Deal-risk and pipeline-health scoring: win rate on closed deals went from **~10% to ~15%**.
- Security questionnaire / RFP automation: **1.5–3 weeks → under 2 days**, with human review kept on the parts that needed verification.

## Questions to expect, and where the answer lives

| Question | Answer in |
|---|---|
| "Have you used Clari?" | [Clari spec](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/clari_admin/clari-configuration-spec.md): forecasting method is my experience; Clari mechanics researched |
| "How would you handle data security with AI?" | [PII guard](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/pii_guard.py) + [[AI Governance]] |
| "What would you do first?" | First-90-days plans (linked above) |
| "Why both roles?" | [[Architecture]]: they share a data model, a stack vendor (Clari + Salesloft) and a new CRO |
