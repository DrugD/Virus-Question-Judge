# results_archive — 历史评测结果归档 / Archived evaluation results

> 本目录收纳 **v0.3.0 之前** 产生的所有评测结果。归档原因：v0.3.0 改了 Pass@5 算法
> （位置加权 → 计数式）、收紧了 data_grounding 评分、并把默认 judge 固定为 Claude Opus 4.7。
> 旧结果与新算法不可直接比较，故单独存档，并**按评测所用的 LLM Judge 分目录标注**。

每个子目录对应一个 judge（或一类来源）：

| 目录 | LLM Judge | 内容 | 备注 |
|---|---|---|---|
| `judge-gpt-5.1/` | **GPT-5.1** (provider openai) | 顶层旧 `results/`（claude-code / codex-cli / qwen3.6-plus / 烟测） | 含 `judge_scores.json`（judge_model=gpt-5.1） |
| `judge-gpt-5-mini/` | **GPT-5 mini** | `STATS_eval-v1_judge-gpt-5-mini.{md,xlsx}` + eval-v1 跑批 | 题集 `eval-v1-invertebrate_rna_virosphere_2016` 的 gpt-5-mini 评测 |
| `judge-gemini-2.5-flash/` | **Gemini 2.5 Flash** | `STATS_eval-v1_judge-gemini-2.5-flash.{md,xlsx}` + eval-v1 跑批 | 同题集的 gemini-2.5-flash 评测 |
| `aggregate-multi-judge/` | 多 judge 汇总 | `STATS.md`、`STATS_eval_v1.xlsx`、`STATS_matrix.xlsx` | 跨 judge / 跨题集的合并矩阵，非单一 judge |
| `judge-unjudged-agent-outputs/` | **（未评测）** | 20 个 `upl_*` 上传跑批，仅含 agent 报告 + transcript | 这些 run 只跑了 agent，从未经过 judge 打分 |

## 旧版 Pass@5 算法（仅适用于本归档内的分数）

本目录内任何"Pass@5"均为**位置加权**口径：
通过 rank `i` 记 `(1 + w_i)`，`w = (5,4,3,2,1)`，分子除以 20。
例：仅 rank-1 过 = 30%，rank 1+2 = 55%，全过 = 100%。

v0.3.0 起改为**计数式**：每通过 1 条 +0.2（`pass_count / 5`），与排名无关。
新旧分数不可混用比较。
</content>
