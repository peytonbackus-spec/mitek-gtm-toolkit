# Mitek Company Brief (GTM lens)

![Shared](https://img.shields.io/badge/supports-BOTH%20roles-7B61FF)

> Built from public sources on **Oct 5, 2026**. Figures marked *call coverage* come from third-party write-ups of the FY26 Q3 earnings call. Verify them against the 10-Q before quoting them in an interview.

## What Mitek sells

Mitek reports revenue in two segments. Every scoring, routing and forecasting script in this repo keys off the same split (`product_lines` in [`config/mitek.yaml`](../../config/mitek.yaml)).

| Product line | Products | What it does |
|---|---|---|
| **Check Verification** | Mobile Deposit, Check Fraud Defender, Check Intelligence, Positive Pay Plus | Mobile check capture, plus check fraud detection backed by a consortium data network |
| **Fraud & Identity** | MiVIP (Verified Identity Platform), IDLive Face, IDLive Doc, MiPass, Digital Fraud Defender | Identity verification across onboarding, login and transactions; passive liveness; biometric authentication; GenAI-era fraud defence (deepfakes, injection attacks, synthetic identities) |

Tagline: **"Protect what's real."** Mitek says more than 7,000 organizations use its products. Its main markets are banking, fintech, digital marketplaces and iGaming.

## Numbers that shape the GTM job

| Metric | Value | Source |
|---|---|---|
| FY26 Q2 revenue (qtr ended Mar 31, 2026) | $54.8M; Fraud & Identity $25.7M (+28% YoY); Check $29.1M; SaaS $21.2M (+18%) | Mitek press release |
| FY26 Q3 Fraud & Identity SaaS growth | ~37% YoY; total SaaS ~+36% | *call coverage* |
| Check Fraud Defender ACV | >$22M, +73% YoY | *call coverage* |
| Consortium data network | ~70% of US checking accounts | *call coverage* |
| SaaS share of TTM revenue | ~46% (from ~41% a year earlier) | *call coverage* |
| Financial services share of revenue | ~80% | *call coverage* |
| FY26 guidance (raised at Q3) | Revenue $195–200M; Fraud & Identity $105–109M | *call coverage* |
| Channel | Fiserv live as a reseller; Abrigo, CSI and Data Advisor partnerships; FICO Marketplace listing | *call coverage*, FICO Marketplace |
| Leadership | Ed West (CEO), Dave Lyle (CFO); stated ethos "Unify and Grow" | Press release / call |

Mitek's fiscal year ends **September 30**. The forecast tooling in this repo uses Mitek fiscal quarters (FY26 Q4 = Jul–Sep 2026).

## What this means for the two roles (my read, not Mitek's)

| Shift | Why it matters | GTM Engineer 🟦 | Strategy & Ops 🟩 |
|---|---|---|---|
| License to SaaS | Recurring revenue makes renewals, usage telemetry and forecast accuracy matter more | Usage and intent signals feed lead scoring | [Renewal signals](../../gtm_strategy_ops/renewals/), [forecast accuracy](../../gtm_strategy_ops/forecasting/) |
| "Unify": cross-selling identity into the check base | Expansion pipeline from existing bank customers is the cheapest growth | Routing sends existing customers to the account owner, not the SDR pool | Expansion is its own opportunity type with its own coverage line |
| Channel scale (Fiserv, Abrigo, CSI) | Community banks and credit unions arrive through partners, so attribution breaks easily | Partner-referral leads route to a partner manager | [Partner-sourced opportunity workflow](../../gtm_strategy_ops/partner_ops/) |
| Check volume is in secular decline (management said so) | Check renewals carry structural downside risk | n/a | Renewal health weights volume trend first |
| GenAI fraud (deepfakes, injection) | Creates new urgency at fintechs and marketplaces, and a fast-moving signal set | Intent signals: deepfake webinar, fraud-team hiring, fraud-leader job change | Deal-risk model accounts for long technical validations (POCs) |
| Regulation-driven demand (e.g. EMEA age verification) | Demand spikes come from external events | Event-based signals in Clay | Region-level forecast variance |

## Sources

- [Mitek homepage and product pages](https://www.miteksystems.com/)
- [Mitek FY26 Q2 results press release](https://www.miteksystems.com/press-releases/mitek-reports-record-fiscal-2026-second-quarter-results-raises-full-year-outlook)
- [FY26 Q3 earnings call highlights (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/mitek-systems-inc-mitk-q3-050554552.html)
- [Digital Fraud Defender launch](https://www.miteksystems.com/press-releases/mitek-unveils-digital-fraud-defender-next-gen-defense-against-deepfakes-and-emerging)
- [MiVIP on FICO Marketplace](https://marketplace.fico.com/mitek-verified-identity-platform-mivip)
- Job postings: [GTM Engineer](https://jobs.lever.co/miteksystems-2/45e6c07b-c64d-4bc1-93dd-caf9e7b649ed), [GTM Strategy and Operations Manager](https://jobs.lever.co/miteksystems-2/158d6add-b1b5-4de6-aaa4-5975e241766d)
