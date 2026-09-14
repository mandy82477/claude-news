# CLAUDE.md

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki。

## 本站目標

為**需要深度與穩定資訊的工程師**而建：Claude Code 重度使用者（有什麼壞了、值不值得升版）、AI 系統開發者（社群驗證了什麼、踩過哪些坑）、Anthropic 生態追蹤者（政策、融資、合作怎麼走）。三個主軸：官方核心（公告、Changelog、SDK / API 迭代）、社群實測（HN / Reddit 的真實回饋、Bug 與變通）、生態動態（只收會改變工程師決策的融資、合作與政策）。取捨是穩定而非即時：26–30 小時延遲是設計，不追 X / Discord 秒級訊號，不碰 NDA 內部資訊，不做在地化市場觀測。對外完整版是 `README.md`，網站「關於」頁與它同源。

**收不收錄一律問這句：** 這份資料能幫助**需要深度與穩定資訊的工程師**更了解 Claude / Anthropic 生態系嗎？若否，不收錄。
目標讀者、蒐集範圍與不收錄清單：`.claude/rules/collection-scope.md`（動到 `src/news_aggregator/` 時自動載入）。

## 專案架構

| 路徑 | 是什麼 |
|---|---|
| `src/news_aggregator/` | Python 爬蟲，每日產 `news/YYYY-MM-DD.md`；日誌 `src/logs/`，模組說明 `src/DesignDocument/` |
| `news/` | 日報，唯讀原料 |
| `wiki/` | 從日報萃取的知識庫，規則在 `wiki/CLAUDE.md` |
| `web_reader/` | 日報與 wiki 的網站版，`scripts/build_web.py` 建置 |
| `.claude/reporter-rules/` | 記者與主編規則，明文 Read |
| `docs/rules-changelog/` | 規則沿革，只有人讀 |

## 這是一個 LLM wiki：三個動作

- **Ingest（每日，`/news-pipeline`）**：爬蟲產日報（`news/` 唯讀原料）→ 主編分類、派六位記者各寫自己領域的頁 → 主編彙整 `wiki/index.md`、`feature-radar.md`、`log.md`。頁面是「被策展的現在」，log 是不可改的過去，index 只放路由；每個事實只有一個家，別處用 wikilink 指過去。
- **Query（任何 session）**：專有名詞／issue 號／版本號 → 直接 Grep `wiki/`；概念、選型 → `python scripts/wiki_search.py "<原句>"` 全文排序（候選薄時加 `--expand`），再從 `wiki/index.md` 挑頁補候選，候選全開，頁頂 callout 是最新狀態；「最近怎樣」→ `wiki/log.md` 先 Grep 日期；誰負責哪頁 → `.claude/reporter-rules/<類別>/daily.md` 的負責頁面表；引用關係 → `python scripts/wiki_graph.py`。完整六路見 `wiki/CLAUDE.md`「搜尋策略」；查詢流程與答案回流見 `.claude/skills/wiki-query/SKILL.md`（`/wiki-query`）。
- **Lint（每週，`/weekly`、`/wiki-lint`）**：矛盾、孤兒、過期、蒸餾封存；歷史質疑抽題代打。
- **使用者提問通道**：使用者在對話中點名的事實，由主編以 web 工具查證一手來源後直接寫進 wiki（標查證日＋來源），並在 `wiki/log.md` append 一筆 Query 條目；不經日報，歸因 slug `user-query`。

## 環境限制

**此專案沒有 `ANTHROPIC_API_KEY`，開發時不得假設其存在。**

- **`claude -p` 任何情境一律禁止**：commands / skills 本身、它們呼叫的 script、子程序、間接觸發，全部不行
- 不得新增任何「有 API key 才能運作」的功能或 fallback；唯一合法的 LLM 路徑是 Claude session 直接執行
- 判斷式：這個改動在完全沒有 `ANTHROPIC_API_KEY` 的環境下也能正確運作嗎？若否，重新設計

## 開發完工定義

改 pipeline、script、hook、規則檔或 web reader 程式時，怎樣才算完成見 `.claude/rules/dev-done.md`（碰這些目錄自動載入；測試綠與 commit 範圍由 hook 強制）。

