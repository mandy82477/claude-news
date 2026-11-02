# 第 22 波逐字稿：topics/market-signals 拆成母頁＋四子頁（2026-11-02）

> 頁面逐字以 `<scratchpad>/w22/design/out/wiki/topics/` 五頁為準（`split.py` 輸出，臨時副本跑過 gen 後的版本）。本稿由 `make_draft.py` 從 `newtext.py`（頁面新字）、`rules_patch.py`（規則檔）、`scripts.diff`（腳本，臨時副本 `git diff`）直接產生，不手抄。
> 「原 Lnnn」指 `wiki/topics/market-signals.md` 在 commit `7dbc92e` 的原檔（1,699 行）。frontmatter 由 `gen_wiki_frontmatter.py` 生成，不手填。

# 進頁面

## A. 母頁 `wiki/topics/market-signals.md`（正文 116 行）

節序：H1 → 使命句（新）→ 標頭 → 免責 → callout → `## 摘要`（＋「現在」段）→ `## 買得到的標的` → `## 近期判讀`（子頁路由表＋三段記號說明＋同名殼＋`### 未歸類`）→ `## 回顧結算`（說明＋合計表＋股價半邊說明）→ `## 相關實體` → `%% 拆頁評估 %%`。

**使命句（插在 H1 之後）**

````markdown
Anthropic 的消息放進市場框架怎麼讀：它動到哪個數字、碰到哪個你買得到的標的、兩週後對不對——判讀依四條子線往下鑽。
````

**標頭、callout、摘要的替換（原行：舊→新）**

- 原 L31：
  ````text
  **最後更新：** 2026-10-31
  →
  **最後更新：** 2026-11-02
  ````
- 原 L39：
  ````text
  僅標題可用。
  →
  僅標題可用（見 [[topics/market-signals-ipo]]）。
  ````
- 原 L42：
  ````text
  僅標題可用。
  →
  僅標題可用（見 [[topics/market-signals-compute]]）。
  ````
- 原 L50：
  ````text
  只有會進 S-1（美國上市前必須公開的申報文件，唯一揭露真實財務的地方）、或會改變 S-1 數字的六類消息才寫上來；
  →
  只有會進 S-1（美國上市申報文件，Anthropic 的公開版已於 2026-10-26 提交）、或會改變它數字的六類消息才寫上來——S-1 公開之後，看的是修正版與上市後第一份季報會不會改到這些數字；
  ````
- 原 L50：
  ````text
  多數日子沒有這種消息，本頁就不動
  →
  沒有這種消息的日子，本頁就不動
  ````

**摘要「現在」段（插在 `## 摘要` 之後）**

````markdown
**現在**：公開版 S-1 已於 10-26 提交、尚未生效，股數、價格區間與掛牌日都未公布；Anthropic 本體仍買不到，能交易的只有下表的間接標的（事實見 [[topics/anthropic-ipo]]）。判讀依題材分住四個子頁，從「近期判讀」的表往下鑽。
````

**原 L76**：砍（表中空行；Schwab 列 L77 因此回到表內）。

**`## 近期判讀` 開頭（取代原 L91–1402 的 88 則，判讀下沉四子頁）**

````markdown
判讀依題材住四個子頁，各頁最新在上；每則最後的「一課」彙整成課程表在 [[topics/market-lessons]]。

| 你想知道 | 去哪頁 | 最新一則 |
|---|---|---|
| IPO 走到哪一格、外流與 S-1 的數字該打幾折、評等怎麼看 | [[topics/market-signals-ipo]] | 10-31 Blackstone 預期上市後 BB 級 |
| 官司、機關調查、政府採購會不會寫進風險因素 | [[topics/market-signals-legal]] | 10-28 GSA 折扣擴大、向加州州長表態 |
| 誰借錢給 Anthropic 買算力、條件多貴 | [[topics/market-signals-compute]] | 10-30 Nvidia 洽談信用支持 |
| 價格怎麼改、客戶誰進誰出、對手怎麼比價 | [[topics/market-signals-customers]] | 10-29 Financial Advisors 額度、Copilot Fusion |
| 學過哪些課、未上市的消息線各走到哪 | [[topics/market-lessons]] | 每週更新 |
````

其後接原 L87、L89 原文。

**原 L1521 改寫（里程碑記號說明，從里程碑節搬到這裡，四子頁共用）**

````markdown
每則的「下一個催化劑」登記在該子頁的「追蹤中的里程碑」，日報出現後續時會被偵測到。每筆怎麼讀：「標」是登記日、「查」是我們在日報裡盯的關鍵字、「複」是複查日、「訊」是日報出現後續的那天。
````

**同名指路殼（接 yann-lecun L49 的錨點）**

````markdown
#### 💰 Reuters 獨家：Anthropic IPO 招股書外流，首度書面警示 AI 存在性風險（2026-09-29）

這則判讀搬到了 [[topics/market-signals-ipo#💰 Reuters 獨家：Anthropic IPO 招股書外流，首度書面警示 AI 存在性風險（2026-09-29）]]。
%% 同名指路殼：接 [[entities/yann-lecun]] 的錨點；人物頁改指子頁後刪。h4 不吃 build_web 的 MARKET_SIGNAL_RE（只認 ###），不會被當成最新判讀。 %%
````

**`### 未歸類`**

````markdown
### 未歸類

%% 判不出該歸哪個子頁的新線先寫這裡（照常用 `### 💰` 格式，網站一樣讀得到），每週分派；路由見 .claude/reporter-rules/market/pages.md。 %%
目前沒有。
````

**`## 回顧結算` 合計表（接在原 L1407 說明之後；其後接原 L1502）**

````markdown
| 子頁 | 已結算 | ✅ 對 | ❌ 錯 | ～ 仍懸 | — 不可驗證 | ⏳ 待結算 |
|---|---|---|---|---|---|---|
| [[topics/market-signals-ipo]] | 17 | 2 | 0 | 14 | 1 | 8 |
| [[topics/market-signals-legal]] | 19 | 6 | 0 | 10 | 3 | 7 |
| [[topics/market-signals-compute]] | 8 | 1 | 1 | 1 | 5 | 6 |
| [[topics/market-signals-customers]] | 20 | 4 | 0 | 11 | 5 | 5 |
| **合計** | **64** | **13** | **1** | **36** | **14** | **26** |

數字截至 2026-11-02，逐列在各子頁的「回顧結算」。已結算 64 列裡 50 列是仍懸或不可驗證：兩週對官司、融資這類催化劑常常太短，命中率要等更多列定案才看得出來。
````

**拆頁評估（取代原 L1699）**

````markdown
%% 拆頁評估 2026-11-02：已拆（第 22 波，四子頁）。母頁留摘要、買得到的標的、子頁路由與四頁合計的命中率；88 則判讀連同各自的結算列與里程碑依線別下沉 market-signals-ipo／-legal／-compute／-customers。落選：三子頁（定價與算力合一約 670 行，出生即超 600）、延後 30 天不拆（上市日官方未公布）。`#### 💰 Reuters 獨家…` 是同名指路殼。成長約每月 50 則，四子頁 1–2 個月內會再逼近 600 行，屆時先蒸 2026-09 時段（12-01 起滿 3 個月）。 %%
````

純搬移（母頁）：原 L26–49、L51–75、L77–89、L1403–1408、L1502、L1516–1518、L1691–1698。原 L1688–1690（重複分隔線）、L90／L1501／L1503 空行不留。

## B. 子頁 `wiki/topics/market-signals-ipo.md`（IPO 與財務揭露這則怎麼判）

**標頭（H1、使命句、欄位、來歷備忘）**

````markdown
# IPO 與財務揭露這則怎麼判

IPO 走到哪一格、外流與 S-1 的數字該打幾折、評等消息怎麼讀——這類消息放進市場框架怎麼判。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/market-signals]]
**開始日期：** 2026-08-13
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-10-31
%% 2026-11-02 第 22 波自 [[topics/market-signals]] 拆出：IPO 進程 21 則與 S-1 風險因素、S-1 操作風險、Public Benefit Fund、競品估值各 1 則，連同各自的回顧結算列與追蹤中的里程碑原文照搬，歸群照線別（同一條線的後續判讀寫進同一頁）。 %%
````

**免責（同母頁原 L35–36 字樣）＋callout**

````markdown
> ⚠️ **教學型事件研究，非投資建議**
> 本頁把消息面事件拆成分析師的六個問題練習判讀，不推薦任何標的、不下買賣指令。作者非持牌投資顧問，讀者自負決策責任。

> **最新判讀**（2026-10-31）
> - **Blackstone 告訴投資人預期 Anthropic 上市後拿 BB 級信評**：[TechCrunch](https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/) 引 FT，推翻「2027 年前達投資級」說法；三大評等機構都還沒出手。
````

**`## 現在怎麼判`（每週重寫）**

````markdown
- **走到哪**：公開版 S-1 已於 10-26 提交，尚未生效；股數、價格區間與掛牌日官方都未公布。1.5 兆、2 兆這些估值都是投資人轉述，S-1 本身不含估值。
- **數字打幾折**：上半年淨損 807 億看起來最大，但多家引 S-1 指出約 724 億是非現金的公允價值變動，營業損失約 6.9 億；先拆會計科目再判方向。
- **評等**：KBRA 6 月給非投資級最高一檔、Blackstone 預期上市後 BB 級，標普、穆迪、惠譽都還沒出手。
- **下一個會讓答案變清楚的事**：承銷商公布定價區間。
- 一眼、結算與里程碑的記號怎麼讀見 [[topics/market-signals#近期判讀]]；你買得到的標的見 [[topics/market-signals#買得到的標的]]。
````

**`## 回顧結算` 開頭一句（其下接表頭原 L1409–1410 與本群結算列）**

````markdown
怎麼讀、四頁合計的命中率見 [[topics/market-signals#回顧結算]]。
````

**`## 相關`**

````markdown
- [[topics/market-signals]] — 買得到的標的、四頁合計的命中率
- [[topics/anthropic-ipo]] — IPO 與 S-1 的事實層
- [[topics/anthropic-business]] — 融資、估值與營收的事實層
- [[topics/market-lessons]] — 課程表、IPO 流程六格與 S-1 先看五處（週更）
````

判讀、結算列、里程碑的原行號逐筆見 `-proposal-map.md` 第二～四節。

## C. 子頁 `wiki/topics/market-signals-legal.md`（官司、監管與政府這則怎麼判）

**標頭（H1、使命句、欄位、來歷備忘）**

````markdown
# 官司、監管與政府這則怎麼判

官司、機關調查與政府採購的消息，會不會寫進 S-1 的風險因素、動到哪個數字。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/market-signals]]
**開始日期：** 2026-09-11
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-10-28
%% 2026-11-02 第 22 波自 [[topics/market-signals]] 拆出：訴訟、機關調查、政府採用與流失 15 條線 24 則，連同各自的回顧結算列與追蹤中的里程碑原文照搬，歸群照線別（同一條線的後續判讀寫進同一頁）。 %%
````

**免責（同母頁原 L35–36 字樣）＋callout**

````markdown
> ⚠️ **教學型事件研究，非投資建議**
> 本頁把消息面事件拆成分析師的六個問題練習判讀，不推薦任何標的、不下買賣指令。作者非持牌投資顧問，讀者自負決策責任。

> **最新判讀**（2026-10-28）
> - **Anthropic 擴大與 GSA 的合作，折扣提升到 40%**：官方 10-27 公告（[原文](https://www.anthropic.com/news/expanding-partnership-gsa)），延伸到州、地方、部落與屬地政府；採購量與合約金額未揭露。
> - **Anthropic 向加州州長表態，主張法院應有權封鎖風險模型**：提案尚未進正式法案。
````

**`## 現在怎麼判`（每週重寫）**

````markdown
- **會進風險因素的有三種**：訴訟（反壟斷合謀、Reddit 資料、音樂著作權）、機關調查（FTC 傳票）、政府客戶（五角大廈列黑名單後停用）。
- **還沒有一件落到金額**：沒有判決、罰款或和解數字，多數判讀停在敘事型；GSA 折扣 40% 是本頁少數帶數字的一則。
- **結算多半仍懸**：已結算 19 列裡 10 列「仍懸」，判決、和解、法案定案通常比兩週長。
- 一眼、結算與里程碑的記號怎麼讀見 [[topics/market-signals#近期判讀]]；你買得到的標的見 [[topics/market-signals#買得到的標的]]。
````

**`## 回顧結算` 開頭一句（其下接表頭原 L1409–1410 與本群結算列）**

````markdown
怎麼讀、四頁合計的命中率見 [[topics/market-signals#回顧結算]]。
````

**`## 相關`**

````markdown
- [[topics/market-signals]] — 買得到的標的、四頁合計的命中率
- [[topics/anthropic-government-policy]] — 政府採購、軍方與監管的事實層
- [[topics/anthropic-business]] — 訴訟與風險的事實層
- [[topics/market-lessons]] — 課程表與消息線走向（週更）
````

判讀、結算列、里程碑的原行號逐筆見 `-proposal-map.md` 第二～四節。

## D. 子頁 `wiki/topics/market-signals-compute.md`（算力與融資這則怎麼判）

**標頭（H1、使命句、欄位、來歷備忘）**

````markdown
# 算力與融資這則怎麼判

誰在借錢給 Anthropic 買算力、條件多貴，這則消息動到的是成本還是只有傳聞。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/market-signals]]
**開始日期：** 2026-09-16
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-10-30
%% 2026-11-02 第 22 波自 [[topics/market-signals]] 拆出：晶片商循環融資、Nscale 等 9 條線 14 則，連同各自的回顧結算列與追蹤中的里程碑原文照搬，歸群照線別（同一條線的後續判讀寫進同一頁）。 %%
````

**免責（同母頁原 L35–36 字樣）＋callout**

````markdown
> ⚠️ **教學型事件研究，非投資建議**
> 本頁把消息面事件拆成分析師的六個問題練習判讀，不推薦任何標的、不下買賣指令。作者非持牌投資顧問，讀者自負決策責任。

> **最新判讀**（2026-10-30）
> - **Nvidia 洽談為 Nscale 與 Anthropic 的雲端協議提供信用支持**：[Reuters](https://news.google.com/rss/articles/CBMixgFBVV95cUxOeFZKQnF5QVdNQlBQRzNMTE5PbjhUSXF0Y0NzYXpyaVJFeGplang3clhEYUtGUF9Fd2tPRjE0VllQVjV0cncwdU9za2RGZkFjQ2ZSTGdpQ3hXSkRBSjVtY2tvTzhEVTYtUkxYQjdfc1A3blJMd0c2ajJTUFp0eGMtOEtMbEk2NGl2Y2hrRFVlSHVaT1VQWi1qaGhLTkoyZVhXWFVFaXpDVEpZQV90MFNSZzN2dTl0WXJWZEhBRzJmUFVpNzI2Smc?oc=5) 引《The Information》，僅標題可用；對象、金額與條件未披露。
````

**`## 現在怎麼判`（每週重寫）**

````markdown
- **錢從三條路來**：晶片商與銀行安排的融資（Broadcom 630 億、Blackstone 雙位數殖利率私募信貸）、算力夥伴合約（Nscale、Akamai、SpaceX）、S-1 揭露逾 5,000 億的雲端承諾。
- **多數只有標題**：14 則裡 10 則硬度是單一標題，方向多判兩面或未定；10-29 銀行撤回德州資料中心債券是第一個實際受挫的訊號。
- **下一個會讓答案變清楚的事**：630 億融資定價發行、Nvidia 信用支持的條件。
- 一眼、結算與里程碑的記號怎麼讀見 [[topics/market-signals#近期判讀]]；你買得到的標的見 [[topics/market-signals#買得到的標的]]。
````

**`## 回顧結算` 開頭一句（其下接表頭原 L1409–1410 與本群結算列）**

````markdown
怎麼讀、四頁合計的命中率見 [[topics/market-signals#回顧結算]]。
````

**結算細節小標（複製原 L1506 字樣，接本群那一條）**

````markdown
**2026-10-03 結算細節**（上表「兩週後」欄原文，搬位置不刪）
````

**`## 相關`**

````markdown
- [[topics/market-signals]] — 買得到的標的、四頁合計的命中率
- [[topics/anthropic-business]] — 算力合約與融資的事實層
- [[topics/market-lessons]] — 課程表與消息線走向（週更）
````

判讀、結算列、里程碑的原行號逐筆見 `-proposal-map.md` 第二～四節。

## E. 子頁 `wiki/topics/market-signals-customers.md`（定價、通路與客戶這則怎麼判）

**標頭（H1、使命句、欄位、來歷備忘）**

````markdown
# 定價、通路與客戶這則怎麼判

價格怎麼改、客戶誰進誰出、對手怎麼比價，這則消息往毛利與成長率哪邊推。

**狀態：** ongoing
**領域：** 💼 商業
**上層：** [[topics/market-signals]]
**開始日期：** 2026-08-26
**最後更新：** 2026-11-02
**最後新聞更新：** 2026-10-29
%% 2026-11-02 第 22 波自 [[topics/market-signals]] 拆出：定價改版、企業採用等 16 條線 25 則，連同各自的回顧結算列與追蹤中的里程碑原文照搬，歸群照線別（同一條線的後續判讀寫進同一頁）。 %%
````

**免責（同母頁原 L35–36 字樣）＋callout**

````markdown
> ⚠️ **教學型事件研究，非投資建議**
> 本頁把消息面事件拆成分析師的六個問題練習判讀，不推薦任何標的、不下買賣指令。作者非持牌投資顧問，讀者自負決策責任。

> **最新判讀**（2026-10-29）
> - **Anthropic 給 Claude for Financial Advisors 用戶最高 4,800 美元額度**：[Citywire](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMHpXNmtnSGZiWFFLTzVfaG04VlNQbnpuZHUtTnozWHBVbFpCbk5yNWh1cmQzNFlrQUp3UlczaG9oSDg3Y0djVmZxRXJrd0JKaVY0TVpGa2JaVU9NRzFPdWVGYVVYdERzS0ltOHF5b0JvQlhoM19WWklPNHMxdTdiWmFlUUh1THFMckd2MVJkWDc5Z2haeVJ4bHNKVXFOLWZsN0NLa21PZXM?oc=5) 報導，僅標題可用；與 10-24 的 20 席門檻方向相反。
> - **GitHub Copilot Fusion 宣稱以一半 API 成本勝過 Claude Code**：基準測試方法未公開。
````

**`## 現在怎麼判`（每週重寫）**

````markdown
- **價格在降**：Opus 5.5、Haiku 5.5 牌價下修，Managed Agents 改毫秒計費；對毛利率的影響至今沒有一則被財報或 S-1 拆出來。
- **客戶兩邊都有**：具名擴大（Barclays、JPMorgan、Novo Nordisk）與具名縮減（Meta、Microsoft、Replit、Accenture 每月 29 美元上限）並存，金額多數未經官方證實。
- **線很散**：16 條線裡 14 條只有一則，單一消息很難看出方向，要對照「買得到的標的」表的同一列看。
- 一眼、結算與里程碑的記號怎麼讀見 [[topics/market-signals#近期判讀]]；你買得到的標的見 [[topics/market-signals#買得到的標的]]。
````

**`## 回顧結算` 開頭一句（其下接表頭原 L1409–1410 與本群結算列）**

````markdown
怎麼讀、四頁合計的命中率見 [[topics/market-signals#回顧結算]]。
````

**結算細節小標（複製原 L1506 字樣，接本群那一條）**

````markdown
**2026-10-03 結算細節**（上表「兩週後」欄原文，搬位置不刪）
````

**`## 相關`**

````markdown
- [[topics/market-signals]] — 買得到的標的、四頁合計的命中率
- [[entities/pricing]] — 訂閱與 API 計費事實
- [[topics/enterprise-tool-tracker]] — 具名企業採用與退出
- [[topics/competitor-landscape]] — 競品動態與定價對照
- [[topics/market-lessons]] — 課程表與消息線走向（週更）
````

判讀、結算列、里程碑的原行號逐筆見 `-proposal-map.md` 第二～四節。

## F. 照查證改的句子（判讀與里程碑內，原行：舊→新）

- 原 L181：
  ````text
  ### 💰 GSA 擴大 OneGov 合作：
  →
  ### 💰 GSA 擴大合作（媒體稱 OneGov）：
  ````
- 原 L185：
  ````text
  新資訊是 Anthropic 官方部落格宣布擴大與美國總務署（GSA）的 OneGov 合作，
  →
  新資訊是 Anthropic 官方部落格 10-27 宣布擴大與美國總務署（GSA）的合作（[原文](https://www.anthropic.com/news/expanding-partnership-gsa)；「OneGov」是媒體用語，官方頁不用此名），
  ````
- 原 L185：
  ````text
  未記錄過 GSA OneGov 這類
  →
  未記錄過 GSA 這類
  ````
- 原 L406：
  ````text
  HN 討論亦質疑此數字與先前「連續獲利」揭露的口徑是否一致。
  →
  HN 討論亦質疑此數字與先前「連續獲利」揭露的口徑是否一致——10-26 公開版 S-1 經多家引述給了答案：807 億裡約 724 億是可轉換票據、衍生負債與 SAFE 的公允價值變動（非現金，估值越高越大），營業損失約 6.9 億。
  ````
- 原 L447：
  ````text
  宣布捐出 5% 股權成立「Public Benefit Fund」公益信託
  →
  宣布將 5% 股權撥入全資子實體「Public Benefit Fund」
  ````
- 原 L451：
  ````text
  撥入新設「Public Benefit Fund」公益信託
  →
  撥入新設的全資子實體「Public Benefit Fund」
  ````
- 原 L451：
  ````text
  可持續加碼的股權捐贈
  →
  可持續加碼的股權撥入
  ````
- 原 L458：
  ````text
  公司把股權捐給公益信託
  →
  公司把股權撥入自設的公益實體
  ````
- 原 L459：
  ````text
  捐出的股權
  →
  撥出的股權
  ````
- 原 L1529：
  ````text
  **GSA OneGov 折扣擴大後
  →
  **GSA 折扣擴大後（媒體稱 OneGov）
  ````
- 原 L1547：
  ````text
  官方 10-18 宣布捐出 5% 股權
  →
  官方 10-18 宣布將 5% 股權撥入全資子實體
  ````
- 原 L1680：
  ````text
  ｜**公開版 S-1 尚未遞交**：官方 06-01 部落格證實機密遞交草案；09-20 查 SEC EDGAR 公開資料庫無符合結果，確認公開版仍未遞交。
  →
  ｜**當時公開版 S-1 尚未遞交**：官方 06-01 部落格證實機密遞交草案；09-20 查 SEC EDGAR 公開資料庫無符合結果。
  ````

**原 L1681（過時句，整行改寫並縮排）**

````markdown
  - 已過時（2026-11-02 查證）：公開版 S-1 已於 10-26 提交（見本節「公開版 S-1 已於 2026-10-26 提交 SEC」條），「10 月上市」的預期落空，股數、價格區間與掛牌日官方仍未公布。
````

**沒縮排的續行補兩格縮排（字不改）**：原 L1583、L1587、L1600、L1686；L1681 見上。原 L1543（與 L1567 同一事實的重複條，無懸置標記）砍——裁決點 N1。

# 進規則檔

每條「舊→新」都由 `rules_patch.py` 在臨時副本套用過（斷言舊字串唯一），`check_rules.py` 綠。

### `.claude/reporter-rules/market/pages.md`：從 `## topics/market-signals` 到檔尾整段換成

````markdown
## topics/market-signals（母頁）與四子頁

母頁是索引＋重要結論：摘要、買得到的標的、子頁路由、四頁合計的命中率。判讀、它的結算列與它的里程碑住同一個子頁（一則三件同頁）。

### 一則判讀寫進哪頁（路由）

照**線**歸頁：同一條線的後續判讀寫進該線已有判讀的那頁；開新線才照題材判。判不出的新線寫進母頁 `## 近期判讀` 下的 `### 未歸類`（照常用 `### 💰` 格式），每週分派——它不是預設子頁。

| 子頁 | 收哪些線 |
|---|---|
| `topics/market-signals-ipo` | IPO 進程、S-1 揭露（風險因素、操作風險、財務數字）、資本結構（如 Public Benefit Fund）、估值比較樣本 |
| `topics/market-signals-legal` | 訴訟、機關調查與執法、立法與遊說、政府採用與流失 |
| `topics/market-signals-compute` | 算力合約、晶片與資料中心融資、雲端承諾、算力成本 |
| `topics/market-signals-customers` | 定價改版、通路、具名企業採用與流失、競品比價 |

### 結論表的歸屬

| 表 | 住哪頁 | 誰維護、何時 | 一列是什麼 | 欄位 |
|---|---|---|---|---|
| `## 買得到的標的` | 母頁（摘要之後、近期判讀之前） | **你，每日**：判讀涉及上市公司時當天覆寫對應列 | 一個上市標的（主鍵＝代號）。入口：任一子頁有判讀提到它、或它是 Anthropic 的投資人；具名採用但無帶金額消息的上市公司不佔列，表下一句指 [[topics/enterprise-tool-tracker]] | 標的｜跟 Anthropic 的關係｜本頁判讀｜現在方向｜下一個催化劑 |
| `## 近期判讀` 路由表 | 母頁 | **你，每日**：寫了判讀就覆寫那個子頁那列的「最新一則」 | 一個子頁（＋教材頁一列） | 你想知道｜去哪頁｜最新一則 |
| `## 回顧結算` 合計表 | 母頁 | **主編，每週**（`/wiki-lint` 5h，見 `.claude/reporter-rules/market/weekly.md`） | 一個子頁＋合計列 | 子頁｜已結算｜✅ 對｜❌ 錯｜～ 仍懸｜— 不可驗證｜⏳ 待結算 |
| `## 現在怎麼判` | 各子頁（callout 之後） | **主編，每週**（5h）：整段重寫，≤ 4 條，只寫這週哪條線的答案變了；末條固定指回母頁的記號說明 | 一條結論 | — |
| `## 買不到的消息線（教材）` | `wiki/topics/market-lessons.md` | **主編，每週**（`/wiki-lint` 5h，見 `.claude/reporter-rules/market/weekly.md`） | 一條未上市主角的消息線（主鍵＝線名） | 線｜現在方向｜則數 · 最後一則｜下一個催化劑｜這條線的課 |
| `## 一課一課學` | `wiki/topics/market-lessons.md` | 同上 | 一課（主鍵＝課名；「複習：」開頭者不新增列，只在例題欄追加日期） | 課名｜下次怎麼認｜例題｜押對了嗎 |

你**只寫母頁與四子頁**；教材頁唯讀。教材頁的兩張表從你每則判讀的「一眼」（線名、正負）、「下一個催化劑」與「一課｜課名」機械抽出，所以這三段的形狀要守住，課名 ≤ 12 字且同一課第二次出現寫「複習：課名」。

`## IPO 這條線，你要先懂的`（教材頁）是通用知識，不吃日報、記者不動；主編每週順檢它與 IPO 線最新一則是否對得上，Anthropic 公開版 S-1 出現時把「S-1 打開先看五個地方」改成對照實際文件的五句。

### `## 回顧結算`（各子頁，累積，永久保留）

你每寫一則判讀就在**同一子頁**的回顧結算加一列 ⏳（欄值見 `.claude/reporter-rules/market/daily.md`「每日動作」第 2 步 c）；「兩週後」與「對錯」兩欄由主編於 `/wiki-lint` 5h 回填，**你不填**，母頁的合計表也是主編的。已結算列永久保留（表是判準的紀錄，不是待辦清單）；某子頁表長超過 20 列時，該頁最舊的時段依 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」處理。

### `## 追蹤中的里程碑`（各子頁）

每則判讀的「下一個催化劑」依 `.claude/reporter-rules/daily-contracts.md`「懸置標記語法」登記在**同一子頁**，探針寫得出可在 `news/*.md` grep 到的字串；日報出現後續時只能加 `訊 YYYY-MM-DD`，結案屬主編。記號怎麼讀的說明只住母頁 `## 近期判讀`，子頁不另抄。
````

### `.claude/reporter-rules/market/daily.md`

````text
**唯一負責頁面：** `wiki/topics/market-signals.md`（其餘頁面唯讀，含週更的教材頁 `wiki/topics/market-lessons.md`）。
→
**負責頁面：** `wiki/topics/market-signals.md`（母頁）與四子頁 `topics/market-signals-ipo`／`-legal`／`-compute`／`-customers`（一則判讀寫進哪頁見 `.claude/reporter-rules/market/pages.md`「路由」；其餘頁面唯讀，含週更的教材頁 `wiki/topics/market-lessons.md`）。
````

### `.claude/reporter-rules/market/daily.md`

````text
——本頁不複製任何事實敘述，
→
——這五頁不複製任何事實敘述，
````

### `.claude/reporter-rules/market/daily.md`

````text
`scripts/build_web.py` 的 `MARKET_SIGNAL_RE`（解析最新一則判讀，日期等於某日日報時在該日網站頁面注入 💰 條目）
→
`scripts/build_web.py` 的 `MARKET_SIGNAL_RE`（`market_signal_pages()` 讀母頁與上層指向它的子頁，取日期最新的一則；日期等於某日日報時在該日網站頁面注入 💰 條目）
````

### `.claude/reporter-rules/market/daily.md`

````text
新判讀 **prepend 進 `## 近期判讀`**（最新在上）。
→
新判讀 **prepend 進該子頁的 `## 近期判讀`**（最新在上；寫進哪頁照 `.claude/reporter-rules/market/pages.md`「路由」）。
````

### `.claude/reporter-rules/market/daily.md`

````text
2. 有六類消息 →（a）寫判讀 prepend 進 `## 近期判讀`；（b）判讀涉及上市公司時覆寫「買得到的標的」對應列；（c）`## 回顧結算` 表加一列
→
2. 有六類消息 →（a）寫判讀 prepend 進對應子頁的 `## 近期判讀`；（b）判讀涉及上市公司時覆寫母頁「買得到的標的」對應列；（c）同一子頁 `## 回顧結算` 表加一列
````

### `.claude/reporter-rules/market/daily.md`

````text
登記進 `## 追蹤中的里程碑`；（e）更新「最後更新」與「最後新聞更新」兩個日期欄位
→
登記進同一子頁 `## 追蹤中的里程碑`；（e）覆寫該子頁 callout、母頁 callout 與母頁 `## 近期判讀` 路由表該列的「最新一則」；（f）更新該子頁「最後更新」與「最後新聞更新」；母頁只更新「最後更新」，當天覆寫了標的表才連「最後新聞更新」一起更新，歸因同一則多回報一筆母頁
````

### `.claude/reporter-rules/market/daily.md`

````text
更新頁面：[topics/market-signals or 無]
→
更新頁面：[topics/market-signals-xxx（＋母頁）list or 無]
````

### `.claude/reporter-rules/market/weekly.md`

````text
1. 讀 `wiki/topics/market-signals.md` 的 `## 回顧結算` 表，
→
1. 讀四子頁（`wiki/topics/market-signals-ipo／-legal／-compute／-customers.md`）的 `## 回顧結算` 表，
````

### `.claude/reporter-rules/market/weekly.md`

````text
另看 `## 追蹤中的里程碑` 對應標記有沒有 `訊`
→
另看同一子頁 `## 追蹤中的里程碑` 對應標記有沒有 `訊`
````

### `.claude/reporter-rules/market/weekly.md`

````text
6. 更新頁面「最後更新」；**不動「最後新聞更新」**（回填是非新聞性維護）
→
6. 覆寫母頁 `## 回顧結算` 合計表（每子頁一列＋合計，表下寫數字截至日）與各子頁 `## 現在怎麼判`（≤ 4 條，只寫這週哪條線的答案變了，不 append）；更新動到的頁的「最後更新」；**不動「最後新聞更新」**（回填是非新聞性維護）
````

### `.claude/reporter-rules/market/weekly.md`

````text
表長超過 20 列時，最舊的時段依
→
某子頁表長超過 20 列時，該頁最舊的時段依
````

### `.claude/agents/wiki-reporter-market.md`

````text
負責 wiki/topics/market-signals.md 的每日消息面判讀
→
負責 wiki/topics/market-signals.md（母頁）與四子頁的每日消息面判讀
````

### `.claude/agents/wiki-reporter-market.md`

````text
你只寫一頁：`wiki/topics/market-signals.md`；
→
你只寫投資訊號母頁 `wiki/topics/market-signals.md` 與它的四個子頁（路由見規則檔）；
````

### `.claude/agents/wiki-reporter-market.md`

````text
3. `wiki/topics/market-signals.md` — 你唯一負責的頁面（動筆前先讀現況）
→
3. `wiki/topics/market-signals.md` 與這則要寫進的子頁 — 你負責的頁面（動筆前先讀現況；寫進哪頁見 `.claude/reporter-rules/market/pages.md`「路由」）
````

### `.claude/agents/wiki-reporter-market.md`

````text
- **只寫 `wiki/topics/market-signals.md`**；
→
- **只寫 `wiki/topics/market-signals.md` 與四子頁 `market-signals-ipo／-legal／-compute／-customers`**；
````

### `.claude/agents/wiki-reporter-market.md`

````text
- **`## 回顧結算` 的「兩週後」與「對錯」欄不由你填**
→
- **各子頁 `## 回顧結算` 的「兩週後」與「對錯」欄、母頁合計表、子頁 `## 現在怎麼判` 不由你填**
````

### `.claude/reporter-rules/page-lifecycle.md`

````text
路由見 `.claude/reporter-rules/features/pages.md` 第 0 條）；
→
路由見 `.claude/reporter-rules/features/pages.md` 第 0 條；`topics/market-signals` 的 `## 買得到的標的`——判讀涉及上市公司時覆寫，見 `.claude/reporter-rules/market/pages.md`）；
````

### `.claude/skills/wiki-lint-sweeps/references/sweeps.md`

````text
`wiki/topics/market-signals.md` 的判讀是**預測性宣稱**，本步是它唯一的結算端：對 `## 回顧結算` 表中
→
`wiki/topics/market-signals.md` 四子頁（`-ipo／-legal／-compute／-customers`）的判讀是**預測性宣稱**，本步是它唯一的結算端：對各子頁 `## 回顧結算` 表中
````

### `.claude/skills/wiki-lint-sweeps/references/sweeps.md`

````text
回填「兩週後」與「對錯」；接著
→
回填「兩週後」與「對錯」，再覆寫母頁 `## 回顧結算` 合計表與各子頁 `## 現在怎麼判`；接著
````

### `.claude/reporter-rules/commercial/daily.md`

````text
> **唯一例外：`wiki/topics/market-signals.md`**——該頁領域雖為 💼 商業，但由**投資分析記者**維護（`.claude/reporter-rules/market/daily.md`），你不寫該頁的判讀內容；懸置掃描把該頁的標記派給你時，照共用規則只加 `訊`。
→
> **唯一例外：`wiki/topics/market-signals.md` 與四子頁 `market-signals-ipo／-legal／-compute／-customers`**——領域雖為 💼 商業，但由**投資分析記者**維護（`.claude/reporter-rules/market/daily.md`），你不寫這五頁；懸置掃描的命中直接派給投資分析記者（`scripts/pending_markers.py` 的 `PAGE_TO_REPORTER`），你不會收到。
````

### `.claude/review-registry.json`

````text
        "### 💰 事件名（YYYY-MM-DD）|MARKET_SIGNAL_RE",
        "market-signals"
      ],
→
        "### 💰 事件名（YYYY-MM-DD）|MARKET_SIGNAL_RE",
        "market-signals",
        "market_signal_pages"
      ],
````

### `src/DesignDocument/Design Diagram.md`

````text
→ wiki/topics/market-signals.md 判讀
→
→ wiki/topics/market-signals 母頁＋四子頁判讀
````

# 進腳本

臨時副本 `git diff -U2` 原樣（`<scratchpad>/w22/design/scripts.diff`）。驗紅：把新測試檔放進「頁已拆、腳本未改」的副本跑，13 個案例紅（見 proposal 閘表）。

````diff
diff --git a/scripts/build_web.py b/scripts/build_web.py
index 82c158a..28e8f16 100644
--- a/scripts/build_web.py
+++ b/scripts/build_web.py
@@ -878,5 +878,5 @@ def attach_sedimented_badges(digest_all: dict, entities: list, topics: list,
 
 
-# ── 投資訊號（wiki/topics/market-signals.md → 日報頁 💰 條目）───────────────
+# ── 投資訊號（wiki/topics/market-signals.md 與其子頁 → 日報頁 💰 條目）──────────
 # 判讀標題是規格與程式的共同契約：`### 💰 事件名（YYYY-MM-DD）`。規格端住
 # `.claude/reporter-rules/market/daily.md`「判讀格式（機械契約字串）」表，兩端互相指認
@@ -887,12 +887,31 @@ MARKET_SIGNAL_RE = re.compile(r"^###\s+💰\s*(.+?)（(\d{4}-\d{2}-\d{2})）\s*$
 
 
-def parse_market_signal(f: Path) -> dict | None:
-    """取最新一則判讀（頁面 `## 近期判讀` 最新在上，故第一個命中即最新）。"""
-    if not f.exists():
-        return None
-    m = MARKET_SIGNAL_RE.search(read_md(f))
-    if not m:
-        return None
-    return {"title": m.group(1).strip(), "date": m.group(2)}
+def market_signal_pages(root_page: Path = MARKET_SIGNALS_PAGE) -> list[Path]:
+    """母頁＋標頭 `**上層：** [[topics/market-signals]]` 指向它的子頁（2026-11-02 第 22 波起判讀住四子頁）。
+    子頁清單從上層欄現算、不寫死：日後增減子頁不必改這裡，漏改也不會讓 💰 條目靜默消失。"""
+    slug = f"{root_page.parent.name}/{root_page.stem}"
+    pages = [root_page]
+    for f in sorted(root_page.parent.parent.glob("*/*.md")):
+        if f == root_page:
+            continue
+        m = META_RE["parent"].search("\n".join(read_md(f).splitlines()[:60]))
+        if m and m.group(1).strip() == slug:
+            pages.append(f)
+    return pages
+
+
+def parse_market_signal(pages: Path | list[Path]) -> dict | None:
+    """取子樹裡最新的一則判讀。每頁 `## 近期判讀` 最新在上，故各頁第一個命中即該頁最新；
+    跨頁取日期最大者，同日取清單先出現者（母頁在前、子頁依檔名）。"""
+    if isinstance(pages, Path):
+        pages = [pages]
+    best = None
+    for f in pages:
+        if not f.exists():
+            continue
+        m = MARKET_SIGNAL_RE.search(read_md(f))
+        if m and (best is None or m.group(2) > best["date"]):
+            best = {"title": m.group(1).strip(), "date": m.group(2), "page": f.stem}
+    return best
 
 
@@ -1831,5 +1850,5 @@ def build():
     # 讀者版的日期不注入：市場記者的判讀本就是當日 wiki diff 的一部分，
     # 由讀者版自己寫在 💼 商業節末一條——注入與自寫擇一，不要雙份。
-    _signal = parse_market_signal(MARKET_SIGNALS_PAGE)
+    _signal = parse_market_signal(market_signal_pages())
     if _signal and _signal["date"] in reader_all:
         _signal = None
diff --git a/scripts/check_wiki_freshness.py b/scripts/check_wiki_freshness.py
index 078955a..4db0e34 100644
--- a/scripts/check_wiki_freshness.py
+++ b/scripts/check_wiki_freshness.py
@@ -76,5 +76,5 @@ DERIVED_PAGES = {
     "topics/market-lessons":
         ".claude/reporter-rules/market/weekly.md「教材頁週更」"
-        "（週更，吃 market-signals 的判讀與結算表，非新聞條目；每日 ingest 不更新）",
+        "（週更，吃 market-signals 四子頁的判讀與結算表，非新聞條目；每日 ingest 不更新）",
     "topics/claude-code-experimental":
         ".claude/reporter-rules/features/daily.md 負責頁面表「Build Flags」列"
diff --git a/scripts/pending_handoffs.py b/scripts/pending_handoffs.py
index 91a54f2..10474e4 100644
--- a/scripts/pending_handoffs.py
+++ b/scripts/pending_handoffs.py
@@ -52,5 +52,7 @@ DOMAIN_TO_CATEGORY = {"模型": "模型", "工具/功能": "功能", "商業": "
 # （.claude/reporter-rules/commercial/daily.md）；feature-radar 不在目錄表，歸功能記者
 OWNER_OVERRIDES = {"topics/market-signals": "投資分析", "feature-radar": "功能",
-                   "topics/coding-workflow-guide": "開發實務"}
+                   "topics/coding-workflow-guide": "開發實務",
+                   # 四子頁沿 parent 也推得到投資分析；明列是讓 owner_of 不必依賴 frontmatter 已生成
+                   **{f"topics/market-signals-{s}": "投資分析" for s in ("ipo", "legal", "compute", "customers")}}
 _WIKILINK = re.compile(r"\[\[([^\]|#]+)")
 _PARENT = re.compile(r'^parent:[ \t]*"?([^"\r\n]*?)"?[ \t]*$', re.MULTILINE)
diff --git a/scripts/pending_markers.py b/scripts/pending_markers.py
index 3e3941a..fc82ece 100644
--- a/scripts/pending_markers.py
+++ b/scripts/pending_markers.py
@@ -510,6 +510,9 @@ def page_domain(path: Path) -> str | None:
 
 
-# 領域欄推不出真正負責人的頁（同 pending_handoffs.OWNER_OVERRIDES）：手冊領域是工具/功能、由開發實務記者維護
-PAGE_TO_REPORTER = {"topics/coding-workflow-guide": "wiki-reporter-devpractice"}
+# 領域欄推不出真正負責人的頁（同 pending_handoffs.OWNER_OVERRIDES）：手冊領域是工具/功能、由開發實務記者維護；
+# 投資訊號母頁與四子頁領域是商業、由投資分析記者維護（缺這列時命中全派給商業記者，2026-11-02 第 22 波查到 285 筆）
+PAGE_TO_REPORTER = {"topics/coding-workflow-guide": "wiki-reporter-devpractice",
+                    **{f"topics/market-signals{s}": "wiki-reporter-market"
+                       for s in ("", "-ipo", "-legal", "-compute", "-customers")}}
 
 
diff --git a/scripts/scan_pending_verifications.py b/scripts/scan_pending_verifications.py
index 0c7f61d..eb4966d 100644
--- a/scripts/scan_pending_verifications.py
+++ b/scripts/scan_pending_verifications.py
@@ -81,4 +81,5 @@ REPORTER_LABEL = {
     "wiki-reporter-people": "人物",
     "wiki-reporter-devpractice": "開發實務",
+    "wiki-reporter-market": "投資分析",
 }
 # 顯示順序依 DOMAIN_TO_REPORTER 的 domain 插入順序（模型/功能/商業/安全政策/社群/人物），
diff --git a/src/tests/test_market_signals.py b/src/tests/test_market_signals.py
index 07bc7ee..9aede01 100644
--- a/src/tests/test_market_signals.py
+++ b/src/tests/test_market_signals.py
@@ -6,5 +6,6 @@
 的死法。本檔把三件事釘住：
 
-  1. 取的是最新一則（頁面最新在上）且標題／日期解析正確
+  1. 取的是子樹裡最新一則（各頁最新在上、跨頁比日期）且標題／日期／所在頁解析正確
+     （2026-11-02 第 22 波起判讀住四子頁，母頁沒有 `### 💰`；只讀母頁的話 💰 條目會靜默消失）
   2. 日期對得上的那天才注入 marketSignal，其餘日期不動
   3. 頁面不存在或無任何判讀時回 None（無訊號的日子頁面本來就不動）
@@ -45,5 +46,19 @@ class TestParseMarketSignal(unittest.TestCase):
     def test_takes_latest_entry(self):
         sig = build_web.parse_market_signal(self._write(PAGE))
-        self.assertEqual(sig, {"title": "最新事件名", "date": "2026-09-04"})
+        self.assertEqual(sig, {"title": "最新事件名", "date": "2026-09-04", "page": "market-signals"})
+
+    def test_takes_latest_across_pages(self):
+        """子頁的日期比母頁新 → 取子頁那則，並帶出所在頁（網站點擊直達子頁）。"""
+        d = Path(tempfile.mkdtemp())
+        (d / "market-signals.md").write_text("# 母頁\n\n本頁不放判讀。\n", encoding="utf-8")
+        (d / "market-signals-ipo.md").write_text(PAGE, encoding="utf-8")
+        (d / "market-signals-legal.md").write_text("### 💰 更新的一則（2026-09-05）\n", encoding="utf-8")
+        sig = build_web.parse_market_signal([d / "market-signals.md", d / "market-signals-ipo.md",
+                                             d / "market-signals-legal.md"])
+        self.assertEqual(sig, {"title": "更新的一則", "date": "2026-09-05", "page": "market-signals-legal"})
+
+    def test_h4_shell_is_not_a_signal(self):
+        """母頁的同名指路殼用 h4，不得被當成判讀（只認 ###）。"""
+        self.assertIsNone(build_web.parse_market_signal(self._write("#### 💰 殼（2026-09-29）\n")))
 
     def test_missing_page_returns_none(self):
@@ -85,15 +100,26 @@ class TestAttachMarketSignal(unittest.TestCase):
 
 
+CHILDREN = {"market-signals-ipo", "market-signals-legal", "market-signals-compute", "market-signals-customers"}
+
+
 class TestRealPage(unittest.TestCase):
-    def test_live_page_parses_if_it_has_entries(self):
+    def test_subtree_found_by_parent_field(self):
+        """子頁清單從標頭「上層」現算：四子頁都要被找到（漏一頁＝那頁的判讀永遠上不了網站）。"""
         page = REPO_ROOT / "wiki" / "topics" / "market-signals.md"
         if not page.exists():
-            self.skipTest("market-signals.md 尚未建立")
-        text = page.read_text(encoding="utf-8")
-        if "### 💰" not in text:
+            self.skipTest("market-signals.md 不存在")
+        found = {f.stem for f in build_web.market_signal_pages(page)}
+        self.assertTrue(CHILDREN <= found, f"上層指向 market-signals 的子頁少了：{CHILDREN - found}")
+
+    def test_live_subtree_parses_if_it_has_entries(self):
+        pages = build_web.market_signal_pages()
+        texts = [f.read_text(encoding="utf-8") for f in pages if f.exists()]
+        if not any("### 💰" in t for t in texts):
             self.skipTest("正式頁目前無判讀條目")
-        sig = build_web.parse_market_signal(page)
-        self.assertIsNotNone(sig, "正式頁有 ### 💰 標題卻解析不出——標題形狀已漂")
+        sig = build_web.parse_market_signal(pages)
+        self.assertIsNotNone(sig, "子樹有 ### 💰 標題卻解析不出——標題形狀已漂")
         self.assertRegex(sig["date"], r"^\d{4}-\d{2}-\d{2}$")
+        newest = max(m[1] for t in texts for m in build_web.MARKET_SIGNAL_RE.findall(t))
+        self.assertEqual(sig["date"], newest, "取到的不是子樹裡最新的一則")
 
     def test_disclaimer_callout_is_first_callout(self):
@@ -104,10 +130,32 @@ class TestRealPage(unittest.TestCase):
         掃了只會誤報。
         """
-        page = REPO_ROOT / "wiki" / "topics" / "market-signals.md"
-        if not page.exists():
-            self.skipTest("market-signals.md 不存在")
-        body = page.read_text(encoding="utf-8").split("\n# ", 1)[-1]
-        first_callout = next((ln for ln in body.splitlines() if ln.startswith(">")), "")
-        self.assertIn("非投資建議", first_callout)
+        for name in ["market-signals", *sorted(CHILDREN)]:
+            page = REPO_ROOT / "wiki" / "topics" / f"{name}.md"
+            if not page.exists():
+                continue
+            with self.subTest(page=name):
+                body = page.read_text(encoding="utf-8").split("\n# ", 1)[-1]
+                first_callout = next((ln for ln in body.splitlines() if ln.startswith(">")), "")
+                self.assertIn("非投資建議", first_callout)
+
+
+class TestOwnership(unittest.TestCase):
+    """懸置命中與轉知帳都要派給投資分析記者——領域欄是商業，沒有覆寫就會派給商業記者
+    （第 22 波查到 data/pending-signals.jsonl 本頁 285 筆命中全記在商業記者名下）。"""
+
+    def test_pending_hits_go_to_market_reporter(self):
+        pm = load_script_module("pending_markers")
+        spv = load_script_module("scan_pending_verifications")
+        for name in ["market-signals", *sorted(CHILDREN)]:
+            with self.subTest(page=name):
+                r = pm.reporter_of(pm.WIKI_DIR / "topics" / f"{name}.md")
+                self.assertEqual(r, "wiki-reporter-market")
+                self.assertEqual(spv.REPORTER_LABEL.get(r), "投資分析", "標籤缺了，scan 的分組輸出會整組漏印")
+
+    def test_handoff_owner_is_market(self):
+        ph = load_script_module("pending_handoffs")
+        for name in ["market-signals", *sorted(CHILDREN)]:
+            with self.subTest(page=name):
+                self.assertEqual(ph.OWNER_OVERRIDES.get(f"topics/{name}"), "投資分析")
 
 
diff --git a/src/tests/test_reader_tags.py b/src/tests/test_reader_tags.py
index 9fa6c4f..5dfe15c 100644
--- a/src/tests/test_reader_tags.py
+++ b/src/tests/test_reader_tags.py
@@ -70,4 +70,8 @@ class TestDecidedExclusions(unittest.TestCase):
     EXCLUDED = {
         "market-signals": "投資訊號判讀，不是程式（使用者原話：「market signal 不是程式」）",
+        "market-signals-ipo": "同 market-signals（第 22 波拆出的子頁）",
+        "market-signals-legal": "同 market-signals（第 22 波拆出的子頁）",
+        "market-signals-compute": "同 market-signals（第 22 波拆出的子頁）",
+        "market-signals-customers": "同 market-signals（第 22 波拆出的子頁）",
         "competitor-landscape": "競品雷達＝市場在幹嘛；「別家誰強」的主出口 model-task-leaderboard 已在名單",
         "anthropic-business": "估值／IPO／營收，跟寫 code 的距離同 market-signals",
diff --git a/web_reader/assets/app.js b/web_reader/assets/app.js
index 492aa41..8e1fbad 100644
--- a/web_reader/assets/app.js
+++ b/web_reader/assets/app.js
@@ -322,8 +322,8 @@
       parts.push(`<li class="focus-item"><span class="focus-tag focus-tag--${cls}">${esc(f.tag)}</span><span>${esc(f.text)}</span>${refs}</li>`);
     });
-    // 投資訊號（wiki/topics/market-signals.md 的最新判讀日期＝本日時才有）：
+    // 投資訊號（wiki/topics/market-signals.md 子樹最新判讀日期＝本日時才有；page＝判讀所在子頁）：
     // 沿用 focus-item 版式接在聚焦列表末尾，點擊進判讀頁。教學型事件研究、非投資建議。
     if (d.marketSignal) {
-      parts.push(`<li class="focus-item focus-item--market"><span class="focus-tag focus-tag--market">投資訊號</span><button type="button" class="focus-item__link" onclick="openWikiPage('market-signals','topic')">${esc(d.marketSignal.title)} — 看判讀 →</button></li>`);
+      parts.push(`<li class="focus-item focus-item--market"><span class="focus-tag focus-tag--market">投資訊號</span><button type="button" class="focus-item__link" onclick="openWikiPage('${esc(d.marketSignal.page || 'market-signals')}','topic')">${esc(d.marketSignal.title)} — 看判讀 →</button></li>`);
     }
     parts.push('</ul>');
@@ -958,4 +958,5 @@ ${pmxOpenBtn(s.page, `看「${s.name}」的 wiki 頁`)}`;
     'community-tech-patterns': '社群工作流', 'recursive-self-improvement': 'AI 自我改進',
     'safety-china-trust-dispute': '中美信任', 'market-signals': '投資訊號', 'code-quality-decline': '效能退步',
+    'market-signals-ipo': '投資·IPO', 'market-signals-legal': '投資·官司監管', 'market-signals-compute': '投資·算力融資', 'market-signals-customers': '投資·定價客戶',
   };
   const PPL_ORBIT_KEY = 'claude-news-ppl-orbit';
````
