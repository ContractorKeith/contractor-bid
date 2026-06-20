---
name: division-03-concrete-bid-scope
description: Whole-division starter rules for CSI Division 03 - Concrete. Use when starting, triaging, validating, or packaging a commercial concrete bid.
---

# Division 03 - Concrete Bid Scope

Company: Your Company
CSI division(s): 03
Spec section hints: 03 00 00, 03 10 00, 03 20 00, 03 30 00, 03 35 00, 03 40 00, 03 60 00

## Scope Rule

Base bid is limited to CSI Division 03 - Concrete work specifically assigned to the bidder: forming, reinforcing, cast-in-place, precast, finishes, and concrete repair. Earthwork, asphalt paving, utilities, landscaping, structural steel, waterproofing, and delegated design must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- concrete formwork
- reinforcing steel and accessories
- cast-in-place concrete
- concrete slabs and pads
- concrete finishing and curing
- precast concrete when assigned
- concrete repair and patching when assigned

## Terms That Usually Identify This Scope

- concrete
- cast-in-place
- precast
- rebar
- reinforcing
- formwork
- slab
- footing
- curb
- 03 00

## Adjacent Scope To Exclude By Default

- asphalt
- striping
- landscaping
- irrigation
- site utility

## Adjacent Scope To Flag Before Pricing

- sawcut
- demolition
- excavation
- vapor barrier
- waterproofing

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-03-concrete`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-03-concrete` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
