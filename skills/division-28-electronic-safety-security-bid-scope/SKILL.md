---
name: division-28-electronic-safety-security-bid-scope
description: Whole-division starter rules for CSI Division 28 - Electronic Safety and Security. Use when starting, triaging, validating, or packaging a commercial security, access control, CCTV, or fire alarm bid.
---

# Division 28 - Electronic Safety and Security Bid Scope

Company: Your Company
CSI division(s): 28
Spec section hints: 28 00 00, 28 05 00, 28 10 00, 28 13 00, 28 20 00, 28 31 00, 28 46 00

## Scope Rule

Base bid is limited to CSI Division 28 - Electronic Safety and Security work specifically assigned to the bidder: access control, intrusion detection, video surveillance, electronic detection, fire alarm, and related safety systems. Door hardware, electrical power, network infrastructure, monitoring contracts, owner credentials, and fire protection must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- access control systems when assigned
- intrusion detection when assigned
- video surveillance when assigned
- fire alarm systems when assigned
- safety and security cabling when assigned
- head-end equipment and panels
- testing and certification when assigned

## Terms That Usually Identify This Scope

- security
- access control
- card reader
- CCTV
- camera
- intrusion
- fire alarm
- detection
- 28 00

## Adjacent Scope To Exclude By Default

- electrical power
- door hardware
- locksmith
- sprinkler
- network switch

## Adjacent Scope To Flag Before Pricing

- door hardware
- monitoring
- network
- permit
- programming

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-28-electronic-safety-security`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-28-electronic-safety-security` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
