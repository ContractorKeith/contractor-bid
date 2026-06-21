# Quick Start

This page creates a bid workspace from a built-in profile. It does not require real pricing
data yet.

## 1. Create A Workspace

```bash
mkdir contractor-bid-workspace
cd contractor-bid-workspace
```

## 2. Create A Bid Project

Choose a profile. Whole-division starters use `division-XX-*` ids. Narrow examples like
`fences-gates`, `electrical`, and `hvac` are also included.

```bash
contractor-bid new bids/070126-example-project \
  --profile division-32-exterior-improvements \
  --project-name "Example Project" \
  --bid-due "2026-07-01 14:00"
```

The project will include:

```text
bids/070126-example-project/
  bid-docs/
  bid-package-working/
  project.json
```

## 3. Add Source Documents

Put source PDFs and bid forms in:

```text
bids/070126-example-project/bid-docs/
```

Do not commit real bid documents, supplier quotes, estimates, tracker files, or customer data
to the public repo.

## 4. Run Triage

```bash
contractor-bid triage bids/070126-example-project \
  --profile division-32-exterior-improvements \
  --render
```

Review:

- `bid-package-working/takeoff/candidate-pages.md`
- `bid-package-working/takeoff/scope-pages-sources.suggested.json`

Copy only approved source pages into:

```text
bid-package-working/takeoff/scope-pages-sources.json
```

## 5. Build Review Artifacts

```bash
contractor-bid build-packets bids/070126-example-project
```

Then fill the project takeoff JSON from source-backed quantities and quotes. After that:

```bash
contractor-bid build-workbook bids/070126-example-project \
  --profile division-32-exterior-improvements

contractor-bid check bids/070126-example-project \
  --profile division-32-exterior-improvements

contractor-bid package-sendoff bids/070126-example-project
```

Use `status` when you want a non-writing readiness check:

```bash
contractor-bid status bids/070126-example-project \
  --profile division-32-exterior-improvements
```
