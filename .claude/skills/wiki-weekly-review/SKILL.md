---
name: wiki-weekly-review
description: 每週判斷本週有哪些主題值得加碼追蹤（建頁/加開子區塊/升熱度），經使用者確認後執行。
---

# Wiki 週度延伸回顧

> **這是每週工作的第二段，不是入口。** 平常跑 `/weekly`（總指揮，會先跑 `.claude/skills/weekly-report/SKILL.md` 再跑本 skill）；單獨執行本 skill 只在補做策展那一段時使用。
> 單獨執行時，收尾（步驟 6）由本 skill 自己負責；由 `/weekly` 帶起時，**步驟 6 一律跳過**，收尾交給總指揮統一做（單一 push）。

每週執行一次，建議在週末或週一執行，可與 `.claude/skills/wiki-lint/SKILL.md` 同一天跑。

**與 `.claude/skills/wiki-lint/SKILL.md` 的分工：** wiki-lint 處理結構性正確性與精簡（矛盾、孤立頁面、過期狀態、過長頁面重構）；本 skill 只做**延伸判斷**——找出值得加碼追蹤的主題，是主觀取捨，需要使用者確認才能執行。

派工 prompt 全文、月度聚焦校準 agent 規格與輸出表、彙整清單格式、log 模板住 `.claude/skills/wiki-weekly-review/references/dispatch.md`，本檔不重述——**派工前逐字讀它**。

---

## 步驟

### 1. 載入本週範圍

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/reporter-rules/wiki-ingest.md` — 分類標準（沿用六類記者分工）
- 過去 7 天的 `news/*.md`
- `wiki/log.md` 近期 ingest 紀錄
- `wiki/index.md`
- `wiki/reader-notes.md` — 使用者「記一下」的待辦收件匣（本週要消費的讀者需求訊號）

### 1b. 讀者回饋入口（GitHub Issues）`[加入: 2026-09-04]`

網站頁尾「這段看不懂／這條錯了？」連到 GitHub Issue 範本（label `reader-feedback`），是唯一的**真人**訊號入口——冷讀者 review 再多都是模擬。本步：

```
gh issue list --label reader-feedback --state open --json number,title,createdAt
```

每筆依內容分類 append 進 `wiki/reader-notes.md`（🎨 版面／📝 內容修正／🔍 興趣主題），註明 issue 編號，隨既有消費路徑處理；處理完在 issue 留一句去向並關閉。**雲端環境無 `gh` 或無網路時寫「讀者回饋：本輪無法讀取（環境限制）」，不得寫成「無回饋」。**

### 2. 六位記者並行判斷（同一訊息中平行呼叫全部）

沿用 `.claude/skills/wiki-ingest/references/dispatch.md` 的類別對應表與派工方式（`subagent_type: "general-purpose"`＋prompt 首段角色前導導向 `.claude/agents/wiki-reporter-[category].md`）。每個 Agent 呼叫必須帶 `model: "sonnet"`（lint 與策展為有界判斷任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

prompt 全文見 `.claude/skills/wiki-weekly-review/references/dispatch.md`「六記者派工 prompt」。

### 月度加項：聚焦校準 `[加入: 2026-07-05]`

**每月執行一次**（判斷方式：`wiki/metrics.md` 的「聚焦命中率」欄**本月尚無數值** → 執行；已有數值 → 輸出「本月聚焦校準已執行，跳過」並跳過本節）。判斷產出物而非執行記錄（立法理由見沿革檔 `docs/rules-changelog/wiki-weekly-review.md` 2026-07-16）。

執行時派一個 Sonnet agent（`model: "sonnet"`），規格與輸出表見 `.claude/skills/wiki-weekly-review/references/dispatch.md`「月度聚焦校準」。命中率數字 append 進 `wiki/metrics.md` 對應欄（只 append 不改舊列）。

### 3. 彙整回報給使用者確認

收齊六位記者回報後，彙整成單一清單呈現給使用者，**不自動執行**。格式見 `.claude/skills/wiki-weekly-review/references/dispatch.md`「彙整確認清單」。

**同時處理 `wiki/reader-notes.md` 收件匣**（本 skill 是它的每週消費者）：
- 🔍 興趣主題被記者採納為加碼建議 → 在清單標明來源，該 note 待使用者確認執行後標 ✅ 已納入
- 🎨 版面建議、📝 內容修正 → 列進呈現清單提醒使用者（版面由使用者觸發 web 改動、內容修正轉下次 ingest/lint）；使用者確認處置後標 ✅
- 未被採納的 🔍 興趣主題 → 保留 ⏳（不強制清除，訊號可能之後成形）
- 📌 📓 雜記 → 讀作「近期方向背景」輔助本週判斷，不需動作；**清除距今 > 30 天的雜記**（日記性質，過期即除）

### 4. 依確認執行

使用者確認後，若牽涉多頁修改可再次平行派工對應記者執行；若牽涉新頁面建立，讀 `.claude/reporter-rules/wiki-ingest-format.md` 頁面格式模板。此階段派工同樣沿用 `model: "sonnet"`。

### 5. 記錄

完成後在 `wiki/log.md` 末尾 append，模板見 `.claude/skills/wiki-weekly-review/references/dispatch.md`「log 條目」。

### 6. 收尾閉迴路：commit wiki + build web + 單一 push `[加入: 2026-07-10]`

> **由 `/weekly` 帶起時跳過本步驟**（`.claude/commands/weekly.md` 會在兩個子流程都跑完後統一收尾）。只有單獨執行本 skill 時才執行以下內容。

**僅當步驟 4 實際執行了頁面修改時才需要**（使用者「都不要」且無 log 以外變更 → 仍須 commit log.md 這一筆，照走本步）。理由同 `.claude/skills/wiki-lint/SKILL.md` 步驟 10：本 skill 改 `wiki/*.md` 不會自動上站，web build 僅發生於本步與 `/news-pipeline`。

依序執行（`REPO_ROOT` = `C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS`，`PYTHON` = `C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe`）：

1. `git -C REPO_ROOT add wiki/` → `git -C REPO_ROOT commit -m "wiki: weekly review YYYY-MM-DD"`（無變更則跳過）
2. `PYTHON REPO_ROOT\scripts\run_tests.py`（失敗 → 跳過 build 與 web commit，仍執行步驟 4 推送 wiki commit）
3. `PYTHON REPO_ROOT\scripts\build_web.py` → `git -C REPO_ROOT add web_reader/` → `git -C REPO_ROOT commit -m "web: rebuild YYYY-MM-DD（週度回顧上站）"`
4. `git -C REPO_ROOT push`（單一 push，理由見 `.claude/skills/web-publish/SKILL.md` Step 5）

---

## 邊界

- 由主 session 執行並派工六記者（`model: "sonnet"`）；記者只回報，不直接修改頁面。
- 繁體中文為主；`wiki/log.md` 只能 append，不可修改既有條目；`news/` 唯讀。
- 本 skill 產出的建議屬主觀判斷，**未經使用者確認一律不得執行修改**。
- 單獨執行時步驟 6 的 `run_tests.py` 綠了才 build web；由 `/weekly` 帶起時步驟 6 跳過，收尾由總指揮負責。
