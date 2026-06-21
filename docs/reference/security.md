# Security

`contractor-bid` is a local-first CLI and optional stdio MCP server. It does not run a hosted
service, collect credentials, or send bid documents to ContractorKeith.

See the repository security policy:

- [SECURITY.md](https://github.com/ContractorKeith/contractor-bid/blob/main/SECURITY.md)

## Data Safety

Do not commit:

- proprietary bid documents
- supplier quotes
- private estimates
- customer files
- real bid tracker data
- local correction logs
- generated sendoff packages

The repo `.gitignore` excludes the common generated and local data paths, including:

- `**/bid-docs/`
- `**/bid-package-working/page-images/`
- `**/bid-package-working/text-extracts/`
- `**/bid-package-working/*.pdf`
- `**/bid-package-working/*.xlsx`
- `.contractor-bid/bid-tracker.json`
- `Bid-Tracker.xlsx`

## Agent And MCP Safety

The MCP server is intended for trusted local agent clients over stdio. Do not expose it as a
public network service.

Tracker write tools require explicit confirmation in the MCP layer. Agents should preserve
that same confirmation rule when driving CLI tracker commands.
