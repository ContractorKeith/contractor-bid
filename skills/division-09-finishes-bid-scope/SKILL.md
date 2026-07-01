---
name: division-09-finishes-bid-scope
description: Whole-division starter rules for CSI Division 09 - Finishes. Use when starting, triaging, validating, or packaging a commercial finishes bid.
---

# Division 09 - Finishes Bid Scope

Company: Your Company
CSI division(s): 09
Spec section hints: 09 00 00, 09 21 16, 09 29 00, 09 30 00, 09 51 00, 09 65 00, 09 68 00, 09 90 00

## Scope Rule

Base bid is limited to CSI Division 09 - Finishes work specifically assigned to the bidder: gypsum assemblies, tile, ceilings, flooring, wall finishes, painting, coatings, and specialty finishes. Structural framing, MEP supports, waterproofing, Division 10 specialties, and furniture must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- metal studs and gypsum board when assigned
- tile and setting materials
- acoustical ceilings
- resilient flooring
- carpet and walk-off mats when assigned
- painting and coatings
- wall coverings and specialty finishes when assigned

## Terms That Usually Identify This Scope

- finishes
- gypsum
- drywall
- tile
- ceiling
- flooring
- paint
- coating
- wall covering
- 09 00

## Adjacent Scope To Exclude By Default

- structural steel
- waterproofing
- casework
- toilet accessories

## Adjacent Scope To Flag Before Pricing

- level 5
- moisture mitigation
- floor prep
- fire-rated assembly

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-09-finishes`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-09-finishes` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
