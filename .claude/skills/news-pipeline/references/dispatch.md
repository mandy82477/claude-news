# /news-pipeline 兩段背景 agent 的派工 prompt

`.claude/skills/news-pipeline/SKILL.md` 的 Phase A 與 Phase C 各派一個背景 agent，prompt 全文在此。兩段共用下列設定，派工時把三行逐字貼進 prompt 的「設定」欄。

## 設定

- REPO_ROOT   = 本repo根目錄
- PYTHON      = python
- TARGET_DATE = 今日的 UTC 日期或 `$ARGUMENTS`，格式 YYYY-MM-DD

REPO_ROOT 由 Bash `git rev-parse --show-toplevel` 取；PYTHON 即 PATH 上的 `python`；TARGET_DATE 由 `date -u +%F` 取。

## Phase A 步驟：背景 agent 執行 Step 0 + 1a + 1b

使用 **Agent tool**：

| 參數 | 值 |
|------|---|
| description | `News pipeline Phase A {TARGET_DATE}` |
| run_in_background | `true` |
| model | `sonnet` |

**prompt**（`{TARGET_DATE}` 替換為實際日期）：

```text
你是 Claude News Pipeline Agent（Phase A）。

設定：照 .claude/skills/news-pipeline/references/dispatch.md「設定」節的三行，其中 TARGET_DATE = {TARGET_DATE}。

讀取 `.claude/skills/news-gather/SKILL.md`（Step 0、Step 0b、Step 1a、Step 1c）與 `.claude/skills/news-digest/SKILL.md`（Step 1b，另讀 `.claude/skills/news-digest/references/format.md` 與 `.claude/skills/news-digest/references/selection.md`），依序執行 Step 0 → 0b → 1a → 1b → 1c，只做這五步，也不呼叫 Agent tool 派工任何 sub-agent。完成後回報 Step 0/1a/1b 各自結果；**若本次走了 archive replay 路徑（`cp src/gathered_archive/<date>.json`）而非現抓，回報中必須明講**（Step 5 的「replay 路徑收尾」是條件式規則，而執行它的 Phase C 看不到 Phase A 的過程）。若 Step 1a 失敗，立即停止並明確標註「Aggregator FAILED」。使用繁體中文輸出。
```

Phase A agent 完成後自動通知呼叫的 session。

## Phase C 步驟：備用 agent 執行 Step 3–6

**2026-09-24 起 Phase C 預設由本 session 直接執行**（`.claude/skills/news-pipeline/SKILL.md` Phase C），本節只在本 session 額度耗盡或環境不允許時才用。Phase B 結束後（成敗皆進入本階段，Step 6 的 log 才寫得成）spawn 第二個背景 agent：

| 參數 | 值 |
|------|---|
| description | `News pipeline Phase C {TARGET_DATE}` |
| run_in_background | `true` |
| model | `sonnet` |

**prompt**（`{PHASE_A_RESULT}`／`{PHASE_B_RESULT}` 替換為本 session 已知的 Phase A、Phase B 結果摘要）：

```text
你是 Claude News Pipeline Agent（Phase C）。

設定：照 .claude/skills/news-pipeline/references/dispatch.md「設定」節的三行，其中 TARGET_DATE = {TARGET_DATE}。

已知結果（供 Step 6 log 寫入使用，不必重新查證）：
- Phase A（Step 0/1a/1b）：{PHASE_A_RESULT}
- Phase B（Step 2 wiki ingest）：{PHASE_B_RESULT}

讀取 `.claude/skills/web-publish/SKILL.md`，執行 Step 3、Step 4、Step 5、Step 6，也不呼叫 Agent tool 派工任何 sub-agent。Step 6 log 需整合上述已知結果與本階段（Step 3/4/5）實際結果。使用繁體中文輸出。
```

Phase C agent 完成後自動通知呼叫的 session，由該 session 彙整 Phase A + B + C 結果輸出完成摘要。
