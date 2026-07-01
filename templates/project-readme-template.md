# {{PROJECT_NAME}} - {{TRADE_NAME}} Bid Project

Scope profile: `{{PROFILE_ID}}`  
Bid due: {{BID_DUE}}  
GC: {{GC}}  
Address: {{ADDRESS}}

## Start Here

1. Put bid documents in `bid-docs/`.
2. Run triage from the workspace root:

```bash
contractor-bid triage "{{PROJECT_NAME}}" --profile {{PROFILE_ID}} --render
```

3. Review:
   - `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals)
   - `bid-package-working/takeoff/review-pages.md`

4. Fill `bid-package-working/takeoff/scope-pages-sources.json`.
5. Run `contractor-bid build-packets "{{PROJECT_NAME}}"`.
6. Fill the takeoff JSON in `bid-package-working/takeoff/`.
7. Run `contractor-bid build-workbook "{{PROJECT_NAME}}" --profile {{PROFILE_ID}}`.
8. Run `contractor-bid check "{{PROJECT_NAME}}" --profile {{PROFILE_ID}}`.
9. Run `contractor-bid package-sendoff "{{PROJECT_NAME}}"` when the package is ready to share.

## Scope Rule

{{SCOPE_RULE}}

## Folder Map

- `bid-docs/` - source PDFs, addenda, bid forms, spreadsheets, and GC files.
- `bid-package-working/` - generated and edited package files.
- `bid-package-working/takeoff/` - JSON source of truth for page packets and BOM.
- `.agent/skills/` - generated model-readable scope skill for this project.
