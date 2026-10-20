---
page: "entities/claude-slides"
kind: "entity"
type: "feature"
status: "beta"
domain: "🛠️ 工具/功能"
last_updated: "2026-10-17"
last_news_update: "2026-09-25"
status_main: "beta"
days_since_news: 25
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 25
inbound_links: 4
attribution_count: 2
attribution_last: "2026-09-25"
top_source: "hn-repo-bridge"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Slides

**類型：** feature
**狀態：** beta
**領域：** 🛠️ 工具/功能
**首次出現：** 2026-09-17
**最後更新：** 2026-10-17
**最後新聞更新：** 2026-09-25

> **最新動態**（2026-09-25）
> Help Center release notes 新增段落：可在任何對話中直接向 Claude 要求簡報，**含 Claude Code 與 Artifact 介面**。

---

## 現況

Claude Slides 是 Anthropic 於 2026-09-17 隨 [[entities/cowork|Claude Cowork 與 Chat 合併]]同步推出的官方簡報工具（2026-10-08 起已脫離 beta，見 [[entities/claude-design]]）。搭配整合進對話的 [[entities/claude-design|Claude Design]]，使用者可直接在 Claude 對話中編輯、展示簡報，並下載為 PowerPoint 或 PDF 格式。首波僅 Pro、Max 方案可用，2026-10-17 查官方說明頁已改載所有方案、預設開啟。

**09-25 操作路徑部分確認：** Help Center release notes 新增段落，稱可在任何對話中直接向 Claude 要求簡報，**含 Claude Code 與 Artifact 介面**；範本與匯出已由 2026-10-17 查證補齊（見下段），多人協作機制仍未載明。

**官方說明頁確認操作路徑、匯出與編輯方式（2026-10-17 查證）：** 依 [Help Center〈What are artifacts〉](https://support.claude.com/en/articles/17153992-what-are-artifacts)，Slides（decks）可由你的筆記、報告或對話內已有的工作產出。建立：與 Docs 相同，在任何對話要求、選 Output 挑 Slides 範本或從 Artifacts 分頁開始。編輯與展示：可直接編輯任何一頁並在 Claude 內直接簡報（亦支援鍵盤與螢幕閱讀器）。匯出：PowerPoint 或 PDF，也可直送 Google Slides 成為可編輯檔。範本：Slides 本身即範本型 artifact，且可套用你的 design system（色彩、字型、元件）。協作：說明頁只把協作明確寫在 Docs，Slides 的多人協作機制未載明。方案：所有方案、預設開啟（Enterprise 自 2026-10-15 預設開啟，owner 可提早啟用）。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ⏳ 觀望 |
| 最適合 | 待社群實測後補齊 |
| 不適合 | 待社群實測後補齊 |

> 首日僅官方公告與媒體轉述，尚無社群操作心得；詳細最新熱度見 [[feature-radar]]

## 使用指南

Pro／Max 方案使用者於 claude.ai 對話中直接請 Claude 建立或編輯簡報，即可觸發 Claude Slides（beta）；完成後可從 Claude 直接展示，或下載為 PowerPoint／PDF。具體選單路徑官方未附截圖，待補。

## 核心功能

- **對話內建立、編輯簡報**：搭配整合進對話的 Claude Design。
- **直接展示或匯出**：可從 Claude 內展示，或下載為 PowerPoint／PDF。
- 其餘功能細節（範本庫、協作、版本歷史）官方摘要未載明，待補。

## 相關議題

- 同批推出：[[entities/cowork]]（Cowork／Chat 合併）、[[entities/claude-docs]]、[[entities/claude-design]]（整合進對話）
- [[entities/claude-code]]（同日桌面版終端機 session 帳號設定同步異動，屬同一「帳號統一」方向）

## 參考來源

- [Claude Help Center release notes](https://support.claude.com/en/articles/12138966-release-notes)（官方文件變更偵測，2026-09-25 查，非新聞報導）
- [官方部落格：Claude Cowork and chat are now one Claude](https://claude.com/blog/cowork-is-now-claude)（2026-09-17；HN 討論 226 分；Simon Willison 部落格轉引）
- Google News／Reuters、TechCrunch、Axios、Fortune、VentureBeat、Computerworld（2026-09-17，同事件媒體報導，僅標題／框架可用）
- [[news/2026-09-17]]、[[news/2026-09-25]]

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-09-25 | Help Center release notes 新增段落：可在任何對話（含 Claude Code、Artifact 介面）直接要求簡報；範本與協作機制仍未載明 |
| 2026-09-17 | 建頁。官方隨 Cowork／Chat 合併同步推出 Claude Slides（beta），可下載為 PowerPoint／PDF，先開放 Pro、Max 方案 |
