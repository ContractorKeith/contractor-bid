# Agent Instructions

This repo builds AI-ready commercial subcontractor bid projects.

## Operating Rules

- Read `profiles/<profile>.json` and `skills/<profile>-bid-scope/SKILL.md` before making scope calls.
- Source PDFs and bid forms belong in `bid-docs/`; generated artifacts belong in `bid-package-working/`.
- Treat `takeoff/*.json` as the source of truth for workbook generation.
- Do not silently include excluded or review-only adjacent scopes in base bid.
- Carry the same scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff.
- Record user corrections with `contractor-bid learn`; only update durable profile rules when the user confirms the correction should persist.

## Standard Pipeline

```bash
python -m contractor_bid triage <project> --profile <profile> --render
python -m contractor_bid build-packets <project>
python -m contractor_bid build-workbook <project> --profile <profile>
python -m contractor_bid check <project> --profile <profile>
python -m contractor_bid package-sendoff <project>
```

## Review Before Pricing

- Latest addendum/revision basis.
- Manual measurements and quantity basis.
- Scope exclusions and review-only terms.
- Alternates versus base bid.
- GC bid-form requirements.
- Supplier quote inputs and lead times.
