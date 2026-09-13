---
name: news-digest
description: 每日 pipeline Step 1b：讀 gathered_items.json 寫 news/ 日報並自檢、commit；骨架見 format.md，判準見 selection.md。
disable-model-invocation: true
---

# Step 1b：生成日報

由 `.claude/skills/news-pipeline/SKILL.md` 的 Phase A 背景 agent 讀取執行，接在 `.claude/skills/news-gather/SKILL.md` 的 Step 1a 之後、Step 1c 之前。REPO_ROOT／PYTHON／TARGET_DATE 由派工 prompt 傳入。**本 skill 不 spawn 子 agent。**

兩份參考檔，正文不重述：

- **格式** → `.claude/skills/news-digest/references/format.md`（機械契約字串表、骨架、每條排版格式、檔尾規則）
- **選材** → `.claude/skills/news-digest/references/selection.md`（聚焦門檻、各區塊收錄條件、防重複、禁詞清單）

---

## 0-1. 新鮮度防線（強制，生成前先做）

讀取 `src/gathered_items.json`，確認 `date` 等於 TARGET_DATE 且 `items` 非空。

- 兩者皆滿足 → 繼續
- 任一不滿足 → **中止，不生成假日報**。Step 6 log 寫 `ABORTED: gathered_items.json date=<實際值> items=<數量>，非目標日期的新鮮資料`，結束

本機剛跑完 Step 1a 時這道檢查通常必然通過（資料才剛產生）；它真正保護的是**replay 路徑**——雲端每日班與補跑都是 `cp gathered_archive/<date>.json` 進來，而檔名只差一個字就會 replay 錯一天，這道檢查是唯一擋得住的地方。兩種環境都執行，不因「應該不會發生」而略過。

## 0-2. 原料健康檢查（強制）

新鮮度防線只擋「沒抓到」，擋不住「抓到但殘缺」——10 個來源掛 9 個仍會生出一份看起來正常、實則系統性偏食的日報，並被六記者沉澱進 wiki 變成長期污染。

```
PYTHON REPO_ROOT\scripts\check_gather_health.py
```

- **exit 0 且輸出無 ⚠️** → 正常生成
- **exit 0 但輸出有 ⚠️（失敗來源達警示數）** → 照常生成，但**必須**在日報的 `📡 來源狀態` 區塊上方加一行 `> ⚠️ 本日 N 個來源抓取失敗，涵蓋面較平日窄`，Step 6 log 一併記錄
- **exit 2 或 3** → **中止，不生成日報**。Step 6 log 寫 `ABORTED: gather health check failed`＋腳本輸出，結束

門檻與校準依據寫在腳本內（依 07-10~07-24 實績設定），要調整改腳本常數，不要在這裡另寫一套數字。

## 1. 讀料

讀取 `src/gathered_items.json`。

## 2. 生成

直接用繁體中文生成日報 Markdown（**不呼叫任何外部 API**）：骨架與語氣分寸照 `.claude/skills/news-digest/references/format.md`，各區塊收什麼照 `.claude/skills/news-digest/references/selection.md`。

## 3. 寫入

寫入 `news/TARGET_DATE.md`（完整 Markdown）。

## 3a. 格式自檢（強制）

寫入後執行下列指令，若輸出為 0 表示條目格式錯誤，必須依 `format.md`「每條排版格式」重寫再檢：

```
grep -cE '^\*\*\[.+\]\(https?://' news/TARGET_DATE.md
```

（今日聚焦以外的每個區塊各條目都應貢獻一個匹配；正常日報此數值 ≥ 5）

## 3a-2. 內規外洩自檢（強制）

對 `news/TARGET_DATE.md` 跑 `.claude/skills/news-digest/references/selection.md`「禁詞清單」節的 grep，**應為零命中**；有命中就刪除該段再檢。

## 3b. 來源狀態表存在性檢查（強制）

```
grep -c "^| .* | [✅❌] | [0-9]" news/TARGET_DATE.md
```

（應 ≥ 8，代表來源狀態表已寫入；若不足，補寫 📡 來源狀態區塊再檢）

## 3d. 摘要忠實度自檢（強制）

抽樣核對說明句是否忠於原文——**凡進了日報的條目，記者就是讀你寫的摘要來沉澱**（未進日報者另走 `scripts/list_digest_omissions.py` 直接餵原始抓取資料），摘要失真會被沉澱成長期污染：

- 抽樣：今日聚焦**全抽**＋其餘區塊各抽 1 條（合計約 8–10 條）
- 逐條對照 `gathered_items.json` 中同 URL 條目的 `title` / `summary`：說明句中的**事實成分**（數字、版本號、主詞、因果、結論）必須能從原文支撐；原文沒有的具體數字或結論不可出現
- 不符 → 以原文為準改寫該條說明句，改寫後重檢
- 結果記入本 Step 回報（「忠實度自檢：抽 N 條，改寫 M 條」）；**M ≥ 3 視為摘要品質異常**，除改寫外須在回報中標 ⚠️ 供使用者判斷是否深查
- 判斷原則：這是「忠實」檢查不是「精彩」檢查——語氣、取捨、詳略不管，只管事實有沒有依據

## 3e. 週報未結案預告偵測（機械，非 LLM）

```
PYTHON REPO_ROOT\scripts\scan_open_forecasts.py TARGET_DATE
```

- 讀 `weekly/` 最新一期的未結案預告，取其判準結尾的「｜查證：關鍵字」對今日日報做字串比對，命中則 append 至 `weekly/open-signals.jsonl`，供下期 `/weekly-report` 回收時取用（免去憑記憶重讀七天日報）
- **純字串比對，不做判斷、不改日報**；命中與否都不影響本日產出，失敗只記錄不阻斷 pipeline
- ⚠️ **此步驟必須留在選材與寫入之後**：若讓選材階段知道週報正在賭什麼，會產生確認偏誤——選材傾向撿能證實預告的條目，命中率虛高，並連帶破壞每月聚焦校準的獨立性（校準量測的正是選材品質，兩者不得互相知情）。規格見 `.claude/skills/weekly-report/references/forecast.md` 第 (3) 段

## 3f. 懸置標記命中偵測（機械，非 LLM）

```
PYTHON REPO_ROOT\scripts\scan_pending_verifications.py TARGET_DATE
```

- 拿 wiki 全庫「懸置標記」（見 `.claude/reporter-rules/page-templates.md`「懸置標記語法」節）的探針比對今日日報，命中則 append 至 `data/pending-signals.jsonl`，並在 stdout 印出依記者分組、可直接貼進派工的附件
- 輸出由執行 Step 2（wiki ingest）的主 session 取用：把對應記者類別的派工附件段落原樣附在該記者的派工訊息裡，讓記者知道「今天日報可能回答了哪個懸置」
- **B 級（僅單一弱探針命中且僅在內文）不進派工附件**，只記入 jsonl 供之後查核，不得轉貼給記者
- **純字串比對，不做判斷、不改 wiki**；失敗只記錄不阻斷 pipeline，不影響本日其餘產出

## 3g. 截止日到期前強制官方複查（機械，非 LLM）

```
PYTHON REPO_ROOT\scripts\scan_expiring_deadlines.py
```

- 掃全 wiki 的「⏰ 倒數中」表列與散文 `⏰ YYYY-MM-DD` 標記，列出**已過期**與**7 天內到期**者
- **記者不處理這批**（無 web 工具，不可自行推斷）。輸出接進 Step 6 的完成摘要「📋 待使用者裁示」（格式見 `.claude/skills/web-publish/SKILL.md`），由主編層 WebFetch 查官方原文後三選一：日期仍有效 → 不動／已延長 → 更新截止日並記事件／已作廢 → 移除倒數並**回掃全庫引用方**（同一截止日常散在 3 處以上，只改一處等於沒改）
- 無命中時印「無需複查的截止日」，不佔用摘要版面；失敗只記錄不阻斷 pipeline

## 4. Commit（先不 push）

用 Bash git 暫存並 commit（**先不 push**，本次所有變更於 Step 5 統一推送，避免多次 push 觸發 Pages 部署並發競爭）：

```
git -C REPO_ROOT add news/TARGET_DATE.md
git -C REPO_ROOT add data/pending-signals.jsonl
git -C REPO_ROOT commit -m "news: daily digest TARGET_DATE"
```

- `data/pending-signals.jsonl` 為 3f 產出（懸置標記命中紀錄），無變更時 `git add` 為 no-op，不影響 commit
- 若 commit 失敗，停止並回報錯誤，不繼續後續步驟

commit 成功後回到 `.claude/skills/news-gather/SKILL.md` 的 `Step 1c：確認 emitted-cache`。

---

> **沿革檔：** `docs/rules-changelog/news-pipeline-steps.md`——條文中「沿革檔 YYYY-MM-DD」皆指該檔對應段（歷史敘事不進 agent 讀取範圍，）
