# 第 24 波評審複核：pricing 拆頁實作（2026-11-02）

> 複核的是 `5ddc98b`（wiki＋規則＋帳）、`d3b76c9`（gen frontmatter）、`65c202c`（web）。對照的依據是我上一輪的 `-review.md`（實作單 0–9 步、🔴1–2、🟡1–3）和 `-verified.md` 第四節。設計輸出 `<scratchpad>/w24/design/out/` 跟 repo 四頁的差異只在 gen frontmatter（parent／children／inbound／signal 等），正文逐字相同。我的閘輸出放在 `<scratchpad>/w24/recheck/`。

## 結論

**放行。** 0–9 步全部照做或屬於可接受的偏離，沒有漏做；🔴1–2 和 🟡1–3 都已落地。本輪 🔴 0 條、🟡 1 條（帳面措辭，不擋放行）。

## 逐步表

| 步 | 判定 | 證據 |
|---|---|---|
| 0 驗原檔與官方 | 照做 | `git diff --stat 933a34d 194aa92 -- pricing／archive／reporter-rules／test` 無輸出；verified 第四節逐字寫了「No 5-hour limit for verified accounts.」「10x Pro usage every week」「50% of weekly limits*」（L35–37）。偏離：寫在第四節，沒有照實作單寫成第一節 #12，內容等價 |
| 1–2 套修法、重跑 | 照做 | `split.py` L116 已無 `M_ROW_5H`；正文行 母 293／I 296／H 295（`check_page_thickness.body_lines`），跟評審預期一致；archive 204 |
| 3 肉眼抽驗 | 照做 | 母頁 grep「推論\|5 小時用量窗」只剩 L281（轉售商列，跟 Ultra 無關）；I `^#### ⛔` 0 行；H L48–62 有 09-19、08-10 兩行，「還沒證實的」只剩實驗性重置（H L62） |
| 4 重產 draft／map | 照做 | draft 裡「驗證帳號無 5 小時上限」4 筆；map 在 5ddc98b 改了 2 行 |
| 5 落地 | 照做 | `verify.py <pristine> wiki`：`544 行；懸置 4→4`、`OK`；index L57 投影出三個子故事 |
| 6 懸置基線 | 照做 | `pending-marker-count.json` note 為「3 筆換 slug」，check_pending_markers：212／基線 212 |
| 7 baseline-moves | 照做 | 標題 21–24 波，L7 改成「added 210（107＋46＋57）」，removed 加上 `entities/pricing` |
| 8 全閘 | 照做 | 見下節 |
| 9 帳與收尾 | 照做（兩處偏離） | handoff H-f9ab90／H-1cf735／H-fa1aa2 已開（jsonl L379–381，`list` 有列出），H-645373 已結（L382，`list` 沒列出）；log.md 有 Query 條目；ledger 總帳第 24 列已定稿。偏離一：handoff 4 沒開帳，index 由主編直接改，log 寫了「index 一項主編同波直接改」，`check_log_handoffs` 綠，接受。偏離二：`--from 商業` 跟提案 §6 表 L56–61 相同，不算偏離。gen frontmatter 拆成獨立 commit d3b76c9，無害 |

## 抽驗

- **方案表**（M L64–72）：Max $100＝5x、旗艦 50%、$100 credits；Ultra $200＝每週 10x、驗證帳號無 5 小時上限、旗艦同 Max、$200 credits；Team 池上限 $500（每席 $20／$100 依據的是 M L265 引用的官方文件，10-24 查證）；Enterprise $20／席年繳 20 席起＋API 費率。逐格對得上 verified #1–3 和第四節。
- **Ultra 兩項**：M L69、M L45（「Max、Ultra 與 Team premium 標配、上限為週用量的 50%」，對 verified L37 Team「on premium seats」）、I L41、I L257、H L48 都寫成已查證；「還沒確定」表（M L160–165）已沒有 Ultra 列。
- **API 表**：M L138 Haiku 5.5 $0.10／$0.50（≤100K）、$0.50／$2.50（>100K），快取 $0.01／$0.05，跟 verified #5 一致；M L246 長脈絡「Haiku 5.5 除外」前後一致。
- **事故表**（I L52–59）8 列依序是：10-01 credit 入帳 → 09-09 infostealer → 07-20 帳務 → 04-25 HERMES ⛔ → 10-21 ⚖️ → 10-24 #56281 → 10-24 #79337 → 09-17 #16157；表下第 9 名是 #38335（I L61）。跟評審排序相同。
- **I L176**：`#### ✅ 2026-08-28`。全頁 `^#### ⛔` 0 筆，⛔ 只剩表裡的 HERMES。
- 🟡1 舊名（M L88、L265 已改；L94「Max 5x／20x」在 10-17 查證引文裡，L207／L278 是歷史敘述，照評審不改）、🟡2（M L94 Free 含）、🟡3（H L58、L60）都已落地。

## 閘

- `check_hierarchy` ✅（32 母頁）；`check_pending_markers` ✅ 212／212；`check_wiki_freshness` OK 142 頁；`check_rules` ✅；`build_web` exit 0，`斷鏈 WARN 23／錨點 WARN 0`。build 跑完改到的 `data.js`／`index.html`／`sw.js` 已用 `git show HEAD:` 還原。
- `src/` 下 `python -m unittest tests.test_reader_tags`：6 tests OK。
- `run_tests.py`：exit 1，`FAILED: 1 個失敗、0 個錯誤（共 1334 個案例）`，失敗的就是 `test_repo_currently_has_no_new_hits…`；讀者語言閘 2 筆（known-issues L281、releases L236，都是存量、都不是 pricing 子樹）；字元上限閘 210 筆。紅燈只有這三項，跟預期相符。
- `moves.py tmp_before <repo>`：命中 62、配回 62（換頁名 57）、配不回 0；reader 0／0。
- `git show --stat 5ddc98b` 有 19 檔，沒有一檔符合 `guard_roles.py` L52–56 的 GATE_FILES（`pending-marker-count.json` 不符合 `data/*baseline*.json`）。

## 發現

**🟡1 ledger N8 那條還寫「查證未涵蓋」，跟實作結果對不上。** ledger L126 寫「N8 Ultra 是否取消 5 小時窗進『還沒確定』表；Ultra 是否保留 Fable 50% 上限標『推論』（查證未涵蓋）」。5ddc98b 只改了總帳 L61（`git show 5ddc98b -- ledger.md` 是 1 行替換），實作單第 9 步要的「N8 補記 🔴1 的結果」只寫進了總帳列。只讀裁決紀錄的人會以為這兩項還沒查證。修法：在 L126 句末「H-645373 本波結案。」之後接上這句（裁決紀錄沒有 append-only 約束，前幾波也有補記）：

```
（11-02 補：評審 🔴1 後主 session 逐字重抓 claude.com/pricing，兩項皆官方一手——Ultra 驗證帳號無 5 小時上限、Fable 上限 50% 同 Max——照 N3 移出「還沒確定」表、寫進方案表；原文見 `pricing-2026-11-02-verified.md` 第四節。）
```

**觀察（不列入等級）**：`pricing-incidents` 和 `pricing-history` 的 frontmatter `signal: "孤島"`（inbound 2）。incidents 等 H-f9ab90／H-1cf735 落地後會解除。history 沒有子樹外的 handoff，推論它會維持孤島，跟第 21 波的 `claude-code-features` 同型，留給 `/wiki-lint`。

## 轉知

H-f9ab90（商業→功能，known-issues）、H-1cf735（商業→社群，code-quality-decline）、H-fa1aa2（商業→社群，community-cost）開著；H-645373 已結。本複核不新開帳。
