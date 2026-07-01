from __future__ import annotations

from pathlib import Path
from typing import Any

from .util import now_iso, read_json, resource_dirs, slugify, write_json


DEFAULT_QUESTIONS = [
    "What CSI division(s) and spec sections define your normal scope?",
    "What work do you always carry in base bid?",
    "What adjacent work should be excluded, flagged, or carried only by approval?",
    "What terms, product names, sheet titles, or spec sections usually identify your scope?",
    "What quantities or units matter most for takeoff?",
    "What proposal clarifications should appear on every bid?",
]


def profile_path(root: Path, profile_id: str) -> Path:
    return root / "profiles" / f"{profile_id}.json"


def load_profile(path_or_id: str | Path, root: Path) -> dict[str, Any]:
    raw = Path(path_or_id)
    if raw.exists():
        return read_json(raw)
    for base in [root / "profiles", *resource_dirs("profiles")]:
        path = base / f"{path_or_id}.json"
        if path.exists():
            return read_json(path)
    raise FileNotFoundError(f"Scope profile not found: {path_or_id}")


def list_available_profiles(root: Path) -> list[tuple[str, str, str]]:
    seen: set[str] = set()
    rows: list[tuple[str, str, str]] = []
    for source, base in [("workspace", root / "profiles")] + [
        ("built-in", path) for path in resource_dirs("profiles")
    ]:
        if not base.exists():
            continue
        for path in sorted(base.glob("*.json")):
            try:
                profile = read_json(path)
            except Exception:
                continue
            profile_id = str(profile.get("profile_id") or path.stem)
            if profile_id in seen:
                continue
            seen.add(profile_id)
            rows.append((profile_id, str(profile.get("trade_name") or profile_id), source))
    return rows


def build_profile(
    *,
    company_name: str,
    trade_name: str,
    profile_id: str | None = None,
    skill_description: str | None = None,
    scope_rule: str | None = None,
    divisions: list[str] | None = None,
    base_scope: list[str] | None = None,
    include_terms: list[str] | None = None,
    spec_sections: list[str] | None = None,
    quantity_units: list[str] | None = None,
    review_terms: list[str] | None = None,
    exclude_terms: list[str] | None = None,
    proposal_exclusions: list[str] | None = None,
) -> dict[str, Any]:
    pid = slugify(profile_id or trade_name, "scope")
    return {
        "schema_version": 1,
        "profile_id": pid,
        "company_name": company_name,
        "trade_name": trade_name,
        "csi_divisions": divisions or [],
        "created_at": now_iso(),
        "skill_description": skill_description
        or (
            f"Bid-project scope rules for {trade_name}. Use when starting, triaging, "
            "validating, or packaging a bid for this subcontractor scope."
        ),
        "scope_rule": scope_rule
        or (
            f"Base bid is limited to {trade_name}. Adjacent scopes must be explicitly "
            "included, excluded, or flagged before pricing."
        ),
        "base_scope": base_scope or [],
        "include_terms": include_terms or [],
        "spec_sections": spec_sections or [],
        "quantity_units": quantity_units or ["EA", "LF", "SF", "CY", "TON", "HR"],
        "review_terms": review_terms or [],
        "exclude_terms": exclude_terms or [],
        "proposal_exclusions": proposal_exclusions or [],
        "intake_questions": DEFAULT_QUESTIONS,
        "deliverables": {
            "summary": "bid-package-working/00-Bid-Scope-Summary.md",
            "takeoff_workbook": "bid-package-working/01-Takeoff-Worksheet-REV1.xlsx",
            "proposal_letter": "bid-package-working/02 - Proposal Letter.md",
            "scope_pages": "bid-package-working/scope-pages.pdf",
            "spec_pages": "bid-package-working/spec-pages.pdf",
            "alerts": "bid-package-working/ALERTS.md",
        },
        "learning": {
            "feedback_log": ".contractor-bid/feedback.jsonl",
            "instruction": (
                "When the user corrects a scope call, add the correction with "
                "`contractor-bid learn`, then update this profile and regenerated skill "
                "only after the user confirms the new rule should persist."
            ),
        },
    }


def render_skill(profile: dict[str, Any]) -> str:
    include_terms = "\n".join(f"- {term}" for term in profile.get("include_terms", [])) or "- Not filled yet"
    exclude_terms = "\n".join(f"- {term}" for term in profile.get("exclude_terms", [])) or "- Not filled yet"
    review_terms = "\n".join(f"- {term}" for term in profile.get("review_terms", [])) or "- Not filled yet"
    base_scope = "\n".join(f"- {item}" for item in profile.get("base_scope", [])) or "- Not filled yet"
    sections = ", ".join(profile.get("spec_sections", [])) or "Not filled yet"
    divisions = ", ".join(profile.get("csi_divisions", [])) or "Not filled yet"
    return f"""---
name: {profile["profile_id"]}-bid-scope
description: {profile.get("skill_description") or f"Bid-project scope rules for {profile['trade_name']}. Use when starting, triaging, validating, or packaging a bid for this subcontractor scope."}
---

# {profile["trade_name"]} Bid Scope

Company: {profile["company_name"]}
CSI division(s): {divisions}
Spec section hints: {sections}

## Scope Rule

{profile["scope_rule"]}

## Base Scope

{base_scope}

## Terms That Usually Identify This Scope

{include_terms}

## Adjacent Scope To Exclude By Default

{exclude_terms}

## Adjacent Scope To Flag Before Pricing

{review_terms}

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile {profile["profile_id"]}`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile {profile["profile_id"]}` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
"""


def write_profile(root: Path, profile: dict[str, Any]) -> tuple[Path, Path]:
    pid = profile["profile_id"]
    profile_file = profile_path(root, pid)
    skill_file = root / "skills" / f"{pid}-bid-scope" / "SKILL.md"
    write_json(profile_file, profile)
    skill_file.parent.mkdir(parents=True, exist_ok=True)
    skill_file.write_text(render_skill(profile), encoding="utf-8")
    return profile_file, skill_file


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [piece.strip() for piece in value.split(",") if piece.strip()]
