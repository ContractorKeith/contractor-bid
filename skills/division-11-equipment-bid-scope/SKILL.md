---
name: division-11-equipment-bid-scope
description: Whole-division starter rules for CSI Division 11 - Equipment. Use when starting, triaging, validating, or packaging a commercial equipment bid.
---

# Division 11 - Equipment Bid Scope

Company: Your Company
CSI division(s): 11
Spec section hints: 11 00 00, 11 10 00, 11 30 00, 11 40 00, 11 52 00, 11 53 00, 11 70 00

## Scope Rule

Base bid is limited to CSI Division 11 - Equipment work specifically assigned to the bidder: commercial, foodservice, loading dock, laboratory, athletic, and other facility equipment. Utility rough-ins, structural supports, controls, owner-furnished equipment, and commissioning must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- commercial equipment when assigned
- foodservice equipment when assigned
- loading dock equipment when assigned
- laboratory equipment when assigned
- athletic and recreational equipment when assigned
- equipment anchorage when assigned
- startup assistance when assigned

## Terms That Usually Identify This Scope

- equipment
- foodservice
- appliance
- dock leveler
- laboratory equipment
- athletic equipment
- washer
- dryer
- 11 00

## Adjacent Scope To Exclude By Default

- electrical wiring
- plumbing piping
- gas piping
- structural steel

## Adjacent Scope To Flag Before Pricing

- owner furnished
- rough-in
- startup
- warranty
- anchorage

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-11-equipment`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-11-equipment` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
