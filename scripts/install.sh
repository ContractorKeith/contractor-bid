#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${CONTRACTOR_BID_REPO_URL:-https://github.com/ContractorKeith/contractor-bid.git}"
APP_DIR="${CONTRACTOR_BID_HOME:-$HOME/.contractor-bid}"
SRC_DIR="$APP_DIR/src/contractor-bid"
VENV_DIR="$APP_DIR/venv"
BIN_DIR="${CONTRACTOR_BID_BIN:-$HOME/.local/bin}"
INSTALL_POPPLER=0

usage() {
  cat <<'EOF'
Usage: scripts/install.sh [--install-poppler] [--repo URL]

Installs contractor-bid into ~/.contractor-bid and writes a contractor-bid
launcher into ~/.local/bin.

Options:
  --install-poppler  Try to install Poppler with Homebrew (macOS) or apt (Linux).
  --repo URL         Override the Git repository URL.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --install-poppler)
      INSTALL_POPPLER=1
      shift
      ;;
    --repo)
      REPO_URL="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 2
      ;;
  esac
done

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

need_cmd python3
need_cmd git

PY_OK="$(python3 - <<'PY'
import sys
print("1" if sys.version_info >= (3, 11) else "0")
PY
)"
if [[ "$PY_OK" != "1" ]]; then
  echo "Python 3.11+ is required. Found: $(python3 --version)" >&2
  exit 1
fi

mkdir -p "$APP_DIR" "$BIN_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHECKOUT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
if [[ -f "$CHECKOUT_DIR/pyproject.toml" && -d "$CHECKOUT_DIR/src/contractor_bid" ]]; then
  SRC="$CHECKOUT_DIR"
else
  if [[ -d "$SRC_DIR/.git" ]]; then
    git -C "$SRC_DIR" pull --ff-only
  else
    mkdir -p "$(dirname "$SRC_DIR")"
    git clone "$REPO_URL" "$SRC_DIR"
  fi
  SRC="$SRC_DIR"
fi

python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install "$SRC"

cat > "$BIN_DIR/contractor-bid" <<EOF
#!/usr/bin/env bash
exec "$VENV_DIR/bin/contractor-bid" "\$@"
EOF
chmod +x "$BIN_DIR/contractor-bid"

if [[ "$INSTALL_POPPLER" == "1" ]] && ! command -v pdftotext >/dev/null 2>&1; then
  case "$(uname -s)" in
    Darwin)
      if command -v brew >/dev/null 2>&1; then
        brew install poppler
      else
        echo "Homebrew is not installed. Install Poppler manually: https://poppler.freedesktop.org/" >&2
      fi
      ;;
    Linux)
      if command -v apt-get >/dev/null 2>&1; then
        sudo apt-get update
        sudo apt-get install -y poppler-utils
      else
        echo "Install Poppler with your package manager, usually package: poppler-utils" >&2
      fi
      ;;
    *)
      echo "Install Poppler manually for rendered page images and best PDF text extraction." >&2
      ;;
  esac
fi

echo
echo "Installed contractor-bid."
echo "Launcher: $BIN_DIR/contractor-bid"
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
  echo "Add this to your shell profile if needed:"
  echo "  export PATH=\"$BIN_DIR:\$PATH\""
fi
echo
"$BIN_DIR/contractor-bid" doctor || true
