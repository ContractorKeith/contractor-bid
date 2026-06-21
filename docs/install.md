# Install

## Requirements

Required:

- Python 3.11 or newer
- Git
- `pipx`, recommended for isolated CLI installs

Installed as Python package dependencies:

- `openpyxl`, for Excel workbooks
- `pypdf`, for PDF packet generation and PDF parsing fallback

Recommended system dependency:

- Poppler: `pdfinfo`, `pdftotext`, and `pdftoppm`

Poppler gives faster PDF extraction and candidate page image rendering. Without Poppler, some
PDF operations can fall back to `pypdf`, but page images are unavailable.

## Install With pipx

Install the CLI:

```bash
pipx install contractor-bid
```

Install the CLI plus the optional MCP server for agent integrations:

```bash
pipx install "contractor-bid[mcp]"
```

Check the install:

```bash
contractor-bid doctor
```

## Install From A Source Checkout

macOS or Linux:

```bash
git clone https://github.com/ContractorKeith/contractor-bid.git
cd contractor-bid
scripts/install.sh --install-poppler
```

Windows PowerShell:

```powershell
git clone https://github.com/ContractorKeith/contractor-bid.git
cd contractor-bid
.\scripts\install.ps1 -InstallPoppler
```

## Development Install

From a cloned repo:

```bash
python3 -m pip install -e ".[mcp]"
contractor-bid doctor
```

For docs work:

```bash
python3 -m pip install -e ".[docs]"
mkdocs serve
```
