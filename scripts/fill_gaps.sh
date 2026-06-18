#!/bin/bash
# Fill remaining gaps: invertebrate, oyster, rvmt (+ flavi if needed)
set -e
cd "$(dirname "$0")/.."
LOG="eval-v1-fill.log"
echo "=== fill gaps start ===" > "$LOG"

for task in flavi_jingmen invertebrate oyster rvmt; do
  echo "[$(date +%H:%M:%S)] running $task ..." >> "$LOG"
  python3 -m eval.run_systematic \
    --judges gpt-5.5-high \
    --agents gemini-3.5-flash minimax-m3 qwen3.7-max gemini-3.1-pro \
    --tasks "$task" \
    --resume \
    >> "$LOG" 2>&1
  echo "[$(date +%H:%M:%S)] done $task" >> "$LOG"
done

echo "=== fill gaps ALL DONE ===" >> "$LOG"
