# AI Governance

Both postings ask for the same four things: production AI workflows; defined prompts, outputs, evaluation criteria and human-in-the-loop controls; governance for data security; and measured gains. The full standard is in [shared_core/ai_governance/README.md](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/README.md).

## The six parts every AI workflow has

| # | Part | Where |
|---|---|---|
| 1 | Versioned prompt file (id, version, owner, inputs, output keys, rules) | `*/prompts/*.md` |
| 2 | Output contract: JSON with declared keys, or the call fails | [`llm_client.py`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/llm_client.py) |
| 3 | Data boundary: field allow-list plus redaction of emails, phones, SSNs, account and card numbers | [`pii_guard.py`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/pii_guard.py) |
| 4 | Eval set run in CI on every prompt change | [`eval_harness.py`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/eval_harness.py) + `*/evals/*.json` |
| 5 | Human-review policy: what can auto-apply, what always waits for a person | [`hitl.py`](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/hitl.py) |
| 6 | Impact metric with a baseline captured before launch | [AI standard: measuring gains](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/shared_core/ai_governance/README.md#measuring-realized-gains) |

## The three workflows

| Workflow | Role | Model decides? | Always human-reviewed |
|---|---|---|---|
| [Account research brief](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_engineer/ai_research/account_research.py) | 🟦 | Drafts the brief and suggests next action | Disqualify, route to AE |
| [Deal-risk commentary](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/ai_deal_risk/deal_risk.py) | 🟩 | No: rules decide risk; the model explains it | Every flag and every category change |
| [Renewal brief](https://github.com/peytonbackus-spec/mitek-gtm-toolkit/blob/main/gtm_strategy_ops/renewals/renewal_signals.py) | 🟩 | Suggests the play | Escalations |

## Why stricter than usual at Mitek

Mitek's customers send it identity documents, selfies and check images. A GTM team at an identity-verification company that leaked prospect or customer data into a model would be a credibility problem, not just a compliance one. So the default is deny: only allow-listed fields reach a prompt, every call is logged (field names, not values), and live mode needs an explicitly set model and vendor terms approved by security.

## The same pattern in my past work

At Certa I cut security-questionnaire and RFP turnaround from 1.5–3 weeks to under 2 days by automating the routine answers and keeping human review on the parts that needed verification. That's the same human-in-the-loop split this repo encodes in `hitl.py`.
