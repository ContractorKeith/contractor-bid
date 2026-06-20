param(
  [string]$Repo = "https://github.com/ContractorKeith/contractor-bid.git",
  [switch]$InstallPoppler
)

$ErrorActionPreference = "Stop"

$HomeDir = $env:USERPROFILE
$AppDir = if ($env:CONTRACTOR_BID_HOME) { $env:CONTRACTOR_BID_HOME } else { Join-Path $HomeDir ".contractor-bid" }
$SrcDir = Join-Path $AppDir "src\contractor-bid"
$VenvDir = Join-Path $AppDir "venv"
$BinDir = if ($env:CONTRACTOR_BID_BIN) { $env:CONTRACTOR_BID_BIN } else { Join-Path $HomeDir ".local\bin" }

function Find-Python {
  $commands = @("py", "python3", "python")
  foreach ($cmd in $commands) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
      if ($cmd -eq "py") {
        return @("py", "-3")
      }
      return @($cmd)
    }
  }
  throw "Python 3.11+ is required."
}

$Python = Find-Python
$PythonArgs = @($Python | Select-Object -Skip 1)
$VersionCheck = & $Python[0] @PythonArgs -c "import sys; print('1' if sys.version_info >= (3, 11) else '0')"
if ($VersionCheck -ne "1") {
  throw "Python 3.11+ is required."
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "Git is required. Install it from https://git-scm.com/download/win"
}

New-Item -ItemType Directory -Force -Path $AppDir, $BinDir | Out-Null

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$CheckoutDir = Resolve-Path (Join-Path $ScriptDir "..")
if ((Test-Path (Join-Path $CheckoutDir "pyproject.toml")) -and (Test-Path (Join-Path $CheckoutDir "src\contractor_bid"))) {
  $Src = $CheckoutDir
} else {
  if (Test-Path (Join-Path $SrcDir ".git")) {
    git -C $SrcDir pull --ff-only
  } else {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $SrcDir) | Out-Null
    git clone $Repo $SrcDir
  }
  $Src = $SrcDir
}

& $Python[0] @PythonArgs -m venv $VenvDir
$VenvPython = Join-Path $VenvDir "Scripts\python.exe"
& $VenvPython -m pip install --upgrade pip
& $VenvPython -m pip install $Src

$CmdPath = Join-Path $BinDir "contractor-bid.cmd"
Set-Content -Path $CmdPath -Value "@echo off`r`n`"$VenvDir\Scripts\contractor-bid.exe`" %*`r`n"

if ($InstallPoppler -and -not (Get-Command pdftotext -ErrorAction SilentlyContinue)) {
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    winget install --id oschwartz10612.Poppler -e
  } elseif (Get-Command choco -ErrorAction SilentlyContinue) {
    choco install poppler -y
  } else {
    Write-Host "Install Poppler manually for PDF page images and best text extraction."
  }
}

Write-Host ""
Write-Host "Installed contractor-bid."
Write-Host "Launcher: $CmdPath"
Write-Host "Add this folder to PATH if needed: $BinDir"
Write-Host ""
& $CmdPath doctor
