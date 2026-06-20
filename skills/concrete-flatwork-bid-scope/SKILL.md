---
name: concrete-flatwork-bid-scope
description: Bid-project scope rules for concrete flatwork. Use when starting, triaging, validating, or packaging a commercial concrete flatwork bid.
---

# Concrete Flatwork Bid Scope

Company: Your Company
CSI division(s): 03
Spec section hints: 03 30 00, 03 20 00

## Scope Rule

Base bid is limited to concrete flatwork defined by the profile. Adjacent sitework, asphalt, striping, landscaping, and utility work must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- slabs
- sidewalks
- curbs
- equipment pads
- reinforcing for carried concrete

## Terms That Usually Identify This Scope

- concrete
- slab
- sidewalk
- curb
- equipment pad
- rebar
- 03 30

## Adjacent Scope To Exclude By Default

- landscaping
- irrigation
- utility
- electrical
- fence

## Adjacent Scope To Flag Before Pricing

- sawcut
- demo
- asphalt
- striping
- excavation

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile concrete-flatwork`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile concrete-flatwork` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
