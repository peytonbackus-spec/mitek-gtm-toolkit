# Decision Log

Design choices, and the reasoning behind each, so they can be defended or changed on purpose.

| # | Decision | Why | Alternative considered |
|---|---|---|---|
| 1 | **Split the repo at lead conversion** (🟦 / 🟩 / 🟪) | It's where the two postings actually divide, and it matches Salesforce object ownership | One combined toolkit: rejected because it hides which work supports which role |
| 2 | **Shared core built once** | ~40% of the requirements overlap; duplicating them would let definitions drift | Copy into each track |
| 3 | **Two-axis lead score (fit × intent)** | Blended scores hide opposite cases (quiet ideal buyer vs noisy non-buyer) | Single 0–100 score |
| 4 | **Routing as an ordered rule list with a reason stamped on every lead** | The order is the policy; "why did this go to X?" is answerable from the record | Assignment rules without audit trail |
| 5 | **Rules decide deal risk; AI only explains** | Explainable, testable, and nobody has to trust a black box with the forecast | Model-scored risk |
| 6 | **Every revenue-affecting AI action goes to human review** | Forecast categories and disqualifications are too costly to get wrong silently | Confidence-only auto-apply |
| 7 | **Deny-by-default PII guard** | Identity-verification company; prospect data is sensitive by association | Prompt-level instructions only |
| 8 | **Security review and technical validation as their own stage gates** | They're the long poles in bank and fintech IDV deals | Generic 5-stage model |
| 9 | **Renewals forecast separately; check renewals weighted for volume decline** | A large check renewal shouldn't mask a new-business miss; check is in structural decline per management | One blended forecast |
| 10 | **Product-line and partner views from the warehouse, not Clari roll-ups** | Clari rolls up along the Salesforce role hierarchy only | Restructure the role hierarchy (breaks record access) |
| 11 | **No Salesforce formula fields as Clari inputs; Flow-stamped fields instead** | Clari can't consume formula fields | Duplicate logic in Clari |
| 12 | **Mock LLM by default, live mode opt-in** | Runs and tests anywhere with no key and no data leaving the machine | Live-only |
| 13 | **Synthetic, seeded data with planted patterns** | Reproducible demos with real findings (mis-weighted segment, regional forecast bias) | Random data with no signal |
| 14 | **Python + SQL return identical numbers (tested)** | One definition per metric across both roles | Separate reporting stacks |
