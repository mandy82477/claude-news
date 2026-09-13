# Claude News

> A quiet wiki of noisy news.

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki，給需要穩定訊號而非即時噪音的工程師。

本檔與網站「關於」頁同源；蒐集門檻的實作版在 `.claude/rules/collection-scope.md`。

## 四個主軸

| | 主軸 | 內容 |
|---|---|---|
| i. | **官方核心** | Anthropic 公告、GitHub Changelog、SDK 與 API 迭代、定價結構變化。Source of truth。 |
| ii. | **社群實測** | Hacker News 與 Reddit 上工程師驗證過的工作流、agent 設計、Bug 回報與變通。Field reports。 |
| iii. | **生態動態** | 融資、人事、大型企業合作（AWS / Google）、政策趨勢與周邊工具。只收會改變工程師決策的那些：定價、可用性、法規強制、供應商鎖定。 |
| iv. | **時效延遲** | 26–30 小時的穩定資訊，不是秒級快訊。社交平台首發訊號請另尋管道。Stable, not instant。 |

## 一天怎麼歸檔

1. **多來源抓取**：每日 10 個管道。Anthropic Blog、Anthropic Status、GitHub Releases、GitHub Issues、Hacker News、Reddit、Google News、dev.to、API Release Notes、技術部落格 RSS。
2. **去重過濾**：URL 與標題模糊比對。
3. **相關性評分**：1 到 5 分，3 分以上保留。
4. **LLM 摘要**：繁中 Markdown 日報，落在 `news/YYYY-MM-DD.md`。
5. **Wiki 沉澱**：日報條目整理進 `wiki/`（人物、產品、事件、議題、功能雷達）。條目進了 wiki 才算「已沉澱」。
6. **網站更新**：重建靜態 web reader 並部署，日報與 wiki 都能在瀏覽器讀，不必開 Obsidian。

## 我們做

- **技術與定價迭代**：精準追蹤 GitHub Changelog、SDK 演進與 API 定價結構變化。
- **合作與融資動態**：Anthropic 融資、大型企業合作案與政策趨勢，只在會改變工程師決策時收。
- **工作流模式與實戰技巧**：從 HN / Reddit 萃取工程師驗證過的 agent 工作流、multi-agent 設計與 Claude Code 使用技巧。

## 我們不做

- **X 與 Discord 即時訊號**：無法捕捉首發於社交平台的秒級爆料、漏洞回報與突發動態。26–30 小時延遲是設計取捨，不是缺陷。
- **企業內部非公開資訊**：NDA 保護下的實測數據、內部佈署經驗與未公開的產品路線。
- **非英語系市場在地化**：日、韓、中開發社群的特定 Bug 與應用案例觀測受限。
- **IG / Discord 流傳的實用 Skill**：財務分析、前端設計等實用型 Claude Code skill 多在 IG、Discord 擴散，不走 HN / Reddit，無法自動收錄。遇到請手動告知補充。

## 適合誰

**適合**

- **Claude Code 重度使用者**：想第一時間知道有什麼壞了、值不值得升版，不用自己刷 HN。
- **AI 系統開發者**：在建 agent 或工作流，想知道社群驗證了什麼、踩過哪些坑。
- **Anthropic 生態追蹤者**：關注政策、融資、合作動態，一站掌握生態走向。

**不適合**

- **即時新聞工作者**：需要追蹤社交平台秒級爆料與突發事件。
- **影音學習者**：以影音教學或互動 Demo 為主要學習方式。
- **在地化專才**：主要關注特定語系本地市場動態。

> 「濾除社群雜訊，直擊 Claude Code 技術核心。」為需要深度與穩定資訊的工程師而建。

## 從原始碼跑

```
news/         每日日報（YYYY-MM-DD.md，唯讀原料）
wiki/         LLM 維護的知識庫（entities/ topics/）
src/          Python 新聞聚合器
web_reader/   靜態網頁閱讀器
scripts/      建置與檢查工具
```

1. `pip install -r src/requirements_news.txt`
2. repo 根目錄建 `.env`，填 `GITHUB_TOKEN`（建議）、Reddit 金鑰（可選）
3. 在 Claude Code 裡執行 `/news-pipeline`，日誌在 `src/logs/task_scheduler.log`

需要 Python 3.13+ 與 Claude Code。開發者規則入口是根目錄 `CLAUDE.md`，流程設計見 `src/DesignDocument/Design Diagram.md`。
