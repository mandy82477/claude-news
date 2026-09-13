<p align="center">
  <a href="https://mandy82477.github.io/claude-news/web_reader/"><img src="web_reader/icons/icon-192.png" width="96" alt="Claude News logo"></a>
</p>

<h1 align="center">Claude News</h1>

<p align="center"><em>A quiet wiki of noisy news.</em></p>

[![daily-gather](https://github.com/mandy82477/claude-news/actions/workflows/daily-gather.yml/badge.svg)](https://github.com/mandy82477/claude-news/actions/workflows/daily-gather.yml)
[![daily-watchdog](https://github.com/mandy82477/claude-news/actions/workflows/daily-watchdog.yml/badge.svg)](https://github.com/mandy82477/claude-news/actions/workflows/daily-watchdog.yml)
[![quality](https://github.com/mandy82477/claude-news/actions/workflows/quality.yml/badge.svg)](https://github.com/mandy82477/claude-news/actions/workflows/quality.yml)
[![weekly-linkcheck](https://github.com/mandy82477/claude-news/actions/workflows/weekly-linkcheck.yml/badge.svg)](https://github.com/mandy82477/claude-news/actions/workflows/weekly-linkcheck.yml)
![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue)

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki，給需要穩定訊號而非即時噪音的工程師。

*A daily, LLM-curated digest and wiki of Claude Code / Anthropic news, written in Traditional Chinese. Stable, not instant.*

**📖 線上閱讀：<https://mandy82477.github.io/claude-news/web_reader/>** ｜ 日報與 wiki 都能在瀏覽器讀，不必開 Obsidian。

## 目錄

- [三個主軸](#三個主軸)
- [一天怎麼歸檔](#一天怎麼歸檔)
- [自動化怎麼運作](#自動化怎麼運作)
- [收錄範圍](#收錄範圍)
- [適合誰](#適合誰)
- [快速開始](#快速開始)
- [專案結構](#專案結構)

## 三個主軸

| | 主軸 | 內容 |
|---|---|---|
| i. | **官方核心** | Anthropic 公告、GitHub Changelog、SDK 與 API 迭代、定價結構變化。這是 source of truth。 |
| ii. | **社群實測** | Hacker News 與 Reddit 上工程師驗證過的工作流、agent 設計、Bug 回報與變通。 |
| iii. | **生態動態** | 融資、人事、大型企業合作（AWS / Google）、政策趨勢與周邊工具。只收會改變工程師決策的那些：定價、可用性、法規強制、供應商鎖定。 |

**取捨是穩定而非即時**：26–30 小時延遲是設計，不追 X / Discord 的秒級訊號。社交平台首發訊號請另尋管道。

## 一天怎麼歸檔

1. **多來源抓取**：十餘個管道。Anthropic Blog、Anthropic Status、GitHub Releases、GitHub Issues、Hacker News、Reddit、Google News、dev.to、Lobsters、API Release Notes、官方文件變動、技術部落格 RSS。完整清單見 `src/news_aggregator/sources/`。
2. **去重過濾**：URL 與標題模糊比對。
3. **相關性評分**：1 到 5 分，3 分以上保留。
4. **LLM 摘要**：繁中 Markdown 日報，落在 `news/YYYY-MM-DD.md`。
5. **Wiki 沉澱**：日報條目整理進 `wiki/`（人物、產品、事件、議題、功能雷達）。條目進了 wiki 才算「已沉澱」。
6. **網站更新**：重建靜態 web reader 並部署到 GitHub Pages。

## 自動化怎麼運作

每日 pipeline 全自動、關機也跑，拆成三層：

```
① GitHub Actions  daily-gather      純 Python 抓料，不需 LLM，網路無限制
        ↓  commit gathered_items.json 回 master
② 雲端 routine    daily-news-pipeline-cloud
                                    Claude Code 訂閱 LLM 生日報、六位記者 ingest wiki、建站、單一 push
        ↓
③ GitHub Actions  daily-watchdog    檢查當日產出是否齊全，缺了就通知
```

為什麼拆成兩段（雲端沙盒 egress 封鎖、重試取代緩衝）見 [`docs/daily-automation.md`](docs/daily-automation.md)；雲端 routine 的 trigger 定義與 runbook 見 [`docs/cloud-runbooks/`](docs/cloud-runbooks/README.md)。每週另有 wiki lint 與連結檢查。

## 收錄範圍

**收**

- **技術與定價迭代**：精準追蹤 GitHub Changelog、SDK 演進與 API 定價結構變化。
- **合作與融資動態**：Anthropic 融資、大型企業合作案與政策趨勢，只在會改變工程師決策時收。
- **工作流模式與實戰技巧**：從 HN / Reddit 萃取工程師驗證過的 agent 工作流、multi-agent 設計與 Claude Code 使用技巧。

**不收**

- **X 與 Discord 即時訊號**：無法捕捉首發於社交平台的秒級爆料、漏洞回報與突發動態。
- **企業內部非公開資訊**：NDA 保護下的實測數據、內部佈署經驗與未公開的產品路線。
- **非英語系市場在地化**：日、韓、中開發社群的特定 Bug 與應用案例觀測受限。
- **IG / Discord 流傳的實用 Skill**：財務分析、前端設計等實用型 Claude Code skill 多在 IG、Discord 擴散，不走 HN / Reddit，無法自動收錄。遇到請手動告知補充。

收錄門檻的實作版在 `.claude/rules/collection-scope.md`。

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

## 快速開始

**需求**

- Python 3.13+
- [Claude Code](https://claude.com/claude-code)：摘要、評分與 wiki 沉澱都在 Claude session 內執行。本專案**不使用** `ANTHROPIC_API_KEY`，沒有 Claude Code 只能跑到抓料階段。
- `.env`（repo 根目錄）：

  | 變數 | 必要 | 用途 |
  |---|---|---|
  | `GITHUB_TOKEN` | 建議 | GitHub Releases / Issues 來源，避免匿名速率限制 |
  | `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET` | 可選 | Reddit 來源 |

**安裝**

```bash
pip install -r src/requirements_news.txt
```

**只抓料，不用 LLM**

```bash
python -m news_aggregator.main --gather-only
```

**完整跑一天**（在 Claude Code 裡）

```
/news-pipeline
```

日誌在 `src/logs/task_scheduler.log`。補跑過去日期用 `/wiki-backfill`，查 wiki 用 `/wiki-query`。

**本機預覽網站**

```bash
python scripts/build_web.py
```

然後執行 `web_reader/serve.bat` 或任何靜態伺服器。

## 專案結構

| 路徑 | 是什麼 |
|---|---|
| `news/` | 每日日報 `YYYY-MM-DD.md`，唯讀原料 |
| `wiki/` | LLM 維護的知識庫：`entities/`、`topics/`、`index.md` 路由、`log.md` 不可改的過去、`feature-radar.md` |
| `src/news_aggregator/` | Python 新聞聚合器；`sources/` 每個來源一檔 |
| `src/DesignDocument/` | 流程設計與模組說明 |
| `web_reader/` | 靜態網頁閱讀器，`scripts/build_web.py` 建置 |
| `scripts/` | 建置、連結檢查、wiki 圖譜等工具 |
| `.claude/` | Claude Code 的 skills、commands、rules、記者 agent 規則，也就是 pipeline 的 LLM 端 |
| `.github/workflows/` | `daily-gather`、`daily-watchdog`、`quality`、`weekly-linkcheck` |
| `docs/` | 自動化架構、雲端 runbook、規則沿革、頁面健檢紀錄 |

開發者規則入口是根目錄 `CLAUDE.md`；wiki 的維護規則在 `wiki/CLAUDE.md`。
