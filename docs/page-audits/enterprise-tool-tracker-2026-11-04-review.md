# 第 25 波評審：topics/enterprise-tool-tracker 一家一列買方名冊＋08 月蒸餾（2026-11-04）

> 審的對象：`enterprise-tool-tracker-2026-11-04-{proposal,proposal-map,draft}.md`；上游健檢卡、`wave25-cold-reader-2026-11-04.md`、`-verified.md`；ledger 裁決紀錄最上面兩條（十個裁決點、N1–N8）。
> 設計者產物在 `<scratchpad>/w25/design/`（下稱 `D/`）。我的重跑在 `<scratchpad>/w25/review/d/`（下稱 `R/`），是 `D/` 腳本與 `tmp_before` 的副本，`out/`、`tmp_after/` 都在副本裡重產；`D/`、wiki、規則檔我都沒動，也沒做 git 寫入。
> 修法寫成兩支腳本：`<scratchpad>/w25/review/fix_review.py`（只改 `newtext.py`）、`<scratchpad>/w25/review/splice_docs.py`（同步提案文件的數字）。兩支都在 `R/` 實際跑過，結果見實作單第 2 步。行號：「P Lnnn」指原檔（`e90dace`，366 行）；「M Lnnn」指改後主頁。

## 結論

- 🔴 2 條、🟡 4 條。我重算了行帳、逐字、懸置、家數、排序、cell／reader 搬家和錨點，數字全部對得上。
- 🔴1：細節區拆掉後，表裡還有 6 格寫「細節見下方」或「詳見下方細節」。其中 Shopify、ReliaQuest、Samsung 三列的細節已經隨 08 月搬進 archive，主頁上找不到。另外 05 月時序 P L335 還寫「富士通、Nimble Gravity（詳見上方使用現況表）」，但這兩家已經移出表。
- 🔴2：選型影響第 4 條寫「按量計費的 Claude Code 會被設上限：Accenture 每月 $29」。被砍掉的 P L160 原文是「是否限 Claude Code 未見細節」，表上 Accenture 列也寫「不限特定工具」。這條是虛報，違反裁決 (6)。
- 頁面在設計後沒被動過：`git log e90dace..HEAD` 動到本頁、archive、partnerships-compute、commercial 規則檔、review-registry 的 commit 都是 0 筆。HEAD `ac8d8ef` 只加了 page-audit 文件，工作樹乾淨。`news/` 最新的是 11-03；11-04 雲端 ingest 是 aborted（`6458a99`）。11-04、11-05 補跑隨時會進來，所以第 0 步要先 fetch 再驗。
- **放行條件**：吃下 🔴1–2 和 🟡1–2（都在 `fix_review.py` 裡，一次套用）。🟡3–4 是轉知和一處 Edit，照第 6、8 步做。

## 自己重算的數字

| 項目 | 設計者／主 session | 我重算 | 證據 |
|---|---|---|---|
| 行帳 | P 1–366 每行恰消費一次 | **屬實**。`R/` 重跑後 `out/` 跟 `D/out/` 用 `diff -r` 比沒有差異（修法前）。去向 M 212／A 41／改 22／併入 9／砍 81／結構 1 | `R/accounting.txt` |
| 砍 81 | — | **屬實**。分項：43–82 共 40；細節區 7（154、155、160、161、168、171、172）；工具態勢 187–204 共 18；市場分層 205–212 共 8；通路 8 | 腳本按區間數 |
| 照搬逐字、懸置 | 155 行；0→0 | **屬實**。修法後是 150 行：P95、106、111、117、335 改成「M（改）」。懸置 0→0，全站 220 筆不動 | `R/rebuild` 輸出 |
| `verify.py` 第一參數 | 指改前副本 | **屬實**。改前內容一律用 `git show e90dace:<path>` 取（verify L22–27），`argv[1]` 只是 repo 根。所以落地後跑 `verify.py <repo> <repo>/wiki` 仍然是在對改前的 blob | — |
| `build.py` 防呆 | blob＋乾淨工作樹 | **屬實**。L24–29 比對 `HEAD:f == e90dace:f`，外加 `diff --quiet`；`rebuild_after.sh` 有 `pipefail`，`\| tail -1 \|\| exit 1` 擋得住。`rules_patch.py` 用 sha256 鎖住 pages.md 本頁節 | redtest 1 |
| 主表家數 | 48；✅35／⚠️7／❌3／🔄1／❓2 | **屬實**。我寫了腳本數改後表：48 列，`Counter` 結果相同，排序違規 0，備註 >120 字 0 | `<scratchpad>/w25/review/count.py` |
| 多列怎麼併 | 狀態取「現在整體」 | **合理**，逐家核過。JPMorgan：美國本部 ✅、香港 ❌，06-30 解除 → ✅；Microsoft：L118 ⚠️、L138 ❌、L139 ✅ → ⚠️（verified #4）；Rubrik 3 列都是 ✅，確認日取最新的 10-09；Goldman 兩列都是 ❌，取 11-02；Uber 兩列都是 ⚠️，取 06-02 | P L94–148 原列 |
| 表頭 | 不改 | **屬實**。verify 第 4 項斷言表頭字串唯一；`build_web.py` L446 的判斷是 `"企業" in line and "AI 編碼工具" in line`；工具欄整串當鍵，不拆分（L470–474）。矩陣 48／48／27／48 | `gates_after` |
| cell／reader | 新增 0 | **屬實**。命中 2，都配回基線；配不回 0；釋出 7；reader 0／0。修法後也一樣，修法字串都是等長、縮短，或寫在本來就沒命中的 PICK 條上 | `R/` moves |
| 規則檔／閘檔 | 不碰 H6 | **屬實**。改的是 `commercial/pages.md`、`daily.md`、`review-registry.json`，都不符合 `guard_roles.py` L52–56 的 GATE_FILES；`tmp_after` 的 `data/`、`scripts/` 用 `diff -rq` 比對為 0 | — |
| callout 歸因 | PYMNTS 網址 | **屬實**。M L38 網址跟 `data/source_attribution.jsonl` 裡 2026-11-03、`topics/enterprise-tool-tracker` 那筆 `item_url` 逐字相同；標題是「Goldman Sachs Bars Bankers From Using Claude Code and GitHub」 | — |

**通路 8 家逐家核「有家」**（第 1 項重點）：Cognizant → pc L207「升為全球首要夥伴（07-28）」，加上本頁 archive L44、business-archive；Globant／DataArt／Okta → pc L208「06-30：Rubrik、Okta、DataArt、Globant」，加上本頁 archive L99、business-archive L381、L471–473；DXC → pc L208、L476，本頁 archive L128；富士通 → pc L208，本頁 archive L74，business-archive L560；KPMG → pc L208，business-archive L561；Nimble Gravity → 只剩本頁 archive L76（N3 已裁決）。表列裡的細節（Okta 的 XAA、DXC 的數萬認證工程師、Globant 的 AI Pods）都在各自的 archive 原條裡。**8 家都有家**，可以移。
**補的 6 家**：Nvidia、Palantir、Booz Allen 三列的字句對得上 product-vulns L380「媒體稱」那條和 customers L525–529（官方未回應，懸置留在 customers）。Palantir 11-01 對 pc L298（`#### 2026-11-01` 下）。Novo Nordisk「Reuters 等 4 家」對 pc L165（Reuters、Bloomberg、WSJ、politico.eu，共 4 家）。Schwab／Orion 對 pc L167、L323（20 席下限）。**都是原文**，沒有新造的事實。

**去向表抽驗**（map 第一節 → `accounting.txt`，3 節都相符）：
- 現況表 94–152 共 59 行：原字 30、改 12、併入 9、砍 8；30＋12＋新 6＝48。
- 細節區 154–177 共 24 行：M 12（插進時序）、A 5、砍 7（含標題）。
- 時序 08 274–310 共 37 行：結構 1、A 36；A 41＝36＋細節 5。
- 另外核了被砍的 6 條細節跟它們對應的時序條（P L155↔229、160↔233、161↔236、168↔248、171↔263、172↔269）。只有 L160 的「是否限 Claude Code 未見細節」沒有別的家，這就是 🔴2。

## 一、冷讀者

**🔴1 「下方細節」指向已拆掉的細節區；05-27 指向已移出的列**
- 有問題的位置：M L58 Epic、L60 Replit、L64 Meta 寫「細節見下方」；L75 Shopify、L76 ReliaQuest、L80 Samsung 寫「（詳見下方細節）」，這三家的細節現在在 archive `#2026-08`，要從主頁 08 月總結的連結進去。M L226（P L335）寫「富士通、Travelport+Cognizant、Nimble Gravity 三案新增採用（詳見上方使用現況表）」，但其中兩家已經不在表上。
- 修法（`fix_review.py`）：表內一律改成「細節見時序」（等長），或「（細節見時序）」（縮短）。Epic、Shopify 兩列改 `ROW_SUBS`；Replit、ReliaQuest、Samsung、Meta 四列和 P335 追加到 `LINE_SUBS`。P335 改成：
  `Travelport+Cognizant 新增採用（見上方表）；富士通、Nimble Gravity 屬通路夥伴`（56≤57 字，build.py L57 的不變長斷言照樣過）

## 二、明天的維護者

**🟡1 Goldman 工具欄「Claude Code ＋ GitHub」跟新條文衝突**
- 新 pages.md 規定工具欄「並用他家寫『＋X』」。可是 GitHub 是被禁的對象，不是並用的工具，維護者照字面會讀成「Goldman 同時用 Claude Code 和 GitHub」。M L56 的備註已經寫了「禁止行員用 Claude Code 與 GitHub」。
- 修法：`| Goldman Sachs | 頂尖 | Claude Code；Claude AI（香港） |`（矩陣工具欄仍是 27 欄，鍵只是換字）。

**🟡4 `shared.md` L137 自查句寫「已同步新增列」，跟一家一列衝突**
- 修法（Edit，主編檔）：old `出現具名企業採用/退出/切換 → \`enterprise-tool-tracker.md\` 已同步新增列？` → new `出現具名企業自己用 Claude 的採用/減用/退出/切換 → \`enterprise-tool-tracker.md\` 已新增或更新該公司那一列（一家一列；通路夥伴不開列）？`

## 三、機器

**無發現**。補充兩點：
- `fix_review.py` 對同一份 `newtext.py` 只能跑一次（每筆都斷言 count==1）。要重跑，先 `cp D/newtext.py` 還原。
- 改完後 draft 和 map 要重產（第 4 步）。map 第二節由 `make_map.py` 印到 stdout，`splice_docs.py` 會把它接回 proposal-map，同時改掉 3 處數字和 proposal §7 的「155 行」。

## 四、治理

**🔴2 選型影響第 4 條把 Accenture 算成 Claude Code 上限（虛報）**
- 證據：P L160「是否限 Claude Code 未見細節」（本波砍掉）；表上 Accenture 列寫「Claude（員工一般使用，不限特定工具）」。
- 修法：`**員工的 Claude 用量會被設上限**：Accenture 報銷每月 $29（是否限 Claude Code 未見）、JPMorgan 部分工程師 Claude Code 每月 $2,000、Uber 燒完全年預算後設上限；…`。這樣也把 L160 唯一的那句 caveat 救回來了。

**🟡2 選型影響第 1、3、5 條各有一處撐不住**
- 第 1 條：「減用最多」沒有比較基礎。表上只有 Meta、Microsoft 有減用數字，Nvidia 等沒有量化。「同期 Amazon 雙軌並行」也不對：Amazon 是 05-05，Meta／Microsoft 的數字是 10-05。改成 `減用有數字的 Meta、Microsoft 都自己賣編碼工具（…），而 Google（09-15）開放全體工程師使用、Amazon（05-05 起）雙軌並行`。
- 第 3 條：漏了 Notion。M L88 工具欄寫「Claude Agents + Cursor」，跟「其餘只寫用了 Claude」矛盾。補 `，Notion 則在自家產品同時接 Claude 與 Cursor`。
- 第 5 條：把媒體說法寫成事實。customers L529 明寫「因果為媒體說法，非官方」，懸置也在 customers L525。改成 `09-14 The Information 稱 Nvidia、Palantir、Booz Allen 都因資料外洩疑慮限縮（官方未回應個案）`。
- 第 2、4（修後）、6、7 條核過，都撐得住：M L156 有 `#### 2026-10-05`，同頁錨點有前例（recursive-self-improvement L56）；business-risks L53 有「換得了模型供應商」；`competitor-landscape#Microsoft／GitHub` 對到 L177 的 h3。

**🟡3 `market-signals.md` L90 仍說 Globant 的採用事實在本頁**
- L90：「其他具名採用 Claude 的上市公司（ICON、Globant、Rubrik 等）的採用事實在 [[topics/enterprise-tool-tracker]]」。Globant 移出後，這句指錯了家。這頁屬投資分析記者（commercial/daily.md L29），所以走轉知 3（第 8 步），本批不改。

**照條文跑過、無發現**：
- N2：市場分層 L207–209 各家都在表上；L209 的 BI 05-23 在 competitor-landscape L626；整節沒有懸置。
- 新 6 列的官方懸置沒有複製到本頁，跟裁決 (8) 一致。pc L165、L167 以合作框架保留（同維護者），不算第二個家。
- 規則檔沒有留下「工具競爭態勢」字樣（`tmp_after` pages.md 0 筆）。

## 照順序執行（實作單）

`D`＝`<scratchpad>/w25/design`，`V`＝`<scratchpad>/w25/review`。第 0–4 步都在 `<repo>` 還是原樣時做。

0. **驗原檔沒被 ingest 動過**：`git -C <repo> fetch origin && git -C <repo> diff --stat e90dace origin/master -- wiki/topics/enterprise-tool-tracker.md wiki/topics/enterprise-tool-tracker-archive.md wiki/topics/market-signals.md .claude/reporter-rules/ .claude/review-registry.json`，接著同一組路徑跑 `git diff --stat e90dace HEAD -- …` 和 `git status --short wiki .claude` → 驗收：三段都沒有輸出。有輸出就停，續用設計者重跑設計，不准手切。
1. **套修法**：`python3 -I V/fix_review.py D` → 驗收：`fix ok`。
2. **一鍵重跑**：`bash D/rebuild_after.sh <repo>` → 驗收（我在 `R/` 的實跑結果）：
   - `ok {'main': 259, 'archive': 194} {'M': 212, '改': 22, '砍': 81, '併入': 9, 'A': 41, '結構': 1}`
   - `照搬行逐字核對 150 行；懸置標記 0→0；表 59 列/50 家 → 48 列/家（通路移出 8）`、`結論：OK`（出現兩次）
   - `rules ok; old section sha 936139d1…`
   - 閘全部 exit 0：`check_hierarchy … 32 個母頁`、`check_wiki_freshness … 143 頁`、`check_cell_limits … 無新增超限`、`check_reader_language … 無新增命中`、`錨點 WARN 0`
   - `matrix rows 48 enterprises 48 tools 27 cells 48`
   - moves：`配不回（新寫或改長）0；改前槽位釋出 7`
3. **肉眼抽驗**：
   - `grep -c "下方細節\|細節見下方" D/out/wiki/topics/enterprise-tool-tracker.md` → `0`
   - `grep -n "Notion 則在\|是否限 Claude Code 未見\|官方未回應個案）" D/out/wiki/topics/enterprise-tool-tracker.md` → 3 行，都落在 L119–121
   - `grep -n "^| Goldman" D/out/wiki/topics/enterprise-tool-tracker.md` → 工具欄是 `Claude Code；Claude AI（香港）`
4. **重產文件**：`python3 -I D/make_draft.py <repo>/docs/page-audits/enterprise-tool-tracker-2026-11-04-draft.md && python3 -I V/splice_docs.py <repo> D` → 驗收：`draft …`、`docs ok`；`grep -c "細節見時序" <repo>/docs/page-audits/enterprise-tool-tracker-2026-11-04-draft.md` ≥2。
5. **落地**：`cp -r D/out/wiki/. <repo>/wiki/ && python3 -I D/rules_patch.py <repo> | tail -1 && (cd <repo> && python3 scripts/gen_wiki_frontmatter.py | tail -1)` → 驗收：`rules ok; …`、gen exit 0。接著 `python3 -I D/verify.py <repo> <repo>/wiki | tail -2` → `150 行；懸置標記 0→0`、`OK`。
6. **shared.md**（Edit）：照 🟡4 換 L137 那半句 → 驗收：`cd <repo> && python3 scripts/check_rules.py | tail -1` 的結果是 `✅ 全部確定性檢查通過`。
7. **repo 內全閘**：
   - `cd <repo> && python3 scripts/check_pending_markers.py | tail -1` → ✅（220 筆，不需要 `--rebuild-count`）
   - `python3 scripts/check_cell_limits.py | tail -1`、`python3 scripts/check_reader_language.py | tail -1` → 兩支都是 OK 無新增
   - `python3 scripts/build_web.py | grep 健檢合計` → `錨點 WARN 0`
   - `python3 scripts/run_tests.py; echo exit $?` → exit 0（對照 `D/run_tests_after.txt`）
   - build_web 改到 web_reader 產物、而本批不打算 commit 的，用 `git show HEAD:<path> > <path>` 還原
8. **轉知**：每一筆先加 `--dry-run` 驗負責人和單號，再去掉 `--dry-run` 正式開立。
   - 提案 §6 的 handoff 1、2 照原文。
   - 新增 3：`python3 scripts/pending_handoffs.py open --from 商業 --to 投資分析 --page topics/market-signals --note "第 25 波 enterprise-tool-tracker 通路夥伴移出主表：L90「ICON、Globant、Rubrik 等的採用事實在 enterprise-tool-tracker」去掉 Globant（通路夥伴，家在 anthropic-partnerships-compute）"`
   - 驗收：三筆單號都印出。
9. **帳與收尾**：照提案「可行性前提」做——ledger 定稿列（註明評審 🔴1–2、🟡1–4 已吃）、`wiki/log.md` Query 條目、index 鉤子（handoff 2 由主編同波改）。commit 用指名 `git add`：兩頁、gen 改到的 frontmatter／index、`commercial/pages.md`、`commercial/daily.md`、`shared.md`、`review-registry.json`、handoff 帳本、ledger、log、page-audit 四件（proposal、map、draft、review）。add 前先看 `git status --short`，名單外的檔不要加。
