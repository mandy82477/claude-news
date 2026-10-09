# 第 18 波設計提案：topics/community-tech-patterns 拆成母頁＋七個子頁（2026-10-09）

> 上游：健檢卡 `patterns-2026-10-09.md`、冷讀者 `wave18-cold-reader-2026-10-09.md`、查證 `patterns-2026-10-09-verified.md`；代判見 ledger 裁決紀錄 2026-10-09（使命句沿用第 8 波、**Context 管理歸 B**、archive 不拆）。
> 機械產物全在 scratchpad `w18\`：`split_patterns.py`（搬家）、`verify_split.py`（獨立逐字核對）、`build_tmp.py`＋`run_gates.py`＋`final_validate.py`（臨時 repo 實跑閘）、`patch\`（第一輪 freshness 補丁，已由評審 `review\check_wiki_freshness_v2.py` 取代）、`patch2\`（讀者版去重）、`out\`（八頁輸出）、`out\generated\`（跑過 gen 後含 frontmatter 的八頁）。行號一律指現檔。

## 1. 推薦案

251 則節點一字不改，依「與既有模式的關係」行裡第一個逐字寫出的類別名（pages.md 第 0 條；主線 tag 句不算；零命中者依健檢卡 §3 歸群表）搬進**七個子頁**的 `## 技術彙整／### YYYY-MM`；F2 不併 F1。母頁剩 180 行正文：摘要、子頁路由表、模式概覽（錨點改指子頁）、跨群收斂、未歸類＋早期時段總結。slug 不帶 `-patterns` 後綴，理由見 §10。

## 2. 子頁清單（全部 `**上層：** [[topics/community-tech-patterns]]`、領域 🌐 社群、`kind: topic`）

| 群 | slug | H1 | 一句使命 | 涵蓋類別 | 節點／節點行 | 頁正文行 |
|---|---|---|---|---|---|---|
| A | `topics/community-multi-agent` | 社群做法：多 agent 怎麼分工與協調 | 多個 agent 怎麼分工、隔離、隔離之後怎麼協調、開到多大、怎麼停 | Multi-agent 架構、Agent 規模化、Loop 終止條件、確定性框架；帶學術對照／誰負責拆分／缺口追蹤三節 | 42／374 | 494 |
| B | `topics/community-memory` | 社群做法：記憶、CLAUDE.md 與 context | 讓 agent 跨 session 記得專案、CLAUDE.md 怎麼寫、context 怎麼不撐爆 | 記憶與知識管理、CLAUDE.md 管理、**Context 管理**、記憶保護 | 37／320 | 367 |
| C | `topics/community-cost` | 社群做法：token、成本與模型路由 | 省 token、看見花費、任務派給哪個模型 | Token / 成本優化、模型使用策略、預算控制 | 40／338 | 392 |
| D | `topics/community-skills` | 社群做法：Skills 怎麼寫 | skill 怎麼寫才會觸發、慣例與地雷、品質怎麼量 | Skills 設計、可靠性測試 | 39／350 | 403 |
| E | `topics/community-guardrails` | 社群做法：規則強制、審查與安全 | 讓 agent 守規矩、產出有人審、防亂來與洩漏密鑰 | Hooks、安全架構、多代理 PR Review、規格驅動、架構邊界合約、版本控制；帶查證備註、把關層彙整 | 32／272 | 348 |
| F1 | `topics/community-integrations` | 社群做法：MCP、plugin 與外部工具整合 | 接外部服務、工具與創作軟體，MCP 長連線怎麼不斷 | Plugin / MCP、MCP 長 Session、創意工具 | 38／340 | 387 |
| F2 | `topics/community-interfaces` | 社群做法：手機遠端、介面與 agent 可視化 | 從手機控制、換更好的介面、看見 agent 在做什麼 | 介面元件複用、行動裝置遠端、活動可視化、跨 Repo 依賴可視化 | 23／198 | 239 |

- 數字來源：`out\accounting.txt`（`split_patterns.py` 分段實數；節點行 2,192 比 nodes.json 的 2,208 少 16，差額＝兩個「懸置細節」區塊 3＋13 行，nodes.json 把它們算進最後一則節點）。
- 第二輪：第一輪用 nodes.json `cats[0]` 分群（不照文中順序、還把主線 tag 當類別），與自己寫的第 0 條不一致，7 則落錯頁（評審 🔴1）；改用 `first_cat()` 後 L641、L713、L1634、L1758、L2036、L2148、L2268 換子頁，上表已是新數字。
- 與健檢卡差異一處：skillcrossroads 那則（L992，Q3 的 69%）關係行第一個類別是「安全架構」，依規則住 E；D 的「慣例與地雷」引它並連 `[[topics/community-guardrails#2026-09]]`。不為它開例外，路由才是一條規則（pages.md 第 0 條）。
- 懸置：⟨Q-01⟩⟨Q-03⟩⟨Q-04⟩→E、⟨Q-02⟩→F1、⟨Q-05⟩→C、⟨Q-07⟩→A、⟨Q-06⟩ 留母頁；短標記與細節區同頁（`verify_split.py` 逐頁核過）。

## 3. F2 併不併：不併

1. **有自己的問題**：答得出——「能不能從手機控制」「怎麼看到 agent 在做什麼」是概覽 L69、L70 兩列的題，trends 趨勢八是獨立收斂的方向（trends L251）。
2. **有自己的結論與時序**：答得出——「先試官方遠端控制（trends L263 已寫官方確認可用），社群 bot／MCP／web-app 三路互不相通」是 F1 寫不出的結論；22 則跨 07-08～10-07。
3. **被獨立引用**：答得出（照精神）——trends 趨勢六、八依類別對照表（weekly.md L152、L154）撈的就是這一群，趨勢八啟示會連進來。
- 加一條不併的理由：F1 十月前 7 天就進 15 則（全群最多），併成 526 行後兩三週就再過 600 行。

## 4. 母頁剩什麼（`out\generated\community-tech-patterns.md`：205 行＝frontmatter 25＋正文 180）

| 節 | 行（正文） | 內容 |
|---|---|---|
| 標頭＋callout＋分隔 | 15 | 原文照留；「最後更新」改拆頁日，「最後新聞更新」不動 |
| `## 摘要` | 8 | 三段：本頁角色、定案四句＋「十六類裡 2026-09-25 起十類有動靜」（修掉 L44 對 L2438 的互斥）、官方唯一一手依據指路（pages.md §8(b)）、鄰頁分工 |
| `## 每一類做法住哪一頁` | 14 | 七列路由表（子頁｜答什麼｜收哪幾類｜最後動態）＋一句歸類規則 |
| `## 模式概覽` | 32 | 20 列＋圖例＋表下七類；只改錨點（§5）與表上說明一句 |
| `## 現在收斂到哪、哪些還在試` | 28 | 定案四類（原文）、七群各一句指子頁、成本跨群一條＋⟨Q-06⟩、還在試計數句；過渡 h3「缺口追蹤」一行 |
| `## 技術彙整` | 46 | 說明一行、`### 未歸類`（目前沒有）、`### 2026-07` 分住路由段＋`%%` 拆頁評估、05／06 時段總結原文 |
| `## 相關實體`＋`## 參考來源` | 37 | 原文照留 |

## 5. 模式概覽 20 列的錨點（照 pages.md 第 1 條「最後動態」定義重算，取那一則所在子頁）

Skills→`community-skills#2026-10`（L207）｜Multi-agent→`community-multi-agent#2026-10`（L261）｜Hooks→`community-guardrails#2026-10`（L405）｜CLAUDE.md→`community-memory#2026-10`（L549）｜Plugin/MCP→`community-integrations#2026-10`（L216）｜記憶→`community-memory#2026-10`（L198）｜Context→`community-memory#2026-10`（L243）｜Token→`community-cost#2026-10`（L297）｜模型→`community-cost#2026-09`（L623）｜PR Review→`community-guardrails#2026-09`（L1372）｜介面→`community-interfaces#2026-10`（L288）｜安全→`community-guardrails#2026-10`（L342）｜創意→`community-integrations#2026-10`（L369）｜行動→`community-interfaces#2026-10`（L378）｜可視化→`community-interfaces#2026-10`（L495）｜規模化→`community-multi-agent#2026-09`（L1073）｜規格→`community-guardrails#2026-09`（L1128）｜Loop→`community-multi-agent#2026-08`（L1709）｜MCP 長 Session→`community-integrations#2026-08`（L1780）｜架構邊界合約→**`community-skills#2026-08`**（L1796 第一類別是 Skills 設計，照規則落 D）。
表下 L79：版本控制→`community-guardrails#2026-07`、預算控制→`community-skills#2026-07`（L2140）、可靠性測試→`community-skills#2026-07`（L2236）；後三類刪掉指向 `#2026-07` 的空錨（關係行零命中，只剩 archive#2026-06）。
腳本另發現：L62 Context 列「最後動態」寫 10-07，照定義算是 10-06（L243）——不屬本波，留給週更重算。

## 6. 搬家的機械方法

- **腳本**：`scratchpad\w18\split_patterns.py`（只讀 wiki，輸出到 `w18\out\`）。分段 L183–2402 成節點／懸置細節逐筆；每行原文必須恰被消費一次，否則 assert（L219–248）。模板 `w18\tpl\*.md` 用 `@@L a-b`（照搬）、`@@LS a-b`（照搬＋替換表 `SUBS`，L115–146；歸群 `first_cat()` L40）、`@@NODES`。
- **獨立核對**：`verify_split.py` 用另一套分段比對 251 則全文：「251 則全數出現恰一次；允許差異 1 則」＝L346 WaLiAPI 節點內的 `#2026-10` 改指 E（它指的 ThinkWatch-Lite L360 住 E），這是 251 則裡唯一被動到的字元。
- **行數對帳（正文 2,461 行）**：照搬留母頁 107＋照搬進子頁 2,289＋替換後搬 37＋包裝行丟棄 16＋改寫 12＝**2,461，相等**。
  - 包裝 16＝`## 技術彙整` 標頭與說明 4、四個月份標題＋空行 8、兩個「懸置細節」標頭／尾空行 4（子頁各自重建）。
  - 改寫 12＝L32、L44–46、L52、L79、L81、L91、L110–111、L2432、L2438（逐行理由在 `accounting.txt`）。
  - 輸出正文 2,810 行＝原文 2,433＋新寫 296＋包裝重建 81；比拆前多 349 行。

## 7. 外部錨點與入邊

| 出處 | 現指 | 新目標 | 誰改 |
|---|---|---|---|
| discussions L314 | `#2026-09`「Skills 設計」（reladraw，L725） | `[[topics/community-skills#2026-09]]` | 同維護者，只改連結 |
| discussions L321 | `#2026-09`「創意工具」（chess-postmortem，L755） | `[[topics/community-integrations#2026-09]]` | 同上 |
| discussions L858 | `#技術彙整` | 句子改「逐則證據依類別分住七個子頁，入口見 `[[topics/community-tech-patterns#每一類做法住哪一頁]]`」 | 同上 |
| LCW L72／L95／L122／L126／L149 | 整頁 | A／B／B／B／E（omnigent L1887、nightshift L1165、session-indexer L2228、claude-mem L1463、interns-review L1372 的落點） | 同上；L43 留母頁 |
| coding-workflow-guide L478 | `#2026-07`（合併佇列 L2044） | `[[topics/community-multi-agent#2026-07]]` | **轉知開發實務**；未改前落在母頁過渡 `### 2026-07` |
| official-community-gap L41 | `#缺口追蹤：…` | `[[topics/community-multi-agent#缺口追蹤：文獻主張 × Claude Code 現況]]` | **轉知功能**；未改前落在母頁過渡 h3 |
| claude-skills L116 | 整頁「如何寫 skill…皆記錄於該頁」 | `[[topics/community-skills]]`「慣例與地雷」；「74 個 skill」全樹查無 | **轉知功能** |

轉知 3 筆（dry-run 2026-10-09 驗過負責人，單號以實跑為準：H-f55a2c／H-9d1672／H-817203），指令逐字在 draft「進規則檔」§G。index 三處（L69、L113 鉤子、L32 後加兩列）是主編自己的頁，不轉知。

## 8. 閘（實作者在真 repo 跑；我已在臨時副本 `w18\tmprepo` 全跑過，log 在 `final_validate.log`）

| 閘 | 副本結果 | 看守什麼（行號） |
|---|---|---|
| `check_hierarchy.py`（支援 `[wiki_dir]` 位置參數，L159） | ✅ 31 個母頁；未跑 gen 時驗紅：「index 投影缺子頁」 | 上層存在 L105、領域繼承 L121、hub callout ≥ 子樹新聞 L137、投影 L150 |
| `check_pending_markers.py` | ✅ 152 筆（基線檔 131，2026-10-03） | 指紋鍵含 slug L238 → 3 減 3 增；計數閘只擋減少 L306，總數不變所以不擋；同頁雙向對帳 L186 |
| `check_wiki_freshness.py` | 現版**紅**：7 子頁「無從對照」；套評審 v2（`w18\review\check_wiki_freshness_v2.py`）後 ✅ | 見 §9 |
| `patterns_tree_audit.py`（新增，唯讀、不進 run_tests） | ✅ OK；第一輪分群跑出 7 則、exit 1（評審驗紅） | 母頁 ≤300 行、母頁技術彙整無節點回流、節點落點對第 0 條 |
| `check_reader_language.py` | 白名單兩筆 `page` 改子頁後 ✅（不改＝3 筆新增） | 白名單比對 L263 以頁為鍵 |
| `check_cell_limits.py` | `--rebuild --allow-grow --reason` 後 ✅：新增恰 66、全在七子頁，母頁 66 移除 | 基線以頁為鍵；新增須帳本 L438 |
| `build_web.py` 錨點 | 錨點 WARN 0→0；驗紅：不改 discussions、拿掉母頁兩個過渡錨 → 4 | `check_wikilink_anchors` L369–390 |
| `test_index_sync` | ✅（子頁靠投影過 L65–83） | |
| `check_rules.py` | 副本無法跑（讀 `.claude/`）；實作者改完規則檔照跑 | registry sync_pairs[39] 兩個 pattern 仍在 daily／weekly |

- pending 不需 `--rebuild-count`：若同期別的 session 結案標記導致計數閘紅，rebuild 理由寫「第 18 波拆頁：3 筆正式標記隨節點搬到 community-integrations／community-guardrails，指紋鍵含 slug（check_pending_markers.py L238）改變，非結案」，並核對印出的 −／＋ 恰為 auto-undo、Certified Architect、silent failure 三對。
- **新增錨點**：七子頁各 `## 摘要`、`## 目前結論`、`## 技術彙整`、`### 2026-10/09/08/07`；A 另有學術對照三節；D 有 `## 慣例與地雷`；母頁 `## 每一類做法住哪一頁`、`### 未歸類`、過渡 `### 2026-07` 與 `### 缺口追蹤：…`。舊錨點全數改指或有過渡落腳，所以 WARN 不增。

## 9. 撞到的第二個問題（freshness 兩處假紅，修法在 draft §F）

- **根因**：`check_wiki_freshness.py` L184–197 對母頁拿「子樹歸因」同時判第 1、2 類。歸因帳本 append-only、以寫入當時的頁為鍵，拆頁不搬帳——子頁拆出當天零歸因（第 2 類紅）；拆後新聞落子頁、母頁「最後新聞更新」照母頁契約不動（page-lifecycle L55），第 1 類就判母頁「漏更」。
- **證實**：`w18\fresh_sim.py` 同一組輸入跑修前修後：修前「拆頁當天」exit 1（7 頁）、「隔天子頁進新聞母頁不動」exit 1（母頁漏更＋6 頁）；修後兩案 exit 0；現行全庫（未拆）修前修後都 exit 0。第一輪四案測試已換成評審 v2 五案（`review\test_wiki_freshness_hierarchy_v2.py`，第 5 案見 draft §F）。
- **修法（第二輪定稿＝評審 v2）**：第 1 類只比自己的歸因；第 2 類「自己／子樹／上層」三處任一撐得住才放行，上層歸因**只在那筆的 `item_url` 出現在本頁正文**時才算，且宣稱日不晚於它。第一輪版本不比網址，會放過「活躍母頁下的新子頁漏報歸因」（評審第 5 案）。沒有這條，拆頁 commit 會擋 web build（run_tests 掛 freshness）。

## 10. 不選的方向

- **按月拆**：拆出來是 log 不是故事（page-lifecycle L25、L31）。
- **按成熟度拆**：✅⚡⏳ 會隨時間移動，節點得反覆搬家；也不是讀者問的題。
- **只蒸餾不拆**：07 月全蒸也只減約 423 行，仍逾 2,000 行（L27「蒸餾與拆分各管各的」）。
- **F2 併 F1**：見 §3。
- **每個子頁各開 archive**：ledger 裁決不拆；archive 按月封存，與分群無關。
- **slug 帶 `-patterns` 後綴**：實測概覽表四格（Multi-agent、Plugin、介面、行動）超過 120 字元（check_cell_limits 判新增），所以用短 slug。
- **Context 歸 C**：ledger 代判 B；使用者翻案時改 `w18/common.py` 的 `CAT` 與 pages.md 第 0 條兩列、重跑腳本並改 B／C 兩頁導言。

**可行性前提**：freshness 修法、cell 基線 `--allow-grow`、白名單兩筆、gen 投影、規則檔四處與八頁搬家在**同一個 commit** 進去並 push（page-lifecycle L68–70）；任一缺，run_tests 或 web build 當天紅。

## 11. 最不確定的一件事

每日記者照第 0 條把新節點寫進對的子頁。第二輪加了 `scripts/patterns_tree_audit.py`，週更第 4 步會抓出關係行有類別名卻住錯頁的節點；但 64／251 則今天關係行就沒有類別名，那一類只能靠記者判斷，腳本不判。錯一週才被抓到，讀者會先看到一週的混群。

## 第二輪：逐條回應評審（`patterns-2026-10-09-review.md`）

接受 11、改寫 1、反駁 0。評審事實我逐條重核過（命令與結果在括號）。

| 條 | 處置 | 怎麼改、在哪 |
|---|---|---|
| 🔴1 分群≠第 0 條 | 接受 | 重核 L2268、L1634 關係行屬實；`split_patterns.py` 換評審 `first_cat()`、SUBS[139]／[2434] 指 A、D 開始日期 07-12；重跑後 A42／B37／C40／D39／E32／F1 38／F2 23、對帳仍 2,461；draft A2 補口徑句與泛化例；map 月份分布與 L139、L2434 列改 |
| 🔴2 freshness 放寬過頭 | 接受 | 採 v2；draft §F 換成三處 diff 與五案說明（我重跑：現版 2 FAIL、第一輪補丁 1 FAIL、v2 5 OK） |
| 🔴3 子 agent 改不了閘檔 | 接受 | 重核 `guard_roles.py` L48–53、L76–77 屬實；draft §H 標「主 session」：第 9–14 步（9 freshness、10 allowlist、11 gen＋cell rebuild、12 跑閘、13 commit、14 轉知與 push） |
| 🟡4 cell rebuild 順帶收緊 64 筆 | 接受 | draft §E 補核對句與 commit 訊息要求 |
| 🔴5 母頁也報歸因會紅 | 接受 | draft C（daily.md L13）補「歸因一律記子頁、母頁 callout 不報」＋例題 |
| 🟡6 母頁契約無看守 | 接受 | `scripts/patterns_tree_audit.py` 掛 weekly 第 4 步開頭；回報格式加一行「patterns_tree_audit：OK ／ ❌ N 則（落點錯 a、母頁回流 b、母頁超 300 行 c）→ 已修」 |
| 🟡7 路由表最後動態無定義 | 接受 | draft A2：＝子頁「最後新聞更新」照抄 |
| 🟡8 收哪幾類是第二份副本 | 接受 | draft A2 與 weekly 第 4 步：＝第 0 條該列 ∩ 目前概覽表上的類別，週更照抄 |
| 🟡9 D 慣例第二條違反 A12 | 接受 | A12 入口補 discussions「現在吵到哪」已不再爭的結論 |
| 🟡10 讀者版印兩次 | **改寫** | 評審的過濾會把「有子頁同日 callout」的母頁整項略過，連母頁自己的新聞（如 anthropic-agent-stack 有自己的新聞、managed-agents 同日也有）一起吞掉。改成只略過「callout 連到同日有 callout 的子頁」的母頁項；daily 規則已要求母頁 callout 連子頁。draft §I；合成資料驗過（修前 4 項、修後 3 項、不連子頁的母頁保留），真資料驗證列為實作單第 12 步 |
| 🟡11 過渡標題退場只在 `%%` | 接受 | weekly 第 4 步末加 `wiki_graph.py explain … --section` 入邊為 0 就刪 h3（社群記者做）；`### 2026-07` 在 07 蒸餾時改指 archive；draft §H 末寫明 |
| 🟡12 轉知漏 L669 | 接受 | 重核 coding-workflow-guide L669 屬實；§G 第一筆 note 補句 |

定稿數字：子頁正文 A 494／B 367／C 392／D 403／E 348／F1 387／F2 239，母頁 205 行（正文 180）；對帳 107＋2,289＋37＋16＋12＝2,461；八頁正文合計 2,810。第二輪副本全閘（v2 freshness、allowlist、cell `--allow-grow` 新增 66、tree audit）exit 0，錨點 WARN 0→0（`w18\final_validate.log`）。實作單 14 步，主 session 做第 9–14 步，第 1–2 步是設計者、已完成。
