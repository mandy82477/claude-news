# 第 23 波 draft：逐字稿（2026-11-02）

> 單一來源：`<scratchpad>/w23/design/newtext.py`（頁面）、`rules_patch.py`（規則檔）；本檔由 `make_draft.py` 生成，改字請改那兩支再重生。行號指設計 commit `702e5a6` 原檔（B＝business、I＝ipo）。實作者跑 `split.py <repo>` 產全文，不手抄本檔。

# 進頁面

## A. 母頁 topics/anthropic-business

使命句（標題下）：

```markdown
Anthropic 的錢現在是什麼狀況、外面拿哪些數字在賭它，以及哪幾件事會反過來改到你用的 Claude——合作與算力、風險各往下鑽，上市與財報在 [[topics/anthropic-ipo]]。
```

拆頁評估（取代 B33）：
```markdown
%% 拆頁評估 2026-11-02：已拆（第 23 波，`docs/page-audits/ledger.md` 裁決紀錄）。合作與算力 → topics/anthropic-partnerships-compute；風險與商業模式 → topics/anthropic-business-risks；營收估值與數字出處併入 topics/anthropic-ipo（標題改「上市與財報」）。母頁留指標表、IPO 一句、子線路由、人物、公司動態時序與時段總結；子頁時序照搬未去重（G1 約 65% 是指路句），去重列 /wiki-lint 候選。 %%
```

新節「往下鑽：三條子線」（插在 `## IPO 走到哪一格` 之後）：
```markdown
## 往下鑽：三條子線

**事實和數字在下面三頁；同一則消息該打幾折、誰的股票有感，在 [[topics/market-signals]]。**

| 子頁 | 答什麼 | 最後動態 |
|---|---|---|
| [[topics/anthropic-ipo]] | 上市走到哪、S-1 寫了多少營收和虧損、這些數字是誰說的 | 2026-11-01 |
| [[topics/anthropic-partnerships-compute]] | 跟誰合作、算力和資金從哪來、跟 Google／Amazon／Microsoft 各是什麼關係、哪個合作會改到你用的 Claude | 2026-11-01 |
| [[topics/anthropic-business-risks]] | 哪裡會出事、你能先做什麼，以及它怎麼賺錢 | 2026-11-01 |

#### 算力與資金從哪來
這一節現在在 [[topics/anthropic-partnerships-compute#算力與資金從哪來]]。

#### 哪個合作會改到你用的 Claude
這一節現在在 [[topics/anthropic-partnerships-compute#哪個合作會改到你用的 Claude]]。

#### 還沒過去的風險
這一節現在在 [[topics/anthropic-business-risks#還沒過去的風險]]。

#### 這些數字是誰說的
這張出處表依事實分住三頁：財務與估值列在 [[topics/anthropic-ipo#這些數字是誰說的]]，合作列在 [[topics/anthropic-partnerships-compute#這些數字是誰說的]]，風險與商業模式列在 [[topics/anthropic-business-risks#這些數字是誰說的]]。
%% 指路殼四個：「哪個合作會改到你用的 Claude」「還沒過去的風險」「這些數字是誰說的」有 daily/ 讀者版日報（不可改的過去）錨點指入，永久保留；「算力與資金從哪來」只剩 entities/tom-brown L47 指入，人物頁改指子頁後刪（第 23 波 handoff）。 %%
```

`## 時序` 開頭：
```markdown
**本節只收公司動態**（辦公室、雇主排名、經濟研究、組織文化）；合作與算力、上市與財報、風險與商業模式的逐日條目在三個子頁的 `## 時序`。

### 未歸類

（目前沒有）

```

08 月時段總結（插在 `### 2026-07（時段總結）` 之前；原文一字不刪搬進 archive `## 2026-08`）：
```markdown
### 2026-08（時段總結）

- 營收與估值：08-15 Q2 營收逾 115 億美元；08-18 年化營收 650 億美元（7 月數字）；08-13 起多家報投資人估值上看 2 兆美元。
- IPO 籌備：08-14 CFO 展開早期投資人會議；08-18 傳創辦人保留超級投票權、上市前信用額度逾 100 億；08-22 NYT 稱擬募資至多 1,000 億。進程見 [[topics/anthropic-ipo]]。
- 估值質疑：08-23 Damodaran 稱撐起 2 兆需第 10 年營收 1.2 兆；08-26 傳向投資人簡報 TAM 30 兆美元。
- 算力：Volta 六年 100 億（08-04）、Riot 20 年 90 億（08-11）、Nscale 450 億（08-28）、資料中心私募信貸 13 億（08-19），逐筆見 [[topics/anthropic-partnerships-compute#算力與資金從哪來]]。
- 晶片：08-05～07 公司證實成立內部晶片設計團隊，仍走多晶片路線；08-21 延攬 Google TPU 創辦人 Amir Salek。
- 合作：Claude for Legal 部門（08-07）、Claude Academy（08-23）、Salesforce Claudeforce（08-26）、Claude for Teachers（08-31）；洽購 Decart（08-13），09-08 撤回。
- 法律：Round Hill Music 求償 10 億（08-18）、Sony 與 Warner Chappell 提告（08-29），見 [[topics/anthropic-business-risks#還沒過去的風險]]。
- 採用反面：FT（08-23）與 cio.com（08-25）稱旗艦模型對一般消費者與部分企業吸引力不足。
- 公司動態：Axios（08-24）稱面試會問候選人「使命」與「金錢」的優先順序。

原始條目見 [[topics/anthropic-business-archive#2026-08]]

```

## B. 子頁 topics/anthropic-partnerships-compute（新）

```markdown
# Anthropic 合作與算力：跟誰簽、算力從哪來

Anthropic 跟誰簽了合作、算力和資金從哪來、跟三大雲各是什麼關係，以及哪幾筆會改到你拿得到什麼、付多少——事實和數字在這頁；同一筆交易該怎麼判讀，在 [[topics/market-signals-compute]]（算力與融資）與 [[topics/market-signals-customers]]（通路與客戶）。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/anthropic-business]]
**開始日期：** 2026-05-28
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-11-01

> **最新動態**（2026-11-01）
> - **Palantir CTO 稱不後悔與 Anthropic 合作**：先前曾因資料外洩疑慮限縮內部使用（[The Next Web](https://news.google.com/rss/articles/CBMilgFBVV95cUxPYXNMa2gzTHVCVzJJazJUQmY1S0FxeDlOdVA2V0ZIR1BpLUZBNkZQMXFYLXF2MEpjWXNlSmk2RkpEWF85bWgyeDFxdXhha3puWGk1VWtPX1R1cTRkN0EzODlaSmRkS3lOUEJzeE9iMVNsUm42cEY2ZjdiNGFVS2VTR2Y2VVd0OTUzQzZMWXBqMk5CZ2otY2c?oc=5)）

---

```

新節「跟三大雲各是什麼關係」（冷讀者 Q4；放這頁的理由見 proposal §1）：
```markdown
## 跟三大雲各是什麼關係

**同一家公司可以同時是出資者、算力供應商、通路，也可能是客戶或對手。** 每格一句，金額的家在格內連結。

| 公司 | 出資 | 算力 | 通路 | 也是客戶或對手 |
|---|---|---|---|---|
| Google | 2026-04-24 宣布最高 $400 億，見 [[entities/google-investment]] | TPU；S-1 承諾 $1,140 億（多家引 S-1） | Vertex AI，費率由 Google 自訂，見下方合作表 | Gemini 是直接對手，見 [[topics/competitor-landscape]] |
| Amazon | 2023–2024 共 $40 億（媒體稱）；Series H 再出 $50 億（2026-05-28，多家報導） | S-1 承諾 $1,100 億（多家引 S-1） | Bedrock、Claude Platform on AWS；2025 年近半營收經 Amazon、Google 雲端市集賣出 | 賣家工具首波接 Claude（09-23）；Alexa 傳降低對高成本模型依賴（07-23） |
| Microsoft | 未見持股報導 | Azure 容量 $300 億（[官方 05-06 公告](https://www.anthropic.com/news/higher-limits-spacex)提及，2026-11-02 查證） | Microsoft Foundry，CCU 後付 | 以自研 MAI 取代 Excel／Outlook 裡的 Claude，見 [[topics/anthropic-business-risks#還沒過去的風險]] |

Nscale、Akamai、SpaceX 等其餘算力來源見下表；2025 年雲端市集 47% 的口徑見 [[topics/anthropic-ipo#S-1 揭露了什麼]]。

```

07 月合作清單彙整（取代 30 列，插在 B464 之前）：
```markdown
**其餘合作彙整（2026-07，30 筆）**：算力與晶片——TeraWulf（07-06，20 年 190 億美元租約）、AMD（07-22，最高 50 億投資＋晶片協議）、Meta 運算力租賃洽談（07-17，100 億）、Samsung 代工洽談（07-02／07-06）、SK 集團晶片供應接洽（07-26）、澳洲 1.4GW 資料中心採購（07-05）；企業與服務夥伴——UST（07-10／07-14／07-20）、Cognizant 升為全球首要夥伴（07-28）、Deloitte（07-17）、FIS（07-17）、LTM（07-13）、Optum（07-14）、Blackstone 合資 Ode（07-16，15 億美元）；資安整合——Orca Security、Druva（07-21）、Cyberhaven（07-23）、Surf AI（07-28）、Varonis（07-14）、Oxide 加入 Glasswing（07-29）；雲端與工具——AWS 治理功能（07-09）、Enterprise Gateway（07-01）、Google Workspace（07-06）、Claranova（07-15）、MixRoute（07-05）、企業支出控管（07-04）；政府——美國商務部協議（07-01）、加拿大政府 1,000 萬加幣（07-15）；另有 Blackstone 高淨值基金表現（07-02）。原始條目見 [[topics/anthropic-business-archive#2026-07]]。
```

時序尾句（三子頁共用）：
```markdown
2026-08 以前的條目見 [[topics/anthropic-business#時序]] 的時段總結。
```

出處表備忘（合作算力、風險兩頁新寫；ipo 照搬原 B191）：
```markdown
%% 維運備忘：本表與「現在的數字」不重複寫數值；累積封頂 20 列，三頁（anthropic-ipo／-partnerships-compute／-business-risks）各自計，滿了汰除來源日期最舊者。 %%
```

## C. 子頁 topics/anthropic-business-risks（新）

```markdown
# Anthropic 風險與商業模式：哪裡會出事、怎麼賺錢

Anthropic 哪裡會出事、你能先做什麼，以及它靠什麼賺錢、產品有沒有人要——事實和你的選項在這頁；官司與監管消息該打幾折，在 [[topics/market-signals-legal]]。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/anthropic-business]]
**開始日期：** 2026-05-28
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-11-01

> **最新動態**（2026-11-01）
> - **Business Insider：內部用 Claude 的用量價值已超過員工薪資**：按對外收費換算，換算方式未附（[Business Insider](https://news.google.com/rss/articles/CBMiogFBVV95cUxPckZlQklSTUE5MnZLZDM2U1RWbGFtQzRmVU1mTTk5YUVLNEVta3FmZnM5OWIxUW9DN253ZlctTGk4RFEybHFGQU9hXzNSdkE5SGZRbjNKLUd6RE9OaEN6NWkzd2dpcnRDRjdGR01DN0JyQWVjcFhkaEs5UmlmNS1oZV9VSVhjbHk3d0M3aHVwa0lfODdOZFF4NnVHSTBRUy1EZlE?oc=5)）

---

```

風險表新列（插在 B223 之後；B226 UTRF 列讓位）：
```markdown
| 上市前的虧損、通路與算力長約（2026-10-26） | 全部使用者（供應商穩定性與定價走向） | 把關鍵工作流做成換得了模型供應商；簽長約前看 S-1 修正版與首份季報 | ⚠️ 中 | 一級媒體引公司或投資人（多家引 S-1） |
```

圖例下（B229 之後）：
```markdown

**個人訂閱用戶最直接相關的是「訂閱補貼收窄」與「多 agent 併發推高用量」兩列**；其餘多落在企業採購或特定用途。

UTRF 專利訴訟（求償含禁制令）目前不在表上，訴訟仍在進行，進度見下方細節區。
```

備忘（B236 之後）：
```markdown
%% 維運備忘：2026-11-02 第 23 波新進「上市前的虧損、通路與算力長約」（多家引 S-1，⚠️ 中；虧損、通路集中、供應商依賴三類同一個讀者動作，合為一列），表滿載觸發讓位，依留表優先序讓位者為 UTRF 專利訴訟（你能先做什麼＝沒有繞法、⚠️ 中、最後動態 08-24），細節區已加註。 %%
```

細節區新條（B239 之後）：
```markdown
- **上市前的虧損、通路與算力長約（2026-10-26，多家引 S-1）**：上半年營業層虧約 6.9 億、淨損約九成為非現金；2025 年近半營收經 Amazon、Google 雲端市集賣出；算力長約四家合計逾 5,000 億。數字見 [[topics/anthropic-ipo#S-1 揭露了什麼]]。
```

UTRF 讓位註記（B278 之後）：
```markdown
%% 未列入風險表（UTRF 專利訴訟）：表滿載，2026-11-02 %%
```

## D. topics/anthropic-ipo（改造）

新節頭：`## 上市走到哪一格`（插在 I43 之後）、`### 誰說撐不住：唱空與質疑`（I64 之後，收 B266–267、B283–285）、`## 數字細節`（取代 B66 粗體）、`## 時序`（I204 之後）。

S-1 表新增兩列（I71 之後、I76 之後）：
```markdown
| 營業損益口徑 | 上半年營業層虧約 $6.9 億；排除股權報酬、非現金捐贈、和解費用後的調整後營業利益約 $16 億 | 多家引 S-1 | 「連續第二季獲利」只在調整後口徑成立，別當成會計獲利 |
| 通路與客戶集中 | 2025 年約 47%（約 $21.6 億）營收經 Amazon、Google 雲端市集賣出；兩家未具名客戶各占 12%；換算 2025 全年營收約 $46 億（推論） | Reuters 引外流招股書（10-17 查證） | 雲端市集是通路不是客戶；兩家雲的條件變動會先傳到走 Bedrock、Vertex 的用戶 |
```

相關頁面新增：
```markdown
- [[topics/anthropic-partnerships-compute]]：合作與算力（算力承諾的對手方逐筆）
- [[topics/anthropic-business-risks]]：這些數字會不會波及你用的 Claude
```

## E. 照查證與冷讀者改的句子（逐行）

### business 原行（去向見 proposal-map 第一節）

**B31**　原：`**最後更新：** 2026-11-01…`

- 「**最後更新：** 2026-11-01」→「**最後更新：** 2026-11-02」

**B43**　原：`**最新（2026-10-15）：** Anthropic 揭露 2026 Q3 營收達 168 億美元（季增約 46%），公司稱為 IPO 前最後一次對投資人…`

整行改為：
```markdown
**最新（2026-10-26）：** 公開版 S-1 提交 SEC：上半年淨損 807 億美元，約九成是估值上升造成的非現金會計損失；上半年營收約 163 億（多家引 S-1）。股數、價格區間與掛牌日未定。
```

**B45**　原：`**（2026-09-04）：** FT／NYT 報導 IPO 承銷投行組合首度具體化；The Information 報導 Anthropic 自建支付技術可…`

整行改為：
```markdown
**（2026-10-15）：** 揭露 2026 Q3 營收 168 億美元（季增約 46%），公司稱為 IPO 前最後一次對投資人揭露；紐約市主計官同日要求暫緩 IPO。
```

**B47**　原：`> **這家公司沒有公開財報。** 下表每一列的最後兩欄告訴你這個數字是誰說的、下一次會有新數字的時點。**五種數字量級不同，不可互相替代或加總**——年化營收…`

整行改為：
```markdown
> **公開版 S-1 已提交但尚未生效，上市前沒有季度財報。** 下表每一列的最後兩欄告訴你這個數字是誰說的、下一次會有新數字的時點。**五種數字量級不同，不可互相替代或加總**——年化營收、單季營收、官方估值、IPO 估值預期、市場總量各答各的問題。
```

**B53**　原：`| 年化營收（ARR） | 年化推估，非單季實收 | $650 億（2026-07 數字，08-18 報導） | 一級媒體引公司 | 下次投資人揭露 |…`

- 「$650 億（2026-07 數字，08-18 報導）」→「$650 億（2026-07 數字，08-18 報導；之後未見新值）」

**B54**　原：`| 單季營收 | 2026 Q3 實際入帳，公司稱為 IPO 前最後一次對投資人揭露 | $168 億（2026-10-14） | 一級媒體引公司 | S-1 …`

- 「$168 億（2026-10-14）」→「$168 億（2026-10-15）」

**B55**　原：`| 獲利 | 連續獲利季數，公司對投資人的口頭揭露 | 連續第二季獲利（2026-09-13） | 一級媒體引公司 | S-1 財報 |…`

整行改為：
```markdown
| 獲利 | 調整後營業利益（排除股權報酬、非現金捐贈、和解費用），不是會計淨利 | 連續第二季為正（2026-09-13 口頭）；S-1 上半年調整後約 $16 億 | 一級媒體引公司 | S-1 修正版或首份季報 |
```

**B56**　原：`| 淨損（2026 上半年） | 公司層級會計虧損，與上方「獲利」列的口頭揭露為不同口徑 | $807 億（2026 H1，2026-10-26 公開版 S-1…`

整行改為：
```markdown
| 淨損（2026 上半年） | 會計淨損；約 $724 億是可轉換工具隨估值上升的非現金損失，營業層虧約 $6.9 億 | $807 億（2026 H1，2026-10-26 公開版 S-1） | 一級媒體引公司（多家引 S-1） | 下次財報揭露 |
```

**B58**　原：`| Public Benefit Fund 股權承諾 | 承諾撥入公益信託的股權比例，待股東會核准 | 5%（市值每漲 50% 加碼 2%，2026-10-18…`

- 「承諾撥入公益信託的股權比例，待股東會核准」→「承諾撥入全資子實體 Public Benefit Fund 的股權比例，待股東會核准」

**B66**　原：`**數字細節**…`

整行改為：
```markdown
## 數字細節
```

**B67**　原：`- **公開版 S-1 正式提交，淨損 $807 億確認為官方數字（2026-10-26）**：此前僅 WSJ 獨家外流，今日官方公告＋SEC 文件確認，來源等…`

整行改為：
```markdown
- **公開版 S-1 正式提交（2026-10-26）**：淨損 $807 億與 10-20 WSJ 外流草稿同數字，多家引 S-1 為 80,748 百萬美元；本站未讀到原文，來源等級記為一級媒體引公司（[官方公告](https://www.anthropic.com/news/s1-sec)）。
```

**B71**　原：`- **這筆虧損近九成不是花掉的現金**——約 $720 億來自可轉換工具隨估值上升產生的會計帳列損失；同期實際投入基礎建設與運算的現金約 $90 億（前一年同…`

- 「約 $720 億來自可轉換工具」→「約 $724 億來自可轉換工具」

**B73**　原：`- **淨損與「獲利」列口徑不同（推論）**：09-13 口頭揭露「連續第二季獲利」為公司自陳利潤指標，與本次會計虧損計算基礎不同，官方未說明；HN 兩則討論（…`

整行改為：
```markdown
- **淨損與「獲利」列口徑不同**：S-1（多家引）上半年營業層仍虧約 $6.9 億，排除股權報酬、非現金捐贈與和解費用的調整後營業利益約 $16 億——「連續第二季獲利」只在調整後口徑成立；HN 兩則討論（166 分、39 分）質疑此落差。
```

**B74**　原：`- **IPO 估值預期下修至約 $1.5 兆（2026-10-16，Telegraph／Reuters）**：部分出席本週投資人日的與會者討論將估值由先前 $…`

- 「本季營收年增率已從」→「本季營收季增率已從」

**B94**　原：`- **各夥伴分項**（AWS、Broadcom、Lambda、AMD 等）：見 [[#算力與資金從哪來]]。…`

- 「見 [[#算力與資金從哪來]]」→「見 [[topics/anthropic-partnerships-compute#算力與資金從哪來]]」

**B95**　原：`- **AI 市場現況（未列入指標表，2026-10-21 讓位）**：Damodaran 估算當前實際市場規模 $2,500 億（2026-08-23），完整…`

- 「**AI 市場現況（未列入指標表，2026-10-21 讓位）**」→「**AI 市場現況（2026-10-21 移出指標表）**」

**B102**　原：`**一句結論：** 公開版 S-1 已於 2026-10-26 正式提交 SEC（擬掛牌代號「ANT」）；最後定價 $9,650 億，投資人預期 10-16 下…`

整行改為：
```markdown
**一句結論：** 公開版 S-1 已於 2026-10-26 提交 SEC（擬掛牌代號「ANT」），尚未生效；最後定價 $9,650 億，投資人預期 10-16 下修至約 $1.5 兆；股數、價格區間與掛牌日未定。五格表、S-1 揭露、營收與估值細節見 [[topics/anthropic-ipo]]。
```

**B115**　原：`**商業邏輯轉變**：6/15 原定政策（06-16 已暫停）是 Anthropic 從「訂閱補貼一切」走向「人工使用用訂閱，自動化使用按量付費」的明確信號。這…`

- 「這讓 Anthropic 的收入結構更接近雲端供應商而非 SaaS 公司。」→「政策若重啟，Anthropic 的收入結構會更接近雲端供應商而非 SaaS 公司（推論）。」

**B189**　原：`**`⟨Q-nn⟩` 是這一格還沒查實的地方，完整說明在表下細節區同編號那一條。**…`

整行改為：
```markdown
**表中 ⟨Q-01⟩ 對應下方細節區同編號那一條，寫的是這個數字查證後的實際範圍（已查證）。**
```

**B198**　原：`- **TechRadar：「AI 界的 Apple」**：TechRadar 發表評論文章，稱 Anthropic 雖為業界定價最高者，卻拿下最多營收，稱其為…`

- 「（見「IPO 追蹤」 表）」→「（見下方 IPO 細節）」

**B238**　原：`**商業風險細節** 區保留原有條目，並新增：Nvidia-Lambda 循環融資質疑、黃仁勳對投資規模「後悔」、Chamath 質疑 IPO 前景、Steve…`

整行改為：
```markdown
**商業風險細節**：表外的評論、單一來源與已移出表的風險都在這裡；唱空與估值質疑在 [[topics/anthropic-ipo#誰說撐不住：唱空與質疑]]。
```

**B242**　原：`- **S-1 揭露一個月訓練暫停與資安事件（2026-10-27，Fox News／CNBC 引路透社）**：申報文件揭露公司曾有為期一個月的訓練暫停，以及資…`

整行改為：
```markdown
- **S-1 揭露一個月訓練暫停與資安事件（2026-10-27，Fox News／CNBC 引路透社）**：事實見 [[topics/anthropic-ipo#S-1 揭露了什麼]]，操作面見 [[topics/ai-agent-safety]]。
```

**B244**　原：`- **訊 2026-10-26 追蹤**：NYT、衛報、Mashable、Fox News 跟進 Elvis Presley 版權方告 Anthropic 案…`

- 「**訊 2026-10-26 追蹤**」→「**2026-10-26 跟進**」

**B245**　原：`- **訊 2026-10-24 追蹤**：Billboard、Hollywood Reporter 同日報導另一起音樂出版商告 Anthropic 案，指控用…`

- 「**訊 2026-10-24 追蹤**」→「**2026-10-24 跟進**」

**B246**　原：`- **訊 2026-10-22 追蹤**：Billboard 報導音樂出版商 Reservoir 加入控告 Suno 與 Anthropic，指控兩家公司「意…`

- 「**訊 2026-10-22 追蹤**」→「**2026-10-22 跟進**」

**B247**　原：`- **訊 2026-10-21 追蹤**：Reuters 報導 Anthropic 與音樂出版商將在 AI 訓練資料訴訟案提出關鍵論點，意味案件進入實質審理階…`

- 「**訊 2026-10-21 追蹤**」→「**2026-10-21 跟進**」

- 「（Google News/Reuters）」→「（Reuters）」

**B252**　原：`- **Broadcom 貸款租賃晶片（2026-10-01／10-02）**：與 07-22 AMD、09-02 Nvidia-Lambda 同屬循環投資疑慮…`

- 「見 [[#算力與資金從哪來]]（Google News/Reuters；Barron's；Yahoo Finance）」→「見 [[topics/anthropic-partnerships-compute#算力與資金從哪來]]（Reuters；Barron's）」

**B253**　原：`- **訊 2026-10-06 追蹤**：Financial Times 報導華爾街銀行已正式 launch 600 億美元晶片融資案，由「考慮中」「啟動」進…`

- 「**訊 2026-10-06 追蹤**」→「**2026-10-06 跟進**」

**B259**　原：`- **訊 2026-10-05 追蹤**：BBC 報導國防部在把 Anthropic 列入黑名單後已停用其 AI 工具；同日 AWS 官方部落格詳述 Clau…`

- 「**訊 2026-10-05 追蹤**」→「**2026-10-05 跟進**」

**B260**　原：`- **訊 2026-10-06 追蹤**：BBC 原始報導於 HN 累積 12 分，國防部官員稱「已停止使用 Anthropic 產品」，未見新進展（Hack…`

- 「**訊 2026-10-06 追蹤**」→「**2026-10-06 跟進**」

**B274**　原：`- **訊 2026-10-05 追蹤**：The Information 報導 Meta、Microsoft 持續要求員工減少內部使用 Claude，≥5 家…`

- 「**訊 2026-10-05 追蹤**」→「**2026-10-05 跟進**」

**B296**　原：`| Nscale（第一筆） | $450 億，460 MW Vera Rubin 世代，年期未見（08-28） | 已簽 | 目前無可見後果；第二筆金額同為 $…`

- 「$450 億，460 MW Vera Rubin 世代，年期未見（08-28）」→「$450 億，460 MW Vera Rubin 世代，年期未見（08-28）；Nscale 全部客戶合約共 1,030 億，含 Microsoft」

**B300**　原：`| SpaceX | 每月 $12.5 億運算容量（媒體稱，Anthropic 發言人向 Business Insider 證實；官方 [05-06 公告](h…`

- 「| 目前無可見後果。下一個觸發點：算力規模公開 |」→「| 已見後果：05-06 官方隨 Colossus 1 容量提高用量上限。下一個觸發點：月費與期限的官方說法 |」

**B309**　原：`| AWS | 承諾逾 $1,000 億，屬 $5,170 億算力總額分項（推論）（09-06） | 已承諾，招股書可能揭露更多 | 通路有價格後果：Bedro…`

- 「| 承諾逾 $1,000 億，屬 $5,170 億算力總額分項（推論）（09-06） | 已承諾，招股書可能揭露更多 |」→「| S-1 揭露承諾 $1,100 億（多家引 S-1，10-26）；先前報導逾 $1,000 億（09-06） | 已承諾 |」

**B322**　原：`**此表未列、仍在洽談或僅具名**：GIC（新加坡主權基金）與 Macquarie 合作開發資料中心（08-11，規模未見）；Morgan Stanley 領投…`

- 「各案細節見下方合作表一行制清單。」→「各案細節見下方「其餘合作」清單。」

**B324**　原：`**財務面**：單月承諾量級逼近年化營收（本頁 08-29 資本支出算術），風險面見風險表。Amazon／Google 通路集中（2025 年近半營收經兩家雲端…`

整行改為：
```markdown
**財務面**：S-1 揭露的算力長約四家合計逾 5,000 億美元，會不會轉成定價壓力見 [[topics/anthropic-business-risks#還沒過去的風險]]；Amazon／Google 通路集中（2025 年近半營收經兩家雲端市集銷售，非客戶集中）見 [[topics/anthropic-ipo#S-1 揭露了什麼]]。
```

**B326**　原：`**目前唯一寫得出的算力吃緊後果**：07-18 Startup Fortune 稱 Anthropic 因運算資源吃緊收緊 Fable 5 存取；本站查證的官…`

整行改為：
```markdown
**寫得出後果的只有兩則**：05-06 官方隨 SpaceX Colossus 1 容量上線提高用量上限；07-18 Startup Fortune 稱因運算吃緊收緊 Fable 5 存取，本站查證的官方文件只寫方案分界、未載原因，見 [[entities/pricing]]「當前生效的計費規則」07-20 條。各列共同的下一個觸發點是正式定價與股數公告（公開版 S-1 已於 2026-10-26 提交）。
```

**B351**　原：`**資本支出算術（本頁計算，2026-08-29）：** Nscale 單筆 450 億美元（08-28）≈ 年化營收 650 億美元的 **69%**（450…`

整行改為：
```markdown
**資本支出的量級（本頁計算，2026-08-29）：** Nscale 單筆 450 億美元（08-28）是多年期合約總額、年期未見，不能拿去跟一年的營收（年化 650 億）直接相比；同月另有 AMD、Nvidia 兩筆算力布局、13 億美元私募信貸（08-19）與 Bastrop County 洽租（08-25）。循環融資質疑見 [[topics/anthropic-business-risks#還沒過去的風險]] 細節區。
```

**B353**　原：`**其餘合作（一行制，日期倒序）** — 未列入上表者每筆一行：…`

- 「**其餘合作（一行制，日期倒序）**」→「**其餘合作（新的在上）**」

**B464**　原：`**其餘合作彙整（2026-05～06，21 筆，一行制清單已蒸餾）**：晶片／資本——Samsung+SK Hynix（05-28，Series H 同步入股…`

- 「21 筆，一行制清單已蒸餾）」→「21 筆）」

- 「Google（2024，$400 億，見 [[entities/google-investment]]）」→「Google（2026-04-24，最高 $400 億，見 [[entities/google-investment]]）」

**B466**　原：`%% 維運備忘：原「意義」欄的敘述併進上方一句，不另外開細節條目；一句寫不下者才下沉「戰略合作細節」區。本清單只保留最近 3 個完整月，逾窗列滾動蒸餾。2026…`

整行改為：
```markdown
%% 維運備忘：原「意義」欄的敘述併進上方一句，不另外開細節條目；一句寫不下者才下沉「戰略合作細節」區。本清單只保留最近 3 個完整月，逾窗列滾動進 archive。2026-09-20：21 列 ≤2026-06-30 搬出；2026-11-02（第 23 波）：07 月 30 列與 07 月細節 12 條搬至 archive「## 2026-07」末，表清單現起點為 2026-08-01（08 月列 12-01 到期）。條文的家在 `.claude/reporter-rules/commercial/pages.md` 第 5 條。 %%
```

**B711**　原：`- **[商業模式，第三方研究] SemiAnalysis：Anthropic 訂閱方案提供的價值為 OpenAI 的 5 倍以上**：HN 75 分、6 個來…`

- 「見 [[topics/market-signals]]）」→「見 [[topics/market-signals-customers]]）」

### ipo 原行

**I26**　原：`# Anthropic IPO 追蹤…`

整行改為：
```markdown
# Anthropic 上市與財報
```

**I28**　原：`Anthropic 上市進程的事實層：遞件、時程、估值、承銷、質疑，以及逐日細節。…`

整行改為：
```markdown
Anthropic 的上市走到哪、S-1 和財報寫了多少營收和虧損、這些數字是誰說的——數字和原文在這頁；該打幾折、誰的股票有感，在 [[topics/market-signals-ipo]]。
```

**I34**　原：`**最後更新：** 2026-11-01…`

- 「**最後更新：** 2026-11-01」→「**最後更新：** 2026-11-02」

**I40**　原：`**怎麼讀這頁：** IPO 對工程師的意義是兩件事——供應商穩定性（燒錢速度、資金與算力能不能撐住服務）與定價走向（上市壓力會不會推動漲價或限縮方案）。市場判…`

整行改為：
```markdown
**怎麼讀這頁：** 上半是現況（五格表、S-1 揭露了什麼、數字細節、誰說的），下半是逐日細節。這頁只放事實；會不會波及你用的 Claude 見 [[topics/anthropic-business-risks]]，判讀見 [[topics/market-signals-ipo]]；母頁指標表見 [[topics/anthropic-business#現在的數字]]；定價見 [[entities/pricing]]。
```

**I44**　原：`**這一節回答四件事：遞件了沒、什麼時候上市、值多少、誰說撐不住。** 事實層在這裡，把這些消息放進市場框架的判讀（方向、該打幾折、接下來看哪個里程碑）見 [[…`

整行改為：
```markdown
**這一節回答五件事：遞件了沒、什麼時候上市、值多少、誰承銷、誰說撐不住。** 該打幾折、接下來看哪個里程碑見 [[topics/market-signals-ipo]]。
```

**I49**　原：`| 什麼時候上市 | 公司沒給過時程；投資人先前預期 9–10 月，09-07 Forbes 稱延至 10 月中並鎖定 $150 億信用額度，09-08 Yah…`

整行改為：
```markdown
| 什麼時候上市 | 掛牌日與價格區間官方仍未公布；公開版 S-1 已提交、未生效，先前「10 月上市」「延後」都只是媒體說法 🔎 查無官方 ⟨Q-03⟩ | Anthropic 官方公告（2026-10-26）；FT、Forbes、Yahoo Finance（08-13～09-08） | 官方一手／一級媒體 |
```

**I50**　原：`| 值多少 | 最後一次定價 $9,650 億；投資人原估 $2 兆，10-16 下修至約 $1.5 兆；10-20 S-1 首度揭露 H1 淨損 807 億美…`

- 「；10-20 S-1 首度揭露 H1 淨損 807 億美元（WSJ）」→「；H1 淨損 807 億美元（10-20 外流草稿首度揭露，10-26 公開版多家引同數字）」

- 「Telegraph（2026-10-16）；WSJ（2026-10-20）」→「Telegraph（2026-10-16）；WSJ（2026-10-20）；多家引 S-1（10-26）」

**I54**　原：`**下一個時點已達成：公開版 S-1 已於 2026-10-26 提交。** 下一個時點是股數與價格區間公告（路演期間或掛牌前）。…`

整行改為：
```markdown
**下一個時點：** 股數與價格區間公告（路演期間或掛牌前）。公開版 S-1 已於 2026-10-26 提交，尚未生效。
```

**I61**　原：`**目前結論（推論）：** 估值鏈條呈現典型「私募狂熱 vs 公開市場質疑」剪刀差——一方面 Series H 定價、次級市場溢價、獲利首度曝光都在推升估值敘事…`

整行改為：
```markdown
**目前結論（推論）：** 公開版 S-1 已在 10-26 提交，剩股數、價格區間與生效。估值仍是「私募定價 9,650 億 vs 公開市場質疑」的剪刀差，投資人預期已從 2 兆下修到約 1.5 兆。S-1 揭露的淨損約九成是非現金，營業層虧約 6.9 億。
```

**I63**　原：`**資本佈局背景（推論）：** 近兩週兩條線同步升溫——基礎建設／算力合約線（見 [[topics/anthropic-business#哪個合作會改到你用的 …`

- 「（見 [[topics/anthropic-business#哪個合作會改到你用的 Claude]]：」→「（見 [[topics/anthropic-partnerships-compute#算力與資金從哪來]]：」

**I65**　原：`**S-1 揭露了什麼**…`

整行改為：
```markdown
## S-1 揭露了什麼
```

**I67**　原：`S-1 原文：<https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthr…`

- 「下表數字取自本頁與 [[topics/anthropic-business]] 既有條目，來源層級照條目原標示，本頁未直接核對原文。」→「下表數字取自本頁「數字細節」與逐日條目，來源層級照條目原標示，本頁未直接核對原文。」

**I71**　原：`| H1 淨損與可轉換工具會計損失 | 2026 上半年淨損 $807 億，已由官方公告與 SEC 文件確認；約 $720 億是可轉換工具隨估值上升的帳列損失，…`

整行改為：
```markdown
| H1 淨損與可轉換工具會計損失 | 2026 上半年淨損 $807 億；約 $724 億是可轉換工具隨估值上升的非現金損失，營業層虧約 $6.9 億，實際基建與運算現金約 $90 億 | 多家引 S-1 | 虧損近九成是帳列數字，不等於現金燒掉的速度；供應商穩定性看現金與融資，不看這個總數 |
```

**I76**　原：`| 算力承諾總額 | Google $1,140 億、AWS $1,100 億、Broadcom $1,610 億、SpaceX $1,200 億（HN 909…`

- 「| 容量有長約保障，服務不易斷供；」→「| 容量有長約保障，服務不易斷供（推論）；」

**I83**　原：`**IPO 細節**…`

整行改為：
```markdown
## IPO 細節
```

**I87**　原：`  - 他先前唱空言論見 [[topics/anthropic-business#還沒過去的風險]]。…`

- 「[[topics/anthropic-business#還沒過去的風險]]」→「[[#誰說撐不住：唱空與質疑]]」

**I89**　原：`  - Anthropic 與 Blackstone 皆拒評論，評等機構尚未公開評等（推論：僅單一媒體轉述）。融資成本面見 [[topics/anthropic…`

- 「[[topics/anthropic-business#算力與資金從哪來]]」→「[[topics/anthropic-partnerships-compute#算力與資金從哪來]]」

**I92**　原：`- **2026-10-30 Fortune：S-1 以 69,800 字描述 AI 對投資人的風險，社會整體風險著墨相對少**：報導僅標題層級，具體段落與對照…`

- 「[[topics/anthropic-business#還沒過去的風險]]」→「[[topics/anthropic-business-risks#還沒過去的風險]]」

**I95**　原：`- **2026-10-29 Bloomberg：華爾街銀行已撤回一筆與 Anthropic 相關的德州資料中心債券發行案**：背景為 08-02 Morgan…`

- 「（見 [[topics/anthropic-business#算力與資金從哪來]]），撤回原因未見報導（Google News/Bloomberg.com）」→「（見 [[topics/anthropic-partnerships-compute#算力與資金從哪來]]），撤回原因未載（Bloomberg）」

**I102**　原：`- **2026-10-20 WSJ 獨家：Anthropic S-1 首度揭露具體虧損數字，2026 上半年淨損 807 億美元**：WSJ 報導營收仍快速成…`

- 「[[topics/anthropic-business#現在的數字]]」→「[[#數字細節]]」

**I107**　原：`- **2026-10-16 Telegraph／Reuters：部分投資人討論將 IPO 估值由 $2 兆下修至約 $1.5 兆**：出席本週投資人日的與會者…`

- 「本季營收年增率已從」→「本季營收季增率已從」

- 「[[topics/anthropic-business#現在的數字]]」→「[[#數字細節]]」

**I109**　原：`- **2026-10-15 FT／Bloomberg：Q3 營收揭露 168 億美元，公司稱為 IPO 前最後一次財報揭露**：季增約 46%（上季 140%…`

- 「[[topics/anthropic-business#現在的數字]]」→「[[#數字細節]]」

**I118**　原：`- **2026-10-05 CNN：儘管市場降溫疑慮，投資人圈仍預期推進 IPO**：CNN 報導即使 AI 熱潮降溫疑慮升高，市場仍預期 Anthropic…`

- 「而非⟨Q-03⟩「何時上市」」→「而非「何時上市」」

**I130**　原：`- ⟨Q-03⟩ 🔎 **查無官方**（標 2026-09-06｜查 calcalistech、IPO 延後｜複 2026-11-10｜訊 2026-10-26…`

整行改為：
```markdown
- ⟨Q-03⟩ 🔎 **查無官方**（標 2026-09-06｜查 calcalistech、IPO 延後｜複 2026-11-24｜訊 2026-10-26）｜**掛牌日與價格區間何時公布**：10-26 官方公告 S-1 已提交，沒給掛牌日與價格區間；2026-11-02 查 [anthropic.com/news](https://www.anthropic.com/news) 仍未公布。
```

**I131**　原：`  - **官方唯一確認過的是 2026-06-01 向 SEC 機密送交 S-1 草案**（不設股數與價格、明載仍視市況）；「十月上市」「延後」「路演」全屬媒…`

整行改為：
```markdown
  - **10-26 以前**官方只確認過 2026-06-01 機密送交 S-1 草案；「十月上市」「延後」「路演」都是媒體推估且彼此不一致，兩邊都不採信為事實。
```

**I141**　原：`  - Marcus on AI（Substack）評論文章直批「$30 trillion fantasy」；24/7 Wall St. 引述知名創投人 Cha…`

- 「[[topics/anthropic-business#還沒過去的風險]]」→「[[#誰說撐不住：唱空與質疑]]」

**I161**　原：`  - 本則以近期傳聞之更高 IPO 估值區間（見 08-13 傳 $2 兆美元、08-15 Reuters 獨家 2028 年 $1,900–2,000 億營…`

- 「（見 [[topics/anthropic-business#哪個合作會改到你用的 Claude]] $400 億美元投資記錄，」→「（見 [[topics/anthropic-partnerships-compute#跟三大雲各是什麼關係]] Amazon 列，」

**I177**　原：`  - 屬評論文章，非事實揭露或官方數字——作者以坊間流傳的 2 兆美元估值數字（延續 08-13 PYMNTS／FT／WSJ 的報導）為引子，展開對整體 AI…`

- 「[[topics/anthropic-business#還沒過去的風險]]」→「[[#誰說撐不住：唱空與質疑]]」

**I209**　原：`- [[topics/anthropic-business]]：母頁，商業健康度與逐日時序…`

整行改為：
```markdown
- [[topics/anthropic-business]]：母頁，指標表與子線路由
```

**I210**　原：`- [[topics/market-signals]]：IPO 消息的市場判讀…`

整行改為：
```markdown
- [[topics/market-signals-ipo]]：IPO 消息的市場判讀
```

## F. archive 與鄰居

- archive L34：「**最後更新：** 2026-10-25」→「**最後更新：** 2026-11-02」
- archive L37：「重點層（現在的數字、還沒過去的風險）都在主頁；IPO 進程見 [[topics/anthropic-ipo]]。」→「重點層在主頁與三個子頁：現在的數字在主頁，風險在 [[topics/anthropic-business-risks]]，合作與算力在 [[topics/anthropic-partnerships-compute]]，上市與財報在 [[topics/anthropic-ipo]]。」
- archive `## 2026-06` 之前新增節頭：`### 其餘合作彙整（原「哪個合作會改到你用的 Claude」一行制清單與戰略合作細節，2026-11-02 蒸餾搬入）`（其下照搬 B 的 07 月清單 30 列與細節 12 條）；`## 2026-07` 之前插 B900–1016（`### 2026-08`→`## 2026-08`、`#### 日`→`### 日`）

- `wiki/topics/competitor-landscape.md` L180：「[[topics/anthropic-business#還沒過去的風險]]」→「[[topics/anthropic-business-risks#還沒過去的風險]]」
- `wiki/entities/google-investment.md` L47：「為不同輪次事件，見 [[entities/pricing]]。」→「為不同輪次事件，結果（2026-05-28 Series H）見 [[topics/anthropic-business#現在的數字]]。」
- `wiki/entities/google-investment.md` L71：「- Amazon 也是 Anthropic 的重要投資者，形成多方大廠支持格局」→「- Amazon 也是 Anthropic 的重要投資者，形成多方大廠支持格局；三大雲各自的關係見 [[topics/anthropic-partnerships-compute#跟三大雲各是什麼關係]]」
- `wiki/index.md` L137：「Anthropic 商業健康度：公開版 S-1 已於 2026-10-26 正式提交 SEC（擬掛牌代號 ANT），確認 2026 上半年淨損 807 億美元；現在的數字、合作會不會改到你的帳單」→「Anthropic 的錢現在怎樣：指標表與 IPO 一句；往下鑽合作與算力（含跟 Google／Amazon／Microsoft 的關係）、風險與商業模式、上市與財報」

（competitor-landscape、google-investment 是同維護者〔商業〕的互指句；index L137 是主編的鉤子，↳ 投影由 gen 重生）

# 進規則檔（`rules_patch.py`，臨時副本實套後 `check_rules.py` ✅）

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
## topics/anthropic-business

```
新：
```markdown
## topics/anthropic-business（母頁）與三子頁

```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
**觸發條件：** 融資輪次、公司收購、戰略合作（雲端、SDK 生態、企業客戶）、**IPO 與估值進程**、**公司層級財務數字**、**公司層級商業風險**（訴訟、企業退出、補貼結構）。

**每次 ingest 後依序：**
```
新：
```markdown
**觸發條件：** 融資輪次、公司收購、戰略合作（雲端、SDK 生態、企業客戶）、**IPO 與估值進程**、**公司層級財務數字**、**公司層級商業風險**（訴訟、企業退出、補貼結構）。

**子樹：** 母頁 `topics/anthropic-business` ＋ 三子頁 `topics/anthropic-ipo`（上市與財報）、`topics/anthropic-partnerships-compute`（合作與算力）、`topics/anthropic-business-risks`（風險與商業模式）；舊時段共用 `topics/anthropic-business-archive`。以下各條寫明表住哪一頁；沒寫的指母頁。

**0. 路由（一則新聞寫進哪頁）：**

| 事件 | 寫進 |
|---|---|
| 融資輪次、IPO 與估值進程、公司層級財務數字、治理與股權 | `topics/anthropic-ipo` |
| 戰略合作（雲端、SDK 生態、企業客戶）、收購、算力合約與資本支出、政府採購 | `topics/anthropic-partnerships-compute` |
| 訴訟、企業退出、補貼結構、商業模式與定價策略、PMF 訊號 | `topics/anthropic-business-risks` |
| 公司動態（辦公室、雇主排名、經濟研究、組織文化） | 母頁 `## 時序` |
| 判不出 | 母頁 `## 時序` 的 `### 未歸類`，`/wiki-lint` 5j 分派 |

母頁每日只動：頂部 callout、`## 往下鑽：三條子線` 路由表的「最後動態」、`## 現在的數字`（第 1 條）、`## 時序` 的公司動態與未歸類（`.claude/reporter-rules/page-lifecycle.md` 母頁契約的登記例外）。母頁 callout 日期不得早於子樹最新新聞（`scripts/check_hierarchy.py`）。母頁 `#### 指路殼` 四個不動：三個有 `daily/` 讀者版日報錨點指入（不可改的過去），「算力與資金從哪來」等人物頁改指後由主編刪。

**每次 ingest 後依序：**
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
1. **`## 現在的數字`（覆寫式，上限 10 列）。**
```
新：
```markdown
1. **母頁 `## 現在的數字`（覆寫式，上限 10 列；表下細節區住 `topics/anthropic-ipo` 的 `## 數字細節`）。**
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
2. **IPO 五格表（住子頁 `topics/anthropic-ipo` 頁首；本頁只留一句結論加連結；覆寫式，五格固定不增減）。** IPO 進程的逐日細節也寫進子頁，本頁 `## 時序` 只留一行指標。
```
新：
```markdown
2. **IPO 五格表（住 `topics/anthropic-ipo` 的 `## 上市走到哪一格`；母頁 `## IPO 走到哪一格` 只留一句結論加連結；覆寫式，五格固定不增減）。** IPO 進程的逐日細節寫進該頁 `## IPO 細節`，營收估值類的一行制寫進該頁 `## 時序`。
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
公開版 S-1 出現時整表重判。
```
新：
```markdown
公開版 S-1 出現時整表重判（2026-10-26 觸發，2026-11-02 第 23 波執行）；S-1 修正版或首份季報出現時再判一次。
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
3. **`## 這些數字是誰說的`（證據層，累積封頂 20 列）。**
```
新：
```markdown
3. **`## 這些數字是誰說的`（證據層，三子頁各一張，依列隨事實歸頁：財務估值→ipo、合作→partnerships-compute、風險與模式→business-risks；各頁累積封頂 20 列）。**
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
4. **現在還會影響讀者的商業風險表（覆寫式，上限 6 列；現名 `## 還沒過去的風險`，措辭可改）。**
```
新：
```markdown
4. **現在還會影響讀者的商業風險表（住 `topics/anthropic-business-risks`；覆寫式，上限 6 列；現名 `## 還沒過去的風險`，措辭可改）。**
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
5. **`## 哪個合作會改到你用的 Claude`（覆寫式，上限 6 列）。**
```
新：
```markdown
5. **`## 哪個合作會改到你用的 Claude`（住 `topics/anthropic-partnerships-compute`；覆寫式，上限 6 列）。**
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
6. **`## 上面提到的人是誰`（覆寫式，上限 8 人）。** 只收在本頁的表或 `## 時序` 裡有一個可查證動作的人
```
新：
```markdown
6. **母頁 `## 上面提到的人是誰`（覆寫式，上限 8 人）。** 只收在本子樹（母頁與三子頁）的表或 `## 時序` 裡有一個可查證動作的人
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
他所連的那一列或那一則移出頁面時，本列一併移除。
```
新：
```markdown
他所連的那一列或那一則移出子樹時，本列一併移除。
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
7. **`## 時序` 一行制**：非上述四表的事件在 `## 時序` 最上方加一行。
```
新：
```markdown
7. **`## 時序` 一行制**：非上述各表的事件，依第 0 條路由在該頁 `## 時序` 最上方加一行。
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
archive 子頁為 `topics/anthropic-business-archive`，`## 時序` 為對象。
```
新：
```markdown
archive 子頁為 `topics/anthropic-business-archive`（**子樹共用**：三子頁的舊時段也搬進這頁，新時段開 `## YYYY-MM`），對象為四頁的 `## 時序`、ipo 的 `## IPO 細節`、partnerships-compute 的「其餘合作」清單與「戰略合作細節」。
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
10. **週更觸發邊**：上述第 1、4、5、6 條
```
新：
```markdown
10. **週更觸發邊**：上述第 1、4、5、6、12 條
```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
11. 更新「最後更新」；有新事件時一併更新「最後新聞更新」。

```
新：
```markdown
11. 更新「最後更新」；有新事件時一併更新「最後新聞更新」。母頁「最後新聞更新」只在母頁自己收了公司動態或指標換值時才動。
12. **`## 跟三大雲各是什麼關係`（住 `topics/anthropic-partnerships-compute`；三列固定 Google／Amazon／Microsoft，五欄固定：`公司｜出資｜算力｜通路｜也是客戶或對手`；週更覆寫）。** 每格一句加 wikilink 指向該事實的家（算力表、`entities/google-investment`、`entities/pricing`、anthropic-ipo 的 S-1 表），不在格內累積歷史；答不出的格寫「未見報導」。每日 ingest 不動本表，三家任一有新事實時在回報寫「⚠️ 三大雲表待週更：[哪一格]」。
13. **`## 算力與資金從哪來`（住 `topics/anthropic-partnerships-compute`；一個對手方一列，四欄固定：`對手方｜金額與期限（日期）｜狀態｜對可用性或價格的影響`）。** 新合約進表；影響欄寫不出就寫「目前無可見後果」並列下一個觸發點。**退場：** 交易取消、或距最後日期逾 180 天且無新事實 → 移出表，結論留在「其餘合作」清單。

```

### `.claude/reporter-rules/commercial/pages.md`

原：
```markdown
| Anthropic 自己的動作（融資、合作、估值、資本支出） | [[topics/anthropic-business]]；IPO 進程寫子頁 [[topics/anthropic-ipo]] |
```
新：
```markdown
| Anthropic 自己的動作（融資、合作、估值、資本支出） | [[topics/anthropic-business]] 子樹：合作與算力 [[topics/anthropic-partnerships-compute]]、上市與財報 [[topics/anthropic-ipo]]、風險 [[topics/anthropic-business-risks]] |
```

### `.claude/reporter-rules/commercial/daily.md`

原：
```markdown
| `wiki/topics/anthropic-business.md` | 融資、收購、戰略合作、企業採用率、**公司層級財務數字**、**公司層級商業風險**（訴訟、企業退出、補貼結構）|
| `wiki/topics/anthropic-ipo.md`（`anthropic-business` 子頁） | **IPO 與估值進程**：遞件、時程、估值、承銷、質疑與逐日細節（五格表住這頁） |
```
新：
```markdown
| `wiki/topics/anthropic-business.md`（母頁） | 公司動態（辦公室、雇主排名、經濟研究、組織文化）；`## 現在的數字` 指標換值；子線路由表「最後動態」。其餘商業事件寫進下面三子頁（路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條） |
| `wiki/topics/anthropic-ipo.md`（子頁「上市與財報」） | **IPO 與估值進程**、融資輪次、**公司層級財務數字**、治理與股權（五格表、S-1 揭露表、數字細節住這頁） |
| `wiki/topics/anthropic-partnerships-compute.md`（子頁「合作與算力」） | 戰略合作、收購、算力合約與資本支出、政府採購、企業採用率 |
| `wiki/topics/anthropic-business-risks.md`（子頁「風險與商業模式」） | **公司層級商業風險**（訴訟、企業退出、補貼結構）、商業模式、PMF 訊號 |
```

### `.claude/reporter-rules/commercial/weekly.md`

原：
```markdown
同批回掃 [[topics/anthropic-business]]「哪個合作會改到你用的 Claude」
```
新：
```markdown
同批回掃 [[topics/anthropic-partnerships-compute]]「哪個合作會改到你用的 Claude」
```

### `.claude/skills/wiki-lint-sweeps/references/sweeps.md`

原：
```markdown
`wiki/topics/anthropic-business.md` 的 `## 現在的數字`（上限 10 列）、商業風險表（現名 `## 還沒過去的風險`）（上限 6 列）、`## 哪個合作會改到你用的 Claude`（上限 6 列）與 `## 上面提到的人是誰`（上限 8 人）的退場與補位條文，本步即其週更觸發邊，複查規則見 `.claude/reporter-rules/commercial/pages.md`「anthropic-business 更新規則」第 1、4、5、6 條。
```
新：
```markdown
`wiki/topics/anthropic-business.md` 的 `## 現在的數字`（上限 10 列）與 `## 上面提到的人是誰`（上限 8 人）、`topics/anthropic-business-risks` 的商業風險表（現名 `## 還沒過去的風險`）（上限 6 列）、`topics/anthropic-partnerships-compute` 的 `## 哪個合作會改到你用的 Claude`（上限 6 列）與 `## 跟三大雲各是什麼關係`（三列，覆寫）的退場與補位條文，本步即其週更觸發邊，複查規則見 `.claude/reporter-rules/commercial/pages.md`「topics/anthropic-business（母頁）與三子頁」第 1、4、5、6、12 條；母頁 `### 未歸類` 有條目時依第 0 條分派。
```

### `.claude/skills/wiki-lint-sweeps/references/sweeps.md`

原：
```markdown
人物表看每人所連的那一列或那一則是否仍在頁上
```
新：
```markdown
人物表看每人所連的那一列或那一則是否仍在子樹（母頁與三子頁）上
```

### `.claude/reporter-rules/page-lifecycle.md`

原：
```markdown
判讀涉及上市公司時覆寫，見 `.claude/reporter-rules/market/pages.md`）；
```
新：
```markdown
判讀涉及上市公司時覆寫，見 `.claude/reporter-rules/market/pages.md`；`topics/anthropic-business` 的 `## 現在的數字`（指標換值）與 `## 時序`（只收公司動態），路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條）；
```

### `.claude/reporter-rules/features/daily.md`

原：
```markdown
| 商業合作 / 融資 | TCS / DXC 合作 | `topics/anthropic-business` |
```
新：
```markdown
| 商業合作 / 融資 | TCS / DXC 合作 | 合作 → `topics/anthropic-partnerships-compute`；融資 → `topics/anthropic-ipo` |
```

### `.claude/reporter-rules/market/daily.md`

原：
```markdown
| 成交價是唯一經對手方驗證的估值；條款決定誰先拿錢 | [[topics/anthropic-business]] |
```
新：
```markdown
| 成交價是唯一經對手方驗證的估值；條款決定誰先拿錢 | [[topics/anthropic-ipo]]（融資輪）、[[topics/anthropic-partnerships-compute]]（算力融資） |
```

### `.claude/agents/wiki-reporter-commercial.md`

原：
```markdown
負責 anthropic-business、enterprise-*
```
新：
```markdown
負責 anthropic-business 子樹（母頁＋anthropic-ipo／-partnerships-compute／-business-risks）、enterprise-*
```

### `.claude/agents/wiki-reporter-market.md`

原：
```markdown
事實頁（anthropic-business、pricing
```
新：
```markdown
事實頁（anthropic-business 子樹、pricing
```

# 進腳本

**無。** 逐支確認不必改：
- `scripts/pending_markers.py` `PAGE_TO_REPORTER`（L514）：兩新子頁領域 💼 商業，`reporter_of()` 走 `DOMAIN_TO_REPORTER` → `wiki-reporter-commercial`（臨時副本實測三子頁皆是）。
- `scripts/pending_handoffs.py` `OWNER_OVERRIDES`（L53）：`owner_of()` 沿 frontmatter `parent` 走到 business（index 💼 商業）→ 商業（實測）；不加覆寫，因為 market-signals 那種「領域與維護者不同」的情形這裡不存在。
- `scripts/build_web.py`、`web_reader/assets/app.js`：grep 無寫死 business 節名；`PPL_ISSUE_SHORT`（app.js L956）只是人物議題短標，缺鍵時退回頁名，不改。
- `scripts/check_hierarchy.py`、`gen_wiki_frontmatter.py`：子頁靠標頭「上層」欄自動接上（gen 後 children 四個、兩新子頁 `page_role: "child"`）。
- `src/tests/test_reader_tags.py` EXCLUDED：只防回流，新子頁不在 tags 名單，不必加。

