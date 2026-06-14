<#
.SYNOPSIS
  Bootstrap + smoke-test the only-Question batch judge (Windows / PowerShell).

.DESCRIPTION
  1. Creates .venv (if missing) and installs the slim headless deps.
  2. Copies .env.example -> .env (if missing) and reminds you to set the key.
  3. Runs a no-token DRY-RUN against the bundled examples/batch_judge sample,
     proving desensitization + validation + the import chain all work.
  4. Prints the real-run command template.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File scripts\run_batch_judge.ps1
#>
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$Venv = Join-Path $Root ".venv"
$Py   = Join-Path $Venv "Scripts\python.exe"

# 1. venv + deps -------------------------------------------------------------
if (-not (Test-Path $Py)) {
  Write-Host "[1/4] creating venv at .venv ..."
  python -m venv $Venv
} else {
  Write-Host "[1/4] reusing existing venv at .venv"
}
Write-Host "      installing eval/requirements-batch.txt ..."
& $Py -m pip install --quiet --upgrade pip
& $Py -m pip install --quiet -r (Join-Path $Root "eval\requirements-batch.txt")

# 2. .env --------------------------------------------------------------------
$EnvFile = Join-Path $Root ".env"
if (-not (Test-Path $EnvFile)) {
  Copy-Item (Join-Path $Root ".env.example") $EnvFile
  Write-Host "[2/4] created .env from .env.example - EDIT it and set NEWAPI_KEY before a real run."
} else {
  Write-Host "[2/4] .env already present"
}

# 3. dry-run smoke test (no token needed) ------------------------------------
Write-Host "[3/4] dry-run smoke test on examples/batch_judge ..."
$env:PYTHONUTF8 = "1"
& $Py -m eval.batch_judge `
  --data       (Join-Path $Root "examples\batch_judge\sample_data") `
  --gold       (Join-Path $Root "examples\batch_judge\gold.json") `
  --candidates (Join-Path $Root "examples\batch_judge\candidates") `
  --out        (Join-Path $Root "batch_runs\_smoke") `
  --judge      gpt-5.5-high `
  --dry-run

# 4. next step ---------------------------------------------------------------
Write-Host @"

[4/4] OK - environment ready. To run a REAL evaluation on your own inputs:

  `$env:PYTHONUTF8 = "1"
  .venv\Scripts\python.exe -m eval.batch_judge ``
      --data        <your_data_dir_or.zip> ``
      --gold        <your_gold.json> ``
      --candidates  <your_candidates_dir\> ``
      --out         batch_runs\<run_name> ``
      --judge       gpt-5.5-high ``
      --concurrency 4

Outputs land in batch_runs\<run_name>\: summary.md, leaderboard.json, progress.json.
See BATCH_JUDGE.md for input formats and options.
"@
