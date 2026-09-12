---
name: wiki-ingest
description: 讀取今日日報並更新 wiki 知識庫。每天聚合器執行後使用。
---

# Wiki Ingest

讀取今日日報，以多記者架構更新 wiki 知識庫。**TARGET_DATE** = 呼叫時傳入的日期（`$ARGUMENTS`，或 pipeline 傳入的 TARGET_DATE）；未提供則用今天的日期。

> `.claude/commands/news-pipeline.md` 的 Phase B 直接讀本 skill 執行，不另維護副本——修改本檔的分類、派工或彙整邏輯時，`/news-pipeline` 會自動套用最新版本，不需同步修改其他檔案。

兩份參考檔，正文不重述：

- **派工** → `.claude/skills/wiki-ingest/dispatch.md`（類別↔角色檔對照表、六記者 prompt 模板、防偏誤說明、4b／4c 首段）——**派工前逐字讀它**
- **核對與寫檔** → `.claude/skills/wiki-ingest/checklist.md`（共用檔案的逐檔寫入規則、完成前強制核對清單、完成摘要表）

---

## 步驟

### 1. 確認今日日報與 wiki 現況

讀取 `news/TARGET_DATE.md`。若檔案不存在，停止並告知使用者。

**再取當日「未進日報」的條目（強制）`[加入: 2026-07-26]`：**

```
python scripts/list_digest_omissions.py --date TARGET_DATE
```

**日報是給讀者看的，只留讀者要讀的重點，篩掉一部分是預期行為；但 wiki 是沉澱層，要考慮全部。** 收不收由各類別記者依自己的門檻判斷——**不收可以，沒看過不行**。上述指令列出的條目與日報條目一起進入下一步分類。

**再取懸置標記命中偵測結果 `[加入: 2026-08-10]`：** 若當日 `/news-pipeline` 已跑過 Step 3f，直接取用其 stdout 印出的派工附件（依記者分組的「待查證命中」清單）；若無此輸出（如單獨補跑 `/wiki-ingest`），自行執行：

```
python scripts/scan_pending_verifications.py TARGET_DATE
```

輸出依記者類別分組，供下一步派工時原樣附在對應記者的訊息裡；某類別無命中則該記者派工訊息此區塊寫「無」。規格見 `.claude/reporter-rules/wiki-ingest-format.md`「懸置標記語法」節。

**再取轉知待接手清單 `[加入: 2026-08-15]`：** 執行 `python scripts/pending_handoffs.py list`，輸出依目標記者分組，派工時附在對應記者訊息的「轉知待接手」區塊；無則寫「無」。這是先前 ingest 的記者「⚠️ 需主編轉知」經主編登帳後的未結案項（帳本 `data/pending-handoffs.jsonl`，規格見 `.claude/reporter-rules/wiki-ingest.md`「第三步」轉知帳本段）。

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/reporter-rules/wiki-ingest.md` — 分類標準與派工流程（主編指南）
- `wiki/index.md` — 取得所有現有頁面清單
- `wiki/log.md` — 確認最近是否已處理過同一份日報（避免重複 ingest）

### 2. 分類（主編）

讀完**日報條目 + 上一步列出的未收錄條目**後，依 `.claude/reporter-rules/wiki-ingest.md` 的分類表為每則新聞標記類別。
跨類別條目可標多個類別。

未進日報的條目在原文節錄中標一行 `- **日報未收錄**（僅原始抓取資料，摘要較簡略）`，讓記者知道細節密度不同、判斷時以自己的類別門檻為準。

**專頁定向抓取的條目（`topic` 欄非空）`[加入: 2026-08-13]`**：`gathered_items.json` 中 `topic` 非空者，是為某個 wiki 專頁定向抓來的（來源標籤 `Topic Watch / <slug>`），**直接路由給該 slug 所屬領域的記者**，不必再走類別判斷。原文節錄中標一行 `- **專頁定向**（目標頁：topics/<slug>；收錄判準為該專頁觸發條件，**不套用 Claude/Anthropic 關聯門檻**）`。

> 這批的標題天生不含 Claude/Anthropic——那正是它們被定向抓來的原因。記者**不得因為「跟 Claude 沒關係」而略過**，但仍須依該專頁自己的觸發條件判斷收不收——不收可以，沒看過不行。

分類完成後，為每個有條目的類別整理原文節錄（格式如下）：

```
## [類別] 條目（共 N 則）

### [條目標題]
- **來源：** [媒體/平台]
- **日期：** YYYY-MM-DD
- **摘要：** [原文關鍵內容，保留數字、版本號、具名企業等細節]
- **原文重點：** [直接引用日報中的關鍵段落，不壓縮細節]

### [下一則...]
```

無條目的類別標記「無」，不派工。

### 3. 派工（Agent tool）

**對每個有條目的類別，呼叫 Agent tool**。有多個類別時，在同一訊息中同時發出所有 Agent 呼叫（並行執行）。每個呼叫一律 **`subagent_type: "general-purpose"` + `model: "sonnet"`**（本機與雲端唯一正典派工路徑，理由見 `.claude/reporter-rules/wiki-ingest.md`「派工方式」；sonnet 因分類與頁面更新為有界任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

> ⚠️ **記者 agent 必須以 foreground（同步）方式啟動，不可設 `run_in_background: true`。** 背景記者的完成通知無法回到派工 agent，會造成永久等待。

類別↔角色檔對照表、prompt 五區塊模板與防偏誤說明住 `.claude/skills/wiki-ingest/dispatch.md`，逐字照它派。

### 4. 彙整共用檔案（主編）

收到所有記者回報後，統一更新共用檔案：`wiki/feature-radar.md`、`wiki/index.md`、`wiki/log.md`、`data/source_attribution.jsonl`、`data/pending-handoffs.jsonl`，以及視情況更新 `wiki/overview.md`。**逐檔寫入規則見 `.claude/skills/wiki-ingest/checklist.md`**，本檔不重述。

### 4b. devpractice 沉澱派工（主編）`[加入: 2026-09-02]`

彙整完成後（wiki 檔案已定稿），派 devpractice 記者做每日沉澱——他不吃日報條目，吃**本輪 ingest 寫進 wiki 的 diff**，所以必須排在彙整之後。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段見 `.claude/skills/wiki-ingest/dispatch.md`。

收報後把「候選 N 筆／本日無候選」記入 log.md 本次 ingest 紀錄一行 `devpractice 沉澱：…`；`data/devpractice-candidates.jsonl` 與 `data/devpractice_state.json` 併入收尾 commit（雲端與本機共用同一條 diff 基準線，不 commit 會斷）。

### 4c. market 判讀派工（主編）`[加入: 2026-09-05]`

與 4b 同批派出（兩者互不相干，可並行）。投資分析記者不吃分類路由，吃**當日日報本身**換市場框架重讀，但判讀要 wikilink 指向已定稿的事實頁，故同樣排在彙整之後。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段見 `.claude/skills/wiki-ingest/dispatch.md`，其後附今日日報條目節錄（與六記者同一份步驟 2 產物，不另篩）。

收報後把「判讀 N 則／本日無訊號」記入 log.md 本次 ingest 紀錄一行 `market 判讀：…`；記者回報的來源歸因照步驟 4 append 至 `data/source_attribution.jsonl`（slug 用該則日報條目的來源，不是 `user-query`）。

### 5. 完成前強制核對與摘要

**在宣告完成之前**，逐項確認 `.claude/skills/wiki-ingest/checklist.md` 的核對清單，再依該檔的摘要表格式輸出完成摘要。

---

## 邊界

- 由主 session（本機）或頂層 session（雲端）執行並 foreground 派工；記者不可再呼叫 Agent tool 委派工作。
- 繁體中文為主，英文術語保留英文。
- 所有 wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下；`news/` 目錄唯讀，不可修改日報內容。
- `wiki/log.md`、`data/source_attribution.jsonl`、`data/pending-handoffs.jsonl` 皆為 append only，不可修改既有條目。
- 若日報今日無新內容（來源全部失敗），在 log.md 記錄一筆「無新內容」即可。
- **收件匣提醒**：ingest 完成後檢查 `wiki/reader-notes.md`，若有狀態 ⏳ 且距今 > 14 天的項目，在完成摘要末尾列出提醒（避免使用者「記一下」的想法積壓無人處理）；無則不提。
- 驗證閘：核對清單逐項有值、完成摘要已輸出，才算完成。

> **沿革檔：** `docs/rules-changelog/wiki-ingest.md`——條文中的教訓敘事住該檔，執行時不必讀。
