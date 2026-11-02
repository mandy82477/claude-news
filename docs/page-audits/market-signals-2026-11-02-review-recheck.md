# 第 22 波評審複核：market-signals 拆頁實作（2026-11-02）

> 複核對象：實作 commit `7ec4d2b`（及 `b1ab51d` gen、`0ea2e1a` web、`0312981` 作廢註、`c764cc9` 冷讀者複驗修正）。上一輪＝`market-signals-2026-11-02-review.md`（🔴1–3、🟡1–5、實作單 10 步）。
> `D/`＝`<scratchpad>/w22/design/`；我的暫存在 `<scratchpad>/w22/recheck/`。沒做 git 寫入、沒改 repo 檔。附帶：`build_web.py` 重寫了 `web_reader/{data/data.js,index.html,sw.js}`（版本戳＋兩列 hub 順序對調），`scan_pending_verifications.py` append 了 `data/pending-signals.jsonl` 7 行，兩者都已用 `git show HEAD:<檔> > <檔>` 還原，`git status` 乾淨。

## 結論

- **有條件放行**：🔴 1 條（本輪新發現，修法一行指令）、🟡 3 條。10 步裡照做 7 步、偏離 2 步（都可接受）、漏做 1 步（第 10 步）。
- 頁面、腳本、規則、基線、閘的數字全部和實作單對得上；第 21 波那組紅不多不少（cell 107、reader 2、unittest 1 FAIL），本波貢獻 0。

## 逐步表

| 步 | 判 | 證據 |
|---|---|---|
| 1 | 照做 | `git rev-parse 7ec4d2b^:wiki/topics/market-signals.md`＝`e12d896`；`7dbc92e..7ec4d2b^` 之間只有 page-audit commit |
| 2 | 照做（有一處已知偏離） | `D/scripts.diff` 不再含 `check_wiki_freshness`（`grep -c` 0；hunk 只剩 build_web、pending_handoffs、pending_markers、scan_pending、2 支測試、app.js）；`wc -l D/attribution_1029.jsonl`＝1。`7ec4d2b` 的 `+/-` 行和 `D/scripts.diff` 逐行相同。M_SUBS 第 58 行改走 `take_e(58,58)`，所以照搬行數從 1084 變 1083，與 commit 訊息一致 |
| 3 | 偏離（可接受） | proposal／draft／map 正文沒有改，只在檔頭加了「文中相反的句子作廢」註（`0312981`，三檔各 +2 行）。因此實作單第 3 步的 grep 驗收仍會命中，但不會誤導讀者 |
| 4 | 照做 | `python -I D/verify.py D/tmp_before <repo>/wiki/topics` → `照搬行逐字核對 1083 行；懸置標記 69→69（母 0／A 19／B 21／C1 12／C2 17）`、`結論：OK` |
| 5 | 照做 | `check_hierarchy` `✅ 通過（32 個母頁）`；index L138 投影出四子頁；鉤子 67 字，≤120 |
| 6 | 照做 | `data/pending-marker-count.json` 的 diff 是 −69（market-signals）、＋69（ipo 19／legal 21／compute 12／customers 17）；note 用的是指定字串；gate 印出 `212 筆（基線 212）` |
| 7 | 偏離，handoff 4 **有誤**（見 🔴A） | 開了 4 張單：H-5978d7、H-a450ba、H-5f3c59、H-6109b3（`data/pending-handoffs.jsonl` 末 4 行）。H-5f3c59 補了 🟡3 的句子，但少了「跑 build_web 確認錨點 WARN 不增」（🟡C）。log 的 Query 條目帶了單號和「補 1 筆、3 筆不補」；`check_log_handoffs` 綠 |
| 8 | 照做 | freshness `OK…138 頁`；rules `✅`；build_web `斷鏈 WARN 23／錨點 WARN 0`；四支測試 75 個案例全 OK；`run_tests` 只有第 21 波那組紅（見下） |
| 9 | 照做 | 在 `claude/stoic-edison-ewvmcx` 上，已 push（`origin/...` 含 `7ec4d2b`）；`git show --stat 7ec4d2b` 不含 `scripts/check_*`、`data/*baseline*`、`data/*-allow.json` |
| 10 | **漏做** | ledger L59 第 22 波那列仍寫「進行中。主編查證已交」；全檔 grep `116／494`、`69→69`、`補 1 筆` 都沒有命中（🟡A） |

## 抽驗新文字是否照 verified

- **S-1 已公開**：母頁摘要寫「公開版 S-1 已於 10-26 提交、尚未生效，股數、價格區間與掛牌日都未公布」。ipo 里程碑 L505 把過期句改寫成「已過時（2026-11-02 查證）…『10 月上市』的預期落空」。和 verified #1、#7 一致。
- **807 億非現金**：ipo L152 判讀補了「724 億是可轉換票據、衍生負債與 SAFE 的公允價值變動（非現金…）」；「現在怎麼判」L49 是同一口徑。和 verified #2 一致；原檔 `724` 出現 0 次。
- **GSA 10-27**：legal L62 寫「官方部落格 10-27 宣布…『OneGov』是媒體用語」，callout L42 也寫 10-27。小標的 `（2026-10-28）` 是判讀日，不算錯。
- **PBF**：ipo L163、L167 寫「撥入新設的全資子實體」「董事會可額外加碼」。和 verified #6 一致。
- **🟡4／🟡5**：母 L62 表頭已改「相關判讀（所在子頁見…）」，pages.md L26 也改成「相關判讀」；compute L49 補了評等面，並指到 ipo。

## 硬數字

- **正文行（body_lines）**：母 116（`7ec4d2b`），`c764cc9` 補「曝險多大」後是 122；ipo 494、legal 483、compute 304、customers 513。母頁 ≤300、子頁 ≤600 都過。
- **run_tests**：cell 閘 107 筆，全在第 21 波頁面（known-issues 86／releases 15／features 6）；reader 閘 2 筆（known-issues L281、releases L236）；unittest 1 FAIL＝`test_check_cell_limits…no_new_hits`。三者都沒有 market-signals。
- **網站 💰**：`parse_market_signal(market_signal_pages())` 會讀五頁，回傳 `{date: 2026-10-31, title: FT／TechCrunch：Blackstone…BB 級信評…, page: market-signals-ipo}`，app.js L327 用 `d.marketSignal.page` 開頁。但 10-31 有 `daily/2026-10-31.md` 讀者版，build_web L1853 依設計不注入，所以 `digest/2026-10-31.json` 的 `marketSignal` 是 null。站上可見的是讀者版 L49 的 `[[topics/market-signals|投資訊號判讀]]`，指到母頁，母頁 callout 再指 ipo，要多點一下。這是設計行為，不是缺陷；下一個沒有讀者版的判讀日才會直達子頁（推論）。

## 發現與修法

**🔴A H-a450ba 派錯人，記者寫不了 market-lessons。** 主 session 改派的理由是「market/weekly.md 規定投資分析記者週更」，但規則檔寫的正好相反：
- weekly.md L3：5h「由**主編親做**」。
- pages.md L30–31：`market-lessons` 兩張表都是「**主編，每週**（5h）」。
- agents/wiki-reporter-market.md L29：記者「**只寫** market-signals 與四子頁」。
- ledger L126 (3) 自己也寫「market-lessons…記者唯讀」。

照 🔴2 修好之後，wiki-ingest 4c 會把「→ 投資分析」轉知附給記者，等於叫記者去改一頁它不准寫的頁。修法（`--to 主編` 不做負責人核對，所以不用 `--force`）：
```
python scripts/pending_handoffs.py void H-a450ba --result "改派主編：market-lessons 由主編 5h 週更、記者唯讀（weekly.md L3、pages.md L30、agent L29、ledger L126(3)）"
python scripts/pending_handoffs.py open --from 主編 --to 主編 --page topics/market-lessons --note "第 22 波拆頁：消息線表與 #回顧結算 的連結改指四子頁（一線一列各指其子頁；合計表留母頁）；IPO 線「18 則 · 10-21」更新為 21 則 · 10-31；下次 5h 做"
```
log 的 Query 條目照實補一行：`- 轉知更正：H-a450ba 作廢改開 H-xxxxxx（→主編，market-lessons 屬主編 5h）`。改完跑 `check_log_handoffs.py`。

**🟡A 第 10 步沒做。** ledger L59 那列改成：`定稿（主 session 自決，使用者授權）：拆母頁＋四子頁 ipo／legal／compute／customers；正文 116／494／483／304／513（複驗後母 122）；懸置 69→69；rebuild 212，＋69／－69 全在子樹；N2 補 1 筆（Citywire）、3 筆不補；check_wiki_freshness.py L78 說明字串屬閘檔，留使用者本機改；run_tests 紅只限第 21 波那組`，後兩格填 `7ec4d2b` 與本檔、`-review.md`。

**🟡B proposal 正文和實作不一致**（第 3 步偏離）：檔頭註已經作廢了相反的句子，可以接受。若要讓第 3 步 grep 歸零，照上一輪 🔴1、🔴3 的修法逐字改 proposal §5 L58、「腳本 6 支→5 支」、§7、§8 N2。不改不擋放行。

**🟡C H-5f3c59 結案條件少半句。** 結案時 `result` 要寫：`已刪母頁 h4 殼三行；build_web 錨點 WARN 0→0`。不必改帳本，只要在結案那一步照做。

**觀察（不擋）**：`c764cc9` 的「曝險多大」寫「分三型看」，但下面有 4 條；第 4 條是「本體買不到」的附註。可以改成「分三型看（另附一句本體）」，也可以把第 4 條移出條列，變成一句普通段落。

## 放行

🔴A 那兩行指令跑完、log 補一行、`check_log_handoffs` 綠，再補 🟡A 的 ledger 定稿列，就放行。頁面、腳本、基線不必重做。
