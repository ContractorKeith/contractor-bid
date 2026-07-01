---
name: division-31-earthwork-bid-scope
description: Whole-division starter rules for CSI Division 31 - Earthwork. Use when starting, triaging, validating, or packaging a commercial earthwork bid.
---

# Division 31 - Earthwork Bid Scope

Company: Your Company
CSI division(s): 31
Spec section hints: 31 00 00, 31 10 00, 31 20 00, 31 23 00, 31 25 00, 31 31 00, 31 50 00

## Scope Rule

Base bid is limited to CSI Division 31 - Earthwork work specifically assigned to the bidder: clearing, grading, excavation, fill, compaction, dewatering, earth retention, and subgrade preparation. Site utilities, paving, concrete, landscaping, contaminated soils, rock removal, and survey must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- site clearing when assigned
- mass excavation and grading
- trenching and backfill when assigned
- fill and compaction
- subgrade preparation
- dewatering when assigned
- earth retention when assigned

## Terms That Usually Identify This Scope

- earthwork
- excavation
- grading
- fill
- backfill
- compaction
- subgrade
- dewatering
- 31 00

## Adjacent Scope To Exclude By Default

- site utility
- asphalt paving
- concrete paving
- landscaping
- irrigation

## Adjacent Scope To Flag Before Pricing

- rock
- unsuitable soils
- dewatering
- erosion control
- survey

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-31-earthwork`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-31-earthwork` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
