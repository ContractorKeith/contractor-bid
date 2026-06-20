---
name: division-07-thermal-moisture-protection-bid-scope
description: Whole-division starter rules for CSI Division 07 - Thermal and Moisture Protection. Use when starting, triaging, validating, or packaging a commercial roofing, waterproofing, insulation, firestopping, or sealants bid.
---

# Division 07 - Thermal and Moisture Protection Bid Scope

Company: Your Company
CSI division(s): 07
Spec section hints: 07 00 00, 07 10 00, 07 21 00, 07 24 00, 07 27 00, 07 50 00, 07 60 00, 07 84 00, 07 90 00

## Scope Rule

Base bid is limited to CSI Division 07 - Thermal and Moisture Protection work specifically assigned to the bidder: waterproofing, insulation, air barriers, roofing, flashing, sheet metal, firestopping, joint protection, and sealants. Structural deck, framing, roof drains, interior finishes, and MEP penetrations must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- below-grade waterproofing when assigned
- thermal insulation
- air and vapor barriers
- roofing assemblies
- flashing and sheet metal
- firestopping
- joint sealants and expansion joints

## Terms That Usually Identify This Scope

- roofing
- waterproofing
- insulation
- air barrier
- vapor barrier
- flashing
- sheet metal
- firestopping
- sealant
- 07 00

## Adjacent Scope To Exclude By Default

- structural deck
- roof drain plumbing
- metal framing
- interior painting

## Adjacent Scope To Flag Before Pricing

- wood blocking
- roof drain
- curb
- penetration
- warranty

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-07-thermal-moisture-protection`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-07-thermal-moisture-protection` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
