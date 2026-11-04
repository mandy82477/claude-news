# 第 23 波評審：topics/anthropic-business 拆成母頁＋兩新子頁，營收估值併入 anthropic-ipo（2026-11-02）

> 審的對象：`anthropic-business-2026-11-02-{proposal,proposal-map,draft}.md`；上游健檢卡、`wave23-cold-reader-2026-11-02.md`、`-verified.md`（含第四節 N4 補查）；ledger 裁決紀錄最上面兩條（N1–N8、八個裁決點）。
> 設計者產物在 `<scratchpad>/w23/design/`（下稱 `D/`），我的重跑在 `<scratchpad>/w23/review/`（下稱 `R/`：`R/run/` 是 split／verify／moves 的副本，`R/pristine/` 是 `git archive 702e5a6 wiki scripts`，`R/rcopy/` 是 HEAD `.claude/` 套 `rules_patch.py` 的副本）。我沒改 `D/`、wiki、規則檔，也沒做 git 寫入。
> 行號：「B Lnnn」指原檔 `wiki/topics/anthropic-business.md`（1,048 行），「I Lnnn」指原檔 `anthropic-ipo.md`（211 行），「P／R／M Lnnn」指 `D/out/wiki/topics/` 下的改後全文。

## 結論

- 🔴 3 條、🟡 6 條。切法、行帳、懸置、錨點殼、cell／reader 搬家都重算過，數字對得上。
- 🔴1：N4 補查沒寫進三大雲表。P L49–50 還是「2023–2024 共 $40 億」「未見持股報導」，跟 ledger N4 和 verified 第四節都對不上。
- 🔴2：`rebuild_after.sh` 寫的是 `split.py … | tail -1 || exit 1`。管線的退出碼是 `tail` 的，所以防呆斷言紅了腳本也不會停，接著會把舊的 `out/wiki` 拷進副本，閘照樣全綠。
- 🔴3：母頁 `## IPO 走到哪一格` 的一句結論沒有任何人會去更新它。每日 ingest 准動的清單沒有它，週更觸發邊（第 10 條：1、4、5、6、12）也沒有第 2 條。所以五格表一換值（⟨Q-03⟩ 11-24 複查），母頁跟 ipo 就會互相矛盾。
- 頁面設計後沒被動過：`git log 702e5a6..HEAD` 動到六個檔的 commit 是 0 筆（只有 `85faced`，三份 page-audit 文件加 ledger），工作樹乾淨，`news/` 最新的是 11-01。不過 11-02 的 ingest 還沒跑，所以實作單第 0 步要先驗這件事。
- **放行條件**：照文末清單吃下 🔴1–3，6 條 🟡 同一輪吃掉（每條都是改單一來源腳本裡的一兩行）。重跑後的驗收輸出要跟清單寫的一致。

## 自己重算的數字

| 項目 | 主 session／設計者 | 我重算 | 證據 |
|---|---|---|---|
| 行帳 | B 1–1,048、I 1–211 每行恰消費一次 | **屬實**。我在 `R/run/` 重跑 `split.py`，產出跟 `D/out/wiki` 的 `diff -r` 一樣，`accounting.txt` 也一樣。計數是 A 159／I 151／M 166／P 317／R 198／砍 1／結構 56，合計 1,048 | `R/run/accounting.txt` |
| 照搬逐字、懸置 | 912 行；3→3；全站 212→212 | **屬實**。`verify.py R/pristine` 和 `verify.py R/pristine D/tmp_after/wiki`（過 gen 之後）兩種跑法都得到 `912 行；3→3`、`結論：OK`。`D/gates_after/check_pending_markers.txt` 是 212 筆／基線 212，其中 1 筆換 slug（Post-Crescent） | — |
| 第一參數能不能指向改前副本 | 可以 | **可以**。原檔讀的是 `argv[1]`，改後頁讀的是 `argv[2]`。但實作後如果把 `<repo>` 當第一參數，就會變成拿新頁去比新頁，所以第一參數一定要是 pristine（清單第 6 步） | `verify.py` L16–21 |
| 防呆記 blob | 比對 `702e5a6` 六檔 blob | **屬實**。它對每個檔做 `rev-parse HEAD:f == 702e5a6:f`，外加 `diff --quiet HEAD`。只是 🔴2 讓它在一鍵腳本裡失效 | `split.py` L22–34 |
| 正文行 | 母 189／ipo 396／合作算力 449／風險 312 | **屬實**。用 `check_page_thickness.body_lines` 跑 `D/tmp_after`，全行數是 220／422／481／342；archive 401→565 行，時序條目 178→249（＋71） | — |
| 時序歸群 | 母 8／ipo 57／合作算力 88／風險 56；公司動態 9 則 | **屬實**。G0 新 8＋舊 1（舊的那 1 則隨 08 月進 archive），和 ledger (4)「9 則」一致；L774 覆寫後 G2 57、G3 56 | `timeline_groups.json` |
| cell 搬家 | ＋46，全部配回；reader ＋0 | **屬實**。`moves.py D/tmp_before D/tmp_after` 的結果是命中 46、配回 46、配不回 0、改前槽位未用 28；reader 改前 0、改後 0。FAIL 107→153，存量 419→345（business 原本那 74 筆＝46 搬走＋28 失效） | — |
| daily/ 錨點 | 7 筆 | **屬實**。`#還沒過去的風險` 2、`#這些數字是誰說的` 1、`#哪個合作會改到你用的 Claude` 4；`#時序`、`#IPO 走到哪一格`、`#現在的數字` 在母頁都留著。build 錨點 WARN 0→0 | `grep -rnoE` |
| rules_patch | 9 檔，不碰閘檔 | **屬實**。在 HEAD 副本實套，輸出 `ok：24 筆，9 檔`；9 檔沒有一個符合 `guard_roles.py` L52–56 的 `GATE_FILES`。`--rebuild-count` 不在 L57 的 `BASELINE_FLAGS` 裡（L120 是逐 token 精確比對） | `R/rcopy/` |
| 子樹認領 | 不加 override | **屬實**。四頁的 `reporter_of` 都是 `wiki-reporter-commercial`，`owner_of` 都是「商業」 | `D/tmp_after` 實測 |

**去向表抽驗**（map 一節 → `accounting.txt` 計數，4 節都相符）：數字細節 B66–96 → I 29＋P 2（B79–80 Accenture）；商業模式 B106–137 → R 32；戰略合作細節 B468–529 → P 50＋A 12；風險節 B216–285 → R 64＋I 5（唱空）＋砍 1（B226）。另外 map 寫清單 B353–463「109 行」，實際是 111（P 81＝79 列＋2 行標題），不影響帳。

**重點審 1（N1 保命）**：B226 不是任何懸置標記的家，這列砍掉後它的事實仍住在風險子頁：B277（07-21 提告、兩個專利號、要求禁制令、「將全力抗辯」、Bloomberg Law）和 B278（Knoxville 同案、08-24 Daily Beacon 跟進）都去了 R；表下也有一句點名（`newtext.py` L144），細節區另加了 `%%` 讓位註記（L151）。時序那份副本（B936，08-24）隨 08 月進了 archive。**不列 🔴**。

## 一、機器

**🔴2 一鍵重跑腳本吞掉防呆，而且沒套規則檔**
- `D/rebuild_after.sh` L5 的 `python3 -I $H/split.py $R | tail -1 || exit 1` 沒開 `pipefail`。L6 的 `verify.py $R` 拿現行 repo 當改前副本，實作後重跑會變成拿新頁比新頁。腳本裡也沒有 `rules_patch.py`，可是提案 §7 說 `tmp_after` 是「套本案＋規則檔」。build_web 也沒有串進來。
- 修法：整檔換成下面這份。

```bash
#!/bin/bash
# 用法：bash rebuild_after.sh <repo> <改前副本>：重切、獨立核對、重建 tmp_after（含規則檔）、跑閘與 build_web
set -u -o pipefail
H=$(cd "$(dirname "$0")" && pwd); R=$1; P=${2:?第二參數＝改前副本（git archive 702e5a6 wiki scripts）}
python3 -I $H/split.py $R | tail -1 || exit 1
python3 -I $H/verify.py $P | tail -2 || exit 1
rm -rf $H/tmp_after && cp -a $R $H/tmp_after && cp -r $H/out/wiki/. $H/tmp_after/wiki/
python3 -I $H/rules_patch.py $H/tmp_after || exit 1
bash $H/gates.sh $H/tmp_after after
(cd $H/tmp_after && python3 scripts/build_web.py > $H/build_after.txt 2>&1; echo "build exit $?"; grep 健檢合計 $H/build_after.txt)
python3 -I $H/moves.py $H/tmp_before $H/tmp_after | head -3
```

**🟡2 風險表排序違反第 4 條**
- 第 4 條規定「嚴重度降序，同級依最後動態新者在上」。改後 R L48–55 的 ⚠️ 中依序是 10-26、09-17、09-06、10-27，保險列（B227，10-27）排在最底。這是原表就有的錯，但這次插了新列，正好一起修。
- 修法：`D/split.py` 的「風險節」頭兩行（`R_RISK = …` 和 `R_RISK += take("B", 227, 229, …`）換成：
```python
R_RISK = take("B", 216, 223, "R") + take("B", 227, 227, "R") + [T.R_NEW_ROW] + take("B", 224, 225, "R")
mark("B", 226, 226, "砍（UTRF 列讓位；結論與懸置無涉，細節住 L277–278）")
R_RISK += take("B", 228, 229, "R") + T.R_AFTER_LEGEND + take("B", 230, 236, "R") + [T.R_MEMO_NEW]
```
（原本中間那行 `mark(...)` 刪掉，免得重複消費；verify 用多重集比對，不受列序影響。）

**🟡5 網站人物頁 chip 與讀者標籤看守沒跟上子樹**（第 22 波 `7ec4d2b` 同 commit 有改這兩處）
- `web_reader/assets/app.js` L955–961 的 `PPL_ISSUE_SHORT` 沒有三個子頁。L1186 的退路是取名稱前 7 字加「…」，所以會顯示成「Anthrop…」。tom-brown 改指合作算力頁後立刻就會碰到。
- 修法：在 L960 `'market-signals-customers': '投資·定價客戶',` 後面加 `'anthropic-ipo': '商業·上市財報', 'anthropic-partnerships-compute': '商業·合作算力', 'anthropic-business-risks': '商業·風險',`
- `src/tests/test_reader_tags.py` L77 `"anthropic-business": …` 後面加三行：
```python
        "anthropic-ipo": "同 anthropic-business（第 23 波子樹）",
        "anthropic-partnerships-compute": "同 anthropic-business（第 23 波拆出的子頁）",
        "anthropic-business-risks": "同 anthropic-business（第 23 波拆出的子頁）",
```

## 二、明天的維護者

**🔴3 母頁 IPO 一句結論沒有寫入邊**
- 在 `rules_patch.py` 的 `SUB_ROUTE`，把「母頁每日只動：頂部 callout、`## 往下鑽：三條子線` 路由表的「最後動態」、`## 現在的數字`（第 1 條）、」改成「母頁每日只動：頂部 callout、`## 往下鑽：三條子線` 路由表的「最後動態」、`## 現在的數字`（第 1 條）、`## IPO 走到哪一格` 的一句結論（ipo 五格表任一格換值時同批覆寫，第 2 條）、」。
- 第 2 條 patch 新字串裡的「母頁 `## IPO 走到哪一格` 只留一句結論加連結；」改成「母頁 `## IPO 走到哪一格` 只留一句結論加連結，五格表任一格換值時同批覆寫這一句；」。
- page-lifecycle patch 新字串裡的「`topics/anthropic-business` 的 `## 現在的數字`（指標換值）與 `## 時序`（只收公司動態）」改成「`topics/anthropic-business` 的 `## 現在的數字`（指標換值）、`## IPO 走到哪一格`（一句結論，隨 ipo 五格表覆寫）與 `## 時序`（只收公司動態）」。
- daily.md patch 母頁列的「`## 現在的數字` 指標換值；」改成「`## 現在的數字` 指標換值；`## IPO 走到哪一格` 一句結論（五格表換值時同批）；」。

**🟡4 兩處派工字面會讓同一則寫兩個家**
- `rules_patch.py` 的 daily.md 合作算力列寫了「企業採用率」，但企業採用率（Ramp 指數）是母頁 `## 現在的數字` 的一列（M L57），第 0 條路由表也沒有這一類。修法：把該列的「戰略合作、收購、算力合約與資本支出、政府採購、企業採用率」改成「戰略合作、收購、算力合約與資本支出、政府採購、具名企業導入（採用率指數換值寫母頁 `## 現在的數字`）」。
- `.claude/reporter-rules/market/daily.md` L33（一手財務揭露：S-1、毛利率、客戶集中度）還指 `anthropic-business「現在的數字」`，但 S-1 表現在的家是 ipo。修法：在 `PATCHES` 末尾加一筆：
```python
    (".claude/reporter-rules/market/daily.md",
     "| [[topics/anthropic-business]]「現在的數字」 |",
     "| [[topics/anthropic-ipo]]「S-1 揭露了什麼」（指標換值在 [[topics/anthropic-business]]「現在的數字」） |"),
```
（舊子字串在 HEAD 只出現 1 次，已驗。）

## 三、冷讀者

**🔴1 三大雲表沒照 N4 補查改**
- ledger N4 和 verified 第四節都寫了：Microsoft 承諾投資最高 $50 億（2025-11）＋$300 億 Azure；Amazon 累計 $80 億（2023-09～2024-11 三筆）＋Series H $50 億。`newtext.py` L118–119、P L49–50、draft L104–105 還是舊字。全 wiki 也找不到這兩個數字的其他家（grep「80 億」「Microsoft…50 億」都是 0），所以這張表就是它們的家，出處要寫在頁上。
- 修法：`D/newtext.py` 的 `P_CLOUDS`，Amazon 列的「2023–2024 共 $40 億（媒體稱）；」改成「累計 $80 億（2023-09～2024-11 三筆，媒體稱）；」。Microsoft 列的「| 未見持股報導 | Azure 容量 $300 億（[官方 05-06 公告]({SPACEX_URL})提及，2026-11-02 查證） |」改成「| 2025-11 承諾投資最高 $50 億（多家報導；實際入股金額未見） | 承諾購買 Azure 容量 $300 億（2025-11；[官方 05-06 公告]({SPACEX_URL})提及） |」。表後那行空行之後插一行：
```python
    "Amazon 累計 $80 億與 Microsoft 承諾最高 $50 億是 2026-11-02 多家媒體交叉（[Fortune](https://fortune.com/2024/11/22/amazon-4-billion-investment-startup-anthropic-founder-defected-openai/)、[Nasdaq](https://www.nasdaq.com/articles/microsoft-and-nvidia-deals-push-anthropic-toward-350-bln-valuation)），未見 Anthropic 一手。",
    "",
```
（合作算力頁因此多 2 行：全行 483，正文 451。）

**🟡3 兩處引號節名搬家後指錯頁**（提案 §1 把這類列為 lint 候選；這兩處對讀者是直接誤導，成本是 2 筆 sub）
- 在 `D/newtext.py` 末尾加：
```python
B_SUBS += [
    (203, "與本頁「企業採用率」43.5%", "與 [[topics/anthropic-business#現在的數字]]「企業採用率」43.5%"),
    (1023, "同日 UTRF 專利訴訟成案（見風險表）", "同日 UTRF 專利訴訟成案（見 [[topics/anthropic-business-risks#還沒過去的風險]] 細節區）"),
]
```
（B203 去了 ipo，那頁沒有企業採用率；B1023 留在母頁的 07 月總結，母頁沒有風險表，UTRF 也已經讓位出表。）

**分得出 market-signals 嗎**：三頁的使命句後半各有一句互指（P L28、R L28、ipo L28），母頁路由表上方也有一句總指 market-signals。ms 那一側的對稱句走 handoff 2(e)。子故事三題三頁都過：各有自己的 callout（11-01）和時序（88／56／57 則），也各有入邊（ipo→P 算力、competitor→R、ms-customers→P 殼）。母頁 189 行，比 300 少；路由表一子頁一行（答什麼、最後動態）；未歸類節在。**無發現**，🔴3 除外。

## 四、治理

**🟡1 第 4 條「訴訟一律留表」跟 N1 讓位字面衝突**
- pages.md L39 寫「**訴訟不適用 90 天**——在判決、和解或撤訴前一律留表」。週更 5j 照字面讀，會把 UTRF 補回表裡、把別列擠掉，下一輪再照留表優先序讓出去，來回翻。
- 修法：在 `PATCHES` 加一筆（舊子字串在 HEAD 只出現 1 次，已驗）：
```python
    (CP, "**訴訟不適用 90 天**——在判決、和解或撤訴前一律留表。",
     "**訴訟不適用 90 天**——在判決、和解或撤訴前不因 90 天退場；表滿載時仍照下方留表優先序讓位（細節區保留、表下點名）。"),
```

**🟡6 使用者本機重建清單還寫 107**
- `docs/page-audits/claude-code-2026-11-01-baseline-moves.md` 第 1 步寫「預期 added 107」，reason 也只寫第 21 波。N6 累計後是 153，使用者照舊字去跑會對不上。
- 修法：第 1 步的「預期 added 107／removed 181」改成「預期 added 153（第 21 波 107＋第 23 波 46）；removed 以輸出為準，都在舊頁名 `entities/claude-code`、`topics/anthropic-business` 下」。reason 字串末尾加「；第 23 波 anthropic-business 拆頁 46 筆同性質，清單見 docs/page-audits/anthropic-business-2026-11-02-proposal-map.md 第六節」。

## 照順序執行（實作單）

`D`＝`<scratchpad>/w23/design`。第 1–5 步都在 `<repo>` 還是原樣時做。

0. **驗原檔沒被 ingest 動過**：`git -C <repo> diff --stat 702e5a6 HEAD -- wiki/topics/anthropic-business.md wiki/topics/anthropic-ipo.md wiki/topics/anthropic-business-archive.md wiki/topics/competitor-landscape.md wiki/entities/google-investment.md wiki/index.md .claude/ && git -C <repo> status --short wiki .claude` → 驗收：**兩段都沒有輸出**。有輸出就停：續用設計者，把 diff 附上（新條目照第 0 條路由入 newtext／split、`DESIGN_COMMIT` 改成新 HEAD、行號重對），然後從第 1 步重跑；不准手切。
1. **改單一來源**（Edit）：`D/newtext.py` 吃 🔴1、🟡3；`D/split.py` 吃 🟡2；`D/rules_patch.py` 吃 🔴3、🟡1、🟡4；`D/rebuild_after.sh` 整檔換成 🔴2 那份。
2. **改前副本**：`mkdir -p <scratchpad>/w23/pristine && git -C <repo> archive 702e5a6 wiki scripts | tar -x -C <scratchpad>/w23/pristine` → 驗收：`ls <scratchpad>/w23/pristine/wiki/topics/anthropic-business.md` 存在。
3. **一鍵重跑**：`bash D/rebuild_after.sh <repo> <scratchpad>/w23/pristine` → 驗收：
   - `ok {'anthropic-ipo': 422, 'anthropic-partnerships-compute': 483, 'anthropic-business-risks': 342, 'anthropic-business': 220, 'anthropic-business-archive': 565} …`
   - `照搬行逐字核對 910 行；懸置標記 3→3`、`結論：OK`（少 2 行是 🟡3 那兩筆改成「改」）
   - 規則檔 `ok：26 筆，9 檔`；`check_rules exit 0`；`check_hierarchy … ✅ 通過（32 個母頁）`；`check_pending_markers … ✅`；`check_wiki_freshness … 140 頁`；`check_cell_limits` 是 `153 筆`
   - `build exit 0`、`錨點 WARN 0`
   - moves 是 `配不回（新寫或改長）0`、reader `0、改後 0`
4. **肉眼抽驗**：`sed -n 47,53p D/out/wiki/topics/anthropic-partnerships-compute.md`，要看到「累計 $80 億」「承諾投資最高 $50 億」和出處行；`sed -n 46,55p D/out/wiki/topics/anthropic-business-risks.md`，⚠️ 中的日期要是 10-27、10-26、09-17、09-06。
5. **重產 draft／map**（repo 還沒動，讀的是原檔）：`python3 -I D/make_draft.py <repo> > <repo>/docs/page-audits/anthropic-business-2026-11-02-draft.md && python3 -I D/make_map.py <repo> > <repo>/docs/page-audits/anthropic-business-2026-11-02-proposal-map.md` → 驗收：`grep -c "累計 \$80 億" <repo>/docs/page-audits/anthropic-business-2026-11-02-draft.md` ≥1。
6. **落地**：`python3 -I D/split.py <repo> | tail -1 && cp -r D/out/wiki/. <repo>/wiki/ && python3 -I D/rules_patch.py <repo> && (cd <repo> && python3 scripts/gen_wiki_frontmatter.py | tail -3)` → 驗收：`ok：26 筆，9 檔`、`index 子故事投影：改動 1 列`。接著 `python3 -I D/verify.py <scratchpad>/w23/pristine <repo>/wiki | tail -2` → 驗收：`910 行；懸置標記 3→3`、`結論：OK`。
7. **網站與測試**（Edit）：照 🟡5 改 `web_reader/assets/app.js` L960 和 `src/tests/test_reader_tags.py` L77；照 🟡6 改 `docs/page-audits/claude-code-2026-11-01-baseline-moves.md` 第 1 步。
8. **懸置基線**：`cd <repo> && python3 scripts/check_pending_markers.py --rebuild-count --reason "第 23 波 business 拆頁：Post-Crescent 1 筆換 slug（topics/anthropic-business→topics/anthropic-business-risks）" | tail -2` → 驗收：212 筆、沒有低於基線。
9. **repo 內全閘**：`cd <repo> && python3 scripts/build_web.py | grep 健檢合計` → `錨點 WARN 0`；`python3 -I D/moves.py D/tmp_before <repo> | head -2` → `配不回（新寫或改長）0`；`python3 scripts/run_tests.py; echo exit $?` → 驗收：`FAILED: 1 個失敗`（`test_repo_currently_has_no_new_hits…`）、讀者語言閘 2 筆、字元上限閘 **153 筆**、共 1,334 案。紅的只准是這一組（N6）。
10. **帳與收尾**照提案 §6 與「可行性前提」：handoff 1–3 先 `pending_handoffs.py open --dry-run` 再開，H-6109b3 結案（note 寫明第 3 項移入 handoff 2(d)），然後是 `devpractice_diff.py mark`、`wiki/log.md` Query 條目、ledger 定稿列。commit 指名 `git add`：五頁＋鄰居三檔、規則檔 9 份、`data/pending-marker-count.json`、app.js、test、baseline-moves 檔、draft／map。
