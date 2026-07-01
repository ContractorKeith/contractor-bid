---
name: division-04-masonry-bid-scope
description: Whole-division starter rules for CSI Division 04 - Masonry. Use when starting, triaging, validating, or packaging a commercial masonry bid.
---

# Division 04 - Masonry Bid Scope

Company: Your Company
CSI division(s): 04
Spec section hints: 04 00 00, 04 05 00, 04 20 00, 04 22 00, 04 40 00, 04 70 00

## Scope Rule

Base bid is limited to CSI Division 04 - Masonry work specifically assigned to the bidder: unit masonry, stone, masonry accessories, reinforcement, grout, mortar, cleaning, and restoration. Structural steel, concrete, waterproofing, sealants, insulation, and delegated engineering must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- CMU and unit masonry
- brick masonry
- stone assemblies when assigned
- mortar and grout
- masonry reinforcement and ties
- lintels and masonry accessories when assigned
- masonry cleaning and restoration when assigned

## Terms That Usually Identify This Scope

- masonry
- CMU
- concrete masonry unit
- brick
- block
- stone
- mortar
- grout
- 04 00

## Adjacent Scope To Exclude By Default

- structural steel
- cast-in-place concrete
- sealant
- waterproofing

## Adjacent Scope To Flag Before Pricing

- lintel
- flashing
- weep
- cavity insulation
- restoration

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-04-masonry`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-04-masonry` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
