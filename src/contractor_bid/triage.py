from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .util import markdown_table, rel_display, slugify, write_json


ROLE_PATTERNS = {
    "site / layout": r"\b(site\s+plan|overall\s+plan|layout|key\s+plan)\b",
    "detail": r"\b(detail|section|elevation|assembly|schedule)\b",
    "specification": r"\b(specification|project\s+manual|section\s+\d{2}\s+\d{2})\b",
    "addendum / revision": r"\b(addendum|addenda|revision|bulletin|rfi)\b",
    "access / controls": r"\b(access\s+control|operator|panel|controller|keypad|reader|alarm)\b",
}

SHEET_RE = re.compile(r"\b([A-Z]{1,4}[- ]?\d+(?:\.\d+)?[A-Z]?)\b")
SOURCE_PLACEHOLDERS = ("PROJECT NAME", "YYYY-MM-DD", "TBD", "TODO", "{{", "}}")


@dataclass
class PageHit:
    source_file: str
    source_relpath: str
    pdf_page: int
    score: int
    status: str
    include_terms: list[str]
    review_terms: list[str]
    exclude_terms: list[str]
    role_hints: list[str]
    quantity_mentions: list[str]
    snippet: str
    rendered_image: str = ""


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def pattern_for_terms(terms: list[str]) -> str:
    cleaned = [re.escape(term.strip()) for term in terms if term.strip()]
    if not cleaned:
        return r"a^"
    return r"\b(?:" + "|".join(cleaned) + r")\b"


def find_terms(text: str, terms: list[str]) -> list[str]:
    found: list[str] = []
    lower = text.lower()
    for term in terms:
        if term and term.lower() in lower:
            found.append(term)
    return found


def find_regex_terms(text: str, patterns: dict[str, str]) -> list[str]:
    return [name for name, pattern in patterns.items() if re.search(pattern, text, re.I | re.S)]


def quantity_mentions(text: str, units: list[str]) -> list[str]:
    unit_part = "|".join(re.escape(unit) for unit in units if unit)
    if not unit_part:
        unit_part = r"EA|LF|SF|CY|TON|HR"
    regex = re.compile(
        rf"\b(?:\d{{1,3}}(?:,\d{{3}})*|\d+)(?:\.\d+)?\s*(?:{unit_part})\b"
        rf"(?:\s+(?:of|for)\s+)?[A-Za-z0-9'\"/#().,& -]{{0,90}}",
        re.I,
    )
    values: list[str] = []
    for match in regex.finditer(text):
        value = compact(match.group(0)).strip(" ,;:-")
        if value and value.lower() not in {v.lower() for v in values}:
            values.append(value)
        if len(values) >= 8:
            break
    return values


def snippet_for(text: str, terms: list[str], radius: int = 320) -> str:
    lower = text.lower()
    positions = [lower.find(term.lower()) for term in terms if term and lower.find(term.lower()) >= 0]
    pos = min(positions) if positions else 0
    start = max(0, pos - radius)
    end = min(len(text), pos + radius)
    snippet = compact(text[start:end])
    if start:
        snippet = "..." + snippet
    if end < len(text):
        snippet += "..."
    return snippet


def pdf_count(pdf: Path) -> int:
    if shutil.which("pdfinfo"):
        info = run(["pdfinfo", str(pdf)]).stdout
        match = re.search(r"^Pages:\s+(\d+)\s*$", info, re.M)
        if match:
            return int(match.group(1))
    try:
        from pypdf import PdfReader
    except Exception as exc:
        raise RuntimeError("Install Poppler or pypdf to read PDF page counts") from exc
    return len(PdfReader(str(pdf)).pages)


def extract_page_text(pdf: Path, page: int) -> str:
    if shutil.which("pdftotext"):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "page.txt"
            run(["pdftotext", "-layout", "-f", str(page), "-l", str(page), str(pdf), str(out)])
            return out.read_text(encoding="utf-8", errors="ignore")
    try:
        from pypdf import PdfReader
    except Exception as exc:
        raise RuntimeError("Install Poppler or pypdf to extract PDF text") from exc
    reader = PdfReader(str(pdf))
    return reader.pages[page - 1].extract_text() or ""


def split_pdftotext_output(text: str, page_count: int) -> list[str] | None:
    pages = text.split("\f")
    if len(pages) == page_count + 1 and not pages[-1].strip():
        pages = pages[:-1]
    if len(pages) != page_count:
        return None
    return pages


def extract_pdf_text_pages(pdf: Path, page_count: int) -> list[str]:
    if shutil.which("pdftotext"):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "all-pages.txt"
            run(["pdftotext", "-layout", str(pdf), str(out)])
            text = out.read_text(encoding="utf-8", errors="ignore")
        pages = split_pdftotext_output(text, page_count)
        if pages is not None:
            return pages

    try:
        from pypdf import PdfReader
    except Exception as exc:
        raise RuntimeError("Install Poppler or pypdf to extract PDF text") from exc
    reader = PdfReader(str(pdf))
    return [(reader.pages[idx].extract_text() or "") for idx in range(page_count)]


def classify(score: int, includes: list[str], reviews: list[str], excludes: list[str]) -> str:
    if includes and score >= 10:
        return "primary-review"
    if includes:
        return "secondary-review"
    if reviews:
        return "flag-review"
    if excludes:
        return "exclude-review"
    return "low"


def score_page(includes: list[str], reviews: list[str], excludes: list[str], roles: list[str]) -> int:
    score = len(includes) * 5 + len(reviews) * 2 - len(excludes) * 2
    if "specification" in roles:
        score += 4
    if "site / layout" in roles or "detail" in roles:
        score += 3
    return score


def render_page_image(pdf: Path, page: int, out_dir: Path, status: str) -> str:
    if not shutil.which("pdftoppm"):
        return ""
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = out_dir / f"{slugify(pdf.stem)}-p{page:03d}-{status}"
    run(["pdftoppm", "-png", "-f", str(page), "-singlefile", "-r", "180", str(pdf), str(prefix)])
    image = prefix.with_suffix(".png")
    return image.name if image.exists() else ""


def best_effort_sheet(text: str) -> str:
    match = SHEET_RE.search(text)
    return match.group(1).replace(" ", "") if match else ""


def suggested_scope_entries(hits: list[PageHit]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    seen: set[tuple[str, int]] = set()
    for hit in hits:
        if hit.status not in {"primary-review", "secondary-review"}:
            continue
        key = (hit.source_relpath, hit.pdf_page)
        if key in seen:
            continue
        seen.add(key)
        entries.append(
            {
                "source_pdf": hit.source_relpath,
                "pdf_page": hit.pdf_page,
                "sheet": best_effort_sheet(hit.snippet),
                "title": "",
                "evidence": hit.snippet,
            }
        )
    return entries


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
    return any(token in upper for token in SOURCE_PLACEHOLDERS)


def canonical_sources_empty(data: dict[str, Any]) -> bool:
    for field in ("scope_pages", "spec_pages", "excluded_or_reference_only"):
        if data.get(field):
            return False
    fields = (
        "bid_decision_summary",
        "what_to_open_first",
        "scope_items",
        "quantity_mentions",
        "brand_or_product_mentions",
        "access_or_interface_notes",
        "not_in_base_scope",
        "open_questions",
        "no_spec_pages_found",
    )
    return all(empty_or_placeholder(data.get(field)) for field in fields)


def build_suggested_sources(project: Path, hits: list[PageHit]) -> dict[str, Any]:
    work = project / "bid-package-working"
    canonical = work / "takeoff" / "scope-pages-sources.json"
    if canonical.exists():
        try:
            data = json.loads(canonical.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    suggested = dict(data)
    suggested.setdefault("project_name", project.name)
    suggested.setdefault("prepared", "")
    suggested.setdefault("scope_note", "")
    suggested["scope_pages"] = suggested_scope_entries(hits)
    suggested.setdefault("spec_pages", [])
    suggested.setdefault("excluded_or_reference_only", [])
    return suggested


def triage_project(
    project: Path,
    profile: dict[str, Any],
    *,
    render: bool = False,
    max_render: int = 20,
    write_sources: bool = False,
) -> list[PageHit]:
    project = project.resolve()
    bid_docs = project / "bid-docs"
    work = project / "bid-package-working"
    text_dir = work / "text-extracts"
    takeoff_dir = work / "takeoff"
    image_dir = work / "page-images"
    for folder in (text_dir, takeoff_dir):
        folder.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(bid_docs.rglob("*.pdf"))
    if not pdfs:
        raise FileNotFoundError(f"No PDFs found under {bid_docs}")

    include_terms = (
        profile.get("include_terms", [])
        + profile.get("base_scope", [])
        + profile.get("spec_sections", [])
    )
    review_terms = profile.get("review_terms", [])
    exclude_terms = profile.get("exclude_terms", [])
    units = profile.get("quantity_units", [])

    hits: list[PageHit] = []
    scanned_warnings: list[str] = []
    rendered = 0
    for pdf in pdfs:
        pages = pdf_count(pdf)
        page_texts = extract_pdf_text_pages(pdf, pages)
        mean_chars = sum(len(compact(text)) for text in page_texts) / max(pages, 1)
        if mean_chars < 15:
            warning = (
                f"WARNING: {rel_display(pdf, project)} looks scanned/image-only - "
                "needs OCR before triage works."
            )
            print(warning)
            scanned_warnings.append(warning)
        combined_text: list[str] = []
        for page, text in enumerate(page_texts, start=1):
            combined_text.append(f"\n\n--- PAGE {page} ---\n{text}")
            includes = find_terms(text, include_terms)
            reviews = find_terms(text, review_terms)
            excludes = find_terms(text, exclude_terms)
            roles = find_regex_terms(text, ROLE_PATTERNS)
            quantities = quantity_mentions(text, units)
            score = score_page(includes, reviews, excludes, roles)
            status = classify(score, includes, reviews, excludes)
            if status == "low":
                continue
            image = ""
            if render and rendered < max_render and status in {
                "primary-review",
                "secondary-review",
                "flag-review",
            }:
                image = render_page_image(pdf, page, image_dir, status)
                rendered += 1 if image else 0
            hit = PageHit(
                source_file=pdf.name,
                source_relpath=rel_display(pdf, project),
                pdf_page=page,
                score=score,
                status=status,
                include_terms=includes,
                review_terms=reviews,
                exclude_terms=excludes,
                role_hints=roles,
                quantity_mentions=quantities,
                snippet=snippet_for(text, includes + reviews + excludes),
                rendered_image=image,
            )
            hits.append(hit)
        (text_dir / f"{slugify(pdf.stem)}.txt").write_text(
            "".join(combined_text), encoding="utf-8", errors="ignore"
        )

    hits.sort(key=lambda item: (item.status != "primary-review", -item.score, item.source_relpath, item.pdf_page))
    write_outputs(project, profile, hits, scanned_warnings=scanned_warnings, write_sources=write_sources)
    return hits


def write_outputs(
    project: Path,
    profile: dict[str, Any],
    hits: list[PageHit],
    *,
    scanned_warnings: list[str] | None = None,
    write_sources: bool = False,
) -> None:
    work = project / "bid-package-working"
    text_dir = work / "text-extracts"
    takeoff_dir = work / "takeoff"

    json_hits = [asdict(hit) for hit in hits]
    write_json(text_dir / "page-hits.json", {"profile": profile["profile_id"], "hits": json_hits})
    with (text_dir / "page-hits.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "status",
                "score",
                "source_relpath",
                "pdf_page",
                "include_terms",
                "review_terms",
                "exclude_terms",
                "role_hints",
                "quantity_mentions",
                "rendered_image",
            ],
        )
        writer.writeheader()
        for hit in hits:
            row = asdict(hit)
            writer.writerow({key: json.dumps(row[key]) if isinstance(row[key], list) else row[key] for key in writer.fieldnames})

    signals = {
        "profile": profile["profile_id"],
        "quantity_mentions": sorted({q for hit in hits for q in hit.quantity_mentions}),
        "include_terms": sorted({term for hit in hits for term in hit.include_terms}),
        "review_terms": sorted({term for hit in hits for term in hit.review_terms}),
        "exclude_terms": sorted({term for hit in hits for term in hit.exclude_terms}),
    }
    write_json(text_dir / "scope-signals.json", signals)

    candidate_lines = [
        f"# Candidate Pages - {project.name}",
        "",
        f"Profile: `{profile['profile_id']}` ({profile['trade_name']})",
        "",
    ]
    if scanned_warnings:
        candidate_lines += ["## Warnings", ""]
        candidate_lines += [f"- {warning}" for warning in scanned_warnings]
        candidate_lines.append("")
    for status in ("primary-review", "secondary-review", "flag-review", "exclude-review"):
        bucket = [hit for hit in hits if hit.status == status]
        candidate_lines += [f"## {status}", ""]
        if not bucket:
            candidate_lines += ["No pages found.", ""]
            continue
        rows = [
            [
                hit.score,
                hit.source_relpath,
                hit.pdf_page,
                ", ".join(hit.include_terms or hit.review_terms or hit.exclude_terms),
                hit.rendered_image,
            ]
            for hit in bucket
        ]
        candidate_lines += markdown_table(
            ["Score", "Source", "PDF page", "Why it matched", "Image"], rows
        )
        candidate_lines.append("")
    (takeoff_dir / "candidate-pages.md").write_text("\n".join(candidate_lines), encoding="utf-8")

    triage_lines = [
        f"# Triage Scope Signals - {project.name}",
        "",
        "Use these signals as a prompt aid. They are not a takeoff.",
        "",
        "## Quantity Mentions",
        "",
    ]
    triage_lines += [f"- {value}" for value in signals["quantity_mentions"]] or ["- None found."]
    triage_lines += ["", "## Include Terms", ""]
    triage_lines += [f"- {value}" for value in signals["include_terms"]] or ["- None found."]
    triage_lines += ["", "## Flag / Review Terms", ""]
    triage_lines += [f"- {value}" for value in signals["review_terms"]] or ["- None found."]
    triage_lines += ["", "## Exclusion Terms", ""]
    triage_lines += [f"- {value}" for value in signals["exclude_terms"]] or ["- None found."]
    (takeoff_dir / "triage-scope-signals.md").write_text(
        "\n".join(triage_lines) + "\n", encoding="utf-8"
    )

    suggested = build_suggested_sources(project, hits)
    suggested_path = takeoff_dir / "scope-pages-sources.suggested.json"
    write_json(suggested_path, suggested)
    suggested_count = len(suggested.get("scope_pages", []))
    print(
        f"Suggested {suggested_count} scope page(s) -> review "
        "`bid-package-working/takeoff/scope-pages-sources.suggested.json`."
    )
    if write_sources:
        canonical_path = takeoff_dir / "scope-pages-sources.json"
        current = {}
        if canonical_path.exists():
            current = json.loads(canonical_path.read_text(encoding="utf-8"))
        if not current or canonical_sources_empty(current):
            write_json(canonical_path, suggested)
            print("Wrote suggested pages into `bid-package-working/takeoff/scope-pages-sources.json`.")
        else:
            print(
                "Skipped `scope-pages-sources.json` because it already has user-entered content."
            )

    metadata = {
        "profile": profile["profile_id"],
        "project": str(project),
        "python": sys.version.split()[0],
        "hits": len(hits),
        "scanned_warnings": scanned_warnings or [],
        "suggested_scope_pages": suggested_count,
    }
    write_json(text_dir / "extraction-metadata.json", metadata)
