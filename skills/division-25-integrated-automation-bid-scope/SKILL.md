---
name: division-25-integrated-automation-bid-scope
description: Whole-division starter rules for CSI Division 25 - Integrated Automation. Use when starting, triaging, validating, or packaging a commercial building automation or integration bid.
---

# Division 25 - Integrated Automation Bid Scope

Company: Your Company
CSI division(s): 25
Spec section hints: 25 00 00, 25 05 00, 25 08 00, 25 10 00, 25 30 00, 25 50 00, 25 90 00

## Scope Rule

Base bid is limited to CSI Division 25 - Integrated Automation work specifically assigned to the bidder: building automation integration, networking, controllers, programming, sequences, analytics, and system interfaces. Mechanical controls in Division 23, electrical power, low-voltage cabling, cybersecurity requirements, and owner platform work must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- integrated automation controllers
- building automation software when assigned
- integration gateways and interfaces
- sequences and programming
- automation network coordination
- graphics and trend setup when assigned
- commissioning support when assigned

## Terms That Usually Identify This Scope

- integrated automation
- building automation
- BAS
- BMS
- DDC
- controls integration
- gateway
- sequence of operation
- 25 00

## Adjacent Scope To Exclude By Default

- electrical power
- mechanical equipment
- low-voltage cabling
- fire alarm

## Adjacent Scope To Flag Before Pricing

- owner platform
- cybersecurity
- network
- commissioning
- training

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-25-integrated-automation`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-25-integrated-automation` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
