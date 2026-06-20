from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path
from typing import Any

from .util import markdown_table, read_json


CHECKLIST = [
    ("00-Bid-Scope-Summary.md", "Bid scope summary", True),
    ("00-Scope-Reference-Index.md", "Scope reference index", True),
    ("01-Takeoff-Worksheet-REV1.xlsx", "Takeoff/BOM workbook", True),
    ("02 - Proposal Letter.md", "Proposal letter", True),
    ("takeoff", "takeoff/ folder", True),
    ("takeoff/review-pages.md", "Reviewed-pages audit log", True),
    ("takeoff/scope-pages-sources.json", "Page-packet sources JSON", True),
    ("text-extracts", "text-extracts/ from triage", False),
    ("takeoff/candidate-pages.md", "Candidate pages", False),
    ("takeoff/triage-scope-signals.md", "Triage scope signals", False),
    ("scope-pages.pdf", "Scope pages packet", False),
    ("scope-pages-index.md", "Scope pages index", False),
    ("spec-pages.pdf", "Spec pages packet", False),
    ("supplier-sendoff", "Supplier sendoff package", False),
]

SUMMARY_FIELDS = {
    "bid_decision_summary": "plain-English quick read",
    "what_to_open_first": "best pages to open first",
    "scope_items": "carried scope items",
    "not_in_base_scope": "explicit exclusions",
}

PLACEHOLDERS = ("PROJECT NAME", "YYYY-MM-DD", "TBD", "TODO", "{{", "}}")


def parse_due_date(folder_name: str) -> date | None:
    match = re.match(r"^(\d{2})(\d{2})(\d{2})-", folder_name)
    if not match:
        return None
    mm, dd, yy = (int(group) for group in match.groups())
    try:
        return date(2000 + yy, mm, dd)
    except ValueError:
        return None


def empty_or_placeholder(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, list):
        return not value or all(empty_or_placeholder(item) for item in value)
    if isinstance(value, dict):
        return not value or all(empty_or_placeholder(item) for item in value.values())
    text = str(value).strip()
    if not text:
        return True
    upper = text.upper()
    return any(token in upper for token in PLACEHOLDERS)


def scan_text_extracts(text_dir: Path, terms: list[str]) -> dict[str, int]:
    counts = {term: 0 for term in terms if term}
    if not text_dir.exists():
        return counts
    for txt in sorted(text_dir.glob("*.txt")):
        content = txt.read_text(encoding="utf-8", errors="ignore").lower()
        for term in counts:
            counts[term] += content.count(term.lower())
    return counts


def find_takeoff_jsons(work: Path) -> list[Path]:
    takeoff = work / "takeoff"
    if not takeoff.exists():
        return []
    return [
        path
        for path in sorted(takeoff.glob("*.json"))
        if path.name != "scope-pages-sources.json" and not path.name.startswith("_")
    ]


def check_takeoff_jsons(work: Path, profile: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    exclude_terms = [term.lower() for term in profile.get("exclude_terms", [])]
    review_terms = [term.lower() for term in profile.get("review_terms", [])]
    for cfg in find_takeoff_jsons(work):
        try:
            data = read_json(cfg)
        except Exception as exc:
            warnings.append(f"{cfg.name}: cannot parse JSON ({exc})")
            continue
        for idx, row in enumerate(data.get("bom", []), start=1):
            text = " ".join(str(row.get(key, "")) for key in ("section", "item", "description")).lower()
            status = str(row.get("status", ""))
            qty = row.get("qty", 0) or 0
            if status.startswith("Included"):
                for term in exclude_terms:
                    if term and term in text:
                        errors.append(f"{cfg.name} BOM row {idx}: excluded term `{term}` is Included.")
                for term in review_terms:
                    if term and term in text:
                        warnings.append(f"{cfg.name} BOM row {idx}: review term `{term}` is Included.")
            if status.startswith("Excluded") and isinstance(qty, (int, float)) and qty:
                warnings.append(f"{cfg.name} BOM row {idx}: excluded row has qty {qty}.")
    return errors, warnings


def check_page_sources(work: Path) -> list[str]:
    warnings: list[str] = []
    sources = work / "takeoff" / "scope-pages-sources.json"
    if not sources.exists():
        return warnings
    try:
        data = read_json(sources)
    except Exception as exc:
        return [f"takeoff/scope-pages-sources.json: cannot parse JSON ({exc})"]
    for field, label in SUMMARY_FIELDS.items():
        if empty_or_placeholder(data.get(field)):
            warnings.append(f"Page-packet sources missing {label}: fill `{field}`.")
    if not data.get("spec_pages") and empty_or_placeholder(data.get("no_spec_pages_found")):
        warnings.append("No spec_pages[] and no no_spec_pages_found note; confirm specs are absent.")
    return warnings


def validate_project(
    project: Path,
    profile: dict[str, Any],
    *,
    today: date | None = None,
    write: bool = True,
) -> tuple[Path, int, list[str], list[str]]:
    project = project.resolve()
    work = project / "bid-package-working"
    today = today or date.today()
    alerts: list[str] = []
    errors: list[str] = []
    warnings: list[str] = []

    lines = [
        f"# Bid Package Alerts - {project.name}",
        "",
        f"Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} by contractor-bid check",
        "",
        f"Profile: `{profile['profile_id']}` ({profile['trade_name']})",
        "",
        "## Bid Due Date",
        "",
    ]

    due = parse_due_date(project.name)
    if due:
        days = (due - today).days
        if days < 0:
            msg = f"Bid date {due.isoformat()} is {-days} day(s) past. Confirm status."
        elif days <= 2:
            msg = f"URGENT: bid due {due.isoformat()} - {days} day(s) left."
            alerts.append(msg)
        else:
            msg = f"Bid due {due.isoformat()} - {days} day(s) left."
        lines.append(f"- {msg}")
    else:
        lines.append("- Folder name has no MMDDYY due-date prefix; urgency cannot be computed.")
    lines.append("")

    checklist_rows: list[list[str]] = []
    if not work.exists():
        errors.append("bid-package-working/ does not exist.")
    for rel, label, required in CHECKLIST:
        target = work / rel
        exists = target.exists()
        status = "OK" if exists else ("MISSING" if required else "optional")
        checklist_rows.append([status, label, f"`bid-package-working/{rel}`"])
        if required and not exists:
            alerts.append(f"Missing required deliverable: bid-package-working/{rel}")
    lines += ["## Deliverable Checklist", ""]
    lines += markdown_table(["Status", "Deliverable", "Path"], checklist_rows)
    lines.append("")

    source_warnings = check_page_sources(work)
    warnings.extend(source_warnings)

    json_errors, json_warnings = check_takeoff_jsons(work, profile)
    errors.extend(json_errors)
    warnings.extend(json_warnings)

    flag_terms = profile.get("exclude_terms", []) + profile.get("review_terms", [])
    counts = scan_text_extracts(work / "text-extracts", flag_terms)
    if counts:
        lines += ["## Scope-Flag Scan", ""]
        lines += markdown_table(
            ["Term", "Mentions", "Action"],
            [
                [
                    term,
                    count,
                    "Exclude or flag before pricing"
                    if term in profile.get("exclude_terms", []) + profile.get("review_terms", [])
                    else "Review",
                ]
                for term, count in counts.items()
                if count
            ]
            or [["No tracked terms found", 0, ""]],
        )
        lines.append("")

    addenda = sorted(
        p
        for p in project.rglob("*")
        if p.is_file()
        and "bid-package-working" not in p.parts
        and re.search(r"addend|revision|\brev\b|bulletin", p.name, re.I)
    )
    if addenda:
        warnings.append("Addendum/revision-named files found; confirm takeoff uses latest basis.")
        lines += ["## Addendum / Revision Files", ""]
        lines += [f"- `{path.relative_to(project)}`" for path in addenda]
        lines.append("")

    if warnings:
        lines += ["## Warnings", ""]
        lines += [f"- {warning}" for warning in warnings]
        lines.append("")
    if errors:
        lines += ["## Hard Errors", ""]
        lines += [f"- {error}" for error in errors]
        lines.append("")

    if not warnings and not errors and not alerts:
        lines += ["## Result", "", "- Clean: no hard errors or warnings found.", ""]
    else:
        lines += ["## Result", "", f"- Alerts: {len(alerts)}", f"- Warnings: {len(warnings)}", f"- Hard errors: {len(errors)}", ""]

    out = work / "ALERTS.md"
    if write:
        out.write_text("\n".join(lines), encoding="utf-8")
    exit_code = 1 if errors else 0
    return out, exit_code, warnings, errors
