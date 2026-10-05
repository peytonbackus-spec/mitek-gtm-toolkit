# Sales Engagement Layer: Salesloft · Nooks · Qualified · Sales Navigator

![GTM Engineer](https://img.shields.io/badge/role-GTM%20Engineer-1F6FEB)

> **Posting:** "Administer and optimize Salesforce, Salesloft, Lusha, Clay, Nooks, Qualified and LinkedIn Sales Navigator" · "Hands-on sales engagement platform experience" · "Lead lifecycle and SDR process design"

This is a design spec: how I would configure each tool so it reinforces the lead lifecycle instead of running its own version of it.

## Salesloft: cadence architecture

**Principle:** a small set of cadences keyed to *segment × product line × intent*. Not one per rep.

| Cadence | Entry | Steps (days) | Exit |
|---|---|---|---|
| `HR-Hand-Raise` | Demo request or Qualified chat (any ICP) | Call + email within 1h, then D1, D3, D6 (6 touches) | Meeting booked → SQL path; no response → `Working-Std` |
| `BANK-Check-Fraud` | Bank/CU, check interest, MQL | 9 touches / 18 days; references to the consortium network | Meeting / Recycle |
| `BANK-Identity-XSell` | Existing check customer, identity signal | AE-owned, 5 touches, exec-sponsor email | Expansion opp |
| `FINTECH-IDV` | Fintech, marketplace or iGaming MQL | 8 touches / 14 days; deepfake / injection angle | Meeting / Recycle |
| `ABM-Tier1` | Top-25 bank target account, A3/A4 | Multi-thread: 3 personas in parallel, LinkedIn steps | Meeting / quarterly re-enroll |

**Config standards**

- Cadence enrollment writes `Status = Working` and a `Cadence__c` stamp through the Salesforce sync. Cadence membership is reportable.
- Personalization variables (`{{use_case}}`, `{{persona_angle}}`) are populated from the [AI research brief](../ai_research/account_research.py) **after HITL acceptance only**.
- Bounce or opt-out removes the person from every cadence and sets `HasOptedOutOfEmail`. CASL and GDPR rules apply to the EMEA pod.
- Enrollment automation (rules that auto-add MQLs to a cadence) is the one piece I haven't built in production before. I'd pilot it on `HR-Hand-Raise` first, with SDR override, and measure speed-to-lead before and after.

## Nooks: dialer

- Call lists are generated from Salesforce views sorted by `Lead_Grade__c`, never from static CSVs.
- Dispositions map 1:1 to Salesforce task outcomes (`Connected-Meeting`, `Connected-NotNow`, `Wrong Number`, `Gatekeeper`…). The connect rate per data provider feeds the [waterfall](clay-enrichment-waterfall.md) review.
- Power-hour blocks are aligned to regional calling windows by pod.

## Qualified: website conversion

- Routing on Qualified uses the same pod rules. A known customer visiting goes to the AE, a known open opp goes to the opp owner, and an ICP fit goes to the live SDR.
- The Qualified "engaged" event writes `qualified_chat_engaged@date` to the signal log, which carries the highest intent weight after a demo request.
- Meetings booked in Qualified skip MQL and go straight to SAL with a 1-hour first-touch SLA.

## LinkedIn Sales Navigator

- Saved account lists mirror the Salesforce segments: one list per pod.
- Job-change alerts for `head_of_fraud` / `ciso_identity` personas at ICP accounts feed Clay as `fraud_leader_job_change`, an 18-point signal with a 60-day half-life.
- CRM sync is on, so InMail and connection activity logs to Salesforce as activity.
