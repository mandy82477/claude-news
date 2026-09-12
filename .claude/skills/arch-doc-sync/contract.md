# 架構文件契約

`.claude/skills/arch-doc-sync/SKILL.md` 的文件分工、class 契約與驗證檢查表單一來源。步驟不在本檔。

## 三份文件與其分工（改哪個看這裡）

| 檔案 | 角色 | 什麼時候改 |
|------|------|-----------|
| `src/DesignDocument/Design Diagram.md` | **現況的單一事實來源**（mermaid） | 任何現況架構變動，**先改這裡** |
| `docs/architecture-current.html` | 現況操作視圖（5 張 HTML box 圖 + filter）| 跟著 Design Diagram.md 改 |
| `docs/architecture-evolution.html` | 演進敘事（時間軸事件 + diagram A–F）| 只有「里程碑級」變動才加一筆事件 |
| `docs/architecture.css` | 兩頁共用樣式（token + class）| **只有改設計（顏色/字體/間距）才動；改內容不碰** |

> `docs/architecture-evolution-react.bak.html` 是舊 React 版備份，唯讀，不要拿它當範本。

## `.dgm-*` class 契約（`docs/architecture-current.html`）

5 張圖各是一個 `#dgm-<key>` panel（overview / agg / ingest / lint / artifacts），用 `architecture.css` 的 class 畫：`.dgm-box`、`.dgm-step`、`.dgm-arrow`、`.phase--a/b/c`（a/c=success 綠、b=ochre）、`.dgm-row`。

filter bar 每個 tab 是 `.dgm-tab`＋`data-dgm="<key>"`，JS 以 `getElementById('dgm-' + this.dataset.dgm)` 取 panel。

## `.event-*` class 契約（`docs/architecture-evolution.html`）

時間軸事件卡片結構：`.event-card`（含 `.event-date`、`.event-title`、`.event-tag--script/llm/agent`、可選 `.event-tag--diagram`、`.event-body` 內 `.event-md` + 可選 `.event-diagram`）。

## 驗證檢查表

### A. preview 可用時（首選）

launch.json 已有 `docs-preview`（port 3132）。preview_start 後對**每個改過的 HTML** 逐項查（用 preview_eval / preview_inspect）：

| 檢查 | 怎麼查 | 為什麼（哪次踩過）|
|------|--------|------------------|
| **charset UTF-8** | `document.characterSet==='UTF-8'` 且 h1 中文非亂碼 | 漏 `<meta charset="utf-8">` 會整頁亂碼，且**不產生 console error** |
| 共用 CSS 有套上 | 抽一個 `.dgm-box` 查 `borderTopColor` 是 `rgb(176,137,104)` | class 名不符會 fallback 成無樣式，肉眼未必立刻看出 |
| 版面置中 | 容器 `maxWidth` 是 `896px`、`margin:auto` | utility class 缺失會讓版面全寬爆掉 |
| filter / 互連 | 實際點擊，確認 panel 切換、cross-link href 正確 | — |
| console | `preview_console_logs` level error 為空 | — |

- **截圖工具此環境會逾時，不要用 screenshot**，一律 eval/inspect
- **不可只信「看起來好了」或 agent 的「已驗證」**——親自 eval 查渲染後的實際值

### B. preview 工具不可用時（fallback，不可略過驗證、不可靠肉眼代替）

跑靜態三件套，缺一不可：

1. `python scripts/check_arch_docs.py`（步驟 5 上方已跑，此處確認為綠）
2. HTML 標籤結構平衡：用 Python 標準庫 `html.parser` 解析兩份改過的 HTML，確認 `feed()` 不拋例外、且無明顯未閉合標籤（可用 `HTMLParser` 搭配 tag stack 檢查 start/end 配對）
3. 新增 tab（若有）的 JS 通用性確認：確認 filter bar 用的是既有 `.dgm-tab` class + `getElementById('dgm-' + this.dataset.dgm)` 這類通用邏輯——新 panel 只要照既有 `data-dgm` 命名規則加 tab 與 panel，**不需要改 JS**；若新增邏輯偏離此模式，視為未過驗證
