# 讀者版日報（`daily/YYYY-MM-DD.md`）格式契約

`.claude/skills/reader-digest/SKILL.md`（Step 2b）的格式單一來源。檔案由 `scripts/build_reader_digest.py` 產生，本表描述的是它的輸出形狀與挑選規則，人不手寫 `daily/`。

## 機械契約字串（勿改；新增時登記 `.claude/review-registry.json`）

**script 會 grep 的字串只住這張表**，規則引用時指回本表、不另抄。改任何一格必須同步右欄消費端。

| 契約字串／形狀 | 產出端 | 消費端 | 改壞的後果 |
|---|---|---|---|
| 標題 `# YYYY-MM-DD 今天 wiki 學到什麼` | `build_reader_digest.py` TITLE_FMT | `build_web.py` READER_TITLE_RE、`check_reader_digest.py` TITLE_RE | 標題行不被認得（日期仍取檔名，不致命）|
| 無新知行 `> 今日 wiki 無新知（YYYY-MM-DD）` | NO_NEWS_FMT | `build_web.py` READER_NO_NEWS_RE | 空日會被當成「有內容但解不出來」，網站出空頁 |
| 六個領域節名 `## 🛠️ 功能`／`## 🤖 模型`／`## 💼 商業`／`## 🏛️ 安全政策`／`## 🌐 社群`／`## 👤 人物` | DOMAIN_TO_SECTION | `build_web.py` READER_DOMAIN_SECTIONS、`check_reader_digest.py` DOMAIN_LABELS、`app.js` readerDigestHtml | 該領域整段靜默消失（同 2026-08-14 區塊 emoji 的死法）|
| 頁面小節 `### [[頁名|頁面標題]]`（一頁一節，別名＝頁面 H1）| PAGE_HEADING_FMT | `build_web.py` READER_PAGE_RE、`check_reader_digest.py` PAGE_RE | 該頁的 callout 變成散落的 `>` 行，不上站 |
| 頂部兩節 `## 📌 今日聚焦`／`## ⭐ 重點話題` | FOCUS_SECTION／TOP_SECTION（從 `news/TARGET_DATE.md` 的 `### 📌 今日聚焦`／`### ⭐ 重點話題` 搬） | `build_web.py` READER_PASSTHROUGH_SECTIONS（認得但不收，網站資料取自 news/ 解析）、`check_reader_digest.py` PASSTHROUGH_LABELS | 格式閘把它們當成「不在六領域內」而報錯 |
| callout 首行：wiki 頁上 `> **標籤**（YYYY-MM-DD）`，日報裡剝成 `> **標籤**`（日期是挑選鍵不是內容，檔名已是那一天；`（日期，尾巴）` 只留尾巴）| wiki 頁頂原文 → `build_reader_digest.py` strip_callout_date；形狀規則在 `.claude/reporter-rules/page-templates.md`「頂部 delta-first callout」 | `build_reader_digest.py` CALLOUT_RE、`build_web.py` READER_CALLOUT_RE、`check_reader_digest.py` CALLOUT_RE、`scripts/check_hierarchy.py` CALLOUT_DATE_RE | 該頁永遠不會被挑進讀者版；網站上標籤與日期空白 |

---

## 挑選規則（產生器實作，這裡是規格）

- **來源**：`wiki/entities/*.md`、`wiki/topics/*.md` 的頁首（H1 到第一條 `---` 之間）。分隔線之後的引述不算。
- **收哪些**：頁首裡每一段 `>` 引述區塊，首行符合 callout 首行形狀且括號日期＝TARGET_DATE 的，整段照抄。同一頁多段都符合就都收；沒日期的（如 ⚠️ 免責、❓ 待查證）不收。
- **該收的頁有沒有漏**：產生器只看得到有當日 callout 的頁。標頭「最後新聞更新」＝TARGET_DATE 卻沒有當日 callout 的頁，由 `scripts/check_callout_coverage.py` 在產出前點名，產生器產出時也會把同一份結果印成 WARN（判定與豁免表住 `build_reader_digest.py` 的 `coverage_gaps`，豁免僅限機器整頁覆寫的頁）。
- **標籤與內容自由**：最新動態／最新判讀／本週衝擊／這頁在回答什麼……都是合法標籤；內容是條列或散文、幾行、有沒有 wikilink，由各頁記者依該頁的重點決定，產生器與格式閘一字不查。
- **分節**：依頁面 frontmatter `domain`（wiki 標頭「領域」欄同源）對到六個節名；`domain` 缺或不在六領域者不收並 WARN。
- **節內順序**：frontmatter `inbound_links` 高者在前，同分按路徑。
- **沒有內容的領域整節省略**，不寫空節也不寫「本日無」；六節全空時整份檔只寫標題加無新知行，不拿舊料充數。
- **不寫總結句**：讀者版頂部已有 Step 1b 的今日聚焦。網站卡片的 preview 由 `build_web.py` 取第一頁的頁名＋callout 首句。
- **頂部兩節**：`news/TARGET_DATE.md` 存在時，📌 今日聚焦的條列行原樣搬到標題下；⭐ 重點話題只留 URL 不在聚焦行內連結裡的（聚焦已講過的不重複），去掉來源行，最多 5 則，剔完零則整節省略。`news/` 不存在（如補跑歷史日期）就兩節都省略。
- **聚焦漏收 WARN**：聚焦每條的來源 URL 既不在 `data/source_attribution.jsonl` 當日歸因、也沒出現在任何今日覆寫 callout 的頁正文 → 產生器印 WARN 點名該條，這是乙版放棄的「記者漏收」保險的機械版；WARN 不阻斷，抄進完成摘要給人判斷。

## 模板（產生器輸出）

```markdown
# TARGET_DATE 今天 wiki 學到什麼

## 📌 今日聚焦

- **[重大事件]** ……（news/ 原文，含行內來源連結）

## ⭐ 重點話題

**[標題](URL)**
一句摘要（news/ 原文；來源行不搬）

## 🛠️ 功能

### [[entities/claude-code|Claude Code]]

> **最新動態**
> - **v2.1.268**：……（callout 原文，只剝掉首行日期）

## 🏛️ 安全政策

### [[topics/ai-agent-safety|AI Agent 安全與可靠性]]

> **最新安全事件**
> ……
```

## 網站上讀者版日期的版面

頂部先畫 Step 1b 產出的 **📌 今日聚焦**與 **⭐ 重點話題**（剔掉 URL 已在聚焦裡的，前 5 則，`build_web.py` reader_top_stories 算好放 `readerTopStories`；不畫來源標籤、抓取時間、情緒符號），再接本步的六領域「知識庫今天學到什麼」：每頁一條，頁面按鈕＋標籤與日期＋callout 原文（markdown 渲染，wikilink 變按鈕）。技術更新／付費方案／媒體報導／技術熱度討論這些區塊不上站。**市場記者的 💰 判讀**就是 `topics/market-signals` 頁頂的當日 callout，會自然落在 `## 💼 商業`；有讀者版的日期 `build_web.py` 不再另外注入 💰 條目。
