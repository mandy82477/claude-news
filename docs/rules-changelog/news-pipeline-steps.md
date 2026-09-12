# .claude/commands/news-pipeline-steps.md 沿革（教訓存檔）

本檔是 .claude/commands/news-pipeline-steps.md（2026-09-13 起為 .claude/skills/ 下四個 pipeline skill）的歷史敘事，不是待執行規則；條文處的「沿革檔 YYYY-MM-DD[ 字母]」皆指本檔對應段。考古鏈：`[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

本檔是**歷史敘事，不是待執行步驟**——步驟已在上方，執行 pipeline 時不必讀本檔。存放於此的原因：步驟本身已能獨立執行，敘事只在有人想問「為什麼有這條」時才需要。考古鏈為 `[加入: 日期]` → 本檔 → `wiki/log.md` 同日 Query 條目。

## 2026-09-12

**日報改版「乙」：讀者版從「今天發生什麼」改成「今天 wiki 學到什麼」**（`Step 2b：讀者版日報` 的立法依據）。

使用者裁決原文：

> 為什麼改：使用者讀日報的感受是「商業太多」。實測 09-02～09-11 十天：📰 媒體報導日均 6.7 條，🔧 官方技術更新日均 2.0 條，前者是後者 3.3 倍。但病因不是跑題，是同一事件被重複計算：09-11 媒體區 8 條裡 7 條是同一份威脅情報報告的不同媒體覆述，而今日聚焦第一條已經講完了。爬蟲 dedup 只合併「同一則」，合併不了「同一事件不同角度」。根本原因：現在的日報回答的是新聞聚合器的問題（今天發生了什麼），但這個專案已經是 LLM wiki，讀者版該回答「知識庫今天學到什麼、改變了什麼判斷」。媒體覆述之所以不進 wiki，正因為沒有新資訊——沉澱過濾和商業過濾在這裡是同一件事。日報的「原料」職能其實早已被 gathered_items.json 接走（記者規則「不收可以，沒看過不行」，派工數常多於日報條數），所以改讀者版不會反轉資料流。collection-scope.md 的第三類讀者「Anthropic 生態追蹤者：關注政策、融資、合作動態」是媒體區膨脹的合法依據，只要它還在，任何選材規則都擋不住「對生態追蹤者有價值」的辯護。
>
> 決策：產出時機從 Step 1b（ingest 前）搬到 ingest 後、build_web 前；來源是 wiki 的 git diff，不靠歸因記錄。每條格式：一句新事實 → [[頁名]] → 改變了什麼判斷；分區改按 wiki 六領域（功能／模型／商業／安全政策／社群／人物），不再按來源分區。原本 news/YYYY-MM-DD.md 照產照存，供原料與 lint 溯源（5d、7b），但不再上站；web_reader 日報改讀新讀者版。collection-scope.md「生態追蹤者」降級為條件收錄：政策／融資／合作只在會改變工程師決策時收（定價、可用性、法規強制、供應商鎖定）。已知取捨：記者當天漏收的東西讀者版看不到，靠每週 lint 補抓。這是刻意放棄「先攤出來給人看」那層保險，因為那層正是噪音來源。

**已知取捨（使用者明示接受）：** 記者當天漏收的東西，讀者版看不到——舊版「先把抓到的攤出來給人看」那層保險刻意放棄，因為那層正是噪音來源。補救靠每週 lint 補抓，而非把噪音留在讀者面前。

**為什麼 Step 1b 一字不動：** 爆炸半徑刻意壓到最小。Step 1b 的機械契約字串表、📌📡 區塊 emoji 看守、`.claude/review-registry.json` 既有 sync_pair、`test_digest_contract.py`／`test_focus_inline_links.py` 全數保留並繼續有效——`news/*.md` 仍是原料層，它壞掉會讓 lint 5d／7b 溯源與各記者沉澱一起斷。讀者版是**新加一層**，不是改寫舊層。

**為什麼 digest JSON 仍保留新聞欄位：** `web_reader/data/digest/*.json` 有三個內部消費端——`/wiki-lint` 6e 讀 `sourceStatus` 做來源健康檢查、`/pipeline-change-check` 讀各區塊條目數與 body 比率當解析健康 proxy、`scripts/daily_health_check.py` 驗該檔存在。「不再上站」是**呈現層**的承諾（`app.js` 有 `reader` 欄就整頁改渲染讀者版，新聞條目一個都不畫、搜尋索引也只收讀者版文字），不是把量測面板一起拆掉。

**為什麼退回而不是一次換掉：** 改版日之前的 137 份日報沒有讀者版，`build_web.py` 對沒有 `daily/<date>.md` 的日期照舊解析 `news/`、`app.js` 照舊渲染新聞式版面。歷史頁不可壞，而「新舊並存」在這裡不需要額外旗標——`reader` 欄在不在就是那個旗標。

**為什麼 💰 注入改成擇一：** `attach_market_signal()` 原本會在最新判讀日期等於某日日報時，於該日日報頁注入一則 💰 條目。讀者版的 `## 💼 商業` 節本來就會寫到 market-signals 的當日改動（它是 wiki diff 的一部分），兩邊都留就是同一件事出現兩次。做法：有讀者版的日期不注入，注入路徑只服務歷史頁。`MARKET_SIGNAL_RE` 與其 registry sync_pair 一字不動。

**乙-2（同日晚間）：今日聚焦與重點話題回到讀者版頂部。** 使用者看過首份讀者版樣本後的原話：「我發現我還是喜歡今日聚焦、重點話題」，另加一句「有些沒必要出現在頁面的字就不用出現」。判斷：改版乙的病灶是 📰 媒體報導把同一事件覆述七次，不是聚焦那 3–5 條——聚焦是舊格式裡校準最久、規則最嚴的一節（30 天存活率追蹤、防重複、行內連結）；而首份「學到什麼」樣本記的是拆頁、汰表這類知識庫自身的整理，讀起來像維護日誌，不像今天發生了什麼。做法：讀者版日期在網站上先畫 news/ 解析出的 focus 與前 5 則 topStories，再接六領域；技術更新／付費／媒體／討論仍不畫；搜尋索引跟著收聚焦文字與那 5 則標題。「沒必要的字」落實為：讀者版日期不畫來源標籤（`HN Repo Bridge` 這類內部來源名）、UTC 抓取時間、情緒符號，頁首也不印來源數與產生時間。`daily/*.md` 契約與 Step 2b 產出一字未動——聚焦不必抄進讀者版檔，`build_web.py` 兩邊資料本來就都有。歷史頁（無 reader 欄）渲染不變。


## 2026-09-13

**步驟檔拆成四個 skill。** .claude/commands/news-pipeline-steps.md（626 行）刪除，不留轉址殼；步驟語意搬進 `.claude/skills/`，格式與判準抽成 skill 同目錄的 reference。本檔續為那四份 skill 的共同沿革檔（標題保留舊路徑，供考古鏈 `[加入: 日期]` 對得上）。

使用者原則（原話）：

> 「SKILL 負責步驟。格式應該要放在 REFERENCE／RULE。」
> 「這個 SKILL 會用到的 DOC 盡量放到跟 SKILL 一樣的地方。」

以及：校準史、立法理由、`[加入: …]`／`[改版: …]` 的來龍去脈進本檔，skill 與 reference 正文不留敘事；每個事實只有一個家，拆完後只能存在一處，其他地方用一句路徑指過去。

**新舊對照：**

| 原檔的節 | 新家 |
|---|---|
| 檔首說明（兩個背景 agent 分讀、Step 2 不可包進背景 agent） | `.claude/commands/news-pipeline.md`；「Step 2 不在本檔案」一句在 `.claude/skills/news-gather/SKILL.md` |
| `## 設定`（REPO_ROOT／PYTHON／模型／TARGET_DATE） | `.claude/commands/news-pipeline.md` 的兩段 Agent prompt（單一家，skill 端只寫「由派工 prompt 傳入」） |
| `# Phase A 步驟`／`# Phase C 步驟` 標題 | `.claude/commands/news-pipeline.md` 的 `## Phase A 步驟：`／`## Phase C 步驟：` |
| `## 本機與雲端的行為必須一致` | `.claude/skills/news-gather/SKILL.md` |
| `## Step 0`／`## Step 0b`／`## Step 1a`＋`### 補跑（backfill）注意事項`／`## Step 1c`／`## Step 2（不在本檔案）` | `.claude/skills/news-gather/SKILL.md` |
| `## Step 1b：生成日報` 的步驟（0-1／0-2／讀料／寫入／3a／3a-2／3b／3d／3e／3f／3g／commit） | `.claude/skills/news-digest/SKILL.md` |
| Step 1b 的「機械契約字串」表、輸出骨架、每條排版格式、檔尾兩行說明、📡 來源狀態表、System 語氣句 | `.claude/skills/news-digest/format.md` |
| Step 1b 的聚焦四標籤門檻、行內連結格式、重點話題三條准入、各區塊收錄條件（含 🧭 專頁雷達與廠商發布判準）、存量盤點寫法、聚焦防重複、分層原則、3a-2 禁詞清單 | `.claude/skills/news-digest/selection.md` |
| `## Step 2b：讀者版日報` 的步驟（取 diff／寫檔／`check_reader_digest.py`／內規外洩自檢／產出失敗退回） | `.claude/skills/reader-digest/SKILL.md` |
| Step 2b 的「機械契約字串」表、模板、每條 ≤200 字元等格式條件、「不算學到」清單、主詞規則、網站版面 | `.claude/skills/reader-digest/format.md` |
| `## Step 3`／`## Step 4`＋`### gate 擋下時的修復迴圈`／`## Step 5`／`## Step 6`／`## 完成摘要`＋`### 📋 待使用者裁示` | `.claude/skills/web-publish/SKILL.md` |
| `## 注意事項` | 逐條分進 news-gather 與 web-publish 的「本 skill 的邊界」節；Phase 劃分那一條回 `.claude/commands/news-pipeline.md` |

**本次自條文搬進本檔的教訓敘事（正文只留判準句）：**

- 「2026-07-25 與 2026-09-03 都發生過規則被原樣印進日報」——原在 Step 1b 輸出結構的開頭警語（現 `.claude/skills/news-digest/selection.md` 檔首）。
- 「校準顯示此類條目 30 天存活率 0/9」（[新工具]）、「2026-08-01 校準顯示此類條目 30 天後續產出 0/2」（[持續追蹤]）、「2026-09-06 校準：此型 30 天存活率 0/2，樣本偏薄，下輪校準複核」（[社群趨勢]）——原在 Step 1b 聚焦選材門檻四條（現 `.claude/skills/news-digest/selection.md`「📌 今日聚焦」，只留判準句＋一行指回本檔）。
- 「冷讀者實測：抓取時刻的來源行時間戳讓最沒新聞性的條目看起來最新鮮」「2026-09-04 冷讀者實測」（星數千分位）——原在 Step 1b 存量盤點條目的寫法（現 `.claude/skills/news-digest/selection.md`）。
- 「2026-08-02 提出的 feature-radar 防霸榜裁示因此擱置 6 天」——原在完成摘要「📋 待使用者裁示」（現 `.claude/skills/web-publish/SKILL.md`，改指「起因見沿革檔 2026-08-08」）。
- 「2026-09-05 弄丟三位記者的成品」——原在 Step 5 的 `git stash` 禁令（現 `.claude/skills/web-publish/SKILL.md`，教訓仍指 `.claude/reporter-rules/wiki-reporter-shared.md`）。

**registry 同步：** `.claude/review-registry.json` 原 25 組指向舊檔的 sync_pair 逐組換家；其中三組原本靠「所有 pattern 都住同一檔」成立，拆檔後依 pattern 所在 skill 分組——步驟標題錨點對 runbook 那組分成四組、本機／雲端一致那組分成三組、Phase 劃分那組分成三組，pattern 逐字不動。wiki-lint 6g 指路的檔名 pattern 改指 `.claude/skills/news-digest/selection.md`；bare_references 的舊檔 line_allowlist 條目失效刪除（該檔本來就沒有裸露的根目錄規則檔引用）。


**2026-07-25 A**（本機／雲端行為一致）：冪等閘、push 重試最初只寫進雲端 runbook，等於本機跑同一條 pipeline 卻少了兩道保護。

**2026-07-24**（Step 1c 漏做的後果）：2026-07-14～07-24 雲端自動化期間，每日確認率幾乎為 0（僅本機手動執行的 07-19、07-22 為 100%），兩階段確認機制形同空轉，跨日去重完全靠 `seen_urls.json` 獨撐。

**2026-07-31**（web build gate 的由來）：舊規則是「整包測試過才建 web」。當日雲端日更因 3 個抓料端的 `ModuleNotFoundError` 判定失敗而跳過 build，網站整天停在前一天——但日報與 wiki 都已正常產出並 commit，那 3 個案例跟 `build_web.py` 的輸入毫無關係。

**2026-08-15**（多來源條目的來源欄）：記者依日報來源欄做歸因、`data/source_attribution.jsonl` 再餵 `scripts/source_scorecard.py` 的 wiki 率，於是低流量官方來源（幾乎必定輸給 HN／Google News）長期看起來零貢獻——當日 Anthropic Blog 供了最大條的浮水印報導，掛名全歸 HN。

**2026-08-26**（gate 擋下時的修復迴圈）：wiki 懸置探針含千分位逗號 `$1,125` 被切成 `$1` 而 FAIL，日報與 wiki 全部正常，網站卻停更一天，瑕疵本身也沒人修。

**2026-09-02**（append-only 衝突自動解）：雲端 17:00 UTC 班完整跑完日報＋wiki＋web，push 撞上本機同時間的 commit，衝突檔只有 `wiki/log.md`（兩側各自 append 段落，無語意衝突），依舊規則放棄整輪，22:00 班重做一遍。
