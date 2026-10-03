---
name: wiki-ingest
description: 讀取今日日報並更新 wiki 知識庫。每天聚合器執行後使用。
---

# Wiki Ingest

讀取今日日報，以多記者架構更新 wiki 知識庫。**TARGET_DATE** = 呼叫時傳入的日期（`$ARGUMENTS`，或 pipeline 傳入的 TARGET_DATE）；未提供則用今天的日期。

> `.claude/skills/news-pipeline/SKILL.md` 的 Phase B 直接讀本 skill 執行，不另維護副本——修改本檔的分類、派工或彙整邏輯時，`/news-pipeline` 會自動套用最新版本，不需同步修改其他檔案。

兩份參考檔，正文不重述：

- **派工** → `.claude/skills/wiki-ingest/references/dispatch.md`（類別↔角色檔對照表、六記者 prompt 模板、防偏誤說明、4b／4c 首段）——**派工前逐字讀它**
- **核對與寫檔** → `.claude/skills/wiki-ingest/references/checklist.md`（共用檔案的逐檔寫入規則、完成前強制核對清單、完成摘要表）

---

## 步驟

### 1. 確認今日日報與 wiki 現況

讀取 `news/TARGET_DATE.md`。若檔案不存在，停止並告知使用者。

**再取當日「未進日報」的條目（強制）：**

```
python scripts/list_digest_omissions.py --date TARGET_DATE
```

**日報是給讀者看的，只留讀者要讀的重點，篩掉一部分是預期行為；但 wiki 是沉澱層，要考慮全部。** 收不收由各類別記者依自己的門檻判斷——**不收可以，沒看過不行**。上述指令列出的條目與日報條目一起進入下一步分類。

**再取懸置標記命中偵測結果：** 若當日 `/news-pipeline` 已跑過 Step 3f，直接取用其 stdout 印出的派工附件（依記者分組的「待查證命中」清單）；若無此輸出（如單獨補跑 `/wiki-ingest`），自行執行：

```
python scripts/scan_pending_verifications.py TARGET_DATE
```

輸出依記者類別分組，供下一步派工時原樣附在對應記者的訊息裡；某類別無命中則該記者派工訊息此區塊寫「無」。規格見 `.claude/reporter-rules/page-templates.md`「懸置標記語法」節。

**再取轉知待接手清單：** 執行 `python scripts/pending_handoffs.py list`，輸出依目標記者分組，派工時附在對應記者訊息的「轉知待接手」區塊；無則寫「無」。這是先前 ingest 的記者「⚠️ 需主編轉知」經主編登帳後的未結案項（帳本 `data/pending-handoffs.jsonl`，主編端的登帳與結案動作見 `.claude/skills/wiki-ingest/references/checklist.md`）。

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/skills/wiki-ingest/references/classification.md` — 分類表、分流鐵則與派工正典
- `wiki/index.md` — 取得所有現有頁面清單
- `wiki/log.md` — 確認最近是否已處理過同一份日報（避免重複 ingest）

### 2. 分類（主編）

讀完**日報條目 + 上一步列出的未收錄條目**後，依 `.claude/skills/wiki-ingest/references/classification.md` 的分類表為每則新聞標記類別，跨類別條目可標多個。**主編要寫的只有一張 routing 表**（url → 類別或排除理由，schema 見 classification.md「分類紀錄」），先產骨架（每則原料一筆）：

```
python scripts/build_ingest_packets.py --date TARGET_DATE --init --routing data/ingest-packets/TARGET_DATE/routing.json
```

逐則填 `categories`；排除者填 `reason`；只針對該則的事實性提示寫 `note`；排除條目的摘要是殼層時補 `summary_override`。

**專頁定向抓取的條目（`topic` 欄非空）**：來源標籤 `Topic Watch / <slug>`，是為某個 wiki 專頁定向抓來的，**直接路由給該 slug 所屬領域的記者**，不必再走類別判斷。包裡會自動標 `專頁定向`。

> 這批的標題天生不含 Claude/Anthropic——那正是它們被定向抓來的原因。記者**不得因為「跟 Claude 沒關係」而略過**，但仍須依該專頁自己的觸發條件判斷收不收——不收可以，沒看過不行。

**分類紀錄、對帳與產包（強制，派工前）：**

```
python scripts/build_ingest_packets.py --date TARGET_DATE --routing data/ingest-packets/TARGET_DATE/routing.json --out data/ingest-packets/TARGET_DATE/
```

它依 routing 把當日每則原料 append 進 `data/classification-log.jsonl`、內呼 `python scripts/check_classification_log.py --date TARGET_DATE` 對帳，綠了才產包：每類一份 `<類別>.md`（逾 25K 字元切成 `<類別>-k.md`）與給複核記者的 `排除.md`，印出各包路徑與大小。來源 slug、日報段落原文、`日報未收錄`／`專頁定向` 旗標、同事件聚合、`已收錄比對`（前幾天已歸因到哪頁）都由腳本填，記者照抄 slug 進「來源歸因」欄。無條目的類別不產包、不派工。

- exit 1＝routing 漏則或多了原料外的 URL、排除沒理由、note 是操作指示、來源未註冊、或模擬對帳有阻斷問題：**未寫帳、未產包**，修 routing 重跑。重跑冪等（與帳上同 URL 最後一行相同者不重複 append）；改判就改 routing 重跑，腳本 append 更正行（帳本不改舊行，同 URL 最後一行勝出）。
- exit 3＝原料或日報缺檔：跑 `python scripts/check_classification_log.py --date TARGET_DATE` 分辨。它 exit 2＝原料已逾 14 天保留窗（逾期 backfill）：無原料可產包，改從 `news/TARGET_DATE.md` 手工整理各類節錄（每則標來源 slug），帳本每行 `reason` 註明「原料已逾保留窗，未對帳」，照常進步驟 3。它 exit 3＝原料在窗內卻缺檔或損毀＝抓料缺件，**不得跳過**，先修抓料（`docs/daily-automation.md`）再回來。

主編分類是整條鏈唯一沒有第二人把關的一步，這是它唯一的留痕與對帳點。

### 3. 派工（Agent tool）

**對每個有條目的類別，呼叫 Agent tool**，同批**加派分類複核記者**（覆核步驟 2 產出的 `排除.md`，prompt 見 `.claude/skills/wiki-ingest/references/dispatch.md`「3b」；當日排除 0 則則不派，完成摘要記「排除 0 則，未派複核」）。有多個類別時，在同一訊息中同時發出所有 Agent 呼叫（並行執行）。每個呼叫一律 **`subagent_type: "general-purpose"` + `model: "sonnet"`**（本機與雲端唯一正典派工路徑，理由見 `.claude/skills/wiki-ingest/references/classification.md`「派工方式」；sonnet 因分類與頁面更新為有界任務，不需旗艦模型；未指定會繼承主 session 模型，六記者並行足以打穿訂閱配額）。

> ⚠️ **記者 agent 必須以 foreground（同步）方式啟動：每個呼叫明寫 `run_in_background: false`**（Agent 工具未指定時預設背景；`.claude/hooks/guard_roles.py` 擋下漏寫的派工）。背景記者的完成通知無法回到派工 agent，會造成永久等待。

每位記者 prompt 的條目節錄＝貼入 `data/ingest-packets/TARGET_DATE/<類別>.md` 全文（切份者依序貼齊，每份末行 `END` 都要在）。類別↔角色檔對照表、prompt 五區塊模板與防偏誤說明住 `.claude/skills/wiki-ingest/references/dispatch.md`，逐字照它派。

### 3b. 處理分類回退（主編，同輪內處理，不等下一輪）

收齊六記者與分類複核記者的回報後，彙整所有「分類回退」項目（六記者回報欄＋分類複核記者的「誤排除」判定），逐項核對：

1. **目標類別原輪是否已收到這則？** 查 `data/classification-log.jsonl` 該則的 `categories`——已含目標類別就不追加派工（那位記者已經處理過，再派會用新 context 重讀頁面、有機會重複寫入），在完成摘要記「已由原輪 [類別] 記者處理」即可
2. **理由是否成立？** 比對 `.claude/skills/wiki-ingest/references/classification.md`「分類表」與「分流鐵則」。記者／複核記者的判斷多數可採信，主編只擋明顯錯誤；不成立則不派，完成摘要註明理由
3. **按類別合併追加派工。** 成立的項目依目標類別分組，一類一次呼叫（不是一則一次——每次呼叫都是完整記者啟動，讀角色檔與規則檔就要十幾萬 token），模板見 `.claude/skills/wiki-ingest/references/dispatch.md`「3c」。**同輪內完成**，不登轉知帳本（轉知是「兩面都有事實」，分類回退是主編分錯，責任在主編，當場修）
4. **一則最多一跳。** 追加派工的記者若再回退，不再派，記入完成摘要待使用者裁示。雲端無人值守，沒有這條會來回乒乓
5. 追加派工的回報併入步驟 4 彙整，視同該記者原輪就收到；並在 routing 把該則 `categories` 補上目標類別、`reason` 附一句「分類回退自 [原類別]」後重跑步驟 2 的產包指令（腳本 append 更正行，不改舊行；3c 的條目區塊從重產的目標類別包裡取）

無分類回退項目時本步驟略過。

### 4. 彙整共用檔案（主編）

收到所有記者回報後，先把六記者（與 4c 投資分析記者）每份回報的最終訊息原文存成 `data/ingest-packets/TARGET_DATE/reports/<類別>.md`，跑收報腳本：

```
python scripts/collect_reporter_reports.py --date TARGET_DATE data/ingest-packets/TARGET_DATE/reports/
```

預設只印不寫：待 append 的歸因行（slug 未註冊、頁面不存在的行已剔除並警示）、轉知 close 指令、open 指令草稿（負責人依 `wiki/index.md` 推）、未回應清單（包裡有、回報沒提到的 URL）與 log 條目骨架。看過警示與未回應清單、該追問的追問完，加 `--apply` 重跑才 append `data/source_attribution.jsonl` 並執行 close。分類複核記者的判定走步驟 3b，不放進此夾。

接著統一更新共用檔案：`wiki/feature-radar.md`、`wiki/index.md`、`wiki/log.md`、`data/source_attribution.jsonl`、`data/pending-handoffs.jsonl`，以及視情況更新 `wiki/overview.md`。**逐檔寫入規則見 `.claude/skills/wiki-ingest/references/checklist.md`**，本檔不重述。

### 4b. devpractice 沉澱派工（主編）

彙整完成後（wiki 檔案已定稿），派 devpractice 記者做每日沉澱——他不吃日報條目，吃**本輪 ingest 寫進 wiki 的 diff**，所以必須排在彙整之後。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段見 `.claude/skills/wiki-ingest/references/dispatch.md`。

收報後把「候選 N 筆／本日無候選」記入 log.md 本次 ingest 紀錄一行 `devpractice 沉澱：…`；`data/devpractice-candidates.jsonl` 與 `data/devpractice_state.json` 併入收尾 commit（雲端與本機共用同一條 diff 基準線，不 commit 會斷）。

### 4c. market 判讀派工（主編）

與 4b 同批派出（兩者互不相干，可並行）。投資分析記者不吃分類路由，吃**當日日報本身**換市場框架重讀，但判讀要 wikilink 指向已定稿的事實頁，故同樣排在彙整之後。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段見 `.claude/skills/wiki-ingest/references/dispatch.md`，其後依序貼入 `data/ingest-packets/TARGET_DATE/` 六類包檔全文（與六記者同一份步驟 2 產物，不另篩）。

收報後把「判讀 N 則／本日無訊號」記入 log.md 本次 ingest 紀錄一行 `market 判讀：…`；記者回報存進步驟 4 的 `reports/` 夾（檔名 `<類別>.md` 同規則）後照步驟 4 跑收報腳本落帳（slug 用該則日報條目的來源，不是 `user-query`）。

### 4½. 內容閘（主編）

4、4b、4c 全部寫完後、步驟 5 之前跑：

```
python scripts/ingest_gate.py --date TARGET_DATE
```

它從 `scripts/run_tests.py` 挑內容類閘來跑（新鮮度、feature-radar 對帳、懸置標記、階層、讀者語言、字元上限、tools 決策表、log 轉知對帳），綠只印末行、紅印全文。**exit 非 0 由主編同輪修到綠才可進步驟 5**——這些紅多半出在本輪剛寫的檔，拖到 Phase C 就變成另一個執行者事後補。

- 修失敗訊息指名的位置、改內容本身；不動 `scripts/check_*.py`
- 輸出末段列出基線／白名單檔（`data/*baseline*.json`、`data/*-allow.json`）相對 HEAD 的變動：把命中收進基線或白名單也會轉綠，只在確屬誤判時才收，理由寫進 commit 訊息
- log 轉知對帳紅＝該行沒對上帳本：先照步驟 4 `open` 登帳，把單號補進本輪該行（本輪紀錄尚未 commit）；確實不需登帳的寫「不登帳：<理由>」

### 5. 完成前強制核對與摘要

**在宣告完成之前**，逐項確認 `.claude/skills/wiki-ingest/references/checklist.md` 的核對清單，再依該檔的摘要表格式輸出完成摘要。

**量測帳本（只量不評，不擋 commit）：** log 寫完後跑

```
python scripts/ingest_metrics.py --date TARGET_DATE
```

它從本機 subagent transcript 為每位記者 append 一行到 `data/ingest-metrics.jsonl`（併入收尾 commit），並印摘要表（角色／run／turns／tool_uses／edits／cache_read／output／wiki 整讀數／狀態）。看三件事：同角色與前幾天比 turns、cache_read 有沒有明顯跳動；`wiki_full_reads` 有沒有整讀大頁；狀態欄「⚠️ 不完整」的行數字只是下限，不拿來比。找不到 transcript 時（雲端 routine 是否留有 transcript 尚未以探針證實）腳本印「無 transcript」、exit 0、不寫任何行——log 帶一句「本輪無量測」即可，**不手補零值行**。重跑同日冪等。

---

## 邊界

- 由主 session（本機）或頂層 session（雲端）執行並 foreground 派工；記者不可再呼叫 Agent tool 委派工作。
- 繁體中文為主，英文術語保留英文。
- 所有 wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/` 路徑下；`news/` 目錄唯讀，不可修改日報內容。
- `wiki/log.md`、`data/source_attribution.jsonl`、`data/pending-handoffs.jsonl` 皆為 append only，不可修改既有條目。
- 若日報今日無新內容（來源全部失敗），在 log.md 記錄一筆「無新內容」即可。
- **收件匣提醒**：ingest 完成後檢查 `wiki/reader-notes.md`，若有狀態 ⏳ 且距今 > 14 天的項目，在完成摘要末尾列出提醒（避免使用者「記一下」的想法積壓無人處理）；無則不提。
- 驗證閘：步驟 4½ `ingest_gate.py` 綠、核對清單逐項有值、完成摘要已輸出，才算完成。

> **沿革檔：** `docs/rules-changelog/wiki-ingest.md`——條文中的教訓敘事住該檔，執行時不必讀。
