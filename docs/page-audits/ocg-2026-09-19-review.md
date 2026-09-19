# 第 14 波評審：topics/official-community-gap

對象：提案三件（以磁碟現行檔為準）。上游 `-verified.md` 已補「## 六、補查」（L72–86），本檔第六節逐列對過；draft 寫於該節之前，衝突處列為第二輪必改。
行號＝各該檔案原始行號。機械項全部自跑，指令與輸出見文末。
判定：**🔴 13 條、🟡 12 條**。結論：**放行進第二輪，但表的內容有實質必改**（第六節五條 🔴 全部直接改變表上狀態或列數）。

---

## 〇、代判數字重算（不採信提案宣稱）

| 提案宣稱 | 我算的 | 判定 |
|---|---|---|
| 新表 17 列（保守 14） | 表格 19 行 −表頭−分隔＝**17**；刪 3 列＝**14** | ✅（但第六節後應為 16／13，見 🔴-9） |
| 4 ❌／8 🧪／5 ✅；保守 2／7／5 | draft L58–61／L62–69／L70–74 逐行數＝4／8／5；保守＝2／7／5 | ✅（第六節後應為 3／7／6 與 1／6／6，見 🔴-9、🔴-10） |
| 兩閘 0 命中 | 自建 9 fence／82 行暫存檔：reader language **0**、cell limits **0**、最長格 110（上限 120） | ✅ |
| 懸置 188 筆、本頁 2 筆 | `check_pending_markers.py`：188（基線 140），本頁 L92＋L153 | ✅ |
| Slack 列 2026-09-22 滿 90 天 | 2026-06-24 ＋90＝**2026-09-22** | 日期對、**結論錯**（🔴-1） |
| `check_rules.py`／`check_hierarchy.py` | 均 ✅（改動前基線） | ✅ |

---

## 一、明天的維護者

### 🔴-1 退場條文一列三句兩答案，且 ✅ 的 90 天條款結構上永不觸發
B-1 L164／proposal L52 三句：①「`✅` 列在官方功能仍可用期間一律保留」→ Claude Tag 可用 → **留**；②「連續 90 天無新社群工具、無新 issue、官方無變動者移出」→ 09-22 → **移出**；③「還在跑的產品行為不因天數移出」→ **留**。自測結論只吃了 ②。ledger「退場條文三句三答案」原樣復發。更壞：五個 `✅` 全是還在跑的產品行為，③ 對每列都成立 → ② 永不生效，宣稱治好的「L62 沒有退場路」仍沒路。
**修法（B-1「退場」整段換）：**
```markdown
**退場，只有一條：** 一列的去留看**社群這一側還在不在**，不看官方那一側。連續 90 天既無新社群工具、也無新 issue 或新留言，且「官方給的是什麼」無變動者移出，移出時於該頁 `## 時序` 記一行。官方功能還在跑不是留下的理由——留下的理由是還有人在痛。**唯一例外：** `❌` 列不因天數移出，「官方到今天還沒補」本身就是結論。
```
**用現有列重跑（每列單一答案）：** `❌` 例外全留；`🧪` 最舊者「多 agent 工作流腳本化」（v2.1.202，07-07）→ 10-05 才到期，全留；`✅` 中 AGENTS.md（09-18）、subagent／通知（08-17）、破壞性指令（08-04）全留；**Slack**（06-24，社群前驅只有 Ano，此後無新工具無 issue）→ 09-22 移出。與 L62 自承「僅供對照參考」對得上。

### 🔴-2 B-1 落在他 session 宣告路徑上，但節名改名不掛裁決點 → 不能延後
`.claude/tree-claims/601a5b6e….json` 宣告 `.claude/reporter-rules/`（含 `features/pages.md`）、`wiki/index.md`、`wiki/log.md`、`scripts/check_wiki_freshness.py`、`docs/rules-changelog/`。proposal L102 把 B-1 歸「可獨立延後」，但 map L17 的節名改（→`## 官方補了沒`）兩案都會發生。頁面上而 B-1 沒上，`features/pages.md:156` 即指向不存在的節、指示不存在的兩欄——ledger 病「規則檔指向不存在的節」復發，且是每日 ingest 的觸發邊。
**修法：** 實作單把「協調 601a5b6e」提為第 0 步；談不成就本波不改節名（A-4 只換表頭與內容）。`wiki-lint-sweeps/`、`review-registry.json`、`docs/cloud-runbooks/` **未被宣告**，B-2／B-3／B-4 可逕行。

### 🔴-3 加 5n 的字面同步漏 4 處、漏一個檔、registry 寫成條件式
自跑 `grep -rn "十三\|5a–5m"` 共 **7 處**：`sweeps.md:1`、`SKILL.md:3／7／9／13／43`、`wiki-lint/SKILL.md:15`。B-2 只列 3 處。且 `review-registry.json` 有一組 `all_contain`（「雲端 weekly runbook <-> sweeps.md：B 段步驟標題錨點逐字相符」），`files` 含 **`docs/cloud-runbooks/weekly-lint.md`**，`_note` 明寫「新增步驟時必須同步加進本 patterns」；B-3 寫成「若有…pattern」且完全沒提 runbook——只改 sweeps.md 配對仍全綠，正是該 `_note` 記載的靜默漂移再犯。
**修法（B-4，列進實作單）：** ① `sweeps.md:1`→`# Wiki Lint B 段：5a–5n 逐步判準與回報格式`，新節用 `## ` 非 `### `，逐字 `## 5n. official-community-gap「官方補了沒」表對官方一手（主編親做）`；② `SKILL.md` 五處（`:3`／`:7`／`:9` 這十四步／`:13` `## 十四步`／`:43` 十四行回報）；③ `wiki-lint/SKILL.md:15`→`5a–5n …十四個掃描`；④ `docs/cloud-runbooks/weekly-lint.md` 加一列，標題與 sweeps.md 逐字相同；⑤ registry 該組 `patterns` 加 `"5n\\. official-community-gap「官方補了沒」表對官方一手"`，跑 `check_rules.py` 不得轉紅。

### 🟡-1 上限 18 用掉 17，無滿載規則
**修法（B-1 上限句後）：** `表滿時不硬塞：新列先與最下方的 `✅` 列比「哪一個還有人在痛」，輸的依退場條款移出並於 `## 時序` 記一行；兩者都還在痛就把上限議題寫進 `wiki/log.md`，不自行擴表。`

### 🟡-2 lint 5n 第 1 步會倒出整包留言
實跑 `--json state,stateReason,comments`（#28300，exit 0）回傳全部留言本文；#6235 有 405 則。B-1 自己寫「關閉狀態比留言數重要十倍」，指令卻要全文。**修法（B-1／B-3 第 1 步）：**
```
gh issue view <號> -R anthropics/claude-code --json state,stateReason,closedAt,comments \
  -q '{state,stateReason,closedAt,official:[.comments[]|select(.authorAssociation=="COLLABORATOR" or .authorAssociation=="MEMBER")|{login:.author.login,body:.body[0:400]}]}'
```
第 2 步 CHANGELOG 語法實測可用，grep `^## 2.1.277` 與 verified L38 逐字相符。

### 🟡-3 `check_wiki_freshness.py:65` 硬編「產品化矩陣同步」
該行把本頁維護來源寫成字串 `".claude/reporter-rules/features/daily.md 產品化矩陣同步"`，B-1 整節重寫會刪掉這五字且無 registry 看守＝靜默漂移；該檔又在 601a5b6e 宣告內。**零風險修法：** B-1 新節起首寫 `**產品化矩陣同步（「官方補了沒」表）：**`。

---

## 二、機器

- 兩閘全綠可複現（reader language 0、cell limits 0、最長格 110）；懸置 188 不變、L92 定義與新表短標記成對；`check_rules.py` ✅、`check_hierarchy.py` ✅；新表無 `#錨點` 出邊（map L26 降為頁級），`build_web.py` 錨點 WARN 只減不增。
- **`check_verify_dates.py`：值得，但本波不做、形狀要縮。** 現況確實零看守（三句我都核過原始碼屬實）。但它要掛 `run_tests.py` 而實作者不准動該檔；且 11 列核對日是 `—`，首跑必紅。**最小形狀（寫進機制待辦）：** 只掃「核對日」欄，`—` 不計逾期只計數；逾 45 天 WARN、逾 90 天 FAIL；**照 `reader-language-baseline.json` 先例帶存量基線**，首跑把 `—` 全收進基線。沒有基線它落地當天就會被關掉。

---

## 三、冷讀者（原四題對 draft 走一遍）

| 原題 | 舊 | 新 | 判定 |
|---|---|---|---|
| Q1 AGENTS.md ＋怎麼辦 | 2 跳半拿到 | 2 跳拿到（`claude-code:375` 改 ✅，三個邊界即「怎麼辦」） | 改善；index 仍無互通性入口（跨維護者第 4 筆被延後）🟡 |
| Q2 額度告警 | 3 跳半拿到 | 3 跳，官方側拿到（VS Code 70% 橫幅正面答「事前告警」） | 「裝哪個」見 🔴-8 |
| Q3 哪些官方沒做 | 2 跳拿到 | 2 跳拿到；`❌` 排最上、三值有圖例、L66 同列打架消失 | ✅ 最大改善 |
| Q4 Dreaming 能不能用 | 5 跳繞 3 頁 | ⟨G-05⟩ 直寫「Managed Agents 那邊、beta 內更受限的研究預覽、須另外申請」，兩處死引用拿掉 | 2 跳拿到 ✅ |

**官方事實逐列抽驗：對 verified 一～五節，17 列全數有出處、無設計者自編**（5 列有逐字背書且核對日 09-19，12 列出自對象頁既有記錄且誠實寫 `—`）。**對第六節則有五條實質衝突，見第六節。**

### 🔴-7 表上引言第三行是分工條文洩漏進正文
A-4 L46「issue 的留言數與讚數不記在這裡，那些住 [[entities/claude-code]]；本表只記 issue 號與它開著還是關了」＝欄位歸屬條文；冷讀者第 4 節第 8 條抓過同型（index:88）。原則 7：條文住規則檔（B-1 已有），正文只留一句讀者語言。
**修法（整行換）：** `> 每個 issue 現在多少人在吵、官方回了什麼，見 [[entities/claude-code]]。`

### 🔴-8 「該裝哪個只留一個出口」不成立
表上不列工具名了，但 ⟨G-05b⟩（7 個）、⟨G-07⟩（LimitBar、CCLimitPing）、⟨G-13⟩（5 個）仍在且無日期、無快照註記——冷readers 翻到細節區又拿到第二組答案。他自己開的兩個選項，draft 只做了第一個。
**修法（`**缺口細節**` 標題下一行）：** `> 下面提到的社群工具是當時的代表案例，不是現在的推薦；要裝哪個一律看 [[topics/community-tech-tools]]「我卡在這裡」。`

### 🟡-4／5／6／7 過閘但違原則 4／7 的四句
- A-4 L45 核對日定義是「我們多久查一次」。**改**：`> 「核對日」＝這一列最後一次對過官方文件或 CHANGELOG 的日期；`—` 代表還沒對過，要拿它做決定時建議自己再查一次官方文件。`
- A-5 L82「這幾段是本頁在別處找不到的東西」＝自我評語，**整句刪**，保留其後「但它們說的是到目前為止的理由，不是預言」。
- A-9 末則「兩張表併成一張」把頁面整理寫進時序（`整理語` 只掃 callout 故過閘，設計者 L145 自己也承認）。**改**：`- **同一個痛點不再有兩個互相打架的狀態**：先前「多模型路由」一處寫「官方無對應」、另一處寫「部分對應」，跨 session 記憶也有兩個狀態；現在每個痛點只有一個狀態，並標出最後一次對過官方的日期。`
- A-4 第 6 列「門檻也不能自訂」去掉了 verified L47 的「推論」標註 → 改 `門檻似乎不能自訂`。

**17 列 × 5 欄讀得下去**：最長格 110、第 4 欄平均約 45 字，`❌`→`🧪`→`✅` 讓讀者的行動集中在上半。可接受。

---

## 四、治理

### 去向表抽驗（開原頁核行號，8 段）
L39 刪→家在 L198–200（2026-09-12 段確有 orca／spec-kit／comet）✅｜L43 刪→Cowork／v2.1.196／Dreaming 分在 L153／L106／L58，推薦案下 L106 刪但上移新表第 7 列、L107 上移第 12 列，均不消失 ✅｜L62 自承句保留 ✅（draft L74）｜L64 ⟨Q-02⟩ 短標記 ✅（draft L60 第 4 格，與 L92 成對）｜L92／L153 原文不動 ✅（188 不變）｜L77 393 字元拆 ⟨G-05⟩＋⟨G-05b⟩ ✅（7 個工具名與三種機制描述一字不失）｜L79 死引用修掉 ✅｜**L100 備註不實 🟡-8**：`/loop`／`/batch` 全庫查無於 agent-stack，家在 `feature-radar:349` 與本頁 L116（留原處）——事實未消失，歸屬寫錯。

### 🔴-4 「節名未凍結已查證」不實，推薦案破 topics 模板契約
proposal L89 稱三節名在 `scripts/` 零命中。自跑 `grep -rn` **命中 4 處**：`scripts/wiki_graph.py:62`（「目前結論」在 `TEMPLATE_HEADINGS`）、**`.claude/reporter-rules/page-templates.md:87`（topics 模板把 `## 目前結論` 列為必備節，該檔只允許 `技術彙整` 依類別自訂名）**、`wiki-lint-reporters/references/dispatch.md:37／45`、`wiki-lint-sweeps/references/sweeps.md:178`（三處 lint 步驟都以「補『目前結論』」派活）。
**故裁決點 (2)：內容全換同意、改名反對。** 第三案兩邊好處都拿得到且不必多開規則改動：
```markdown
## 目前結論

**官方為什麼還沒補**

上面三個 ❌ 裡有兩個、加上「花費估不準」這一面，……（以下照 A-5 原文，數字依 🔴-9 調整）
```
位置仍照推薦案前移到表格之後（不受模板與腳本拘束，map L79 已查證無錨點入邊）。若第二輪堅持改名，B 段須加：`page-templates.md` 補一句「`目前結論` 亦可依議題自訂名，命名原則同 `技術彙整`」，並回掃 dispatch.md／sweeps.md 兩處措辭。

### 🔴-5 回掃清單漏一頁（跨維護者，社群）
`grep -rln "AGENTS.md" wiki/` 共 11 檔。proposal 涵蓋 claude-code、coding-workflow-guide、feature-radar，**漏 `topics/community-tech-discussions:171／222`**——表列與細節條目仍寫成「社群長期呼籲…跨平台已成競品共識」、`🌙靜候`、數字停在 08-27。該頁屬社群記者（`community/daily.md:14`）。
**修法（跨維護者加第 6 筆）：** `→ **社群**：`community-tech-discussions:171／222` 仍把 AGENTS.md 寫成進行中的社群呼籲；官方已於 v2.1.277（09-18）原生支援、#6235 於 08-17 CLOSED/COMPLETED，請更新表列狀態與細節條目。`
🟡-9：`overview.md:73`（主編週更自然覆寫）與 `competitor-landscape.md:264`（08-26 時序內的 36Kr 報導，屬歷史）建議只記進 `wiki/log.md`。

### 🔴-6 同維護者回掃漏 5 筆，是本波 verified 自己證實的
全庫掃 issue 號，`entities/claude-code`（功能記者＝同維護者）尚有 5 筆標 🔴 未修復：`:200` #24316、`:255` #14227（NOT_PLANNED 05-25）、`:256` #47023、`:379` #29006、`:380` #28322。proposal 只列 `:375`，並說組頭統計 +1——實際跨兩組（#14227／#47023 屬 🧠、#29006／#28322 屬 🔌），不是 −1。
**修法（同維護者表加一列）：** `| `entities/claude-code:200／255／256／379／380` | 五筆仍標 🔴 未修復 | 依 verified 第二節改 ✅ 已修復（附關閉日與官方怎麼答）；#14227 改 ⛔ 官方拒修；**只改狀態詞與一句官方回覆，不重寫條目**；同批重算兩組組頭的未修復條數 |`

### 保守預設是否真的保守
- **裁決點 (1)：支持推薦案「併」。** 保守預設留 3 列會留下第二套符號（`⚡`）與第二張表，正是本波要治的病；且第六節之後 ❌ 只剩 3 個（推薦）／1 個（保守），保守案的 A-5 導言會變得幾乎寫不出來——這本身就是「別留第二張表」的證據。真要走保守，至少得把 `⚡` 改寫成三值之一。
- 🟡-10：proposal L68 說 claude-code「三處引用本頁」（88／262／655），實為 **4 處**（另 `:666`）。只核對不改字，無害，但數字要對。
- 🟡-11：需主編補查 9 項齊全，第 6 項正對上健檢卡第 9 節「❌ 列舉證責任反了」，收得好；第六節交件後 1–8 項已結，僅第 9 項（radar 缺 v2.1.277）待辦。

---

## 五、對 verified 第六節：draft 的五條實質衝突（第二輪必改）

draft 寫於第六節之前，以下五條**直接改變表上狀態或列數**，不是文字潤飾。

### 🔴-9 「Agent 跟 agent 做生意」列過不了設計者自己寫的入口判準 → 應移出表
六-8：`gh api` 實測 5,855★ 但 **9 watchers、1 貢獻者、4 筆 commit、08-19 後無更新**，判「採用未證實，星數不可作熱度依據」。B-1 入口判準 ①＝「≥2 個獨立社群工具，或一則 issue ≥100 讚」——本列只有 internet-court-skill 一個工具、無 issue，**不過 ①**。新表第一天就有一列違反自己上方的判準（ledger「修法自己破閘」同族）。其餘三個 `❌` 我逐一核過均過 ①（Writ／Caliber／Patina；loopx 等 8 款；recap／modularity／命名一致性）。
**修法：** ① A-4 刪第 3 列；② ⟨Q-02⟩ 於 L92 結案（逐字：`- ⟨Q-02⟩ **已查證**（2026-09-19）：internet-court-skill 星數 5,855 但 watchers 僅 9、貢獻者 1 人、commit 4 筆、08-19 後無更新——星數撐不起採用程度，本表不列此痛點；工具本身見 [[topics/community-tech-tools]]。`）；③ ⟨G-12⟩ 壓成一句指向 `community-tech-tools`（該工具在 `:202`／`:308` 與 `community-tech-patterns:663` 都有家，不消失）；④ `## 時序` 新段補一行記移出理由。⑤ **懸置數：** L92 結案後 188→187，高於基線 140，`check_pending_markers.py` 只擋「低於基線」→ 過閘，保命條款不受影響。

### 🔴-10 「多 agent 工作流腳本化」列三處事實過期，且與全庫既有正確值打架
draft L67 寫「Dynamic workflows（**研究預覽**，最多 1,000 平行子代理）」「官方版本在 feature-radar 評為暫不推薦（**退款爭議未解**）」、核對日 `—`。六-1a：官方文件「available on **all paid plans**…On Pro, turn them on from the Dynamic workflows row in `/config`」，**已無 research preview 字樣**；退款爭議官方無專文，**未查得**，不得寫成已解或未解。且 `feature-radar:337` 與 `anthropic-agent-stack:226` 兩處早已寫對（「全部付費方案」），draft 會成為第三個互打的家。六-1b：Claude Code Projects＝public beta（僅 Pro／Max），可列為本列官方對應之一；是否解「看不到誰卡住」官方未明說，不寫。
**修法（整列換，狀態 🧪→✅）：**
```markdown
| 把多 agent 工作流寫成能重跑的腳本 | ✅ | Dynamic workflows：全部付費方案可用（Pro 要在 `/config` 打開），最多 1,000 平行子代理，跑到額度上限會暫停而不是失敗；Claude Code Projects 讓一個對話協調多個雲端 session（public beta，限 Pro／Max） | 本庫因 UltraCode 1.7M token 事件在 [[feature-radar]] 標為暫不推薦，官方未就此發過說明 ⟨G-02⟩ | 2026-09-19 |
```
⟨G-02⟩ 同批改（map L36 本就要求改第二行但 draft 未給逐字，屬 🟡 漏件）：刪「2026-05-28 Research Preview」，改寫為「首發時是研究預覽，現已開放全部付費方案」；#28322／#29006 已於 08-19／08-17 關閉，「官方可能已悄悄鋪路」改「已出貨」。

### 🔴-11 「想自己決定哪段用哪個模型」再犯本波根因（低估官方）
draft L64「org default model、`enforceAvailableModels`——**兩者都是企業管理端**」「個人的動態路由官方沒有」。六-3：`model-config` 的 **`opusplan`**「uses `opus` during plan mode, then switches to `sonnet` for execution」是個人端就有的官方模型切換。漏掉它正是 verified 第五節第 1 句點名的病。
**修法（第 3、4 格換，核對日填 2026-09-19）：**
```markdown
| 想自己決定哪段用哪個模型、不被鎖住 | 🧪 | 個人端有 `opusplan`：規劃時用 Opus、開始執行自動換 Sonnet；org default model（v2.1.196）與 `enforceAvailableModels` 白名單則是企業管理端 | 只有這一種固定切換，依成本或任務動態選模型的路由截至 2026-09-19 官方文件未見；換設定差多少錢見 [[topics/model-comparison]] ⟨G-13⟩ | 2026-09-19 |
```
⟨G-13⟩ 首句同步補 `opusplan`。

### 🔴-12 Cowork 列：日期錯、「正式擴展」不成立、且 L153 懸置已可結案
六-5：官方 blog 發布日 **07-07**（07-08 是日報日）；用詞是 **beta access**「rolling out over the next several weeks starting with Max users」，不是「正式擴展」；且「Desktop remains the place for deep work, and it's **the full Cowork experience**, where Claude can also use your local files and browser」——**行動／網頁版不等同桌面已有官方答案**。draft L69 仍寫「行動版功能範圍是否等同桌面待查」。map L75 說 L153「留原處、標記一字不動」，proposal §5 保命條款據此宣稱本波懸置不變——現在該懸置已可結案。
**修法：** ① A-4 第 12 列換成：
```markdown
| 手機或瀏覽器用得到嗎 | 🧪 | 用得到但不完整：Artifacts 可把成果輸出成網頁分享；Cowork 網頁／行動版自 2026-07-07 起逐步開放（beta，先給 Max 用戶），任務在雲端續跑 | 官方明說桌面版才是完整體驗——只有桌面能讓它用你本機的檔案與瀏覽器 | 2026-09-19 |
```
② L153 懸置結案（逐字接在該段末）：`❓ 已查證（2026-09-19）：官方說明桌面版才是完整的 Cowork 體驗，網頁與行動版不能使用本機檔案與瀏覽器；發布日為 07-07，官方用詞是 beta access 而非正式擴展。` ③ L43 的 07-08 隨 A-3 一併消失，本頁 07-07／07-08 兩個日期的打架同時解掉（健檢卡查證表第 3 項）。④ 懸置數再 −1：加 🔴-9 後 188→**186**，仍高於基線 140，過閘。

### 🔴-13 「看不到誰卡住」與「品質夠不夠」兩列的官方欄不完整
六-1c：`agent-view` 文件「Agent view is in **research preview**」且每列「appears as a row showing whether it's **working, waiting on you, or done**」，一般 session 提示列還有「`← 2 agents`」計數。draft L65「是列表不是即時地圖；誰在等誰、誰卡住仍得自己拼」——「誰卡住」官方其實顯示了，**又是一次低估官方**；且漏了「研究預覽」這個讀者會踩的限定。
六-2：Outcomes＝**Beta，同 Managed Agents beta header**；draft L68 只寫「Outcomes 規格驗證」無任何限定，讀者會以為打開就能用（正是冷讀者 Q4 對 Dreaming 踩過的坑）。
**修法（兩列，核對日皆填 2026-09-19）：**
```markdown
| 一堆 agent 在跑，看不到誰卡住 | 🧪 | Agent view（研究預覽）每個 session 一列，標出它在跑、在等你、還是做完了；一般 session 的提示列會顯示還有幾個 agent 在等你；`--forward-subagent-text` 讓 `stream-json` 帶出子代理文字 | 看得到單一 session 的狀態，看不到誰在等誰這種依賴關係的全圖 ⟨G-09⟩ | 2026-09-19 |
| 它說做完了，但品質夠不夠 | 🧪 | `/goal` 判完成條件（一般功能）、`/code-review`（v2.1.218 起背景執行）；Outcomes 規格驗證屬 Managed Agents，仍是 beta、要帶 beta header | 答的是「做完沒」不是「寫得好不好」；社群的多模型對抗審查無公開對照數據 ⟨G-06⟩ | 2026-09-19 |
```

### 🟡-12 三處連帶調整（同批做，不另列 🔴）
① A-5 第一段末補跨裝置限制（六-4）：`/usage` 已能把用量拆到 skills、子代理、外掛與個別 MCP server，但它只算這台機器上的紀錄，別台裝置與 claude.ai 不算在內，單一請求為什麼這麼貴也還是沒有。` ② 四個 `❌` 的否定證明現有範圍（六-6），核對日可填 2026-09-19，第 3 格由「無」改 `截至 2026-09-19 官方文件未見`。③ 破壞性指令列六-7 明示**未重查**，核對日**維持 `—`**——draft 原就寫 `—`，第二輪不得順手填 09-19。

### 數字重算（第六節全部吃進後）
移出商業往來列、工作流腳本化改 ✅ → **推薦案 16 列：3 ❌／7 🧪／6 ✅**；保守案（再刪 CLAUDE.md、AI 副作用、手機瀏覽器）→ **13 列：1 ❌／6 🧪／6 ✅**。A-3 摘要、A-5 導言（「上面三個 ❌ 裡有兩個」）、A-4 保守預設註三處數字全部要改。懸置由 188 → **186**（基線 140，過閘）。

---

## 六、照順序執行（實作單）

> **〔決1〕**＝依裁決點 1；**〔決2〕**＝依裁決點 2；**〔協〕**＝需主 session 先協調 601a5b6e。

0. **〔協〕** 協調 `features/pages.md`；談不成則第 3 步不改節名、第 12 步 B-1 延後並記 ledger。（🔴-2）
1. 標頭 A-1、callout A-2、摘要 A-3（數字用 🔴-9〜13 後的 16／3／7／6，保守則 13／1／6／6）。
2. 新表取代 L47–67：5 欄表頭、圖例三行（第三行用 🔴-7、加 🔴-8 快照句）；**吃進 🔴-9〜13 的五列逐字**。**〔決1〕** 16 或 13 列。
3. **〔協〕** 節名改 `## 官方補了沒`。
4. 缺口細節 A-6 七條＋⟨G-02⟩（🔴-10）、⟨G-12⟩ 壓縮（🔴-9）、⟨G-13⟩ 補 `opusplan`（🔴-11）。
5. 懸置結案兩筆：L92 ⟨Q-02⟩（🔴-9）、L153 Cowork（🔴-12）。可驗：`check_pending_markers.py` 為 **186**，不得低於 140。
6. **〔決1〕** 對照矩陣：併則整節刪（L96–108）；保守則只留 3 列並把 `⚡` 改寫成 `🧪`。
7. 技術彙整 L131／L135 事實更正；L139／L143／L161 三段搬出（L141 那段依 🟡-12① 補跨裝置句）。
8. **〔決2〕** 目前結論：採 🔴-4 第三案（節名留、粗體小標、前移到表格後）；若堅持改名，先做 `page-templates.md` 配套。
9. 相關實體 A-8；時序 prepend A-9（末則用 🟡-6 修法，並補「商業往來列移出」「Cowork 待查結案」兩行）。
10. 跑閘：`check_cell_limits.py --page official-community-gap` → `check_reader_language.py --page official-community-gap` → `check_pending_markers.py` → `gen_wiki_frontmatter.py` → `check_hierarchy.py` → `build_web.py`（錨點 WARN 不增）。
11. 同維護者回掃：`claude-code:375` ＋ **🔴-6 的五筆狀態更正** ＋ 兩組組頭統計重算；`coding-workflow-guide:134`。
12. **〔協〕** B-1（含 🔴-1 退場、🟡-1 滿載句、🟡-2 指令、🟡-3 保留「產品化矩陣同步」字面）。
13. B-2／B-3／**B-4**：🔴-3 的五項逐字同步。可驗：`check_rules.py` 維持 ✅。
14. **〔協〕** 跨維護者轉知 **6 筆**（原 5＋🔴-5）：`python scripts/pending_handoffs.py open --from 功能 --to 社群 …`。
15. **〔協〕** `wiki/index.md` 鉤子與互通性入口列、`wiki/log.md` Query／定稿條目。
16. `run_tests.py` exit 0；機制待辦記 `check_verify_dates.py`（最小形狀見第二節）；needs-補查只剩 radar 缺 v2.1.277 一項。

---

## 自跑紀錄

`gh issue view 6235 … --json state,stateReason,closedAt` → `CLOSED／COMPLETED／2026-08-17T03:37:37Z`（exit 0）｜`gh api …CHANGELOG.md -H "Accept: application/vnd.github.raw"` → `## 2.1.277` 下第一行與 verified L38 逐字相符（exit 0）｜scratchpad `gate.py` 抽 draft A 段 9 個 fence 成 82 行暫存檔：reader language 0、cell limits 0、最長格 110、表格 19 行｜`check_pending_markers.py` 188／基線 140｜`check_rules.py` ✅｜`check_hierarchy.py` ✅（18 個母頁）｜`grep -rln "AGENTS.md" wiki/` 11 檔｜`grep -rn "十三\|5a–5m"` 7 處／3 檔。

---

## 實作複核（2026-09-20）

對象＝工作樹現行檔（未 commit）。忽略 `docs/architecture-archify/`、約百頁純 frontmatter 日期滾動與 `web_reader/data/*`。
**判定：🔴 3 條、🟡 6 條；有條件放行**——三條 🔴 都只需小改，逐字修法已量過閘，合成「最後一批」見末節。

### 1. 逐步核（proposal §8 的 14 步）

| 步 | 判定 | 證據 |
|---|---|---|
| 1 標頭／callout／摘要 | 照做 | 首屏只剩 `2026-09-20` 一個口徑（L30／31／33）；L43「13 個痛點裡，1／6／6」與表相符 |
| 2 新表＋節名＋三行圖例 | 照做 | L47 `## 官方補了沒`；L49–51 三行（🔴-7／🔴-8 逐字皆在）；13 列＝1❌／6🧪／6✅，我逐列數過 |
| 3 缺口細節＋快照句 | 照做 | L91 快照句在；⟨G-01⟩–⟨G-13⟩ 九條改寫到位 |
| 4〔決1〕對照矩陣留 3 列改三值 | 照做 | L139–141 為 ❌／🧪／❌，L135 有節首圖例 |
| 5 技術彙整四處更正＋三段搬出 | **漏做（🔴-A）** | 四處事實更正皆在（L166／L168／L178／L182），但 `### ⚡ 部分對應：輸出品質驗證`（L160）與 `### ⏳ 正在做但不夠：跨 session 記憶`（L164）兩個標題沒改，同節的 L172／L180 卻已 ⚡→🧪 |
| 6 目前結論節名留、前移、內容換 | 照做 | L71–85 在結論表之後；節名未動（模板契約保住） |
| 7 時序 prepend 八則 | **偏離（🟡-a）** | 實為 9 則：internet-court 一事寫了兩遍（L205 與 L206），L207 掉成沒有粗體開頭的孤兒 bullet；計畫載明的「Slack 移出」那一則**沒有寫**（連帶造成 🔴-C） |
| 8 claude-code 六行＋三組組頭 | 照做，數字我自算 | 六行狀態全對；`groupcount.py` 逐組重數，八個組頭**全部相符**（🧠 51／📂 11＋2 拒修／🔌 平台 67＋3 已修復皆與實數一致） |
| 9 `--rebuild-count` | 照做但見 🟡-c | `count` 140→186、`reason` 已填 |
| 10 六閘 | 照做 | reader language 0 新增、cell limits 0 新增、pending ✅、`check_rules.py` ✅、`check_hierarchy.py` ✅ |
| 11 B-1 | 照做 | `pages.md:156` 起整節換，`### 產品化矩陣同步（「官方補了沒」表）` 字面保住（🟡-3 修法照吃） |
| 12 B-2／B-3／B-4 | 照做 | 我第一輪點名的 7 處字面全改（sweeps.md:1、SKILL.md:3／7／9／13／45、wiki-lint/SKILL.md:15）；runbook L37 有 5n 列；registry L1629 加 `5n\. official-community-gap`；`check_rules.py` ✅ |
| 13 轉知 6 筆＋index＋log | 照做 | `data/pending-handoffs.jsonl` +4 筆（另 2 筆屬主編自持頁，見 §6） |
| 14 `run_tests.py` | 照做 | 我自跑 **exit 0**，八個「狀態：✅」全綠 |

### 2. 設計者三改寫＋一反駁

- **🔴-1 退場改成雙訊號：接受，且比我的版本好**——我的「看社群這一側」確實沒指定時鐘，他用 `## 時序`（本頁唯一留痕又 grep 得到）並說明為何不用核對日（5n 每週會把鐘撥回去）。**但 13 列重跑我判它仍有一列無解，見 🔴-C。**其餘 12 列我逐列跑過皆單一答案。
- **🔴-2 不設協調第 0 步：接受**。我自查 `git log`：601a5b6e 的工作止於 2026-09-16（`4e47e1c1`／`64123d5a`），claim 確為殘留。⚠️ 但 `.claude/tree-claims/601a5b6e….json` **檔案還在**，仍宣告 `.claude/reporter-rules/`，主 session commit 時會被 `block_foreign_stage.py` 擋——收尾前要先處理該檔。
- **🔴-9② 懸置細節整區移除：接受**。我查證無孤兒也無事實消失：`internet-court` 全庫仍 5 檔有家（含 `community-tech-tools:202／308`、`community-tech-patterns:663`），`ERC-7710` 3 檔；本頁 ⟨G-12⟩（L126）據實留一句。他的理由（短標記所屬儲存格已移出、留定義會成 ⟨Q-03⟩ 型孤兒）成立。
- **🟡-10 反駁：接受，我錯了**。`grep -c` 實為 **6** 處（`:88／:262／:655／:666／:730／:731`），我漏了兩筆歷史記錄列。

### 3. 三個偏離逐一判

- **(a) `daily/2026-09-11.md:40` 錨點改頁面連結：照做且正確。** 節名已從「Agent 工作模式產品化追蹤」改掉，該錨點必失效；`daily/` 是讀者版投影不是 wiki 正文，降成頁級連結是最小修，不必改寫日報內容。無異議。
- **(b) `allowlist_patterns` 加 `^scripts/check_verify_dates\.py$`：判「把閘弄鬆了，有更乾淨的寫法」。** 該清單豁免的是路徑存在性檢查（`check_rules.py:169`，只驗反引號內的字串），加一個不存在的腳本等於在「規則檔不得指向不存在的檔」上開一個永久洞，而 `pages.md:197` 同一句**已經**指向 `docs/page-audits/ledger.md` 機制待辦，腳本名是多餘的。**逐字修法（改完把 registry 那兩個新增行還原）：** 把 `pages.md:197` 句末的 `最小看守方案見 ... （`scripts/check_verify_dates.py`，帶存量基線、逾 45 天 WARN／90 天 FAIL）。` 換成 `最小看守方案（帶存量基線、逾 45 天 WARN／90 天 FAIL）見 `docs/page-audits/ledger.md` 機制待辦，腳本名與形狀寫在該檔。`
- **(c) `--rebuild` 收基線：🔴-B，吸收了本波自己新造的超限。** `_hits` 實為 **987→966**（非 960→966）。逐頁：`official-community-gap` 15→5（新增 0，✅ 乾淨）、`entities/pricing` 74→72（新增 0，該頁正文未改、只掉 2 筆陳舊指紋，🟡-d）、**`entities/claude-code` 274→265，新增 6 移除 15**。我用 `check_cell_limits` 同口徑逐行量那六行（剝 URL 後）：

| issue | 改前 | 改後 | |
|---|---|---|---|
| #24316 | 340 | 327 | 變短，本就超限 |
| #14227 | 317 | **353** | 變長 |
| #47023 | 347 | **435** | 變長 |
| #29006 | 249 | **298** | 變長 |
| **#6235** | **167（合規）** | **299** | **本波新造的超限** |
| **#28322** | **200（合規，閘為 `>200`）** | **254** | **本波新造的超限** |

五行變長、**兩行從合規跨進超限**，再被 `--rebuild` 一併收進基線——`check_cell_limits.py` 檔頭「棘輪只能往下轉」對這兩行是往上轉。沒有夾帶他頁的新增（pricing 是純移除）。

### 4. 保命條款與事實去向

- **186 恰為兩筆結案**：改前本頁 L92 ⟨Q-02⟩＋L153 Cowork 共 2 筆，全庫 188；現 frontmatter `pending_count: 0`、全庫 186。188−2＝186 ✅。
- **去向抽驗 8 段（對現行頁）**：`internet-court`／`ERC-7710`（⟨G-12⟩ 留）、`orca`（⟨G-11⟩ L124 留）、`Gorchestra`（⟨G-02⟩ L101 留）、`Workweave`（⟨G-13⟩ L128 留）、`SmolVM`（⟨G-04⟩ L103 留）皆在。**`Ano`（原 L62 Slack 列代表工具）與 `live-log-viewer-next`（原 L66）離開本頁**，兩者全庫各仍有 3 檔有家——**無事實消失**，但 B-1 契約寫「歷史上的代表工具留在 ⟨G-nn⟩」，這兩個沒有落點（Slack 列無 ⟨G-nn⟩、⟨G-09⟩ 只留「社群自建地圖式檢視器」不具名）。🟡-e。

### 5. 官方事實抽驗（13 列「官方給的是什麼」對 verified 一～六節）

逐列核完，**13 列全部對得上，無自編**。第六節五條全部落地：Dynamic workflows 改「全部付費方案」＋Projects public beta（L62，✅）、Agent view 標「研究預覽」且寫出「在跑／在等你／做完了」（L59）、Outcomes 標 beta＋beta header（L61）、`opusplan`（L58）、Cowork 改 07-07／beta access／桌面才完整（L140、L178）。**破壞性指令列核對日維持 `—`**（L66）✅——六-7 的禁令守住了。`❌` 列照新契約寫「截至 2026-09-19 官方文件未見」（L55）✅。

### 6. 讀者語言與條文洩漏

閘 0 新增命中；人眼再掃一遍正文，**無判準／退場／上限條文洩漏**，圖例三行足夠（三值定義＋核對日含「自己再查一次」的讀者動作＋issue 熱度出口）。兩點：🟡-f 摘要 L43 說「13 個痛點」，但同頁 `## 對照矩陣` 另有 3 個痛點，讀者實際看到 16 個；🟡-a 的 L207 孤兒 bullet 讀起來像上一則的斷句。

### 7. 放行與最後一批

**條件放行**——三條 🔴 都是定點小改，做完即可 commit。

1. **🔴-A** 兩個標題改三值（本波主病殘留）：L160 → `### 🧪 部分對應：輸出品質驗證`；L164 → `### 🧪 部分對應：跨 session 記憶`。（改完全頁正文再無 ⚡／⏳，只剩時序歷史段，那是當時的判定、不動。）
2. **🔴-B** 兩行改回合規後**重跑** `python scripts/check_cell_limits.py --rebuild`（我已量過，剝 URL 後分別 186／179 字元，讀者語言 0 命中）：
   - `entities/claude-code:375` 整行換成：`- ✅ **已修復** v2.1.277（2026-09-18）｜**AGENTS.md 規範不支援（GitHub issue #6235，396 則留言、6643 個讚，2026-07-10 首見，全站讚數最高）**：Claude Code 現已原生讀取 [AGENTS.md](https://agents.md/)；三個邊界見 [[topics/official-community-gap]] ⟨G-08⟩。`
   - `entities/claude-code:380` 整行換成：`- ✅ **已修復**（2026-08-19 官方關閉）｜**既有 session 中 `/remote-control`（`/rc`）未被識別為內建指令（GitHub issue #28322，2026-07-13 回報）**：官方答 v2.1.76 修好「Unknown skill」、v2.1.206 起 `/remote-control` 一律解析得到。`
3. **🔴-C** 退場①對 Slack 列沒有時鐘：`## 時序` 與 archive 對「Slack／Claude Tag」**零命中**（我兩邊都 grep 過），`wiki/log.md` 也查不到開列日，故①的備援「從開列日起算」無資料可讀——設計者 §5 自測算出的 2026-09-22，用的是 2026-06-24 這個**官方發布日**，不是開列日。修法兩處：
   - `pages.md` 入口判準段末加一句：`**開新列時 `## 時序` 記一行開列日**——它是退場條款 ① 唯一的時鐘，時序上沒有痕跡的列永遠退不了場。`
   - 本波 `## 時序` 2026-09-20 段補一則（補上計畫第 7 步漏掉的那一則）：`- **「Slack 裡要一個 AI 隊友」這一列開始計時**：這一列的社群前驅一直只有 Ano 一個，開列日在本頁時序上查不到；自 2026-09-20 起算，若往後 90 天社群這邊仍無新東西、官方也沒動，就把它移出表。`
4. 順手（非放行條件）：🟡-a 刪 L205 那則重複、把 L207 併回 L206；🟡-b 照第 3 節 (b) 還原 registry 兩行；🟡-c 把基線 140→186 記進 `wiki/log.md`（另 15 頁的下一次結案會因此吃紅燈，得讓別的 session 知道）；🟡-e 把 `Ano`／`live-log-viewer-next` 補進對應 ⟨G-nn⟩ 或在契約標明例外；🟡-f 摘要數字補一句涵蓋對照矩陣那 3 個。
5. 收尾前先處理 `.claude/tree-claims/601a5b6e….json`（殘留 claim 會擋 commit）。
