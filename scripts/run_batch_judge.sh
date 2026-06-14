#!/usr/bin/env bash
# Bootstrap + smoke-test the only-Question batch judge (Linux / macOS).
#
# What it does:
#   1. Creates .venv (if missing) and installs the slim headless deps.
#   2. Copies .env.example -> .env (if missing) and reminds you to set the key.
#   3. Runs a no-token DRY-RUN against the bundled examples/batch_judge sample,
#      proving desensitization + validation + the import chain all work.
#   4. Prints the real-run command template.
#
# Run from the repository root:
#   bash scripts/run_batch_judge.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

VENV="$ROOT/.venv"
PY="$VENV/bin/python"

# 1. venv + deps -------------------------------------------------------------
if [ ! -x "$PY" ]; then
  echo "[1/4] creating venv at .venv ..."
  python3 -m venv "$VENV"
else
  echo "[1/4] reusing existing venv at .venv"
fi
echo "      installing eval/requirements-batch.txt ..."
"$PY" -m pip install --quiet --upgrade pip
"$PY" -m pip install --quiet -r "$ROOT/eval/requirements-batch.txt"

# 2. .env --------------------------------------------------------------------
if [ ! -f "$ROOT/.env" ]; then
  cp "$ROOT/.env.example" "$ROOT/.env"
  echo "[2/4] created .env from .env.example — EDIT it and set NEWAPI_KEY before a real run."
else
  echo "[2/4] .env already present"
fi

# 3. dry-run smoke test (no token needed) ------------------------------------
echo "[3/4] dry-run smoke test on examples/batch_judge ..."
PYTHONUTF8=1 "$PY" -m eval.batch_judge \
  --data       "$ROOT/examples/batch_judge/sample_data" \
  --gold       "$ROOT/examples/batch_judge/gold.json" \
  --candidates "$ROOT/examples/batch_judge/candidates" \
  --out        "$ROOT/batch_runs/_smoke" \
  --judge      gpt-5.5-high \
  --dry-run

# 4. next step ---------------------------------------------------------------
cat <<'EOF'

[4/4] ✅ environment ready. To run a REAL evaluation on your own inputs:

  PYTHONUTF8=1 .venv/bin/python -m eval.batch_judge \
      --data        <your_data_dir_or.zip> \
      --gold        <your_gold.json> \
      --candidates  <your_candidates_dir/> \
      --out         batch_runs/<run_name> \
      --judge       gpt-5.5-high \
      --concurrency 4

Outputs land in batch_runs/<run_name>/: summary.md, leaderboard.json, progress.json.
See BATCH_JUDGE.md for input formats and options.
EOF
