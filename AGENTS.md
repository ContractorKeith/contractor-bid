# Agent Instructions

This repo builds AI-ready commercial subcontractor bid projects.

## Operating Rules

- Read `profiles/<profile>.json` and `skills/<profile>-bid-scope/SKILL.md` before making scope calls.
- Built-in starter profiles are `fences-gates`, `concrete-flatwork`, `drywall-framing`, and `electrical`.
- If none of the starter profiles fit, run `contractor-bid init` to create a custom profile and matching skill.
- Source PDFs and bid forms belong in `bid-docs/`; generated artifacts belong in `bid-package-working/`.
- Treat `takeoff/*.json` as the source of truth for workbook generation.
- Do not silently include excluded or review-only adjacent scopes in base bid.
- Carry the same scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff.
- Record user corrections with `contractor-bid learn`; only update durable profile rules when the user confirms the correction should persist.

## Standard Pipeline

```bash
contractor-bid doctor
contractor-bid triage <project> --profile <profile> --render
contractor-bid build-packets <project>
contractor-bid build-workbook <project> --profile <profile>
contractor-bid check <project> --profile <profile>
contractor-bid package-sendoff <project>
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
