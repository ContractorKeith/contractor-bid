# Agent Instructions

This repo builds AI-ready commercial subcontractor bid projects.

## Operating Rules

- Read `profiles/<profile>.json` and `skills/<profile>-bid-scope/SKILL.md` before making scope calls.
- Built-in starter profiles are `fences-gates`, `concrete-flatwork`, `drywall-framing`, `electrical`, `plumbing`, `hvac`, and `roofing`.
- If none of the starter profiles fit, run `contractor-bid init` to create a custom profile and matching skill.
- Source PDFs and bid forms belong in `bid-docs/`; generated artifacts belong in `bid-package-working/`.
- Treat `takeoff/*.json` as the source of truth for workbook generation.
- Do not silently include excluded or review-only adjacent scopes in base bid.
- Carry the same scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff.
- Record user corrections with `contractor-bid learn`; only update durable profile rules when the user confirms the correction should persist.
- Keep the workspace bid tracker current with the `track-*` commands, but ALWAYS confirm with the user and show a one-line change summary before writing (see `skills/bid-tracker/SKILL.md`).

## Standard Pipeline

```bash
contractor-bid doctor
contractor-bid triage <project> --profile <profile> --render
# Human review: open candidate-pages.md and scope-pages-sources.suggested.json.
# Copy/merge approved pages into takeoff/scope-pages-sources.json.
contractor-bid build-packets <project>
# Human review: fill the takeoff/BOM JSON from source-backed quantities and quotes.
contractor-bid build-workbook <project> --profile <profile>
contractor-bid check <project> --profile <profile>
contractor-bid package-sendoff <project>
```

Use `contractor-bid status <project> --profile <profile>` for a non-writing readiness check,
or `contractor-bid run <project> --profile <profile>` after the two human-fill steps are done.

## Bid Tracker

Maintain a workspace-wide pipeline view with the `track-*` commands. Source of truth is
`.contractor-bid/bid-tracker.json`; the readable sheet is `Bid-Tracker.xlsx` (Active Bids +
Archived & Completed). Read `skills/bid-tracker/SKILL.md` first.

Hard rule: never write to the tracker silently. Before any `track-add`, `track-update`,
`track-move`, or `track-reopen`, show the user a one-line summary of the change and wait for
confirmation. `track-list` and `track-build` are read-only.

```bash
contractor-bid track-add bids/<project> --progress Triage     # add a bid (pulls project.json)
contractor-bid track-update "<bid>" --progress Submitted --next "Follow up Friday"
contractor-bid track-move "<bid>" --outcome won               # moves it to Archived & Completed
contractor-bid track-list                                     # read-only
```

## Review Before Pricing

- Latest addendum/revision basis.
- Manual measurements and quantity basis.
- Scope exclusions and review-only terms.
- Alternates versus base bid.
- GC bid-form requirements.
- Supplier quote inputs and lead times.

## Installation Assumptions

- Normal users install with `scripts/install.sh` or `scripts/install.ps1`.
- Python package dependencies are installed into the contractor-bid virtualenv.
- Poppler is recommended for PDF extraction/rendering; without it, `pypdf` fallback works for some PDFs but page images are unavailable.
- GitHub CLI is not required for normal use.
