# 第 26 波評審：topics/recursive-self-improvement 結論層重寫＋量化表官方化＋政治五節搬家（2026-11-05）

> 審的對象：`recursive-self-improvement-2026-11-05-{proposal,proposal-map,draft}.md`；上游健檢卡、`wave26-cold-reader-2026-11-05.md`、`-verified.md`（含第四節）；ledger 裁決紀錄最上面兩條（十個裁決點、N1–N10）。
> 設計者產物在 `<scratchpad>/w26/design/`（下稱 `D/`）。我的重跑有兩份：`<scratchpad>/w26/review/dc/` 是 `D/` 腳本加 `tmp_before` 的原樣副本，`dc2/` 是同一份副本套上修法後的結果。`D/`、wiki、規則檔我都沒動，也沒做 git 寫入。
> 修法寫成一支腳本 `<scratchpad>/w26/review/fix_review.py`，參數是設計目錄，會改 `newtext.py`、`build.py`、`rules_patch.py` 三檔，共 10 處，每處都斷言恰好出現一次。已在 `dc2/` 實跑，全閘綠。行號標「P Lnnn」指原檔（`f659da4`，527 行），標「M Lnnn」指修法後的主頁。

## 結論

- 共 🔴 0 條、🟡 6 條。行帳、逐字比對、懸置、cell／reader、錨點、規則檔、H6 閘檔我都自己重跑過，主 session 和設計者給的數字全部對得上（下表）。
- 頁面在設計後沒被動過。`git log f659da4..HEAD` 只有 `60f7b3a` 一筆，而且只動 docs。本頁、archive、gov-policy、market-signals-ipo、anthropic-ipo、commitments、index、safety-policy 規則檔，最後一次 commit 都早於設計（`164b79d`／`61a4b77`／`3a96d6b`／`52497b3`）。`git fetch` 之後 origin 沒有新 commit，工作樹也乾淨。11-04 ingest 已經進來（log L8553）；11-05 日報還沒產，隨時可能到，所以第 0 步要先做。
- **放行條件**：套用 `fix_review.py`（🟡1–4、🟡6），第 6 步的 `--rebuild-count` 照 🟡5 改寫 reason 並核對差集。套完以後就放行，不必回設計者第二輪，因為修法沒有新增裁決點。

## 自己重算的數字

| 項目 | 設計者／主 session | 我重算 | 證據 |
|---|---|---|---|
| 行帳 | 1–527 每行恰消費一次；M 379／A 23／G 32／改 41／砍 40／結構 12 | **屬實**：`dc/` 重產的 `accounting.txt` 跟 `D/` 一致。修法後是 M 377／砍 41／結構 13，其餘不變 | `dc2/make_map.py`：`124 段` |
| 頁長 | 426／120／972 | **屬實**。修法後是 424／120／972 | `ok {'main': 424, …}` |
| 照搬逐字 | 277 行 | **屬實**。修法後 276 行，因為 P L56 由原字改為砍 | verify 輸出 |
| 懸置 | 三頁 20→19，全庫 225→224 | **屬實**：`check_pending_markers` 改前 225、改後 224，基線 212。主頁 7→5（−2 併家、−1 TribLive 搬去 gov、+1 S-1/A），gov 14→15 | 兩次實跑 |
| 14 條砍句 | 不含唯一事實 | **屬實**，逐條核過（見「抽驗」） | P L191…378 |
| 七條長度 | 95–159 字元 | 去掉連結網址算是 **97–161**；只有「質疑」那條含網址，原長 284。cell 閘用的算法下是 0 新增 | `dc2/` cell |
| cell／reader | 本頁 11→3 全配回、釋出 8；gov 48→48；reader 0 | **屬實**，修法後數字也相同 | moves |
| 舊字樣存量 | 提案沒寫 | 19→18：P L152「協議日期與條款官方未載」被刪。這條棘輪只擋增加，閘照樣綠；但「條款未載」這個缺口要留下來，見 🟡2 | `iter_legacy` 實跑 |
| H6 閘檔 | 不碰 | **屬實**。只改了 `safety-policy/pages.md` 和 `daily.md`，都不在 `guard_roles.py` L52–56 的 GATE_FILES 裡。`--rebuild-count` 也不是 `BASELINE_FLAGS`（L57、L120 是逐 token 精確比對） | — |
| daily.md L29 | 改掉「照既有結構 prepend」 | **屬實**：`tmp_after` L29 已換成「技術彙整＋時序 prepend；目前結論與量化表依 pages.md 改寫」 | diff |
| callout 歸因 | epyhia 網址 | **屬實**：跟 `data/source_attribution.jsonl` 裡 2026-11-03、hacker-news 那筆的 `item_url` 逐字相同 | — |

**量化表對 verified**：26%（2 月不到 1%）、AL5 為 0、約 3 萬 agent 限「最常用的內部平台」，這三列都附官方頁連結，跟 verified #1–#3 一致。AL3 以上逾 90% 的說法出自 P L223、L255 的官方頁查證（10-03），也算一手。第五列 8× 標「媒體轉述」，對應 verified #4。表格一個口徑一列，共六列。

**White House Accord**：我在 2026-11-05 重抓了官方 10-15 稿，原句是「We also signed the White House Accord on Super Intelligence, in which companies pledged to partner with independent external auditors or evaluators.」，全文沒有提到暫停、減速或 moratorium。gov 那兩處寫法跟原句相符，主頁 L149 多說了一步（🟡2）。

**去向表抽驗**（map 第一節對 `accounting.txt`，抽 4 節，都相符）：
- **政治五節**（P 187–206、284–294、318–328、366–379，共 56 行）：G 32 行＋砍 14 行＋結構 10 行。砍掉的 14 句逐條核過：L191 的反壟斷豁免提案原本就住 gov；L200「監管俘獲」、L205「HN 10 分」都已在搬過去的 L198–199；L288、289、292、293 是 Jack Clark 職稱和限制句，09-15 的事實住 P L304–308；L372 跟 gov L712 是同一句；L378 只少了 CNN／AOL 兩個轉引媒體名，沒有事實。搬進 gov 的段落裡，「本頁／上方／下方」這類相對指稱是 0 處，自指不會指錯頁。
- **目前結論**（P 62–98，32 條）：每條的事實都另有家。L62 Medium 寫進「質疑」條；L66 Sanders 在時序 M L408（「無人跟進」那句被冷讀者指出被 gov L103 推翻，砍掉反而對）；L67 Model 2 在時序 L511；L75 三步驟在 L350；L80 反壟斷在 gov。L64「邊呼籲邊出口管制衝突」沒有日期也沒有來源，是評語，不是事實（推論）。
- **摘要**（P 39–56）：L43 brake pedal 的家在 L308，媒體名單在 L522；L47 五眼和 CNA 在 L525；L49–55 的 HN 477 在 L521。L56 留下來會跟新條文衝突，見 🟡1。
- **時序 09 月砍的 10 行**（P 447–449、473、481–483、489–491）：每一行的事實都已在搬過去的五節裡。L490「川普淡化＋連署」在 gov L712。

## 一、冷讀者

**🟡1 新條文一落地，這頁就先違約兩處**
- pages.md 新節規定「`## 摘要` 兩段」，但改後 M L47 留著第三段「各階段量化數字口徑與**時間軸**整理見…」。表已經改成覆寫型，沒有時間軸了，這句是錯的。量化表的入口，目前結論「官方量到多少」已經有了。
- 新條文也規定「到哪了」要標硬度，但 06-04 報告的「尚未達到、非必然」只有媒體轉述（verified #4 寫「多家引該報告」），條內卻只寫「官方說…（06-04 報告）」。
- 修法（已含在 `fix_review.py`）：
  - `build.py`：`M += rng(56, 61, "M")` 改成 `mark(56,56,"砍：…")`、`mark(57,57,"結構")`、`M += rng(58, 61, "M")`。
  - `newtext.py`：`（06-04 報告）；` 改成 `（06-04 報告，據媒體轉述）；`。

**🟡6 同一頁裡 Reuters 有兩個日期**
- 量化表寫「Reuters 09-17」，跟 P L250、verified #3 一致；但 L219 的新字寫「與 09-18 Reuters『四分之一』」。
- 修法：改成 `與 09-18 條目 Reuters「四分之一」`（`newtext.py` LINE_SUBS 219）。

## 二、明天的維護者

**🟡4 指路節的 gov 日期錨點，會讓 gov-policy 的 09 月時序永遠蒸不掉**
- 證據：page-lifecycle L87 例外 1 是「有錨點邊指入就不蒸」。改後主頁新增 5 個 `gov#2026-09-1x/2x` 錨點，加上 L149 的 `#2026-10-15`。gov 時序 09 月 12-01 起符合蒸餾門檻，到時 `explain --section` 會列出本頁，這個時段就被凍住，沒有任何條文能解開。另一處：指路節標題帶著「（2026-09-11～09-27）」，以後加了新行，標題就跟內容不符，也可能被誤當成 09 月時段一起蒸走。
- 修法（`fix_review.py`）：
  - 標題改成 `### 政界與政府怎麼回應減速呼籲`（沒有自指錨點指向它，verify 第 4 項仍是 OK）。
  - pages.md 本頁節那一條補上：`標題不帶日期、本節不隨時段蒸餾；topics/anthropic-government-policy 蒸到某月時，本頁指向該月日期錨點的行（含本節）同批改指 topics/anthropic-government-policy-archive#YYYY-MM。`
  - gov 節第 6 條句尾接：`` `## 時序` 的日期錨點若只被 `topics/recursive-self-improvement` 指入，蒸該月時把那幾行改指 archive 的 `#YYYY-MM`，不算 page-lifecycle 例外 1。``。由 `rules_patch.py` 在既有的 sha 鎖之後做替換，並斷言該句恰好出現 1 次。

## 三、機器

**🟡5 `--rebuild-count` 會順手吸收 13 筆別頁的新標記，reason 只寫本波**
- 在 `dc/tmp_after` 實跑 `--rebuild-count`：基線變成 224，差集是 ＋16、−3。
  - −3 正好是預期的三筆：互測（標 09-21）、參議員（標 10-05），以及 TribLive 那筆的舊指紋（它在 ＋ 那邊以 gov 頁鍵重新出現）。
  - ＋16 裡，除了 TribLive（gov 頁鍵）和 S-1/A 兩筆（msi 原筆、本頁新筆），另外 13 筆來自 11-02～11-04 ingest，分屬 ai-agent-safety 樹、competitor-landscape、market-signals-compute、market-signals-ipo。這和第 11 波評審記過的「rebuild 順帶吸收」是同一型。
- 修法：見實作單第 6 步，reason 字串照那裡寫，並核對差集。

**無其他發現**：
- `build.py` 會比對三檔 blob，`rules_patch.py` 有 sha 鎖，`rebuild_after.sh` 開了 `pipefail`，所以 ingest 先動到任何一檔都會先紅。
- 修法後 `make_draft.py` 照樣能跑（120 行）。但 draft 不會呈現 build.py 砍掉 L56 這件事，也不會呈現 gov 第 6 條的補句，這兩處要在 draft 手補（第 4 步）。

## 四、治理

**🟡2 主頁 L149 把白宮協議寫成「內容是…不是暫停」，比官方稿說得多；「條款未載」這個缺口也沒了**
- 官方稿只說企業承諾與外部稽核或評估者合作、沒提暫停（見上方原句）。協議全文沒有人讀過。gov 那邊寫「原文未提」才是對的，但「原文」容易被讀成協議本文。另外 P L152 刪掉「協議日期與條款官方未載」以後，日期確實已經解決（官方稿寫 last month，即 09 月），條款卻還是只有一句描述。
- 修法（`fix_review.py`）：
  - 主頁 L149：`稿中只寫企業承諾與獨立外部稽核或評估者合作，未提暫停；見 [[…#2026-10-15]]`
  - gov 攻防紀錄那一列：`簽署企業承諾與…；官方稿未提暫停或減速；`
  - gov 時序那一條：`…；官方稿未提暫停或減速承諾，協議全文未附（[Anthropic](…)，2026-11-05 查證）`
  - 目前結論「是第三方評估，不是暫停」講的是 Accenture、METR 這兩個已落地的安排，有官方稿撐腰，維持原字。

**🟡3 08 月摘要把「仍待觀察」升級成「不等於」**
- 證據：被蒸走的 P L412 寫「與遞歸自我改進定義的關係仍待觀察…非可由官方一手來源確認或否認」。新摘要卻寫「不等於 AI 自主設計繼任模型」，違反不虛報。
- 修法：改成 `這是 AI 稽核並修復其他模型的對齊問題；與 RSI 定義（AI 自主設計繼任者）的關係，官方未表態。`

**照條文核過、無發現**：
- 七條結論的撐腰事實與日期：Accenture 09-18、METR 10-15、三步驟 09-12（只有 ① 有 METR 員工級存取對應，這是推論，commitments handoff 4 也是這樣寫）、Jack Clark 09-15、連署 09-18（CNBC，逾 100 人）、Burry 09-17 報導、Medium 08-10 查證、Opus 4.8 的 1,600／39，逐一對到原行。
- 兩則前瞻預言都只寫原句和起算日：五眼 06-22 對 P L47、L525；Amodei 09-12 對 P L346 的「AI swarm」「6–12 個月」「殭屍網路」。
- S-1/A ❓ 跟 msi L521 逐字相同；N3 過渡期兩筆都還在。
- 主頁 cell／reader 本波新增 0，修法後仍是 0。

## 照順序執行（實作單）

`D`＝`<scratchpad>/w26/design`，`V`＝`<scratchpad>/w26/review`。第 0–4 步都在 `<repo>` 還是原樣時做。

0. **確認原檔沒被 ingest 動過**：
   - 指令：`git -C <repo> fetch origin && git -C <repo> diff --stat f659da4 HEAD -- wiki/topics/recursive-self-improvement.md wiki/topics/recursive-self-improvement-archive.md wiki/topics/anthropic-government-policy.md wiki/topics/market-signals-ipo.md wiki/topics/anthropic-ipo.md wiki/topics/anthropic-commitments.md wiki/index.md .claude/reporter-rules/safety-policy/`，再用同一組路徑對 `origin/master` 跑一次，最後跑 `git -C <repo> status --short wiki .claude`。
   - 驗收：三個指令都沒有輸出。
   - 有輸出時：前三檔有差就停下，續用設計者，讓他以新 HEAD 改 `build.py` 的 `DESIGN_COMMIT` 與行號斷言、`verify.py`／`make_map.py` 的 `f659da4`，再從第 1 步重來，不准手改；只有 msi、ipo、commitments、index 有差，就照常做，但第 7 步的 handoff 行號要先 grep 重對。
1. **備份並套修法**：
   - 指令：`cp -a D D.pre-review && python3 -I V/fix_review.py D`
   - 驗收：`fix ok {'newtext.py': 7, 'build.py': 1, 'rules_patch.py': 2}`。
   - 這支只能跑一次；要重跑，先用 `D.pre-review` 還原。
2. **一鍵重跑**：`bash D/rebuild_after.sh <repo>`。驗收要對得上我在 `dc2/` 的實跑結果：
   - `ok {'main': 424, 'archive': 120, 'gov': 972}`
   - `照搬行逐字核對 276 行；懸置標記（三頁）20→19（併家 −2、S-1/A 搬入 +1）`、`結論：OK`，兩者各出現兩次
   - `rules ok; pages.md sha 65d18a78…`
   - 全部閘 exit 0，其中 `check_cell_limits … 無新增超限`、`check_reader_language … 無新增命中`、`錨點 WARN 0`
   - moves：本頁 `配不回 0；釋出 8`，gov `48；配不回 0`，reader `新寫 0`
3. **肉眼抽驗**，`O=D/out/wiki/topics`：
   - `grep -c 時間軸 $O/recursive-self-improvement.md` → `0`
   - `grep -n "據媒體轉述）；\|未提暫停；\|官方未表態\|^### 政界與政府怎麼回應減速呼籲$\|09-18 條目 Reuters" $O/recursive-self-improvement.md` → 5 行
   - `grep -c "協議全文未附\|官方稿未提" $O/anthropic-government-policy.md` → `2`
   - `grep -c "不算 page-lifecycle 例外 1\|同批改指" D/tmp_after/.claude/reporter-rules/safety-policy/pages.md` → `2`
4. **重產文件**：
   - 指令：`python3 -I D/make_draft.py <repo>/docs/page-audits/recursive-self-improvement-2026-11-05-draft.md && python3 -I D/make_map.py <repo>`
   - 驗收：`draft lines 120`、`124 段 {'M': 377, '砍': 41, '結構': 13, '改': 41, 'G': 32, 'A': 23}`。
   - 接著用 `D/map_rows.md` 換掉 proposal-map 第二節。
   - 用 Edit 改數字：proposal L20、L102 與 map L31 的 426→424、`正文 503→401` 改 →399、M 379→377（原字 355→353）、砍 40→41、結構 12→13；proposal L103 的 277→276。
   - draft 手補兩句：B 節加「L56 砍（摘要只留兩段）」，M 節後加「gov 節第 6 條句尾補例外 1 豁免句（見 rules_patch.py GOV6_NEW）」。
5. **落地**：
   - 指令：`cp -r D/out/wiki/. <repo>/wiki/ && python3 -I D/rules_patch.py <repo> | tail -1 && (cd <repo> && python3 scripts/gen_wiki_frontmatter.py | tail -1)`
   - 驗收：`rules ok; …`，gen exit 0。
   - 接著跑 `python3 -I D/verify.py <repo> <repo>/wiki | tail -2`，驗收 `276 行…20→19`、`結論：OK`。
6. **懸置基線**：
   - 指令：`cd <repo> && python3 scripts/check_pending_markers.py --rebuild-count --reason "第 26 波 recursive-self-improvement：互測、參議員雙標記併家 −2；TribLive 標記隨節搬到 anthropic-government-policy（指紋換頁）；S-1/A 門檻 ❓ 自 market-signals-ipo 搬入 +1（msi 原筆待 handoff 3 移除）；同批併入 11-02～11-04 ingest 新開未入基線 13 筆（逐筆見本次輸出）"`
   - 驗收：`224 筆`；差集裡「－」恰好 3 行（Stress-Test 09-21、危言聳聽 10-05、TribLive 09-27），「＋」16 行。數字不同就停下，先查是哪一筆再繼續。
7. **轉知**：提案 §9 的 handoff 1–5，每筆先加 `--dry-run` 驗負責人和行號，再正式開立。驗收：五個單號都印出來。
8. **repo 內全閘**：
   - `python3 scripts/check_pending_markers.py | tail -1` → ✅
   - `check_cell_limits.py`、`check_reader_language.py` → 都是 OK 無新增
   - `check_rules.py` → ✅
   - `python3 scripts/build_web.py | grep 健檢合計` → `錨點 WARN 0`
   - `python3 scripts/run_tests.py; echo exit $?` → exit 0
   - build_web 改到的 web_reader 產物如果本批不 commit，用 `git show HEAD:<path> > <path>` 還原
9. **帳與收尾**：
   - 照提案的「可行性前提」做：ledger 定稿列（註明評審 🟡1–6 已吃、🔴 0）、index L142 鉤子（handoff 5，主編同波改）、`wiki/log.md` Query 條目。
   - commit 用指名 `git add`：三頁、frontmatter 被 gen 改到的頁、`safety-policy/pages.md`、`daily.md`、`data/pending-marker-count.json`、handoff 帳本、ledger、log、page-audits 四件。
   - 驗收：`git status --short` 只剩 web_reader 已還原的檔，或沒有輸出。
