# Mitek GTM Toolkit Wiki

**One revenue engine, two owners.** This wiki is the narrative layer on top of the [repository](https://github.com/peytonbackus-spec/mitek-gtm-toolkit). The repo holds the working code and specs; the wiki explains how the pieces fit and why they're built this way.

| | Role | Owns | Start with |
|---|---|---|---|
| 🟦 | **GTM Engineer** | First signal → enrichment → score → route → AI research → SQL | [[GTM Engineer Track]] |
| 🟩 | **GTM Strategy & Operations Manager** | Opportunity → stage gates → deal risk → forecast → close → renewal | [[Strategy and Ops Track]] |
| 🟪 | **Shared Core** | Salesforce data model, data quality, AI governance, metric definitions | [[Shared Core]] |

## Pages

- [[Architecture]]: how data moves from signal to renewal, and where the handoff between roles sits
- [[Running the Toolkit]]: setup, every command, what each report shows
- [[AI Governance]]: the six parts every AI workflow has, and the three workflows in the repo
- [[Mitek Context]]: what Mitek sells, the numbers that matter, and what changed in 2026
- [[Decision Log]]: design choices and the reasoning behind each
- [[Glossary]]: terms used across the repo
- [[Roadmap]]: what I'd build next with real Mitek data

## Ground rules

- **Synthetic data only.** Everything in `sample_data/` is fictional. Mitek facts are sourced in the [company brief](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/context/mitek-company-brief.md).
- **No overclaiming.** What I've done vs what's demonstrated here is laid out in [builder-experience](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/about/builder-experience.md).
