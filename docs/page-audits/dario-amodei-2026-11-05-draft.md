# 第 27 波逐字稿：entities/dario-amodei（2026-11-05）

> 新字的單一來源是 `<scratchpad>/w27/design/newtext.py`（頁面；網址常數在同目錄 `urls.py`）與 `rules_patch.py`（規則檔），本檔由 `make_draft.py` 產出；照搬行不列（見 proposal-map）。行號指原檔（commit `d6afcdb`）。改後全文在 `<scratchpad>/w27/design/out/wiki/entities/`。

## 一、進頁面

### A. 標頭下使命句＋唯一一則 callout（取代 L40–44；L40–41 原字隨 08 月進 archive）

    本頁回答：他是誰、現在公開主張哪幾件事（各附本人原文出處）、誰在公開反對他、與白宮的關係走到哪；主張的論證與後果在各議題頁。

    > **IPO 申報文件：公司 2025 年花約 275 萬美元保護他**（2026-10-29）
    > Fortune 報導（經 [Google News](https://news.google.com/rss/articles/CBMivwFBVV95cUxONTFYMkE3VElIM3Q5QlM3Q3FZSlJXQ2ExZDJwMkdqdmVTenZ0X0pwVXNkTHAwc2lBdkh0NVcxVENFN3Z0S21TZ3E0YWZ1UmZKdlZpc1Nsb0plTWRzU3dsZ05oX1dDX09yamJVWjN5bTRCeV95V0pnNjItWW91MC1Lak9ob3o5c2hGeERMOTJMdzNfSUgxQWdIR0tBeHd0d19XaVZPQkdGLWw3aC1mbTF2bUo3YlBiTkM1VVRpcXFUVQ?oc=5)），引 IPO 申報文件：2025 年 Anthropic 為 Amodei 支出約 275 萬美元人身安全費，是他底薪 65.4 萬美元的四倍多、約佔總薪酬 1,800 萬美元的 15%；金額細項見 [The Next Web](https://thenextweb.com/news/dario-amodei-security-cost-philanthropy-pledge-anthropic-ipo)。

### B. 整行換（原行號 → 新字）

- L37：

    **最後更新：** 2026-11-05

- L104：

    有人物頁者的原話與來源見各人物頁；按論點（動機、可行性、獨立性）整理的質疑見 [[topics/recursive-self-improvement#目前結論]]。

- L115：

    - [[topics/anthropic-government-policy]] — 政府 AI 監管立場與白宮關係；Chris Olah、Tom Brown 等共同創辦人在政府關係線上的角色見 [[topics/anthropic-government-policy#誰在動這幾條線]]

- L117：

    - [[topics/recursive-self-improvement]] — 09-12 減速文章的論證、三步驟與按論點整理的質疑；Anthropic 內部 AI 自動化的量測現況見 [[topics/recursive-self-improvement#自我改進量化指標]]

- L152：

    - [Musk and ChatGPT CEO back calls to slow down development of AI](https://www.itv.com/news/2026-09-12/musk-and-chatgpt-ceo-back-calls-to-slow-down-development-of-ai) — ITV，2026-09-12：Musk、Altman 表態支持減速呼籲

- L156：

    - [Anthropic CEO says AI backlash is 'fundamentally a crisis of trust'](https://techcrunch.com/2026/08/16/anthropic-ceo-says-ai-backlash-is-fundamentally-a-crisis-of-trust/) — TechCrunch，2026-08-16：回應投資人 Gavin Baker 於 All-In podcast 及 X 上的批評

- L158：

    - [Quoting Dario Amodei](https://simonwillison.net/2026/Aug/16/dario-amodei/) — Simon Willison Blog，2026-08-16：全文引述 Amodei 在 X 上談信任危機、治癒癌症的貼文（本人原文）

- L161：

    - [How Dario Amodei Spread Anthropic's Religion and Stirred Up Silicon Valley](https://www.theinformation.com/articles/dario-amodei-spread-anthropics-religion-stirred-silicon-valley) — The Information，2026-08-06：剖析其個人影響力與矽谷觀感（全文付費牆；論旨見 [[entities/dario-amodei-archive#2026-08]]）

- L163：

    - [The Next Web](https://thenextweb.com/news/ai-talent-wars-loyalty-money-mission-anthropic)、[Fortune](https://fortune.com/2026/08/25/anthropic-ipo-could-create-millionaires-but-company-worried-about-money-over-mission-ai-firm-ceo-dario-amodei/)：2026-08-03 起報導他憂心員工為錢不為使命而來；2026-09-06 查實為對同事的內部談話，經 Axios 引述知情人士

- L164：

    - [Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models) — Anthropic 官方部落格，Dario Amodei 署名，2026-07-27（本人原文；政策分析見 [[topics/anthropic-government-policy]]）

- L168：

    - Bloomberg（2026-06-10）：[政府應能阻止新模型發布](https://www.bloomberg.com/news/articles/2026-06-10/anthropic-ceo-says-government-should-be-able-to-block-new-models)、[只有一位直屬下屬](https://www.bloomberg.com/news/articles/2026-06-10/anthropic-ceo-dario-amodei-is-a-manager-to-only-one-direct-report)

- L169：

    - [Anthropic CEO Dario Amodei says culture will win the AI race – spends 40% on it](https://news.google.com/rss/articles/CBMipwFBVV95cUxQZ1djTjV1SG00WXBZNW9zZ0RESGh0SGJmcTNPeDI3MnJMbG4yLXpSajA3V0VZWWpzMFl2cG1mbWxBaDJfQVZ0WC16UGZxd1JpOWVPZmpVSk9HXzZta2VSSkxKSmo5RTBsMXQ1T1FKWmxSXzJQNEZ6bktsal9XdkpNbmZJOTNNYUZYWlp5OFE0c1AxUTdHa0lFM0hVY2lzMUR0UVBaS1lGdw?oc=5) — Fortune（經 Google News），2026-06-08

- L175：

    - 2026-10-29：Fortune 引 IPO 申報文件報導，Anthropic 2025 年為 Amodei 支出約 275 萬美元人身安全費，是他底薪 65.4 萬美元的四倍多、約佔總薪酬 1,800 萬美元（見 10-06）的 15%；另為總裁 Daniela Amodei 支出約 129 萬美元（來源：Google News／Fortune、The Next Web）

- L193：

    - 2026-09-12：發表本人文章〈We Must Pace the Frontier〉，呼籲業界放慢前沿 AI 並密切監控，警告 AI 群體 6–12 個月內可能具備接管網路的能力；Musk、Altman 隨後表態支持，論證見 [[topics/recursive-self-improvement]]（來源：本人網站、BBC、VentureBeat、ITV）

### C. 行內小改（原行號｜舊字 → 新字；L194–202 隨 08 月進 archive）

- L101｜`| 09-28、09-29 |` → `| 09-23 錄製（09-28 報導）、09-29 |`
- L108｜`與 [[entities/chris-olah|Chris Olah]] 等人` → `與 Daniela Amodei、[[entities/chris-olah|Chris Olah]] 等人`
- L141｜`[FT 聯合國大會即時報導]` → `[FT 聯合國安理會簡報即時報導]`
- L194｜`發言的具體場合與完整脈絡未見報導，查證狀態見上方公開立場表格標記` → `2026-09-20 查實場合為 08-26 CNBC 專訪，原話「We're not interested in destroying anyone...We think of this as a very positive sum thing, right?」`
- L196｜`僅標題可用，具體論點與建議內容未見報導，查證狀態見頁首標記` → `論點 2026-09-20 查實，見下方引文`
- L200｜`> 🔎 **查無官方**（標 2026-08-10｜查 Axios、Yahoo Finance｜訊 2026-08-24｜複 2026-09-30）｜` → `> `
- L200｜`**招募實務已由獨立報導證實，但 Dario 本人的具體發言場合與逐字稿查無官方紀錄**，改標查無官方。` → `**招募實務已由獨立報導證實；2026-09-06 查實 Dario 那番話是對同事的內部談話，由 Axios 引述知情人士轉述，沒有公開場合與逐字稿**（[The Next Web](https://thenextweb.com/news/ai-talent-wars-loyalty-money-mission-anthropic)、[Fortune](https://fortune.com/2026/08/25/anthropic-ipo-could-create-millionaires-but-company-worried-about-money-over-mission-ai-firm-ceo-dario-amodei/)）。`
- L202｜`（查證狀態見上方標記）` → `（查證結果見上方引文）`
- L210｜`開源權重模型立場聲明（07-28）` → `開源權重模型立場聲明（07-27）`

### D. `## 現況`（取代 L50–56）

    他目前最主要的公開主張是放慢前沿 AI：2026-09-12 本人文章〈We Must Pace the Frontier〉提出三步驟減速計畫、由 Anthropic 先做第一步，並警告能力更強的 AI 群體 6–12 個月內可能具備接管網路的能力；09-23 在聯合國安理會簡報再提範圍限定的國際協議（媒體轉述）。十月本站所見只有兩則媒體轉述（10-03 呼籲同業對模型能力透明誠實、10-17 重申文化論）。各項主張與本人原文見 [[#核心論述]]，減速的論證與後續見 [[topics/recursive-self-improvement]]。

    與川普白宮的關係從 06 月低點回溫：當時白宮人士不再信任他，出口管制談判改由 [[entities/tom-brown]] 接手；09-27 白宮晚餐、10-01 川普公開說喜歡他（Bloomberg，僅標題），是否完全修復未見報導，逐次互動見 [[topics/anthropic-government-policy#🪖 軍事合約：護欄 vs 無限制存取]]。公司正走向 IPO（[[topics/anthropic-ipo]]，財務長 [[entities/krishna-rao]] 操盤）；他的薪酬（總薪酬約 1,800 萬美元）與公司為他支出的人身安全費見頂部與 [[#歷史記錄]] 10-06、10-29。

### E. `## 核心論述` 主張清單（取代 L60–81）

    | 主張 | 最近一次 | 本人原文 | 論證與後果 |
    |---|---|---|---|
    | 前沿 AI 要放慢並受監控：三步驟減速計畫，Anthropic 先給獨立稽核員員工級權限；警告 AI 群體 6–12 個月內可能具備接管網路的能力 | 2026-09-12（09-15 Dreamforce 重申） | [〈We Must Pace the Frontier〉](https://darioamodei.com/post/we-must-pace-the-frontier)，本人網站 | [[topics/recursive-self-improvement]] |
    | 中國是他的減速方案中「最棘手的兩難」 | 2026-09-13 | 僅媒體轉述（[CNBC](https://www.cnbc.com/2026/09/13/china-dilemma-ai-slowdown-anthropic.html)） | [[topics/recursive-self-improvement]] |
    | 不主張禁止開源權重模型；主張限制強力晶片與製程設備出口中國、打擊工業規模蒸餾、所有夠強的模型（開源與閉源）都要強制安全測試 | 2026-07-27 | [Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models)，官方部落格、本人署名 | [[topics/anthropic-government-policy]] |
    | 國際 AI 安全協議應範圍限定（如禁止 AI 生物武器），各國互相查核承諾、共同測試並通報事件 | 2026-09-23 聯合國安理會簡報 | 僅媒體轉述（[Voce di New York](https://lavocedinewyork.com/en/news/2026/09/24/ai-leaders-warn-un-over-ai-power-and-human-control/)） | [[topics/anthropic-government-policy#2026-09-24]] |
    | 大眾對 AI 的反彈根本上是信任危機；要靠治癒癌症這類具體科學突破扭轉 | 2026-08-16 | 本人 X 貼文（[Simon Willison 全文引述](https://simonwillison.net/2026/Aug/16/dario-amodei/)） | — |
    | Anthropic 無意取代 SaaS 業者：「We're not interested in destroying anyone」，視為正和 | 2026-08-26 | [CNBC 專訪逐字稿](https://www.cnbc.com/2026/08/26/cnbc-exclusive-transcript-salesforce-chair-ceo-marc-benioff-and-anthropic-co-founder-ceo-dario-amodei-speak-with-cnbcs-jim-cramer-on-closing-bell-overtime-today.html)（與 Marc Benioff 同場） | [[topics/anthropic-business]] |
    | 企業文化而非產品決定 AI 競賽勝負；他最多花 40% 工時在文化 | 2026-10-17（06-08 首見） | 僅媒體轉述（[Fortune](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPVndFZDV2OEU0dmx1U1N1Ri1MTnRjeFBpOHlGU040ekJHZ1VHZkhkcWhvYV9qVFdKNXdjdFpZZ0JWbW1wN1BWcGNHakgwY29GYjZRanRXLXl1QTlPaVhiNGg0WDhOZXhYQnNzUEhtRkREVl9nOGRDMXRieDhMUTNPLXNuWF9LSlByZGpqSXFxZEpWWmd5OC0wZDBzclNVUnh0dk1PeHRzR2o?oc=5)） | — |
    | 政府應有能力阻止危險 AI 模型發布 | 2026-06-10 | 僅媒體轉述（[Bloomberg](https://www.bloomberg.com/news/articles/2026-06-10/anthropic-ceo-says-government-should-be-able-to-block-new-models)） | [[topics/anthropic-government-policy]] |
    | 「壓縮 21 世紀」（十年完成百年生醫進展）的願景目前還做不到 | 2026-07-06 | 僅媒體轉述（[STAT 專訪](https://www.statnews.com/2026/07/06/anthropic-ai-biotech-impact/)） | — |
    | 同業應對模型能力保持透明誠實 | 2026-10-03 | 僅媒體轉述（[WSJ，經 Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/nvidias-jensen-huang-other-ceos-213019720.html)） | [[entities/jensen-huang]] |

### F. 表下一句（取代 L83–91：細節區與懸置細節）

    〈We Must Pace the Frontier〉的三步驟、技術依據與社群質疑見 [[topics/recursive-self-improvement#Dario Amodei 親自呼籲 AI 暫緩發展、警告「AI 群體行為」風險（2026-09-12～13 新增，2026-09-27 官方原文查證）]]；Musk（09-11 才稱研究員的示警是「psyop」）與 Altman 隨後表態支持，見 [[#歷史記錄]] 09-12。

### G. `## 公開批評者對照`：表上判準句（L94 後）與三列新列；全表依「何時」重排

    列入本表的是具名的人或政治陣營，公開、直接點名 Amodei 或 Anthropic 的減速呼籲或風險示警；媒體評論文章不列（如 08-24 Fortune 以航空業為鑑的評論，見 [[entities/dario-amodei-archive#2026-08]]）。「何時」是發言日。

    | Gavin Baker | 08-16 前 | 在 All-In podcast 與 X 批他過度悲觀描繪 AI；Amodei 08-16 回應反彈是「信任危機」（[TechCrunch](https://techcrunch.com/2026/08/16/anthropic-ceo-says-ai-backlash-is-fundamentally-a-crisis-of-trust/)） | 投資人；與 Anthropic 有無投資關係未見報導 |
    | Mark Zuckerberg | 09-16 前 | 在 AI 減速辯論中點名批評 Anthropic，批評內容未見報導（[NYT](https://news.google.com/rss/articles/CBMijwFBVV95cUxNbDdJR2JuaHlmNmNBV3BFUDN1WVh6amQzM0VnWUcwLUl5MVFzaUJDMlBSQkNEeUhSSG1ZcjIya21VSWh5TXQ4dll4X0pHRE1BeUl3V3dydTctWEtRU0ZYQmE4V3BkcVM4VHV6MzdKVy1mNWE0WUtidXRubkFLZmxIRVFKblBEZ3NwczBLQ1habw?oc=5) 09-16 報導，僅標題） | Meta 執行長，同業 |
    | 川普陣營盟友（備忘錄作者未具名） | 09-24 前 | 白宮內流傳的備忘錄稱有效利他主義「打造 AI 末日論管線」，點名 Dario 與 Daniela Amodei（[Axios](https://axios.com/2026/09/24/trump-anthropic-ai-doomerism-dario-amodei) 09-24 獨家） | 白宮以外的川普政治顧問，政治對手 |

### H. `## 在 Anthropic 的角色與影響` 末加一條（L81 聯署信的新家）

    - **聯署：** 曾與 Altman、Hassabis、Suleyman 聯署 AI 執行長的生物武器防範信（Wired；日期與原文連結未見）

### I. `## 相關議題` 末加五條（L122 之後）

    - [[topics/anthropic-ipo]] — IPO 進度；申報文件揭露的薪酬與人身安全支出
    - [[topics/ai-agent-safety-product-vulns]] — CNN 專訪：他說的「AI agent 脫離控制」所指為 OpenAI 7 月代理逃逸事件
    - [[entities/tom-brown]] — 共同創辦人，06 月接手白宮出口管制談判
    - [[entities/jack-clark]] — 共同創辦人、政策主管：減速與緊急關閉開關的政策說法
    - [[entities/krishna-rao]] — 財務長，IPO 操盤者

### J. `## 參考來源`：減速文章一手（取代 L150–151）

    - [We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier) — Dario Amodei 本人網站，2026-09-12（本人原文）

### K. `## 歷史記錄` 2026-08 總結（取代 L194–207）

    - 2026-08（總結）：原始條目見 [[entities/dario-amodei-archive#2026-08]]
      - 08-16 在 X 稱大眾對 AI 的反彈根本上是信任危機、要靠治癒癌症這類突破扭轉，回應投資人 Gavin Baker；08-17 Fidji Simo 公開呼應
      - 08-26 與 Marc Benioff 同上 CNBC 專訪，稱 Anthropic「無意摧毀任何人」（Business Insider 08-28 跟進）
      - 08-24 Fortune 評論以航空業為鑑，批他把「安全」當訴求；08-06 The Information 剖析其小圈子決策，與示警正疏遠投資人、對手與部分美國政府
      - 08-03～07 據 Axios 引述知情人士，他對同事憂心新人為錢不為使命而來，查實為內部談話、沒有公開場合與逐字稿；08-24 Axios 另報導面試會問候選人使命與金錢的優先序

### L. archive

- `**最後更新：**` → `**最後更新：** 2026-11-05`
- L37｜`回主頁「現況」或「公開立場與言論」表。` → `回主頁「現況」或「核心論述」表。`
- 檔尾 append `## 2026-08`：原 L194–196、（空行）L40–41 callout（空行）、L197–198、（空行）L200（空行）、L202–204、（空行）L206–207；L194、L196、L200、L202 照 C 節改

### M. 同維護者鄰居（只改互指句日期＋最後更新）

- `wiki/entities/michael-burry.md`｜`2026-09-13 公開呼籲全球 AI 減速` → `2026-09-12 公開呼籲全球 AI 減速`；`**最後更新：**` → `**最後更新：** 2026-11-05`
- `wiki/entities/sridhar-vembu.md`｜`2026-09-13 公開呼籲全球 AI 減速` → `2026-09-12 公開呼籲全球 AI 減速`；`**最後更新：**` → `**最後更新：** 2026-11-05`
- `wiki/entities/jack-clark.md`｜`2026-09-13 曾親自呼籲` → `2026-09-12 曾親自呼籲`；`**最後更新：**` → `**最後更新：** 2026-11-05`

## 二、進規則檔

### N. 新檔 `.claude/reporter-rules/people/pages.md`

    # 人物記者：負責頁的表格契約

    一頁一節，節名＝頁名。只有列在這裡的頁有表格契約；其餘人物頁照 `.claude/reporter-rules/people/daily.md` 與 `.claude/reporter-rules/page-templates.md`「人物頁（類型 person）」。每日該做什麼在 `.claude/reporter-rules/people/daily.md`。

    ---

    ## entities/dario-amodei

    **這頁答什麼：** Dario Amodei 是誰、現在公開主張哪幾件事（各附本人原文出處）、誰在公開反對他、與白宮的關係走到哪。不替讀者判斷他的主張對不對。**不收**：主張的論證、技術依據與社群質疑 → `topics/recursive-self-improvement`（減速）或該主張所屬的議題頁；白宮與政府的逐次互動 → `topics/anthropic-government-policy` 的 `## 攻防紀錄`／`## 時序`；IPO 進度與申報文件總表 → `topics/anthropic-ipo`；批評者的原話與來源 → 該人的 entities 頁。

    **觸發條件：** 他本人的公開發言、文章與訪談；他身上發生的事（白宮互動、薪酬與安保揭露、IPO 角色）；具名的人或陣營對他的公開批評。

    **標頭下一行：** 一句「本頁回答：…」，照上面「這頁答什麼」的讀者語言版，不寫日期與數字。

    **`## 現況`（兩段）：** 第一段寫他目前最主要的公開主張與最近一次說的日期，指 `## 核心論述`；第二段寫他身上正在發生的事（白宮關係、IPO、薪酬與安保揭露），每件一句並指路。有新事件時改寫該段，不在段首接新日期。

    **`## 核心論述`（主張清單，表頭 `| 主張 | 最近一次 | 本人原文 | 論證與後果 |`，上限 10 列）：**
    - 一項主張一列，只收他本人的公開發言；內部談話、媒體推測、他身上發生的事（薪酬、安保、會面、人事）不進表，寫 `## 現況` 或 `## 歷史記錄`。
    - 同一主張再說一次時改寫「最近一次」與出處，不加列；改口或撤回時改寫該列並在主張格寫明。
    - 「本人原文」只認官方部落格、本人文章、逐字稿或本人社群貼文，附連結；找不到原文寫「僅媒體轉述（媒體名）」，有連結就附。
    - 「論證與後果」指向住論證的議題頁，沒有寫「—」；本頁不展開論證。
    - 不因時間移出；滿 10 列時「最近一次」最舊者移出，原字留在它的 `## 歷史記錄` 條目。

    **`## 公開批評者對照`（四欄表 `| 誰 | 何時 | 批評什麼 | 利益關係 |`，一方一列）：**
    - 只收具名的人或政治陣營公開、直接點名 Amodei 或 Anthropic 的減速呼籲或風險示警；媒體評論文章不收。表上一句寫這條判準的讀者語言版。
    - 「何時」寫發言日，不寫報導、轉載或查證日；日期不明寫「MM-DD 前」並在格內寫出最早的報導日。
    - 有人物頁的連人物頁，原話與來源寫在該頁；沒有人物頁的在「批評什麼」格附出處連結，找不到出處不收。同一方再批評時改寫該列。

    **`## 參考來源`：** 同一事件只留一手或最早一條，每條附連結；找不到連結的刪掉，事實留在 `## 歷史記錄`。

    **每日更新動作：**
    1. 事件 prepend 進 `## 歷史記錄`（`- YYYY-MM-DD：…`，附來源媒體名），事件日寫發生日。
    2. 依上面條文判斷 `## 核心論述`、`## 公開批評者對照` 與 `## 現況` 要不要改寫。
    3. 懸置標記住事實所在的那一處；同一事實只標一處。
    4. 更新「最後更新」；有新事件時一併更新「最後新聞更新」與頂部 callout（只留一則，寫最新事件）。

    **蒸餾與封存**照 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」，archive 為 `entities/dario-amodei-archive`，對象是 `## 歷史記錄`，新時段開 `## YYYY-MM`。

### O. `.claude/reporter-rules/people/daily.md`

- L3 舊：`本記者的負責頁無結論表契約，故無 `pages.md`。`
- L3 新：`負責頁的表格契約在 `.claude/reporter-rules/people/pages.md`（一頁一節，只讀本次要動的頁那一節；沒有列在那裡的頁無表格契約）。`
- L16 舊：`| `wiki/entities/dario-amodei.md` | Anthropic CEO 公開聲明、政策立場 |`
- L16 新：`| `wiki/entities/dario-amodei.md` | 本人公開發言與文章、他身上發生的事、具名批評（契約見 `.claude/reporter-rules/people/pages.md` 本頁節） |`
- L30 舊：`**論述記錄：** 有引用價值的公開聲明（含出處）記入 `## 核心論述` 或 `## 現況`；純推測不記錄。`
- L30 新：`**論述記錄：** 有引用價值的公開聲明（含出處）記入 `## 核心論述` 或 `## 現況`；純推測不記錄。`pages.md` 有該頁節的，照該節寫（例：`entities/dario-amodei` 的核心論述是覆寫型主張清單，不 prepend）。`

