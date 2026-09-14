# 本機開發設定

在自己機器上跑這個 pipeline 需要什麼、怎麼跑。原本住在 `README.md` 的「快速開始」，2026-09-14 搬來這裡——README 的讀者是來看這份新聞站的，不是來安裝它的。

## 需求

- Python 3.13+
- [Claude Code](https://claude.com/claude-code)：摘要、評分與 wiki 沉澱都在 Claude session 內執行。本專案**不使用** `ANTHROPIC_API_KEY`，沒有 Claude Code 只能跑到抓料階段。
- `.env`（repo 根目錄）：

  | 變數 | 必要 | 用途 |
  |---|---|---|
  | `GITHUB_TOKEN` | 建議 | GitHub Releases / Issues 來源，避免匿名速率限制 |
  | `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET` | 可選 | Reddit 來源 |

## 安裝

```bash
pip install -r src/requirements_news.txt
```

雲端沙盒環境另有三個套件缺口（`python-dotenv`、`feedparser`、`sgmllib3k`），見 [`cloud-runbooks/_shared.md`](cloud-runbooks/_shared.md)。

## 只抓料，不用 LLM

```bash
python -m news_aggregator.main --gather-only
```

## 完整跑一天

在 Claude Code 裡：

```
/news-pipeline
```

日誌在 `src/logs/task_scheduler.log`。補跑過去日期用 `/wiki-backfill`，查 wiki 用 `/wiki-query`。

## 本機預覽網站

```bash
python scripts/build_web.py
```

然後執行 `web_reader/serve.bat` 或任何靜態伺服器。

## 改動完算不算完成

改 pipeline、script、hook、規則檔或 web reader 程式時，完工定義見 [`../.claude/rules/dev-done.md`](../.claude/rules/dev-done.md)：測試綠、已 commit、依賴缺口已登記，三者到齊才算完成。`python scripts/run_tests.py` 是那一關。
