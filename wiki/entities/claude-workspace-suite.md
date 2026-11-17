---
page: "entities/claude-workspace-suite"
kind: "entity"
type: "feature"
status: "beta（Whiteboards、Sheets 為 beta；Claude Data 為正式版，認證查詢與即時分享仍 beta）"
domain: "🛠️ 工具/功能"
last_updated: "2026-11-15"
last_news_update: "2026-11-15"
status_main: "beta"
matrix_role: "功能"
days_since_news: 2
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 2
inbound_links: 11
attribution_count: 2
attribution_last: "2026-11-15"
top_source: "anthropic-official"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-11-29"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude 協作三件組（Whiteboards、Sheets、Data）

Anthropic 在 Claude 內建的三項團隊協作功能：共用白板、試算表與接資料的儀表板，2026-11 推出。

**類型：** feature
**狀態：** beta（Whiteboards、Sheets 為 beta；Claude Data 為正式版，認證查詢與即時分享仍 beta）
**領域：** 🛠️ 工具/功能
**對照角色：** 功能（產出物；含 Whiteboards、Sheets、Data）
**別名：** Claude Whiteboards, Claude Sheets, Claude Data, Claude Dashboards
**首次出現：** 2026-11-10
**最後更新：** 2026-11-15
**最後新聞更新：** 2026-11-15

> **最新動態**（2026-11-15）
> Enterprise 方案的 Claude Data 11-20 起預設開啟，Whiteboards、Sheets 仍預設關；不想自動開的管理員要在 11-20 前關掉。

---

## 現況

官方文章（[Claude Whiteboards, Claude Sheets, and Claude Data](https://claude.com/resources/articles/sheets-whiteboards-data)）把三項功能一起介紹：Whiteboards 與 Sheets 以 beta 推出，原 Claude Dashboards 轉正式版並更名 Claude Data。三項所有付費方案都能用，網頁、桌面、手機都有（2026-11-14 查證）。

管理員在 Organization settings > Artifacts 開關三項。Enterprise 的 Claude Data 11-20 起預設開啟，倒數見 [[feature-radar]]。

### 三項功能對照

| 功能 | 狀態 | 做什麼 | Team／Enterprise 預設 |
|------|------|--------|------|
| Claude Whiteboards | beta | 團隊與 Claude 共用的腦力激盪白板 | 開／關 |
| Claude Sheets | beta | Claude 陪你建、改的試算表 | 開／關 |
| Claude Data | 正式版（認證查詢、即時分享仍 beta） | 問公司資料，做認證指標與共用儀表板 | 開／11-20 起開 |

- **Claude Data 前置條件**：先接資料 connector（資料倉儲或 CRM）；Dashboards 時期支援的來源清單見 [[entities/claude-design#Claude Dashboards 與 Claude Motion（beta，2026-10-08 發布）]]。
- **Dashboards 沿革**：2026-10-08 以 beta 發布，2026-11-11 轉正式版並更名；查詢可稽核、用量算進方案上限的規則是否沿用，官方文章未再說。
- **Sheets 細節**：官方文章細節本頁尚未取得，下方待查證。

## 與 Claude Meetings 的關係

Claude Meetings 與 Claude Sheets 同日（2026-11-10）見報：TechCrunch 稱 Meetings 把會議討論轉成計畫與任務，Reuters 稱 Claude 可進入 Google Meet 即時處理任務，VentureBeat 稱會議中可起草文件與白板（2026-11-12）。The Verge、Bloomberg 把這批產品形容為 Anthropic 自己的辦公套件、直接對上 Microsoft。

Meetings 目前只見媒體報導、未見官方一手文章，本頁不把它列為三件組成員。

## 時間線

- 2026-11-15：ZDNET 實測稱 Claude Sheets 在四方面比用 Google Sheets 連接器更好用，具體四項與測試方法未載（僅標題可用）。
- 2026-11-15：確認 Enterprise 預設值：Claude Data 11-20 起預設開，Whiteboards、Sheets 預設關（取自官方文章，非 11-19）
- 2026-11-11：官方文章發布，HN 273 分；Dashboards 轉正式版更名 Claude Data
- 2026-11-10：Claude Meetings 與 Sheets 見報；官方定價頁同步出現 Claude Sheets（beta）段落，異動見 [[entities/pricing-history]]
- 2026-10-08：Claude Dashboards（beta）與 Claude Motion 發布，見 [[entities/claude-design]]

## 待查證缺口

- ❓ **待查證**（標 2026-11-15｜查 Claude Sheets、Claude Whiteboards、Claude Meetings）｜**Sheets 與 Whiteboards 功能細節**：能否匯入匯出、與 Google Sheets 或 Excel 的關係、即時共編規則、用量是否算進方案額度，均未取得（官方說用量未載）
- Claude Data 即時分享的對象權限與資料量上限：Dashboards 時期說明中心即未載，轉正式版後未見更新

## 相關實體

- [[entities/claude-design]]：Dashboards、Motion 的原居頁，Docs、Slides、Design 脫離 beta 也記在那裡
- [[topics/anthropic-product-matrix]]：產品 × 功能對照，三項尚未入表
- [[entities/cowork]]、[[entities/pricing-history]]

## 參考來源

- [官方文章：Claude Whiteboards, Claude Sheets, and Claude Data](https://claude.com/resources/articles/sheets-whiteboards-data)（2026-11-11，2026-11-14 查證）
- [官方說明中心：Get started with Claude Dashboards](https://support.claude.com/en/articles/17454700-get-started-with-claude-dashboards)（2026-10-11 取得）
- [[news/2026-11-10]]
- [[news/2026-11-11]]
- [[news/2026-11-13]]

## 歷史記錄

- 2026-11-15：自 [[entities/claude-design]] 分出獨立頁；補 Enterprise 預設開關與 11-20 倒數
