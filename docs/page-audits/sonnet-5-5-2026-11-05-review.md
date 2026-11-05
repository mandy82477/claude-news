# 第 28 波評審：entities/sonnet-5-5（2026-11-05）

> 對象：提案三件（`-proposal`／`-proposal-map`／`-draft`）＋設計者產物 `<scratchpad>/w28/design/`（`out/wiki/entities/sonnet-5-5.md`、`tmp_after/`、`apply.py`、`rules_patch.py`、`handoff.md`）。上游：健檢卡、冷讀者、verified（含第五節）。ledger 十點與 N1–N7 已判定，不重開。
> 評審自己做的一手複核（2026-11-05 WebFetch）：官方發布文（基準表與四條註腳、effort 預設句、設計句）、What's new 全文、Claude Code model-config（預設、別名、effort、fallback、v2.1.280 前沿革）、Sonnet 5 模型頁。行號：新頁指 `out/` 檔（204 行），鄰居指 HEAD `63e1c49`（wiki 內容與 `e66cc9d` 相同）。

## 〇、數字重算

| 項目 | 主 session／設計者 | 評審重算 | 結論 |
|---|---|---|---|
| 主頁行數 | 190→204（正文 164→178） | `wc -l` 190／204；扣 frontmatter 26 行＝164／178 | ✅ |
| 懸置計數 | 223→221（−2） | HEAD 基線 223 筆指紋；`tmp_after` 基線 221；差集恰為 `entities/sonnet-5-5::…v2.1.284、claude code cli 預設` 與 `entities/sonnet-5::…sonnet 5.5、claude code cli 預設` 兩筆，新增 0；副本跑 `check_pending_markers.py` ✅ | ✅（副本 note 是 `sim`，實作時要用正式 `--reason`） |
| 基準項數 | 8 項 | 發布文表 8 列（verified 第一節 7 列＋第五節 FrontierCode）；新頁 L107–114 的 8 列 × 3 欄，24 格裡 23 格與 verified 逐字相同 | ⚠️ FrontierCode 的 Sonnet 5.5 只寫 46.2%，沒照 N2 寫兩個數（🔴1） |
| 表下去重 | 11 條→8 條 | HEAD 三處表下共 12 條（對照表 5 條、基準 5 條、說話 2 條）；新頁 9 條（補充 4、基準 4、說話補充 1） | 數字小誤，不影響實作 |
| 「GDPval 差兩分」 | 4 處→0 | HEAD `grep -c 兩分`＝4；新頁 0 | ✅ |
| v2.1.284 | 8 行→6 行 | 8／6 | ✅ |
| 閘（副本） | cell／reader／pending 綠 | 評審在 `tmp_after` 重跑：`check_cell_limits` OK、`check_reader_language` OK、`check_pending_markers` ✅ 221 | ✅ |

## 一、去向表抽驗（6 節）

| 原節 | 去向表寫的 | 新頁實際 | 判定 |
|---|---|---|---|
| 表下 L80／基準 L94 GDPval 截斷 | 砍 | 兩處都已刪，1844／1846 在表內 | ✅ |
| 核心功能 L132–136 | 「設計敏銳→現況」 | 現況 L52 與對照表 L68 **都沒有**「設計」二字（`grep 設計`＝0） | ❌ 事實遺失（🟡4） |
| 跟它怎麼說話 L121 | 去掉「預設 `high`」，其餘照留 | 「首字延遲就是這樣來的」一句沒了 | ❌ 小遺失（🟡5） |
| L124 hold findings／display | 措辭那半留、display 那半改指新節 | L136 照做；新節 L89 寫 `thinking.display` | ✅ |
| 歷史細節 L184 | 去「並設為 API 預設 Sonnet」 | L198 已去 | ✅，但這是一筆事實改寫，引用方沒回掃完（🔴3） |
| 相關議題 L140–150 | 改鉤子、補 haiku-5-5 | L147–156 照做 | ✅ |

N 裁決核對：N1 ✅（L96，Sonnet 5 模型頁「Good to know」確有 sampling 400）。N2 ❌（🔴1）。N3 ✅（model-comparison 六處，L151–152 移出表，L158 指新節錨點）。N4 ✅。N5 ✅（Sonnet 5 模型頁 Model ID 確為 `claude-sonnet-5`）。N6 ✅（兩處都叫「補充」）。N7 ✅（L113 寫 2.1，opus-5-5 沒動）。

## 二、新頁事實對官方原文（不得超出、不得虛報）

逐條對過 verified，verified 沒涵蓋的部分由評審另抓原文核對：

- **verified 有、對得上**：預設 Opus 5.5／v2.1.280 前 Pro 與 Team Standard 預設 Sonnet 5／`sonnet` 別名分平台／v2.1.284+／effort 兩個預設／5＋1 項／fallback／512 快取／牌價與快取寫入／知識截止／退役日／30%+ 與 30%／tokenizer。✅
- **verified 沒有，評審抓原文後確認成立**：L84（`between_tools` 只收 low／medium／high，xhigh／max 用 adaptive）、L85（`strict: true`／structured outputs）、L86（2026-08-31 起建立的帳號）、L87（`computer_toolset_20260801`、Bedrock 仍收舊版）、L88（四個 advisor）、L89（`display: "omitted"` 預設）、L94（其他類別不重試）、L74「Claude app 也是 medium」（發布文：“In Claude Code and our apps, the default effort is set to Medium”）、L117 前半「TB 4.0 的 Opus 5.5 跑 xhigh」（發布文註腳 ¹）、L63–66 Sonnet 5 一欄（Sonnet 5 模型頁：1M／128K／Batch 300K、Jan 2026、退役不早於 2027-06-30、快取讀取 $0.20、各平台上架）。✅ 但一手紀錄只存在設計者摘要和這份評審裡（🟡7）。
- **ledger 寫錯了，頁面寫對**：ledger (3) 和提案寫的是「可關」，但 model-config 原文是：`switchModelsOnFlag: false` 等於「Ask each time」，**每次問你，不是關掉**。新頁 L93、L184、L193 都寫「改成每次問／詢問」，這是對的。實作時不准改回「可關」。
- **超出原文**：L108 和 L116 對 FrontierCode 只取 max 一個數，因此「差最多 8.2」是挑掉 xhigh 2.3 之後的結果，屬虛報（🔴1）。

## 三、四視角條目

### 🔴1 FrontierCode 沒照 N2 寫兩個數，L116 的結論因此不成立（機器／冷讀者）

N2 判的是「表格寫兩數並註明 max 反低於 xhigh」。新頁 L108 只寫 46.2%，L116 寫「差最多的是 FrontierCode（8.2 個百分點）」，L117 寫「FrontierCode 的 Sonnet 5.5 跑 max effort」。發布文註腳 ²：“Sonnet 5.5 scores lower at Max effort than at Xhigh”。抽取出來的列是 `46.2%Max² | 42.4% | 54.4% | 49.3% | 52.1%Xhigh`，四欄裡有五個值，52.1 對應 Sonnet 5.5 xhigh 是從註腳推出來的（verified 第五節也這樣寫）。照 xhigh 算，百分比制 7 項的落後幅度是 1.7–3.2，Sonnet 5.5 不會在 FrontierCode 上「差最多」。另外 AA-Briefcase 差 11（分數制），用「個百分點」比較會混在一起。修法（`out/` 檔三處，貼上即可）：

L108：
```
| FrontierCode 1.1（Main） | 46.2%（max）／52.1%（xhigh） | 42.4% | 54.4% |
```
L116：
```
- **相對 Opus 5.5**：Terminal-Bench 4.0 高 4.2 個百分點，其餘 7 項落後——百分比項差 1.7–3.2 個百分點（FrontierCode 取 xhigh 差 2.3、取 max 差 8.2），分數制的 GDPval-AA 差 2、AA-Briefcase 差 11；Opus 5.5 那一側的完整表見 [[entities/opus-5-5#這些數字是誰量的]]。
```
L117：
```
- **effort 設定不一**：官方註腳寫明 Terminal-Bench 4.0 的 Opus 5.5 是 xhigh effort 的成績；FrontierCode 的 Sonnet 5.5 列了 max 與 xhigh 兩個數，max 反而較低（註腳稱 max 下較常自跑 code review，導致逾時或多改；52.1% 對應 xhigh 依註腳推得）。
```
改完重跑 `check_cell_limits.py`（L108 那一格 24 字，不會碰到上限）。

### 🔴2 feature-radar 回掃只做到 L37，L519 和 L523 還在講舊說法（治理）

daily-contracts「誰可以動這個標記」規定主編查實之後要「拿探針字串回掃全庫，把仍在說待查證的引用方一併上修」。feature-radar L523「Claude Code CLI 本身的預設 Sonnet 是否同步換為 5.5……見 [[entities/sonnet-5]] 追蹤」就是待查證說法的引用方；L519「已是預設，無需主動嘗試」與官方直接矛盾（預設是 Opus 5.5）。ledger (10) 和 handoff 第 3 筆只點到 L37。這三處都由主編直接改（radar 的家是主編，不開轉知帳）：

L37 第二格：
```
Claude Code 的 `sonnet` 別名改指 Claude Sonnet 5.5；各方案預設仍是 Opus 5.5（官方 model-config，2026-11-05 查證，見 [[entities/sonnet-5-5]]）
```
L519：
```
**現在要試嗎：** 不是預設（Claude Code 各方案預設 Opus 5.5）；要用就 `/model sonnet`（需 v2.1.284+），從 Sonnet 5 換來先看 [[entities/sonnet-5-5#從 Sonnet 5 換過來會壞什麼]]。
```
L523：
```
**注意事項：** Claude Code 各方案預設是 Opus 5.5，Sonnet 5 已列 Legacy（官方 [model-config](https://code.claude.com/docs/en/model-config)，2026-11-05 查證），細節見 [[entities/sonnet-5-5]]。
```
L14、L508（h3）、L835 的「成為 API 預設 Sonnet 模型」照 🔴3 統一改成「`sonnet` 別名」說法。h3 改名前已查過 `feature-radar#Claude Sonnet 5.5 成為 API 預設 Sonnet 模型` 的入邊：0。改完 L37 後跑 `check_cell_limits.py`。

### 🔴3 「API 預設 Sonnet」本頁刪了，同維護者的鄰居和 index 還在講（明天的維護者／冷讀者）

本頁照 verified #1 把「並設為 API 預設 Sonnet」刪掉（去向表 L184）。shared-when「事實更正必回掃」要求把仍在講舊說法的地方一起改。冷讀者 Q2 只拿到「半」，正是因為四頁說法打架。sonnet-5 是同一位維護者，改的是事實句和互指句，在本波範圍內；index 由主編同一個 commit 一起改。要改的地方（歷史段 sonnet-5 L120、model-comparison L230 屬於過去的紀錄，不動）：

- sonnet-5 L37 → `> [[entities/sonnet-5-5|Sonnet 5.5]] 發布，Claude Code 的 `sonnet` 別名改指它；本頁官方已列 Legacy（2026-10-10 查證，見下方「現況」）。`
- sonnet-5 L43 句首 → `**2026-09-28 最新**：Anthropic 發布 [[entities/sonnet-5-5|Claude Sonnet 5.5]]，Claude Code v2.1.284 起可選（`sonnet` 別名改指它）；`（分號之後原文不動）
- sonnet-5 L105 → `- [[entities/sonnet-5-5]] — 2026-09-28 發布的新一代，現行 Sonnet；Claude Code `sonnet` 別名指向它`
- index L48 摘要 → `Claude Sonnet 5.5：2026-09-28 發布的現行 Sonnet（Claude Code `sonnet` 別名，非預設），Terminal-Bench 4.0 由 10.3%→70.6%，牌價維持 $2/$10`（後半照原文）
- 🟡 跨維護者，開轉知：`python scripts/pending_handoffs.py open --from 模型 --to 功能 --page entities/claude-code-releases --note "第 28 波 sonnet-5-5 官方查證（2026-11-05，https://code.claude.com/docs/en/model-config）：L119、L223「Sonnet 5.5 成 API 預設 Sonnet／預設模型」→ Claude Code 各方案預設是 Opus 5.5，v2.1.284 是讓 \`sonnet\` 別名改指 Sonnet 5.5；請改成「\`sonnet\` 別名改指 Sonnet 5.5（需 v2.1.284+）」"`（先加 `--dry-run` 驗負責人）
- 🟡 overview L33、L120：主編下次 `/weekly` 改，或同一批一起改成「`sonnet` 別名」說法。

### 🟡4 「對設計細節敏銳」遺失（去向表抽驗）

去向表說核心功能的「設計敏銳→現況」，實際上被丟掉了。發布文原句是 “It's also got a sharp eye for design.”。修法：新頁 L52 的「修 bug、產出文件／簡報／試算表」後面接 `，官方另稱它對設計很有眼光`。

### 🟡5 「首字延遲」那半句遺失

L133 照去向表應該「其餘照留」。修法：L133「連招呼也算，」後面補 `首字延遲就是這樣來的；`。

### 🟡6 callout 的 `/model sonnet` 對雲平台讀者是錯的（冷讀者；設計者 §9 最不確定的那件事）

model-config 的別名表：Bedrock、Google Cloud、Foundry 上 `sonnet` 指 Sonnet 4.5，Claude Platform on AWS 指 4.6。L43 修法：
```
> - **要用就選**：`/model sonnet`（需 v2.1.284+；Bedrock 等雲平台要寫完整 ID），effort 預設 medium。
```
這一點要在原考題複驗 Q2 加看：有沒有人撞到。

### 🟡7 新頁有 11 處事實的一手紀錄不在 verified（治理）

第二節列的那幾處，現在只有設計者摘要和本評審可查。修法：主編在 `sonnet-5-5-2026-11-05-verified.md` 末尾 append：
```
## 六、補查（評審，2026-11-05 重抓原文）

- What's new：`between_tools` 只收 low／medium／high（xhigh／max 用 adaptive）；強制工具改 `strict: true` 或 structured outputs；thinking block 綁定的 400 只限 2026-08-31 00:00 UTC 起建立的帳號（且未設 `prefix_mismatch_behavior`）；`computer_toolset_20260801` 取代，Bedrock 仍收 `computer_20251124`；`display` 預設 `omitted`；server-side fallback 不重試 bio／reasoning_extraction／general_harms。
- 發布文：註腳 ¹「Terminal-Bench 4.0 results are reported for Claude Opus 5.5 at Xhigh effort」；“In Claude Code and our apps, the default effort is set to Medium”；“sharp eye for design”。
- model-config：`switchModelsOnFlag: false`＝Ask each time，不是關閉 fallback；v2.1.280 前 Sonnet 5 只是 Pro 與 Team Standard 的預設，Max／Ultra／Team Premium／Enterprise／API 自 v2.1.219 起預設 Opus 5、更早是 Opus 4.8。
- Sonnet 5 模型頁：`claude-sonnet-5`、1M／128K／Batch beta 300K、Jan 2026、退役不早於 2027-06-30、快取讀取 $0.20、六平台上架、sampling 參數回 400。
```

### 🟡8 sonnet-5 L57、L95「v2.1.197 起曾是 Claude Code 預設」範圍太寬（同維護者事實句）

model-config：v2.1.280 前 Sonnet 5 只是 Pro 與 Team Standard 的預設；Max 等方案在 v2.1.219 前是 Opus 4.8、之後是 Opus 5。修法：
- L57 → `**Claude Code 預設模型**：v2.1.197 起曾是 Pro 與 Team Standard 的 Claude Code 預設（Max 等方案當時預設 Opus），v2.1.280 起已不是，現在的預設見上方「現況」。`
- L95（新行號 L92）→ `- **Claude Code 預設**：v2.1.197 起曾為 Pro 與 Team Standard 的預設，v2.1.280 起已不是`

### 不列為條目（已核、無須改動）

轉知 `--to` 類別：pricing、pricing-history 屬商業（commercial/daily.md L19、L21），handoff 第 1、2 筆正確；第 3 筆（feature-radar）由 🔴2 主編直接改取代，不開帳。`--reason` 字串正確。`rules_patch.py` 條文與新頁一致（四欄、8 列上限，FrontierCode 一格寫兩個數不違反）。opus-5-5、haiku-5-5、model-comparison 的改動都只限事實句和互指句；haiku 刪掉的 L67、L167 是錯誤事實，不屬於「改歷史」。

## 四、照順序執行（實作單）

1. 確認 HEAD 的五頁（sonnet-5-5、sonnet-5、opus-5-5、model-comparison、haiku-5-5）在 `e66cc9d` 之後沒被 ingest 動過（`git diff e66cc9d -- <五頁>` 為空）。不為空就續用設計者重產，不准手改。
2. 在 `out/wiki/entities/sonnet-5-5.md` 套 🔴1（L108、L116、L117）、🟡4（L52）、🟡5（L133）、🟡6（L43）。
3. 跑 `python apply.py`（全套，含 N3、N4）與 `python rules_patch.py /home/user/claude-news`，再把 `out/` 的 sonnet-5-5 複製進 repo。
4. sonnet-5 加套 🔴3（L37、L43、L105）與 🟡8（L57、L95）。
5. 主編直接改 feature-radar：L37、L519、L523（🔴2），L14、L508、L835 統一成「`sonnet` 別名」說法；改 index L48（🔴3）；overview L33、L120 同批改或記下週。
6. 主編在 verified 末尾 append 第六節（🟡7）。
7. `python scripts/gen_wiki_frontmatter.py`；確認本頁 `pending_count: 0`。
8. `python scripts/check_pending_markers.py --rebuild-count --reason "第 28 波 sonnet-5-5：⟨Q-01⟩ 與 sonnet-5 同題 🔎 兩筆經官方 Claude Code model-config 查實結案（−2）"`，確認 removed 只有這兩筆、added 0，計數 221。
9. 跑閘：`check_cell_limits.py`、`check_reader_language.py`、`check_pending_markers.py`、`check_rules.py`、`build_web.py`（斷鏈 23、錨點 WARN 0）、`run_tests.py`（在 repo 內跑，devpractice 兩筆應轉綠）。
10. 開轉知：handoff 第 1、2 筆（商業 ×2）與 🔴3 的功能 ×1，各先跑一次 `--dry-run`；handoff 第 3 筆不開。
11. `wiki/log.md` append 本波條目（⟨Q-01⟩ 結案、−2、回掃清單）；ledger 記：FrontierCode 照 N2 補兩數、fallback 是「每次問」不是「可關」（更正 ledger (3) 用字）、Foundry 寫法交複驗 Q2。
12. 單一 commit（範圍：五頁＋feature-radar＋index（＋overview）＋models/pages.md＋models/daily.md＋data/pending-marker-count.json＋handoff 帳＋log＋verified＋ledger），然後送評審複核。
