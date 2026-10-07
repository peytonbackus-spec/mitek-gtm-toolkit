"""Generate the synthetic Mitek-shaped dataset in sample_data/.

All accounts, people and numbers are FICTIONAL. Distributions are shaped to
look like a banking-heavy fraud & identity business (check + identity product
lines, partner channel, POC-heavy enterprise cycles) so the scripts in both
role tracks have realistic patterns to find. Seeded, so output is reproducible.

    python scripts/generate_sample_data.py
"""
from __future__ import annotations

import csv
import random
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared_core.config import AS_OF, DATA_DIR, fiscal_quarter, load_config  # noqa: E402

rng = random.Random(42)
cfg = load_config()

# ----------------------------------------------------------------------------- reference lists
PREFIX = ["Harborview", "Summit Ridge", "Cedar Valley", "Blue Mesa", "Northgate", "Ironwood", "Lakeshore",
          "Granite Peak", "Riverbend", "Silverline", "Oakmont", "Prairie First", "Bayfront", "Copper State",
          "Evergreen", "Keystone", "Maple Leaf", "Tidewater", "Stonebridge", "Westfield", "Pinecrest",
          "Crescent", "Highland", "Redwood", "Sterling", "Union Square", "Clearwater", "Falcon", "Meridian", "Arbor"]
SUFFIX = {
    "bank_tier1": ["National Bank", "Financial Group", "Bancorp"],
    "bank_regional": ["Bank", "Bank & Trust", "Bancshares"],
    "bank_community": ["Community Bank", "Savings Bank", "State Bank"],
    "credit_union": ["Credit Union", "Federal Credit Union", "Members CU"],
    "fintech": ["Pay", "Money", "Wallet", "Lend", "Neo"],
    "marketplace": ["Market", "Rentals", "Exchange", "Hub"],
    "igaming": ["Bet", "Gaming", "Sportsbook", "Play"],
    "adjacent_regulated": ["Health", "Insurance", "Mutual", "County Services"],
    "other": ["Consulting", "Labs", "Agency", "Studio"],
}
FIRST = ["Avery", "Jordan", "Morgan", "Riley", "Casey", "Quinn", "Taylor", "Jamie", "Drew", "Reese",
         "Skyler", "Cameron", "Rowan", "Hayden", "Emerson", "Parker", "Sage", "Blake", "Logan", "Kendall"]
LAST = ["Alder", "Brooks", "Calloway", "Dunmore", "Ellery", "Fairbanks", "Garrow", "Hollis", "Ingram", "Jessup",
        "Kestrel", "Lowry", "Marlow", "Nash", "Orwell", "Pruitt", "Quill", "Rourke", "Sutter", "Thorne"]
TITLES = {
    "head_of_fraud": ["VP, Fraud Strategy", "Head of Fraud Prevention", "Director, Fraud Risk"],
    "ciso_identity": ["CISO", "Director, Identity & Access Management", "VP Information Security"],
    "head_of_digital_banking": ["SVP Digital Banking", "Head of Deposit Products", "Director, Digital Channels"],
    "risk_compliance": ["Chief Risk Officer", "BSA/AML Officer", "Director, KYC Operations"],
    "trust_and_safety": ["Head of Trust & Safety", "Director, Trust & Safety"],
    "fintech_product": ["VP Product, Onboarding", "Head of Product, Identity", "Group PM, Account Opening"],
    "fraud_analyst": ["Fraud Analyst", "Senior Fraud Manager", "Fraud Operations Lead"],
    "procurement_it": ["Vendor Risk Manager", "IT Procurement Lead", "Enterprise Architect"],
    "unknown": ["Marketing Coordinator", "Student", "Consultant", "Office Manager"],
}
SDRS = ["SDR - Alex Rivera", "SDR - Bri Okafor", "SDR - Chen Wu", "SDR - Dana Lopes", "SDR - Eli Novak", "SDR - Fran Moretti"]
AES = {"NA": ["AE - Grace Tan", "AE - Hugo Park", "AE - Iris Bell", "AE - Jon Reyes"],
       "EMEA": ["AE - Klara Weiss", "AE - Liam Byrne"], "APAC": ["AE - Mei Lin"], "LATAM": ["AE - Nico Duarte"]}
PARTNER_MGR = "Partner Mgr - Olu Adeyemi"
LEAD_SOURCES = ["Qualified Chat", "Demo Request", "Webinar", "Content Download", "Paid Social", "Event",
                "Outbound - Clay", "Outbound - Sales Nav", "Partner Referral"]
COMPETITORS = ["Competitor A (IDV)", "Competitor B (IDV)", "Competitor C (Check)", "In-house build", "None known"]

SEG_WEIGHTS = {"bank_tier1": 3, "bank_regional": 12, "bank_community": 12, "credit_union": 14, "fintech": 18,
               "marketplace": 8, "igaming": 7, "adjacent_regulated": 6, "other": 12}
SEG_PERSONAS = {
    "bank_tier1": ["head_of_fraud", "ciso_identity", "head_of_digital_banking", "risk_compliance", "fraud_analyst", "procurement_it"],
    "bank_regional": ["head_of_fraud", "head_of_digital_banking", "risk_compliance", "fraud_analyst", "procurement_it"],
    "bank_community": ["head_of_digital_banking", "head_of_fraud", "risk_compliance", "fraud_analyst"],
    "credit_union": ["head_of_digital_banking", "head_of_fraud", "risk_compliance", "fraud_analyst"],
    "fintech": ["fintech_product", "head_of_fraud", "risk_compliance", "ciso_identity"],
    "marketplace": ["trust_and_safety", "fintech_product", "fraud_analyst"],
    "igaming": ["risk_compliance", "trust_and_safety", "fintech_product"],
    "adjacent_regulated": ["ciso_identity", "risk_compliance", "procurement_it"],
    "other": ["unknown", "unknown", "procurement_it"],
}
SIZE = {  # (employees range, assets $B range)
    "bank_tier1": ((20000, 200000), (250, 3000)), "bank_regional": ((1500, 20000), (10, 250)),
    "bank_community": ((50, 1500), (0.3, 10)), "credit_union": ((40, 3000), (0.2, 15)),
    "fintech": ((30, 3000), (0, 0)), "marketplace": ((50, 5000), (0, 0)), "igaming": ((50, 4000), (0, 0)),
    "adjacent_regulated": ((200, 30000), (0, 0)), "other": ((5, 500), (0, 0)),
}
ACV = {  # (min, max) new-logo ACV by segment. [ASSUME] illustrative only
    "bank_tier1": (250_000, 900_000), "bank_regional": (80_000, 300_000), "bank_community": (25_000, 70_000),
    "credit_union": (20_000, 65_000), "fintech": (40_000, 220_000), "marketplace": (35_000, 150_000),
    "igaming": (50_000, 200_000), "adjacent_regulated": (30_000, 120_000), "other": (15_000, 40_000),
}
SIGNALS = list(cfg["lead_scoring"]["intent_signals"].keys())
STAGES = [s["name"] for s in cfg["opportunity"]["stages"]]
OPEN_STAGES = STAGES[:5]


def d(day: date) -> str:
    return day.isoformat() if day else ""


def pick_weighted(weights: dict) -> str:
    keys, w = zip(*weights.items())
    return rng.choices(keys, weights=w)[0]


def region_for(seg: str) -> str:
    if seg in ("bank_community", "credit_union"):
        return "NA"
    return rng.choices(["NA", "EMEA", "APAC", "LATAM"], weights=[70, 20, 6, 4])[0]


# ----------------------------------------------------------------------------- accounts
accounts = []
used = set()
for i in range(450):
    seg = pick_weighted(SEG_WEIGHTS)
    while True:
        name = f"{rng.choice(PREFIX)} {rng.choice(SUFFIX[seg])}"
        if name not in used:
            used.add(name)
            break
    (emin, emax), (amin, amax) = SIZE[seg]
    accounts.append({
        "account_id": f"ACC-{1000 + i}", "account_name": name, "segment": seg, "region": region_for(seg),
        "employees": rng.randint(emin, emax), "total_assets_usd_b": round(rng.uniform(amin, amax), 1) if amax else "",
        "is_customer": seg != "other" and rng.random() < (0.45 if seg.startswith("bank") or seg == "credit_union" else 0.15),
        "products_owned": "",
    })
for a in accounts:
    if a["is_customer"]:
        a["products_owned"] = rng.choice(["check", "check", "identity", "check;identity"])

# ----------------------------------------------------------------------------- leads
leads = []
start = date(2026, 1, 5)
for i in range(900):
    acct = rng.choice(accounts)
    seg = acct["segment"]
    persona = rng.choice(SEG_PERSONAS[seg])
    created = start + timedelta(days=rng.randint(0, (AS_OF - start).days - 1))
    source = rng.choice(LEAD_SOURCES)
    partner = rng.choice([p["name"] for p in cfg["partners"]]) if source == "Partner Referral" else ""
    # intent signals with dates
    n_sig = rng.choices([0, 1, 2, 3, 4], weights=[20, 35, 25, 13, 7])[0]
    if source in ("Demo Request", "Qualified Chat"):
        n_sig = max(n_sig, 1)
    sigs = []
    for _ in range(n_sig):
        s = rng.choice(SIGNALS)
        if source == "Demo Request" and not sigs:
            s = "demo_request"
        if source == "Qualified Chat" and not sigs:
            s = "qualified_chat_engaged"
        sigs.append(f"{s}@{d(min(AS_OF, created + timedelta(days=rng.randint(0, 20))))}")
    fn, ln = rng.choice(FIRST), rng.choice(LAST)
    domain = acct["account_name"].lower().replace(" ", "").replace("&", "") + ".example"
    email = f"{fn.lower()}.{ln.lower()}@{domain}"
    if rng.random() < 0.03:
        email = f"{fn.lower()}{ln.lower()}@gmail.example"  # personal email (DQ issue)
    if rng.random() < 0.02:
        email = ""  # missing email (DQ issue)
    product_interest = rng.choice(["check", "identity"]) if seg.startswith("bank") or seg == "credit_union" else "identity"

    # hidden propensity drives the funnel so scoring has real signal to find
    seg_pts = cfg["segments"][seg]["icp_points"]
    per_pts = cfg["personas"][persona]["points"]
    strong = sum(1 for s in sigs if s.split("@")[0] in ("demo_request", "qualified_chat_engaged", "email_reply_positive", "pricing_page_visit"))
    # "True" propensity the scoring model is trying to learn. Two segments deliberately behave
    # differently from their configured weights (credit unions convert better via partners,
    # regional banks slower) so calibrate_scoring.py has a real finding to surface.
    truth = {"credit_union": 1.35, "bank_regional": 0.8}.get(seg, 1.0)
    fitness = truth * (seg_pts / 30) * (0.35 + 0.65 * per_pts / 25)
    p_mql = min(0.90, 0.01 + 0.55 * fitness + 0.10 * strong + 0.02 * len(sigs))
    p_sql = min(0.80, 0.02 + 0.45 * fitness + 0.08 * strong)
    p_opp = min(0.85, 0.15 + 0.45 * fitness + 0.05 * strong)
    age = (AS_OF - created).days

    status, mql, sal, sql, conv, dq = "New", None, None, None, None, ""
    hours_to_sal = ""
    if age > 2:
        status = "Enriching" if age < 4 else "New"
        if seg == "other" and rng.random() < 0.7:
            status, dq = "Disqualified", rng.choice(["Not ICP", "Student/Job Seeker", "Bad Data"])
        elif rng.random() < p_mql:
            mql = created + timedelta(days=rng.randint(0, 3))
            status = "MQL"
            hours_to_sal = rng.choice([1, 2, 3, 4, 6, 8, 20, 30, 50])
            if age > 3:
                sal = mql + timedelta(days=hours_to_sal // 24)
                status = "Working"
                if rng.random() < p_sql and age > 10:
                    sql = sal + timedelta(days=rng.randint(2, 16))
                    status = "SQL"
                    if rng.random() < p_opp and age > 14:
                        conv = sql + timedelta(days=rng.randint(0, 5))
                        status = "Converted"
                    elif age > 45:
                        status = "Recycled"
                elif age > 60:
                    status = rng.choice(["Recycled", "Disqualified"])
                    dq = rng.choice(cfg["lead_lifecycle"]["disqualify_reasons"]) if status == "Disqualified" else ""
        elif age > 30:
            status = "Recycled" if rng.random() < 0.6 else "Disqualified"
            dq = rng.choice(["Not ICP", "No Fraud/IDV Use Case", "Competitor"]) if status == "Disqualified" else ""
    region = acct["region"] if rng.random() > 0.03 else ""  # missing region (DQ issue)
    leads.append({
        "lead_id": f"L-{5000 + i}", "created_date": d(created), "first_name": fn, "last_name": ln, "email": email,
        "title": rng.choice(TITLES[persona]), "persona": persona, "company": acct["account_name"],
        "account_id": acct["account_id"], "segment": seg, "region": region, "employees": acct["employees"],
        "total_assets_usd_b": acct["total_assets_usd_b"], "lead_source": source, "partner": partner,
        "product_interest": product_interest, "is_existing_customer": acct["is_customer"],
        "intent_signals": "|".join(sigs), "status": status, "mql_date": d(mql), "sal_date": d(sal),
        "mql_to_sal_hours": hours_to_sal if sal else "", "sql_date": d(sql), "converted_date": d(conv), "opportunity_id": "", "disqualify_reason": dq,
        "owner": rng.choice(SDRS) if mql else "Marketing Queue",
    })
# duplicate a few leads (DQ issue)
for dup in rng.sample(leads, 6):
    leads.append({**dup, "lead_id": f"L-{9000 + len(leads)}", "status": "New", "mql_date": "", "sal_date": "",
                  "sql_date": "", "converted_date": "", "mql_to_sal_hours": "", "owner": "Marketing Queue"})

# ----------------------------------------------------------------------------- opportunities
opps = []
acct_by_id = {a["account_id"]: a for a in accounts}


def make_opp(acct, otype, created, source, partner="", product_line=None, amount=None):
    seg = acct["segment"]
    lo, hi = ACV[seg]
    amount = amount or round(rng.uniform(lo, hi) * (0.5 if otype == "Expansion" else 1.0), -3)
    product_line = product_line or ("identity" if seg in ("fintech", "marketplace", "igaming", "adjacent_regulated")
                                    else rng.choice(["check", "identity"]))
    cycle = int(rng.uniform(60, 200) * (1.6 if seg == "bank_tier1" else 1.0) * (0.7 if otype == "Renewal" else 1.0))
    close = created + timedelta(days=cycle)
    fit = cfg["segments"][seg]["icp_points"]
    contacts = rng.randint(1, 7)
    eb = rng.random() < 0.55
    p_win = -0.05 + fit / 150 + (0.12 if eb else -0.08) + 0.03 * min(contacts, 5) + (0.12 if otype == "Expansion" else 0)
    p_win = max(0.05, min(0.92, p_win))
    is_closed = close < AS_OF and rng.random() < 0.92
    stage, fc, won, lost_reason, competitor = None, None, False, "", rng.choice(COMPETITORS)
    if is_closed:
        won = rng.random() < p_win
        stage = "Closed Won" if won else "Closed Lost"
        fc = "Closed" if won else "Omitted"
        if not won:
            lost_reason = rng.choices(cfg["opportunity"]["closed_lost_reasons"], weights=[14, 22, 26, 6, 9, 10, 9, 4])[0]
        stage_entered = close
    else:
        elapsed = (AS_OF - created).days
        idx = min(4, max(0, int(elapsed / max(cycle, 1) * 5)))
        if close < AS_OF:  # slipped past close date, still open: a hygiene problem to detect
            idx = rng.randint(2, 4)
        stage = OPEN_STAGES[idx]
        fc = ["Pipeline", "Pipeline", "Best Case", "Best Case", "Best Case"][idx]
        if (idx == 4 and rng.random() < 0.40) or (idx == 3 and rng.random() < 0.08):
            fc = "Commit"
        stage_entered = max(created, AS_OF - timedelta(days=rng.randint(1, 55)))  # never before the opp existed
    last_activity = (stage_entered if is_closed else AS_OF - timedelta(days=rng.choice([1, 2, 3, 5, 8, 12, 18, 25, 40])))
    return {
        "opportunity_id": f"OPP-{7000 + len(opps)}", "account_id": acct["account_id"], "account_name": acct["account_name"],
        "segment": seg, "region": acct["region"], "type": otype, "product_line": product_line, "source": source,
        "partner": partner, "owner": rng.choice(AES[acct["region"]]), "amount": int(amount), "stage": stage,
        "forecast_category": fc, "created_date": d(created), "close_date": d(close), "stage_entered_date": d(stage_entered),
        "last_activity_date": d(last_activity), "contacts_engaged": contacts, "economic_buyer_engaged": eb,
        "poc_status": rng.choice(["Not Started", "In Progress", "Passed", "N/A"]) if STAGES.index(stage) >= 2 or is_closed else "Not Started",
        "security_review": rng.choice(["Not Started", "In Progress", "Complete"]) if STAGES.index(stage) >= 3 or is_closed else "Not Started",
        "next_step": "" if rng.random() < 0.15 else rng.choice(["Exec alignment call", "POC readout", "Security questionnaire", "Pricing review", "Legal redlines"]),
        "is_closed": is_closed, "is_won": won, "closed_lost_reason": lost_reason, "competitor": competitor,
        "originating_lead_id": "",
    }


for lead in leads:
    if lead["status"] == "Converted":
        acct = acct_by_id[lead["account_id"]]
        otype = "Expansion" if acct["is_customer"] else "New Logo"
        src = "Partner" if lead["partner"] else ("SDR" if lead["lead_source"].startswith("Outbound") else "Marketing")
        o = make_opp(acct, otype, date.fromisoformat(lead["converted_date"]), src, lead["partner"], lead["product_interest"])
        o["originating_lead_id"] = lead["lead_id"]
        lead["opportunity_id"] = o["opportunity_id"]
        opps.append(o)
# AE- and partner-sourced opps that never were leads
for _ in range(110):
    acct = rng.choice([a for a in accounts if a["segment"] != "other"])
    created = date(2025, 10, 1) + timedelta(days=rng.randint(0, 350))
    if acct["is_customer"] and rng.random() < 0.5:
        otype = "Expansion"
        owned = acct["products_owned"]
        pl = "identity" if owned == "check" else ("check" if owned == "identity" else rng.choice(["check", "identity"]))
    else:
        otype, pl = "New Logo", None
    src = "Partner" if acct["segment"] in ("bank_community", "credit_union") and rng.random() < 0.6 else "AE"
    partner = rng.choice(["Fiserv", "Abrigo", "CSI"]) if src == "Partner" else ""
    opps.append(make_opp(acct, otype, created, src, partner, pl))

# Seed a realistic amount of CRM mess so the data-quality monitor has something to catch.
open_early = [o for o in opps if o["stage"] in OPEN_STAGES[:2]]
for o in rng.sample(open_early, min(3, len(open_early))):
    o["forecast_category"] = "Commit"            # O05: rep commits a stage-1 deal
lost = [o for o in opps if o["stage"] == "Closed Lost"]
for o in rng.sample(lost, min(4, len(lost))):
    o["closed_lost_reason"] = ""                 # O03: no loss reason captured
partner_opps = [o for o in opps if o["source"] == "Partner"]
for o in rng.sample(partner_opps, min(2, len(partner_opps))):
    o["partner"] = ""                            # O07: partner attribution lost
dq_leads = [l for l in leads if l["status"] == "Disqualified" and l["disqualify_reason"]]
for l in rng.sample(dq_leads, min(5, len(dq_leads))):
    l["disqualify_reason"] = ""                  # L05: DQ'd with no reason

# ----------------------------------------------------------------------------- renewals
renewals = []
for acct in [a for a in accounts if a["is_customer"]]:
    for pl in acct["products_owned"].split(";"):
        lo, hi = ACV[acct["segment"]]
        arr = int(round(rng.uniform(lo, hi), -3))
        renewal_date = AS_OF + timedelta(days=rng.randint(-20, 300))
        trend = round(rng.gauss(4 if pl == "identity" else -3, 14), 1)  # check volume in secular decline [PUBLIC]
        r = {
            "account_id": acct["account_id"], "account_name": acct["account_name"], "segment": acct["segment"],
            "region": acct["region"], "product_line": pl, "arr": arr, "renewal_date": d(renewal_date),
            "volume_trend_90d_pct": trend, "utilization_pct": max(5, min(160, round(rng.gauss(85, 25)))),
            "sev1_tickets_90d": rng.choices([0, 1, 2, 3], weights=[70, 18, 8, 4])[0],
            "exec_sponsor_active": rng.random() < 0.75, "competitor_signal": rng.random() < 0.18,
            "products_owned": acct["products_owned"], "owner": rng.choice(AES[acct["region"]]),
        }
        renewals.append(r)

# ----------------------------------------------------------------------------- forecast snapshots
# Mitek's fiscal year ends Sep 30 [PUBLIC]; FY26 Q2 = Jan-Mar, Q3 = Apr-Jun, Q4 = Jul-Sep 2026.
QUARTERS = {"FY26-Q2": (date(2026, 1, 1), date(2026, 3, 31)), "FY26-Q3": (date(2026, 4, 1), date(2026, 6, 30)),
            "FY26-Q4": (date(2026, 7, 1), date(2026, 9, 30))}
BIAS = {"NA": 0.92, "EMEA": 1.12, "APAC": 1.05, "LATAM": 1.0}  # NA sandbags commit, EMEA over-calls
snapshots = []
for q, (qs, qe) in QUARTERS.items():
    for region in ["NA", "EMEA", "APAC", "LATAM"]:
        actual = sum(o["amount"] for o in opps if o["is_won"] and o["region"] == region
                     and qs <= date.fromisoformat(o["close_date"]) <= qe and o["type"] != "Renewal")
        if actual == 0:
            continue  # no bookings in this region-quarter, so there's no forecast to grade
        for wk in range(13):
            progress = wk / 12
            noise = rng.gauss(0, 0.12 * (1 - progress))
            commit = actual * (BIAS[region] + noise) * (0.88 + 0.12 * progress)
            snapshots.append({
                "quarter": q, "week": wk + 1, "snapshot_date": d(qs + timedelta(weeks=wk)), "region": region,
                "commit": int(commit), "best_case": int(commit * rng.uniform(1.2, 1.45)),
                "pipeline": int(commit * rng.uniform(2.2, 3.4)), "actual_closed_won": int(actual),
            })


# ----------------------------------------------------------------------------- opportunity field history
# Mirrors Salesforce OpportunityFieldHistory (StageName and CloseDate changes), which is what stage
# velocity and close-date slippage are measured from. It uses its own RNG so adding it leaves every
# other file byte-for-byte unchanged.
# Planted SYNTHETIC patterns, so the sales-leadership reports have something real to find:
#   - Marketing-sourced (inbound) deals wait longer in "1 - Qualify" before discovery is held
#   - one AE converts Qualify -> Discovery slowly
#   - bank segments run long in "3 - Technical Validation" (data-sharing and security approval for the POC)
#   - deals with no economic buyer drag in "4 - Business Case & Security Review"
#   - lost deals get their close date pushed more often, and by more, than won deals
hrng = random.Random(7)
STAGE_BASE_DAYS = [10, 18, 28, 24, 16]
SLOW_VALIDATION_SEGMENTS = {"bank_tier1", "bank_regional"}   # banks: data-sharing and security approval for the POC
SLOW_QUALIFY_AE = "AE - Jon Reyes"


def _stage_days(o: dict, i: int) -> float:
    m = hrng.lognormvariate(0, 0.35)
    if i == 0:
        m *= 2.4 if o["source"] == "Marketing" else 1.0
        m *= 1.8 if o["owner"] == SLOW_QUALIFY_AE else 1.0
    if i == 2 and o["segment"] in SLOW_VALIDATION_SEGMENTS:
        m *= 1.7
    if i == 3 and not o["economic_buyer_engaged"]:
        m *= 1.6
    return STAGE_BASE_DAYS[i] * m


field_history = []
for o in opps:
    created, close = date.fromisoformat(o["created_date"]), date.fromisoformat(o["close_date"])
    if o["is_closed"]:
        reached = 4 if o["is_won"] else hrng.choices(range(5), weights=[30, 28, 22, 12, 8])[0]
        draws, end = [_stage_days(o, i) for i in range(reached + 1)], close   # last draw = time in the final stage
    else:
        reached = OPEN_STAGES.index(o["stage"])
        draws, end = [_stage_days(o, i) for i in range(reached)], date.fromisoformat(o["stage_entered_date"])
    span, total, acc = max((end - created).days, 0), sum(draws) or 1.0, 0.0
    rows = []
    for k in range(1, reached + 1):
        acc += draws[k - 1]
        rows.append((OPEN_STAGES[k - 1], OPEN_STAGES[k], created + timedelta(days=round(span * acc / total))))
    if o["is_closed"]:
        rows.append((OPEN_STAGES[reached], o["stage"], close))
    for old, new, when in rows:
        field_history.append({"opportunity_id": o["opportunity_id"], "field": "StageName",
                              "old_value": old, "new_value": new, "changed_date": d(when)})
    # Close-date pushes, rebuilt backwards from the current close date.
    if o["is_won"]:
        n, sizes = hrng.choices([0, 1, 2], weights=[60, 30, 10])[0], [7, 14, 21]
    elif o["is_closed"]:
        n, sizes = hrng.choices([0, 1, 2, 3], weights=[30, 30, 25, 15])[0], [14, 21, 30, 45, 60]
    else:
        n, sizes = hrng.choices([0, 1, 2, 3], weights=[62, 27, 8, 3])[0], [7, 14, 30, 45]
    new_val, pushes = close, []
    for _ in range(n):
        old_val = new_val - timedelta(days=hrng.choice(sizes))
        if old_val <= created:
            break
        pushes.append([old_val, new_val])
        new_val = old_val
    # A push is made around the old close date, or earlier when that date is still in the future.
    latest = min(AS_OF - timedelta(days=1), close)
    dates = sorted(min(ov - timedelta(days=hrng.randint(0, 5)), latest - timedelta(days=hrng.randint(0, 40)))
                   for ov, _ in pushes)
    for (ov, nv), when in zip(reversed(pushes), dates):
        if when > created:
            field_history.append({"opportunity_id": o["opportunity_id"], "field": "CloseDate",
                                  "old_value": d(ov), "new_value": d(nv), "changed_date": d(when)})
field_history.sort(key=lambda r: (r["opportunity_id"], r["changed_date"], r["field"]))


# ----------------------------------------------------------------------------- marketing ops: campaigns, members, consent
# Campaigns follow the naming convention in config (marketing_ops.campaign_name_pattern); a few break it on
# purpose, as do some UTM values, so the hygiene checks have something to catch. Own RNG: other files unchanged.
mrng = random.Random(11)
MO = cfg["marketing_ops"]
SOURCE_TO_TYPE = {"Event": "EVT", "Webinar": "WBN", "Content Download": "CNT", "Paid Social": "PAID",
                  "Outbound - Clay": "OUT", "Outbound - Sales Nav": "OUT", "Partner Referral": "PRT",
                  "Demo Request": "WEB", "Qualified Chat": "WEB"}
TYPE_UTM = {"EVT": ("events", "event"), "WBN": ("webinar_platform", "webinar"), "CNT": ("linkedin", "organic"),
            "PAID": ("linkedin", "paid_social"), "OUT": ("salesloft", "email"), "PRT": ("partner", "referral"),
            "WEB": ("google", "cpc")}
TYPE_NAMES = {"EVT": ["Banking-Fraud-Forum", "Fintech-Risk-Summit"], "WBN": ["Deepfake-Defense-Live", "Check-Fraud-Briefing"],
              "CNT": ["Check-Fraud-Benchmark", "Identity-Fraud-Guide"], "PAID": ["LinkedIn-Fraud-Leaders", "Retargeting-Banking"],
              "OUT": ["Clay-Job-Change-Trigger", "Sales-Nav-Fraud-Leader"], "PRT": ["Partner-Referral"], "WEB": ["Demo-Request", "Qualified-Chat"]}
TYPE_SPEND = {"EVT": (25000, 60000), "WBN": (2000, 5000), "CNT": (3000, 8000), "PAID": (15000, 40000),
              "OUT": (3000, 6000), "PRT": (0, 0), "WEB": (0, 0)}
campaigns, camp_index = [], {}
CAMPAIGN_QUARTERS = sorted({fiscal_quarter(date.fromisoformat(l["created_date"])) for l in leads})   # quarters the leads span
for q in CAMPAIGN_QUARTERS:
    for ctype, names in TYPE_NAMES.items():
        for nm in names:
            geo = "NA" if ctype == "EVT" and nm == "Banking-Fraud-Forum" else "GLOBAL"
            cid = f"CMP-{100 + len(campaigns)}"
            lo, hi = TYPE_SPEND[ctype]
            row = {"campaign_id": cid, "campaign_name": f"{q}_{ctype}_{geo}_{nm}", "type": ctype, "quarter": q,
                   "region": geo, "start_date": "", "end_date": "", "spend": int(round(mrng.uniform(lo, hi), -2))}
            campaigns.append(row)
            camp_index.setdefault((q, ctype), []).append(row)
for c in mrng.sample([c for c in campaigns if c["type"] in ("WBN", "CNT", "PAID")], 3):
    c["campaign_name"] = c["campaign_name"].split("_")[-1].replace("-", " ") + " " + c["quarter"][-2:]   # broken name

utm_typos = {"linkedin": "LinkedIn", "google": "google.com", "salesloft": "SalesLoft", "partner": "partners"}
members = []


def _member(c, lead, when, responded=True):
    statuses, resp = MO["campaign_types"][c["type"]]["statuses"], MO["campaign_types"][c["type"]]["responded"]
    non_resp = [s for s in statuses if s not in resp]
    responded = responded or not non_resp      # e.g. a content download is always a response
    status = mrng.choice(resp) if responded else mrng.choice(non_resp)
    src, med = TYPE_UTM[c["type"]]
    if mrng.random() < 0.05:
        src = utm_typos.get(src, src + "_")
    members.append({"member_id": f"CM-{50000 + len(members)}", "campaign_id": c["campaign_id"], "lead_id": lead["lead_id"],
                    "status": status, "responded": responded, "touch_date": d(when), "utm_source": src, "utm_medium": med})


for lead in leads:
    created = date.fromisoformat(lead["created_date"])
    q = fiscal_quarter(created)
    ctype = SOURCE_TO_TYPE.get(lead["lead_source"])
    if not ctype or (q, ctype) not in camp_index:
        continue
    first = mrng.choice(camp_index[(q, ctype)])
    _member(first, lead, created)
    end = date.fromisoformat(lead["converted_date"]) if lead["converted_date"] else AS_OF - timedelta(days=1)
    for _ in range(mrng.choices([0, 1, 2, 3], weights=[35, 35, 20, 10])[0]):
        when = created + timedelta(days=mrng.randint(1, max(1, (end - created).days)))
        pool = camp_index.get((fiscal_quarter(when), mrng.choice(["WBN", "CNT", "PAID", "EVT", "OUT"])))
        if pool and when < AS_OF:
            _member(mrng.choice(pool), lead, when, responded=mrng.random() < 0.8)
for c in campaigns:   # dates from the members; event/webinar end date = when the list should have been uploaded
    dates = sorted(m["touch_date"] for m in members if m["campaign_id"] == c["campaign_id"])
    if dates:
        first_touch = date.fromisoformat(dates[0])
        c["start_date"] = d(first_touch - timedelta(days=mrng.randint(10, 30)))
        c["end_date"] = d(first_touch - timedelta(days=mrng.choice([0, 0, 1, 1, 2, 4, 6]))) if c["type"] in ("EVT", "WBN") else d(date.fromisoformat(dates[-1]))
members.sort(key=lambda m: (m["lead_id"], m["touch_date"]))

consent = []
for lead in leads:
    region = lead["region"]
    country = ("CA" if mrng.random() < 0.2 else "US") if region == "NA" else ("GB" if region == "EMEA" and mrng.random() < 0.3 else "")
    if region == "EMEA":
        ctype = mrng.choices(["opt_in", "legitimate_interest", "none"], weights=[70, 22, 8])[0]
    elif country == "CA":
        ctype = mrng.choices(["express", "implied_inquiry", "none"], weights=[55, 38, 7])[0]
    else:
        ctype = mrng.choices(["opt_in", "none"], weights=[60, 40])[0]
    consent.append({"lead_id": lead["lead_id"], "region": region, "country": country, "consent_type": ctype,
                    "consent_date": lead["created_date"] if ctype != "none" else "",
                    "email_opt_out": mrng.random() < 0.04})

# ----------------------------------------------------------------------------- CRM request queue
# Salesforce, Clari and Salesloft requests from the business over the last quarter (fictional).
qrng = random.Random(13)
CRM = cfg["stack"]["crm"]
REQ_TEMPLATES = {
    "Report / Dashboard": ["Pipeline by segment for QBR", "Rep activity dashboard", "Win rate by competitor report", "Webinar attendee report"],
    "List View": ["My open deals closing this quarter", "Unworked MQLs list view"],
    "Access / Permissions": ["New AE needs Salesforce access", "SE needs edit access on opps", "Contractor Clari seat"],
    "Data Fix": ["Merge duplicate accounts", "Fix wrong owner on renewal opps", "Backfill industry on accounts"],
    "Field / Picklist": ["Add a new product to the picklist", "New field: Sandbox start date", "Add competitor value"],
    "Validation Rule": ["Require next step date in stage 4+", "Block Commit without an economic buyer"],
    "Page Layout": ["Show security review fields on opp layout", "Add renewal fields to account"],
    "Email Template": ["Renewal notice template", "Event follow-up template"],
    "Automation / Flow": ["Auto-create renewal opp at T-180", "Alert AE when account health drops", "Stamp stage entry dates"],
    "Object / Data Model": ["Track POC results as an object", "Partner object for referral payouts"],
    "Routing / Assignment": ["Route APAC leads to new AE", "Round-robin inbound demo requests", "Fix routing for partner-sourced leads"],
    "Integration": ["Sync intent signals to the CRM", "Push usage data from billing to the CRM"],
}
TEAMS = ["Sales", "Sales Leadership", "Marketing", "Marketing Ops", "Customer Success", "Finance"]
requests = []
for i in range(72):
    cat = qrng.choices(list(REQ_TEMPLATES), weights=[22, 4, 8, 9, 7, 4, 3, 2, 8, 2, 5, 3])[0]
    submitted = AS_OF - timedelta(days=92) + timedelta(days=qrng.randint(0, 91))   # the quarter before AS_OF
    impact = qrng.choices(["Blocks deal", "Blocks team", "Improves efficiency", "Nice to have"], weights=[8, 20, 45, 27])[0]
    effort = qrng.choices(["S", "M", "L", "XL"], weights=[45, 30, 18, 7])[0]
    if cat in ("Object / Data Model", "Integration"):
        effort = qrng.choice(["L", "XL"])
    resp_days = qrng.choices([0, 1, 2, 4, 7], weights=[40, 30, 15, 10, 5])[0]
    first_resp = submitted + timedelta(days=resp_days)
    work_days = {"S": 2, "M": 6, "L": 15, "XL": 30}[effort] * qrng.uniform(0.6, 1.6)
    done_on = first_resp + timedelta(days=round(work_days))
    status = "Done" if done_on < AS_OF else qrng.choice(["In Progress", "Backlog"])
    if qrng.random() < 0.05:
        status, done_on = "Won't Do", first_resp
    requests.append({
        "request_id": f"REQ-{1000 + i}", "submitted_date": d(submitted), "requester_team": qrng.choice(TEAMS),
        "system": cfg["stack"]["sales_engagement"] if cat == "Email Template" else qrng.choices([CRM, cfg["stack"]["forecasting"], "Both"], weights=[70, 15, 15])[0],
        "category": cat, "summary": qrng.choice(REQ_TEMPLATES[cat]), "revenue_impact": impact,
        "users_affected": qrng.choice([1, 1, 2, 4, 8, 12, 25, 40]), "effort": effort,
        "due_date": d(submitted + timedelta(days=qrng.choice([3, 7, 14, 30]))) if qrng.random() < 0.35 else "",
        "status": status, "first_response_date": d(first_resp) if first_resp < AS_OF else "",
        "completed_date": d(done_on) if status in ("Done", "Won't Do") else "",
    })


def write(name, rows):
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_DIR / name, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows):>4} rows -> sample_data/{name}")


if __name__ == "__main__":
    write("accounts.csv", accounts)
    write("leads.csv", leads)
    write("opportunities.csv", opps)
    write("renewals.csv", renewals)
    write("forecast_snapshots.csv", snapshots)
    write("opportunity_field_history.csv", field_history)
    write("campaigns.csv", campaigns)
    write("campaign_members.csv", members)
    write("lead_consent.csv", consent)
    write("crm_requests.csv", requests)
