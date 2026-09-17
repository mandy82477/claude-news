# data/ — 結構化資料檔（JSONL）

本目錄存放 pipeline 產出的結構化統計資料，**append only**，供後續分析「哪個來源對哪個類別最有幫助」。資料檔（`*.jsonl`）由自動化流程維護：`source_attribution.jsonl` 由 wiki ingest 主編 append；`source_funnel.jsonl` 由每日 GitHub Actions gather / render 時 append 並 commit。

另含兩個非 JSONL 檔（皆為 `scripts/source_scorecard.py` 的輸入，設計說明見 `docs/source-scoring-optimization.md`）：

- **`source_registry.json`**：來源註冊表（單一真相源）——pipeline 註冊名 ↔ attribution slug ↔ 來源層品質標籤（`score_reliability` / `curation_mode`）。手動維護，新增或調整來源時同步更新。
- **`external/domain_pc1.csv`**：Lin et al. (2023, PNAS Nexus) 的 domain 信譽聚合分數（11,520 domains，pc1 0–1），來自 [hauselin/domain-quality-ratings](https://github.com/hauselin/domain-quality-ratings)。靜態外部資料，每季複查時效（見 `docs/workaround-register.md`）。

## source_attribution.jsonl

wiki ingest 時的來源歸因 ledger。主編收齊記者回報後，把各記者「來源歸因」欄逐筆轉為一行 JSON append（記者回報「無」則不寫）。

Schema（每行一筆）：

```json
{"date": "2026-07-11", "source": "hacker-news", "category": "社群", "page": "topics/community-tech-patterns", "item_url": "https://...", "item_title": "...", "publisher": "Financial Times"}
```

| 欄位 | 說明 |
|------|------|
| `date` | 日報日期（YYYY-MM-DD） |
| `source` | 來源 slug（`hacker-news` / `reddit` / `github-issues` / `github` / `google-news` / `devto` / `anthropic-blog` / `anthropic-status` / `claude-api-release-notes` / `blog` / `official-docs` / `official-skills` / `topic-watch`；`lobsters` 僅存歷史資料，來源已於 2026-07-10 移出），對照表見 `.claude/reporter-rules/shared.md`，註冊表 `data/source_registry.json` |
| `category` | 六類別之一：模型 / 功能 / 商業 / 安全政策 / 社群 / 人物 |
| `page` | 寫入的 wiki 相對路徑，不含 `.md`（如 `topics/ai-agent-safety`） |
| `item_url` | 日報條目原始連結 |
| `item_title` | 日報條目標題 |
| `publisher` | **選填**，來源標記斜線後半段（出版者／子版／站名）。記者回報的 `source` 只有斜線前半段，而 `google-news` 底下實際有 250+ 個出版者、品質從 Reuters 到內容農場都有，單一 slug 的品質標籤對它沒有意義。由 `scripts/enrich_attribution_publisher.py` 從日報回推補上（不改記者契約）；日報查無對應 URL、或來源本身無斜線（如 `Hacker News`）時不帶此欄。`topic-watch` 的斜線後半段是 topic slug（如 `ai-talent-flow`），回填後可按專頁統計定向抓取的實際貢獻 |

### publisher 回填

`scripts/enrich_attribution_publisher.py` 掃 `news/*.md` 建 URL → 來源標記對照，為缺 `publisher` 的行補值。**冪等**，可隨時重跑；新歸因 append 後執行一次即可補齊。

```bash
python scripts/enrich_attribution_publisher.py --dry-run   # 只報告
python scripts/enrich_attribution_publisher.py             # 實際寫入
```

首次回填（2026-08-05）：466 筆補上、涵蓋 141 家；`google-news` 涵蓋率 93%（229/247，127 家出版者）。未匹配多為語意差異（HN 條目記原文網址、日報連討論串），非解析錯誤。

## source_funnel.jsonl

每日抓取漏斗統計，由 `src/news_aggregator/main.py` 的 `write_funnel_record()` 寫入。

Schema（每行一筆，每次 gather / render 各一筆）：

```json
{"date": "2026-07-11", "run_ts": "2026-07-11T02:00:00+00:00", "mode": "gather", "lookback_hours": 26, "sources": {"Hacker News": {"ok": true, "gathered": 12, "filtered": 5, "emitted": 3}}, "totals": {"gathered": 80, "filtered": 20, "emitted": 12}}
```

| 欄位 | 說明 |
|------|------|
| `date` | 日報日期 |
| `run_ts` | 執行時間（UTC ISO） |
| `mode` | `gather` / `render` / `backfill` |
| `lookback_hours` | 回看時數 |
| `sources` | 以來源註冊名為 key；`ok`（抓取是否成功）、`gathered` / `filtered` / `emitted` 各階段條目數；對不回註冊名的計數歸入 `"_unmapped"` 桶 |
| `totals` | 三階段總數 |

## classification-log.jsonl

主編當天分類判斷的完整留痕（append only，同 URL 同日最後一行勝出），`[加入: 2026-09-15]`。**記全部原料，不只記排除**：起因是使用者稽核 2026-09-14 那輪發現主編分類完全沒有留痕——70 則原料有 13 則從未進任何派工訊息，其中至少 2 則是漏判。只記排除對不了帳，「忘了處理」和「判斷排除」在帳上都是沒出現；記全部之後才能用 `scripts/check_classification_log.py` 對原料逐 URL 核對。

Schema（每行一筆）：

```json
{"date": "YYYY-MM-DD", "url": "...", "title": "...", "source": "...", "summary": "去 HTML 摘要 ≤240 字", "categories": ["功能"], "reason": ""}
```

`categories` 空陣列＝主編未派給任何記者，`reason` 必填。分類回退後追加派工的條目 append 一行新紀錄補上目標類別，不改舊行；寫錯也是 append 更正行，對帳腳本只看同 URL 的最後一行。

**2026-09-14 那 70 行是 2026-09-15 事後重建**（帶 `backfill` 欄），不是當天寫的——它是這個機制上線前那一天的分類，用來當第一批可對帳的資料；之後的日期沒有 `backfill` 欄。

輪替：帳本一年約 25,000 行，`load_log()` 每次全讀。超過一年時把舊年份搬到 `classification-log-YYYY.jsonl` 歸檔，主檔只留當年；對帳只查目標日期，歸檔檔不必載入。

寫入時機：主編分類完成、派工前，寫完跑 `python scripts/check_classification_log.py --date <date>`。exit 1（原料未進帳本、排除無理由或摘要不可讀、未知類別）不得派工，append 更正行修到零；⚠️ 警示（URL 打錯、壞行）不阻斷，因為它們掩護不了任何一則原料。exit 2＝腳本判定逾 14 天保留窗，可跳過對帳；exit 3＝窗內缺檔，是抓料缺件，不得跳過。分類複核記者（`wiki-reporter-classify-review`）與六記者同批派出，讀 `categories` 為空的行覆核，判定誤排除則走「分類回退」同輪追加派工（`.claude/skills/wiki-ingest/SKILL.md` 步驟 3b、`.claude/skills/wiki-ingest/references/dispatch.md`「3b／3c」）。

## build_flags_history.jsonl

出貨 Claude Code 程式本體的旗標差異帳本（append only，一版一行），`[加入: 2026-09-15]`。寫者是 `src/news_aggregator/sources/build_flags_watch.py`（每個新版本比對 `CLAUDE_CODE_*` 字串），讀者是 `wiki/topics/claude-code-experimental.md` 與 `scripts/build_flags_mentions.py`。

Schema：

```json
{"date": "YYYY-MM-DD", "from": "2.1.271", "to": "2.1.272", "added": [...], "removed": [...], "candidates": [...], "plumbing": [...]}
```

`candidates`＝`added` 裡看起來像功能的（設定類字尾以外）；`plumbing`＝逾時、識別碼等。首行是 2026-09-15 探針回填的十日跨版差（帶 `backfill` 欄），之後每行是單版差。狀態檔 `src/news_aggregator/sources/build_flags_state.json` 存最後一版的完整旗標集，兩者都由 daily-gather commit。

## pending-handoffs.jsonl

記者間「轉知」帳本（append only，最後一筆勝出），`[加入: 2026-08-15]`。跨記者交辦（如社群記者發現新工作模式要功能記者評估產品化矩陣）過去靠主編口頭轉達、無接手驗收；現在照 `pending-signals.jsonl` 的同構做法走閉迴路：主編 `open` 登帳 → 派工時 `list` 附清單 → 記者回報「轉知處置」→ 主編 `close`／`void`。

一律用 `python scripts/pending_handoffs.py {open|list|close|void}` 操作，不手改。行格式：
- 開立：`{"id":"H-xxxxxx","opened":"YYYY-MM-DD","from":"社群","to":"功能","page":"topics/...","note":"...","status":"open"}`
- 結案：`{"id":"H-xxxxxx","closed":"YYYY-MM-DD","status":"done|void","by":"功能","result":"..."}`

id 由（開立日、來源、目標、note）雜湊而來，同一交辦重複開立冪等；`list` 對逾 14 天未結案者標 ⚠️。

## `link_health.json`

wiki 外部連結的健康快照，**唯一寫者是 `.github/workflows/weekly-linkcheck.yml`**（排程見該檔，純 stdlib HEAD 請求、不含 LLM），唯一讀者是 `/wiki-lint` 指標三。

| 欄位 | 意義 |
|---|---|
| `checked_at` | 檢查日期。**消費端必須驗新鮮度**——距今 > 8 天視為過期，不得據以標註頁面（門檻須小於週更間隔，否則漏跑一次不會被發現）|
| `total_unique_links` / `checked` / `ok` | 掃描規模與正常數 |
| `dead[]` | **確認死鏈，只認 404/410**——唯一會驅動頁面標註的桶 |
| `mode` | `full`（每月 1–7 號）或 `incremental`（其餘週次：只驗新連結 + 上次非 OK 者，其餘沿用上次結果）|
| `ok_urls[]` | 本次判定正常的連結全集，供下次分層掃描比對「哪些是新的」|
| `anti_bot[]` | 401/403/429（付費牆、登入牆、限流）。**不算死鏈**、不派工，僅列數字 |
| `unverified[]` | 逾時／連線失敗／5xx，且已用較長逾時重試一次仍失敗。證據不足以判死，不派工；**連續多週落在此桶才值得人工看** |

覆寫式快照（非 append），歷史留在 git。**分層模式下報告仍是完整清單**——沒掃到的連結會沿用上次結果補回，否則 lint 會讀到縮水的死鏈清單、把仍失效的連結當成已修好。分層是省請求，不是省結論。產出這個檔的理由見該 workflow 檔頭：這步是純網路、不需 LLM，套用分裂架構後就不再需要本機。

三桶分類的由來：2026-08-20 首次全量掃描 795 條，舊的「非 2xx 即死鏈」判出 58 條，實際只有 5 條真死。把 401（付費牆）與單次逾時判成死鏈，會讓記者把活著的來源標成失效——污染頁面的成本遠高於漏標一條死鏈。
