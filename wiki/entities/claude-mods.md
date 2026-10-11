---
page: "entities/claude-mods"
kind: "entity"
type: "feature"
status: "active（v2.1.287 起正式發布，預設開啟）"
domain: "🛠️ 工具/功能"
last_updated: "2026-10-04"
last_news_update: "2026-10-04"
status_main: "active"
days_since_news: 7
parent: "entities/claude-code"
children: "[]"
page_role: "child"
days_since_news_subtree: 7
inbound_links: 6
attribution_count: 4
attribution_last: "2026-10-04"
top_source: "google-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Mods

**類型：** feature
**狀態：** active（v2.1.287 起正式發布，預設開啟）
**領域：** 🛠️ 工具/功能
**別名：** Function Hooks, mods, `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`
**上層：** [[entities/claude-code]]
**首次出現：** 2026-09-04
**最後更新：** 2026-10-04
**最後新聞更新：** 2026-10-04

> **最新判讀**（2026-10-04）
> mod 是跑在 Claude Code 行程內的 plugin，官方文件明載它讀得到環境變數與設定檔裡的 API key、不受沙箱隔離；這是設計能力，不是漏洞。裝之前先 `claude plugin validate`，只裝可信來源。

---

## 現況

Claude Mods 是 Claude Code 的外掛機制：mod 是 plugin，以 JS／TS 事件處理函式在 Claude Code 行程內執行，可觀察、改寫或接管 tool call、prompt 與介面繪製。需 v2.1.287 以上，**預設開啟**（官方文件，2026-10-04 查證，[overview](https://code.claude.com/docs/en/plugins/mods/overview)）。

它即先前的「Function Hooks」提案：09-04 的 build 已有 `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` 旗標，09-09 官方在 issue #91870 承諾出貨並更名，10-01 隨 v2.1.287 上線（旗標追蹤見 [[topics/claude-code-experimental]]）。v2.1.288 為 mods 加了 `$.ui.selection()`，回傳使用者在全螢幕模式最後選取的文字。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 想改 Claude Code 行為、介面或審核流程的外掛開發者 |
| 不適合 | 沒有能力讀懂第三方 mod 原始碼、又在放真實 API key 的環境直接安裝陌生 mod 的人 |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

```
# 裝前檢查：列出該 mod 掛了哪些 hooks、做了哪些 calls
claude plugin validate ./some-mod

# 單一 mod 停用：在 /plugin 介面操作
# 一次 session 全關：
claude --safe-mode

# 全部關閉（settings.json）：
"disableAllHooks": true

# 內建的 you-should-know 預設停用，要用才開：
/plugin enable cc-plugin-you-should-know@builtin
```

官方入口（皆 2026-10-04 查證）：[overview](https://code.claude.com/docs/en/plugins/mods/overview)、[create](https://code.claude.com/docs/en/plugins/mods/create)；10-02 文件索引一次新增 10 頁 mods 文件，涵蓋管理、API、建立、事件、介面、測試、疑難排解。

## 權限與安全

官方文件「What a mod can reach」明列（官方文件，2026-10-04 查證）：

- **檔案、程式、網路**：以使用者權限讀寫檔案、啟動程式、連網。
- **API key**：讀得到環境變數與設定檔，包含存放其中的 API key。
- **看見一切**：看得到每個 prompt 與每個 tool call，可改寫 prompt 與 tool call。
- **代為核准**：可代使用者核准 tool call，能越過 ask 規則與使用者自己的 PreToolUse hook；改不了權限提示畫面本身。
- **花你的額度**：可用使用者的方案或 API key 呼叫模型。
- **不受沙箱隔離**：開了 sandboxing 也只隔離 Claude 跑的 Bash，mod 啟動的行程在沙箱外。

mixed-news.com（10-02）標題稱 Anthropic 說外掛可讀取 API key，the-decoder、The New Stack（10-03）報導 mods 以使用者權限執行、未經沙箱隔離。官方文件已把這些列為 mod 的明載能力，所以「mod 能讀 API key」是設計，不是未公開的漏洞；風險在於裝了不可信的 mod，等於把上述權限全交給它。

**關閉與管控**：

- 單一 mod：在 `/plugin` 停用。
- 單次 session：`--safe-mode`。
- 全部外掛 hooks：`"disableAllHooks": true`。
- 組織端：`allowManagedModsOnly`。
- 舊的 `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` 已被忽略，不再是開關。
- `disableAllHooks`、`--safe-mode`、`--bare` 都停不了內建 mods。

## 內建與官方範例 mods

內建 mods（官方文件，2026-10-04 查證）：

- `cc-plugin-agents-md`
- `cc-plugin-diff`：即 `/diff`
- `cc-plugin-plugin-authoring`
- `cc-plugin-sec-default`
- `cc-plugin-telemetry`
- `cc-plugin-you-should-know`：旁觀 agent，在使用者或 Claude 可能漏掉某件事時主動提醒；預設停用

官方範例 mods 放在 claude-code-playground repo：token-weather、blast-radius、replay-theater。`diff`、`sec-default`、`telemetry` 三款的原始碼 09-09 起公開在 claude-code repo 的 `mods` 目錄。

## 社群用法與回饋

- **issue #91870**：官方追蹤串（原提案「Mods - make Claude 10x more extensible」），出貨當日累積 233 則留言、218 個讚，官方表示逐一處理使用者回饋。
- **statuslin.es**：Show HN 的 Claude Code status line 樣式庫，收錄見 [[topics/community-tech-patterns]]。
- **statuslin.es 作者的 mod**：10-02 用 Mods 的 function hooks 把狀態列延伸進 Claude 桌面 App；HN 2 分＋Reddit r/ClaudeCode 轉發，訊號薄弱，見 [[topics/community-tech-discussions]]。
- **競品相容層**：Pandaily（經 Google News 轉載，2026-10-04，僅標題可用）報導競品 DeepSeek Harness v0.2.1-alpha.1 新增實驗性 Claude Code Mods 相容層；相容範圍與技術細節未見報導，單一來源。

## 相關議題

- 安全面的社群報導與攻擊面整理：[[topics/ai-agent-safety]]
- 版本脈絡與已知問題：[[entities/claude-code]]
- 功能熱度與試用判斷：[[feature-radar]]

## 參考來源

- [官方文件：Mods overview](https://code.claude.com/docs/en/plugins/mods/overview)（2026-10-04 查證）
- [GitHub Release v2.1.287](https://github.com/anthropics/claude-code/releases/tag/v2.1.287)
- [issue #91870](https://github.com/anthropics/claude-code/issues/91870)
- [[news/2026-10-02]]、[[news/2026-10-03]]

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-10-04 | 建頁；依官方 overview 文件整理權限範圍、關閉方式與內建 mods |
| 2026-10-03 | the-decoder、The New Stack 報導以使用者權限執行、無沙箱；v2.1.288 加入 `$.ui.selection()` |
| 2026-10-01 | v2.1.287 正式出貨，預設開啟 |
| 2026-09-09 | 官方在 #91870 承諾出貨並更名 Claude Mods |
| 2026-09-04 | `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` 旗標現身於 build |
