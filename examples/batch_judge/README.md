# examples/batch_judge — 批量 judge-only 评测样例

演示 `eval/batch_judge.py`:对**多个候选科学问题文件**(不同 agent 或手工设计)做批量评测,
数据自动脱敏,**不调用任何 agent**。

## 目录内容

```
examples/batch_judge/
├── gold.json                 # gold 科学问题(2 条:1 primary + 1 secondary)
└── candidates/               # 每个 *.json 是一个候选集
    ├── agent-strong.json     # 5 条,贴近 gold —— 应得高分
    ├── agent-weak.json       # 5 条,跑偏(GC含量/最大文件…)—— 应得低分
    └── human-designed.json   # 仅 2 条、纯字符串写法 —— 演示宽松候选格式
```

## 跑(dry-run,不需要 key)

先用 `--dry-run` 验证脱敏 + 校验,不花 token:

```bash
PYTHONUTF8=1 .venv/Scripts/python.exe -m eval.batch_judge \
  --data data/rvmt_cell_2022 \
  --gold examples/batch_judge/gold.json \
  --candidates examples/batch_judge/candidates \
  --out batch_runs/example \
  --judge gpt-5.5-high \
  --dry-run
```

## 真正评测(需 `.env` 里有有效 NEWAPI_KEY)

去掉 `--dry-run` 即可。进度实时打印,并持续写入 `batch_runs/example/progress.json`;
结束后产出 `leaderboard.json` 与 `summary.md`。

```bash
PYTHONUTF8=1 .venv/Scripts/python.exe -m eval.batch_judge \
  --data data/rvmt_cell_2022 \
  --gold examples/batch_judge/gold.json \
  --candidates examples/batch_judge/candidates \
  --out batch_runs/example \
  --judge gpt-5.5-high --concurrency 4
```

## 候选文件格式

AgentOutput 形状,1..5 条问题,`question` 必须以 `?` 结尾:

```json
{
  "agent_id": "my-agent",
  "questions": [
    {"rank": 1, "question": "...?"},
    {"rank": 2, "question": "...?"}
  ]
}
```

- `rank` 缺省时按出现顺序自动编号。
- `questions` 也可写成纯字符串数组:`["...?", "...?"]`。
- 加 `--strict` 则强制 5 条互异、rank 1..5(完整 Pass@5 契约)。
