# 第 20 波評審：topics/ai-agent-safety 拆成母頁＋三子頁（2026-10-30）

> 審的對象：`ai-agent-safety-2026-10-30-proposal.md`、`-proposal-map.md`、`-draft.md`；上游健檢卡、冷讀者、verified；ledger 2026-10-30 兩條裁決（七點＋N1–N4，不重開，只核有沒有照判）。
> 我的驗證腳本都在 `scratchpad\w20\review\`（下稱 `R\`），設計者產物在 `w20\design\`（下稱 `D\`）。我沒有改設計者的檔、wiki、`.claude/`，也沒跑 git。行號「原 Lnnn」＝原檔 2,057 行；「D-out」＝`D\out\wiki\topics\` 的改後全文。
> REVIEW-PRINCIPLES 依使用者 CLAUDE.md 不適用本流程（頁面 review 有自己的契約）。

## 結論

- 🔴 4 條、🟡 11 條。逐行搬家屬實：160 則節點、191 條時序我另寫一套切法逐字核，沒有丟、沒有重；懸置 203→202，−1 只有 #43713；錨點 0 BAD；首屏 11 列。
- 最要緊是 🔴2：pages.md 第 0 條的路由是「各頁收什麼」的列舉，跨類時只有一句「依讀者會來問哪一題」。設計者自己的落點已經打架：`.git` 節點住 A，B 的「目前結論」卻把它列為 B 的事、母頁也叫讀者去 B 找。
- 🔴4 是實作單第 5 步的驗收寫錯了。pending 基線檔停在 10-18（165 筆），`--rebuild-count` 印出來的會是 ＋79／−43，不會是「− 比 ＋ 多 1」，主 session 照單會卡住。
- 主 session 判定的行數是「總行−frontmatter」算的，沒扣 `%%`。照 page-lifecycle L25 與 `check_page_thickness.py` 的口徑，正文是 178／570／621／468。門檻判斷都不變：母頁 ≤300，B 仍逾 600，所以 B 還是要交代切法。
- **放行條件**：設計者第二輪吃下 🔴1–4，🟡 能吃就吃，不需要重開設計方向。

## 自己重算的數字

| 項目 | 主 session／設計者 | 我重算 | 證據 |
|---|---|---|---|
| 正文行數 母／A／B／C | 183／573／628／469 | **178／570／621／468**（扣 frontmatter 25 與 `%%` 5／3／7／1 行）；`check_page_thickness.py` 在 `D\tmp_after` 印 B＝621 | `R\count.py` |
| 節點 160 則 | 119→ABC、29→AR、12 骨架 | 148 則照 map 去向逐行找到、0 則重複；A 43／B 44／C 32（數 `####`）；改字的行全在 `subs.py`／`pattern_subs`，另外只有 L1646、L1682 拿掉「Topic Watch」，map 沒列 | `R\verify.py`、`R\tldiff.py` |
| 時序 191 條 | 47／55／36／E16／AR26／母6／改寫3／刪2 | 相同；A47／B55／C36、eval 3→19。所有映射行恰在目的頁出現一次 | `R\verify.py` |
| 「2 條刪」 | 與 eval 既有同事件 | 屬實。原 L1651 是 S-1 指標行，對 eval L283（10-27）；原 L1661 是對齊評估＋The Register 指標行，對 eval L286–287（10-24 兩條）。兩條原文都只寫「細節併入 eval」，沒有獨有事實 | 逐字比對 |
| 懸置 | 203→202，−1＝#43713 | 203→202；去掉 slug 後比對指紋，差集只有 `2026-10-11::43713…`、新增 ∅、非本家族頁 ∅。A 9／B 13／C 9，母頁 0 | `R\markers.py` |
| 首屏表 | 11 列 | 11 列（rm 列退場、#81138 補位） | `R\sections.py` |
| 網攻表 | 25→23（07-29、07-22 退場） | 25→23；剩下最舊一列 09-01 | 同上 |
| 錨點 | WARN 0→0 | 自寫解析器掃 `D\tmp_after\wiki`＋真 repo `daily/`、`weekly/`：0 BAD。daily 有 41 筆（技術彙整 38、其餘三個錨點各 1）；mythos L174、rsi L337、eval L83×3、log L7259、gov 5 筆（`eval#事件年表`×3、`eval#技術彙整`×2）、eval 4 筆 `product-vulns#2026-09` 全部能解析 | `R\anchors.py` |
| cell `--allow-grow` | 新增 2 | 新增 2（product-vulns「官方原文核心論點」625、prompt-injection「09-02 新增（媒體稱官方無修復計畫）」351）。但 `--rebuild` 會連帶移除 **254 筆**失效存量：本頁 105 筆，其中 100 筆今天就已失效；他頁 149 筆。見 🟡10 | `R\cells.py` |
| handoff 負責人 | 已驗 | 四筆 `--dry-run` 都過 | — |

**去向表抽驗**（從 map 抽六節＋三則，對照 D-out 逐字核）：網攻表 L126–158→C，33 行只有 map 列的 L140、L146、L155、L156、L158 不同。提示注入節 L89–123→A，只有 L106、L120 不同。拿什麼擋 L172–180→母，只有 L174 不同。舊分類骨架 L1569–1609→AR，41 行全同。05 月摘要→母，只有標題 L1558 不同。現況表 L55–73→母，只有 L64–67 不同。三則節點抽 L759（A）、L1202（B）、L984（C），本文逐字相同。L759 只有 map 列的「母頁「…」」替換，L1202、L984 一字未動。07／06 月：AR 收進 29 則節點與 26 條時序，逐行都找得到；archive 原文唯一的改動是標頭「最後更新」。「一字不刪」成立。

## 一、機器

**🔴1 #43713 節點結案了，下一行卻還寫「尚無官方回應」**
B 的 #43713 節點（D-out product-vulns L135–143）標題、安全意涵、✅ 結案行都改了，可信度評估（原 L465）沒改，還寫「尚無官方回應確認修補時程」，同一則前後矛盾。這是 verified 第 3 列沒有完整落地。修法：`subs.py` 加一行
`465: "- **可信度評估**：GitHub Issue 一手回報，41 則留言、👍 84；官方 2026-08-19 關閉並確認修好（見上方結案）",`

**🔴4 pending `--rebuild-count` 的驗收條件不可能成立**
`data/pending-marker-count.json` 是 10-18 的 165 筆。拿 `D\tmp_after` 模擬 `_do_rebuild` 的差集，會印出 added 79／removed 43（`R\rebuild_sim.py`），不是「− 比 ＋ 多 1」。修法：draft §H 第 5 步整列換成
`| 5 | 主 session | python scripts/check_pending_markers.py --rebuild-count --reason "第 20 波 ai-agent-safety 拆頁：#43713 主編查證結案（08-19 官方已修）；31 筆隨節點搬到三子頁（指紋含 slug，同數減增）；基線自 10-18 165 筆未重建，期間 ingest 淨增 38 筆一併入帳" | 先跑 python -I <scratchpad>\w20\review\markers.py <repo> <scratchpad>\w20\design\tmp_before\wiki <repo>\wiki：slug 無關差集 removed 只有 43713、added ∅、non-family ∅；rebuild 後 count＝202 |`

**🟡1 正文行數照規則口徑改**
B 頁的 `%%` 有兩處要改：標頭備忘「agent 自己越界的 16 則」改成 **14 則**（16 則裡 L1281、L1398 是 07 月，已蒸餾進 AR）；拆頁評估「正文 627 行」改成 **621 行**。proposal §1／§2、draft 行數表也照 178／570／621／468 改；ledger 定稿列用這組數字。

**🟡2 eval 新收的時序裡有 4 個自連**
D-out eval L290、L293、L307、L316 寫「詳見[[topics/ai-eval-boundary-incidents]]」，那就是本頁自己。修法：`pattern_subs` 在 dest=='E' 時加 `('[[topics/ai-eval-boundary-incidents]]','「## 技術彙整」')`。替換後變短，cell 閘不會擋。

## 二、明天的維護者

**🔴2 路由沒有寫成可執行的規則**（特別要查第 6 項）
第 18 波 patterns 的路由是機械判準：看節點關係行裡第一個逐字寫出的類別名。本波第 0 條是三頁各自的收錄列舉，跨類時只說「依讀者會來問哪一題」。設計者的落點已經證明這句判不出唯一答案：`.git` 節點（原 L964）住 A，但 B「目前結論」第 2 條把它列為「升版也還開著的」，母頁「產品層漏洞與誤操作」h3 也叫讀者去 B 找。照現在的寫法，記者明天遇到同類事件一定兩頭擺。修法：draft「進規則檔」A 的第 0 條，表下第一條換成
`- **一則事件只住一頁，依序問，第一個「是」就定案：** ① 發生在評測環境裡（AISI、廠商自揭的評估事故）→ \`topics/ai-eval-boundary-incidents\`；② 主角是模型的攻擊能力、官方資安防護研究與計畫、防守方准入、有人拿 Claude 打第三方、或非資安的政策表態 → \`topics/ai-agent-safety-cyber\`；③ 攻擊者把指令放進代理會讀的內容（網頁、repo 檔案與設定、MCP 回應、記憶、標頭、下載檔），或在談注入擴散 → \`topics/ai-agent-safety-prompt-injection\`，該產品之後出了修補版也一樣；④ 其餘 Claude 產品的漏洞、供應鏈、誤操作、agent 在真實環境越界、帳號與憑證 → \`topics/ai-agent-safety-product-vulns\`。四問都答不出，才寫母頁 \`### 未歸類\`。別頁要提它就寫 \`[[topics/<子頁>#YYYY-MM]]\`。`
設計者第二輪要拿 119 則節點照這四問跑一遍，落點有變的列進 map §二。我抽了 llms.txt、Downloads、`.git`、Auto 讀網址、Haiku 5.5 注入防禦（A），Keyv npm、#81138、deny-list、SneakPeek、MCP SDK（B），CVP、Glasswing（C），全部和現在的落點一致。
另外 B「目前結論」第 2 條（D-out L36）的「正常 clone 不受影響）」後面補 `（證據在 [[topics/ai-agent-safety-prompt-injection#2026-09]] 09-02 條目）`，補完約 170 字，不到 200。

**🔴3 母頁每日能動的東西和 page-lifecycle 母頁契約衝突**
page-lifecycle L52 規定母頁每日「唯讀，除三樣：callout、分支目錄表、懸置加訊」。pages.md 新 §1 的標題寫「只准動三樣」，但它實際列了五樣：callout、路由表最後動態、現況表每日覆寫、懸置加訊、`### 未歸類`。現況表每日覆寫有它的道理（母頁使命就是「現在什麼會打到你」），但兩份規則檔不能各說各話。修法有兩處：
- page-lifecycle L52 中格換成 `**唯讀**，除三樣：頂部 callout（覆寫）、分支目錄表、既有懸置標記加 \`訊\`；另外，母頁本身就是現況表的，該表照它的規則檔每日覆寫（現有：\`topics/ai-agent-safety\` 的 \`## 現在還擋不住的攻擊\`）；判不出的節點寫進 \`### 未歸類\`（見下方「路由」）`。page-lifecycle.md 加進 draft「進規則檔」與 `D\out\rules\`，F 節那句「不用改」刪掉。
- pages.md §1 標題改成 `### 1. 每日（母頁只准動五樣）`；第 3 條開頭改成 `母頁除 callout 與 \`### 未歸類\` 外，只准再動：`。

**🟡3 `.git` 第二變體「至 2.1.252 未修」沒有家**
這個數字只出現在母頁現況表與 B 目前結論，節點裡沒有（A 節點原 L974 只寫「另一條執行路徑仍未修補」）。修法：`subs.py` 加
`974: ["  - 修補狀態：…（原句不動）", "  - 2026-10-30 查證（CSA 09-04 研究註記轉述 Manifold，二手）：Claude Code 第二變體（ultrareview）至 2.1.252 仍未修；正常 \`git clone\` 不重現"],`

**🟡4 pages.md 的子頁規則有三處漏字**
- §1 第 1 條「prepend 進該子頁 `## 技術彙整` 當月節最上方」後面補 `（當月節還沒有就在說明句下新開 \`### YYYY-MM\`）`。
- A §1 寫「週更整段重判」，B、C 沒寫節奏，三頁也都沒登記觸發邊。修法：sweeps 5i 新段落在「母頁 `## 三類各自走到哪`」那句前插 `三個子頁的 \`## 目前結論\` 逐條對照本週新節點，答案變了才改該條。`，B、C §1 末句補 `週更見 sweeps 5i`。
- ledger 裁決 (6) 寫「子頁蒸餾進同一 archive 月節**並標群**」，§5 漏了「標群」。修法：§5 第一條末加 `，搬進的節點標題末尾加子頁短名（〔提示注入〕／〔產品漏洞〕／〔網攻〕）`。本波 07／06 月是拆頁前從母頁蒸餾，不追標。

**🟡5 四筆 handoff：第 1 筆行號錯**
`entities/claude-code` 現檔的 `.git` 列在 **L244**，不是 L238（L238 是 GitHub Actions RCE）；Plugin4Shell 在 **L236**，不是 L234（L234 是 #28240）。修法：note 裡的「L238」「L234」改成 L244、L236，並各補一個標題片段（「惡意 `.git` 設定檔」「Plugin4Shell」），對方檔案先動了也找得到。其餘三筆：給誰、改哪行、為什麼都齊（mythos L174、market-signals L333、official-community-gap L158／L160 都核過原文）。

## 三、冷讀者（拿 D-out 從母頁走四題）

四題路徑都通。Q1：母頁「官方現在擋到哪」第一條。Q2：母頁「產品層」h3，再到 B 目前結論。Q3：C 目前結論「濫用，誰承認的」。Q4：母頁連到 C#防守方能申請什麼。下面幾條會在複驗時被點名。

**🟡6 母頁 callout 三則照抄 B，不是新規則說的「一句總覽」**
修法：D-out 母頁 L36–41 換成
`> **最新動態**（2026-10-29）`
`> - **產品漏洞三則**：#81138 稱 Claude Code 把 email 放進 prompt、再被帶給外部網站（三來源）；#53223 稱 CLAUDE.md 指令沒有強制力；內建瀏覽器元件遭攻破只有標題。細節見 [[topics/ai-agent-safety-product-vulns#2026-10]]。`
callout 日期不變，`check_hierarchy` 照樣綠。L64「判不出歸哪一頁的事件先放本頁…週更時分派」是維護者流程，改成 `%% … %%`。

**🟡7 現況表遞迴刪檔列的指路失效**
原 L68 那格寫「見技術彙整」，但母頁技術彙整已經沒有這一則。修法：`subs.py` 加 68，原句的「見技術彙整）」換成「見產品漏洞子頁 09-25 條目）」，格長 78→80。

**🟡8 冷讀者點名的內部用語，子頁裡還留 32 處**
A 有 Topic Watch 13 處（map 只改了 L234 一處），三個子頁合計「殼層」15 處、「原料」5 處（冷讀者外洩第 2–4 條）。修法：`pattern_subs` 對所有 dest 依序加下列替換，替換後都等長或變短：
`('Topic Watch／ai-agent-safety 定向','提示注入定向補抓'),('Topic Watch／ai-agent-safety、','提示注入定向補抓、'),('（Topic Watch/ai-agent-safety）',''),('Topic Watch/ai-agent-safety，','提示注入定向補抓，'),('Topic Watch／','提示注入定向補抓／'),('Topic Watch，','提示注入定向補抓，'),('原料僅殼層摘要','原文只有摘要'),('原料摘要','摘要'),('原料無可讀','原文無可讀'),('殼層摘要','只有摘要')`

**🟡9 子頁 A、C 缺「蒐集邊界」**
page-templates L26 規定：主題延伸到 Claude 之外的頁，標頭最後一行必填。A 收他家 agent 的注入，C 收 GLM 等他家模型的能力。修法：在「最後新聞更新」下一行加
A：`**蒐集邊界：** 以 Claude 與 Claude Code 讀進外部內容被塞指令的事件為主，另針對提示注入定向補抓（每天最多 3 則）；他家 agent 的注入事件只在補上新載體或新防法時收，其餘會漏。`
C：`**蒐集邊界：** 以 Claude 的網攻能力、濫用與 Anthropic 的防守方計畫為主；他家模型的網攻能力只在官方研究或同一篇報導拿來和 Claude 對照時才會出現。`
另外 C 網攻表 10-22 列（原 L135）「是否源自 10-09 CIDP」改成「10-08」（verified 第 7 列，只動日期，等長）。

## 四、治理

**特別要查第 1 項，verified 落地情形**：第 1 列（rm 退場、補 #81138）落地。第 4 列（`.git` 🔴 部分修補、受害面縮窄）落地，但數字沒有家（🟡3）。第 5 列（deny-list 列標「他人轉述」、母頁加官方立場）落地。第 6 列（Glasswing 改為官方計畫、129,000 改引官方頁，加 5,500、46/50）在 C 的節點、表格、時序三處都改了，其他 wiki 頁搜「資安公司 Glasswing」「使用政策全面收緊」零命中。L224／L230 v2.1.311 的 🔎 附 2.1.309 反證，落地。#43713 結案只差可信度那一行（🔴1）。
**ledger 有沒有照判**：(1) 三子頁、(2) 兩節下沉、(3) B2 併 B、eval 4 筆改指 B、(5) gov 5 筆改指 eval、(7) 先蒸 07，加上 N1–N4，都照判。(6) 的「標群」漏了（🟡4）。設計者偏離指示的地方（保留兩個 h3、07 月 4 則全文搬 AR）ledger 已經接受。

**🟡10 實作單有三處要改**
- 步驟順序和自己的可行性前提矛盾：前提寫「四筆 handoff 在同一個 commit」，§H 卻把 handoff 和 log 放在 commit 之後（第 8 步）。修法：handoff open 與 `wiki/log.md` Query 條目移到閘之前，add 清單補 `data/pending-handoffs.jsonl`、`wiki/log.md`。
- 第 4 步 `--rebuild` 的 removed 預期是約 254 筆：本頁 105 筆，其中 100 筆今天已失效；他頁 149 筆。全是收緊，合法；驗收改成「新增恰 2 筆，removed 全部是 `R\cells.py` 列的 unused」，不要逐筆人工核。
- 第 7 步「`git status` 無本波殘留」做不到：gen 每天會改全庫 frontmatter 的 `days_since_*`（`D\tmp_after` 有 132 頁變動）。改成「殘留只准是 frontmatter 數值漂移」。
- 補一個前置檢查：九個 wiki 檔與規則檔是整檔覆蓋。四個規則檔的換行符和現檔不同，不過 autocrlf=true，內容差異只有預期的那幾段。複製前跑 `git log d797af66..HEAD -- <這 15 檔>` 必須為空；不為空就改用 draft 的 diff 逐段套。

**🟡11 rm 列退場備忘的語意**
B 節點（原 L600 後）新增的是 `- %% 未列入現況表：…狀態翻 ✅… %%`。在 pages.md 第 2 條裡，「未列入現況表」的意思是「表滿被擠掉、日後可補位」，✅ 退場的不該掛這個標記。修法：改成 `%% 2026-10-30 依第 2 條退場（stable 已含修正、狀態翻 ✅），不是補位候選 %%`，前面的「- 」拿掉，網站上才不會多出一個空的條列點。

## 照順序執行（實作單）

| 步 | 誰 | 做什麼 | 驗 |
|---|---|---|---|
| 1 | 設計者（第二輪） | `subs.py`／`pattern_subs` 加 🔴1、🟡2、🟡3、🟡7、🟡8、🟡9（C 日期）、🟡11；D-out 直接改 🔴2 的 B 指路句、🟡6 的母頁 callout 與 L64、🟡9 的 A／C 蒐集邊界、🟡1 的 B 兩處 `%%` | `bash D\after.sh`：verify_split 印 `OK 160 則節點與 191 條時序`；cell 新增仍是 2 筆；pending 202；build_web 錨點 WARN 0 |
| 2 | 設計者（第二輪） | draft「進規則檔」：A 第 0 條換 🔴2 條文；§1 標題與第 3 條照 🔴3 改；§1 第 1 條、§5、B／C §1 照 🟡4 補；sweeps 5i 加子頁目前結論一句；新增 page-lifecycle L52（🔴3）；`D\out\rules\` 同步；119 則照四問重跑，落點有變的列進 map | `check_rules.py` 在副本上只剩檢查 6 紅 |
| 3 | 設計者（第二輪） | draft §G 第 1 筆行號改 L244／L236 並附標題片段（🟡5）；§H 照下列 4–13 步改寫；行數表改 178／570／621／468 | — |
| 4 | 主 session | `git log d797af66..HEAD -- <wiki 9 檔＋規則檔 6>` | 空；不空就改用 draft 的 diff 逐段套 |
| 5 | 實作者 | `D\out\wiki\` 九檔複製進 `wiki/` | `python <scratchpad>\w20\design\verify_split.py <repo>\wiki` 印 OK |
| 6 | 實作者 | `D\out\rules\` 六檔（含 page-lifecycle）複製 | `python scripts/check_rules.py` exit 0 |
| 7 | 主 session | `python scripts/gen_wiki_frontmatter.py` | index L126 投影含三子頁 |
| 8 | 主 session | `python scripts/check_cell_limits.py --rebuild --allow-grow --reason "第 20 波 ai-agent-safety 拆頁：2 筆存量條列隨節點原文搬到子頁（長度不變）；同批收緊已失效存量"` | 新增恰 2：product-vulns「官方原文核心論點」625、prompt-injection「09-02 新增（媒體稱官方無修復計畫）」351；removed 約 254 筆，全是失效存量 |
| 9 | 主 session | 先跑 `python -I <scratchpad>\w20\review\markers.py <repo> <scratchpad>\w20\design\tmp_before\wiki <repo>\wiki`，再跑 `python scripts/check_pending_markers.py --rebuild-count --reason "…"`（理由用 🔴4 那句） | 差集 removed 只有 43713、added ∅；rebuild 後 count＝202 |
| 10 | 主 session | §G 四筆 handoff 先 `--dry-run`、再 `open`；`wiki/log.md` 寫 Query 條目並帶四個單號 | `python scripts/check_log_handoffs.py` 綠 |
| 11 | 主 session | `check_hierarchy && check_pending_markers && check_reader_language && check_cell_limits && check_wiki_freshness && check_rules && build_web && run_tests` 用 `&&` 串起來一次跑 | 全部 exit 0；build_web 尾行「錨點 WARN 0」 |
| 12 | 主 session | 只 `git add` 指名的檔：wiki 9 檔＋規則檔 6＋`data/cell-limit-baseline.json`、`data/baseline-changes.jsonl`、`data/pending-marker-count.json`、`data/pending-handoffs.jsonl`、`wiki/log.md`、`docs/page-audits/ledger.md`；commit 後跑 `python scripts/devpractice_diff.py mark` | `git status` 殘留只准是 gen 改的 frontmatter 數值 |
| 13 | 主 session | ledger 定稿列（行數用 178／570／621／468）；`git fetch` 確認沒有新 commit 才 push | — |

## 實作複核（2026-10-30）

> 複核的對象：真 repo 工作樹（未 commit），對照 proposal「實作單（定稿）」第 4–11 步。原檔用主 session 的快照 `w20\main\orig\wiki\topics\`；我核過，它與 `D\tmp_before` 去掉 CR 後逐位元組相同。新腳本是 `R\verify2.py`（容許改字行，以相似度把它們找回來）和 `R\unm.py`。沒改任何檔，沒跑 git。

**結論：放行 commit。** 不擋 commit 的 🟡 有 3 條：兩條改 docs、一條改實作單驗收句。四條 🔴 都已落地，重算數字全對。

| 步 | 判定 | 依據 |
|---|---|---|
| 4 前置 `git log` 檢查 | 我沒能核 | 複核不准跑 git，由主 session 自證。工作樹裡只有預期的 15 檔、data 4 檔、log、gen 的 frontmatter 與 build_web 產物 |
| 5 九檔進 wiki＋`verify_split.py` | **偏離（驗收句無法執行）** | `verify_split.py` L16 從 repo 的 `wiki/topics/ai-agent-safety.md` 讀「原檔」，複製後那裡已是新母頁，腳本在 L78 報 IndexError。我改用 `R\verify2.py` 獨立重核，通過（見下表）。修法 🟡A |
| 6 規則六檔 | 照做 | 抽驗見下方 🔴 落地 |
| 7 gen | 照做 | index L126 投影含三子頁；`check_hierarchy` ✅ 31 個母頁 |
| 8 cell `--rebuild --allow-grow` | 照做 | 新增恰 2 筆，正是第一輪那兩筆（product-vulns「官方原文核心論點」625、prompt-injection「09-02 新增（媒體稱官方無修復計畫）」351）。removed 267＝本頁 105＋他頁 162，比設計時的 254 多 13 筆。現況重掃：基線外新增 0、未使用槽 0，所以全部都是失效存量，合法收緊。帳本末行 reason＝「第 20 波 ai-agent-safety 拆頁：2 筆存量條列隨節點原文搬到子頁（長度不變）；同批收緊已失效存量」 |
| 9 pending `--rebuild-count` | 照做 | 帳本 count 202、updated 2026-10-30。reason 寫了 #43713 結案（−1）、31 筆同數減增、基線自 10-18 165 筆未重建；和我給的句子措辭略有不同，四個要素都在 |
| 10 handoff＋log | 照做 | 四筆 note 與 draft §G 定稿一致：H-d06051 已改成 L670「stable 目前落差」、L244「惡意 .git 設定檔」、L236「Plugin4Shell」，並註明 `.git` 事件住 A；H-4dcafe、H-b16ef0、H-bf1dd0 逐字相符。log L8288 起的 Query 條目帶齊四個單號；`check_log_handoffs.py` ✅ |
| 11 閘 | 照做（抽跑） | 我重跑 hierarchy／pending／cell／reader_language／freshness，五道全綠；build_web 與 run_tests 用主 session 的結果 |

| 重算項目 | 主 session／設計者 | 我在真 repo 重算 |
|---|---|---|
| 160 則節點 | 119→ABC、29→AR | 148 則（另 12 則是骨架）照第二輪 map 都只有一個家：A 44／B 43／C 32／AR 29；87 行改字都能用相似度找回；相似度 <0.6 的 8 行全是 verified 的改寫（L197、L230、L234、L445、L458 標題、L462、L464、L541） |
| 191 條時序 | A48／B53／C37／E16／AR26／母6／改寫3／刪2 | 相同，零重複。找不到原文的只有預期那 5 條：L1651、L1661（刪）、L2041、L2043、L2044（併入 07 月總結） |
| 懸置 | 203→202 | 202；去掉 slug 比對，removed 只有 `2026-10-11::43713…`，added ∅，非本家族頁 ∅。B 14／A 9／C 8，L295 已隨 L290 搬到 B |
| 首屏表／網攻表 | 11／23 | 11／23 |
| 錨點 | 22 筆＋daily 41 | 全庫、daily、weekly 0 BAD。mythos L174、rsi L337、eval L83 三個、log L7259、gov 5 筆、eval 4 筆 `product-vulns#2026-09`、B 指 A 的 `#2026-09` 都能解析 |
| 正文行數 | 173／587／603／475 | `check_page_thickness.py` 給：母 173、A 587、B 603、C 475。B 的拆頁評估寫「正文 603 行」，數字一致 |

**🔴 落地抽驗**
- 🔴1：product-vulns L171 已改成「…官方 2026-08-19 關閉並確認修好（見上方結案）」。
- 🔴2：pages.md L41 是四問、先答「是」的定案。
- 🔴3：page-lifecycle L52 加了現況表例外；pages.md L45「只准動五樣」、L49「母頁除 callout 與 `### 未歸類` 外」，兩份規則對得上。
- 🔴4：帳本 reason 如上。
- 🟡8：三個子頁 grep「Topic Watch／殼層／原料」都是 0 筆。🟡9：A、C 的 L36 都有蒐集邊界。

**換頁的三則節點**
- L1229 落在 A L480，時序 L1920 在 A L614。
- L290 落在 B L113，懸置 L295 在 B L118。原檔就沒有它的時序行，這是既有缺口，不是本波造成。
- L1090 落在 C L375，時序 L1856 在 C L486。

**🟡A `verify_split.py` 拆頁後不能再跑**：L16 的 `REPO / 'wiki/topics/ai-agent-safety.md'` 換成 `Path(__file__).parent.parent / 'main' / 'orig' / 'wiki' / 'topics' / 'ai-agent-safety.md'`。這是設計者在 scratchpad 的檔，可改可不改；本波的驗收以 `R\verify2.py` 為準。
**🟡B map §五「母:294（L290 節點內）」那列**：去向欄「不動（節點到 C，仍指母頁該節）」改成「不動（第二輪節點到 B，仍指母頁該節）」。
**🟡C 實作單第 12 步的驗收句**：工作樹還有 build_web 產物 `web_reader/`（修改檔加上三個子頁的新 json），不在 add 清單內。把「殘留只准是 gen 改的 frontmatter 數值」改成「殘留只准是 gen 改的 frontmatter 數值與 build_web 產物 `web_reader/`（交給下一次 web rebuild commit）」。
