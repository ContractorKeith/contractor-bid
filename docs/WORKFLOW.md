# Workflow

## One-Time Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
brew install poppler
```

Poppler provides `pdfinfo`, `pdftotext`, and `pdftoppm`. The scripts fall back to `pypdf` for text/page counts, but Poppler is usually faster and better for bid sets.

## Per-Bid Pipeline

1. Create or select a scope profile.
2. Create a bid project folder.
3. Add bid documents.
4. Triage PDFs.
5. Review candidate pages and fill `scope-pages-sources.json`.
6. Build page packets and quick-read summary.
7. Fill the takeoff JSON and build the workbook.
8. Update the reference index and proposal letter.
9. Run alerts check.
10. Package sendoff.

## Naming

Date-prefixed folder names use the bid due date: `MMDDYY-project-slug`. The validator uses that prefix for urgency warnings.

## Package Completeness

A ready project should have:

- `00-Bid-Scope-Summary.md`
- `00-Scope-Reference-Index.md`
- `01-Takeoff-Worksheet-REV1.xlsx`
- `02 - Proposal Letter.md`
- `scope-pages.pdf` and index when scope pages are isolated
- `spec-pages.pdf` and index when spec pages exist
- `takeoff/review-pages.md`
- `takeoff/scope-pages-sources.json`
- a scope takeoff JSON
- `ALERTS.md`
- a sendoff zip when files need to leave the workspace
