---
name: division-10-specialties-bid-scope
description: Whole-division starter rules for CSI Division 10 - Specialties. Use when starting, triaging, validating, or packaging a commercial specialties bid.
---

# Division 10 - Specialties Bid Scope

Company: Your Company
CSI division(s): 10
Spec section hints: 10 00 00, 10 14 00, 10 21 13, 10 22 00, 10 28 00, 10 44 00, 10 51 00

## Scope Rule

Base bid is limited to CSI Division 10 - Specialties work specifically assigned to the bidder: visual display units, signage, partitions, toilet accessories, fire protection specialties, lockers, louvers, postal specialties, and other specialty products. Blocking, backing, electrical, plumbing, structural supports, and installation by others must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- visual display units
- signage when assigned
- toilet compartments and accessories
- fire extinguisher cabinets
- lockers and storage specialties
- operable partitions when assigned
- miscellaneous specialty products

## Terms That Usually Identify This Scope

- specialties
- signage
- toilet accessory
- toilet partition
- locker
- fire extinguisher cabinet
- markerboard
- corner guard
- 10 00

## Adjacent Scope To Exclude By Default

- rough carpentry
- electrical wiring
- plumbing
- structural support

## Adjacent Scope To Flag Before Pricing

- blocking
- backing
- owner furnished
- sign permit
- electrical

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-10-specialties`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-10-specialties` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
