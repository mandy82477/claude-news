# 第 24 波評審：entities/pricing 拆成母頁＋兩新子頁，計費切割死案歸檔（2026-11-02）

> 審的對象：`pricing-2026-11-02-{proposal,proposal-map,draft}.md`；上游健檢卡、`wave24-cold-reader-2026-11-02.md`、`-verified.md`；ledger 裁決紀錄最上面兩條（N1–N8、八個裁決點）。
> 設計者產物在 `<scratchpad>/w24/design/`（下稱 `D/`）。我的重跑在 `<scratchpad>/w24/review/d/`（下稱 `R/`），是 `D/` 腳本的副本，`out/` 和 `tmp_after/` 都在副本裡重產。改前副本用的是 `<scratchpad>/w24/pristine`。我沒動 `D/`、wiki、規則檔，也沒做 git 寫入。
> 修法已經寫成單一腳本 `<scratchpad>/w24/review/fix_review.py`，在 `R/` 實套過，結果見文末第 2 步。行號：「P Lnnn」指原檔 `wiki/entities/pricing.md`（969 行）；「M／I／H Lnnn」指改後全文。

## 結論

- 🔴 2 條、🟡 3 條。行帳、逐字、懸置、錨點殼、cell／reader 搬家我都重算了，數字全部對得上。
- 🔴1：N8 那兩項現在可以從官方一手查到了，應該照 N3 當批移出。我 11-02 用 WebFetch 抓 claude.com/pricing，Ultra 卡片寫「No 5-hour limit for verified accounts」「10x Pro usage」（每週），Fable 那一列寫 Ultra「50% of weekly limits」。所以母頁、incidents、history 共 6 處還寫「官方未見／推論」，跟官方對不上。設計者把這兩項寫成「未查證」，處理方式本身沒錯，不是把未查證的東西寫成事實；問題出在 verified 沒涵蓋這兩點。
- 🔴2：事故表排序條文我拿現有列實跑，跑出一個漏網：I L176 的 `#### ⛔ 2026-08-28`（Reddit 十週時間軸誤讀）。新條文寫「🔴 ⛔ ⚖️ 同步上表」，而 ⛔ 屬第一層，明天的維護者照字面就會把它排進表的第 3 列，把 #16157 擠出去。這則其實已經用官方一手結案了（同則第 2 條，Help Center 09-20），應標 ✅。
- 頁面在設計後沒被動過：`git log 933a34d..HEAD` 動到 pricing、pricing-archive、known-issues、cqd、community-cost、index、四份規則檔和測試檔的 commit 都是 0 筆。HEAD 現在是 `194aa92`（只加了 page-audit 文件），工作樹乾淨，`news/` 最新的是 11-01。11-02 的 ingest 還沒跑，所以第 0 步要先驗。
- **放行條件**：吃下 🔴1–2 和 🟡1–3，全部在 `fix_review.py` 裡，一次套用。重跑後的輸出要跟第 2 步寫的一致。

## 自己重算的數字

| 項目 | 設計者／主 session | 我重算 | 證據 |
|---|---|---|---|
| 行帳 | P 1–969 每行恰消費一次 | **屬實**。`R/` 重跑 `split.py` 後，`out/` 和 `accounting.txt` 跟 `D/` 的 `diff -r` 一樣。969 筆不重不漏，去向是母 297／I 253／H 249／A 109／砍 45／結構 16 | `R/accounting.txt` |
| 砍掉的 45 行 | 不丟事實 | **屬實**。45 行裡出現的 issue 號（#79337、#38335、#5088、#55982、#16157 等）在四頁都還找得到，一個都沒丟。L297 的 ⚖️／官方承認不轉 ⏸ 判準，搬進了新 pages.md 的「兩條不適用 90 天」。L795 待查證的「5 小時上限是否取消」由 N8 那一列接住（🔴1 會再移出） | 掃描腳本輸出 |
| 照搬逐字、懸置 | 548 行；4→4；全站 212 | **屬實**。`verify.py <pristine>` 和 `verify.py <pristine> R/tmp_after/wiki` 兩種跑法都是 `548 行；4→4`、`OK`；每頁分布是 母 1／I 3／H 0／A 0。`check_pending_markers` 綠 | `R/rebuild.txt` |
| `verify.py` 第一參數 | 指改前副本 | **屬實**。L14 讀 `argv[1]`，L15 讀 `argv[2]`，`rebuild_after.sh` L3 強制要第二參數，L5 和 L9 都傳 `$P` | — |
| `split.py` 防呆 | blob＋乾淨工作樹 | **屬實**。L28–33 比對 `rev-parse HEAD:f == 933a34d:f`，外加 `diff --quiet HEAD`；`rebuild_after.sh` 有 `pipefail`，所以 `\| tail -1 \|\| exit 1` 擋得住。`rules_patch.py` 用 sha256 鎖住 pricing 節，其他 4 筆是 count==1 | — |
| 正文行 | 母 294／I 296／H 293 | **屬實**。用 `check_page_thickness.body_lines` 量 `R/tmp_after`，全行是 323／324／322，archive 231。套修法後是 母 293／I 296／H 295 | — |
| cell／reader | +57 全搬家；reader +0 | **屬實**。`moves.py` 的結果：命中 62、配回 62（換頁名 57）、配不回 0；reader 0／0。FAIL 153→210。套修法後一樣是 210、配不回 0 | `R/gates_after/` |
| 錨點 | WARN 0→0 | **屬實**。repo 裡 `entities/pricing#` 的入邊 wiki 有 11 筆、daily 有 7 筆，節名在母頁都還在。`#事故與爭議（…）` 由母頁 M L298 的 `###` 殼接住（daily/2026-10-24 L56）。build 結果是 `斷鏈 23／錨點 0`、exit 0 | — |
| 規則檔／閘檔 | 不碰 GATE_FILES | **屬實**。改的 5 檔沒有一個符合 `guard_roles.py` L52–56；`--rebuild-count` 不在 L57 的 `BASELINE_FLAGS`，L120 是逐 token 精確比對 | — |
| 方案表對 verified 第一節 | 逐格 | **屬實**。Max $100＝5x、$100 credits；Ultra $200＝10x、$200 credits；Team 池上限 $500；Enterprise $20／席、年繳、20 席起、用量按 API 費率；Pro「無月度 API credits」（M L66–72） | 對 verified #1–3 |
| Haiku 5.5 主表 | 對官方 | **屬實**。我 11-02 WebFetch 官方定價頁：≤100K $0.10／$0.50、快取命中 $0.01；>100K $0.50／$2.50、快取命中 $0.05。跟 M L138 一致 | 官方表 L34–35 |
| 事故表 8 列 | 照條文實跑 | **大致屬實**。第一層是 10-01 → 09-09 → 07-20 → 04-25，第二層 10-21，第三層 10-24（起始 08-02）→ 10-24（起始 07-20）→ 09-17，第 9 名 #38335 落到表下一行。唯一例外是 🔴2 | I L53–62 |

**去向表抽驗**（map 第一節 → `accounting.txt`，5 節都相符）：計費切割 L847–948 → A 100＋砍 2（L849–850）；定價與促銷 L545–788 → H 243＋M 1（L602 懸置回母頁）；配額 L789–846 → I 52＋A 4（06-30）＋砍 1（L795）＋結構 1；事故 L337–544 → I 174＋A 5（06-24）＋砍 17（`%%` 備忘）＋結構 12；還沒確定 L157–176 → M 13＋砍 7。

## 一、冷讀者

**🔴1 Ultra 的 5 小時窗、旗艦 50%：官方方案頁已寫明，頁面還寫「未見／推論」**
- 我查到的一手是 claude.com/pricing（2026-11-02 WebFetch）：Ultra「No 5-hour limit for verified accounts」「10x Pro usage」（每週）；Fable 列 Ultra「Capped at 50% of weekly limits」。這段是 WebFetch 摘要器給的引文，主 session 實作前要逐字再抓一次（第 0 步）。
- 頁面有 6 處要改：M L45 現況（「沿用屬推論」）、M L69 Ultra 列、M L163 還沒確定「Ultra 是否取消 5 小時用量窗」整列（照 N3「查證屬實當批移出」）、I L41 callout、I 事件流 P794 改寫行、H L48 和 L59。
- 修法：`fix_review.py` 前 6 筆替換，加上把 `split.py` L116 的 `+ [T.M_ROW_5H]` 拿掉。改後 Ultra 列是 `| Ultra（原 Max 20x） | $200 | 每週 Pro 的 10 倍用量、驗證帳號無 5 小時上限；旗艦上限同 Max | …`；I callout 改成「2026-11-02 對官方方案頁查證兩件都屬實（$200 一檔現名 Ultra，驗證帳號無 5 小時上限）」。
- ledger N8 要補一句：「11-02 評審 WebFetch 查得，兩項轉 ✅、還沒確定表本波移出 5 列」。verified 第一節加一列 #12（逐字＋連結＋日期）。

**🟡1 現況層殘留舊方案名，跟方案表互相矛盾**
- P L90 寫「Max 20x 的差異不只用量…非單純 Pro 的 20 倍」，但官方現在寫 10x，讀者會讀成兩個數字。P L273（帳務坑 1）寫「Max 5x 每月 $100、Max 20x 每月 $200」，P L117 寫「Max 5x 的 $100」。
- 修法（`M_SUBS` 加 5 筆，都在 `fix_review.py` 裡）：
```python
    (117, "Max 5x 的 $100", "Max 的 $100"),
    (90, "**Max 20x 的差異不只用量**", "**Ultra（原 Max 20x）的差異不只用量**"),
    (90, "非單純 Pro 的 20 倍", "不只是倍數不同"),
    (94, "Pro、Max、Team、Enterprise 皆內含，Free 不含；", "Pro、Max、Team、Enterprise 皆內含（Free 自 10-17 起也含，見下條）；"),
    (273, "載 Max 5x 每月 $100、Max 20x 每月 $200", "載 Max 每月 $100、Ultra（原 Max 20x）每月 $200"),
```
- 不改的：事故標題、訴訟、#47509 裡的「Max 20x」。那些是當時的名字，屬於歷史敘述。

**🟡2 方案細節自打（P L94 對 L95）**
- M L92 寫「Free 不含」Design／Slides／Docs，緊接的 L93 是更正，而方案表 Free 列寫「含」。讀者先讀到的是錯的那句。修法是上面 L94 那一筆。

## 二、明天的維護者

**🔴2 ⛔ 08-28 會被新條文排進表**
- 新 pages.md 寫「🔴 ⛔ ⚖️ 同步上 `## 還在發生的事故` 表」，優先序是「⛔ 與官方已公開承認的 🔴」排第一層。I L176 標題帶 ⛔，條目內卻寫「（不列入總表：本則已結案）」。照條文排，它會落在第 3 列（08-28，介於 infostealer 09-09 和 7 月帳務 07-20 之間），#16157 被截掉。設計者的 17 件清單（draft B 節）漏了這一件。
- 修法：`I_SUBS` 加 `(459, "#### ⛔ 2026-08-28：", "#### ✅ 2026-08-28：")`。依據是同則第 2 條的官方 Help Center（09-20），符合「改 ✅ 需官方確認」。改完全頁 ⛔ 只剩 HERMES（I L56），表的 8 列不變。

**🟡3 history「最近三個月變了什麼」漏了兩則官方已生效、會改到帳單的變動**
- 條文說這一段收「已生效、會改到帳單的變動一則一行」，窗口是 08-02 到 11-02，但清單最早只到 09-14。事件流和母頁都有、這裡漏掉的有兩則：08-10 Sonnet 5 $2／$10 永久化（H L203），09-19 Auto mode classifier 不計費（M L184）。漏掉的話，讀者會以為八月沒有事。
- 修法：`H_RECENT` 在 09-22 那行和 09-14 那行之間插 09-19 一行，在 09-14 之後接 08-10 一行，原文在 `fix_review.py`。08-10 那行 11-10 起照條文由 lint 移除。

**照條文跑過、無發現**：表下可見一行（I L62）照同一排序列出 9 件，比對 I 事件流 🔴 標題，全部對得上，沒有漏件；`%% 未列入總表 %%` 0 筆（N5）。8 列上限、互動數只指 known-issues（I L64）、母頁每日准動清單（N4）跟 page-lifecycle L52 新字，三者一致。commercial 記者派工的寫入目標也都對：daily.md 拆三列；pages.md 第 0 條的路由表是事故 → incidents、沿革 → history、現行事實 → 母頁；archive 只收蒸餾和死案，「重啟寫 history、archive 不回填」。

## 三、機器

**無發現**。補充兩點：
- `fix_review.py` 對同一份 `newtext.py` 只能跑一次（每筆都斷言 count==1）。重跑就失敗，這是預期行為。
- `.claude/reporter-rules/features/daily.md` L50 的例子「Agent SDK 計費切割」已經是死案，但改投目標 `entities/pricing` 是子樹入口，路由由商業 pages.md 第 0 條接手，不影響派工。不列入，留給 `/wiki-lint`。

## 四、治理

**無發現**，只補一個流程項：🔴1 的一手查證屬於主編，所以實作單第 0 步由主 session 逐字重抓，抓到的跟上面不同就停，不准照我的字句硬套。母頁契約：294 行（修後 293）低於 300；路由表一子頁一行（答什麼、最後動態）；`%%` 拆頁評估寫了下一刀；永久殼一個（N2）。兩子頁都過子故事三題：各有自己的使命句和 callout，incidents 有事故表＋38 則事件流，history 有結論段＋41 則事件流；入邊：`[[entities/pricing-incidents…]]` 和 `[[entities/pricing-history…]]` 在改後 wiki 裡各有 11 筆，但都來自子樹內（母頁、互指、archive）和 index 投影；子樹外的入邊等 handoff 1–3 落地才會有（推論：known-issues 💰 組改指之後，incidents 的外部入邊會超過 5 筆）。history 結論段的 11 條各指向母頁的一個家，日期和證據等級（「查證」「官方」）沒有虛報；漏掉的兩則由 🟡3 補上。

## 照順序執行（實作單）

`D`＝`<scratchpad>/w24/design`，`F`＝`<scratchpad>/w24/review/fix_review.py`。第 0–4 步都在 `<repo>` 還是原樣時做。

0. **驗原檔與官方**：
   - `git -C <repo> diff --stat 933a34d HEAD -- wiki/entities/pricing.md wiki/entities/pricing-archive.md .claude/reporter-rules/ src/tests/test_reader_tags.py && git -C <repo> status --short wiki .claude` → 驗收：兩段都沒有輸出。有輸出就停，續用設計者重跑設計，不准手切。
   - 主 session 用 WebFetch 抓 `https://claude.com/pricing`，逐字確認 Ultra 卡片的「No 5-hour limit for verified accounts」和 Fable 列 Ultra 的「50% of weekly limits」。
   - 兩句都在：寫進 verified 第一節 #12，往下做。不符：不跑 F，只吃 🔴2／🟡1–3。做法是把 F 的 `R` 清單刪到只剩 🟡 與 🔴2 那幾筆，並刪掉改 split.py 的那段。
1. **套修法**：`python3 -I F <scratchpad>/w24/design` → 驗收：`fix ok`。
2. **一鍵重跑**：`bash D/rebuild_after.sh <repo> <scratchpad>/w24/pristine` → 驗收：
   - `ok {'pricing': 322, 'pricing-incidents': 324, 'pricing-history': 324, 'pricing-archive': 231}`
   - `照搬行逐字核對 544 行；懸置標記 4→4`、`結論：OK`（少 4 行：P90／94／273／459 改成「改」，P117 本來就是改行）
   - `ok：pricing 節整段＋4 筆，5 檔`；`check_hierarchy … ✅ 通過（32 個母頁）`；`check_pending_markers … ✅`；`check_wiki_freshness … 142 頁`；`check_rules … ✅`；`check_cell_limits` 為 `210 筆`；build 為 `斷鏈 WARN 23／錨點 WARN 0`
   - moves：`配不回（新寫或改長）0`；reader：`0、改後 0`
3. **肉眼抽驗**：
   - `grep -n "推論\|5 小時用量窗" D/out/wiki/entities/pricing.md` → 只剩 M L37 的 `%%` 和一小時表的「推算」，不得出現 Ultra。
   - `grep -n "^#### ⛔" D/out/wiki/entities/pricing-incidents.md` → 0 行。
   - `sed -n 44,62p D/out/wiki/entities/pricing-history.md` → 看得到 09-19、08-10 兩行，「還沒證實的」只剩實驗性重置。
4. **重產 draft／map**：`python3 -I D/make_draft.py <repo> > <repo>/docs/page-audits/pricing-2026-11-02-draft.md && python3 -I D/make_map.py <repo> > <repo>/docs/page-audits/pricing-2026-11-02-proposal-map.md` → 驗收：`grep -c "驗證帳號無 5 小時上限" <repo>/docs/page-audits/pricing-2026-11-02-draft.md` ≥1。
5. **落地**：`python3 -I D/split.py <repo> | tail -1 && cp -r D/out/wiki/. <repo>/wiki/ && python3 -I D/rules_patch.py <repo> && (cd <repo> && python3 scripts/gen_wiki_frontmatter.py | tail -2)` → 驗收：`ok：pricing 節整段＋4 筆，5 檔`；index L56 投影出三個子故事。接著 `python3 -I D/verify.py <scratchpad>/w24/pristine <repo>/wiki | tail -2` → `544 行；4→4`、`OK`。
6. **懸置基線**：`cd <repo> && python3 scripts/check_pending_markers.py --rebuild-count --reason "第 24 波 pricing 拆頁：3 筆換 slug（entities/pricing→entities/pricing-incidents）" | tail -2` → 驗收：212 筆，沒有低於基線。
7. **baseline-moves 文件**（Edit）：`docs/page-audits/claude-code-2026-11-01-baseline-moves.md` L7 的「預期 added 153（第 21 波 107＋第 23 波 46）」改成「預期 added 210（第 21 波 107＋第 23 波 46＋第 24 波 57）」，removed 那句加上舊頁名 `entities/pricing`。reason 字串末尾補「；第 24 波 pricing 拆頁 57 筆同性質，清單見 docs/page-audits/pricing-2026-11-02-proposal-map.md 第四節」。
8. **repo 內全閘**：
   - `cd <repo> && python3 scripts/build_web.py | grep 健檢合計` → `錨點 WARN 0`。
   - `python3 -I D/moves.py D/tmp_before <repo> | head -2` → `配不回 0`。
   - `python3 scripts/run_tests.py; echo exit $?` → 只准 `FAILED: 1 個失敗`（`test_repo_currently_has_no_new_hits…`）、讀者語言閘 2 筆、字元上限閘 **210 筆**、共 1,334 案。
   - 跑完 build_web 若改到 web_reader 產物而本批不打算 commit，用 `git show HEAD:<path> > <path>` 還原。
9. **帳與收尾**：照提案 §6 和「可行性前提」走——handoff 1–4 先 `pending_handoffs.py open --dry-run` 再開，H-645373 結案；`wiki/log.md` 加 Query 條目；ledger 定稿列，N8 補記 🔴1 的結果。commit 用指名 `git add`：四頁、index（gen 投影）、known-issues／ai-agent-safety（gen frontmatter）、規則檔 4 份、test、`data/pending-marker-count.json`、baseline-moves、draft／map／review。
