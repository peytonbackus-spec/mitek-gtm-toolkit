"""AI account research + qualification brief (production pattern, offline by default).

GTM Engineer posting: "Design production-ready AI workflows for account research,
enrichment, qualification and routing", "Connect AI capabilities to GTM systems
via low-code tools and APIs", "Define prompts, outputs, evaluation criteria and
human-in-the-loop controls".

Flow (one record):
  Salesforce lead/account -> pii_guard (allow-list + redaction) -> versioned prompt
  -> LLM (mock or live) -> JSON contract check -> HITL policy -> review queue
  -> (on Accept) write brief to Salesforce + Salesloft cadence variable

In production the trigger is a Salesforce Flow / Clay HTTP column calling this as
a small API (or an n8n workflow). The Python is the same either way.

    python -m gtm_engineer.ai_research.account_research            # mock mode, no API key
    GTM_LLM_MODE=anthropic ANTHROPIC_MODEL=<model> python -m ...   # live mode
"""
from __future__ import annotations

from pathlib import Path

from gtm_engineer.lead_scoring.score_leads import score_all
from shared_core.ai_governance.hitl import HITLPolicy, write_queue
from shared_core.ai_governance.llm_client import LLMClient, load_prompt
from shared_core.config import load_config, read_csv, table, to_bool

PROMPT_PATH = Path(__file__).parent / "prompts" / "account_research.md"
REQUIRED_KEYS = ["summary", "likely_use_case", "recommended_products", "persona_angle", "qualification",
                 "evidence", "unknowns", "next_action", "confidence"]

USE_CASES = {
    "bank_tier1": "Check fraud consortium coverage + digital account-opening identity verification",
    "bank_regional": "Mobile deposit modernization and check fraud loss reduction",
    "bank_community": "Mobile deposit + check fraud via core-provider channel",
    "credit_union": "Mobile deposit + check fraud via core-provider channel",
    "fintech": "Onboarding identity verification with deepfake / injection-attack defense",
    "marketplace": "Fake-account and scam prevention at signup (trust & safety)",
    "igaming": "KYC and age verification at onboarding",
    "adjacent_regulated": "Remote identity proofing for member/patient/citizen portals",
}
ANGLES = {
    "head_of_fraud": "Fraud loss and false-positive trade-off; GenAI-era attack vectors",
    "ciso_identity": "Account-takeover resistance and passwordless authentication",
    "head_of_digital_banking": "Deposit experience and abandonment, without adding fraud exposure",
    "risk_compliance": "Defensible KYC/AML audit trail",
    "trust_and_safety": "Stopping fake accounts without adding friction for genuine users",
    "fintech_product": "Onboarding conversion and time-to-verify",
    "fraud_analyst": "Case volume and explainable decisions",
}
CHECK = ["Check Fraud Defender", "Mobile Deposit"]
IDENTITY = ["MiVIP", "IDLive Face"]


def mock_responder(rec: dict) -> dict:
    """Deterministic stand-in for the model: same contract, same rules, no network."""
    seg, persona = rec.get("segment", ""), rec.get("persona", "")
    owned = set(filter(None, str(rec.get("products_owned", "")).split(";")))
    cfg = load_config()
    non_icp = seg in ("other", "") or cfg["personas"].get(persona, {}).get("role") == "none"
    if "check" in owned and "identity" not in owned:
        products = IDENTITY
    elif "identity" in owned and "check" not in owned and (seg.startswith("bank") or seg == "credit_union"):
        products = CHECK[:1]
    elif rec.get("product_interest") == "check":
        products = CHECK
    else:
        products = IDENTITY
    evidence = [{"claim": f"Segment is {seg}", "source_field": "segment"},
                {"claim": f"Title '{rec.get('title', '')}' maps to persona {persona}", "source_field": "title"}]
    if rec.get("intent_signals"):
        evidence.append({"claim": f"Recent signals: {rec['intent_signals'].split('|')[0].split('@')[0]}",
                         "source_field": "intent_signals"})
    unknowns = [f for f in ("total_assets_usd_b", "region", "intent_signals") if not rec.get(f)]
    unknowns.append("current IDV / check-fraud vendor and contract end date")
    confidence = round(max(0.4, 0.95 - 0.12 * (len(unknowns) - 1)), 2)
    customer = to_bool(rec.get("is_existing_customer"))
    return {
        "summary": f"{rec.get('company')} ({cfg['segments'].get(seg, {}).get('label', seg)}, {rec.get('region') or 'region unknown'}). "
                   f"{'Existing Mitek customer' if customer else 'Prospect'}; contact is {rec.get('title')}.",
        "likely_use_case": (f"Cross-sell to existing customer: {', '.join(products)} alongside current {', '.join(sorted(owned))} deployment"
                            if customer and owned and not non_icp
                            else USE_CASES.get(seg, "Unclear: no regulated onboarding or deposit flow identified")),
        "recommended_products": [] if non_icp else products,
        "persona_angle": ANGLES.get(persona, "Confirm role and whether they own fraud or identity outcomes"),
        "qualification": {"fit_assessment": "Non-ICP" if non_icp else ("Strong" if seg in ("bank_tier1", "bank_regional", "fintech") else "Moderate"),
                          "disqualify_flag": non_icp,
                          "disqualify_reason": "Non-ICP segment or non-buyer persona" if non_icp else ""},
        "evidence": evidence,
        "unknowns": unknowns,
        "next_action": "disqualify_lead" if non_icp else ("route_to_ae" if customer else "enroll_cadence"),
        "confidence": confidence,
    }


def research(record: dict, client: LLMClient | None = None) -> dict:
    client = client or LLMClient()
    prompt_id, system = load_prompt(PROMPT_PATH)
    return client.complete_json(prompt_id=prompt_id, system=system, record=record, required_keys=REQUIRED_KEYS,
                                mock_responder=mock_responder, task="Produce the pre-call brief.")


def main() -> None:
    cfg = load_config()
    accounts = {a["account_id"]: a for a in read_csv("accounts.csv")}
    leads = [l for l in score_all(read_csv("leads.csv"), cfg) if l["status"] in ("New", "MQL", "Enriching")][:12]
    policy, queue = HITLPolicy(), []
    for lead in leads:
        rec = {**lead, "products_owned": accounts.get(lead["account_id"], {}).get("products_owned", "")}
        brief = research(rec)
        decision = policy.decide(brief["next_action"], brief["confidence"])
        queue.append({"lead_id": lead["lead_id"], "company": lead["company"], "grade": lead["grade"],
                      "use_case": brief["likely_use_case"], "products": ", ".join(brief["recommended_products"]),
                      "next_action": brief["next_action"], "confidence": brief["confidence"], "decision": decision,
                      "unknowns": "; ".join(brief["unknowns"])})
    print("=== AI account research: review queue ===\n")
    print(table(queue, ["lead_id", "company", "grade", "products", "next_action", "confidence", "decision"]))
    print(f"\nQueue -> {write_queue('account_research', queue)}")
    print("Audit log -> outputs/ai_audit_log.jsonl")


if __name__ == "__main__":
    main()
