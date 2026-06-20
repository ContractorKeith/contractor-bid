# Workflow

## One-Time Setup

```bash
git clone https://github.com/ContractorKeith/contractor-bid.git
cd contractor-bid
scripts/install.sh --install-poppler
```

On Windows, run `.\scripts\install.ps1 -InstallPoppler` from PowerShell.

Poppler provides `pdfinfo`, `pdftotext`, and `pdftoppm`. The scripts fall back to `pypdf` for some text/page-count work, but Poppler is faster and required for rendered page images.

Check a machine with:

```bash
contractor-bid doctor
```

## Per-Bid Pipeline

1. Create or select a scope profile.
2. Create a bid project folder.
3. Add bid documents.
4. Triage PDFs.
5. Review `candidate-pages.md` and `scope-pages-sources.suggested.json`.
6. Copy approved suggestions into `scope-pages-sources.json`; do not blindly accept every hit.
7. Build page packets and quick-read summary.
8. Fill the takeoff JSON and build the workbook.
9. Update the reference index and proposal letter.
10. Run alerts check.
11. Package sendoff.

Use `contractor-bid status <project> --profile <profile>` for a non-writing readiness check.
After the page-source and takeoff JSON files have been reviewed and filled, `contractor-bid run`
can rebuild packets, workbook, alerts, and sendoff in one pass.

Built-in starter profiles:

- Canonical CSI starters use `division-XX-*` ids and cover every active MasterFormat division from 03 through 33.
- Trade-specific examples such as `fences-gates`, `concrete-flatwork`, `drywall-framing`, `electrical`, `plumbing`, `hvac`, and `roofing` show how to narrow a division into a company-specific bid scope.
- See `docs/CSI_DIVISIONS.md` for the full active/reserved division table.

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
