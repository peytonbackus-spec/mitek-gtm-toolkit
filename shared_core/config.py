"""Shared config + IO helpers used by both role tracks.

Everything company-specific lives in config/mitek.yaml; this module is the only
place that knows where that file and the sample data live.
"""
from __future__ import annotations

import csv
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "mitek.yaml"
DATA_DIR = ROOT / "sample_data"
OUTPUT_DIR = ROOT / "outputs"

# Fixed "as of" date so every report is reproducible against the synthetic data.
AS_OF = date(2026, 10, 1)


@lru_cache(maxsize=1)
def load_config(path: str | None = None) -> dict:
    with open(path or CONFIG_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def read_csv(name: str) -> list[dict]:
    path = DATA_DIR / name if not Path(name).is_absolute() else Path(name)
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(name: str, rows: Iterable[dict], fieldnames: list[str] | None = None) -> Path:
    rows = list(rows)
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / name
    if not rows:
        path.write_text("")
        return path
    fieldnames = fieldnames or list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return path


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    return datetime.strptime(value[:10], "%Y-%m-%d").date()


def to_float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def to_bool(value) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def pct(n: float, d: float) -> float:
    return round(100.0 * n / d, 1) if d else 0.0


def table(rows: list[dict], cols: list[str] | None = None) -> str:
    """Tiny dependency-free text table for console output."""
    if not rows:
        return "(no rows)"
    cols = cols or list(rows[0].keys())
    widths = {c: max(len(c), *(len(str(r.get(c, ""))) for r in rows)) for c in cols}
    line = "  ".join(c.ljust(widths[c]) for c in cols)
    sep = "  ".join("-" * widths[c] for c in cols)
    body = "\n".join("  ".join(str(r.get(c, "")).ljust(widths[c]) for c in cols) for r in rows)
    return f"{line}\n{sep}\n{body}"


def dedupe_leads(leads: list[dict]) -> list[dict]:
    """Drop duplicate leads (same email; keep the earliest). Mirrors v_leads.is_duplicate in the
    semantic-layer SQL so Python reports and SQL dashboards count the same leads."""
    seen, out = set(), []
    for lead in sorted(leads, key=lambda l: (l.get("created_date", ""), l.get("lead_id", ""))):
        key = (lead.get("email") or "").lower()
        if key and key in seen:
            continue
        if key:
            seen.add(key)
        out.append(lead)
    return out


def fiscal_quarter(d: date) -> str:
    """Mitek fiscal quarter label. FY ends Sep 30, so Oct-Dec 2026 = FY27-Q1.
    Same logic as close_fiscal_quarter in semantic_layer.sql."""
    fy = d.year + (1 if d.month >= 10 else 0)
    q = (d.month + 2) % 12 // 3 + 1
    return f"FY{str(fy)[2:]}-Q{q}"
