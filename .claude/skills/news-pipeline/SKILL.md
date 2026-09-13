---
name: news-pipeline
description: 完整每日 pipeline：抓新聞 → 日報 → wiki ingest → 讀者版 → 建置 web reader → 推送。說「跑今天的 pipeline」「補跑某日日報」時用。
argument-hint: [YYYY-MM-DD]
disable-model-invocation: true
---

# News Pipeline

## 怎麼用

`/news-pipeline` 跑今天，`/news-pipeline 2026-09-01` 補跑指定日。**要準備什麼：** 無，設定值由派工 prompt 自帶。**會被問什麼：** 完成摘要末尾的「📋 待使用者裁示」區會把當日待確認事項接出來等你回覆。**拿到什麼：** 當日日報、更新過的 wiki、讀者版日報、重建並推送的網站，加一份完成摘要。**成本：** 兩個 Sonnet 背景 agent（Phase A、Phase C）＋本 session 前景跑六記者 ingest。

TARGET_DATE 取 UTC 日期（`date -u +%F`）或 `$ARGUMENTS`。**判準：** 雲端 routine 用的就是 UTC，本機時區的「今天」會與雲端對不上（`docs/cloud-runbooks/daily.md`）。

三段的步驟語意不在本檔，見檔末規範對照表；兩段背景 agent 的派工 prompt 全文見 `.claude/skills/news-pipeline/references/dispatch.md`。

## Phase A：抓料與日報（Step 0 / 0b / 1a / 1b / 1c）

- **做什麼：** 抓當日新聞、寫 `news/TARGET_DATE.md` 日報並 commit
- **誰做：** 背景 agent（Agent tool，`model: sonnet`、`run_in_background: true`），完成後自動通知本 session
- **失敗怎麼辦：** Step 1a 失敗（agent 回報「Aggregator FAILED」）就停在 Phase A，本 session 依 `.claude/skills/web-publish/SKILL.md` Step 6 格式對 `src/logs/task_scheduler.log` append 一行 `Aggregator FAILED - stopping`，完成摘要把 Step 2 以後全標 ⏭️，結束

## Phase B：wiki ingest 與讀者版日報（Step 2 / 2b）

- **做什麼：** 依 `.claude/skills/wiki-ingest/SKILL.md` 分類 → 派六類記者 → 彙整 `wiki/feature-radar.md`／`wiki/index.md`／`wiki/log.md`；接著依 `.claude/skills/reader-digest/SKILL.md` 讀當日 wiki diff 寫 `daily/TARGET_DATE.md`
- **誰做：** Step 2 由本 session 前景執行，六記者以 foreground 派工；`/news-pipeline` 本身也在前景呼叫。巢狀背景下記者的完成通知會送到最上層 session，實證見沿革檔 `docs/rules-changelog/news-pipeline-steps.md` 2026-08-29
- **失敗怎麼辦：** Step 2 失敗記下結果（供 Step 6 log）仍進 Phase C，web build 不依賴 wiki；Step 2b 失敗不阻斷。Step 2b 排在 Step 2 之後、Step 3 之前——它吃的是尚未 commit 的 wiki 改動

## Phase C：收尾與發布（Step 3 / 4 / 5 / 6）

- **做什麼：** commit wiki、建置 web reader、單一 push、寫 `task_scheduler.log`
- **誰做：** 第二個背景 agent（同 Phase A 的設定）；Phase A／B 結果由本 session 填進派工 prompt 的「已知結果」欄，agent 不必重新查證
- **失敗怎麼辦：** Phase B 無論成敗都要進入本階段，Step 6 的 log 才寫得成。agent 回報後本 session 彙整三段結果輸出完成摘要（格式見 `.claude/skills/web-publish/SKILL.md`「完成摘要」），**必含「📋 待使用者裁示」區塊**，無未決項也寫「無」

## 規範對照表

| 順序 | 步驟 | 規範檔 |
|---|---|---|
| Phase A | Step 0 / 0b / 1a / 1c | `.claude/skills/news-gather/SKILL.md` |
| Phase A | Step 1b 生成日報 | `.claude/skills/news-digest/SKILL.md`（＋`.claude/skills/news-digest/references/format.md`、`.claude/skills/news-digest/references/selection.md`） |
| Phase B | Step 2 wiki ingest | `.claude/skills/wiki-ingest/SKILL.md` |
| Phase B | Step 2b 讀者版日報 | `.claude/skills/reader-digest/SKILL.md`（＋`.claude/skills/reader-digest/references/format.md`） |
| Phase C | Step 3 / 4 / 5 / 6 ＋完成摘要 | `.claude/skills/web-publish/SKILL.md` |

## 閘與退路

唯一的閘是 web build gate，住 `.claude/skills/web-publish/SKILL.md` Step 4：不過就不 build、不 push；Step 1a 失敗停在 Phase A；Step 2b 失敗不阻斷，照樣進 Phase C。
