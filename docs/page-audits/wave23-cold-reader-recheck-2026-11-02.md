# 第 23 波冷讀者複驗：Anthropic 商業線（2026-11-02）

**聲明：** 本 session 的系統自動把專案根目錄 `CLAUDE.md` 載進 context（內容為本站目標、架構、三個動作、環境限制；其中「Query」段提到 `wiki/index.md` 與 `wiki/log.md` 等路由）。除此之外未讀 `wiki/` 以外任何檔、未讀 `wiki/log.md`／`wiki/CLAUDE.md`、未 Glob、未跨頁 grep、未用 git。單頁內只做列標題與頁內找字。

**走過的頁（共 6 頁）：** `index` → `topics/anthropic-business`（母頁）→ `topics/anthropic-ipo`、`topics/anthropic-partnerships-compute`、`topics/anthropic-business-risks`；Q4 另點一次 `entities/google-investment`。

---

## 1. 四題結果

### Q1 營收多少、成長多快、誰說的、可信嗎 — **拿到**（成長率的數字彼此對不上）

- **路徑：** index:137 → anthropic-business:43–64 → anthropic-ipo:75–123（2 跳）
- **答案在哪：**
  - 單季營收 Q3 $168 億、季增約 46%：anthropic-business:47、:56；anthropic-ipo:104
  - 年化營收 $650 億（7 月的數字，之後沒有新值）：anthropic-business:55
  - H1 營收約 $163 億（去年同期 $11 億）：anthropic-business:45；anthropic-ipo:83、:100
  - 四季走勢 Q1 $48 億 → Q2 $115 億 → Q3 $168 億：anthropic-ipo:106–107
  - ARR 軌跡 $90 億 → $470 億：anthropic-business:217
  - **誰說的：** 指標表的「來源等級」欄＋分級說明在 anthropic-business:51–64，這樣設計很好；anthropic-ipo:77 明講「本頁未直接核對原文」，anthropic-ipo:93 寫 S-1 原文還沒逐項核對。
- **卡住的原句：**
  - anthropic-ipo:103「本季營收季增率已從上季 **146%** 放緩至約 45%」，下一行 anthropic-ipo:104 寫「上季為 **140%**」。哪個對？用 48→115 自己算是 140%。
  - anthropic-ipo:107「原文稱季營收**年增**近 50%」：同頁 :100 寫 H1 年增約 15 倍，這裡卻說年增近 50%，看起來是把季增誤寫成年增。
  - ARR 在 2 月的數字兩頁說法不同：anthropic-business:217 寫「$120 億（02 月）」，anthropic-ipo:151 寫「$14B/2 月」。
  - 「可信嗎」只能看來源等級欄自己判斷，沒有一句直接回答「這些數字能信到什麼程度」。最接近的是 anthropic-ipo:81–82「虧損近九成是帳列數字」與 anthropic-ipo:184「營收認列黑盒」，但兩處分散。

### Q2 哪個合作會改到我用的 Claude（價格／地區／速度／容量） — **拿到**

- **路徑：** index:137 → anthropic-business:90–91（只剩一句指路）→ anthropic-partnerships-compute:100–117（2 跳）
- **答案在哪：**
  - 價格：GSA 政府折扣 40%（:108）；Bedrock 沒有 50% Batch 折扣（:109）；Claude Platform on AWS 月花費上限 $500（:110）；Vertex 由 Google 自訂費率（:111）
  - 地區：Bedrock 新增首爾／新加坡境內推論（:109、:379）
  - 容量／速度：05-06 SpaceX Colossus 1 容量上線後提高用量上限（:70、:96）
  - 訂閱用戶不受這些通路影響（:117）：這一句對個人用戶最有用。
- **卡住的原句：**
  - :96「**寫得出後果的只有兩則**」，但同一張表 :79（AWS／Bedrock 價格後果）與 :80（Vertex 自訂費率）也有後果，數量對不上。
  - 「速度」幾乎沒有答案：只有 anthropic-business-risks:130 的自研晶片「run faster」一句，而且這句在商業模式段，不在合作頁。

### Q3 還沒過去的商業風險、哪一條最可能波及我 — **拿到**

- **路徑：** index:137 → anthropic-business:93–94 → anthropic-business-risks:42–113（2 跳）
- **答案在哪：**
  - 風險表六列：anthropic-business-risks:46–53
  - 虧損、通路集中、算力長約合成一列：:51；客戶集中的「兩家未具名客戶各占 12%」在 anthropic-ipo:88
  - 官司：音樂著作權（:49、:76–79、:99–100）、UTRF 專利（:59、:107）、反壟斷（:87–89）
  - **最可能波及我：** :57「個人訂閱用戶最直接相關的是『訂閱補貼收窄』與『多 agent 併發推高用量』兩列」，直接回答了這一問。
- **卡住的原句：**
  - :50「AI 相關損失恐超出保險業承保能力」來源等級標「**官方一手（S-1）**」，但 anthropic-ipo:77 說本站沒有直接核對 S-1 原文，:72 也寫「僅標題可用」。
  - 「依賴少數供應商」沒有單獨成列，被併進 :51；五角大廈黑名單、國防部遷出只在細節區 :90–92，沒有進表，也沒寫是否還在動。
  - anthropic-partnerships-compute:50 Microsoft 列寫「以自研 MAI 取代……見 [[topics/anthropic-business-risks#還沒過去的風險]]」，點過去表上卻沒有這一列（已移到細節區 :103–106）。

### Q4 跟 Google／Amazon／Microsoft 各是什麼關係 — **拿到**

- **路徑：** index:137 → anthropic-business:84 → anthropic-partnerships-compute:42–54（2 跳）；補看 entities/google-investment:41–70（3 跳）
- **答案在哪：** anthropic-partnerships-compute:46–50 的四欄表（出資／算力／通路／客戶或對手），一張表就答完。Google 循環融資在 google-investment:53–58，Google 是競爭者在 google-investment:69。
- **卡住的原句：**
  - anthropic-partnerships-compute:50「承諾購買 Azure 容量 $300 億（2025-11；[官方 05-06 公告](…higher-limits-spacex)提及）」：一篇 SpaceX 容量公告為何會證實 Azure 採購？標題和網址看起來對不上。
  - Microsoft 同時是「客戶」這件事（Office 裡用 Claude、「我們付很多錢給 Anthropic」）要讀到 anthropic-business-risks:105 才知道；表格那一格只寫了「取代」。

---

## 2. 入口

- index:137 `[[topics/anthropic-business]]` 的摘要寫著「往下鑽合作與算力（含跟 Google／Amazon／Microsoft 的關係）、風險與商業模式、上市與財報」，四題的關鍵字都在這一列，一看就知道該點。母頁 :81–85 的三列子線表也很好用。
- 不直覺的地方：
  - 這一列排在 Topics 表倒數第五列，前面要先掃過 L47–106 約 60 列人物與模型。index 沒有「💼 商業」的分區或「我想……」表（開發實務有，見 index:24–39）。
  - index:62 的 `entities/google-investment` 和 index:138 的 `market-signals` 會搶走注意力；index:62 標 resolved、摘要「Google 投資 400 億」，看起來像 Q4 的答案，其實只講 Google 一家。

## 3. 分不出差別的兩頁

- **`topics/anthropic-business`「現在的數字」 vs `topics/anthropic-ipo`「數字細節」**：兩處都放營收、估值、淨損、獲利，母頁 :45–47 與 ipo :96–107 重複。改數字時要改哪一處、哪一處是權威，看不出來。Q1 的不一致（ARR 2 月數字）就出在這兩頁之間。

## 4. 每頁判定

| 頁 | 判定 | 理由 |
|---|---|---|
| index | 路由 | — |
| topics/anthropic-business | 雷達偏百科 | 上半是指標表（百科），下半是時序與時段總結（雷達） |
| topics/anthropic-ipo | 雷達 | 現況五格表之後，約 2/3 篇幅是逐日 IPO 細節（:153 以下） |
| topics/anthropic-partnerships-compute | 上半百科、下半雷達 | :42–117 兩張表可當百科用，:284–473 是時序 |
| topics/anthropic-business-risks | 雷達 | 風險表帶「最後動態」；商業模式段（:117–130）其實是百科，但內容停在 06–08 月 |
| entities/google-investment | 百科 | 已結案事件，最後新聞 07-24 |

## 5. 內部用語外洩（10 則）

1. anthropic-ipo:51「🔎 查無官方 ⟨Q-03⟩」：⟨Q-03⟩ 對讀者沒有意義
2. anthropic-ipo:93「（標 2026-11-01｜查 EDGAR、Anthropic S-1｜複 2026-11-15）」：標／查／複三個字沒有解釋
3. anthropic-ipo:200「（標…｜查…｜複 2026-11-24｜訊 2026-10-26）」：同上，又多一個「訊」
4. anthropic-partnerships-compute:128、:133「（2026-10-27｜訊 2026-10-29）」：「訊」沒有解釋
5. anthropic-business:144–146「### 未歸類（目前沒有）」：管線留下的空殼
6. anthropic-business-risks:44、:69「細節區」：讀者不知道「細節區」是什麼
7. anthropic-ipo:73、:122 在本頁連回自己（`[[topics/anthropic-ipo]]`）：拆頁時留下的殘跡
8. anthropic-business:196「逐項見『哪個合作會改到你用的 Claude』」、:193「細節見『現在的數字』」：一個是已搬走的節名且沒有連結，另一個是表上已經沒有的 $1.2 兆
9. 遍布各頁的「Google News/Fortune」這類來源標記（例：anthropic-business:151–172）：聚合器路徑外洩，讀者會以為來源是 Google News
10. anthropic-business-risks:66–67、anthropic-business:35 的 `%% … 第 23 波、docs/page-audits/ledger.md …%%`：若網站版沒有隱藏 `%%` 註解，就會整段外洩（我讀 .md 看得到）

## 6. 撐不起的句子

- anthropic-ipo:103 vs :104：上季季增「146%」與「140%」並存
- anthropic-ipo:107「季營收年增近 50%」：與同頁 :100 的 H1 年增約 15 倍矛盾
- anthropic-business:217「$120 億（02 月）」 vs anthropic-ipo:151「$14B/2 月」
- anthropic-business-risks:50 來源等級「官方一手（S-1）」：本站沒讀 S-1 原文（anthropic-ipo:77），:72 也標「僅標題可用」
- anthropic-partnerships-compute:50 用 SpaceX 容量公告證實 Azure $300 億採購
- anthropic-partnerships-compute:96「寫得出後果的只有兩則」：同表 :79、:80 還有兩列有後果
- anthropic-ipo:65「近兩週兩條線同步升溫」：08-29 寫的相對時間，現在讀起來是錯的
- anthropic-business-risks:101「頂尖模型是否停售企業客戶」：沒有日期，無法判斷是否還在動

## 7. 最想改的三件事

1. **營收數字只留一個家，並對齊矛盾。** 母頁指標表只放「現值＋來源等級」；ipo 頁放走勢與口徑。修 146/140、「年增 50%」、2 月 ARR 三處，並在指標表旁加一句「這些數字能信到哪」的結論（例如：全部是媒體轉述 S-1，本站未核原文；淨損九成是非現金）。
2. **風險表回答「依賴少數供應商／政府黑名單」，修好斷掉的指路。** 把 Microsoft 自研取代、國防部遷出放回表內，或至少讓 partnerships:50 指到正確的錨點；同時把 risks:50 的來源等級改成與實際一致。
3. **把查證標記與管線殘跡翻成人話。** ⟨Q-xx⟩、標／查／複／訊、「細節區」、「未歸類」、「Google News/」前綴、自我連結，統一改寫或在頁首放圖例；index 加一個「💼 商業」的「我想……」小表（營收、合作影響、風險、三大雲關係四列），直接連到各子頁的錨點。
