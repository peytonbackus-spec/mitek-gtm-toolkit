# Repo rules

## What this repo is
Private toolkit built for Peyton's applications to Mitek Systems' GTM Engineer and GTM Strategy & Operations Manager roles. Three colour-coded areas: 🟦 `gtm_engineer/`, 🟩 `gtm_strategy_ops/`, 🟪 `shared_core/` (both).

## Rules
- **Private.** Don't make it public or share links without Peyton asking.
- **No overclaiming.** Experience claims live only in `about/` and `GAPS_AND_PLACEHOLDERS.md` and must be things Peyton has stated. Unknowns stay `[CONFIRM]`.
- **Company facts need a source.** Add the source to `shared_core/context/mitek-company-brief.md`, or tag the value `[ASSUME]` / `[VERIFY]`.
- **Config, not constants.** Mitek-specific values belong in `config/mitek.yaml`, never hardcoded in scripts.
- **Role placement.** New work goes in the folder of the role it supports. If it supports both, it goes in `shared_core/` and gets linked from both track READMEs and `ROLE_MAP.md`.
- **AI workflows** follow `shared_core/ai_governance/README.md`: a versioned prompt file, a JSON contract, the PII guard, an eval set in `*/evals/`, and a HITL policy.
- **Publishing.** Never commit or push unless explicitly asked in that message.
