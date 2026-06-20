# Example Agent Session

This is the intended "open Claude, Codex, or another model" flow. Use fictional or sanitized
project data only.

## 1. User prompt

```text
Start a new bid project for my drywall and metal framing scope.
Project name: Example Tenant Improvement
Bid due: 2026-07-01 14:00
GC: Example GC
```

## 2. Agent reads the scope rules

The agent should read:

- `AGENTS.md`
- `profiles/drywall-framing.json`
- `skills/drywall-framing-bid-scope/SKILL.md`

The important instruction is the scope boundary: carry drywall/framing scope, exclude unrelated
adjacent work by default, and flag review-only terms before pricing.

## 3. Agent creates the project

```bash
contractor-bid new bids/070126-example-ti \
  --profile drywall-framing \
  --project-name "Example Tenant Improvement" \
  --bid-due "2026-07-01 14:00" \
  --gc "Example GC"
```

The user drops PDFs, addenda, bid forms, and sanitized source files into:

```text
bids/070126-example-ti/bid-docs/
```

## 4. Agent triages source PDFs

```bash
contractor-bid triage bids/070126-example-ti --profile drywall-framing --render
```

The agent reviews:

- `bid-package-working/takeoff/candidate-pages.md`
- `bid-package-working/takeoff/triage-scope-signals.md`
- `bid-package-working/takeoff/scope-pages-sources.suggested.json`

The suggested JSON is not final. The user or agent should copy only approved page entries into:

```text
bid-package-working/takeoff/scope-pages-sources.json
```

## 5. Agent builds page packets

```bash
contractor-bid build-packets bids/070126-example-ti
```

This creates the source-backed summary and page packet files when approved page sources exist.
If no pages were approved yet, the summary says to fill the sources JSON and re-run.

## 6. User or agent fills takeoff inputs

The takeoff/BOM JSON in `bid-package-working/takeoff/` must be filled from source-backed
quantities, vendor notes, and estimator judgment before the workbook is built.

The model can help draft rows. It should not invent final quantities.

## 7. Agent builds workbook, checks, and packages

```bash
contractor-bid build-workbook bids/070126-example-ti --profile drywall-framing
contractor-bid check bids/070126-example-ti --profile drywall-framing
contractor-bid package-sendoff bids/070126-example-ti
```

After the human-fill steps are done, the shorthand command is:

```bash
contractor-bid run bids/070126-example-ti --profile drywall-framing
```

## 8. Agent records corrections

When the user corrects a scope call:

```bash
contractor-bid learn \
  --profile drywall-framing \
  --project bids/070126-example-ti \
  --note "Flag shaftwall framing separately when rated assembly details conflict with wall types."
```

Do not make every correction permanent immediately. Update the profile, generated skill, template,
or validator only after the user confirms the correction should become a durable rule.
