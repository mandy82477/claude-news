> **2026-11-05 註：** 評審 🔴1–2、🟡3–6 已由 `fix_review.py` 套用，數字為修法後（參考來源 46→31、照搬 83 行）；與評審檔相反處以評審檔為準。

# 第 27 波設計提案：entities/dario-amodei 核心論述改回主張、事件留給歷史記錄（2026-11-05）

> 上游：健檢卡 `dario-amodei-2026-11-05.md`、冷讀者 `wave27-cold-reader-2026-11-05.md`、查證 `dario-amodei-2026-11-05-verified.md`（含第四節安保費算術）。十個裁決點照 ledger「2026-11-05｜第 27 波」條，不重開。
> 機械產物在 `<scratchpad>/w27/design/`（下稱 `D/`）：`newtext.py`＋`urls.py`（新字單一來源）、`build.py`（斷言原檔 1–213 每行恰消費一次；開頭比對 commit `d6afcdb` 五檔 blob 且工作樹乾淨）、`verify.py`（獨立核對：照搬逐字、懸置去 slug、archive 一字不刪、砍列事實有家、自指錨點、禁留字樣）、`moves.py`（cell／reader 對照）、`rules_patch.py`（daily.md 整檔 sha256 鎖；pages.md 須不存在）、`before.sh`、`gates.sh`、`rebuild_after.sh`（一鍵：build → verify → 建 `tmp_after` → 規則檔 → 全閘 → 再 verify → moves；`set -u -o pipefail`）、`redtest.sh`、`make_map.py`、`make_draft.py`、`out/wiki/entities/`（五頁改後全文）。行號一律指原檔。

## 1. 推薦案（一個）

使命句（裁決 2）放在標頭欄位之後、callout 之前：「本頁回答：他是誰、現在公開主張哪幾件事（各附本人原文出處）、誰在公開反對他、與白宮的關係走到哪；主張的論證與後果在各議題頁。」（位置見 N1）

| 節（改後） | 行（含標題與空行，合計 149） | 內容 |
|---|---|---|
| 標頭＋使命句＋callout | 20 | callout 只留 10-29 安保費一則：算術改正（verified 第四節）＋當日歸因網址（Google News／Fortune）＋The Next Web 細項 |
| `## 現況` | 6 | 兩段：①他現在主張什麼（09-12 文章、09-23 安理會；十月只見兩則媒體轉述）②白宮關係、IPO、薪酬與安保，各一句指路 |
| `## 核心論述` | 17 | 主張清單 10 列＋一句指 RSI 的 Dario 段 |
| `## 公開批評者對照` | 18 | 判準句＋9 列（補 3 列）＋一句指 RSI#目前結論 |
| 角色與影響 | 7 | 補 Daniela Amodei；L81 聯署信改住這裡 |
| 相關議題 | 15 | 去重 2、補 5 |
| 參考來源 | 34 | 46→31 條 |
| 歷史記錄 | 32 | 10、09 月留；08 月蒸成 5 行總結 |

主頁 213→**175 行**（正文 187→149），archive 62→83，鄰居三頁行數不變。原 213 行：照搬 120／行內改 18／進 archive 13（4 行改指路）／改寫 38／砍 19／結構 5（逐段見 map 第二節）。

## 2. 主張清單（裁決 1；逐字在 draft E 節）

| # | 主張 | 最近一次 | 本人原文 |
|---|---|---|---|
| 1 | 前沿 AI 放慢並受監控、三步驟、6–12 個月警告 | 09-12（09-15 重申） | 本人網站〈We Must Pace the Frontier〉 |
| 2 | 中國是最棘手的兩難 | 09-13 | 僅媒體轉述（CNBC） |
| 3 | 不主張禁開源權重；晶片出口管制、打擊蒸餾、開閉源都強制安全測試 | 07-27 | 官方部落格、本人署名（verified #1 補全三項） |
| 4 | 範圍限定的國際協議、互相查核、共同測試與事件通報 | 09-23 安理會 | 僅媒體轉述（gov-policy L677 的出處） |
| 5 | 反彈是信任危機、要靠治癒癌症扭轉 | 08-16 | 本人 X 貼文（Simon Willison 全文引述） |
| 6 | 無意取代 SaaS、「not interested in destroying anyone」 | 08-26 | CNBC 逐字稿 |
| 7 | 文化決勝、40% 工時 | 10-17（06-08 首見） | 僅媒體轉述（Fortune） |
| 8 | 政府應能阻止危險模型發布 | 06-10 | 僅媒體轉述（Bloomberg，網址取自 news/2026-06-11） |
| 9 | 「壓縮 21 世紀」目前還做不到 | 07-06 | 僅媒體轉述（STAT） |
| 10 | 同業應對模型能力透明誠實 | 10-03 | 僅媒體轉述（WSJ 經 Yahoo） |

移出的 8 列非立場（L62 安保、L64 薪酬、L72–74 白宮、L75 FT 字詞密度、L77 扁平組織、L80 速率翻倍）與 L70 內部談話：每列的事實在歷史記錄或 archive 已有原字（`verify.py` 第 5 項逐筆驗）。每格實測 ≤120 字元（網址不計）。

## 3. 批評者表（裁決 3）

判準句：「列入本表的是具名的人或政治陣營，公開、直接點名 Amodei 或 Anthropic 的減速呼籲或風險示警；媒體評論文章不列。「何時」是發言日。」補三列，各附出處：Gavin Baker（08-16 前，[TechCrunch](https://techcrunch.com/2026/08/16/anthropic-ceo-says-ai-backlash-is-fundamentally-a-crisis-of-trust/)，網址取自 news/2026-08-17）、Mark Zuckerberg（09-16，NYT 經 Google News，僅標題）、川普陣營盟友（09-24，Axios 直連，取自 gov-policy L683）。全表依「何時」重排；既有 6 列原字不動。

## 4. 參考來源（裁決 4）

- 砍 15：白宮晚餐留最早 WSJ（L134），L135–139 五家來源的家在 gov-policy 攻防紀錄 09-28 列；L132、L146、L153、L155、L157、L162 同事件另一篇；L166 與 L167 同網址；L150–151 換成減速文章一手一條；L170 無連結（家在 archive L43）；L171 裸日報連結。
- 改 9：L141 標籤「聯合國大會」→「聯合國安理會簡報」；L152 補 ITV（verified 來源）；L156 補 TechCrunch；L158 補 Simon Willison 網址；L161 補 The Information 直連並改指 archive；L163 補 The Next Web、Fortune（原住 ⟨Q-01⟩ 細節）；L164 補官方連結、日期改 07-27；L168 補 Bloomberg 兩條；L169 補 Fortune。
- 剩下無連結的 0 條。

## 5. 減速文章與日期（裁決 6、10）

本頁：L193 改 09-12 並寫出標題；主張清單第 1 列附原文；細節區換成一句指 [[topics/recursive-self-improvement]] 的 Dario 段（錨點＝該 h3 原文，建置會驗，見閘表驗紅 6）。Musk「psyop」（09-11）與「Dario is right」並陳在這一句（冷讀者 §6）。鄰居 burry L55、vembu L59、jack-clark L64 改 09-12。L50 改指 anthropic-ipo（現況第二段）。RSI 的日期走 handoff 2。

## 6. 蒸餾（裁決 8；page-lifecycle：11−8＝3，錨點入邊 0）

歷史記錄×08（L194–207，含 L200、L203–204 兩則 callout）原字進 archive `## 2026-08`，L40–41 航空業 callout 接在 08-24 條下。主頁留 5 行總結：信任危機與 Baker、CNBC 專訪、Fortune 與 The Information、為錢不為使命（查實為內部談話）＋面試實務。例外 2 不成立：新 callout 與現況都不引 08 月事實。cell 基線因此釋出 6 槽（08 月 5、L158 1），本機下次 `--rebuild` 時自然收緊。

## 7. 懸置收尾（裁決 7）

- ⟨Q-01⟩⟨Q-02⟩：兩筆都已查實，細節區刪除；Q-02 原話寫進主張清單第 6 列與 archive 08-28 條（L194），Q-01 的事實與兩條連結併進 L200 引文（成為「為錢不為使命」唯一的家）。
- 🔎 L200：改寫為事實並移除標記（daily-contracts「誰可以動這個標記」主編欄），L202「見上方標記」同步改指。L196「具體論點未見報導」改成「論點 09-20 查實，見下方引文」。
- **計數閘明示**：L200 的欄位順序是「訊」在「複」前，不合 `scripts/pending_markers.py` L36–44 的 `PENDING_RE`（複在訊前），從來沒被計入；⟨Q-01⟩⟨Q-02⟩ 前無 ❓／🔎，也不符 L46 `SHORT_RE`。所以全庫 223→**223**、舊字樣殘餘 18→18、五頁 2→2，**不需 `--rebuild-count`**。

## 8. 規則檔（逐字在 draft N、O 節；臨時副本實套後 `check_rules.py` ✅）

- **新開 `people/pages.md`**，一頁一節，先放本頁節：這頁答什麼＋四個「不收→去哪」；觸發條件；標頭下一句；現況兩段；主張清單（一主張一列、改寫不加列、只收本人公開發言、本人原文四種才算否則寫「僅媒體轉述」、上限 10、不因時間移出）；批評者表（判準、「何時」寫發言日、無人物頁者格內附出處、找不到出處不收）；參考來源一事件一條且須有連結；每日四步；蒸餾照 page-lifecycle。
- `people/daily.md` L3 改指 pages.md；L16 本頁觸發條件改三類；L30 加一句「pages.md 有該頁節的照該節寫」。
- 角色檔 `.claude/agents/wiki-reporter-people.md` 不改：它要求必讀 daily.md，daily.md L3 已指 pages.md。腳本、測試、`data/*baseline*.json`、`data/*-allow.json`：**0 改**。

## 9. handoff（主 session 先 `--dry-run`；兩筆已在 `tmp_after` dry-run 過負責人驗證：H-41afbb、H-d41c04）

| # | --from → --to | 頁 | 事項 |
|---|---|---|---|
| 1 | 人物 → 主編 | index | L72 鉤子改「Anthropic CEO：現在公開主張哪幾件事（附本人原文；減速論證在 [[topics/recursive-self-improvement]]）、誰公開批評他、與白宮的關係」——拿掉「六位」與點名（裁決 3） |
| 2 | 人物 → 安全政策 | topics/recursive-self-improvement | L55「Burry 稱『自利』，09-17 報導」改「Burry 09-14 稱『自利』」；時序 `### 2026-09-17` 的 Suleyman（L372）、Burry（L373）兩行移到發言日 `### 2026-09-16`、`### 2026-09-14`（新開）；技術彙整標題的「新增」日不動（裁決 10） |

## 10. 閘（`D/tmp_before`＝HEAD 工作樹原樣；`D/tmp_after`＝套本案五頁＋規則檔；`bash D/rebuild_after.sh <repo>` 一鍵重跑，輸出在 `D/gates_before`、`D/gates_after`、`D/rebuild_out.txt`）

| 閘 | 改前 | 改後（原樣） | 驗紅（`D/redtest.txt`） |
|---|---|---|---|
| `build.py` 防呆 | — | `ok {'main': 175, 'archive': 83}` | 對改後樹跑 → `AssertionError: … 自設計 commit d6afcdb 後被改過`（1） |
| `verify.py` | — | 照搬 84 行逐字；懸置五頁 2→2；`結論：OK` | 刪聯署信行 → `事實字串不見`、FAIL（2）；`[[#核心論述]]` 打錯 → `自指錨點對不到標題`、FAIL（7） |
| `gen_wiki_frontmatter.py` | exit 0 | exit 0；本頁 `pending_count` 0→0 | — |
| `check_hierarchy.py` | ✅ 32 個母頁 | ✅ 32 個母頁 | — |
| `check_pending_markers.py` | ✅ 223 筆（基線 223） | ✅ 223 筆（基線 223）；舊字樣 18→18 | 見 §7 |
| `check_wiki_freshness.py` | OK 143 頁 | OK 143 頁 | callout 10-29＝最後新聞更新，附當日歸因網址 |
| `check_rules.py` | ✅ | ✅（規則檔已套） | — |
| `check_cell_limits.py` | OK 無新增 | **OK 無新增**；本頁命中 7→1（L159 原字配回 201≤201）、新寫 0、釋出 6；鄰居 0→0 | 相關議題一列加長到 >200 → exit 1（3） |
| `check_reader_language.py` | OK | **OK**（五頁新寫 0） | 使命句寫「結論層」→ exit 1（4） |
| `build_web.py` | 斷鏈 23／錨點 WARN 0，exit 0 | 斷鏈 23／**錨點 WARN 0**，exit 0 | gov 錨點截字 → 錨點 WARN 1、exit 1（5）；RSI 長錨點截字 → WARN 1、exit 1（6） |
| `run_tests.py` | 1,334 案 OK | 1,334 案 OK | — |

cell、reader 兩閘都是 0 筆新增，本波不需要本機 `--rebuild`／`--allow-grow`。

## 11. 新裁決點（主 session 判）

- **N1** 使命句放標頭後、callout 前，不放 H1 下：page-templates L43 規定人物頁 H1 下不另寫「這是什麼」句（由「身分」回答）。pages.md 把這一句寫成契約。
- **N2** 批評者判準字面從 ledger 的「減速論述」放寬為「減速呼籲或風險示警」、批評方從「具名的人」放寬為「具名的人或政治陣營」。不放寬的話，ledger 點名要補的 Baker（批的是 08-16 前的悲觀描繪，早於減速文章）與川普陣營（備忘錄作者未具名）都不合格，判準句就會是假話。放寬後仍不收：Musk「psyop」（09-11，對象是研究員示警，隔天轉為支持）、Fortune 航空業評論（媒體評論）。
- **N3** 08 月條目進 archive 時改 4 行指路（L194、L196、L200、L202）。理由：懸置查實後要改寫為事實（daily-contracts L99），而且原句指向的「上方公開立場表格標記」「頁首標記」在改後都不存在了。這是 archive「一字不刪」的例外，`verify.py` 第 3 項只放過 archive 原有的 L34、L37。
- **N4** 「公開批評者對照」不改名成模板的 `## 爭議`，當作模板允許的專有段。page-templates L113 禁止的同義名只有核心論述與相關議題兩個。
- **N5** 主張清單 10 列中 7 列是「僅媒體轉述」，照實寫，不補猜的網址。L110「呼籲政府不應妨礙州級 AI 法律」沒有出處（V7），不在裁決內，本波不動。
- **N6** 冷讀者想要的「說過 vs 後來」一節不開：ledger 沒裁，RSI L56 明文不判應驗。主張清單第 9 列是本庫唯一有的對照。
- **N7** L141 與 L142（安理會簡報的預告和內容）、L131 與 L133（09-29 同場，但兩條講的事實不同）判成不同事實，四條都留。
- **N8** 主張清單第 8 列的日期從 06-11 改成 06-10（Bloomberg 網址日）。archive L52 的 06-11 是原字，不動。

## 12. 不選的方向

- 收窄成路由卡、核心論述只留指路：ledger (2) 已否，違反 page-templates L113。
- 主張清單改成條列（jack-clark 式）：四欄有得比（來源硬度、日期），所以用表。
- 只清掉 8 列非立場、保留事件流：ledger (1) 選改成主張清單。
- 批評者表維持「有人物頁才收」：ledger (3) 否。
- 歷史記錄×09 一起蒸：11−9＝2，未達門檻。
- 08 月原字照搬、不改指路：會留下 3 句指向不存在的標記與表格（冷讀者 §5 第 8 條同類）。

**可行性前提**：同一個 commit 含五頁、`people/pages.md`（新檔）、`people/daily.md`、ledger 定稿列、handoff 1–2 開帳。跑 `build.py`／`rules_patch.py` 時，五頁仍須是 `d6afcdb` 版，daily.md 整檔 sha 不能變，pages.md 也不能已存在；否則先紅，續用設計者重跑，不准手改。今天 11-05 的 ingest 若先動到本頁或三個鄰居，第 0 步就會擋下。

## 13. 最不確定的一件事

主張清單收哪些、怎麼切成「一項」。第 2 列（中國兩難）可以算成第 1 列的但書，第 10 列（透明誠實）的出處是轉述的轉述。條文只規定「一主張一列、只收本人公開發言」。第 1 列和第 2 列分開放，是因為兩者的來源硬度不同（本人網站 vs 僅媒體轉述），併成一列，讀者就看不出哪一句有原文。這樣切讀者分不分得出來，要看原考題複驗 Q1。
