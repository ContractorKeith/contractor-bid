from __future__ import annotations

from collections import OrderedDict
from pathlib import Path
from typing import Any, Iterable

from .util import coerce_list, markdown_table, rel_display, read_json


def page_numbers(value: Any) -> list[int]:
    if isinstance(value, int):
        return [value]
    if isinstance(value, list):
        nums: list[int] = []
        for item in value:
            nums.extend(page_numbers(item))
        return nums
    if isinstance(value, str):
        nums: list[int] = []
        for piece in value.replace(",", "/").split("/"):
            piece = piece.strip()
            if not piece:
                continue
            if "-" in piece:
                start, end = piece.split("-", 1)
                if start.strip().isdigit() and end.strip().isdigit():
                    nums.extend(range(int(start.strip()), int(end.strip()) + 1))
            elif piece.isdigit():
                nums.append(int(piece))
        return nums
    return []


def resolve_source(raw: str, project: Path, work: Path) -> Path:
    candidate = Path(raw)
    if candidate.is_absolute():
        return candidate
    for base in (project, work):
        path = base / candidate
        if path.exists():
            return path
    return project / candidate


def collect_entries(items: list[dict[str, Any]], project: Path, work: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for item in items:
        source = resolve_source(str(item["source_pdf"]), project, work)
        if not source.exists():
            raise FileNotFoundError(f"Source PDF not found: {item['source_pdf']} ({source})")
        for page in page_numbers(item.get("pdf_page")):
            entry = dict(item)
            entry["pdf_path"] = source
            entry["pdf_page"] = page
            entries.append(entry)
    deduped: OrderedDict[tuple[str, int], dict[str, Any]] = OrderedDict()
    for entry in entries:
        deduped.setdefault((str(entry["pdf_path"]), int(entry["pdf_page"])), entry)
    return list(deduped.values())


def format_item(item: Any) -> str:
    if isinstance(item, dict):
        label_parts = []
        for key in ("sheet", "section", "title"):
            if item.get(key):
                label_parts.append(str(item[key]))
        if item.get("pdf_page"):
            label_parts.append(f"page {item['pdf_page']}")
        if item.get("source_pdf"):
            label_parts.append(f"`{item['source_pdf']}`")
        label = " - ".join(label_parts)
        note = item.get("why") or item.get("evidence") or item.get("note") or ""
        if label and note:
            return f"{label}: {note}"
        return label or note or str(item)
    return str(item)


def bullets(items: Any, empty: str = "Not filled yet.") -> list[str]:
    values = [format_item(item) for item in coerce_list(items)]
    values = [value for value in values if value.strip()]
    return [f"- {value}" for value in values] if values else [f"- {empty}"]


def write_packet(
    entries: list[dict[str, Any]],
    out_pdf: Path,
    out_index: Path,
    data: dict[str, Any],
    project: Path,
    packet_label: str,
    excluded: list[dict[str, Any]] | None = None,
) -> int:
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError as exc:
        raise RuntimeError("pypdf is required for PDF packet generation") from exc

    writer = PdfWriter()
    readers: dict[str, PdfReader] = {}
    rows: list[list[Any]] = []
    for packet_page, entry in enumerate(entries, start=1):
        pdf_path: Path = entry["pdf_path"]
        reader = readers.setdefault(str(pdf_path), PdfReader(str(pdf_path)))
        source_index = int(entry["pdf_page"]) - 1
        if source_index < 0 or source_index >= len(reader.pages):
            raise ValueError(
                f"Page {entry['pdf_page']} out of range for {pdf_path} ({len(reader.pages)} pages)"
            )
        writer.add_page(reader.pages[source_index])
        try:
            writer.add_outline_item(
                f"{entry.get('sheet', '')} {entry.get('title', '')}".strip() or f"Page {packet_page}",
                packet_page - 1,
            )
        except Exception:
            pass
        rows.append(
            [
                packet_page,
                f"`{rel_display(pdf_path, project)}`",
                entry["pdf_page"],
                entry.get("sheet", ""),
                entry.get("title", ""),
                entry.get("evidence", ""),
            ]
        )

    writer.add_metadata(
        {
            "/Title": f"{data.get('project_name', 'Project')} - {packet_label}",
            "/Subject": "Bid source pages extracted by contractor-bid",
        }
    )
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    with out_pdf.open("wb") as fh:
        writer.write(fh)

    lines = [
        f"# {packet_label} Index",
        "",
        f"Project: {data.get('project_name', '')}",
        f"Prepared: {data.get('prepared', '')}",
        f"Output: `{out_pdf.name}`",
        "",
        data.get("scope_note", ""),
        "",
    ]
    lines += markdown_table(
        ["Packet page", "Source file", "Source PDF page", "Sheet / Detail", "Title", "Evidence"],
        rows,
    )
    if excluded:
        lines += ["", "## Excluded / Reference Only", ""]
        lines += markdown_table(
            ["Source file", "Source PDF page", "Reason"],
            [
                [f"`{item.get('source_pdf', '')}`", item.get("pdf_page", ""), item.get("reason", "")]
                for item in excluded
            ],
        )
    lines += ["", "## Output Summary", "", f"- `{out_pdf.name}` pages: {len(entries)}"]
    out_index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(entries)


def write_summary(
    data: dict[str, Any],
    project: Path,
    scope_count: int,
    spec_count: int,
    combined_exists: bool,
) -> Path:
    work = project / "bid-package-working"
    open_first = work / ("scope-and-spec-pages.pdf" if combined_exists else "scope-pages.pdf")
    lines = [
        f"# Bid Scope Summary - {data.get('project_name', project.name)}",
        "",
        f"Prepared: {data.get('prepared', '')}",
        "",
        "## Quick Read",
        "",
        data.get("bid_decision_summary", "Not filled yet."),
        "",
        "## Extracted Packet Location",
        "",
        f"- Open this first: `{open_first}`",
        f"- `{work / 'scope-pages.pdf'}` ({scope_count} page(s))",
    ]
    if spec_count:
        lines.append(f"- `{work / 'spec-pages.pdf'}` ({spec_count} page(s))")
    if combined_exists:
        lines.append(f"- `{work / 'scope-and-spec-pages.pdf'}` ({scope_count + spec_count} page(s))")

    sections = [
        ("What To Open First", "what_to_open_first"),
        ("Scope Items To Consider", "scope_items"),
        ("Quantity Mentions", "quantity_mentions"),
        ("Brand / Product / System Mentions", "brand_or_product_mentions"),
        ("Access / Interface Notes", "access_or_interface_notes"),
        ("Not In Base Scope", "not_in_base_scope"),
        ("Open Questions Before Pricing", "open_questions"),
    ]
    for title, key in sections:
        lines += ["", f"## {title}", ""]
        lines += bullets(data.get(key))

    rows: list[list[Any]] = []
    for label, items in (("Scope", data.get("scope_pages", [])), ("Spec", data.get("spec_pages", []))):
        for item in items:
            rows.append(
                [
                    label,
                    f"`{item.get('source_pdf', '')}`",
                    item.get("pdf_page", ""),
                    item.get("sheet", ""),
                    item.get("title", ""),
                    item.get("evidence", ""),
                ]
            )
    if rows:
        lines += ["", "## Extracted Source Map", ""]
        lines += markdown_table(
            ["Packet", "Source file", "Source PDF page", "Sheet / Detail", "Title", "Evidence"],
            rows,
        )

    excluded = data.get("excluded_or_reference_only", [])
    if excluded:
        lines += ["", "## Excluded / Reference Only", ""]
        lines += markdown_table(
            ["Source file", "Source PDF page", "Reason"],
            [
                [f"`{item.get('source_pdf', '')}`", item.get("pdf_page", ""), item.get("reason", "")]
                for item in excluded
            ],
        )

    lines += ["", "## Scope Rule", "", data.get("scope_note", "Confirm scope boundary before pricing.")]
    out = work / "00-Bid-Scope-Summary.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def build_packets(project: Path, *, sources: Path | None = None) -> dict[str, Any]:
    project = project.resolve()
    work = project / "bid-package-working"
    sources_path = sources or work / "takeoff" / "scope-pages-sources.json"
    data = read_json(sources_path)

    scope_entries = collect_entries(data.get("scope_pages", []), project, work)
    spec_entries = collect_entries(data.get("spec_pages", []), project, work)
    excluded = data.get("excluded_or_reference_only", [])

    scope_count = 0
    spec_count = 0
    if scope_entries:
        scope_count = write_packet(
            scope_entries,
            work / "scope-pages.pdf",
            work / "scope-pages-index.md",
            data,
            project,
            "Scope Pages",
            excluded,
        )
    if spec_entries:
        spec_count = write_packet(
            spec_entries,
            work / "spec-pages.pdf",
            work / "spec-pages-index.md",
            data,
            project,
            "Spec Pages",
            None,
        )

    combined_exists = False
    if scope_count and spec_count:
        try:
            from pypdf import PdfReader, PdfWriter
        except ImportError as exc:
            raise RuntimeError("pypdf is required for combined PDF generation") from exc
        writer = PdfWriter()
        for packet in (work / "scope-pages.pdf", work / "spec-pages.pdf"):
            reader = PdfReader(str(packet))
            for page in reader.pages:
                writer.add_page(page)
        combined = work / "scope-and-spec-pages.pdf"
        with combined.open("wb") as fh:
            writer.write(fh)
        combined_exists = True

    # Keep the summary useful even before the user has installed pypdf or filled pages.
    summary = write_summary(data, project, scope_count, spec_count, combined_exists)

    return {
        "scope_pages": scope_count,
        "spec_pages": spec_count,
        "combined": combined_exists,
        "summary": str(summary),
    }
