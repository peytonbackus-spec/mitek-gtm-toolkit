# Variables: Generic Toolkit → Mitek

My base toolkit is company-agnostic and uses bracketed variables like `[COMPANY_NAME]` and `[ACV_RANGE]`. This repo is the Mitek instance. Every variable is resolved below, and the machine-readable values live in [`config/mitek.yaml`](config/mitek.yaml), which every script reads.

**Provenance:** `PUBLIC` = Mitek site, press release or earnings coverage · `POSTING` = the two Lever postings · `ASSUME` = my working assumption, to validate in the first 30 days · `VERIFY` = from general knowledge, needs checking before use in an interview

| Variable | Mitek value | Provenance | Used in |
|---|---|---|---|
| `[COMPANY_NAME]` | Mitek Systems (NASDAQ: MITK) | PUBLIC | everywhere |
| `[TAGLINE]` | "Protect what's real" | PUBLIC | company brief |
| `[PRIMARY_PRODUCT_SUITE]` | Two lines. **Check Verification:** Mobile Deposit, Check Fraud Defender, Check Intelligence, Positive Pay Plus. **Fraud & Identity:** MiVIP, IDLive Face/Doc, MiPass, Digital Fraud Defender | PUBLIC | `product_lines`, scoring alignment, AI prompts |
| `[SEGMENTS]` | Top-25 banks, regional banks, community banks, credit unions, fintech, marketplaces, iGaming, adjacent regulated (insurance / healthcare / gov) | PUBLIC (markets) + ASSUME (tier cut-offs) | `segments`, routing pods, all reports |
| `[TARGET_BUYER_PERSONA]` | Head of Fraud, CISO/IAM, Head of Digital Banking, Trust & Safety (economic buyers); Risk/BSA-AML (influencer); Fintech product (champion); Procurement/Vendor Risk (gate) | ASSUME from public positioning | `personas`, fit score, deal-risk EB rule |
| `[PRIMARY_PARTNER_ECOSYSTEM]` | Fiserv (reseller), Abrigo, CSI, Data Advisor, FICO Marketplace | PUBLIC | routing R4, partner workflow |
| `[REGIONS]` | NA, EMEA, APAC, LATAM | PUBLIC (EMEA demand noted) + ASSUME (split) | quota, forecast, pods |
| `[FISCAL_YEAR_END]` | September 30 (FY27-Q1 = Oct–Dec 2026) | PUBLIC | fiscal quarter logic (Python + SQL) |
| `[CRM]` | Salesforce | POSTING | object model, Flows |
| `[FORECAST_TOOL]` | Clari + Clari Copilot | POSTING | forecast cadence, Clari spec |
| `[SEQUENCER]` / `[DIALER]` | Salesloft / Nooks | POSTING | engagement layer spec |
| `[ENRICHMENT_STACK]` | Clay (orchestration) + Lusha (contact data) + Sales Navigator (signals) | POSTING | waterfall spec |
| `[WEBSITE_CONVERSION]` | Qualified | POSTING | intent signals, routing |
| `[PRIMARY_SIGNAL_TRIGGERS]` | Demo request, Qualified chat, pricing page, deepfake webinar, check-fraud content, fraud-leader job change, fraud-team hiring, competitor contract-renewal window | ASSUME | `lead_scoring.intent_signals` |
| `[ACV_RANGE]` | ~$20K (credit union) to $900K (Top-25 bank) by segment | ASSUME, illustrative only | sample data generator |
| `[SALES_CYCLE_LENGTH]` | ~60–200 days, ~1.6x longer for Top-25 banks; technical validation and security review are the long poles | ASSUME | stage max-days, deal-risk rules |
| `[REVENUE_CONTEXT]` | FY26 revenue guidance $195–200M; Fraud & Identity growing faster than Check; SaaS ~46% of TTM revenue | PUBLIC (call coverage) | company brief, renewal weighting |
| `[STRATEGIC_THEMES]` | "Unify and Grow"; check consortium network effects; GenAI-era fraud; channel expansion | PUBLIC | expansion routing, renewals, signals |
| `[REGULATORY_CONTEXT]` | KYC/AML, age verification (EMEA demand), bank vendor-risk reviews; CASL/GDPR for outreach | PUBLIC + ASSUME | personas, security-review stage gate, cadence rules |
| `[COMPETITORS]` | Placeholder labels in sample data ("Competitor A (IDV)" etc.). Vendors commonly compared in IDV include Jumio, Socure, Entrust/Onfido, Persona, Incode and AU10TIX | VERIFY | closed-lost analysis |
| `[QUOTA]` | FY27-Q1: NA $1.6M, EMEA $450K, APAC $180K, LATAM $120K | ASSUME, sized to the synthetic data only | coverage report |

## Changing a variable

Edit `config/mitek.yaml` and re-run `make demo`. Segment weights, persona points, stage limits, SLAs, health weights and quota all flow through. Nothing is hardcoded in the scripts.
