# Wiki Lint B 段：5a–5n 逐步判準與回報格式

`.claude/skills/wiki-lint-sweeps/SKILL.md` 的判準單一來源。**執行某步之前逐字讀本檔對應節**；每節末的回報格式原樣填入步驟 8 的 lint 紀錄（模板見 `.claude/skills/wiki-lint/references/log-format.md`）。

立法起因見沿革檔 `docs/rules-changelog/wiki-lint.md`。

---

## 雲端 egress 探測（5b／5c／5m／5n 共用）

雲端執行這三步前先跑對應組的探測，依印出的摘要行決定做或不做。**不得在未探測的情況下直接跳過**——網路白名單是使用者可改的環境設定（Trusted → Custom，見 `docs/cloud-runbooks/_shared.md`「egress 限制」），寫死跳過的條文在環境改好之後也不會自己好起來。

| 步驟 | 探測指令 | 印這行 → 照該節本機步驟執行 | `PARTIAL`／`BLOCKED` → 跳過並寫這條待辦 |
|---|---|---|---|
| 5b | `python scripts/cloud_egress_check.py --group leaderboard` | `EGRESS: leaderboard OK` | 「跨家榜單週更因雲端 egress 未開（leaderboard）跳過，留待本機 `/weekly`」 |
| 5c | `python scripts/cloud_egress_check.py --group official` | `EGRESS: official OK` | 「逾期待查證清算因雲端 egress 未開（official）跳過，留待本機 `/weekly`」；**整步不查證、不改動任何頁面，Lane A 不例外** |
| 5m | `python scripts/cloud_egress_check.py --group github` | `EGRESS: github OK` | 「code-quality-decline issue 狀態複查因雲端 egress 未開（github）跳過，留待本機 `/weekly`」 |
| 5n | `python scripts/cloud_egress_check.py --group github` | `EGRESS: github OK` | 「official-community-gap「官方補了沒」表對官方一手因雲端 egress 未開（github）跳過，留待本機 `/weekly`」 |

待辦一律進 log 的待使用者確認區；該步回報那一行寫「雲端 egress 未開，跳過」。

**5h 不受此限、不需探測**：催化劑那一半純查本庫日報；股價那一半用 **WebSearch**，由 Anthropic 端執行、不經沙盒 egress（`python scripts/cloud_egress_check.py --group market` 的 market 組刻意為空，恆印 `EGRESS: market OK`）。唯一例外是該環境根本沒有 WebSearch 工具可用——此時才寫待辦「投資訊號股價結算因該環境無 WebSearch 跳過，留待本機 `/weekly` 承接」並列入待使用者確認區；日後若本步改用 WebFetch 直抓行情站，須同步把那些網域填進 market 組並改回探測式。

---

## 5a. feature-radar 熱度降溫（主編親做）

`.claude/reporter-rules/features/pages.md`「熱度降溫：它不是棘輪」定的 −1 規則，本步是它的執行點。

1. 取 `wiki/feature-radar.md` 全覽表中**熱度 ≥ 🔥🔥** 的條目（🔥 已是下限，不必檢查）
2. 對每個條目查近 4 週日報有無提及——**用共用腳本查，不要臨場手刻 grep**：`python scripts/news_mentions.py --since 4w "英文名" "中文譯名"`。它強制 ≥2 別名、拒絕過寬詞、且輸出命中原文行——三者分別擋掉漏抓、假命中、與「只看次數就下結論」。理由與實例見該腳本檔頭。
3. 零命中 → 熱度 −1 格，**同步對應 `entities/` 頁的「熱度與試用價值」表**——單邊下修是矛盾的來源
4. **不降的例外**：狀態為「⏰ 倒數中」，或本輪熱度／試用價值有其他變動者
5. **⏳ 逾期處置（同一趟做完）**：全覽表中標 ⏳ 且發布日距今 > 90 天者，依 `.claude/reporter-rules/features/pages.md`「⏳ 觀望是有期限的判斷」三選一處置，不得留原狀

**回報格式：**
```
熱度降溫：檢查 N 條，降 M 條（列出 條目名 舊→新），同步 entities 頁 M 處；⏳ 逾期：K 條，處置（升 a／降 b／加註 c）
```

---

## 5b. 跨家任務榜單週更（主編派工）

`wiki/topics/model-task-leaderboard.md`（任務 × 跨家模型領先者週快照）由本步驟維護——它吃外部榜單網站而非新聞條目，類別路由接不到，此處為其唯一觸發邊；記者無 web 工具，由主編派工執行。

**雲端執行時先探測**，見本檔「雲端 egress 探測」表 5b 列。

1. 派一個 `general-purpose` agent 帶 `model: "haiku"`（低成本抓取任務），prompt 要求：逐一查該頁「涵蓋榜單」清單中的所有榜（頁面表格內含 URL），回報各榜前 3–5 名、分數/Elo/占比、資料日期、來源方式（直接抓取 or 二手搜尋＋日期）；JS 渲染抓不到時退用 WebSearch 近期報導並標注二手；查不到明說，不可編造模型名或分數
2. 主編收報後更新該頁 `## 本週快照` 表：每列覆寫為最新結果（覆寫式快照，歷史不留存於此頁）。**表格形狀固定 4 欄**（任務｜本週前三名｜資料日期｜榜單）——前三名用「A > B > C」短語呈現；**不逐榜記分數與取得方式**（讀者要精確數字點榜單連結），僅異常狀況（榜停更、量測過期、來源歧異）寫入「本週註記（僅列異常）」區並汰除已解除的舊註記；更新每列「資料日期」與頁面「最後更新」；連續 2 週抓不到的榜在該列標「（連續 N 週無法取得，考慮汰換）」並回報使用者；榜頁未載資料日期時，該列資料日期寫「榜頁未標日期（本次 MM-DD 抓取）」，不寫「未載」兩字了事。
3. 此為非新聞性更新，不動「最後新聞更新」；快照數字**不回寫** `model-comparison.md` 或各模型頁（快照只住這一頁，避免過期數字擴散）
4. 頁尾「評比方式索引」為**靜態參考層**（按計分機制分組的巢狀條列，非表格），每週更新不覆寫；僅在新增榜單列時同步在對應機制組補一條，**固定四欄位：題目（含具體題型範例）→ 規模 → 算分 → 盲點**，機制層級描述、不放具體分數，未查證的規模數字寫「未公開」不硬補

**回報格式：**
```
跨家榜單週更（5b）：已更新 N 榜／M 榜無法取得（列出）／雲端 egress 未開，跳過
```

---

## 5c. 逾期待查證清算（主編親查）

記者 agent 無 web 工具，標下的「待查證」在系統內沒有任何人有能力解。本步驟是唯一的消化端。

**⚠️ 雲端執行時先探測**，見本檔「雲端 egress 探測」表 5c 列（本步需存取 `support.claude.com`／`docs.claude.com`／`anthropic.com`）。

**本機執行步驟：**

1. **盤點＋排序**：先跑**完整報告**再跑佇列——

   ```
   python scripts/check_pending_markers.py          # 完整報告：含 WARN
   python scripts/check_pending_markers.py --queue  # 逾期佇列
   ```

 完整報告的 **WARN 逐條處置，不得略過**：語意反轉殘留（同行出現「解除／結案」與 ✅）、探針偵測力退化等。屬本步可解者當場改；屬記者頁面者轉知對應類別記者。WARN 條數與處置寫進本步回報。

 佇列部分：`--queue` 輸出**兩條分流**與**產消對帳**（）：

   - **Lane A（本輪額度 10）**：記者已標 `訊`，代表日報裡已有後續證據——**多數可免 web**，但探針是機械比對、會假命中，須逐筆確認該日條目是否真指此事實；確認不了就退回 Lane B（見步驟 2）。**探測判為未開時整個 5c 跳過**，本區不例外
 - **Lane B（本輪額度 8）**：需 WebFetch 官方一手來源查證，受 egress 與成本限制

   > 為何分流：一個額度混用兩種成本結構的工作，必然被便宜那種佔滿（教訓見沿革檔 2026-08-29 A）。

 **📊 產消對帳那一行必須讀，並抄進本步回報**：它印出「近 7 天新增 N 筆｜每週產能 18 筆（A 10＋B 8）｜本輪實際可消 M 筆｜淨增/淨減」，並標**（概估）**——額度為上限、7 天內建立又已結案者不計入分子。另有「📈 趨勢」與「⏳ 排空預估」兩行，一併抄進回報。**只看「總逾期數」看不出流量。** 出現「⚠️ 產出快過消費」時，在回報中提出處置建議（提高額度／記者端提高標記門檻），不得只抄數字。**`data/pending_queue_history.csv` 每輪會被 append 一列（同日 upsert），須併入步驟 10 的單一 push**——不 push 的話序列會在雲端與本機之間斷掉，趨勢行就失去意義。

 **輸出末尾的「⚠️ 舊語法盲區」不是裝飾**——那是佇列撈不到的存量與其頁面分佈；「總逾期數 0」只代表新語法那半乾淨了。把盲區筆數與前三頁抄進本步回報，並在 3g 派工時優先指定那幾頁回填

2. **查證**（兩條 Lane 走不同路徑）：

   - **Lane B**：對每筆用 WebFetch／WebSearch 查**官方一手來源**（優先序：`support.claude.com` 說明中心 → `docs.claude.com` → `anthropic.com`／`claude.com` → 官方社群帳號 → 具名媒體）
   - **Lane A**：先開該筆 `訊` 日期的日報，**逐筆確認該條目是否真指這件事**——`訊` 由記者依探針字串機械比對加上，會假命中。確認得了 → 走步驟 3 **第四列**；確認不了 → **退回 Lane B**，不可硬結
   - 兩條都需要外部網域者以 Lane B 為準；**探測判為未開時整個 5c 跳過**，Lane A 不例外（它仍須寫回，而寫回品質取決於同一輪的判斷一致性）

3. **寫回**（四選一，不得留原狀）：

   | 查證結果 | 寫法 |
   |---------|------|
   | 查到官方說法 | 改寫為事實，附**來源連結＋查證日**，移除整個懸置標記 |
   | 官方確實未公開 | 狀態符號改 `🔎`、類別詞改 `查無官方`，並更新 `複` 為下次複查日——**「查過了確認沒有」與「沒人查」必須長得不一樣** |
   | 議題已失效（產品下線、政策被取代） | 移除該筆，沿革留在時序區 |
 | **日報有後續、但未查官方**（Lane A 專用） | 依日報更新內文並註明來源日報日期，**狀態符號維持 `❓`**、更新 `複` 為下次複查日，標記**保留** |

 > **第四列為何不可用 `🔎`**：`🔎 查無官方` 的定義是「**已查官方一手來源、確認未載**」；Lane A 沒查官方，用它等於宣稱做過沒做的事。（教訓見沿革檔 2026-08-29 B）

   標記語法見 `.claude/reporter-rules/page-templates.md`「懸置標記語法」節。**你是唯一有權移除標記或改狀態符號的角色**（記者只能加 `訊`）。

4. **金額／數字分級**：官方文件未載而僅媒體有數字者，寫「媒體稱（媒體名）」，不得升格為官方數字

5. **結案回掃（強制，每筆查實後立刻做，不得留到最後）**：語意與 `.claude/reporter-rules/shared.md`「事實更正必回掃」同一套，**先入邊、後 grep**——

   ```
   python scripts/wiki_graph.py explain <該筆所在頁> --section "該筆所在的節標題"
   ```

   入邊清單（錨點邊＋整頁邊）是**必查名單**，逐一開行號確認引用方是否仍在講舊說法；接著才拿該筆標記 metadata 的**探針字串**（`查 A、B` 欄）grep 全庫（`wiki/`，排除 append-only 的 `log.md`）補漏——探針抓得到沒用 wikilink 的散文提及，入邊抓得到探針字串沒涵蓋的措辭，兩者互補、都要跑。命中的其他頁面若仍以「待查證／推算值／尚未確認／待官方公布」等措辭描述同一件事，**一併上修為同一結論**，附同一來源連結與查證日。回報寫 `回掃：入邊 N 處（改 M）＋探針 X 命中 K 處（改 J）`。

   > **為什麼結案一定要回掃：同步是雙向的，但機制只有單向。**（教訓見沿革檔 2026-08-20 A）

**回報格式：**
```
逾期待查證清算（5c）：盤點 N 筆，本輪處理 M 筆（查實 A／確認官方未載 B／失效移除 C），結案回掃上修 D 頁，剩餘 N-M 筆／雲端 egress 未開，跳過
```

---

## 5d. 歸因忠實度抽查（主編親做）

防的是「已確認但被改壞的事實」——claim 被後續改寫走樣、歸因還在，造成虛假的有源感。抽樣控成本，不全查：

1. 從 `data/source_attribution.jsonl` 隨機抽 **5 筆**近 60 天的歸因（`python -c "import json,random;rows=[json.loads(l) for l in open('data/source_attribution.jsonl',encoding='utf-8') if l.strip()];random.shuffle(rows);[print(r['date'],r['page'],r['item_title'][:60]) for r in rows[:5]]"` 後自行過濾日期）
2. 每筆：開該歸因日期的日報（`news/` 下同名日期檔）找到該條目的摘要 → Grep 該 wiki 頁中對應此事實的段落 → 比對**頁面現文是否仍忠於來源**（數字、日期、確定性程度、誰說的）
3. **步驟 2 找不到日報條目時先別判 ❓**：記者的派工涵蓋「當日抓到但未刊出」的條目，這類事實的歸因日期對得上、日報裡卻查無——**這是程序假設與實作不一致，不是頁面有錯**（2026-09-12 於 07-26 issue #48407 實際踩到）。此時改開 `src/gathered_archive/<該日>.json` 比對；該日已過 14 天保留窗則記「來源為未刊出的抓取條目，原料已過保留窗」，兩者都**不計入 ❓**
4. 四種結果：✅ 相符不動；⚠️ 措辭漂移（把「媒體稱」寫成事實、把分歧寫成共識、數字走樣）→ 依日報原文修正該段；📦 來源為未刊出的抓取條目（見上）→ 不算錯，單獨記數；❓ 頁面已無此事實對應段落（被合併或清理）→ 不算錯，記一筆即可
5. **連續 3 週 B=0 可降頻為隔週抽**

**回報格式：**
```
歸因抽查（5d）：抽 5 筆，相符 A／修正漂移 B（頁名 list）／未刊出抓取條目 D／無對應 C
```

---

## 5e. pricing「通路與乘數」複查（主編親查）

`wiki/entities/pricing.md` 的 `## 通路與乘數` 吃的是**官方計價文件**（`platform.claude.com` 與各雲端平台），不是日報——記者無 web 工具，寫成記者責任會製造永遠空著的區塊。依 `.claude/reporter-rules/commercial/weekly.md` 執行：

1. 該區塊「資料截至 YYYY-MM-DD」距今 > 30 天 → WebFetch 官方定價頁與平台可用性頁複查；一致則只更新查證日
2. 本週有新模型世代發布 → 確認長脈絡是否仍不加價、tokenizer 是否再換代；後者走 `data/pending-handoffs.jsonl` 轉知模型記者（`.claude/reporter-rules/models/pages.md` I 條）
3. 商業記者本週回報「⚠️ 需主編查證官方計價文件」→ 逐筆查證後寫入，標來源連結與查證日
4. 本區塊為非新聞性維護：只更新 pricing 的「最後更新」，**不動「最後新聞更新」**

---

## 5f. devpractice 週彙整（主編派工）

六記者收報**之後**（功能記者的 guide 清冊週更、社群記者的 tools 策展已完成，寫入不會互踩），派 devpractice 記者做週彙整。以 `subagent_type: "general-purpose"` + `model: "sonnet"` 派出，prompt 首段：

```
你是 CLAUDE_NEWS wiki 的「開發實務（devpractice）」記者。開工前先 Read `.claude/agents/wiki-reporter-devpractice.md`——那是你的角色定義，逐條照做後執行 **weekly 彙整**（三件事：本週 coding 亮點、guide 社群面待補逐段深查、coding 跨頁對帳）。今日日期：[YYYY-MM-DD]。你不可再呼叫 Agent tool 委派任何工作。
```

收報後：「⚠️ 需主編轉知」逐筆登 `data/pending-handoffs.jsonl`；回報摘要記入 Step 8 log 一行 `devpractice 週彙整：…`。

---

## 5g. 高引用但停滯（signal 消費端，主編親做）

`scripts/gen_wiki_frontmatter.py` 每次執行都印一行 `signal 分布：健康 N、休眠 N、孤島 N、⚠️ 高引用但停滯 N`，並把 `signal` 寫進每頁 frontmatter。本步是它的消費端。

```
python scripts/gen_wiki_frontmatter.py --list-signal "⚠️ 高引用但停滯"
```

判準的家在該腳本（入鏈 ≥ 15 且超過 21 天無新聞；hub 頁看子樹聚合），**列表刻意不另寫一支**，否則會有第二份門檻。指令唯讀、不寫入 frontmatter。

- 這一格是四象限中**最該看的一格**：很多頁指向它，讀者被導過去卻看到舊東西。頁面沒壞、鏈結沒斷，是靜默失效——3c 抓不到它（3c 只看 topics 的 `ongoing` 狀態與 14 天，不看入鏈，且 entities 頁根本不在其射程）；5a 也抓不到（那管的是 feature-radar 熱度，不是頁面新鮮度）
- 每頁**二選一，不得留原狀**：
  - **確實沒新聞可寫** → 派該頁所屬類別的記者確認（跨類別依 index 領域欄派工）：屬 topics 且議題已停 → 依 3c 改 `monitoring`／`resolved` 並補「目前結論」；屬 entities → 在頁面現況段明寫「自 YYYY-MM-DD 起無新動態」，讓讀者看得出停滯是事實而非漏更新
  - **它是引用方該改連到更新的頁** → 高入鏈往往是歷史慣性（早期頁被大量引用，主題已轉移到新頁）。跑 `python scripts/wiki_graph.py explain <該頁>` 看入邊來自哪些頁與哪一節，逐一判斷該引用是否應改指更新的頁；改連結後入鏈自然下降，訊號解除
- **連續 2 輪同一頁仍在清單且處置皆為 c** → 回報使用者：門檻（21 天／入鏈 15）可能不適用於該頁型態，評估調 `gen_wiki_frontmatter.py` 的 `STALE_DAYS`／`INBOUND_HIGH`

**回報格式：**（`c` 只在該頁確實仍是該主題的正確落點、且停滯已在頁面上寫明時才可用，並附一句理由）
```
高引用停滯：N 頁（處置：派記者確認 a／改引用方連結 b／確認無誤留原狀 c）
```

---

## 5h. 投資訊號回顧環（主編親查）

`wiki/topics/market-signals.md` 的判讀是**預測性宣稱**，本步是它唯一的結算端：對 `## 回顧結算` 表中「兩週後」為 ⏳ 且判讀日距今 ≥ 14 天的列，結兩件事——**催化劑在結算日前出現了沒**（查本庫日報，`scripts/news_mentions.py`，每列都做）與**上市標的的兩週粗方向**（↑／↓／～，只做帶代號的列），回填「兩週後」與「對錯」；接著把本週判讀沉澱進週更教材頁 `wiki/topics/market-lessons.md`（消息線表、課程表含「押對了嗎」、IPO 背景段順檢）。記者無 web 工具，查不了股價，這是本步不派工的唯一理由。

**⚠️ 雲端兩半都做、不需探測**，理由見本檔「雲端 egress 探測」節末「5h 不受此限」段。

執行細節（兩種結算的回填格式、不可驗證的寫法、不得回頭改寫「當時判斷」與「催化劑」、連續 4 週全錯的處置）見 `.claude/reporter-rules/market/weekly.md`。

**回報格式：**
```
投資訊號回顧（5h）：結算 N 列（✅ a／❌ b／～ c／不可驗證 d），剩餘 ⏳ M 列／股價半邊該環境無 WebSearch，跳過
```

---

## 5i. 安全政策兩頁結論表退場複查（主編親做）

`wiki/topics/ai-agent-safety.md` 的攻擊面結論表（現名 `## 現在還擋不住的攻擊`）（上限 11 列）與 `## 提示注入已不是單點漏洞，是產業級攻擊面`（上限 8 列）的退場條文，本步即其週更觸發邊，複查規則見 `.claude/reporter-rules/safety-policy/pages.md`「ai-agent-safety 更新規則」第 2、3 條。`wiki/topics/anthropic-government-policy.md` 的 `## 現在有哪幾條線在動`（上限 8 列）同病同治，複查規則見同一規則檔「anthropic-government-policy 更新規則」第 2、3、4 條。

逐列檢查該表的「最後動態」是否距今逾 90 天且本輪無新回報，符合即依規則移除並在事件記錄補註記；表未滿載時挑候選補位並移除其註記。`## 提示注入…攻擊面` 表滿 8 列時汰除最舊者，並確認導言／收斂點／「仍未有答案的」三處則數與表列數一致。政策頁逐列檢查『線』欄括號內的最後動態日期是否逾 90 天且本輪無新事實，符合即依規則移除並在 `## 時序` 對應條目補註記；表未滿載時從 `## 時序` 挑符合三條判準、最後動態最新者補位。另比對 `## 政府動作對你的產品做了什麼` 的項數是否等於上表標『會』的列數，不等即依規則增刪。

**回報格式：**
```
安全兩頁結論表退場（5i）：safety（複查 N 列，移除 a／補位 b／不動 c）／gov-policy（複查 N 列，移除 a／補位 b／不動 c；產品節 M 項對 K 列）
```

---

## 5j. 商業健康度四表退場複查（主編親做）

`wiki/topics/anthropic-business.md` 的 `## 現在的數字`（上限 10 列）、商業風險表（現名 `## 還沒過去的風險`）（上限 6 列）、`## 哪個合作會改到你用的 Claude`（上限 6 列）與 `## 上面提到的人是誰`（上限 8 人）的退場與補位條文，本步即其週更觸發邊，複查規則見 `.claude/reporter-rules/commercial/pages.md`「anthropic-business 更新規則」第 1、4、5、6 條。

逐列檢查：指標表看「資料日期」是否逾 180 天且無人發布新值，符合即移出並在細節區留結論；風險表看「風險」欄括號內的最後動態是否逾 90 天且本輪無新事實（**訴訟不適用 90 天**），符合即移除並在細節區補註記，表未滿載時依判準從細節區補位並移除其註記；合作表看該差異是否已消失或逾 180 天無新事實；人物表看每人所連的那一列或那一則是否仍在頁上。另核合作表上的「資料截至」日與 `entities/pricing`「通路與乘數」是否同批（見 5e）。

**回報格式：**
```
商業健康度四表健檢（5j）：指標 N 列（移除 a／補位 b）／風險 M 列（移除 c／補位 d）／合作 K 列／人物 P 人／通路快照資料截至 YYYY-MM-DD
```

---

## 5k. 社群三張結論表退場複查（主編派社群記者）

`wiki/topics/community-tech-patterns.md` 的 `## 模式概覽`（上限 21 列）、`### 誰負責拆分`（五列固定）與 `### 缺口追蹤`（上限 8 列）的退場、補位、留表優先序條文，本步即其週更觸發邊，複查規則見 `.claude/reporter-rules/community/weekly.md`「community-tech-patterns 模式概覽週更」。

派社群記者執行該節三步：重算「最後動態」（兩段式撈法覆寫日期欄與全頁式錨點）、跑退場與補位（逾 60 天或算不出日期者移出、剛跨線當週處理、表未滿載時從表下補位）、跑合併（代表技巧重疊過半者合併）；同批補填主線 tag（每週 20 則，從最新往回補，累計進度寫進回報）。上限滿載時的讓位交回主編裁決，不由記者自行決定。

`wiki/topics/community-tech-discussions.md` 的 `## 現在吵到哪`（上限 10 列）與 `## 最近在討論什麼`（上限 50 列）同批處理：重算每一列的最後動態與最後一則證據日期、依狀態三值重判、跑退場與補位、把逾 45 天的 🌊延燒 改標 🌙靜候、把逾 90 天的 🌙靜候 移出表。條文見 `.claude/reporter-rules/community/pages.md`「community-tech-discussions 的兩張結論表」。

**回報格式：**
```
社群模式概覽退場複查（5k）：列數 N／21（✅a／⚡b／⏳c）／最後動態已重算 N 列／退場 M 列／補位 K 列／合併 J 組／主線 tag 補填 20 則（累計 N/M，M＝該輪現算的節點總數）／滿載讓位：無 ／ ⚠️ 需裁決
社群討論兩表（5k）：爭論 N/10（還在吵 a／已共識 b／僵住 c）／討論 M/50（移出 d／改標 e）／最後動態已重算 K 列
```

---

## 5l. 模型頁世代表複查（主編親做）

對 `wiki/entities/fable-5.md` 與 `wiki/entities/opus-5.md` 的結論表各跑一次（判準見 `.claude/reporter-rules/models/pages.md`「模型頁兩代對照表」與「entities/opus-5 的兩張表」）：① 兩頁 `## 你現在拿到的是什麼` 表上「資料截至」距今逾 60 天 → WebFetch 官方模型總覽頁重查七列並更新查證日；② fable-5 `## 護欄會怎麼改寫你的請求` 四類是否仍為官方公布的四類；③ opus-5 `## 這些數字是誰量的` 的官方基準是否仍為官方在引用的那幾項，社群側是否首次出現帶測試方法與數字的獨立複測（有則同批改寫導言那句承諾）；④ 兩頁 `## 熱度與試用價值` 對 feature-radar 全覽表對應世代那一列，不一致以 radar 為準覆寫。

**回報格式：**
```
模型頁世代表（5l）：fable-5 資料截至 YYYY-MM-DD（重查 N 列）／護欄四類 一致 or 變動 M 項；opus-5 資料截至 YYYY-MM-DD（重查 N 列）／官方基準 一致 or 變動 K 項／社群獨立複測 無 or 已出現；熱度表 一致 or 已覆寫
```

---

## 5m. code-quality-decline 三條線 issue 狀態複查（主編親做）

「三條線現在到哪」的「現在還在嗎」欄吃 GitHub issue 狀態，不在日報來源清單內，記者無 web 工具。逐一跑（`gh issue view` 一次只吃一個 issue；本 repo 的 remote 是 `mandy82477/claude-news`，不加 `-R` 會查到錯的 repo）：

    for n in 41930 65687 77136 83510; do gh issue view $n -R anthropics/claude-code --json number,state,updatedAt; done

與表上三列比對，不一致即改寫該格並更新表上方「資料截至」；任一列由「還在」翻「已結案」時，同批改寫 `## 摘要` 第一段並回報 index 鉤子。

**⚠️ 雲端執行時先探測**，見本檔「雲端 egress 探測」表 5m 列。

**回報格式：**
```
code-quality-decline 三條線（5m）：N 列比對／M 列已改／資料截至 YYYY-MM-DD ／雲端 egress 未開，跳過
```

---

## 5n. official-community-gap「官方補了沒」表對官方一手（主編親做）

記者無 web 工具，這一步只能主編做。逐列：

1. 表上每個 issue 號只取狀態與官方回覆，不要把整包留言倒進來（#6235 有 405 則）：
   ```
   gh issue view <號> -R anthropics/claude-code --json state,stateReason,closedAt,comments \
     -q '{state,stateReason,closedAt,official:[.comments[]|select(.authorAssociation=="COLLABORATOR" or .authorAssociation=="MEMBER")|{login:.author.login,body:.body[0:400]}]}'
   ```
2. 抓 CHANGELOG 全文再本機 grep 該列關鍵詞：`gh api repos/anthropics/claude-code/contents/CHANGELOG.md -H "Accept: application/vnd.github.raw"`。
3. 官方文件站有對應頁者一併看（code.claude.com／platform.claude.com；否定證明查 `code.claude.com/docs/llms.txt` 的文件索引）。
4. 核完更新該列「核對日」；核對日逾 30 天的列列進 lint 回報。

**⚠️ 雲端執行時先探測**，見本檔「雲端 egress 探測」表 5n 列（`--group github`，與 5m 同組），符合 registry 第 101 組 egress 契約。

**回報格式：**
```
官方補了沒表：N 列比對／M 列已改／核對日逾 30 天 K 列
```
