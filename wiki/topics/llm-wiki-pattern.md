---
page: "topics/llm-wiki-pattern"
kind: "topic"
status: "ongoing"
domain: "🌐 社群"
last_updated: "2026-09-19"
last_news_update: "2026-09-14"
status_main: "ongoing"
days_since_news: 4
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 4
inbound_links: 2
attribution_count: 7
attribution_last: "2026-09-14"
top_source: "user-query"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Karpathy 式 LLM wiki 模式

**狀態：** ongoing
**領域：** 🌐 社群
**別名：** LLM Wiki, Karpathy wiki
**蒐集邊界：** 本頁的事實來自逐筆查證過的一手來源，加上 [[topics/skill-interest-watch]]「LLM 知識庫／文件策展／知識傳承」類的每日 GitHub 星數快照；不談 Claude 的 LLM wiki 專案，若既沒進那份榜、也沒被社群討論引用，本頁就會漏掉。
**開始日期：** 2026-09-12
**最後更新：** 2026-09-19
**最後新聞更新：** 2026-09-14

> **最新動態**（2026-09-14）
> Karpathy 四月提出的三層 wiki 模式已長出六種公開實作，最新一種是打包成可安裝 skill 的 Astro-Han/karpathy-llm-wiki（2.2k 星）；本庫對照三層骨架與三個動作齊備——查詢層 `/wiki-query` 已於 09-12 補上，仍缺機器可讀的查證日與信心欄位。

---

## 摘要

Karpathy 於 2026-04 提出的三層 wiki 模式，五個月內長出至少六種路線互異的公開實作，從個人生產版到可安裝的通用 skill。本頁把那些實作的設計並排，再拿本庫自己對一次。對照結果：三層骨架與三個動作本庫全有，甚至多數更嚴；查詢原本沒有自己的流程，2026-09-12 已補上 `/wiki-query`（六路分流、答案契約、答案回流），現在真正缺的是頁面沒有機器讀得懂的查證日與信心欄位。

## 這個模式長什麼樣

三層：**raw 不可改**（原始資料照原樣留著）／**wiki 由 LLM 生成**（摘要、實體頁、交叉引用、矛盾標記）／**schema 是一份規則檔**（告訴模型頁面該長什麼樣）。三個動作：**寫入**（把新資料吃進 wiki）／**查詢**（從 wiki 拿答案）／**整理**（修矛盾、孤兒、過期）。Karpathy 原文的一句話是「wiki 是產品，chat 只是介面」（2026-09-12 查證）。

| 要素 | Karpathy 原始（2026-04） | 生產版常見延伸 |
|---|---|---|
| 原始資料 | 人工投遞檔案，投進去就不再改 | 換成即時資料源：對話紀錄、diff、PR、URL 自動進料 |
| wiki 頁面 | LLM 生成摘要、實體頁、交叉引用、矛盾標記 | 每頁加短 TL;DR、frontmatter 欄位、標明關係的連結 |
| schema | 一份規則檔講清楚頁面格式 | 規則之外再加 hook 強制與指令路由，不靠臨場提示 |
| 三個動作 | 全部手動貼 prompt，機制未具體化 | 各自變成 slash 指令，並掛上每夜／每週排程 |

三層之中最容易被跳過的是第三個動作：整理沒做，孤兒頁與沒標的矛盾會累積（見下方實錄）。

## 外面的實作

七種路線各挑一個最有辨識度的設計，細節與出處一起放（除註明者外皆 2026-09-12 查證）：

- **Karpathy 原始模式**（2026-04 一則 X 貼文＋一份 gist，數日內 5,000+ 星）：規則檔當 schema；三層與三動作都在，但動作全是手動貼 prompt，沒有機制。整理版本見 [Karpathy's pattern for an LLM wiki in production](https://aaronfulkerson.com/2026/04/12/karpathys-pattern-for-an-llm-wiki-in-production/)。
- **Fulkerson 生產版**（個人生產環境）：學習迴路有「畢業」機制，規則穩定後就從提示裡移出；另四處延伸是即時資料源取代檔案投遞、指令路由取代臨場 prompt、hook 強制、工作流副作用自動增益。作者回頭對照原始 gist 才發現自己缺全庫整理、目錄、活動 log、來源溯源（同上連結）。
- **Ghelbur 重建版**（個人重建＋排程）：排程 agent 的改動先寫成當日 diff，24 小時後才生效；新事實寫在最上方、舊的留著，矛盾依來源新舊／權威／信心自動調和，會自己長出沒人要求的綜合頁；31 個 slash 指令、每夜與每週排程（[I rebuilt Karpathy's LLM wiki](https://theaioperator.io/p/i-rebuilt-karpathys-llm-wiki-heres)）。
- **Jim Liu 六個月實錄**（35 頁／80 篇來源，每日 15 分鐘，每次寫入中位數動 9 檔、範圍 4–23）：每頁 50 字 TL;DR，實測比讀目錄更省 context；500 頁以下 grep 比混合搜尋快，35 頁時把 Postgres 拿掉（[六個月實錄](https://www.openaitoolshub.org/en/blog/karpathy-llm-wiki)）。
  - 採用 `last_verified`、`confidence` 與帶關係詞的連結（如 `(uses)`）。
  - 四個失敗：跳過整理累積孤兒與沒標的矛盾、過度潤飾原文（改用 `do-not-rewrite` 標籤）、蓋掉矛盾丟失歷史（改成 `contradicts:` 並存）、搬家時 schema 漂移長出重複頁。
- **CodeAlmanac**（開源工具，YC S26）：`garden` 指令修過期、斷鏈、重複、無據主張，沒事可修也是合法結果（[GitHub](https://github.com/AlmanacCode/codealmanac/)）。
  - 從 Claude／Codex 對話紀錄與 diff、PR、URL 增量寫入，`topics.yaml` 組織主題，附本地 web 檢視器；本庫 2026-07-22 曾收過此工具，見 [[topics/community-pattern-trends]] 趨勢九。
- **wuphf**（開源工具，多 agent 共腦）：每個主張都帶「哪個 bot、何時、哪個來源」的出處 metadata，沒有出處的主張直接觸發警告；跨 bot 矛盾靠信心分數與時間戳調和（[GitHub](https://github.com/nex-crm/wuphf)）。
- **Astro-Han/karpathy-llm-wiki**（可安裝的 Agent Skill，2,218 星／261 fork，MIT；2026-09-13 查證）：一行 `npx add-skill Astro-Han/karpathy-llm-wiki` 裝進支援 Agent Skills 的工具（[GitHub](https://github.com/Astro-Han/karpathy-llm-wiki)）。
  - `raw/`／`wiki/`／`index.md`／`log.md` 四件套與 Ingest／Query／Lint 三動作都是通用指令；作者自己的 wiki 從 2026-04 維護至今 94 頁／99 個來源。
  - 與前六者的差別是它不是某個人的 wiki，而是任何人拿來起自己 wiki 的殼；README 把自己對比 RAG，知識在寫入時合成而非每次查詢重推。本庫 09-12 的 skill-interest-watch 探針即由它命中，見 [[topics/skill-interest-watch]]。

這一類現在誰大、誰在漲，本頁不抄榜——見 [[topics/skill-interest-watch]] 的「LLM 知識庫／文件策展／知識傳承」類每日快照。

## CLAUDE_NEWS 對照起來

**已經有的**

- **原始資料不可改**：每日日報為唯讀原料，寫進 wiki 後不回頭改它（`news/`）。
- **schema**：頁面格式與書寫上限寫成規則檔，不靠臨場提示（`.claude/` 與 `wiki/CLAUDE.md`）。
- **寫入是一個動作**：每日六個領域各寫自己的頁，再統一整理共用檔案（`/news-pipeline`）。
- **排程**：每日更新與每週檢查都在雲端排程跑。
- **hook 強制**：危險指令與規則改動由 hook 擋，不靠自律（`.claude/hooks/`）。
- **活動 log**：只增不改的歷史，頁面清掉的判斷軌跡都在 [[log]]。
- **目錄**：一頁地圖，只放慢變的路由事實（[[index]]）。
- **來源溯源**：每筆新事實記下它來自哪一則來源，另存帳本（`data/source_attribution.jsonl`）。
- **矛盾與未定並陳**：懸置標記 ❓／🔎 自帶偵測條件，矛盾數字並列不擇一。
- **頁頂就是最新狀態**：頂部提示每次更新時重寫，歷史另有其家。
- **空手是合法結果**：當日無料就明寫「本日無候選」，不硬湊。
- **查詢是第一級動作，答案回流進頁面**：`/wiki-query` 依問題型態走六路（Grep／全文 BM25／標頭欄位／log／負責表／引用圖），答案附出處與「現在／當時」；wiki 沒有的事實查一手來源後寫回該頁並標查證日、[[log]] 記 Query 條目（2026-09-12 補上，對應 Ghelbur 的 31 個指令、Fulkerson 的指令路由）。

**還沒有的**

- **機器讀得懂的 `last_verified`／`confidence` 欄位**（Jim Liu、Ghelbur、wuphf）——值得評估：查證日現在寫在正文，機器數不出哪些頁已過期。
- **每次更新動了幾個檔的健康指標**（Jim Liu：中位數 9 檔，範圍 4–23）——值得：現在看得到頁面有沒有變，看不出變動幅度異不異常。

**刻意不做的三件**

- **向量搜尋**：Jim Liu 實測 500 頁以下 grep 更快，本庫 70 餘頁遠在那條線以下（2026-09-12 查證）。
  - 2026-09-14 補了一層**詞彙**檢索（`scripts/wiki_search.py`：BM25＋同義叢集＋wikilink 圖擴散一跳，零依賴）。BM25 是詞彙排序不是語意向量，這條界線沒有移動。
  - 加的理由不是 grep 慢，是挑候選的方式錯：第 2 路原本靠 `index.md` 一句摘要篩頁，摘要不含正文用詞就整頁看不見（問「agent 視覺化」，答案頁寫「可觀測性」，兩輪都答沒有）。
- **AI-first vault**：Ghelbur 的頁面是寫給模型讀的；本站讀者是人，網站與頁面刻意往相反方向調。
- **改動延後 24 小時生效**：Ghelbur 用它換可逆性，本庫的可逆性已經由 git 提供，再加一層只是延遲。

## 相關實體

- [[topics/community-tech-patterns]]——「記憶與知識管理」類的逐則實作條目
- [[topics/community-pattern-trends]]——趨勢九「跨 Session 記憶層／知識庫」的宏觀線
- [[topics/skill-interest-watch]]——這一類的每日規模快照
- [[topics/community-tech-tools]]——工具該不該裝的判斷

## 參考來源

- [Karpathy's pattern for an LLM wiki in production](https://aaronfulkerson.com/2026/04/12/karpathys-pattern-for-an-llm-wiki-in-production/)——原始模式整理＋Fulkerson 生產版五處延伸（2026-09-12 查證）
- [I rebuilt Karpathy's LLM wiki, here's what I learned](https://theaioperator.io/p/i-rebuilt-karpathys-llm-wiki-heres)——Ghelbur 重建版（2026-09-12 查證）
- [Karpathy LLM wiki 六個月實錄](https://www.openaitoolshub.org/en/blog/karpathy-llm-wiki)——Jim Liu 的量測與四個失敗（2026-09-12 查證）
- [AlmanacCode/codealmanac](https://github.com/AlmanacCode/codealmanac/)——增量寫入與 `garden` 指令（2026-09-12 查證）
- [nex-crm/wuphf](https://github.com/nex-crm/wuphf)——多 agent 共腦的出處 metadata（2026-09-12 查證）

## 時序

### 2026-09-14

- 補第七種路線 Astro-Han/karpathy-llm-wiki（使用者提問，查證其 README）：把模式打包成可安裝 Agent Skill，2.2k 星；本庫 09-12 探針早已命中但本頁未列。

### 2026-09-13

- 頁頂與摘要仍寫「缺的是查詢層」，與同頁「同日已補上 `/wiki-query`」自相矛盾（使用者指出）；改為查詢層已齊備，查詢條目從「還沒有的」移到「有的」。

### 2026-09-12

- 本頁建立：六個一手來源查證後並排四種公開實作，並完成本庫對照；同日補上查詢流程 `/wiki-query`。事實來自使用者提問後的查證，非當日日報。
