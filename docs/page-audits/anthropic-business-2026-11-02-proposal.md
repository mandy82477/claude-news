# 第 23 波設計提案：topics/anthropic-business 拆成母頁＋兩新子頁，營收估值併入 anthropic-ipo（2026-11-02）

> 上游：健檢卡 `anthropic-business-2026-11-02.md`、冷讀者 `wave23-cold-reader-2026-11-02.md`、查證 `anthropic-business-2026-11-02-verified.md`；切法與八點照 ledger「2026-11-02｜第 23 波」條，不重開。
> 機械產物在 `<scratchpad>/w23/design/`（下稱 `D/`）：`newtext.py`（新字單一來源）、`split.py`（切頁；斷言 business 1–1,048、ipo 1–211 每行恰消費一次，開頭比對 commit `702e5a6` 的六個檔 blob，被每日 ingest 改過就先紅）、`verify.py`（獨立逐字核對＋懸置去 slug 比對，第二參數可指向任一份改後副本）、`moves.py`（cell／reader 兩閘子樹命中改前改後對照）、`rules_patch.py`（規則檔逐字）、`rebuild_after.sh`、`gates.sh`、`make_map.py`、`make_draft.py`、`out/wiki/`（五頁＋鄰居三檔改後全文）、`redtest.txt`。行號一律指原檔。

## 1. 推薦案（一個）

照裁決甲案：母頁留指標表、IPO 一句、子線路由、人物、公司動態時序與時段總結；合作與算力、風險與商業模式各開一頁；營收估值與數字出處併進 anthropic-ipo，改標題「上市與財報」。先蒸 08 月時序（→ archive `## 2026-08`）與 07 月合作清單＋細節，再切。

| 頁 | 使命一句 | 節清單 | 正文行 |
|---|---|---|---|
| 母 `topics/anthropic-business`「Anthropic 商業健康度」 | Anthropic 的錢現在是什麼狀況、外面拿哪些數字在賭它，以及哪幾件事會反過來改到你用的 Claude——合作與算力、風險各往下鑽，上市與財報在 anthropic-ipo。 | 使命／標頭／callout／現在的數字（兩段最新＋指標表 10 列）／IPO 走到哪一格／**往下鑽：三條子線**（路由表＋4 個指路殼）／上面提到的人是誰／相關／參考／時序（公司動態 8 則、未歸類、08·07·06 時段總結） | **189** |
| `topics/anthropic-ipo`「Anthropic 上市與財報」 | Anthropic 的上市走到哪、S-1 和財報寫了多少營收和虧損、這些數字是誰說的——數字和原文在這頁；該打幾折、誰的股票有感，在 market-signals-ipo。 | 上市走到哪一格（五格＋估值算術＋結論＋### 誰說撐不住）／S-1 揭露了什麼（+2 列）／數字細節／這些數字是誰說的（9 列）／IPO 細節／時序（57 則）／相關 | **396** |
| 新 `topics/anthropic-partnerships-compute`「Anthropic 合作與算力：跟誰簽、算力從哪來」 | Anthropic 跟誰簽了合作、算力和資金從哪來、跟三大雲各是什麼關係，以及哪幾筆會改到你拿得到什麼、付多少——事實和數字在這頁；同一筆交易怎麼判讀，在 market-signals-compute 與 -customers。 | **跟三大雲各是什麼關係**（新）／算力與資金從哪來／哪個合作會改到你用的 Claude（表＋清單 08–10＋07 彙整＋05–06 彙整＋細節）／這些數字是誰說的（5 列）／時序（88 則）／相關 | **449** |
| 新 `topics/anthropic-business-risks`「Anthropic 風險與商業模式：哪裡會出事、怎麼賺錢」 | Anthropic 哪裡會出事、你能先做什麼，以及它靠什麼賺錢、產品有沒有人要——事實和你的選項在這頁；官司與監管消息該打幾折，在 market-signals-legal。 | 還沒過去的風險（6 列，新進 1、UTRF 讓位）／商業模式／PMF／這些數字是誰說的（7 列）／時序（56 則）／相關 | **312** |

- 正文以 `check_page_thickness.body_lines` 在臨時副本過 gen 後量；四頁都在 150–600，母頁 < 300。archive 401→565 行。business 原 1,048 行的去向：母 166／ipo 151／合作算力 317／風險 198／archive 159／結構空行 56／砍 1（`accounting.txt`）。
- **名字分得出 market-signals**：事實頁用「X 與 Y：發生了什麼」名詞＋問句，判讀頁是「這則怎麼判」。每頁使命句後半是互指句「事實在這、判讀在那」，各指一頁 ms 子頁（ipo→ms-ipo、合作算力→ms-compute＋ms-customers、風險→ms-legal）；母頁路由表上方一句總指 market-signals。ms 那一側的對稱句是跨維護者，走 handoff 2(e)。
- **三大雲對照表放合作算力**，不放母頁：表裡每格都是出資／算力／通路事實，家在算力表、google-investment、pricing、ipo 的 S-1 表；放母頁等於在「索引＋結論」層多一張每週要對帳的事實表。代價是 Q4 從 index 起 2 跳（現在 3 跳、15 處行號）；index 鉤子補「含跟 Google／Amazon／Microsoft 的關係」。表的契約寫進 pages.md 第 12 條（三列固定、週更覆寫、每格一句加連結）。
- **風險表補三類**（虧損、客戶集中、供應商依賴）：三者觸發同一個讀者動作（關鍵工作流換得了供應商），照第 4 條「同一個讀者動作合為一列」併成一列；表滿 6 列，照留表優先序讓位者是 UTRF（「你能先做什麼」＝沒有繞法、⚠️ 中、最後動態 08-24），表下一句點名、細節區加註（新裁決點 N1）。表下補一句「個人訂閱用戶最直接相關的兩列」，取自「誰會遇到」欄，不另立排序。
- **一事一家**：S-1 數字住 ipo「S-1 揭露了什麼」，風險頁新列與細節只指過去；business L242 訓練暫停改指路（原本兩頁各寫一次）。唱空五則（L266–267、L283–285）搬進 ipo「誰說撐不住」，ipo 自己指出去的三筆錨點變頁內。
- **時序第二副本**照裁決 (3) 原文照搬不去重；L774 Eisman 設計者改歸 ipo（細節已去 ipo）。子頁時序裡「詳見『算力與資金從哪來』表」這類引號節名多數仍對（同頁），跨頁的少數不改字，列 `/wiki-lint` 候選。

## 2. 08 月蒸餾範圍（page-lifecycle L84：11−8＝3）

- **時序 × 08**（L900–1016，117 行、71 則）：例外 1 無錨點（`wiki_graph explain --section 2026-08` 0 筆）；例外 2 主編核過的那一處（算力表 L311「上市前信用額度逾 100 億（08-18）」）表列自己寫著、ipo L166 另有細節，不成立；例外 3 狀態 ongoing。→ archive 新開 `## 2026-08`（日標頭 h4→h3，其餘一字不刪），母頁留 13 行時段總結（9 條各 ≤200 字、末行 `原始條目見 [[topics/anthropic-business-archive#2026-08]]`）。
- **合作節 × 07**：清單 30 列（L433–437、L439–463）＋同節「戰略合作細節」07 月 12 條（L517–521、L523–529）視為同一時段（同一個 h2 區塊 × 07 月；N3）→ archive `## 2026-07` 末新節「其餘合作彙整（…2026-11-02 蒸餾搬入）」，比照 09-20 那次的 06 月節頭。合作算力頁留一段 07 月彙整（30 筆點名，末句指 archive）。L438 Amir Salek 是 08-21，留下。
- 每頁每輪 2 個時段，剛好用完。08 月清單 29 列與 08 月細節 12-01 到期，留給下次 lint。ipo「IPO 細節」07／08 月也到期，不在本波（ledger 未裁），下次 lint 照裁決 (6) 搬進同一個 archive。
- 懸置：08 月時序 L1001 的「🔎 查無新訴訟證據」是舊式標籤，不是新語法標記；同一事實的新語法標記住風險細節 L282（隨頁搬到風險頁），計數 212→212。

## 3. 錨點入邊 24 筆逐筆去向（`grep -rnoE`，log 除外）

| 入邊 | 現指 | 拆後 | 誰改 |
|---|---|---|---|
| ms-ipo L107／137／152／182／196／226／286（7） | `#IPO 走到哪一格` | 母頁保留節名（另有 daily/ 4 筆）；可省一跳改指 `anthropic-ipo#上市走到哪一格` | handoff 2(b) |
| ipo L40（1） | `#現在的數字` | 母頁保留，指標表本身 | 不動 |
| ipo L97（1） | `#上面提到的人是誰` | 母頁保留（第 6 條改為「子樹內的人」） | 不動 |
| ipo L102／107／109（3） | `#現在的數字`（實指細節） | 頁內 `[[#數字細節]]` | 本波 |
| ipo L87／141／177（3） | `#還沒過去的風險`（實指唱空） | 頁內 `[[#誰說撐不住：唱空與質疑]]` | 本波 |
| ipo L92（1） | `#還沒過去的風險` | `anthropic-business-risks#還沒過去的風險` | 本波 |
| ipo L63、L161（2） | `#哪個合作會改到你用的 Claude` | L63 實指算力 → `-partnerships-compute#算力與資金從哪來`；L161 Amazon 投資 → `#跟三大雲各是什麼關係`（順修「$400 億投資記錄」錯字） | 本波 |
| ipo L89、L95（2） | `#算力與資金從哪來` | `-partnerships-compute#算力與資金從哪來` | 本波 |
| competitor-landscape L180（1） | `#還沒過去的風險` | `-business-risks#還沒過去的風險`（同維護者互指句） | 本波 |
| tom-brown L47（1） | `#算力與資金從哪來` | 母頁 `####` 指路殼先接住 | handoff 1，落地後刪殼 |
| ms-customers L62、L122（2） | `#哪個合作會改到你用的 Claude` | 母頁指路殼接住 | handoff 2(a) |
| 頁內 L94、L252（2，未計入 24） | `[[#算力與資金從哪來]]` | 改跨頁 `-partnerships-compute#…` | 本波 |

**另有 daily/ 讀者版日報 18 筆**（`build_web` 一併驗）：`#還沒過去的風險` 2、`#這些數字是誰說的` 1、`#哪個合作會改到你用的 Claude` 4 會斷；日報是「不可改的過去」（reader-digest SKILL L48），所以這三個指路殼**永久保留**（N2）。不設殼時臨時副本 build 錨點 WARN 0→3 且 exit 1（`ERROR: 錨點健檢：3 筆`）。

## 4. 照查證與冷讀者改的句子（逐字在 draft E 節）

查證 #2 淨損降「多家引 S-1」並補 724 億非現金、營業層 6.9 億（母 L56、ipo L71、數字細節 L67／L71）；#3 獲利列寫明調整後口徑、S-1 調整後 16 億（L55、L73、ipo 新列「營業損益口徑」）；#4 Q3 日期統一 10-15；#6 Nscale 1,030 億是全部客戶合約、Anthropic 這筆 450 億（算力表 L296）；#8–9 ipo L49 時程、L50「外流草稿首度揭露」、L54、L61 結論；⟨Q-03⟩ 改問「掛牌日與價格區間何時公布」、複查日延到 11-24、探針不動（N8）；L44 四件事→五件；PBF「撥入全資子實體」（第 22 波查證，L58）。冷讀者：L74／ipo L107 年增→季增；ipo 新列「通路與客戶集中」（47%、各 12%、換算 2025 全年約 46 億〔推論〕）；L464 Google 年份→2026-04-24；L300 SpaceX 已見後果、L326 改寫；L351 多年總額不比一年營收；L309 AWS 改 S-1 1,100 億；L115 條件句＋推論；ipo L76 補推論；L53 ARR 標「之後未見新值」；google-investment L47 連結改指母頁指標表、L71 Amazon 接三大雲表；外洩 #1、#4–8、#10 修，#2／#3 是規定的懸置語法不動，#9「Google News/」前綴不在本波（不選第 5 條）。

## 5. 規則檔與腳本（逐字在 draft「進規則檔」；臨時副本實套後 `check_rules.py` ✅）

- `commercial/pages.md`：節名改「topics/anthropic-business（母頁）與三子頁」；加子樹說明與第 0 條路由表（判不出→母頁 `### 未歸類`）、母頁每日可動清單、指路殼說明；第 1–8、10 條寫明表住哪頁；第 2 條記 S-1 整表重判已執行、修正版再判；第 3 條三頁各封頂 20；第 6 條「子樹內」；第 8 條 archive 子樹共用（裁決 (6)）與對象；新增第 12 條三大雲表、第 13 條算力表契約（健檢卡 §11「無契約、只增不退」，N5）；L121 競品第 0 條落點改子樹三頁。
- `commercial/daily.md` L13–14：負責頁面表拆成母＋三子頁四列。`commercial/weekly.md` L29：回掃對象改合作算力頁。
- `page-lifecycle.md` L52：母頁每日寫入例外登記 business 的 `## 現在的數字` 與 `## 時序`（公司動態）。
- `sweeps.md` 5j L249、L251：四表改寫成住哪頁、加三大雲表與未歸類分派、人物表看子樹。
- `features/daily.md` L51：商業合作／融資改投兩子頁。`market/daily.md` L35：資本事件的事實頁改 ipo／合作算力。`agents/wiki-reporter-commercial.md` L9、`agents/wiki-reporter-market.md` L29：「anthropic-business 子樹」。
- **腳本：無**（draft「進腳本」逐支列理由；`reporter_of`／`owner_of` 對三子頁臨時副本實測都回商業）。

## 6. handoff（主 session 先 `pending_handoffs.py open --dry-run`；H-6109b3 本波結案）

| # | --from → --to | 頁 | 事項 |
|---|---|---|---|
| 1 | 主編 → 人物 | entities/tom-brown | L47 `[[topics/anthropic-business#算力與資金從哪來]]` → `[[topics/anthropic-partnerships-compute#算力與資金從哪來]]`；落地後主編刪母頁 `#### 算力與資金從哪來` 殼兩行，build 錨點 WARN 不增 |
| 2 | 主編 → 投資分析 | topics/market-signals（子樹） | (a) ms-customers L62、L122 錨點改指 `-partnerships-compute#哪個合作會改到你用的 Claude`；(b) ms-ipo 7 筆 `#IPO 走到哪一格` 可改指 `anthropic-ipo#上市走到哪一格`；(c) ms-compute L135／137／139／235／278 的 Nscale 口徑改指合作算力算力表 Nscale 列（1,030 億是 Nscale 全部客戶）；(d) ms 母頁 L90「細節（Microsoft 列）」的事實家在 `anthropic-business-risks` 細節區 Azure Marketplace 條，改一句指路；(e) 四子頁頂部加對稱互指句「事實和數字在 anthropic-ipo／-partnerships-compute／-business-risks」；(f) ms-ipo 指 business 的財務事實 21 筆可改指 anthropic-ipo（H-6109b3 第 3 項移來） |
| 3 | 主編 → 商業 | topics/anthropic-business（子樹） | **時序類別標籤固定詞彙提案**（裁決 (8)）：現 46 種、「IPO 前瞻／IPO前瞻」各 26、「重大事件」11 則什麼都收、9 則分不出群；提案收成一張與第 0 條路由對齊的詞表交主編寫進 pages.md 第 7 條。附兩件：「Google News/」來源前綴在讀者面像出處是 Google（冷讀者外洩 #9），記者下筆時去前綴；子頁時序的引號節名指錯頁者 lint 時改 wikilink |

H-6109b3 四項：1（ipo L40／44／210 → ms-ipo）、2（L711 → ms-customers）、4（Nscale 口徑，事實側）本波做完；3（ms 母頁 Microsoft 細節）是投資分析的頁，移入 handoff 2(d)。主編結案時 note 寫明。

## 7. 閘（`D/tmp_before`＝HEAD、`D/tmp_after`＝套本案＋規則檔；`rebuild_after.sh` 一鍵重跑，輸出在 `D/gates_*`、`D/build_*.txt`、`D/run_tests_*.txt`）

| 閘 | 改前 | 改後（最後一行原樣） | 驗紅／看守 |
|---|---|---|---|
| `split.py` 防呆 | — | `ok {…}` | 副本加一行 → `AssertionError: wiki/topics/anthropic-business.md 自設計 commit 702e5a6 後被改過`（`redtest.txt` 1） |
| `verify.py` | — | `結論：OK`（照搬 912 行逐字；懸置 3→3） | 刪合作算力 Akamai 一行＋刪風險頁標記 → 兩項缺、`3→2`、`結論：FAIL`（redtest 2） |
| `gen_wiki_frontmatter.py` | exit 0 | exit 0；母頁 children 四個、兩新子頁 `page_role: "child"`、index L137 投影四子頁 | — |
| `check_hierarchy.py` | `✅ 通過（32 個母頁）` | `狀態：✅ 通過（32 個母頁）` | 母頁 callout 改 10-31 → `❌ hub 落後：…2026-10-31 < 子樹最新新聞 2026-11-01`（redtest 4） |
| `check_pending_markers.py` | ✅（212／基線 212） | `狀態：✅ 懸置標記語法檢查通過`（212，1 筆換 slug 待入基線） | 實作後 `--rebuild-count --reason "第 23 波 business 拆頁：Post-Crescent 1 筆換 slug"` |
| `check_wiki_freshness.py` | OK 138 頁 | `OK: wiki 新鮮度檢查通過（140 頁；…）` | 合作算力 callout 的 11-01 歸因網址換掉 → `[無從對照] topics/anthropic-partnerships-compute`（redtest 5；`ancestor_att` L201） |
| `check_reader_language.py` | FAIL 2（第 21 波，待本機） | FAIL 2（同兩筆）；**本波 0** | `moves.py` reader：改前子樹 0／改後 0 |
| `check_cell_limits.py` | FAIL 107（第 21 波） | FAIL 153；**本波 +46，全是搬家** | `moves.py`：改後子樹 46 筆全配回 business／ipo 舊基線（同錨點、長度不超）、配不回 0；塞一條 240 字 → `新 … list_item 240`、exit 1（redtest 3）。逐筆見 map 第六節 |
| `check_rules.py` | ✅ | `狀態：✅ 全部確定性檢查通過`（規則檔已套） | — |
| `build_web.py` | 斷鏈 23／錨點 0，exit 0 | `wikilink 健檢合計：斷鏈 WARN 23／錨點 WARN 0`，exit 0 | 不設三個永久殼 → 錨點 3、exit 1（§3） |
| `run_tests.py` | 1 FAIL（`test_repo_currently_has_no_new_hits…`）＋2 閘紅、1,334 案 | 同樣 1 FAIL＋2 閘紅、1,334 案 | 本波沒新增紅種類；cell 數 +46 |

## 8. 新裁決點（主 session 判）

- **N1** 風險表 UTRF 讓位（規則機械結果）。備案：第 4 條上限 6→7，UTRF 留表。
- **N2** 母頁三個永久指路殼（daily/ 錨點）＋一個暫時殼。備案：改 daily/ 舊日報的錨點——違反「日報是不可改的過去」。
- **N3** 合作節 × 07 連同 07 月「戰略合作細節」12 條一起搬（同一 h2 區塊同月）。備案：細節留合作算力頁，12-01 再搬。
- **N4** 三大雲表放合作算力頁＋第 12 條契約。**實作前主編查證兩格**：Microsoft 是否持股（現寫「未見持股報導」）、Amazon 2023–2024 投資金額（現沿用頁面 $40 億、標媒體稱）；查不到一手就照現字。
- **N5** 算力表補契約（第 13 條，180 天退場降為清單）。不補則它仍只增不退。
- **N6** cell 基線：本波 46 筆搬家要本機 `--rebuild --allow-grow`（可與第 21 波 107 筆同一次跑，reason 兩波並列，清單在 map 第六節）；雲端 commit 沿用第 21／22 波例外：紅只能是那 153 筆，`moves.py` 證明本波新寫 0。
- **N7** L774 Eisman 時序改歸 ipo（groups.py 歸風險）。
- **N8** ⟨Q-03⟩ 探針「calcalistech、IPO 延後」不改（改了指紋換新、命中次數歸零），只改問句與複查日。

## 9. 不選的方向

- 三大雲表放母頁：一跳少一，但母頁多一張每週對帳的事實表、數字與子頁重複。
- 風險表上限放寬到 7：規則為一波例外改上限，下一波又會有人要第 8 列。
- 子頁時序去重：等於砍列（裁決 (3)）。
- 改 daily/ 舊日報的錨點取代指路殼：日報不可改。
- 本波清「Google News/」前綴：全子樹數百處、是下筆習慣，清了明天又長回來（handoff 3）。
- 指標表加「S-1 上半年營收」列：表 10/10 滿要讓位；放進母頁「最新」段與 ipo 數字細節即可。
- ipo「IPO 細節」07／08 月同波蒸餾：ledger 未裁，每頁每輪 2 段已被 business 用完的是另一頁，但留給 lint 照常規做，避免本波再加一個 archive 節。
- 不加 `OWNER_OVERRIDES`／`PAGE_TO_REPORTER`：領域與維護者一致，沿 parent 已推得到（實測）。

**可行性前提**：同一個 commit 含 wiki 五頁＋鄰居三檔（competitor-landscape、google-investment、index）、規則檔 9 份、`--rebuild-count`、handoff 1–3 開帳與 H-6109b3 結案、`devpractice_diff.py mark`、`wiki/log.md` Query 條目、ledger 定稿列；在六個檔仍是 `702e5a6` 版時跑 `split.py`（否則它先紅，重跑設計）；N4 兩格查證先做；run_tests 依 N6。

## 10. 最不確定的一件事

合作算力頁的長速。正文 449 行，10 月 G1 有 41 則時序＋21 列清單（約 90 行），照此 12 月中前後過 600；12-01 起 08 月清單 29 列與 08 月細節（約 35 行）到期可搬，09 月時序 01-01 才到期。若 handoff 3 的固定詞彙讓「戰略合作」類別收緊（現在 65% 是清單的指路句），每天就只寫一處，這才是根治；不然 01 月得再評一次切法（候選：算力與資金／合作與通路）。
