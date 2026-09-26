# Wiki Ingest — 模型記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/models/pages.md`。

分類為「模型」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/entities/fable-5.md` | Fable 5／5.1 世代動態、護欄與分類器行為、Legacy 與退役時程。**出口管制的政策面不在本頁**（家是 [[topics/anthropic-government-policy]]，屬安全政策線），本頁只在現況留一句指路 |
| `wiki/entities/opus-4-8.md` | Opus 4.8 能力更新、評測新資料 |
| `wiki/entities/opus-4-7.md` | Opus 4.7 後續、思考深度議題 |
| `wiki/entities/mythos.md` | Mythos 漏洞更新、安全模型動態 |
| `wiki/entities/sonnet-5.md` | Sonnet 5 動態、評測、預設模型變化 |
| `wiki/entities/opus-5.md` | Opus 5 世代動態、官方基準與社群實測的對照、Legacy 與退役時程。**跨家分數不在本頁**（家是 [[topics/model-task-leaderboard]]），本頁只留一句結論與出口 |
| `wiki/topics/model-comparison.md` | 任一模型發布/下線/狀態/定價/預設變更（見下方「選型對照同步」）|

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🤖 模型 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

> **`wiki/topics/model-task-leaderboard.md` 例外**：此頁為跨家榜單週快照，吃外部榜單網站而非新聞條目，由 `/wiki-lint` 步驟 5b（主編派 Haiku 抓取）維護；每日 ingest **不更新**此頁，模型記者僅在 lint 時做呈現品質檢查、不自行抓榜（記者無 web 工具）。

> `wiki/entities/pricing.md` 由**商業記者主責**（見 `.claude/reporter-rules/commercial/daily.md`）。模型記者遇模型定價時，將定價細節留給商業記者，僅在模型頁記能力並加 wikilink 至 pricing。

新模型發布時，依 `.claude/reporter-rules/page-templates.md` 建立新 entities/ 頁。

---

## 更新規則

**模型頁基本欄位：** 每次更新必須同步「最後更新」日期。若狀態改變（如 `beta` → `active`），標記回報讓主編同步 `wiki/index.md`。

**評測數據：** 優先記錄官方或三方確認來源，補注測試日期。若有相互矛盾的評測結果，保留兩者並標注來源。

**版本號：** 模型版本號視為元資訊（`entities/` 標頭），不另建頁面。若版本迭代有重大能力差異，加入 `## 歷史記錄` 條目。

**定價歸屬：** 模型本身（能力、評測）進模型頁；定價細節進 `wiki/entities/pricing.md`（**商業記者主責**，模型記者不直接維護該頁）。同一事件有兩面向時，模型記者記能力面、商業記者記定價面，互相加 wikilink。

**prompt 特性同步：** 新模型發布、或日報條目帶到官方 prompting／migration 指南更新時，更新該模型頁 `## 跟它怎麼說話`（契約見 `.claude/reporter-rules/models/pages.md`「各現行模型頁共用」節）；同批打開被取代那一代的頁，有相反傾向的句子兩頁互指。日報沒帶官方內容就留待查證行並回報主編，不自填。

**選型對照同步：** `wiki/topics/model-comparison.md` 是「我該用哪個模型」的單一入口。任一模型發布/下線/狀態/定價/Claude Code 預設變更時，除更新該模型頁外，**必須同步更新對照頁的快速選型表與情境推薦**；深度細節仍留在各模型頁，對照頁只放一行式結論。此項納入回報的「同步自查」欄。

**日期類事實尤其容易漏：** 免費期限、促銷截止日這類「會員疊延長」的日期，往往同時寫在模型頁的「現況」段落＋模型頁自己的子標題/內文＋`model-comparison.md` 快速選型表三處以上。單純判斷「陣容/定位未變」不足以跳過同步——**只要有舊日期字串（如 7/7、7/12）殘留在任何一處描述「當前」或「即將」的句子裡，就必須視為需要同步**，不能只更新歷史記錄新條目就結案。修改前對舊日期字串在該模型頁全文 + `model-comparison.md` 各 grep 一次。

---

## feature-radar 判斷

新模型發布 = 使用者可 `--model` 選用 → **須回報主編新增 feature-radar 條目**。

純模型評測論文或研究報告（無可用介面）→ **不進 feature-radar**，記於模型頁即可。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄，本記者無專屬欄位差異；`feature-radar 新增` 欄填條目標題或「無」。
