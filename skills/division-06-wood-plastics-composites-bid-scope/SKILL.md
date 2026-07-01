---
name: division-06-wood-plastics-composites-bid-scope
description: Whole-division starter rules for CSI Division 06 - Wood, Plastics, and Composites. Use when starting, triaging, validating, or packaging a commercial carpentry or millwork bid.
---

# Division 06 - Wood, Plastics, and Composites Bid Scope

Company: Your Company
CSI division(s): 06
Spec section hints: 06 00 00, 06 10 00, 06 16 00, 06 20 00, 06 40 00, 06 60 00

## Scope Rule

Base bid is limited to CSI Division 06 - Wood, Plastics, and Composites work specifically assigned to the bidder: rough carpentry, sheathing, blocking, architectural woodwork, countertops, and plastic/composite fabrications. Framing in other divisions, casework in Division 12, waterproofing, hardware, and finishes must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- rough carpentry
- wood blocking and backing
- wood sheathing and panels
- architectural woodwork when assigned
- plastic laminate work when assigned
- countertops when assigned
- composite fabrications when assigned

## Terms That Usually Identify This Scope

- rough carpentry
- wood
- blocking
- backing
- sheathing
- millwork
- casework
- plastic laminate
- countertop
- 06 00

## Adjacent Scope To Exclude By Default

- metal framing
- finish painting
- door hardware
- waterproofing

## Adjacent Scope To Flag Before Pricing

- casework
- countertop
- fire-retardant
- blocking by others

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-06-wood-plastics-composites`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-06-wood-plastics-composites` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
