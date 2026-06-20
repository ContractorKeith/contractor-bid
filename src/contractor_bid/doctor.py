from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from dataclasses import dataclass


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    required: bool = True


def command_version(command: str, args: list[str] | None = None) -> str:
    if not shutil.which(command):
        return "not found"
    try:
        proc = subprocess.run(
            [command] + (args or ["--version"]),
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=5,
        )
    except Exception as exc:
        return f"found, but version check failed: {exc}"
    first = (proc.stdout or "").strip().splitlines()
    return first[0] if first else "found"


def module_check(module: str, package_hint: str) -> Check:
    found = importlib.util.find_spec(module) is not None
    return Check(
        name=f"Python module: {module}",
        ok=found,
        detail="installed" if found else f"missing; install with `pip install {package_hint}`",
    )


def run_doctor() -> tuple[list[Check], int]:
    checks: list[Check] = []
    py_ok = sys.version_info >= (3, 11)
    checks.append(
        Check(
            name="Python",
            ok=py_ok,
            detail=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}; requires 3.11+",
        )
    )
    checks.append(module_check("openpyxl", "openpyxl"))
    checks.append(module_check("pypdf", "pypdf"))

    for command in ("pdfinfo", "pdftotext"):
        checks.append(
            Check(
                name=f"Poppler command: {command}",
                ok=shutil.which(command) is not None,
                detail=command_version(command, ["-v"]),
                required=False,
            )
        )
    checks.append(
        Check(
            name="Poppler command: pdftoppm",
            ok=shutil.which("pdftoppm") is not None,
            detail=command_version("pdftoppm", ["-v"]),
            required=False,
        )
    )
    checks.append(
        Check(
            name="git",
            ok=shutil.which("git") is not None,
            detail=command_version("git", ["--version"]),
            required=False,
        )
    )

    hard_fail = any(check.required and not check.ok for check in checks)
    return checks, 1 if hard_fail else 0


def format_doctor(checks: list[Check]) -> str:
    lines = ["contractor-bid environment check", ""]
    for check in checks:
        mark = "OK" if check.ok else ("MISSING" if check.required else "OPTIONAL")
        lines.append(f"[{mark}] {check.name}: {check.detail}")
    lines += [
        "",
        "Notes:",
        "- Poppler is recommended for fast PDF text extraction and page-image rendering.",
        "- Without Poppler, PDF page counts/text can fall back to pypdf, but rendered page images are unavailable.",
        "- No GitHub CLI is required for normal users.",
    ]
    return "\n".join(lines)
