---
name: roofing-bid-scope
description: Bid-project scope rules for roofing. Use when starting, triaging, validating, or packaging a commercial roofing bid.
---

# Roofing Bid Scope

Company: Your Company
CSI division(s): 07
Spec section hints: 07 22 00, 07 54 00, 07 52 00, 07 62 00

## Scope Rule

Base bid is limited to roofing systems defined by the profile: membrane or steep-slope roofing, roof insulation, cover board, flashing, and roof-related sheet metal. Wood blocking and nailers, structural decking, roof drains, and below-grade waterproofing must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- membrane roofing
- roof insulation
- cover board
- base and counter flashing
- coping and edge metal
- roof curb flashing
- pipe boots
- walkway pads

## Terms That Usually Identify This Scope

- roofing
- membrane
- TPO
- EPDM
- modified bitumen
- roof insulation
- flashing
- coping
- 07 22
- 07 54

## Adjacent Scope To Exclude By Default

- structural deck
- metal deck
- below grade waterproofing
- firestopping
- gutters and downspouts

## Adjacent Scope To Flag Before Pricing

- wood blocking
- nailer
- roof drain
- overflow
- skylight
- expansion joint
- lightning protection
- fall protection

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile roofing`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile roofing` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
