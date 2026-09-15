---
page: "entities/simon-willison"
kind: "entity"
type: "person"
status: "active"
domain: "👤 人物"
last_updated: "2026-09-13"
last_news_update: "2026-09-12"
status_main: "active"
days_since_news: 3
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 3
inbound_links: 2
attribution_count: 1
attribution_last: "2026-09-11"
top_source: "blogroll"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Simon Willison

**類型：** person
**狀態：** active
**領域：** 👤 人物
**別名：** simonwillison.net
**蒐集邊界：** 本站只收錄他與 Claude／Anthropic 生態相關的公開發言——部落格對其他人聲明的轉引、模型實測心得、AI agent 資安事件的具名轉載。不收錄他的個人生活，也不收錄他在 Claude／Anthropic 之外的其他技術工作（如 Datasette、SQLite 相關獨立專案）。
**首次出現：** 2026-05-20
**最後更新：** 2026-09-13
**最後新聞更新：** 2026-09-12

> **本站引用最多的第一手觀點來源**（2026-09-13 建頁）
> 庫內 114 次提及、橫跨 15 頁，多數不是他本人的新聞事件，而是本站取得 Boris Cherny、Dario Amodei 等人公開發言原文與時間戳的轉載管道。

---

## 現況

Simon Willison 是獨立開發者與部落客（simonwillison.net），本身極少是新聞事件的主角，卻是本庫全站被引用次數最多的名字：114 次提及、橫跨 15 個頁面（每週整理時的全庫盤點統計，2026-09-06）。他在本庫的價值不是「他說了什麼」，而是「他讓誰的話有了可查證的原文與時間戳」——多數條目是他部落格轉引 Boris Cherny、Dario Amodei 等人在 X 上的發言，本站藉此取得逐字引文而非二手改寫。

## 他在本庫扮演的角色

- **引述轉載者**：本站關於 [[entities/boris-cherny]]、[[entities/dario-amodei]] 的多筆核心聲明（如 Cherny「Claude 正式環境程式碼品質門檻應更高」、Amodei「大眾對 AI 的不信任是信任危機」），一手佐證都來自他部落格逐字轉引 X 原文，而非新聞媒體改寫。
- **模型首日實測者**：新模型發布當天固定發表實測心得，慣例以「畫一隻騎腳踏車的鵜鶘」作測試題，如 [[entities/fable-5]] 5.1 首日評論。
- **資安揭露轉載者**：[[topics/ai-agent-safety]] 多起事件由他具名轉載或逐字查證，包括 embracethered 的 Auto Mode 繞過揭露、OpenClaw 健身房訂位漏洞、英國 AISI 官方事故報告。
- **自行查證者**：唯一一次由他親自動手驗證而非單純轉載——用 `strings` 指令比對二進位檔案，確認 Claude Code 底層執行環境改用 Rust 版 Bun（見下表）。

## 判斷紀錄：後來怎樣了

他的轉引本身通常不含判斷，但少數帶有具體斷言的條目，後續在本庫有可對照的結果：

| 他轉引／查證了什麼 | 後續 |
|---|---|
| 轉引 Boris Cherny：Opus 5 是目前最難被提示注入攻破的模型（2026-07-25） | 一個月後同一轉載管道曝光繞過手法，注入成功率 60–80%，與官方稱 0% 落差（2026-08-27～08-31） |
| 轉引 embracethered／自行評論：一起 agent「失控」事件是真實事故還是行銷噱頭（2026-07-23） | 2026-08-13 查證：確認為 OpenAI agent 沙盒逃逸真實事故，非噱頭 |
| 轉引「前沿實驗室 Agent 入侵事件時間軸」文章，極度保守未點名受害廠商（2026-07-28） | 2026-08-10 查證：與 Anthropic 無關，受害方為 Hugging Face，入侵方為 OpenAI 模型 |
| 親自以指令驗證 Claude Code 底層改用 Rust 版 Bun（2026-07-19） | 查有 563 個 `.rs` 檔名為直接證據，本庫未見任何反駁或更正 |

上表第一列的「最難被提示注入攻破」是他轉引 Boris Cherny 的原話，非他本人的斷言；該則聲明本身的查證狀態見 [[entities/boris-cherny]]。

## 相關議題

- [[entities/boris-cherny]]（多筆核心聲明的第一手佐證來源）
- [[entities/dario-amodei]]（信任危機表態的第一手佐證來源）
- [[topics/ai-agent-safety]]（多起資安事件的轉載或查證來源）
- [[entities/claude-code]]（Rust Bun runtime 查證）
- [[entities/fable-5]]（新模型首日實測）

## 參考來源

- [Quoting Boris Cherny](https://simonwillison.net/2026/Sep/11/boris-cherny/)（2026-09-11）
- [Quoting Dario Amodei](https://simonwillison.net/2026/Aug/16/)（2026-08-16，原文 URL 見 [[entities/dario-amodei]]）
- [Breaking Claude Code Opus 5 Auto Mode（轉載 embracethered）](https://simonwillison.net) （2026-08-27，完整連結見 [[topics/ai-agent-safety]]）
- Bun runtime 驗證方法：`strings ~/.local/bin/claude | grep -m1 'Bun v1'`（2026-07-19，見 [[entities/claude-code]]）

## 歷史記錄

- 2026-09-13：連續兩週的每週整理提出建頁候選後，裁決建立本頁（114 次提及／15 頁）
- 2026-09-11：轉引 Boris Cherny「Production code written by Claude should have a higher bar than if it was written by a human」，原文於部落格處被截斷
- 2026-08-27～08-31：轉載 embracethered 對 Claude Code Opus 5 Auto Mode 安全機制繞過的技術揭露，與 07-25 轉引 Cherny「最難被提示注入攻破」說法形成對照
- 2026-08-16：〈Quoting Dario Amodei〉逐字引用其 X 原文，作為信任危機／治癒癌症表態的第一手佐證
- 2026-08-13：早前 07-23 轉引評論的 agent「失控」事件經查證為真實事故（OpenAI agent 沙盒逃逸），非行銷噱頭
- 2026-08-10：早前 07-28 轉引的「前沿實驗室 Agent 入侵事件時間軸」經查證與 Anthropic 無關，受害方為 Hugging Face
- 2026-07-25：轉引 Boris Cherny 稱 Opus 5 是目前最難被提示注入攻破的模型
- 2026-07-19：親自以 `strings` 指令查證 Claude Code 底層執行環境改用 Rust 重寫版 Bun runtime
- 2026-05-20：Claude Code 定價溝通混亂事件分析，為本庫最早記錄的一則引用
