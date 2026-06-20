---
name: division-12-furnishings-bid-scope
description: Whole-division starter rules for CSI Division 12 - Furnishings. Use when starting, triaging, validating, or packaging a commercial furnishings bid.
---

# Division 12 - Furnishings Bid Scope

Company: Your Company
CSI division(s): 12
Spec section hints: 12 00 00, 12 21 00, 12 24 00, 12 32 00, 12 36 00, 12 48 00, 12 50 00

## Scope Rule

Base bid is limited to CSI Division 12 - Furnishings work specifically assigned to the bidder: window treatments, casework, countertops, entrance mats, furniture, seating, and systems furniture. Millwork in Division 06, appliances, electrical/data connections, blocking, and owner-furnished items must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- window treatments
- manufactured casework when assigned
- countertops when assigned
- entrance floor mats and frames
- furniture and seating when assigned
- systems furniture when assigned
- accessory furnishings when assigned

## Terms That Usually Identify This Scope

- furnishings
- window treatment
- shade
- casework
- countertop
- furniture
- seating
- entrance mat
- 12 00

## Adjacent Scope To Exclude By Default

- rough carpentry
- electrical wiring
- plumbing fixtures
- appliances

## Adjacent Scope To Flag Before Pricing

- blocking
- power/data
- owner furnished
- field measure

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-12-furnishings`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-12-furnishings` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
