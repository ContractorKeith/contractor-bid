---
name: drywall-framing-bid-scope
description: Bid-project scope rules for drywall and metal framing. Use when starting, triaging, validating, or packaging a commercial interiors bid.
---

# Drywall and Metal Framing Bid Scope

Company: Your Company
CSI division(s): 09
Spec section hints: 09 21 16, 09 29 00

## Scope Rule

Base bid is limited to metal framing, gypsum board assemblies, finishing, and listed accessories. Adjacent insulation, ceilings, blocking, painting, and firestopping must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- metal studs
- gypsum board
- shaftwall
- drywall finishing
- corner bead
- control joints

## Terms That Usually Identify This Scope

- gypsum
- drywall
- metal stud
- shaftwall
- partition
- 09 21

## Adjacent Scope To Exclude By Default

- millwork
- casework
- doors
- hardware
- flooring

## Adjacent Scope To Flag Before Pricing

- insulation
- acoustical ceiling
- firestopping
- blocking
- painting

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile drywall-framing`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile drywall-framing` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
