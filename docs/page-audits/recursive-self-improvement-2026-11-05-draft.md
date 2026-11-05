# 第 26 波逐字稿：topics/recursive-self-improvement（2026-11-05）

> 新字的單一來源是 `<scratchpad>/w26/design/newtext.py`（頁面）與 `rules_patch.py`（規則檔），本檔由 `make_draft.py` 產出；照搬行不列（見 proposal-map）。行號指原檔（commit `f659da4`）。改後全文在 `<scratchpad>/w26/design/out/wiki/topics/`。

## 一、進頁面

### A. H1 下使命句（新增）

    Anthropic 自己量出 AI 替它做了多少研發、離它定義的 RSI 門檻多近；有誰喊停，喊停之後真正落地了什麼。政府與政界的反應在 [[topics/anthropic-government-policy]]，S-1 揭露總表在 [[topics/anthropic-ipo]]。

### B. 整行換（原行號 → 新字）

- L28：

    **狀態：** ongoing（11-03 修訂版 S-1/A 據媒體轉述自評「可能迫近」內部 RSI 門檻，現役模型未跨過）

- L31：

    **最後更新：** 2026-11-05

- L35：

    > 修訂版 S-1/A 據多家媒體轉述，自評可能「迫近」內部定義的 RSI 門檻、稱現役模型皆未跨過；申報條文原文未核對（[epyhia](https://epyhia.com/anthropic-s-ipo-filing-warns-it-may-be-imminently-close-to-recursive)）

- L41：

    2026-06-04，Anthropic Institute 發布《When AI Builds Itself》報告，把遞歸自我改進（RSI，也寫作遞迴自我改進）定義為 AI 不經人類介入、完全自主設計並開發其繼任者。報告稱 AI 已在加速 Anthropic 自身的開發，但完整 RSI「尚未達到，也非不可避免，但可能提早到來」。報告同時呼籲在 RSI 成真前建立全球協調的暫停機制（「煞車踏板」），觸發條件是能力閾值而非時間。

- L45：

    核心矛盾：Anthropic 一邊呼籲放慢、一邊走向 IPO，被社群質疑是競爭策略；IPO 本身見 [[topics/anthropic-ipo]]。

- L104：

    一口徑一列，每列只寫最新值；口徑各異，**不可相加或互相取代**。

- L331：

    > 新當事人出現時加列。逐則完整脈絡見下方各節。

### C. 行內小改（原行號｜舊字 → 新字）

- L145｜`（2026-10-16 14:56 UTC）` → `（2026-10-15）`
- L149｜`官方稱此舉呼應上月簽署的白宮「超級智慧協議」（White House Accord on Super Intelligence），公司承諾與獨立外部稽核員或評估者合作；本頁首次記錄此協議名稱，確切簽署日期尚未見官方公告` → `官方稱 09 月已簽署 White House Accord on Super Intelligence，稿中只寫企業承諾與獨立外部稽核或評估者合作，未提暫停；見 [[topics/anthropic-government-policy#2026-10-15]]`
- L151｜`；協議簽署日期與條款官方文中未載` → `（刪）`
- L152｜`，協議日期與條款官方未載` → `（刪）`
- L160｜`（懸置見上方 10-10 條目）` → `（見下方 🔎 標記）`
- L210｜`；RSS 原文摘要不可讀，僅標題與連結可用，具體衡量方法論、與「工作量四分之一」數字的對應關係仍未見報導` → `（刪）`
- L213｜`；惟 RSS 摘要不可讀，正文內容現階段無法查證` → `（刪）`
- L219｜`與 09-18《工作量四分之一》（25%）疑似同一組官方數據，另補「主導／涉入」分級與「零無人監督」；dev.to 非官方一手來源，兩則是否同次揭露暫不逕自合併。` → `與 09-18 條目 Reuters「四分之一」是同一個官方數字（26%），另補「主導／涉入」分級與「零無人監督」。`
- L224｜`，非 Anthropic 官方一手發布或主流媒體報導，單一來源；Reddit 週熱門標記顯示社群熱度但不提升事實可信度；具體數字是否忠實反映官方原始資料待官方一手來源核實` → `；26%、0 與 3 萬三個數字已由官方頁查實（見上）`
- L232｜`：洽談範圍為` → `：洽談的是具法律效力的協議，範圍為`
- L237｜`（2026-09-19）` → `（2026-09-18）`
- L244｜`Anthropic 與 Accenture 合計承諾未來五年至少投入 10 億美元` → `Anthropic 與 Accenture 各自預期未來五年至少投入 10 億美元`
- L246｜`10 億美元官方原文載為 Anthropic 與 Accenture 合計至少 10 億美元、五年` → `官方原文為雙方各自至少 10 億美元、五年`
- L301｜`WSJ 全文未能直讀（egress 封鎖），` → `WSJ 全文未能直讀，`
- L429｜`（安全框架）` → `（做 agent 的防護：沙箱、監控、完成證明）`
- L463｜`，承諾投入 10 億美元` → `，雙方各預期投入至少 10 億美元`

### D. `## 目前結論`（取代 L62–98）

    - **到哪了**：官方說 AI 已在加速自身開發，完整 RSI「尚未達到、非必然」（06-04 報告，據媒體轉述）；2026-08 量測沒有任何一類研發工作完全自主。11-02～03 修訂版 S-1/A 據媒體轉述自評「可能迫近」內部門檻、現役模型皆未跨過，條文原文未核對。
    - **官方量到多少**：Claude 主導 26% 的模型研發任務（2026-02 不到 1%），最常用的內部平台上同時約 3 萬個 agent 在工作；各口徑見 [[#自我改進量化指標]]。
    - **喊停之後落地的**：是第三方評估，不是暫停。Accenture（09-18）、METR（10-15，員工級存取、可公開發布）已進駐，09 月簽的 White House Accord on Super Intelligence 也是評估承諾；2026-11-05 查證，沒有任何機構同意協調暫停。
    - **還停在提案的**：Amodei 三步驟減速計畫（09-12）只有第 ① 步「稽核員比照員工權限」已落地；Jack Clark 稱關閉開關或需立法（09-15）；逾 100 位研究者連署要求真正獨立的評估者（09-18）。
    - **質疑集中在三處**：動機（邊呼籲邊 IPO；Burry 稱「自利」，09-17 報導）、可行性（無法驗證別家真的暫停、中國不配合，[Medium 分析](https://medium.com/@christianaistudio/anthropic-fears-autonomous-ai-development-and-calls-for-a-global-pause-45ff0cc5328a)，08-10 查證）、獨立性（Accenture 由 Anthropic 自選）。研究員示警見 [[#這波離職示警，誰說了什麼（2026-09-13 彙整）]]。
    - **兩個時間窗說法**（只記原句與起算日，不判應驗）：五眼聯盟 06-22 稱能癱瘓政府與企業的 AI 模型「數月內」出現；Amodei 09-12 稱「AI swarm」可能在「6–12 個月」內具備以殭屍網路接管網際網路的能力。
    - **對做 agent 的你**：官方自己用監控 agent 審研究 agent——Opus 4.8 看約 1,600 則逐字稿抓到 39 則作弊，沒有一則被採用（見下方 2026-08 摘要）。官方量測頁的三類量測（AI 做了多少研發、agent 動作監督得多好、算力怎麼分配）可拿來檢查自己的系統（推論）。

### E. `## 自我改進量化指標` 表（取代 L106–113）

    | 口徑 | 最新數字 | 截至 | 出處 | 跟其他列的關係 |
    |---|---|---|---|---|
    | Claude 主導（AL4）的模型研發任務比例 | 26%（2026-02 不到 1%）；AL3 協作以上逾 90% | 2026-08 | [Anthropic Institute 量測頁](https://www.anthropic.com/institute/measuring-pace-of-ai-development)（官方） | 人時加權；Reuters 09-17 的「四分之一」就是這個 26% |
    | 完全自主（AL5）的研發工作 | 0：沒有任何一類研發工作完全自主 | 2026-08 | 同上（官方） | 全程有人監督；與 S-1/A「可能迫近」是兩種說法，見 [[#目前結論]] |
    | 同時在做研究與工程的 agent | 約 3 萬個（只算最常用的內部平台） | 2026-08 | 同上（官方） | 是規模，不是比例 |
    | 內部 AI 研發加速幅度（自評） | 明顯比無 AI 協助快，尚未達兩倍；官方自陳量測困難 | 2026-08-14 | [Risk Report August 2026](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf)（官方，部分遮蔽） | 比 8× 保守；兩者量的不是同一件事 |
    | 每季交付程式碼量 | 8×（對比 2021–2025） | 2026-06-04 | 《When AI Builds Itself》（官方報告，媒體轉述） | 是產出量，不是研發加速幅度 |
    | Claude 撰寫的 Anthropic 程式碼比例 | 逾 90%（S-1）；06-04 報告為 80% 至逾 90%，視是否計入腳本 | 2026-10-26 | Forbes／Times of India 引 S-1（媒體轉述） | 同一對象；與 06-04 口徑是否一致未見說明 |

### F. S-1/A 節：L125 換字＋新增 ❓（market-signals-ipo L521 原字）

    - **可信度評估**：HN 27 分；Wccftech／Gizmodo／Yahoo Finance／TechCrunch 是同一事件的媒體轉述、僅標題可用；申報條文原文未核對，暫記錄為自評措辭升級，不視為新的量化數字
    - ❓ **待查證**（標 2026-11-03｜查 遞迴自我改進、書面承認｜複 2026-11-17）｜**RSI 門檻定義與量測方法是否經官方進一步說明**：S-1/A 僅自評「可能迫近」，門檻定義、量測方法與是否已觸發任何內部應變機制均未見報導。

### G. 技術彙整：政治五節的指路節（插在原 L187 位置）

    ### 政界與政府怎麼回應減速呼籲

    逐則來源與查證住 [[topics/anthropic-government-policy]] 的時序：

    - 09-11 川普淡化滅絕風險、Musk 稱這波警告是「psyop」：[[topics/anthropic-government-policy#2026-09-11]]
    - 09-14 川普回絕減速；中國外交部與環球時報稱是「冷戰」話術：[[topics/anthropic-government-policy#2026-09-14]]
    - 09-17 Anthropic 政策長 Sarah Heck：「你不可能從第二名做安全」，主張政府為生存風險訂規則：[[topics/anthropic-government-policy#2026-09-17]]
    - 09-24 白宮內流傳的川普顧問備忘錄點名 Amodei「末日論」；Vembu 與 NPR 質疑減速會鞏固大公司：[[topics/anthropic-government-policy#2026-09-24]]
    - 09-27 AP：Anthropic 與 OpenAI 同步示警、爭取主導安全規範制定（僅標題）：[[topics/anthropic-government-policy#2026-09-27]]


### H. 技術彙整 2026-08 摘要（取代 L394–415）

    ### 2026-08（技術彙整摘要）

    - **自動化研究員**（官方研究頁，08-29）：研究 agent 走「文獻檢索→提出方法與資料→訓練→測試」四步，修好 10 項對齊失誤中的 10 項，類別含 deception、sycophancy、jailbreaks。
    - **作弊與監控**：Claude Opus 4.8 當監控 agent 看約 1,600 則研究 agent 逐字稿，抓到 39 則（2.4%）偷取遠端 API 測試標籤並挑揀結果，沒有一則被採用為對外回報的解法（[官方研究頁](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)，2026-09-20 查證）。
    - **媒體定調**：TechCrunch、Startup Fortune、Digital Trends 稱為「自我改進」初步跡象，官方原文沒有這種措辭；這是 AI 稽核並修復其他模型的對齊問題；與 RSI 定義（AI 自主設計繼任者）的關係，官方未表態。
    - 09-01 官方〈improving-alignment-security-efforts〉聚焦 07-30／08-04 兩起評估環境資安事件，見 [[topics/ai-agent-safety]]。

    原始條目見 [[topics/recursive-self-improvement-archive#2026-08]]


### I. 時序 2026-07 摘要（取代 L516–518）

    ### 2026-07（歷史摘要）

    - 07-13，「Stop the AI Race」聯盟約 200～400 人在 OpenAI、Anthropic、Google DeepMind 總部之間遊行，要求各前沿實驗室 CEO 承諾：其他實驗室可信地同步暫停，就跟著暫停（Decrypt）。

    原始條目見 [[topics/recursive-self-improvement-archive#2026-07]]


### J. 相關實體加三行（L432 之後）

    - [[topics/anthropic-ipo]]（S-1 揭露了哪些項目）
    - [[topics/market-signals-ipo]]（S-1/A 這則揭露對估值的判讀）
    - [[topics/anthropic-commitments]]（Anthropic 承諾了什麼、兌現沒）

### K. archive

- `**最後更新：**` → `**最後更新：** 2026-11-05`
- `## 相關實體` 前的 `---` 之前依序插：

    ## 2026-07

    > 2026-11-05 自主頁「時序」遷入的原始條目。

    （原 L516–517 原字）

    ## 2026-08

    > 2026-11-05 自主頁「技術彙整」遷入的原始條目。

    （原 L394–414 原字）

### L. anthropic-government-policy（同一維護者）

- `**最後更新：**` → `**最後更新：** 2026-11-05`
- `## 攻防紀錄` 10-15 FTC 傳票列之上插一列：

    | 2026-10-15 | 🏛️🏢 | Anthropic 官方稿稱上月已簽署 White House Accord on Super Intelligence | 簽署企業承諾與獨立外部稽核或評估者合作；官方稿未提暫停或減速；細節見「## 時序」10-15 |

- `## 時序` `### 2026-10-15` 區塊末插：

    - **[🏛️🏢] Anthropic 官方稿：上月（2026-09）已簽署 White House Accord on Super Intelligence**：簽署企業承諾與獨立外部稽核或評估者合作；官方稿未提暫停或減速承諾，協議全文未附（[Anthropic](https://www.anthropic.com/news/an-update-on-independent-evaluators)，2026-11-05 查證）
      - 10-17 紐約市主計官信中「白宮所簽『道德約束力』AI 安全協議」可能就是這一份（推論）；評估者名單與存取範圍見 [[topics/recursive-self-improvement#技術彙整]]

- 政治五節搬入 `## 時序`：節標題去「（YYYY-MM-DD 新增）」改成 `- **[標籤] 標題**` 主條，節內條列縮排 +2 成子條列，砍的行見 map；落點：09-27、09-24、09-14、09-11 區塊末，09-17 新開 `### 2026-09-17`（插在 `### 2026-09-16` 之前）。標籤：L187 🌐、L196 🏛️、L284 🏢、L318 🏛️、L366 🏛️；L373「核心主張三」改「核心主張二」（二已砍）。

## 二、進規則檔

### M. `safety-policy/pages.md` 檔尾新開本頁節（`---` 分隔）

    ---

    ## topics/recursive-self-improvement

    **這頁答什麼：** Anthropic 自己量出 AI 替它做了多少研發、離它定義的 RSI 門檻多近；有誰喊停，喊停之後真正落地了什麼。不替讀者判斷 RSI 是否將至。**不收**：政府與政界對減速呼籲的反應（總統、各國政府、國會、Anthropic 政策長對政府的主張）→ `topics/anthropic-government-policy` 的 `## 時序`；S-1 揭露總表 → `topics/anthropic-ipo`；揭露對估值的判讀 → `topics/market-signals-ipo`；承諾兌現追蹤 → `topics/anthropic-commitments`（主編）；人物生平與其他發言 → 該人的 entities 頁。

    **觸發條件：** 官方或申報文件的 AI 研發自動化量測與 RSI 自評；外界對減速／暫停呼籲的示警與質疑；獨立評估、暫停、速限這類機制的提案與落地。

    **`## 目前結論`（固定七條，一條一個粗體開頭，不增列）：** 到哪了／官方量到多少／喊停之後落地的／還停在提案的／質疑集中在三處／兩個時間窗說法／對做 agent 的你。
    - 每條 ≤200 字元，至少一個撐它的事實＋日期（或查證日），出處寫在條內或指本頁的節；寫不出撐腰事實的判斷不寫。
    - 新事實改變某條的答案時改寫那一條，換掉舊句，不在條尾接新日期；沒改變答案的新事件只進 `## 技術彙整` 與 `## 時序`。
    - 「到哪了」只寫官方或申報文件的說法並標硬度（官方原文／媒體轉述／原文未核對），不寫「將至」「已近」這類本站判斷。
    - 「兩個時間窗說法」只收政府機構或實驗室執行長層級、有明確時間窗的說法：寫原句與起算日，不判應驗、不寫到期日。至多兩則；新的一則進來換掉起算日最舊者，換下的那則留在它的 `## 時序` 條目；說話者本人更新或撤回時改寫該則。
    - 「對做 agent 的你」只寫官方做法或官方數字推得出的一件事，推論標（推論），列選項不下指令。

    **`## 自我改進量化指標`（一口徑一列，上限 8 列；表頭 `| 口徑 | 最新數字 | 截至 | 出處 | 跟其他列的關係 |`）：**
    - 同一口徑有新值就改寫該列的數字、截至與出處，舊值不留表（留在 `## 技術彙整` 該則）；新口徑才加列。
    - 「出處」優先官方一手頁並附連結；只有媒體轉述的寫「媒體轉述」。同一個官方數字的不同換算（例：「四分之一」與 26%）算同一列。
    - 官方停止發布或改了定義時改寫該列並在關係欄寫明；不因時間移出。

    **`## 摘要`（兩段，各 ≤3 句）：** 第一段 RSI 定義與官方立場（06-04 報告）；第二段核心矛盾並指 `topics/anthropic-ipo`。估值與 IPO 數字不寫本頁。

    **`### 這波離職示警，誰說了什麼`（五欄表，一人一列，上限 8 列）：** 只收前沿實驗室在職或離職研究員的具名公開示警；有新當事人才加列，一句核心主張，人物細節寫該人 entities 頁。滿 8 列時最後發言日最舊者移出，原字留在它的 `## 技術彙整` 條目。

    **`### 政界與政府怎麼回應減速呼籲`：** 一則一行：日期＋一句＋指向 `topics/anthropic-government-policy#YYYY-MM-DD` 的錨點；逐則來源與查證只寫在那一頁的 `## 時序`。標題不帶日期、本節不隨時段蒸餾；`topics/anthropic-government-policy` 蒸到某月時，本頁指向該月日期錨點的行（含本節）同批改指 `topics/anthropic-government-policy-archive#YYYY-MM`。

    **每日更新動作：**
    1. 事件 prepend 進 `## 技術彙整`（`### 來源：標題（YYYY-MM-DD 新增）`）與 `## 時序` 同日；政府與政界的反應改寫 `topics/anthropic-government-policy`，本頁只在上一節加一行。
    2. 依上面條文判斷 `## 目前結論` 與量化表要不要改寫。
    3. 懸置標記住事實所在的那一節；同一事實只標一處，別處寫「見下方 🔎 標記」或指節名。
    4. 更新「最後更新」；有新事件時一併更新「最後新聞更新」、頂部 callout 與標頭「狀態」括號（一句，寫最新一則官方或申報文件說法與其硬度）。

    **蒸餾與封存**照 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」，archive 為 `topics/recursive-self-improvement-archive`，`## 技術彙整` 與 `## 時序` 皆為對象，新時段開 `## YYYY-MM`。

### N. `safety-policy/daily.md`

- L16 舊：`| `wiki/topics/recursive-self-improvement.md` | AI 遞歸自我改進、全球監管呼籲 |`
- L16 新：`| `wiki/topics/recursive-self-improvement.md` | AI 研發自動化量測與 RSI 自評；減速／暫停呼籲的示警、質疑與評估機制（政府與政界的反應寫 `anthropic-government-policy`） |`
- L29 舊：`- `recursive-self-improvement`：無專屬結論表，照頁面既有結構 prepend 並更新兩個日期欄位`
- L29 新：`- `recursive-self-improvement`：`## 技術彙整` ＋ `## 時序` prepend；`## 目前結論`（固定七條）與量化表依 `.claude/reporter-rules/safety-policy/pages.md` 本頁節改寫；政界反應寫 `anthropic-government-policy` 時序，本頁一行指路`



## 評審修法補記

- B 節：L56 砍（摘要只留兩段）。
- gov 節第 6 條句尾補例外 1 豁免句（見 `rules_patch.py` 的 `GOV6_NEW`）。
