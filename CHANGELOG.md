# Changelog

## 0.4.0 (unreleased)
- New `gtm_strategy_ops/sales_leadership/`: VP of Sales brief (snapshot or full), rep scorecard, industry win/loss with 80% confidence ranges, stage velocity with drivers and fixes, deal board, sales all-hands inputs, VP intake questions, SQL.
- New `gtm_strategy_ops/sales_planning/`: AE capacity and hiring plan, quota vs capacity, territory carve and balance, pipeline distribution, CRM request intake process and triage.
- New `gtm_engineer/marketing_ops/`: Marketing Ops RACI, campaign operations spec, channel funnel and ROI, W-shaped attribution, campaign and consent hygiene, demand plan.
- Sample data: `opportunity_field_history.csv`, campaigns, campaign members, lead consent, CRM requests; each uses its own seeded RNG, so existing files are unchanged apart from the open-opportunity stage-entry fix.
- Semantic layer: `v_stage_history`, `v_close_date_pushes`. Config: `sales_team`, `sales_planning`, `sales_leadership`, `marketing_ops`.
- `make brief` and the new reports in `make demo`; tests for all three modules.
- Fix: open opportunities could show a stage entry date before the opportunity existed.

## 0.3.1 (2026-10-06)
- Repository made public. Removed internal prep notes (gaps file, walkthrough script, repo-rules file), rewrote `about/builder-experience.md` to confirmed facts only, and updated the README, role map, wiki and license wording accordingly.

## 0.3.0 (2026-10-05)
- Added a wiki (source in `docs/wiki/`, published with `scripts/publish_wiki.sh`): home, five-minute walkthrough, both role tracks, shared core, architecture, running guide, AI governance, Mitek context, decision log, glossary, roadmap.
- Added repo metadata script (`scripts/set_repo_about.sh`), `LICENSE`, `pyproject.toml` and this changelog.

## 0.2.0 (2026-10-05)
- Clari spec rebuilt from Clari's public documentation; Clari–Salesloft merger (Dec 2025) reflected across the stack docs.
- Company brief: Q3 FY26 figures verified against Mitek's press release and 8-K; new CRO Aaron Seyler and what it means for both roles.
- Builder experience and gaps updated: tool experience, AI builds with results (≈80% of pipeline from signal-based prospecting; win rate ~10% → ~15%; RFP turnaround 1.5–3 weeks → under 2 days).

## 0.1.0 (2026-10-05)
- Initial toolkit: 🟦 GTM Engineer track, 🟩 GTM Strategy & Ops track, 🟪 shared core.
- Mitek config, seeded synthetic data, 12 runnable reports, 3 AI workflows with PII guard, evals and human-review policy.
- Role map, variables, gaps & placeholders; 31 tests including SQL/Python parity and prompt evals; CI.
