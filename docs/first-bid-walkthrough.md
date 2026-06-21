# First Bid Walkthrough

This walkthrough explains the intended estimator loop. The exact profile and quantities will
change by trade, but the review pattern should stay the same.

## Step 1. Pick The Closest Scope Profile

Start broad, then narrow.

```bash
contractor-bid list-profiles
```

Use a canonical CSI starter when you want broad coverage:

```text
division-26-electrical
division-32-exterior-improvements
division-33-utilities
```

Use a trade-specific example when it matches the way you actually bid:

```text
fences-gates
concrete-flatwork
drywall-framing
electrical
plumbing
hvac
roofing
```

If none fit, create a custom profile:

```bash
contractor-bid init --profile my-scope
```

## Step 2. Create The Project

Use the bid due date in the folder name. The validator uses the `MMDDYY-` prefix for urgency
warnings.

```bash
contractor-bid new bids/070126-example-project \
  --profile division-32-exterior-improvements \
  --project-name "Example Project" \
  --bid-due "2026-07-01 14:00"
```

## Step 3. Put Source PDFs In `bid-docs/`

Source documents belong here:

```text
bids/070126-example-project/bid-docs/
```

Generated files belong under:

```text
bids/070126-example-project/bid-package-working/
```

Keeping that boundary clear makes the package easier to audit and safer to share.

## Step 4. Triage The PDFs

```bash
contractor-bid triage bids/070126-example-project \
  --profile division-32-exterior-improvements \
  --render
```

Triage produces candidate evidence. It does not approve scope.

Open:

- `bid-package-working/takeoff/candidate-pages.md`
- `bid-package-working/takeoff/triage-scope-signals.md`
- `bid-package-working/takeoff/scope-pages-sources.suggested.json`

If Poppler is installed, rendered page images are written to:

```text
bid-package-working/page-images/
```

## Step 5. Approve Source Pages

Review suggested pages and copy the accepted entries into:

```text
bid-package-working/takeoff/scope-pages-sources.json
```

Do not blindly accept every hit. A keyword match can be:

- real carried scope
- adjacent review-only scope
- an exclusion
- a bid form note
- a detail that needs an RFI

## Step 6. Build Page Packets

```bash
contractor-bid build-packets bids/070126-example-project
```

This creates reviewable PDFs and a quick-read summary when source pages are approved:

- `00-Bid-Scope-Summary.md`
- `scope-pages.pdf`
- `scope-pages-index.md`
- `spec-pages.pdf`
- `spec-pages-index.md`
- `scope-and-spec-pages.pdf`

## Step 7. Fill The Takeoff JSON

The workbook is generated from JSON under:

```text
bid-package-working/takeoff/
```

Use plan measurements, supplier quotes, and source-backed assumptions. Do not turn a PDF text
hit into a final quantity unless the quantity has been measured or explicitly accepted as a
placeholder.

## Step 8. Build The Workbook

```bash
contractor-bid build-workbook bids/070126-example-project \
  --profile division-32-exterior-improvements
```

The workbook keeps supplier inputs, line totals, RFIs, alerts, and source references together.

## Step 9. Validate The Package

```bash
contractor-bid check bids/070126-example-project \
  --profile division-32-exterior-improvements
```

Review `ALERTS.md` before pricing. Hard errors usually mean the package is not ready.

Common warnings include:

- missing source summary fields
- no confirmed spec pages
- addendum or revision files that need reconciliation
- review-only or excluded terms appearing in carried scope

## Step 10. Package The Sendoff

```bash
contractor-bid package-sendoff bids/070126-example-project
```

The sendoff zip is intended for suppliers, vendors, or internal review. Check it before
sending. It should not include unrelated private files.
