# 第 23 波評審複核：實作是否照實作單（2026-11-02）

> 上一輪：`anthropic-business-2026-11-02-review.md`（🔴1–3、🟡1–6、實作單 0–10 步）。原評審 agent 無法續用，本輪由新評審接手，把那份當自己的上一輪。
> 對象：`dc81869`（實作）＋`9b5d0e5`（gen）＋`f15d236`（web）。複核途中主 session 又提交了 `26d5774`（冷讀者複驗修正），本檔兩個版本都核過。
> 暫存在 `<scratchpad>/w23/recheck/`；`D/`＝`<scratchpad>/w23/design/`，`P/`＝`<scratchpad>/w23/pristine/`。我沒改 repo 檔（build_web 改到的 `web_reader/` 兩次都用 `git show HEAD:` 還原），也沒做 git 寫入。

## 逐步表

| 步 | 判定 | 證據 |
|---|---|---|
| 0 驗原檔 | 照做 | `702e5a6..85faced` 沒有動到六檔（上一輪已驗）；`dc81869` 是第一個動到它們的 commit |
| 1 改單一來源 | 照做 | 對 `.bak` 做 diff：`newtext.py` L118–121 吃 🔴1、L313–317 吃 🟡3；`split.py` L186/188 吃 🟡2；`rules_patch.py` L20/31/55/57/68 吃 🔴3＋🟡4、L79–83 吃 🟡1＋🟡4；`rebuild_after.sh` 跟上一輪那份逐字一致 |
| 2 改前副本 | 照做 | `P/wiki/topics/anthropic-business.md` 在 |
| 3 一鍵重跑 | 照做 | 用 `verify.py P/ <dc81869 的 wiki>` 重跑：`照搬行逐字核對 910 行；懸置標記 3→3`、`結論：OK` |
| 4 肉眼抽驗 | 照做 | 合作算力頁 L49「累計 $80 億」、L50「承諾投資最高 $50 億」、L52 出處行；風險頁 L50–53 的 ⚠️ 中依序是 10-27／10-26／09-17／09-06 |
| 5 重產 draft／map | 照做 | 拿 `P/` 重跑 `make_draft`／`make_map`，跟 repo 檔 `diff` 都是 0。draft 有 2 處「累計 $80 億」。map 內容沒變，所以沒進 commit，屬實 |
| 6 落地 | 照做 | `D/out/wiki` 八個檔跟 `dc81869` 只差 gen 欄位（last_updated、inbound_links、parent/children、index 投影），正文差 0 |
| 7 網站與測試 | 照做 | `app.js` L960 補了三個 chip；`test_reader_tags.py` L78–80 補三行；baseline-moves 第 1 步改成 153 |
| 7 附 | 偏離（已知，可接受） | baseline-moves 檔標題改成「第 21–23 波」，加了一段說明「第 22 波貢獻 0 筆」。這兩處不影響本機指令 |
| 8 懸置基線 | 照做 | `pending-marker-count.json` count 212，note 跟實作單逐字一致；Post-Crescent 的 key 換成 `anthropic-business-risks` |
| 9 全閘 | 照做 | 見下節 |
| 10 帳與收尾 | 照做，一處已知偏離 | H-fec1b0／H-4dbf62／H-f000d4 是 open，H-6109b3 是 done；log 有 Query 條目；ledger 第 23 列定稿。`devpractice_diff.py mark` 沒做，理由寫在 log 第 4 點（第 20–22 波同樣沒做），**接受** |

## 新文字抽驗（照 verified）

- **淨損**：母頁 L58 寫「約 $724 億是可轉換工具…非現金」「營業層虧約 $6.9 億」，等級是「一級媒體引公司（多家引 S-1）」，對 verified #2 ✅
- **獲利**：母頁 L57 寫「調整後營業利益（排除股權報酬、非現金捐贈、和解費用）…S-1 上半年調整後約 $16 億」；ipo L82 新增「營業損益口徑」列。對 #3 ✅
- **三大雲**：合作算力頁 L49–50、L52 的字面跟 🔴1 修法逐字一致，對 verified 第四節 ✅
- **anthropic-ipo 四處過期句**：L46「五件事」、L52「10-20 外流草稿首度揭露，10-26 公開版多家引同數字」、L56「下一個時點：股數與價格區間」、L63 結論都改了。原本 I L44/L50/L54/L61 的舊句已經不在 ✅。時序 L172、L304 留著「S-1 首度揭露」，那是當日原文，屬不可改的過去，不改
- **⟨Q-03⟩**（ipo L200）：問句改成「掛牌日與價格區間何時公布」；`複 2026-11-24`；探針「calcalistech、IPO 延後」沒動，照 N8 ✅
- **H-6109b3 三項落地**：ipo L40、L46 指向 `market-signals-ipo`，L419 改成 `market-signals-ipo`；原 B711 現在是 risks L255，指向 `market-signals-customers`；Nscale 口徑寫在合作算力頁 L66。第 3 項已移入 H-4dbf62(d) ✅
- **頁長**：母頁全行 219／正文 189，≤300 ✅。子頁全行／正文：ipo 422／396、合作算力 482／451、風險 341／312，都 ≤600 ✅

## 閘（在 HEAD 跑；f15d236 與 26d5774 兩次結果相同）

- `check_hierarchy` ✅（32 個母頁）；`check_pending_markers` ✅（212 筆，基線 212）；`check_wiki_freshness` OK（140 頁）；`check_rules` ✅；三者 exit 0
- `build_web` exit 0：`斷鏈 WARN 23／錨點 WARN 0`。斷鏈 23 跟改前 `D/build_before.txt` 一樣，不是本波帶來的
- `python -m unittest tests.test_reader_tags`：6 個 OK
- `run_tests.py` exit 1，紅的只有三組：
  - `FAILED: 1 個失敗`（`test_repo_currently_has_no_new_hits…`，共 1334 案）
  - 讀者語言閘 2 筆
  - 字元上限閘 153 筆
  
  這組正是預期的 N6 組合 ✅
- `moves.py D/tmp_before <repo>`：`配不回（新寫或改長）0`、reader 0 ✅
- 四個 commit 的 `--stat` 都沒有 `scripts/check_*`、`data/*baseline*`、`data/*-allow.json` ✅

## 發現

**🟡A 風險表 ⚠️ 高 兩列也違反第 4 條「同級新者在上」**
- 位置：`wiki/topics/anthropic-business-risks.md` L48（10-16）排在 L49（10-26）上面。
- 來歷：這是原表 B216–B217 的順序。我上一輪只抓了 ⚠️ 中，漏了這組。
- 修法：L48 跟 L49 兩列對調（只換列序，內容不改）。也可以留給商業記者下次覆寫時照第 4 條順手排。

**ℹ️B `26d5774` 之後 verify 會變 FAIL，這是預期中的**
- 在 HEAD 跑 `verify.py P/ <repo>/wiki` 得到 909 行、`缺：B227`。原因是 26d5774 照冷讀者複驗，把保險列的來源等級從「官方一手（S-1）」改成「多家引 S-1＋一級媒體」，這是刻意更正，不是回歸。
- 同一份 verify 對 `dc81869` 是 910、OK。
- 修法：不必修。之後若要拿 verify 當驗收，要以 `dc81869` 為對象，ledger 第 23 列不必改。

## 放行

**放行。** 🔴1–3、🟡1–6 都已落地，閘的結果跟實作單的驗收值一致。已知偏離兩處（devpractice mark 沒做、baseline-moves 標題改寫），都有理由也有紀錄，接受。🟡A 不擋放行。
