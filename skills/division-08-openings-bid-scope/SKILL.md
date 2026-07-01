---
name: division-08-openings-bid-scope
description: Whole-division starter rules for CSI Division 08 - Openings. Use when starting, triaging, validating, or packaging a commercial doors, frames, hardware, glazing, or storefront bid.
---

# Division 08 - Openings Bid Scope

Company: Your Company
CSI division(s): 08
Spec section hints: 08 00 00, 08 11 00, 08 14 00, 08 31 00, 08 41 00, 08 44 00, 08 71 00, 08 80 00

## Scope Rule

Base bid is limited to CSI Division 08 - Openings work specifically assigned to the bidder: doors, frames, access panels, entrances, storefront, curtain wall, windows, hardware, glazing, and louvers. Structural steel, low-voltage wiring, access control, painting, and wall construction must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- hollow metal doors and frames
- wood doors when assigned
- access doors and panels
- aluminum entrances and storefront when assigned
- windows and curtain wall when assigned
- finish hardware
- glazing and louvers when assigned

## Terms That Usually Identify This Scope

- door
- frame
- hardware
- storefront
- curtain wall
- window
- glazing
- louver
- access panel
- 08 00

## Adjacent Scope To Exclude By Default

- low-voltage wiring
- card reader
- painting
- structural steel

## Adjacent Scope To Flag Before Pricing

- access control
- electric strike
- panic
- closer
- fire rating

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-08-openings`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-08-openings` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
