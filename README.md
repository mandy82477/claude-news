<p align="center">
  <a href="https://mandy82477.github.io/claude-news/web_reader/"><img src="web_reader/icons/icon-192.png" width="96" alt="Claude News logo"></a>
</p>

<h1 align="center">Claude News</h1>

<p align="center"><em>A quiet wiki of noisy news.</em></p>

[![read](https://img.shields.io/badge/read-mandy82477.github.io%2Fclaude--news-8E5F3D?style=flat-square&labelColor=4A4640)](https://mandy82477.github.io/claude-news/web_reader/)
[![latest digest](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmandy82477.github.io%2Fclaude-news%2Fweb_reader%2Fdata%2Fstats.json&query=%24.latestNews&label=latest%20digest&style=flat-square&labelColor=4A4640&color=8E5F3D)](https://mandy82477.github.io/claude-news/web_reader/)
[![digests](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmandy82477.github.io%2Fclaude-news%2Fweb_reader%2Fdata%2Fstats.json&query=%24.digests&label=digests&style=flat-square&labelColor=4A4640&color=8E5F3D)](https://mandy82477.github.io/claude-news/web_reader/)
[![wiki](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmandy82477.github.io%2Fclaude-news%2Fweb_reader%2Fdata%2Fstats.json&query=%24.wikiPages&suffix=%20pages&label=wiki&style=flat-square&labelColor=4A4640&color=8E5F3D)](https://mandy82477.github.io/claude-news/web_reader/)
[![daily-watchdog](https://github.com/mandy82477/claude-news/actions/workflows/daily-watchdog.yml/badge.svg)](https://github.com/mandy82477/claude-news/actions/workflows/daily-watchdog.yml)

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki，給需要穩定訊號而非即時噪音的工程師。

*A daily, LLM-curated digest and wiki of Claude Code / Anthropic news, written in Traditional Chinese. Stable, not instant.*

**📖 線上閱讀：<https://mandy82477.github.io/claude-news/web_reader/>** ｜ 日報與 wiki 都能在瀏覽器讀，不必開 Obsidian。

📱 網站是 PWA：iPhone 用 Safari 開啟後「分享 → 加入主畫面」，Android 用 Chrome 選單「安裝應用程式」，即可像 app 一樣全螢幕閱讀，已看過的頁面離線也能開。

## 目錄

- [規模](#規模)
- [三個主軸](#三個主軸)
- [一天怎麼歸檔](#一天怎麼歸檔)
- [每週一份週報](#每週一份週報)
- [知識圖譜](#知識圖譜)
- [這是一個 LLM wiki：三個動作](#這是一個-llm-wiki三個動作)
- [自動化怎麼運作](#自動化怎麼運作)
- [適合誰](#適合誰)
- [快速開始](#快速開始)
- [專案結構](#專案結構)

## 規模

| | 數量 |
|---|---|
| 每日日報 | 138 份（2026-04-25 起，涵蓋 142 天） |
| 每週週報 | 8 份（2026-W30 起連續八週） |
| wiki 頁面 | 85 頁（人物與產品 47 頁、長期議題 38 頁） |
| 抓取管道 | 14 個 |

wiki 頁面依領域分佈：

| 領域 | 頁數 |
|---|---|
| 👤 人物 | 21 |
| 🛠️ 工具/功能 | 17 |
| 💼 商業 | 16 |
| 🌐 社群 | 12 |
| 🏛️ 政策/安全 | 10 |
| 🤖 模型 | 9 |

六個領域各由一位記者認領維護，另有兩位不認領領域頁的專責記者（開發實務沉澱、投資訊號判讀）。規則在 `.claude/reporter-rules/`。

## 三個主軸

| | 主軸 | 內容 |
|---|---|---|
| i. | **官方核心** | Anthropic 公告、GitHub Changelog、SDK 與 API 迭代、定價結構變化。這是 source of truth。 |
| ii. | **社群實測** | Hacker News 與 Reddit 上工程師驗證過的工作流、agent 設計、Bug 回報與變通。 |
| iii. | **生態動態** | 融資、人事、大型企業合作（AWS / Google）、政策趨勢與周邊工具。只收會改變工程師決策的那些：定價、可用性、法規強制、供應商鎖定。 |

**取捨是穩定而非即時**：26–30 小時延遲是設計，不追 X / Discord 的秒級訊號。社交平台首發訊號請另尋管道。另外兩個抓不到的：NDA 保護下的企業內部實測與未公開路線圖；以及 IG / Discord 擴散的實用型 Claude Code skill（財務分析、前端設計那類不走 HN / Reddit，**遇到請開 issue 告知補充**）。收錄門檻的實作版在 `.claude/rules/collection-scope.md`。

## 一天怎麼歸檔

1. **多來源抓取**：14 個管道。Anthropic Blog、Anthropic Status、GitHub Releases、GitHub Issues、Hacker News、Reddit、Google News、dev.to、API Release Notes、官方文件變動、技術部落格 RSS。完整清單見 `src/news_aggregator/sources/`。
2. **去重過濾**：URL 與標題模糊比對。
3. **相關性評分**：1 到 5 分，3 分以上保留。
4. **LLM 摘要**：繁中 Markdown 日報，落在 `news/YYYY-MM-DD.md`。
5. **Wiki 沉澱**：日報條目整理進 `wiki/`（人物、產品、事件、議題、功能雷達）。條目進了 wiki 才算「已沉澱」。
6. **網站更新**：重建靜態 web reader 並部署到 GitHub Pages。

## 每週一份週報

日報是當天發生什麼，週報是這一週的敘事。四節固定：頭條敘事、技術討論與深挖、下週看什麼、本週數字。頭條從使用者側的具體事件開篇，不從公司公告開篇——本週的頭條主角是一位英國顧問，他沒開工那天用量卻從 45% 爬到 55%。

「下週看什麼」寫下的每個預測都進 `weekly/open-signals.jsonl`（目前 88 筆），隔週回頭對帳：命中、落空，還是條件變了。寫預測容易，記錄自己猜錯比較難。

## 知識圖譜

wiki 是 Obsidian vault，但要看關聯圖不必開 Obsidian——網站「地圖」分頁重畫了一次，可篩選、可搜尋、點節點開側欄。

89 個節點、615 條連結。關鍵在邊怎麼算：連結分正文引用（497 條）與樣板區引用（310 條），地圖預設勾「只看正文引用」。多數自動產生的知識圖把每條連結等價計算，「相關實體」「延伸閱讀」那種樣板區一算進去就糊成毛球；這裡預設只畫有人真的在正文裡寫下的關聯，需要時再把樣板邊打開。

節點帶領域色與「距上次更新幾天」，哪一塊還在動、哪一塊冷掉了，一眼看得出來。

## 這是一個 LLM wiki：三個動作

上面那條線只是**寫入**。wiki 還有另外兩個動作，三者合起來才是這個知識庫的運作方式：

| 動作 | 頻率 | 做什麼 |
|---|---|---|
| **寫入 Ingest** | 每日 | 主編分類日報、派六位記者各寫自己領域的頁；每個事實只有一個家，別處用 wikilink 指過去。頁面是「被策展的現在」，`log.md` 是不可改的過去，`index.md` 只放路由。 |
| **查詢 Query** | 任何時候 | 在 Claude Code 裡 `/wiki-query`。依問題型態走六條路之一：專有名詞／issue 號直接 Grep、概念先跑 `scripts/wiki_search.py` 全文排序（同義叢集橋接用詞落差、`--expand` 沿 wikilink 擴散）再從 index 補挑、候選全開讀頁頂 callout、「最近怎樣」查 `log.md`、引用關係跑 `scripts/wiki_graph.py`。答案一律附出處與「現在／當時」狀態；wiki 裡沒有的事實，查一手來源後寫回該頁並標查證日，`log.md` 記一筆 Query 條目。設計全貌見 [`docs/wiki-ingest-query-design.md`](docs/wiki-ingest-query-design.md)。 |
| **整理 Lint** | 每週 | `/weekly`、`/wiki-lint`：找矛盾、孤兒頁、過期 callout，蒸餾封存；歷史質疑抽題重驗。 |

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
| `weekly/` | 每週週報 `YYYY-Www.md`；`open-signals.jsonl` 是預測對帳帳本 |
| `wiki/` | LLM 維護的知識庫：`entities/`、`topics/`、`index.md` 路由、`log.md` 不可改的過去、`feature-radar.md` |
| `src/news_aggregator/` | Python 新聞聚合器；`sources/` 每個來源一檔 |
| `src/DesignDocument/` | 流程設計與模組說明 |
| `web_reader/` | 靜態網頁閱讀器，`scripts/build_web.py` 建置 |
| `scripts/` | 建置、連結檢查、wiki 圖譜等工具 |
| `.claude/` | Claude Code 的 skills、commands、rules、記者 agent 規則，也就是 pipeline 的 LLM 端 |
| `.github/workflows/` | `daily-gather`、`daily-watchdog`、`weekly-linkcheck` |
| `docs/` | 自動化架構、雲端 runbook、規則沿革、頁面健檢紀錄 |
