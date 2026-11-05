# 第 27 波評審：entities/dario-amodei 核心論述改主張清單＋批評者判準＋08 月蒸餾（2026-11-05）

> 審的對象：`dario-amodei-2026-11-05-{proposal,proposal-map,draft}.md`；上游健檢卡、`wave27-cold-reader-2026-11-05.md`、`-verified.md`（含第四節安保費算術）；ledger 裁決紀錄最上面兩條（十個裁決點、N1–N8）。
> 設計者產物在 `<scratchpad>/w27/design/`（下稱 `D/`）。我重跑了兩份：`<scratchpad>/w27/review/d/` 是 `D/` 腳本加 `tmp_before` 的原樣副本，`d2/` 是同一份副本套上修法的結果。`D/`、wiki、規則檔我都沒動，也沒做 git 寫入；兩次 `rebuild_after.sh` 跑完，repo 的 `git status` 都是空的。
> 修法寫成 `<scratchpad>/w27/review/fix_review.py`，參數是設計目錄。它會改 `newtext.py` 6 處、`build.py` 1 處，每處都斷言恰好出現一次。我已在 `d2/` 實跑，全閘綠。「P Lnnn」指原檔（`d6afcdb`，213 行），「M Lnnn」指修法後的主頁。

## 結論

- 共 🔴 2 條、🟡 4 條，每條都附修法。行帳、逐字、懸置、cell／reader、錨點、H6、callout 歸因，我都自己重跑過。數字只有一處對不上：參考來源實為 46→**31**，不是 32（🟡4）。
- 設計之後頁面沒被動過。`git log` 顯示五頁、RSI、index、`people/daily.md` 最後一次 commit 都早於 `d6afcdb`（`24ca38a`／`164b79d`／`d6bcfac`／`ed75031`）。`git fetch` 後，origin 三條分支對這些路徑都沒有新 commit，工作樹乾淨，11-05 日報也還沒產。不需要重跑設計；第 0 步照樣要做。
- **放行條件**：套用 `fix_review.py`（🔴1、🔴2、🟡3），並照實作單做 🟡4–🟡6 的文件和角色檔 Edit。修法沒有新增裁決點，所以套完就放行，不必回設計者第二輪。

## 自己重算的數字

| 項目 | 設計者／主 session | 我重算 | 證據 |
|---|---|---|---|
| 行帳 | 1–213 每行恰消費一次；照搬 121／行內改 17／archive 13／改寫 38／砍 19／結構 5 | **屬實**：`make_map.py` 原樣得 `69 段 {'M': 121, 'M（改）': 17, 'A': 9, 'A（改）': 4, '改': 38, '砍': 19, '結構': 5}`。修法後 M 120、M（改）18、71 段 | `d/`、`d2/` 的 `accounting.txt` 差一行（P101） |
| 頁長 | 主頁 175、archive 83 | **屬實**，修法後也相同 | `ok {'main': 175, 'archive': 83}` |
| 照搬逐字 | 84 行 | **屬實**。修法後 83 行，因為 P L101 黃仁勳列改成行內改 | verify 輸出兩次 |
| 懸置「原本就不入計數」 | 223→223、舊字樣 18→18，不需 `--rebuild-count` | **屬實**。我用 `pending_markers` 的 `PENDING_RE`／`SHORT_RE`／`QDEF_RE`／`LEGACY_RE` 直接掃 P 檔：四個 regex 都 0 命中。P L200 的欄位是「訊 2026-08-24｜複 2026-09-30」，regex 要求「複」在「訊」前，所以對不上；⟨Q-01⟩⟨Q-02⟩ 前面沒有 ❓／🔎。全庫 `iter_pending` 改前 223、改後 223；`check_pending_markers` 改後印「223 筆（基線 223）」「舊字樣 18 筆」 | 實跑 |
| 參考來源 | 46→32（proposal L18、map L20、ledger L129 N7） | **46→31**。原 46 條砍掉 16 行（L132、L135–139、L146、L150–151、L153、L155、L157、L162、L166、L170–171），加 1 條減速文章一手。§4 的「砍 15」是把 L150–151 當成一條算 | `awk` 數 `## 參考來源` 下的 `^- `：46／31 |
| cell／reader | 本頁 7→1 全配回、釋出 6；鄰居 0；reader 0 | **屬實**，修法後數字也相同 | moves |
| H6 閘檔 | 新檔 `people/pages.md` 不碰閘檔 | **屬實**：`pages.md`、`daily.md` 都不在 `guard_roles.py` L52–56 的 GATE_FILES 裡，本波也不跑 BASELINE_FLAGS | — |
| callout 歸因 | 10-29 附 Google News／Fortune 網址 | **屬實**：`data/source_attribution.jsonl` L3591（2026-10-29、google-news、entities/dario-amodei）的 `item_url` 跟改後 callout 的網址逐字相同，也就是原頁 P L126 留下的那條 | — |
| 安保費算術 | 「底薪 65.4 萬的四倍多、總薪酬約 1,800 萬的 15%」 | **屬實**：callout 和 M L146 都照 verified 第四節寫。改後五頁沒有殘留「4 倍以上」「四倍以上」（P L43、L50、L62、L175 四處都清掉了） | grep |
| open-weights 與減速文章 | 07-27、補全三項主張；09-12 並寫出標題 | **屬實**：主張清單第 3 列寫出三項，含「開源與閉源都要強制安全測試」，附 anthropic.com 連結；M L164 改 09-12〈We Must Pace the Frontier〉；改後主頁的 07-28 和指減速文章的 09-13 都是 0。剩下的 09-13 是 CNBC 中國兩難，是另一件事 | grep |

## 主張清單 10 列的「本人原文」逐列核

第 1、3、6 列算一手：本人網站，RSI L272 查證 09-27；官方部落格，verified #1；CNBC 逐字稿，P L154。第 5 列是本人 X 貼文，經 Simon Willison 全文引述，P L198 寫明「本人第一手發言」，合 pages.md「本人社群貼文」。其餘 6 列都標了「僅媒體轉述」並附連結。第 4 列安理會三點跟 gov-policy L677 逐點相符；第 2 列只有 CNBC 報導，沒有逐字稿，標轉述是保守的做法，照實。**唯一出錯的是第 8 列，見 🔴1。**

## 批評者表三列新列（N2 判準）

Baker：出處 TechCrunch，見 news/2026-08-17 L133；P L198 寫明他批的是 Amodei「過度悲觀描繪 AI」，屬於風險示警。Zuckerberg：NYT 標題「Takes Aim at Anthropic in Debate Over A.I. Slowdown」（P L145），屬於減速呼籲。川普陣營：gov L683 的 Axios 直連，備忘錄點名兩位 Amodei，屬於風險示警（末日論）。三列都合 N2。問題在「何時」欄，見 🔴2。

## 抽驗去向表（4 節）

- **參考來源 16 行砍句**：逐條核過，沒有唯一事實。白宮晚餐五家來源的家在 gov L247／L354（「WSJ 首報；Axios、紐約郵報等至少 5 個來源」）。L166 和 L167 是同一 WIRED 網址。L170 的事實在 archive L43。L162 的 Techmeme 推文只多了「社群留言兩極」，而 08-03 這個事實由 L163 TNW／Fortune 承接。L150–151 的 BBC、VentureBeat 標題住 RSI L272。
- **歷史記錄×08 → archive**：我拿 P L194–207、L40–41 和改後 archive `## 2026-08` 逐行 diff，只有 C 節列的 L194／L196／L200／L202 四處不同，callout 接在 08-24 條下。archive 其餘只改了 L34、L37。
- **核心論述 20 列 → 10 列＋去處**：P L62、L64 進現況和 M L146／L148；P L72–74 進現況第二段；P L81 進角色節「聯署」（拼法改 Suleyman）。06 月各列的原字在 archive L50–56。
- **批評者表**：既有 6 列，除了黃仁勳列（🔴2），原字都沒動；依「何時」重排的結果見 d2 M L74–84。

## 🔴 1　主張清單第 8 列把社群解讀寫成他的主張

- **證據**：draft E 節第 8 列寫「政府應有能力阻止危險 AI 模型發布，**主要針對中國競爭者**」，但出處 news/2026-06-11 L98 原文是「Dario Amodei 接受採訪表示政府應有權阻止危險 AI 模型發布，**社群評論指出**此言論主要針對中國競爭者」。Bloomberg 標題也只說「Government Should Be Able to Block New Models」。新契約 pages.md 寫「只收他本人的公開發言；媒體推測不進表」，這一列等於違反了自己剛立的條文。原字 P L78 會隨 06 月留在 archive L52，不會丟失。
- **修法**（fix_review.py 第 1 處），主張格改成：`| 政府應有能力阻止危險 AI 模型發布 |`

## 🔴 2　判準句寫「『何時』是發言日」，但表中三列不是

- **證據**：①黃仁勳列寫「09-28、09-29」，可是「odd」那段出自 The Ezra Klein Show **09-23 錄製**，09-28 是 Yahoo 的報導日（jensen-huang L52、L74）。健檢卡 §5 早就點出這一點，提案卻寫「既有 6 列原字不動」。②Zuckerberg 只有 NYT 09-16 的標題，③川普陣營備忘錄只有 Axios 09-24 獨家，兩者實際的發言或流傳日都不明。pages.md 自己的條文是「日期不明寫『MM-DD 前』並在格內寫出最早的報導日」，Baker 列已經照這條寫「08-16 前」，這兩列卻沒照做。第 26 波冷讀者質疑的正是「批評者日期對不上」，判準句當場寫錯，會重蹈覆轍。
- **修法**（fix_review.py 第 2–4、6 處，加 build.py 1 處）：
  - 黃仁勳：`| 09-23 錄製（09-28 報導）、09-29 |`，並把這列移到 Vembu（09-23）之後、川普陣營之前，維持依日期排序
  - Zuckerberg：`| 09-16 前 |`，格內 `（[NYT](…) 09-16 報導，僅標題）`
  - 川普陣營：`| 09-24 前 |`，格內 `（[Axios](…) 09-24 獨家）`

## 🟡 3　ledger N6 裁的「量測現況指 RSI 量化表」沒有落進稿

- **證據**：ledger L129 N6 寫「不開『說過 vs 後來』節（資料撐不起，量測現況指 RSI 量化表）」，但改後全文對「量化」的 grep 是 0；verified 第二節 Q2 也指向 RSI 量化表。
- **修法**（fix_review.py 第 5 處）：相關議題 M L99 句尾補「；Anthropic 內部 AI 自動化的量測現況見 [[topics/recursive-self-improvement#自我改進量化指標]]」。我在 d2 實跑：錨點 WARN 0，cell／reader 都 0 新增。

## 🟡 4　參考來源條數 32→31；ledger 兩處理由寫錯

- **證據**：數字見上表。另外 ledger N4 的理由「（有入邊）」與健檢卡「錨點入邊 0」矛盾，提案 N4 的真實理由是「模板允許的專有段」。ledger N3 說「只改指路、不刪內容」，但 P L200 的處理是刪掉 🔎 標頭、把結論改寫為事實（daily-contracts L99），不只是指路。
- **修法**：用 Edit 把 proposal L18、map L20 的 `46→32` 改成 `46→31`。ledger 已提交的 L129 不改，把更正寫進定稿列：「更正 N7：參考來源 46→31（砍 16 行、新 1）；N4 理由應為模板允許的專有段（錨點入邊 0）；N3 中 L200 屬懸置收尾的改寫，不只是指路」。

## 🟡 5　人物角色檔的必讀清單沒有列 pages.md

- **證據**：已有 pages.md 的 6 類記者（commercial、community、devpractice、features、models、safety-policy），角色檔「開始前必讀」都有一條 pages.md（例如 `wiki-reporter-models.md` L15）。提案 §8 說「daily.md L3 已指過去，所以角色檔不改」，但派工時角色檔才是單一來源（`wiki-reporter-people.md` L7），而且它 L23 還寫「可引用聲明…入核心論述」，沒有提覆寫型。少這一條，每日記者最容易照舊 prepend。
- **修法**：Edit `.claude/agents/wiki-reporter-people.md`，在 L14 之後插入一行，原 L15 改號為 4：
  `3. 頁面表格契約 → `.claude/reporter-rules/people/pages.md`——**一頁一節，只讀本次要動的頁的那一節**（先 Grep `^## ` 取節名與行號，再 Read 該範圍）；沒有列在那裡的頁無表格契約`

## 🟡 6　draft、map 要跟修法同步

- **修法**：套完修法後，用 `make_draft.py` 重產 draft（我驗過：原樣重產的輸出跟已提交的 draft 位元組相同；修法後變成 203 行），用 `make_map.py` 重產 map 第二節。步驟見實作單第 4 步。

## 照順序執行（實作單）

`D`＝`<scratchpad>/w27/design`，`V`＝`<scratchpad>/w27/review`。第 0–4 步都要在 `<repo>` 還是原樣時做。

0. **確認原檔沒被 ingest 動過**
   - 指令：`git -C <repo> fetch origin && git -C <repo> diff --stat d6afcdb HEAD -- wiki/entities/dario-amodei.md wiki/entities/dario-amodei-archive.md wiki/entities/michael-burry.md wiki/entities/sridhar-vembu.md wiki/entities/jack-clark.md wiki/topics/recursive-self-improvement.md wiki/index.md .claude/reporter-rules/people/ .claude/agents/wiki-reporter-people.md`，同一組路徑對 `origin/master` 再跑一次，最後跑 `git -C <repo> status --short wiki .claude`
   - 驗收：三個指令都沒有輸出
   - 有輸出時：前五檔有差就停下，續用設計者，讓他以新 HEAD 改 `build.py` 的 `DESIGN_COMMIT` 和行號斷言、`make_map.py` 的 `d6afcdb`，再從第 1 步重來，不准手改。只有 RSI 或 index 有差時照常做，但第 7 步的 handoff 行號要先 grep 重對
1. **備份並套修法**
   - 指令：`cp -a D D.pre-review && python3 -I V/fix_review.py D`
   - 驗收：`fix ok {'newtext.py': 6, 'build.py': 1}`
   - 這支只能跑一次；要重跑，先用 `D.pre-review` 還原
2. **一鍵重跑**
   - 指令：`bash D/rebuild_after.sh <repo>`
   - 驗收（要和我在 `V/d2/` 的實跑結果一致）：
     - `ok {'main': 175, 'archive': 83}`
     - `照搬行逐字核對 83 行；懸置標記（五頁）2→2`、`結論：OK`，兩者各出現兩次
     - `rules ok; daily.md sha c55b4005…`
     - 全部閘 exit 0：`check_pending_markers` 223（基線 223）、cell `無新增超限`、reader `無新增命中`、`錨點 WARN 0`、run_tests exit 0
     - moves：本頁 `配不回 0；改前槽位釋出 6`、鄰居三頁 0、reader `新寫 0`
3. **肉眼抽驗**（`O=D/out/wiki/entities/dario-amodei.md`）
   - `grep -c "主要針對中國" $O` → `0`
   - `grep -n "09-23 錄製（09-28 報導）\|09-16 前\|09-24 前\|自我改進量化指標" $O` → 4 行
   - `grep -c "4 倍以上\|四倍以上\|07-28" $O` → `0`
   - `awk '/^## 參考來源/{f=1;next}/^## /{f=0}f&&/^- /' $O | wc -l` → `31`
4. **重產文件**
   - 指令：`python3 -I D/make_draft.py <repo>/docs/page-audits/dario-amodei-2026-11-05-draft.md && python3 -I D/make_map.py <repo>`
   - 驗收：`draft lines 139`、`71 段 {'M': 120, 'M（改）': 18, 'A': 9, '結構': 5, '改': 38, '砍': 19, 'A（改）': 4}`
   - 接著用 `D/map_rows.md` 換掉 proposal-map 第二節；用 Edit 把 proposal L18、map L20 的 `46→32` 改成 `46→31`，proposal L21 的「照搬 121（含 frontmatter 26）／行內改 17」改成「照搬 120／行內改 18」（🟡4、🟡6）
5. **落地**
   - 指令：`cp -r D/out/wiki/. <repo>/wiki/ && python3 -I D/rules_patch.py <repo> | tail -1 && (cd <repo> && python3 scripts/gen_wiki_frontmatter.py | tail -1)`
   - 驗收：`rules ok; …`，gen exit 0
   - 接著照 🟡5 Edit 角色檔，然後跑 `python3 -I D/verify.py <repo> <repo>/wiki | tail -2`，驗收 `83 行；…2→2`、`結論：OK`
6. **懸置**：不跑 `--rebuild-count`
   - 指令：`cd <repo> && python3 scripts/check_pending_markers.py | grep 筆`
   - 驗收：`懸置標記 223 筆（基線 223，未低於）`、`舊字樣…共 18 筆`
7. **轉知**：提案 §9 的 handoff 1（`--to 主編`，index L72）、handoff 2（`--to 安全政策`，RSI L55、L372–373），每筆先加 `--dry-run` 驗負責人和行號，再正式開立
   - 驗收：兩個單號都印出來
8. **repo 內全閘**
   - `check_hierarchy`、`check_rules`、`check_wiki_freshness` → ✅／OK
   - `check_cell_limits`、`check_reader_language` → OK 無新增
   - `build_web.py` → `錨點 WARN 0`、exit 0
   - `run_tests.py` → exit 0
   - `web_reader` 產物照本專案慣例處理：不 commit 的話，就用 `git show HEAD:<path> > <path>` 還原
9. **ledger**：定稿列要寫的內容
   - 套了 🔴1–2、🟡3–6
   - 🟡4 那句更正（N7 改 46→31、N4 的理由、N3 中 L200 的性質）
   - 頁長 213→175、archive 62→83、懸置 223→223
   - 回訪日 2026-11-12
   - 然後照 dev-done 指名路徑 commit：五頁、`people/pages.md`、`people/daily.md`、角色檔、四份 docs、ledger
