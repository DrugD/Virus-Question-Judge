# Batch Judge — only-Question 批量评测（可分发 CLI）

把**多个候选科学问题文件**（不同 agent，或人工设计）一次性对一份 **gold 评测标准**打分，**不调用任何 agent**。这是网页端「CANDIDATE · 判官直评」的批量 / headless 版本，适合发给别人独立跑。

数据会**自动脱敏**（目录拍平、文件统一改名为 `1.ext / 2.ext …`、嵌套压缩包递归展开、`filename_map.json` 仅判官可见），所以候选**无法靠引用 `43059586_RdRp_motif_collection.xlsx` 这类含义文件名来骗分** —— 与网页端走的是同一套脱敏代码。

---

## 你需要准备的 3 类输入

| 输入 | 形态 | 说明 |
|------|------|------|
| **data** | 一个目录 或 一个 `.zip` | 研究数据。脱敏后才喂给判官（**必需**，本工具不支持无 data 评测）。 |
| **gold** | 一个 `.json` | 你标注的 gold 科学问题（评分标准）。 |
| **candidates** | 一个目录下的若干 `*.json`，或若干显式 `.json` | 每个文件 = 一个候选集（一个 agent 的产出）。 |

### 候选 JSON 格式（AgentOutput 形状）
```json
{
  "agent_id": "claude-opus-4-7",
  "questions": [
    { "rank": 1, "question": "Does X drive Y in this dataset?" },
    { "rank": 2, "question": "..." }
  ]
}
```
- 1..5 条；`question` 必须以 `?` 结尾；`rank` 缺省时按出现顺序自动编号。
- `questions` 也可写成纯字符串数组：`["...?", "...?"]`（方便人工设计）。
- 加 `--strict` 则强制 **5 条互异、rank 1..5**（完整 Pass@5 契约）。

---

## 快速开始（一键 bootstrap）

从仓库根目录运行。脚本会建 venv、装精简依赖、生成 `.env`，并对自带样例跑一次 **dry-run 冒烟**（不花 token）。

**Windows（PowerShell）**
```powershell
powershell -ExecutionPolicy Bypass -File scripts\run_batch_judge.ps1
```

**Linux / macOS**
```bash
bash scripts/run_batch_judge.sh
```

依赖很轻（`eval/requirements-batch.txt`：pydantic / pyyaml / python-dotenv / openai / anthropic）——**不含 deepeval / fastapi**，纯批量评测用不到。

---

## 手动安装（不用脚本）
```bash
python -m venv .venv
# Windows: .venv\Scripts\python.exe   *nix: .venv/bin/python
.venv/bin/python -m pip install -r eval/requirements-batch.txt
cp .env.example .env          # 然后编辑，把 NEWAPI_KEY 换成真实 key
```

---

## 先 dry-run（不需要 key）
先验证脱敏 + 校验链路，**不花 token**：
```bash
PYTHONUTF8=1 .venv/bin/python -m eval.batch_judge \
  --data       examples/batch_judge/sample_data \
  --gold       examples/batch_judge/gold.json \
  --candidates examples/batch_judge/candidates \
  --out        batch_runs/_smoke \
  --judge      gpt-5.5-high \
  --dry-run
```
应看到：脱敏后文件名变为 `1.ext / 2.ext …`、`filename_map.json` 写在 workspace 根（判官可见，**不在** `raw_no_name/` 里）、所有候选校验通过、判官未被调用。

## 真正评测（需 `.env` 里有有效 `NEWAPI_KEY`）
```bash
PYTHONUTF8=1 .venv/bin/python -m eval.batch_judge \
  --data        <你的data目录或.zip> \
  --gold        <你的gold.json> \
  --candidates  <你的candidates目录/> \
  --out         batch_runs/<run_name> \
  --judge       gpt-5.5-high \
  --concurrency 4
```

---

## 产出（在 `--out` 目录下）
| 文件 | 内容 |
|------|------|
| `summary.md` | 排行榜表格（avg_composite / best / pass@1 / pass@5 / pass_count / 命中 gold），人读首选。 |
| `leaderboard.json` | 完整结构化排名，给程序消费。 |
| `progress.json` | 每评完一个候选就重写一次；从别的进程 tail / 轮询它即可做实时面板。 |
| `results/<candidate>/<ts>/` | 每个候选的逐条评分明细（`judge_scores.json` + `judge_scores_all_candidates.json`）。 |

---

## 常用选项
| 选项 | 作用 |
|------|------|
| `--dry-run` | 只脱敏+校验，不调判官（不花 token）。 |
| `--strict` | 强制 5 条互异、rank 1..5。 |
| `--concurrency N` | 判官并发数（默认 4）。 |
| `--spacing S` | 每次判官调用后 sleep S 秒（限速）。 |
| `--reuse-workspace` | 复用已脱敏的 `<out>/workspace`，不重建。 |
| `--force` | 重评已完成的候选（默认会跳过，支持断点续跑）。 |
| `--threshold T` | pass 阈值（默认取 `eval/config.yaml` 的 0.6）。 |

---

## 常见问题
- **`NEWAPI_KEY is a placeholder`**：`.env` 还是占位值。dry-run 不受影响；真跑前请填真实 key。
- **断点续跑**：再跑同一 `--out` 会自动跳过已产出 `judge_scores.json` 的候选；要重评加 `--force`。
- **脱敏能关吗**：不能，且不应关 —— 关了候选就能靠文件名骗分。
- 更小的样例与 candidate 写法参见 [`examples/batch_judge/`](examples/batch_judge/)。
