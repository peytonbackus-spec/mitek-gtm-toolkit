# ICP, Segments & Buying Committee

![Shared](https://img.shields.io/badge/supports-BOTH%20roles-7B61FF)

The GTM Engineer posting asks to "operationalize ICP segmentation and target-account strategies". The Strategy & Ops posting asks for "analytical views segmented by region, product, source and owner". Both need one segment model that every system shares. This is that model. The machine-readable copy is in [`config/mitek.yaml`](../../config/mitek.yaml) and is the one the code reads.

> **Status:** these are working hypotheses built from Mitek's public positioning. They are not Mitek's internal ICP. In the first 30 days I'd validate them against closed-won data (see the [scoring calibration](../../gtm_engineer/lead_scoring/calibrate_scoring.py) approach).

## Segments

| Segment key | Definition | Fit points | Primary motion | Likely product entry |
|---|---|---|---|---|
| `bank_tier1` | Top-25 US banks | 30 | Enterprise ABM, multi-threaded | Check Fraud Defender (consortium), MiVIP |
| `bank_regional` | US banks with $10B–$250B in assets | 28 | Enterprise ABM | Mobile Deposit → Check Fraud Defender → identity cross-sell |
| `fintech` | Neobanks, lenders, payments, wallets | 26 | Velocity (inbound + SDR) | MiVIP, IDLive, Digital Fraud Defender |
| `igaming` | Sportsbooks, online gaming (age/KYC obligations) | 22 | Velocity | MiVIP, age verification |
| `marketplace` | Two-sided marketplaces, rentals, P2P | 20 | Velocity | IDV and liveness for trust & safety |
| `bank_community` | US banks under $10B | 18 | Partner-led (Fiserv, CSI, Abrigo) | Mobile Deposit, Check Fraud Defender via core provider |
| `credit_union` | Credit unions | 18 | Partner-led | Same as community banks |
| `adjacent_regulated` | Insurance, healthcare, government | 12 | Partner-led (new markets per Q3 call) | MiVIP |
| `other` | Non-ICP | 0 | Nurture or disqualify | — |

## Anti-ICP (disqualify or nurture)

- No regulated onboarding, payments or deposit flow, so no fraud/IDV use case.
- Under roughly 20 employees and outside a partner channel. They can't fund an enterprise IDV deployment.
- Researchers, students, job seekers and vendors (a common source of inbound noise).
- An open opportunity already exists on the account. Route it to the owner; don't create a new lead.

## Buying committee

| Persona key | Typical titles | Role in deal | What they care about |
|---|---|---|---|
| `head_of_fraud` | VP Fraud Strategy, Head of Fraud Prevention | Economic buyer | Fraud loss rate, false positives, deepfake/injection exposure |
| `ciso_identity` | CISO, Director IAM | Economic buyer | Account takeover, passwordless (MiPass), vendor security posture |
| `head_of_digital_banking` | SVP Digital Banking, Head of Deposits | Economic buyer (check) | Mobile deposit experience, deposit growth, abandonment |
| `trust_and_safety` | Head of Trust & Safety | Economic buyer (marketplace) | Fake accounts, scams, conversion of genuine users |
| `fintech_product` | VP Product, Onboarding | Champion | Onboarding conversion, pass rates, time to verify |
| `risk_compliance` | CRO, BSA/AML, KYC Ops | Influencer / veto | KYC/AML defensibility, audit trail, regulator expectations |
| `fraud_analyst` | Fraud Manager, Analyst | Champion / user | Case volume, tooling, explainability |
| `procurement_it` | Vendor Risk, Architecture | Blocker / gate | Security review, data residency, integration effort |

**Why it matters for Strategy & Ops:** stage 3+ deals without an economic buyer engaged are flagged by both the [data-quality monitor](../data_quality/dq_monitor.py) (rule O06) and the [deal-risk model](../../gtm_strategy_ops/ai_deal_risk/deal_risk.py).

**Why it matters for the GTM Engineer:** persona points feed the fit axis of the [lead score](../../gtm_engineer/lead_scoring/score_leads.py). Persona is derived from title with the Clay title-normaliser described in the [Clay waterfall spec](../../gtm_engineer/platform_admin/clay-enrichment-waterfall.md).
