# Virus-Question-Judge

Rubric-based DeepEval judge for the **Life_Virus_001** task: an autonomous research agent reads an anonymized blind subset of a petabase-scale public-sequencing RdRP search and proposes the single most important scientific question the dataset can answer. The judge LLM scores the agent's top-1 question against a 6-dimension weighted rubric.

```
agent (Qwen3.6-Plus | Codex CLI | Claude Code | …)
        │  reads
        ▼
   sandbox copy of  INSTRUCTIONS.md, checklist.json, info.json, data/raw_data/
        │  writes
        ▼
   agent_questions.json  +  report/report.md
        │
        ▼
   DeepEval custom metrics (one per rubric dimension, weighted composite)
        │  reads judge-only target_study/question_rubric.json
        ▼
   judge_scores.json
```

## 版本更新记录 / Changelog

> 远程仓库：<https://github.com/DrugD/Virus-Question-Judge>（账号 `likun9876543210@163.com`）。
> 后续改动统一同步到 **`sync-test`** 分支。

### v0.3.0 — 2026-06-02

- **数据脱敏（文件名为主）.** 上传数据进入 workspace 时被拍平并重命名为 `1.csv`、`2.json`、`3.tsv` …（只保留扩展名，丢弃目录名），原名映射写入 judge-only 的 `workspace/filename_map.json`。这样 agent 无法仅靠引用 `43059586_RdRp_motif_collection.xlsx` 之类的“暗示性文件名”白拿 data_grounding 分。详见 `webapp/pipeline_runner.py::_desensitize_data`。
- **data_grounding 评分收紧.** 仅引用文件名/变量名/accession/figure 标签视为表层引用，**不再**给高分；高分要求从数据中真正推导出统计量、分布或关系。锚点与定义见 `eval/metrics/gold_rubric_metric.py`（UI 与 judge prompt 同步）。
- **数据有效性检查.** 上传校验新增有效性检查：空文件、只有表头无数据行的表格、空 FASTA、无法解析的 JSON 会被标记为 warning，并在 `valid_file_count` 汇总；若全部文件无效则直接拒绝（`webapp/validator.py`）。
- **Pass@5 改为计数式.** 5 条候选每通过 1 条记 **+0.2**（`pass_count / 5`），与排名无关：全对 = 1.0，全错 = 0.0。取代原“位置加权 / 20”算法。涉及 `webapp/pipeline_runner.py`、`eval/rejudge.py` 及所有 agent/UI 文案。
- **不再持久化 sandbox 数据.** 每次 run 结束后自动删除 `webapp_runs/.../sandboxes/<agent>/<ts>/data/`（成功与失败路径都清理），仅保留 agent 输出与 `_debug/`。一次性清理了历史遗留的 ~1.5 GB 拷贝，并在 `.gitignore` 中排除该路径。
- **judge model 默认最强模型.** 默认 judge 固定为 **Claude Opus 4.7**（`eval/config.yaml`，当前最强档；后续可扩展为最强 n 个 LLM 的集成评审）。

## Layout

```
病毒-Question-Judge/
├── INSTRUCTIONS.md            # agent prompt (mandates the two output files)
├── checklist.json             # 6-dim rubric, agent-visible
├── info.json                  # task spec + agent_output_schema
├── files.json                 # workspace tree manifest
├── data/raw_data/             # blind-data (32 runs / 53 fragments)
├── target_study/              # JUDGE-ONLY: groundtruth + flags + anchors
│   ├── checklist.json         # byte-equal copy of root checklist.json
│   ├── question_rubric.json   # GQ_001..008 + 8 refusal flags + 10 calib anchors
│   └── README.md
├── eval/                      # DeepEval pipeline
│   ├── config.yaml            # judge LLM provider + threshold
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── run_judge.py           # score one agent-run dir
│   ├── run_pipeline.py        # end-to-end multi-agent + leaderboard
│   ├── metrics/
│   │   ├── judge_llm.py
│   │   ├── rubric_dimension_metric.py
│   │   └── rubric_composite_metric.py
│   ├── agents/
│   │   ├── base.py
│   │   ├── qwen_agent.py
│   │   ├── codex_cli_agent.py
│   │   └── claude_code_agent.py
│   └── utils/{workspace.py, schemas.py}
└── results/{agent}/{run_id}/{agent_questions.json, report/report.md, judge_scores.json}
```

## Why DeepEval + custom Metric (and not exact-match / single GEval)

- **Per-dimension transparency.** Every rubric row in `checklist.json` becomes one `RubricDimensionMetric`. The judge LLM is asked one focused question per call (which 0–5 anchor matches the candidate?), so we get six independent reasoning traces instead of one opaque "good/bad" verdict.
- **Weighted aggregation with refusal caps.** `RubricCompositeMetric` weight-averages the six dimensions, then applies caps from `target_study/question_rubric.json#refusal_flags` (e.g. forbidden-entity leak caps `question_matching` at 1; missing top question zeroes everything). Exact-match would miss all of this.
- **Calibration anchors.** `target_study/question_rubric.json#calibration_anchors` ships 10 worked examples (perfect / strong / generic / wrong-direction / unrelated / …) so the judge LLM is anchored to consistent score floors and ceilings instead of drifting.
- **Pluggable judge.** `JudgeLLM` speaks OpenAI, DashScope/Qwen (OpenAI-compatible), and Anthropic, so the same metric stack runs against GPT-5, Claude Opus 4.7, or Qwen3.6-Plus without code changes.

## Quickstart

```bash
# 1. install
cd eval
pip install -r requirements.txt

# 2. set credentials (only the ones you intend to use)
export OPENAI_API_KEY=...           # judge default in config.yaml
export DASHSCOPE_API_KEY=...        # for Qwen3.6-Plus agent
export ANTHROPIC_API_KEY=...        # only if Claude Code uses an API key

# 3. end-to-end: run all three agents, judge, leaderboard
cd ..
python -m eval.run_pipeline \
  --workspace . \
  --agents qwen3.6-plus codex-cli claude-code \
  --judge-config eval/config.yaml

# 4. judge an existing agent-run dir
python -m eval.run_judge \
  --workspace . \
  --agent-output results/qwen3.6-plus/20260516T101010 \
  --judge-config eval/config.yaml
```

## Adding a new agent

1. Subclass `eval.agents.base.AgentRunner`, set `agent_id`, implement `_invoke(self, sandbox)`.
2. Register it in `eval/agents/__init__.py::REGISTRY`.
3. Pass `--agents <your_id>` to `run_pipeline.py`.

The base class handles sandbox creation (only agent-visible files copied — `target_study/` is never exposed), output validation against `info.json#/agent_output_schema`, and timing.

## Output

`results/{agent}/{run_id}/judge_scores.json`:

```jsonc
{
  "composite_score": 0.78,            // 0..1 weighted average (after caps)
  "composite_score_raw": 3.9,         // 0..5 weighted average
  "passed": true,                     // composite_score >= threshold
  "threshold": 0.6,
  "refusal_triggered": false,
  "flags_hit": [],
  "dimensions": [
    {
      "id": "question_matching",
      "weight": 0.4,
      "raw_score": 4,
      "normalized": 0.8,
      "capped_raw": 4,
      "capped_normalized": 0.8,
      "flags": [],
      "reasoning": "Hits archive-scale + RdRP + ref-DB gap; misses 'petabase' wording."
    },
    /* novelty, importance, testability, data_support, specificity */
  ],
  "candidate": { /* the agent's top question */ },
  "agent_id": "qwen3.6-plus",
  "judge_model": "claude-opus-4-7",
  "judge_provider": "openai"
}
```
