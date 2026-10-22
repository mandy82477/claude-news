---
page: "entities/claude-docs"
kind: "entity"
type: "feature"
status: "beta"
domain: "🛠️ 工具/功能"
last_updated: "2026-10-17"
last_news_update: "2026-09-25"
status_main: "beta"
days_since_news: 27
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 27
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
# Claude Docs

**類型：** feature
**狀態：** beta
**領域：** 🛠️ 工具/功能
**首次出現：** 2026-09-17
**最後更新：** 2026-10-17
**最後新聞更新：** 2026-09-25

> **最新動態**（2026-09-25）
> Help Center release notes 新增段落：可在任何對話中直接向 Claude 要求文件，**含 Claude Code 與 Artifact 介面**。

---

## 現況

Claude Docs 是 Anthropic 於 2026-09-17 隨 [[entities/cowork|Claude Cowork 與 Chat 合併]]同步推出的官方文件工具（2026-10-08 起已脫離 beta，見 [[entities/claude-design]]），讓使用者可直接在 Claude 對話中建立、編輯文件，不需切換到外部應用程式。首波僅 Pro、Max 方案可用（2026-10-17 查官方說明頁已改載所有方案、預設開啟，見下方）；與既有 Artifacts 的功能邊界見下方 2026-10-17 查證段。

**09-25 操作路徑部分確認：** Help Center release notes 新增段落，稱可在任何對話中直接向 Claude 要求文件，**含 Claude Code 與 Artifact 介面**；輸出格式與 Artifacts 邊界已由 2026-10-17 查證補齊，見下段。

**官方說明頁確認操作路徑、匯出與 Artifacts 邊界（2026-10-17 查證）：** 依 [Help Center〈What are artifacts〉](https://support.claude.com/en/articles/17153992-what-are-artifacts)，Docs 是「與 Claude 及團隊即時共同撰寫的 living documents」。建立：在任何對話要求、於訊息框選 Output 後挑 Docs 範本，或從 Artifacts 分頁開始。編輯：直接打字，或選取文字按「Edit with Claude」，Claude 只改標記段落。匯出：Word、PDF、Markdown、Google Docs。與 Artifacts 的邊界：Docs／Slides／Design 是現行的「範本型」artifact；2026-09-16 前在對話建立的屬 legacy artifact，仍可發佈分享但不能再新建。方案：所有方案、預設開啟（Enterprise 自 2026-10-15 預設開啟，owner 可提早啟用）。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ⏳ 觀望 |
| 最適合 | 待社群實測後補齊 |
| 不適合 | 待社群實測後補齊 |

> 首日僅官方公告與媒體轉述，尚無社群操作心得；詳細最新熱度見 [[feature-radar]]

## 使用指南

Pro／Max 方案使用者於 claude.ai 對話中直接請 Claude 建立或編輯文件，即可觸發 Claude Docs（beta）；具體選單路徑官方未附截圖，待補。

## 核心功能

- **對話內建立與編輯文件**：不需離開 Claude 對話介面。
- 其餘功能細節（版本歷史、協作、匯出格式）官方摘要未載明，待補。

## 相關議題

- 同批推出：[[entities/cowork]]（Cowork／Chat 合併）、[[entities/claude-slides]]、[[entities/claude-design]]（整合進對話，可輸出 PowerPoint／PDF）
- [[entities/claude-code]]（同日桌面版終端機 session 帳號設定同步異動，屬同一「帳號統一」方向）

## 參考來源

- [Claude Help Center release notes](https://support.claude.com/en/articles/12138966-release-notes)（官方文件變更偵測，2026-09-25 查，非新聞報導）
- [官方部落格：Claude Cowork and chat are now one Claude](https://claude.com/blog/cowork-is-now-claude)（2026-09-17；HN 討論 226 分；Simon Willison 部落格轉引）
- Google News／Reuters、TechCrunch、Axios、Fortune、VentureBeat、Computerworld（2026-09-17，同事件媒體報導，僅標題／框架可用）
- [[news/2026-09-17]]、[[news/2026-09-25]]

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-09-25 | Help Center release notes 新增段落：可在任何對話（含 Claude Code、Artifact 介面）直接要求文件；輸出格式與跟 Artifacts 邊界仍未載明 |
| 2026-09-17 | 建頁。官方隨 Cowork／Chat 合併同步推出 Claude Docs（beta），先開放 Pro、Max 方案 |
