---
name: arch-doc-sync
description: 系統架構變動時，快速同步更新架構文件（Design Diagram.md + 現有架構頁 + 演進頁），內建防坑檢查。
---

# Architecture Doc Sync

當 CLAUDE_NEWS 系統結構改變（新 pipeline 步驟、新來源、新記者規則、新治理機制、模型分工變化等）時，用此流程把三份架構文件同步到最新。

三份文件的分工表、`.dgm-*`／`.event-*` class 契約、驗證 A／B 檢查表住 `.claude/skills/arch-doc-sync/references/contract.md`，本檔不重述——**動手前先讀它**。

---

## 分工（省 token）

- **主 session 只做判斷性工作**：判斷變更範圍（步驟 1）、改事實來源 `src/DesignDocument/Design Diagram.md`（步驟 2）。
- **機械式 HTML 鏡射交給 sonnet agent**：`Design Diagram.md` 定稿後，把「照 Design Diagram.md 更新 `docs/architecture-current.html` 對應 panel／`docs/architecture-evolution.html` 對應事件卡」派給 `model: "sonnet"` 的 agent 執行（步驟 3、4）——這是照抄既有 class 寫法的機械式編輯，不需要旗艦模型判斷。
- **主 session 最後重驗 disk 上的最終檔**：無論步驟 3/4 是自己做還是派工，commit 前都必須親自跑 `python scripts/check_arch_docs.py` 與步驟 5 的驗證。

---

## 步驟

### 1. 判斷變更範圍
- 讀 `src/DesignDocument/Design Diagram.md` 標頭「最後更新」日期
- `git log --oneline --since="<那個日期>"` 看這段期間的 commit，挑出**結構性**變動（pipeline 步驟增減、`sources/*.py` 增減、`.claude/rules/`、`.claude/reporter-rules/` 或 `.claude/commands/` 的流程改動、新治理機制）
- 分類每筆變動：
  - **現況變動**（改了系統「現在怎麼運作」）→ 要更新 Design Diagram.md + current 頁
  - **里程碑**（一次有意義的架構演進，值得記入歷史）→ 額外在 evolution 頁加一筆事件
  - 純 bug fix / 微調 → 通常不進架構文件

### 2. 先更新事實來源 `Design Diagram.md`
- 對照**實際系統**核實，不憑記憶：pipeline 讀 `.claude/skills/news-pipeline/SKILL.md`、`.claude/skills/news-gather/SKILL.md`、`.claude/skills/news-digest/SKILL.md`、`.claude/skills/reader-digest/SKILL.md`、`.claude/skills/web-publish/SKILL.md`；來源清單讀 `src/news_aggregator/main.py` 的 `sources = [...]`；lint 讀 `.claude/skills/wiki-lint/SKILL.md`；派工讀 `.claude/reporter-rules/wiki-ingest.md`
- 改對應的 mermaid 圖與文字；更新標頭「最後更新」為今日
- 這是下游 HTML 的依據，**先它、後 HTML**

### 3. 更新 `docs/architecture-current.html`
- 只改有變動的那張 panel，比照既有 box 的 class 寫法（class 與 panel key 見 `.claude/skills/arch-doc-sync/references/contract.md`）
- 若新增一張圖：filter bar 加一個 `.dgm-tab`（`data-dgm="<key>"`）+ 一個 `#dgm-<key>` panel
- **更新日期標記**「現況截至 YYYY-MM-DD」為今日
- 設計 token（顏色/字體）若要調，**只改 `architecture.css`**，不在 HTML 內寫死

### 4. 更新 `docs/architecture-evolution.html`（僅里程碑）
- 事件卡片結構見 `.claude/skills/arch-doc-sync/references/contract.md`
- 新事件插入**對應月份分組**、依日期排序（不是塞末尾）
- `track` 三選一：`script`（腳本/pipeline）/ `llm`（LLM 呼叫點）/ `agent`（Agent 設計）
- 只有真正的新架構模式才配新 diagram（SVG）；沿用既有 A–F 的畫法

### 5. 驗證（強制，preview 可用時首選；不可用時走靜態 fallback，兩者皆不可略過）

**先跑機械漂移檢查（永遠先跑，不管 preview 是否可用）：**
```
python scripts/check_arch_docs.py
```
涵蓋來源清單一致、日期三處同步、charset meta、CSS token 存在性四類，不管走哪條驗證路徑都必須通過。

接著照 `.claude/skills/arch-doc-sync/references/contract.md`「驗證檢查表」走 A（preview 可用，首選）或 B（靜態 fallback）。

### 6. Commit
- Commit 前再跑一次 `python scripts/check_arch_docs.py` 到零錯誤
- `git add docs/ src/DesignDocument/`，commit 訊息 `docs: 架構文件同步 <一句話變動>`，結尾加 Co-Authored-By 行；push

---

## 🚫 不變式（違反必出事；立法理由見沿革檔 `docs/rules-changelog/arch-doc-sync.md` 2026-07-05/06）

1. **charset meta 必備**：每個 HTML 檔 `<html>` 後必須有 `<meta charset="utf-8">`。
2. **設計 token 單一來源**：顏色/字體/圓角只在 `architecture.css` 的 `:root` 改；HTML 內不寫死色碼。
3. **獨立驗證**：改完一定親自查渲染後的實際值，不靠肉眼、不靠「已完成」回報。
4. **派工要重驗最終狀態**：把機械式 HTML 編輯派給 sonnet agent 時，主 session 必須在最後重新驗證 disk 上的最終檔。
5. **先事實來源、後 HTML**：永遠先改 `Design Diagram.md`，HTML 跟著它。
6. **原 React 備份唯讀**：`docs/architecture-evolution-react.bak.html` 不當範本、不修改。

---

## 邊界

- 由主 session 執行；步驟 3／4 的機械式 HTML 鏡射可派 `model: "sonnet"` agent，判斷與驗證不外包。
- 截圖工具此環境會逾時，不要用 screenshot，一律 eval/inspect。
- `python scripts/check_arch_docs.py` 零錯誤＋步驟 5 的 A 或 B 全項通過才算完成，否則不得 commit。
