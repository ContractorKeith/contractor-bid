# Troubleshooting

## `contractor-bid` Is Not Found

Check that the install location is on your `PATH`.

For `pipx` installs:

```bash
pipx ensurepath
```

Then open a new terminal and run:

```bash
contractor-bid doctor
```

## PDF Pages Do Not Render

Rendered candidate page images require Poppler's `pdftoppm`.

Check:

```bash
contractor-bid doctor
```

Install Poppler with your platform package manager, then rerun triage with `--render`.

## Triage Finds No Candidate Pages

Common causes:

- source PDFs are scanned image-only and need OCR first
- the wrong profile was selected
- bid documents are not in `bid-docs/`
- the relevant scope is described with terms missing from the profile

Review `bid-package-working/text-extracts/` when text extraction is available. If those files
are empty or nearly empty, OCR is probably needed before triage can work.

## `build-packets` Writes No Packet PDFs

`build-packets` uses approved source pages from:

```text
bid-package-working/takeoff/scope-pages-sources.json
```

Review `scope-pages-sources.suggested.json`, copy approved entries into the canonical file,
and rerun:

```bash
contractor-bid build-packets <project>
```

## Workbook Build Fails

The workbook builder expects exactly one takeoff JSON file besides the page-source JSON unless
you pass `--config`.

Check:

```text
bid-package-working/takeoff/
```

Then run:

```bash
contractor-bid build-workbook <project> --profile <profile> --config <takeoff-json>
```

## Scope Guardrails Fail

If a BOM row includes an excluded term and is marked `Included`, the workbook build or check
can fail. That is intentional.

Fix the BOM row by:

- changing the status to excluded or review-only
- moving it to an alternate
- updating the profile only if the company truly carries that scope

## GitHub Pages Does Not Deploy

The docs workflow expects GitHub Pages to use GitHub Actions as the source. A repository admin
can configure that in GitHub repository settings or through the Pages API.

The workflow builds with:

```bash
mkdocs build --strict
```

Run that locally before pushing docs changes.
