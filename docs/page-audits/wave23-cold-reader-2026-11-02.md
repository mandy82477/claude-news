# Wave 23 冷讀者實測：Anthropic 的生意與合作會不會影響我用的 Claude（2026-11-02）

**讀者設定：** 用 Claude 做開發的工程師，第一次來，只從 `wiki/index.md` 出發沿 `[[連結]]` 走。
**聲明：** 系統自動把專案根目錄 `CLAUDE.md` 與 `wiki/CLAUDE.md` 載進了 context（非我主動讀取）。後者含「搜尋策略」與資訊架構哲學，我沒有照它的路徑走（沒用 wiki_search／wiki_graph／log），但它讓我知道 `↳ 子故事` 的意思、`%% %%` 會被網站剝除——一般冷讀者不會知道。除此之外只讀了 wiki 頁面；單頁內用了列標題與頁內找字。
**開過的頁：** index → topics/anthropic-business → topics/anthropic-ipo → entities/google-investment → entities/pricing（#通路與乘數）→ topics/competitor-landscape（雷達＋雷達細節）→ topics/anthropic-government-policy（摘要＋線表）。
行號都指原始 .md 檔。

---

## 1. 四題逐題

### Q1 年營收多少、成長多快、誰說的、可信嗎
- **路徑：** index:137 → topics/anthropic-business「現在的數字」（**1 跳**）；為了核對成長率再到 topics/anthropic-ipo:72、107（2 跳）
- **結果：** 拿到（成長率只能算半拿到）
- **答案在哪：** anthropic-business:49-56（指標表：ARR $650 億、Q3 單季 $168 億、H1 淨損 $807 億，每列有「來源等級」）、:62（來源等級由硬到軟的定義）、:71（H1 營收 $163 億 vs 前一年同期 $11 億）、:78（Q1 $48 億補齊季度走勢）；anthropic-ipo:72（S-1 營收成長 14 倍）。「誰說的、可不可信」那欄設計得好，一眼就看得到哪些是官方一手、哪些是媒體引公司。
- **卡住的原句：**
  - anthropic-business:74「本季營收**年增率**已從上季 146% 放緩至約 45%」，對照 :43「季增約 46%」、:75「本季季增約 46%，上季為 140%」、:78「原文稱季營收**年增**近 50%」。同一個數字，一下寫年增、一下寫季增。拿 :71 算一下（前一年 H1 只有 $11 億），年增不可能只有 45%，所以 :74 應該是季增被寫成了年增。我看不出到底成長多快。ipo:107 也照抄了同一句。
  - 「一年營收多少」沒有直接寫出來的一句：ARR $650 億（:53）是 07 月的數字，已經三個月了；2025 全年營收頁上沒寫，只能從 ipo:123（$21.6 億＝47%）自己反推出約 $46 億。

### Q2 最近哪個合作會改到我用的 Claude（價格、地區、速度、容量）
- **路徑：** index:137 → anthropic-business「哪個合作會改到你用的 Claude」 → entities/pricing「通路：誰定價、怎麼開票」（**2 跳**）
- **結果：** 半拿到
- **答案在哪：**
  - 價格：anthropic-business:338（GSA 政府折扣 40%）、:339（Bedrock 沒有 50% Batch 折扣）、:343（Foundry CCU）；pricing:229-243
  - 地區：anthropic-business:339（Bedrock 首爾／新加坡新增境內推論）；pricing:252-253（資料落地與地區端點 ×1.1）
  - 速度：只有 pricing:261（Opus 5.5 fast mode 開放到 Google Cloud 與 Foundry），**anthropic-business 的合作表沒收這條**
  - 容量：anthropic-business:326「目前唯一寫得出的算力吃緊後果」只有 07-18 那一則
  - 「訂閱用戶不受影響」寫在 :347，這句很有用
- **卡住的原句：**
  - anthropic-business:293-311 算力總表 17 列幾乎都寫「目前無可見後果」。我想知道的「容量會不會變多」完全沒有答案。
  - :300 SpaceX 列也寫「目前無可見後果」，可是它引的官方公告網址叫 `higher-limits-spacex`，看起來那次就是調高了額度，跟這欄的說法對不上。
  - :341 Vertex 新路線標「單一來源各一」，我不知道該不該信。
  - 表的「最後動態」多是 09 月，10 月唯一的新列是 GSA，那只跟政府採購有關，答不了「最近」。

### Q3 還沒過去的商業風險、哪條最可能波及我
- **路徑：** index:137 → anthropic-business「還沒過去的風險」 → topics/anthropic-ipo「S-1 揭露了什麼」 → topics/anthropic-government-policy 線表（**3 跳**）
- **結果：** 半拿到
- **答案在哪：**
  - 官司：anthropic-business:223（音樂著作權）、:226（UTRF 專利，「全部使用者，求償含禁制令」）
  - 虧損：anthropic-business:56、:71；anthropic-ipo:71、:78（BB 信評＝融資成本偏高）
  - 客戶／通路集中：anthropic-ipo:122-123（2025 年 47% 營收經 Amazon／Google 市集賣出、兩家未具名客戶各占 12%）
  - 依賴少數供應商：anthropic-ipo:76（Google $1,140 億、AWS $1,100 億、Broadcom $1,610 億、SpaceX $1,200 億）
  - 政府：government-policy 線表（五角大廈那條標「不會」改到商用）
- **卡住的原句：**
  - anthropic-business:218「只列現在還在動、而且答得出『你能先做什麼』的風險」。結果題目問的四類裡，虧損、客戶集中、供應商依賴三類都不在表上，要再跳到 IPO 頁才找得到。:324 一句「Amazon／Google 通路集中……見 [[topics/anthropic-ipo]]」是唯一的指路。
  - 「哪一條最可能波及到我」沒有任何一頁替我排序。嚴重度（:229）只量「有沒有人改了做法」，不量「會不會波及個人開發者」。我自己推論最可能波及我的是 :225 訂閱補貼收窄，加上 ipo:73「企業大戶 20:1 → 個人訂閱要留意收窄」，但這是我拼出來的。
  - 細節區 :240-285 共 45 行混著評論、唱空、追蹤，讀不出哪條還活著。

### Q4 跟 Google、Amazon、Microsoft 各是什麼關係
- **路徑：** index:62 → entities/google-investment → 回 anthropic-business 算力表與合作表 → topics/competitor-landscape 雷達（**3 跳**；Amazon、Microsoft 在 index 都沒有入口）
- **結果：** 半拿到（Google 拿到，Amazon、Microsoft 要自己從各段拼）
- **答案在哪：**
  - **Google**
    - 投資人：google-investment:43、:54，anthropic-business:310
    - 供應商：google-investment:77（TPU），anthropic-ipo:76
    - 通路：anthropic-business:341，pricing:234
    - 競爭者：competitor-landscape:53、:136-139，google-investment:69
    - 帶頭找融資的角色：anthropic-business:514
  - **Amazon**
    - 投資人：只有 anthropic-business:464 埋在一段蒸餾彙整裡的「Amazon（2023–2024，$40 億）」，以及 google-investment:71「Amazon 也是重要投資者」（沒寫金額）
    - 供應商：anthropic-business:309，anthropic-ipo:76
    - 通路：anthropic-business:339-340
    - 客戶：anthropic-business:272（Alexa 降低依賴）、:387（Seller Assistant）
  - **Microsoft**
    - 通路：anthropic-business:343
    - 客戶在降低依賴：anthropic-business:275（Suleyman「目標是降低並最終消除這筆成本」）、:274
    - 競爭者：competitor-landscape:52、:176-180
    - 有沒有投資 Anthropic：查不到
- **卡住的原句：**
  - index 沒有任何一列在回答「跟三大雲的關係」，:62 只寫了 Google。
  - google-investment:71「Amazon 也是 Anthropic 的重要投資者，形成多方大廠支持格局」寫到這裡就斷了，沒有連結。
  - anthropic-business:464「歷史投資——Google（2024，$400 億……）、Amazon（2023–2024，$40 億）」：Google 的年份跟 google-investment:32、:43 寫的 2026-04-24 不一樣。

---

## 2. 入口
- **index:137（topics/anthropic-business）** 是 Q1-Q3 唯一的入口。鉤子「現在的數字、合作會不會改到你的帳單」直接對上 Q1、Q2，**很直覺**。但這格開頭是「S-1 已提交、淨損 807 億」，風險這件事沒有寫在鉤子裡，Q3 是硬著頭皮點進去的。
- **Q4 沒有直覺入口。** 只有 index:62 的 Google；Amazon、Microsoft 在 Entities 表只出現在人物列的描述裡（index:94 Suleyman），看起來像是講人，不像是講公司關係。
- index:138 market-signals、index:139 market-lessons 標了「投資判讀」，工程師看了不會點，這是對的。但 :138 的 `↳ market-signals-customers` 看起來像是「客戶集中」的家，讓人猶豫要不要點。

## 3. 分不出差別的兩頁
- **topics/anthropic-business「還沒過去的風險」＋「現在的數字·數字細節」 vs topics/anthropic-ipo「S-1 揭露了什麼」。** S-1 的淨損、算力承諾、企業採用「早期階段」、訓練暫停兩頁都寫：
  - 淨損：business:67/:71 vs ipo:71
  - 算力承諾：business:68 vs ipo:76/:100
  - 訓練暫停：business:242 vs ipo:75
  - 頁首 ipo:40 說 IPO 頁講的是「供應商穩定性與定價走向」，但那正是 Q3 想問的風險。我分不出風險的家到底在哪一頁。

## 4. 百科還是雷達
| 頁 | 判定 | 理由 |
|---|---|---|
| index | 百科（地圖） | 慢變路由，不過 :137 鉤子塞了日期和金額 |
| topics/anthropic-business | **雷達** | 1048 行，頭 330 行是結論表，後面 700 行是合作清單與時序；指標表會換手（:64） |
| topics/anthropic-ipo | 雷達 | 逐日細節（:83 起）占大半 |
| entities/google-investment | 百科（而且已休眠） | 最後新聞 07-24；狀態寫「resolved（後續新輪融資進行中）」 |
| entities/pricing（通路與乘數節） | 百科 | 通路表、乘數表穩定，有查證日 |
| topics/competitor-landscape | 雷達 | 對手雷達加逐日時序 |
| topics/anthropic-government-policy | 雷達 | 八條線狀態表加時序 |

## 5. 內部用語外洩（網站可見，不含 `%% %%` 內）
1. anthropic-business:176、:189「⟨Q-01⟩」「`⟨Q-nn⟩` 是這一格還沒查實的地方」：讀者看不懂短標記
2. anthropic-business:282「🔎 **查無官方**（標 2026-08-13｜查 Post-Crescent、著作權訴訟｜複 2026-11-10）」：標／查／複是懸置語法
3. anthropic-ipo:81「🔎 **查無官方**（標 2026-11-01｜查 EDGAR、Anthropic S-1｜複 2026-11-15）」：同上
4. anthropic-business:244-247「**訊 2026-10-26 追蹤**」：「訊」是內部標記
5. anthropic-business:95「（未列入指標表，2026-10-21 讓位）」、:87 同類：「讓位」是表格維運語言
6. anthropic-business:238「本輪另移出『雲端夥伴以自研模型替代』，結論見下方細節區標記」：寫給維護者看的
7. anthropic-business:353「其餘合作（一行制，日期倒序）」、:464「一行制清單已蒸餾」：「一行制」「蒸餾」是內部用語
8. anthropic-business:198「（見『IPO 追蹤』 表）」：本頁沒有這一節，是舊節名
9. anthropic-business:69、:117、:119 等「（Google News/The New York Times；Google News/The New Stack）」：「Google News/」是爬蟲來源前綴，讀者會以為報導出自 Google
10. anthropic-ipo:118「回答的是『是否仍會上市』而非⟨Q-03⟩『何時上市』」：引用另一格的短標記

## 6. 撐不起的句子
1. **anthropic-business:74**（ipo:107 同句）「年增率已從上季 146% 放緩至約 45%」：跟 :75「季增約 46%」、:71「前一年 H1 $11 億」互相矛盾，年增率不可能是 45%
2. **anthropic-business:464**「Google（2024，$400 億）」：跟 google-investment:32/:43、本頁 :310 寫的 2026-04-24 衝突
3. **anthropic-business:300** SpaceX「目前無可見後果」：同一格引的官方公告叫 higher-limits-spacex，看起來就是調高額度那次。:326「唯一寫得出的算力吃緊後果」也因此站不住
4. **anthropic-business:351**「Nscale 單筆 450 億 ≈ 年化營收 69%……單月算力承諾已逼近年化營收本身量級」：拿多年期合約的總額去比一年的營收，單位對不上
5. **anthropic-business:309** AWS「承諾逾 $1,000 億（推論）」：同頁 :68 已經有 S-1 的 $1,100 億，表沒更新，還標著推論
6. **anthropic-business:115**「收入結構更接近雲端供應商而非 SaaS 公司」：依據是一條 06-16 已暫停的政策（:108）
7. **anthropic-ipo:76**「容量有長約保障，服務不易斷供」：這是推論，卻寫成結論，沒標推論
8. **anthropic-business:53** ARR $650 億放在「現在的數字」：資料是 07 月的，Q3 都已經有了，這欄卻沒標「舊」
9. **entities/google-investment:47**「新一輪 $500 億融資……見 [[entities/pricing]]」：融資的家不在計費頁，連錯地方

## 7. 最想改的三件事
1. **「現在的數字」補一句年營收、修好成長率。** 用一句話寫「2025 全年約 $X 億（S-1）；目前 Q3 單季 $168 億、季增 46%」，並更正 :74／ipo:107 的「年增」錯字。這是 Q1 唯一的硬傷。
2. **新增「三大雲各是什麼關係」對照表**，放在 anthropic-business，index:137 鉤子加一句。四欄是投資人／算力供應商／銷售通路／客戶或競爭者，每格附金額與連結。Amazon 投資和 Microsoft 有沒有持股要查證補上，同時修 :464 的 Google 年份。現在 Q4 要跳 3 頁、拼 15 處行號。
3. **風險表補上結構性風險，加一欄「會不會波及個人開發者」。** 要補的四列：現金燒速與融資成本（BB 信評）、通路集中 47%、算力供應商承諾逾 $5,000 億、五角大廈線。補完後替讀者排出「最可能波及你」的一條。同時跟 anthropic-ipo「S-1 揭露了什麼」分清楚：風險的家在 business，IPO 頁只指路過去。
