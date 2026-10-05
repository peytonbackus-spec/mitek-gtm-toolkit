# Mitek Company Brief (GTM lens)

![Shared](https://img.shields.io/badge/supports-BOTH%20roles-7B61FF)

> Built from public sources on **Oct 5, 2026**. Q2 and Q3 FY26 figures are verified against Mitek's own press releases (the Q3 release is also filed as an 8-K exhibit). Three figures marked *call coverage* come only from third-party write-ups of the Q3 earnings call. Treat those as approximate.

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
| FY26 Q3 revenue (qtr ended Jun 30, 2026) | **$54.0M, +18% YoY** | Q3 press release / 8-K |
| FY26 Q3 Fraud & Identity | $29.0M, +14%; F&I **SaaS $24.8M, +37%** | Q3 press release |
| FY26 Q3 Check Verification | $25.0M, +24% (management expects check to decline over time) | Q3 press release; decline comment from call coverage |
| FY26 Q3 total SaaS revenue | $26.2M, +36% | Q3 press release |
| FY26 Q2 revenue (qtr ended Mar 31, 2026) | $54.8M; Fraud & Identity $25.7M (+28%); Check $29.1M; SaaS $21.2M (+18%) | Q2 press release |
| FY26 guidance (raised at Q3) | Revenue $195–200M (~10% growth); Fraud & Identity $105–109M (~19%); adj. EBITDA margin 32–34% | Q3 press release |
| Check Fraud Defender consortium | A top-five US bank completed its pilot and joined the consortium in Q3 | Q3 press release |
| Channel | Partner and reseller channel "materially expanded… within reach of thousands of additional financial institutions"; Fiserv live as reseller; Abrigo, CSI, Data Advisor; FICO Marketplace listing | Q3 press release (quote); partner names from call coverage and FICO Marketplace |
| Check Fraud Defender ACV | >$22M, +73% YoY | *call coverage* |
| Consortium data coverage | ~70% of US checking accounts | *call coverage* |
| SaaS share of TTM revenue | ~46% (from ~41%) | *call coverage* |
| **New CRO** | **Aaron Seyler, effective Aug 17, 2026.** Leads a newly unified GTM org: sales, channel partnerships, customer success and support, sales engineering and professional services. Previously ran a 17-country GTM org at Vonage (API business, partner and channel heavy), and before that GTM at Telesign (digital identity and fraud), where revenue grew from ~$200M to $600M+. | Q3 press release; trade coverage |
| Leadership | Ed West (CEO), Dave Lyle (CFO), Mark Rossi (non-executive Chairman from Oct 1, 2026); ethos "Unify and Grow" | Press releases |

Mitek's fiscal year ends **September 30**. The forecast tooling in this repo uses Mitek fiscal quarters (FY26 Q4 = Jul–Sep 2026).

## What this means for the two roles (my read, not Mitek's)

| Shift | Why it matters | GTM Engineer 🟦 | Strategy & Ops 🟩 |
|---|---|---|---|
| License to SaaS | Recurring revenue makes renewals, usage telemetry and forecast accuracy matter more | Usage and intent signals feed lead scoring | [Renewal signals](../../gtm_strategy_ops/renewals/), [forecast accuracy](../../gtm_strategy_ops/forecasting/) |
| "Unify": cross-selling identity into the check base | Expansion pipeline from existing bank customers is the cheapest growth | Routing sends existing customers to the account owner, not the SDR pool | Expansion is its own opportunity type with its own coverage line |
| Channel scale (Fiserv, Abrigo, CSI) | Community banks and credit unions arrive through partners, so attribution breaks easily | Partner-referral leads route to a partner manager | [Partner-sourced opportunity workflow](../../gtm_strategy_ops/partner_ops/) |
| Check volume is in secular decline (management said so) | Check renewals carry structural downside risk | n/a | Renewal health weights volume trend first |
| GenAI fraud (deepfakes, injection) | Creates new urgency at fintechs and marketplaces, and a fast-moving signal set | Intent signals: deepfake webinar, fraud-team hiring, fraud-leader job change | Deal-risk model accounts for long technical validations (POCs) |
| **New CRO unifying sales, channel, CS, SE and PS (Aug 2026)** | A new revenue leader merging five functions usually triggers a rebuild of stage definitions, forecast cadence, routing and reporting. That's probably why both roles exist now. His background is identity/fraud and channel-led API scaling. | Routing and lead lifecycle get redesigned across direct and channel | Forecast cadence, stage gates, partner workflow, CS renewal process in one operating rhythm |
| Regulation-driven demand (e.g. EMEA age verification) | Demand spikes come from external events | Event-based signals in Clay | Region-level forecast variance |

## Sources

- [Mitek homepage and product pages](https://www.miteksystems.com/)
- [Mitek FY26 Q2 results press release](https://www.miteksystems.com/press-releases/mitek-reports-record-fiscal-2026-second-quarter-results-raises-full-year-outlook)
- [Mitek FY26 Q3 results press release](https://www.miteksystems.com/press-releases/mitek-reports-fiscal-third-quarter-revenue-of-540-million-up-18-year-over-year) · [8-K exhibit 99.1 (SEC)](https://www.sec.gov/Archives/edgar/data/807863/000080786326000035/mitk-20260630xexx991xq326e.htm)
- [FY26 Q3 earnings call highlights (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/mitek-systems-inc-mitk-q3-050554552.html)
- [Mitek appoints Aaron Seyler as CRO (Yahoo Finance)](https://finance.yahoo.com/technology/articles/mitek-appoints-aaron-seyler-chief-215400010.html) · [background coverage](https://theaisoftwarereport.com/former-vonage-executive-aaron-seyler-takes-helm-as-mitek-chief-revenue-officer/)
- [Digital Fraud Defender launch](https://www.miteksystems.com/press-releases/mitek-unveils-digital-fraud-defender-next-gen-defense-against-deepfakes-and-emerging)
- [MiVIP on FICO Marketplace](https://marketplace.fico.com/mitek-verified-identity-platform-mivip)
- Job postings: [GTM Engineer](https://jobs.lever.co/miteksystems-2/45e6c07b-c64d-4bc1-93dd-caf9e7b649ed), [GTM Strategy and Operations Manager](https://jobs.lever.co/miteksystems-2/158d6add-b1b5-4de6-aaa4-5975e241766d)
