#!/usr/bin/env bash
# =============================================================================
# run_all_judge.sh — 11 tasks × 3 judges one-command batch evaluation
#
# Usage:
#   bash scripts/run_all_judge.sh <candidates_root> [--dry-run] [--judges "j1 j2 j3"]
#
# Example:
#   bash scripts/run_all_judge.sh ./my_candidates
#   bash scripts/run_all_judge.sh ./my_candidates --dry-run
#   bash scripts/run_all_judge.sh ./my_candidates --judges "gpt-5-mini gemini-2.5-flash"
#
# Candidates directory layout (each task has a subdirectory of *.json files):
#
#   my_candidates/
#     amphibian_reptile_virome_2022/
#       agent1.json
#       agent2.json
#     arthropod_neg_sense_2015/
#       agent1.json
#       ...
#     ...all 11 task dirs...
#
# Each *.json file follows the AgentOutput schema:
#   {
#     "agent_id": "my-model",
#     "questions": [
#       {"rank": 1, "question": "...?"},
#       {"rank": 2, "question": "...?"},
#       ...up to 5 distinct questions...
#     ]
#   }
#
# Outputs land in:
#   batch_runs/<judge_id>/<task_name>/
#     summary.md, leaderboard.json, progress.json, results/<candidate>/...
#
# Requirements:
#   - .env with a valid NEWAPI_KEY
#   - pip install pyyaml python-dotenv openai  (or run scripts/run_batch_judge.sh first)
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# ---- defaults ---------------------------------------------------------------
DEFAULT_JUDGES="gpt-5.5-high gpt-5-mini gemini-2.5-flash"
TASKS=(
  amphibian_reptile_virome_2022
  arthropod_neg_sense_2015
  bat_btcn_virome_2024
  flavi_jingmen_jvi_2016
  invertebrate_rna_virosphere_2016
  oyster_rna_virome_2024
  rvmt_cell_2022
  tara_oceans_science_2022
  tick_metavirome_2023
  vertebrate_rna_viruses_2018
  zooplankton_rna_virosphere_2022
)

# ---- parse args -------------------------------------------------------------
CANDIDATES_ROOT=""
DRY_RUN=""
JUDGES="$DEFAULT_JUDGES"
CONCURRENCY=4
FORCE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)   DRY_RUN="--dry-run"; shift ;;
    --force)     FORCE="--force"; shift ;;
    --judges)    JUDGES="$2"; shift 2 ;;
    --concurrency) CONCURRENCY="$2"; shift 2 ;;
    -h|--help)
      head -35 "$0" | grep -E '^#' | sed 's/^# \?//'
      exit 0 ;;
    *)
      if [[ -z "$CANDIDATES_ROOT" ]]; then
        CANDIDATES_ROOT="$1"; shift
      else
        echo "ERROR: unexpected argument: $1" >&2; exit 1
      fi ;;
  esac
done

if [[ -z "$CANDIDATES_ROOT" ]]; then
  echo "Usage: bash scripts/run_all_judge.sh <candidates_root> [--dry-run] [--judges \"j1 j2 j3\"]"
  echo ""
  echo "candidates_root must contain subdirectories named after each task, e.g.:"
  echo "  candidates_root/invertebrate_rna_virosphere_2016/*.json"
  exit 1
fi

# ---- detect python ----------------------------------------------------------
if [[ -x "$ROOT/.venv/bin/python" ]]; then
  PY="$ROOT/.venv/bin/python"
elif command -v python3 &>/dev/null; then
  PY="python3"
elif [[ -x "$ROOT/.venv-win/Scripts/python.exe" ]]; then
  # Windows venv (only works on Windows)
  PY="$ROOT/.venv-win/Scripts/python.exe"
else
  echo "ERROR: no python found. Create a venv or install python3." >&2
  exit 1
fi

echo "============================================================"
echo " run_all_judge.sh"
echo " python:     $PY"
echo " candidates: $CANDIDATES_ROOT"
echo " judges:     $JUDGES"
echo " tasks:      ${#TASKS[@]}"
echo " dry-run:    ${DRY_RUN:-no}"
echo "============================================================"
echo ""

# ---- main loop --------------------------------------------------------------
TOTAL=0
PASS=0
FAIL=0
SKIP=0

for JUDGE in $JUDGES; do
  echo ""
  echo "================================================================"
  echo " JUDGE: $JUDGE"
  echo "================================================================"

  for TASK in "${TASKS[@]}"; do
    TOTAL=$((TOTAL + 1))

    DATA_DIR="$ROOT/data/$TASK/raw"
    GOLD="$ROOT/data/$TASK/gold_scientific_questions.json"
    CAND_DIR="$CANDIDATES_ROOT/$TASK"
    OUT_DIR="$ROOT/batch_runs/$JUDGE/$TASK"

    # validate inputs exist
    if [[ ! -d "$DATA_DIR" ]]; then
      echo "  SKIP $TASK: data/raw not found at $DATA_DIR"
      SKIP=$((SKIP + 1))
      continue
    fi
    if [[ ! -f "$GOLD" ]]; then
      echo "  SKIP $TASK: gold not found at $GOLD"
      SKIP=$((SKIP + 1))
      continue
    fi
    if [[ ! -d "$CAND_DIR" ]]; then
      echo "  SKIP $TASK: no candidates dir at $CAND_DIR"
      SKIP=$((SKIP + 1))
      continue
    fi
    CAND_COUNT=$(find "$CAND_DIR" -maxdepth 1 -name "*.json" | wc -l | tr -d ' ')
    if [[ "$CAND_COUNT" -eq 0 ]]; then
      echo "  SKIP $TASK: no *.json files in $CAND_DIR"
      SKIP=$((SKIP + 1))
      continue
    fi

    echo ""
    echo "  ── $TASK ($CAND_COUNT candidates) ──"
    if PYTHONUTF8=1 "$PY" -m eval.batch_judge \
        --data "$DATA_DIR" \
        --gold "$GOLD" \
        --candidates "$CAND_DIR" \
        --out "$OUT_DIR" \
        --judge "$JUDGE" \
        --concurrency "$CONCURRENCY" \
        --reuse-workspace \
        $DRY_RUN $FORCE 2>&1; then
      PASS=$((PASS + 1))
    else
      echo "  FAILED: $TASK with judge $JUDGE"
      FAIL=$((FAIL + 1))
    fi
  done
done

# ---- summary ----------------------------------------------------------------
echo ""
echo "============================================================"
echo " ALL DONE"
echo " total=$TOTAL  pass=$PASS  fail=$FAIL  skip=$SKIP"
echo " results in: $ROOT/batch_runs/<judge>/<task>/"
echo "============================================================"
