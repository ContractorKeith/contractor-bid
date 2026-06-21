# Self-Learning Pattern

This project should improve from user corrections without pretending that the scripts can infer every durable rule automatically.

## Correction Flow

1. User corrects the model or estimator.
2. Run `contractor-bid learn --note "...correction..." --profile <profile> --project <project>`.
3. Review `.contractor-bid/LESSONS.md` before the next similar bid.
4. If the correction is reusable, update one or more of:
   - `profiles/<profile>.json`
   - `skills/<profile>-bid-scope/SKILL.md`
   - templates under `templates/`
   - scripts under `src/contractor_bid/`
5. Commit the durable improvement.

## What Belongs In A Profile

- Scope terms that identify pages.
- Exclusion and review-only terms.
- CSI section hints.
- Standard proposal exclusions.
- Quantity units and common measurement basis.

## What Belongs In Scripts

- Artifact generation.
- Validation rules that apply across profiles.
- Deterministic checks for missing files, stale sendoff packages, included excluded terms, and addenda.

## What Belongs In Project Notes

- One-off GC instructions.
- Project-specific RFIs.
- Manual measurement assumptions.
- Temporary pricing placeholders.
