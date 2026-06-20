# Claude / Model Workflow

When the user says "start a new bid project for [scope]", do this:

1. Identify or create the scope profile with `contractor-bid init`.
2. Create the bid folder with `contractor-bid new`.
3. Ask the user to place bid documents in `bid-docs/` if the folder is empty.
4. Run triage when PDFs exist.
5. Fill `scope-pages-sources.json` from reviewed source pages.
6. Build packets and workbook.
7. Write/update the reference index and proposal letter.
8. Run `contractor-bid check` and resolve alerts before packaging.
9. Record corrections with `contractor-bid learn`.

The model should not invent final quantities from PDF text hits. Text hits are triage evidence only; quantities require source-backed measurement or a stated manual placeholder.
