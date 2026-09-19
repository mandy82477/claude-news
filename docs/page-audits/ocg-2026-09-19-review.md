# 第 14 波評審：topics/official-community-gap

對象：提案三件（`-proposal.md`／`-proposal-map.md`／`-draft.md`，以磁碟現行檔為準）。
行號＝各該檔案原始行號。機械項全部自跑，指令與輸出見文末「自跑紀錄」。
判定：**🔴 8 條、🟡 11 條**。結論：**有條件放行進第二輪**（🔴-1／2／3／4／6 必須回應；🔴-5／7／8 已給逐字修法可直接吃）。

---

## 〇、代判數字重算（全部自算，不採信提案宣稱）

| 提案宣稱 | 我算的 | 判定 |
|---|---|---|
| 新表 17 列（保守 14） | 表格行 19 −表頭−分隔＝**17**；刪 3 列＝**14** | ✅ |
| 4 ❌／8 🧪／5 ✅；保守 2／7／5 | draft L58–61＝4 ❌、L62–69＝8 🧪、L70–74＝5 ✅；刪 CLAUDE.md・AI 副作用・手機＝2／7／5 | ✅ |
| 兩閘 0 命中 | `check_reader_language` 逐詞跑 9 個 fence：**0**；`check_cell_limits`：**0**，最長格 110 字元（上限 120） | ✅ |
| 懸置標記 188 筆、本頁 2 筆 | `check_pending_markers.py`：188（基線 140），本頁 L92＋L153 | ✅ |
| Slack 列 2026-09-22 滿 90 天 | 2026-06-24 ＋90 日＝**2026-09-22** | 日期對，**結論錯**，見 🔴-1 |
| `check_rules.py`／`check_hierarchy.py` 現況 | 兩者均 ✅ 通過（改動前基線） | ✅ |

---

## 一、明天的維護者

### 🔴-1 退場條文一列三句兩答案，且 ✅ 的 90 天條款結構上永不觸發

B-1 L164／proposal L52 三句：①「`✅` 列在官方功能仍可用期間一律保留」→ Claude Tag 可用 → **留**；②「連續 90 天無新社群工具、無新 issue、官方無變動者移出」→ 2026-09-22 → **移出**；③「還在跑的產品行為不因天數移出」→ **留**。設計者自測結論「屆時移出」只吃了 ②。這正是 SKILL 四「不得三句三答案」與 ledger「退場條文三句三答案」抓過的同一條。
更壞的是：五個 `✅` 全部是還在跑的官方產品行為，③ 對每一列都成立 → ② 永遠不會對任何 `✅` 列生效，等於本波宣稱「治好 L62 沒有退場路」的那條路仍然沒有。

**修法（B-1「退場」整段換成）：**
```markdown
**退場，只有一條：** 一列的去留看**社群這一側還在不在**，不看官方那一側。連續 90 天既無新社群工具、也無新 issue 或新留言，且「官方給的是什麼」無變動者移出，移出時於該頁 `## 時序` 記一行。官方功能還在跑不是留下的理由——留下的理由是還有人在痛。**唯一例外：** `❌` 列不因天數移出，「官方到今天還沒補」本身就是結論。
```
**用現有 17 列重跑（每列只有一個答案）：** 4 個 `❌` → 例外，留。8 個 `🧪` 最後動態最舊者為「多 agent 工作流腳本化」（v2.1.202，07-07）→ 10-05 才到期，全留。`✅`：AGENTS.md（09-18）、subagent（#24316 08-17）、通知（#29006 08-17）、破壞性指令（v2.1.222 08-04）皆留；**Slack**（2026-06-24，社群前驅只有 Ano，此後無新工具、無 issue）→ 2026-09-22 移出。單一答案，且與 L62 自承「僅供對照參考」對得上。

### 🔴-2 B-1 落在他 session 宣告路徑上，但節名改名不是裁決點 —— 不能延後

`.claude/tree-claims/601a5b6e….json` 宣告 `.claude/reporter-rules/`（含 `features/pages.md`）、`wiki/index.md`、`wiki/log.md`、`scripts/check_wiki_freshness.py`、`docs/rules-changelog/`。proposal L102 把 B-1 歸入「可獨立延後」。但 map L17 的節名改（`## Agent 工作模式產品化追蹤` → `## 官方補了沒`）**不掛在任何裁決點上**，兩案都會發生。頁面一上、B-1 沒上，`features/pages.md:156` 就指向不存在的節，且指示功能記者更新「官方對應」與「狀態」兩個已不存在的欄——ledger 病「規則檔指向不存在的節」原樣復發，而且是每日 ingest 的觸發邊。
**修法：** 實作單把「與 601a5b6e 協調 `features/pages.md`」提為**第 0 步**（在動 A-4 之前），協調不到就本波不改節名（A-4 只換表頭與內容，節名留 `## Agent 工作模式產品化追蹤`，B-1 延後）。`wiki-lint-sweeps/`、`review-registry.json`、`docs/cloud-runbooks/` 三者**未被宣告**，B-2／B-3 可自行進行。

### 🔴-3 加一步 5n 的字面同步漏 4 處、漏一個檔、registry 寫成條件式

自跑 `grep -rn "十三\|5a–5m"`，全庫共 **7 處**：`sweeps.md:1`（H1）、`SKILL.md:3／7／9／13／43`、`wiki-lint/SKILL.md:15`。B-2 只列 3 處（description／H1／導言）。漏掉 `SKILL.md:13`「## 十三步」、`SKILL.md:43`「十三行回報全部有值」、`sweeps.md:1`、`wiki-lint/SKILL.md:15`。
更關鍵：`.claude/review-registry.json` 有一組 `all_contain` 同步配對（「雲端 weekly runbook <-> sweeps.md：B 段步驟標題錨點逐字相符」），`files` 含 **`docs/cloud-runbooks/weekly-lint.md`**，`_note` 明寫「新增步驟時必須同步加進本 patterns」。B-3 的登記檢查寫成「若有…pattern」是條件式，且完全沒提 runbook。只加 sweeps.md 不加 runbook 與 patterns，配對仍全綠（它只驗「清單裡的都在」）＝ 這組 _note 記載的靜默漂移原樣再犯。
**修法（B-2／B-3 之外再加 B-4，並列進實作單）：**
1. `sweeps.md:1` → `# Wiki Lint B 段：5a–5n 逐步判準與回報格式`；新節標題用 `## ` 不用 `### `，逐字：`## 5n. official-community-gap「官方補了沒」表對官方一手（主編親做）`
2. `SKILL.md` 五處：`:3` description、`:7` H1、`:9`「這十四步」、`:13`「## 十四步」、`:43`「十四行回報」
3. `wiki-lint/SKILL.md:15` → `5a–5n 主編親做／親查的十四個掃描`
4. `docs/cloud-runbooks/weekly-lint.md` 步驟表加一列，標題與 sweeps.md **逐字相同**
5. `review-registry.json` 該組 `patterns` 陣列加 `"5n\\. official-community-gap「官方補了沒」表對官方一手"`；改完跑 `python scripts/check_rules.py`（現為 ✅，不得轉紅）

### 🟡-1 上限 18 用掉 17，沒有滿載規則
B-1 L162 定上限 18，新表開局就 17。入口判準過了但表滿了怎麼辦沒寫，下一次就得臨場發明。**修法**：在上限那句後補一句 —— `表滿時不硬塞：新列先與最下方的 `✅` 列比「哪一個還有人在痛」，輸的那列依退場條款移出並於 `## 時序` 記一行；兩者都還在痛就把上限議題寫進 `wiki/log.md`，不自行擴表。`

### 🟡-2 lint 5n 第 1 步會倒出整包留言
實跑 `gh issue view 28300 -R anthropics/claude-code --json state,stateReason,comments`（exit 0）回傳全部留言本文；#6235 有 405 則，主編照做會被留言洗掉。B-1 自己也寫「關閉狀態比留言數重要十倍」，指令卻要留言全文。
**修法（B-1／B-3 第 1 步逐字）：**
```
gh issue view <號> -R anthropics/claude-code --json state,stateReason,closedAt,comments \
  -q '{state,stateReason,closedAt,official:[.comments[]|select(.authorAssociation=="COLLABORATOR" or .authorAssociation=="MEMBER")|{login:.author.login,body:.body[0:400]}]}'
```
第 2 步（CHANGELOG）語法實測可用：`gh api repos/anthropics/claude-code/contents/CHANGELOG.md -H "Accept: application/vnd.github.raw"`，grep `^## 2.1.277` 拿到的三行與 verified L38 逐字相符。

### 🟡-3 `check_wiki_freshness.py:65` 硬編「產品化矩陣同步」
該檔第 64–65 行把 `topics/official-community-gap` 的維護來源寫成字串 `".claude/reporter-rules/features/daily.md 產品化矩陣同步"`。B-1 整節重寫會刪掉這五個字，而沒有任何 registry 配對看守 → 靜默漂移。該腳本又在 601a5b6e 宣告內。**修法（零風險側）：** B-1 新節內保留字面，起首寫 `**產品化矩陣同步（「官方補了沒」表）：**`。

---

## 二、機器

- **閘全綠且可複現**：自建「進頁面」暫存檔（9 個 fence、82 行）跑兩閘 → reader language 0、cell limits 0、最長格 110。設計者宣稱屬實。
- **registry／階層**：`check_rules.py` ✅、`check_hierarchy.py` ✅（改動前）。新表無 `#錨點` 出邊（map L26 把 `[[topics/model-comparison#…]]` 降為頁級），`build_web.py` 錨點 WARN 只會減不會增 ✅。
- **懸置基線**：188 不變，L92 定義＋新表第 3 列第 4 格短標記成對 ✅。
- 🔴-4 見下節（節名凍結宣稱不實，屬機器＋治理交界）。

### `check_verify_dates.py` 值不值得：**值得，但本波不做，且形狀要縮**
理由：現況確實零看守（`check_wiki_freshness.py` 只看頁層、`check_cell_limits.py` 只看字元、`check_pending_markers.py` 只看懸置——三句我都核過原始碼，屬實）。但它要掛 `run_tests.py`，而 SKILL 二明訂實作者不准改 `run_tests.py`；且 17 列裡 11 列核對日是 `—`，首跑必然一片紅。
**最小形狀（寫進 proposal「機制待辦」，下一波做）：** 只掃「核對日」欄，`—` 不算逾期只計數；逾 45 天 WARN、逾 90 天 FAIL；**照 `reader-language-baseline.json` 的先例帶存量基線**，首跑把現有 `—` 全數收進基線，棘輪只往下轉。沒有基線這一條，它會在落地當天被關掉。

---

## 三、冷讀者（拿原四題對 draft 走一遍）

| 原題 | 舊 | 新 | 判定 |
|---|---|---|---|
| Q1 AGENTS.md 讀不讀＋怎麼辦 | 2 跳半拿到 | 2 跳（index→claude-code:375 改 ✅）**拿到**，三個邊界即「怎麼辦」 | 改善；但 index 仍無互通性入口（跨維護者第 4 筆被延後），起點問題未動 🟡 |
| Q2 額度告警 | 3 跳半拿到 | 3 跳，官方側**拿到**（VS Code 70% 橫幅正面回答「事前告警」） | 「裝哪個」見 🔴-8 |
| Q3 哪些官方沒做 | 2 跳拿到 | 2 跳拿到，`❌` 排最上、三值有圖例、L66 同列打架消失 | ✅ 最大改善 |
| Q4 Dreaming 能不能用 | 5 跳繞 3 頁 | ⟨G-05⟩ 直接寫「Managed Agents 那邊、beta 內更受限的研究預覽、須另外申請」；死引用（`⏰ 倒數中`、`試用價值⏳觀望`）都拿掉 | 2 跳拿到 ✅ |

**官方事實逐列抽驗（每一列「官方給的是什麼」欄）：17 列全數對得上出處，無設計者自編。** 5 列有 verified 逐字背書（AGENTS.md／通知／額度／記憶／傳訊，核對日皆 2026-09-19）；12 列出自對象頁既有記錄且核對日誠實寫 `—`（模型路由、可觀測性、工作流腳本化、品質驗證、平台可及性、破壞性指令、Slack 等）。**無 🔴。**

### 🔴-7 表上引言第三行是分工條文洩漏進正文
A-4 L46：「issue 的留言數與讚數不記在這裡，那些住 [[entities/claude-code]]；本表只記 issue 號與它開著還是關了。」——這是寫給維護者的欄位歸屬條文，冷讀者第 4 節第 8 條抓過同型（index:88「為刻意設計差異」）。原則 7：條文住規則檔（B-1 已有），正文只留一句讀者語言。
**修法（A-4 第三行整行換成）：**
```markdown
> 每個 issue 現在多少人在吵、官方回了什麼，見 [[entities/claude-code]]。
```

### 🔴-8 「該裝哪個只留一個出口」不成立
proposal L15 宣稱冷讀者「兩頁兩答案」解掉。表上確實不列工具名了，但同一頁的 ⟨G-05b⟩（ltm／VIR／CoreMem／OKF／OzBrain／ambient-context／brain.md）、⟨G-07⟩（LimitBar、CCLimitPing）、⟨G-13⟩（Workweave Router、Dragoman、Council、Ungate、Rayline）仍在，且無日期、無「這是當時的快照」。冷讀者翻到細節區就又拿到第二組答案——他自己開的兩個選項，draft 只做了第一個。
**修法（A-4 圖例之後、或 `**缺口細節**` 標題下一行加一句）：**
```markdown
> 下面提到的社群工具是當時的代表案例，不是現在的推薦；要裝哪個一律看 [[topics/community-tech-tools]]「我卡在這裡」。
```

### 🟡-4／5／6 撐不起或維運口吻的三句（皆過閘，但屬原則 4／7）
- A-4 L45 核對日定義是「我們多久查一次」。**改**：`> 「核對日」＝這一列最後一次對過官方文件或 CHANGELOG 的日期；`—` 代表還沒對過，要拿它做決定時建議自己再查一次官方文件。`
- A-5 L82「這幾段是本頁在別處找不到的東西」＝自我評語。**改**：整句刪，保留其後「但它們說的是**到目前為止**的理由，不是預言」。
- A-9 末則「兩張表併成一張」把頁面整理寫進時序（`整理語` 只掃 callout 故過閘，但精神相同，設計者 L145 自己也承認）。**改**：`- **同一個痛點不再有兩個互相打架的狀態**：先前「多模型路由」一處寫「官方無對應」、另一處寫「部分對應」，跨 session 記憶也有兩個狀態；現在每個痛點只有一個狀態，並標出最後一次對過官方的日期。`
- 🟡-7：A-4 第 6 列「門檻也不能自訂」去掉了 verified L47 的「推論：官方文件未見此設定，非官方明示沒有」。⟨G-07⟩ 有保留，表格格內建議加二字：`門檻似乎不能自訂`。

**17 列 × 5 欄讀得下去**：最長格 110 字元、第 4 欄平均約 45 字，`❌`→`🧪`→`✅` 排序讓讀者的行動集中在上半。可接受。

---

## 四、治理

### 去向表抽驗（開原頁核行號，8 段）
| 抽驗 | 結果 |
|---|---|
| L39 刪 → 家在 L198–200 | ✅ 原頁 2026-09-12 段確有 orca／spec-kit／comet 三則 |
| L43 刪 → Cowork 07-08／v2.1.196／Dreaming 分別在 L153／L106／L58 | ✅ 三處皆在；推薦案下 L106 刪但內容上移新表第 7 列、L107 上移第 12 列，均不消失 |
| L62 自承句保留 | ✅ draft L74「社群前驅稀薄、官方主導色彩強，放在這裡只供對照」 |
| L64 ⟨Q-02⟩ 短標記 | ✅ draft L60 第 4 格 `❓ 待查證 ⟨Q-02⟩`，與 L92 定義成對 |
| L92／L153 懸置原文不動 | ✅ 兩筆的家都還在，腳本 188 不變 |
| L77 ⟨G-05⟩ 393 字元拆成 ⟨G-05⟩＋⟨G-05b⟩ | ✅ 7 個工具名與 OzBrain／ambient-context／brain.md 機制描述一字不失 |
| L100 刪，官方對應五項「在 agent-stack 八卡各有家」 | 🟡-8 **備註不實**：`/loop`／`/batch` 全庫查無於 agent-stack，家在 `feature-radar:349` 與本頁 L116（留原處）。事實未消失，但 map 的歸屬寫錯，請改備註 |
| L79 死引用（`feature-radar ⏰ 倒數中`）修掉 | ✅ ⟨G-07⟩ 已改為 `/usage`／statusline／VS Code 三項事實 |

### 🔴-4 「節名未凍結已查證」不實，且推薦案破 topics 模板契約
proposal L89 宣稱三個節名在 `scripts/` 零命中。自跑 `grep -rn`，**命中 4 處**：
- `scripts/wiki_graph.py:62` —「目前結論」在 `TEMPLATE_HEADINGS`（模板標題上捲、不作錨定名）。改名後該節會變成圖上的錨定節點（後果良性，但宣稱錯）。
- `.claude/reporter-rules/page-templates.md:87` — **topics/ 頁面格式模板把 `## 目前結論` 列為必備節**；該檔只允許 `技術彙整` 依類別自訂名，不含本節。
- `.claude/skills/wiki-lint-reporters/references/dispatch.md:37／45`、`wiki-lint-sweeps/references/sweeps.md:178` — 三處 lint 步驟都以「補『目前結論』」派活，改名後找不到節。

**故我對裁決點 (2) 的意見：內容全換同意，改名反對。** 保守預設（節名留、位置不動）與推薦案（改名＋前移）之間取第三案，兩邊的好處都拿得到，且不必多開一份規則改動：
```markdown
## 目前結論

**官方為什麼還沒補**

上面四個 ❌ 裡有兩個、加上「花費估不準」這一面，原因不是「還沒排到」，而是官方的動機本身指向別的方向。……（以下照 A-5 原文）
```
**位置**：仍照推薦案前移到表格之後（位置不受模板與腳本拘束，map L79 已查證無錨點入邊）。若第二輪仍堅持改名，B 段必須加第四項：`page-templates.md` 的 topics 模板補一句「`目前結論` 亦可依議題自訂名，命名原則同 `技術彙整`」，並回掃 dispatch.md／sweeps.md 兩處措辭。

### 🔴-5 回掃清單漏一頁（跨維護者，社群）
自跑 `grep -rln "AGENTS.md" wiki/` 共 11 檔。proposal 第 6 節涵蓋 claude-code、coding-workflow-guide、feature-radar。**漏 `wiki/topics/community-tech-discussions.md:171／222`**：表列與細節條目都把 AGENTS.md 寫成「社群長期呼籲…跨平台已成競品共識」、狀態 `🌙靜候`、數字停在 08-27（385 則／6525 讚）。該頁是社群記者的（`community/daily.md:14`），必須走轉知。
**修法（跨維護者清單加第 6 筆）：** `→ **社群**：`topics/community-tech-discussions:171／222` 仍把 AGENTS.md 寫成進行中的社群呼籲；官方已於 v2.1.277（2026-09-18）原生支援、issue #6235 於 08-17 CLOSED/COMPLETED，請更新表列狀態與細節條目。`
🟡-9：`wiki/overview.md:73`（「已知問題持續累積（AGENTS.md…）」，主編週更自然覆寫）與 `topics/competitor-landscape.md:264`（2026-08-26 時序內的 36Kr 報導，屬歷史記錄）兩處建議只記進 `wiki/log.md`，不另開轉知。

### 🔴-6 同維護者回掃漏 5 筆，而且是本波 verified 自己證實的
verified 第二節列出 08-17／08-19 一次關掉的 issue。全庫掃 issue 號，`entities/claude-code`（功能記者＝同維護者）還有 **5 筆仍標 🔴 未修復**：
`:200` #24316（CLOSED/COMPLETED 08-17）、`:255` #14227（CLOSED/**NOT_PLANNED** 05-25）、`:256` #47023（CLOSED/COMPLETED 08-17）、`:379` #29006（CLOSED/COMPLETED 08-17）、`:380` #28322（CLOSED/COMPLETED 08-19）。
proposal 只列 `:375` 一筆，並說組頭統計「🔌 平台相容性（70 條未修復）」同批更新 +1 ——實際受影響的組頭不只一組（#14227／#47023 屬 🧠 記憶組、#29006／#28322 屬 🔌 組），數字不是 −1。
**修法：** 同維護者表加一列 —— `| `entities/claude-code:200／255／256／379／380` | 五筆仍標 🔴 未修復 | 依 verified 第二節改為 ✅ 已修復（附關閉日與官方怎麼答）；#14227 改 ⛔ 官方拒修（NOT_PLANNED，2026-05-25）；**只改狀態詞與一句官方回覆，不重寫條目**；同批重算受影響組頭的未修復條數 |`
（合乎 SKILL 五「同維護者鄰居只改入口句」的邊界：這是逐行狀態更正，不是重寫頁。）

### 保守預設是否真的保守
- **裁決點 (1)**：保守預設「留 `## 對照矩陣` 節、只剩 3 列」**不夠保守也不夠好**——它保留了第二套符號（`⚡`）與第二張表，正是本波要治的病，且那 3 列的內容在新表都有欄位可裝。**我支持推薦案（併）**；保守預設若真要用，至少得把 `⚡` 改寫成三值之一，否則圖例與表 2 再度打架。
- **裁決點 (2)**：保守預設（節名留、位置不動）安全但讀不到推薦案的效果；見 🔴-4 的第三案。
- 🟡-10：proposal L68 說 claude-code 有「三處引用本頁」（88／262／655），實為 **4 處**（另 `:666` 相關頁面清單）。只核對不改字，無害，但數字要對。
- 🟡-11：需主編補查 9 項齊全，第 6 項（四個 `❌` 列的否定證明）正對上健檢卡第 9 節「❌ 列舉證責任反了」，收得好。

---

## 五、照順序執行（實作單）

> 分岔標示：**〔決1〕**＝依裁決點 1；**〔決2〕**＝依裁決點 2；**〔協〕**＝需主 session 先協調 601a5b6e。

0. **〔協〕** 與 601a5b6e 協調 `features/pages.md`。談成 → 照下表全做；談不成 → 第 3 步不改節名、第 11 步 B-1 整項延後並在 ledger 記「頁面節名未動，規則檔待協調」。（🔴-2）
1. 標頭 A-1、callout A-2、摘要 A-3（保守案時同步改數字為 14／2／7／5）。可驗：`grep -c "2026-09-1" wiki/topics/official-community-gap.md` 首屏只剩一個日期口徑。
2. 新表取代 L47–67：表頭 5 欄、圖例三行（第三行用 🔴-7 修法、加 🔴-8 快照句）。**〔決1〕** 17 列或 14 列。
3. **〔協〕** 節名改 `## 官方補了沒`。
4. 缺口細節 A-6 七條改寫／拆條；確認 ⟨Q-02⟩ 短標記在新表第 3 列第 4 格。可驗：`python scripts/check_pending_markers.py` 仍 188。
5. **〔決1〕** 對照矩陣：併則整節刪（L96–108）；保守則只留 3 列並把 `⚡` 改寫成 `🧪`。
6. 技術彙整 L131／L135 事實更正；L139／L143／L161 三段搬出。
7. **〔決2〕** 目前結論：採 🔴-4 第三案（節名留、粗體小標、前移到表格後）＝ 推薦與保守都不必再分岔；若堅持改名，先做第 12 步的 `page-templates.md` 配套。
8. 相關實體 A-8 六條；時序 prepend A-9（末則用 🟡-6 修法）。
9. 跑閘：`python scripts/check_cell_limits.py --page official-community-gap` → `check_reader_language.py --page official-community-gap` → `check_pending_markers.py` → `gen_wiki_frontmatter.py` → `check_hierarchy.py` → `build_web.py`（錨點 WARN 不增）。
10. 同維護者回掃：`entities/claude-code:375` ＋ **🔴-6 的五筆狀態更正** ＋ 組頭統計重算；`coding-workflow-guide:134`。
11. **〔協〕** B-1（含 🔴-1 退場修法、🟡-1 滿載句、🟡-2 指令、🟡-3 保留「產品化矩陣同步」字面）。
12. B-2／B-3／**B-4**：🔴-3 的五項逐字同步（sweeps.md H1＋新節、SKILL.md 五處、wiki-lint/SKILL.md:15、cloud-runbooks/weekly-lint.md、registry patterns）。可驗：`python scripts/check_rules.py` 維持 ✅。
13. **〔協〕** 跨維護者轉知 **6 筆**（原 5 筆＋🔴-5）：`python scripts/pending_handoffs.py open --from 功能 --to 社群 …`。
14. **〔協〕** `wiki/index.md` 鉤子與互通性入口列、`wiki/log.md` Query／定稿條目。
15. `python scripts/run_tests.py` exit 0；proposal「機制待辦」記 `check_verify_dates.py`（最小形狀見第二節）。

---

## 自跑紀錄

`gh issue view 6235 -R anthropics/claude-code --json state,stateReason,closedAt` → `{"closedAt":"2026-08-17T03:37:37Z","state":"CLOSED","stateReason":"COMPLETED"}`（exit 0）
`gh api repos/anthropics/claude-code/contents/CHANGELOG.md -H "Accept: application/vnd.github.raw"` → `## 2.1.277` 下第一行與 verified L38 逐字相符（exit 0）
兩閘：scratchpad `gate.py` 抽 draft A 段 9 個 fence 成 82 行暫存檔 → reader language 0 命中、cell limits 0 超限、最長格 110、表格 19 行。
`check_pending_markers.py` 188／基線 140；`check_rules.py` ✅；`check_hierarchy.py` ✅（18 個母頁）。
