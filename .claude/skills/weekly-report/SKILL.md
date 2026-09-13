---
name: weekly-report
description: 產生本週深度週報（頭條敘事＋技術討論深挖＋下週看什麼＋檔尾數字），輸出 weekly/YYYY-Wnn.md。週報本體，通常由 /weekly 代為呼叫。
---

# Weekly Report — 週報產生

> **這是週報本體，不是每週的入口。** 平常跑 `/weekly`（總指揮，會依序帶起本 skill 與 `.claude/skills/wiki-weekly-review/SKILL.md`）；單獨執行只在補跑或修正單一期週報時使用。
> 單獨執行時，收尾（步驟 6）由本 skill 自己負責；由 `/weekly` 帶起時，**步驟 6 一律跳過**，收尾交給總指揮統一做（單一 push，理由見該檔）。

「當週技術新聞的教學式深挖」專欄。題目跟新聞走（本週最有料的技術題），寫法是教學的（基礎快講＋進階深挖混合深度），**不是預排課綱**。

**讀者：** 使用者自己＋會分享給別人（冷讀者要能讀懂，基礎概念不可跳過）。
**全文 5 分鐘讀完。**

**使用方式：** `/weekly-report` 產生本週（今日所在 ISO 週）；`/weekly-report 2026-W30` 指定週次（用於補跑或修正），週次即 `$ARGUMENTS`。

四份參考檔，正文不重述——**寫該段之前逐字讀對應那份**：

| 參考檔 | 內容 |
|---|---|
| `.claude/skills/weekly-report/references/contracts.md` | 機械契約字串表（script 會 grep 的字串只住那裡） |
| `.claude/skills/weekly-report/references/headline.md` | 第 (1) 段：頭條標題三判準、必附行動、十條規則、冷讀者三問 |
| `.claude/skills/weekly-report/references/deepdive.md` | 第 (2) 段：選題三判準、寫作方向三件套、來源紀律、四段骨架、禁用內部詞 |
| `.claude/skills/weekly-report/references/forecast.md` | 第 (3)(4) 段：兩表格式、回收書寫紀律、帳目生命週期、判準四規格、檔尾數字 |

---

## 步驟

### 1. 決定週次與輸出路徑

取 ISO 週號（若 `$ARGUMENTS` 指定則用指定值，否則用今日所在週），輸出至 `weekly/YYYY-Wnn.md`（`weekly/` 目錄不存在則建立）。

### 2. 蒐集素材

**選題素材**（決定寫什麼）固定涵蓋窗：**近 7 日** `news/*.md`（唯讀，不可修改）＋ `wiki/log.md` 同期 ingest 紀錄＋ `wiki/feature-radar.md`＋ **`wiki/reader-notes.md` 狀態 ⏳ 的 🔍 興趣主題**。

**內容素材**（決定深度）不受此窗限制——`wiki/` 既有頁面、任何一期歷史日報、官方文件、以及**依缺口向外查找**的第三方來源皆可用。約束不在來源位置，在來源可取回性，見 `.claude/skills/weekly-report/references/deepdive.md`「來源紀律」。

> **素材窗是用來確保選題貼著本週，不是用來限制能查多深。**（教訓見沿革檔 2026-W33 A）

### 3. 檢查已深挖題目清單（防重複）

掃描既有 `weekly/*.md`（若有）的「深挖：」小標題，列出近期已深挖過的題目。本週選題撞到舊題目時，必須有**新角度**（新事實或新機制層）才准再上；否則換題。

### 4. 撰寫四段式結構

| 段 | 規範檔 |
|---|---|
| (1) 頭條敘事（300–500 字，不列清單） | `.claude/skills/weekly-report/references/headline.md` |
| (2) 技術討論＋深挖（本週版本／討論綜述／深挖 900–1,300 字） | `.claude/skills/weekly-report/references/deepdive.md` |
| (3) 下週看什麼（新開表在上、回收表在下） | `.claude/skills/weekly-report/references/forecast.md` |
| (4) 檔尾數字（5 個，條列不得寫成表格） | `.claude/skills/weekly-report/references/forecast.md` |

四段的節標題、表頭、判準尾巴等字串一律照 `.claude/skills/weekly-report/references/contracts.md`，不憑記憶寫。

### 5. 凍結存檔

寫入 `weekly/YYYY-Wnn.md` 後視為當週凍結版本，不因後續 ingest 回頭修改（下週報若要回收上週對錯，於新一期第 (3) 段處理，不修舊檔）。唯一例外：同日發現、同日改的可讀性缺陷（見 `.claude/skills/weekly-report/references/headline.md`）。

### 6. 收尾閉迴路

> **由 `/weekly` 帶起時跳過本步驟**（`.claude/commands/weekly.md` 會在三段都跑完後統一收尾）。只有單獨執行 `/weekly-report` 補跑時才執行以下內容。

**沒有這一步，週報只會躺在工作目錄裡**：未 commit、未 build（web reader 的「週報」分頁仍顯示「尚無週報」）、未 push（線上看不到）。

- commit 範圍與訊息：`git -C REPO_ROOT add weekly/` → `commit -m "weekly: YYYY-Wnn 週報"`；web commit 訊息用 `"web: rebuild YYYY-Wnn 週報上站"`
- **其餘照 `.claude/skills/web-publish/SKILL.md` 的 `Step 4`／`Step 5` 形狀做，不另寫一套**：測試閘（`run_tests.py` 失敗 → 跳過 build，仍推送已完成的 weekly commit，回報標「Tests FAILED - build skipped」）、`build_web.py` → add `web_reader/` → commit、**單一 push**、push 失敗重試（`pull --rebase` 上限 2 次）
- **與排程的關係**：`/weekly` 沒有雲端排程，不會與 `daily-news-pipeline-cloud`（每日 12/17/22 UTC 三班）或 `weekly-wiki-lint-cloud`（每週六 03:00 UTC）衝突；產出檔在 `weekly/`，與那兩者會動的 `news/`、`wiki/` 不重疊

---

## 編輯守則

- **淡週寧短勿編**：本週材料單薄時，各段落寧可寫短，不可為了填滿篇幅硬湊。
- **查無不補位**：任一段落（尤其深挖專欄）找不到夠格的題目時，直接省略該段並註明「本週略過」，不可用不夠格的材料硬填。
- **引用具名出處**：所有事實性陳述附具名來源（媒體名、issue 編號、討論串連結等），不可空泛歸因「社群」「有人」。
- 互動數（讚數、留言數等）一律標「（MM-DD 快照）」，避免讀者誤判為即時數字。
- 與 `.claude/skills/wiki-weekly-review/SKILL.md` 分工寫死：對內策展與對外交付**由 `/weekly` 依序帶起，但不可合併成同一段工作**，順序固定為週報先、策展後（三個理由見 `.claude/commands/weekly.md`）。

---

## 邊界

- 由本機 session 執行（`/weekly` 帶起或單獨補跑）；無 egress 環境的退路見 `.claude/skills/weekly-report/references/deepdive.md`。
- 繁體中文為主；`news/` 唯讀，不可修改日報內容；不自行改 `wiki/reader-notes.md` 的狀態。
- 契約字串一律以 `.claude/skills/weekly-report/references/contracts.md` 為準，改任何一格必須同步該表右欄消費端。
- 驗證閘：`scripts/check_weekly_ledger.py`（掛在 `scripts/run_tests.py` 內）綠了才算完；單獨執行時測試失敗則跳過 build，仍推送已完成的 commit。

## 後續（不在本次範圍）

- 第二期 `scripts/weekly_stats.py`：把「檔尾數字」的管線型數字改為腳本自動計算，取代人工盤點；本體裁先跑 2–3 週確認值得讀，再投資腳本化

> **沿革檔：** `docs/rules-changelog/weekly-report.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，）
