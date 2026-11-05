# Wave 27 冷讀者實測：Dario Amodei（2026-11-05）

**聲明：** 開工時系統自動把根目錄 `CLAUDE.md` 與 `wiki/CLAUDE.md`（含「搜尋策略」）載進了 context。我沒有照它的指示用 grep 或 script，只從 `wiki/index.md` 出發點 wikilink 走；頁內只用「列標題」和 Ctrl-F。我沒讀 `log.md`，也沒讀 wiki 以外的檔。

**走過的頁：** `index` → `entities/dario-amodei` → `entities/dario-amodei-archive` → `topics/recursive-self-improvement` → `topics/anthropic-government-policy` → `topics/anthropic-commitments`

行號都指原始 .md 檔。

---

## 1. 四題結果

### Q1 最近一兩個月說了什麼（風險、時間表、減速）——**拿到（只拿到九月；十月沒拿到）**
- **路徑：** index:72 → `entities/dario-amodei`（1 跳）→ `topics/recursive-self-improvement`（2 跳）
- **答案在哪：**
  - dario-amodei:65–67、83–87：09-12/13 呼籲全球減速、「AI swarm」6–12 個月、09-15 Dreamforce 重申
  - dario-amodei:66：中國是「最棘手的兩難」
  - dario-amodei:184：09-23 在聯合國安理會主張安全協議要「範圍限定」
  - recursive-self-improvement:270–281：〈We Must Pace the Frontier〉原文、三步驟減速計畫、技術依據。這是全庫最好的一段。
- **卡住的地方：**
  - dario-amodei:50–52 的「現況」頭兩段寫的是「公司花 275 萬美元保護他」「操盤 2 兆 IPO」，都是僅標題可用的周邊新聞，不是他說了什麼。真正的答案（09-12 那篇文章）在表格第 6 列才出現。
  - 十月他本人說了什麼，只有 dario-amodei:178 一句「呼籲同業對模型能力保持透明誠實」。我分不出這是「十月他沒說話」，還是「本庫沒收」。
  - dario-amodei:67 的原句寫「公開撰文」，但沒給文章連結；連結要跳到另一頁的 RSI:272 才有。

### Q2 以前的預測準不準（「90% 程式碼」、各種時間點）——**沒拿到（只有旁證）**
- **路徑：** index:72 → dario-amodei → dario-amodei-archive → recursive-self-improvement → anthropic-commitments（4 跳）
- **在 dario-amodei 頁 Ctrl-F：** 「90%」「預測」都零命中。
- **旁證：**
  - recursive-self-improvement:72、87–92：S-1 稱 Claude 寫 Anthropic **自家**逾 90% 程式碼。這只是 Anthropic 內部的數字，沒有連回他當年「AI 會寫 90% 程式碼」那句預測，也沒說準不準。
  - dario-amodei-archive:62：STAT 專訪中他自承「壓縮 21 世紀」願景「目前還做不到」。這是唯一一則「說過 vs 現實」的對照，卻埋在封存頁。
- **卡住的原句：** recursive-self-improvement:56「兩個時間窗說法（只記原句與起算日，**不判應驗**）」。這頁明文不做這件事，而且沒有指出去哪裡看。anthropic-commitments 只追「承諾」，不追「預測」，見 commitments:41、51。

### Q3 誰在公開批評他、重點是什麼——**拿到**
- **路徑：** index:72 → dario-amodei（1 跳）
- **答案在哪：** dario-amodei:93–104「公開批評者對照」表。六人各列批評重點和利益關係，整頁最好用的一塊。補充在 recursive-self-improvement:55（動機、可行性、獨立性三處質疑）。
- **缺口：** 表外還有幾位批評者，散在別處。我是靠 Ctrl-F 才湊齊的：
  - Zuckerberg（dario-amodei:188）
  - Gavin Baker（dario-amodei:69）
  - Fortune 航空業評論（dario-amodei:40–41）
  - Musk 的「psyop」（recursive-self-improvement:153）
  - 川普陣營的「末日論」備忘錄（dario-amodei:183）

### Q4 他的立場怎麼影響產品／政策（會不會改到我用的 Claude）——**半拿到**
- **路徑：** index:72 → dario-amodei → anthropic-government-policy（2 跳）→ recursive-self-improvement → anthropic-commitments（4 跳）
- **答案在哪：**
  - anthropic-government-policy:191–201「政府動作對你的產品做了什麼」：香港不在可用區、浮水印、Fable 高風險請求改由 Opus 4.8 執行。這節寫得清楚，但講的是**政府**動作的後果。
  - anthropic-government-policy:221–227「根本矛盾」：安全論述反過來給了政府干預的正當性。這是唯一把「他的立場」接到「你的 Claude」的推理。
  - recursive-self-improvement:53：減速呼籲落地的是第三方評估，不是暫停。commitments:51 的狀態是「部分兌現」。
  - dario-amodei:80：05-12 他親自宣布 Pro/Max 速率翻倍。這是唯一一則直接改到用戶的事。
- **卡住的原句：** dario-amodei:106–110「在 Anthropic 的角色與影響」只有三條空泛的話（「企業代言人」「積極參與 AI 治理政策討論」），沒說他的立場落到哪個產品決策。整個問題要讀者自己跨三頁拼起來。

---

## 2. 入口
- index:72 `[[entities/dario-amodei]]`。
- 很直覺：人物表裡一眼就找得到，鉤子「AI 風險論述與政府監管立場；九、十月六位公開批評者」直接對上 Q1 和 Q3。
- 不足：鉤子沒提「減速呼籲／三步驟計畫的家在 RSI 頁」。index:142 的 RSI 鉤子寫「誰喊停」，但沒寫是 Dario。冷讀者不會想到 Dario 的核心論述住在一個叫「遞歸自我改進」的頁。

## 3. 分不出差別的兩頁
- **`entities/dario-amodei` vs `topics/recursive-self-improvement`：** 同一則 09-12/13 減速呼籲有兩個家，而且日期不一致：
  - dario-amodei:67、193 寫 09-13「公開撰文」
  - RSI:270–281 寫 09-12 發布於本人網站，並附原文
  
  讀者不知道哪頁才是權威版本。
- 頁內也有重複：dario-amodei 的「核心論述」表（60–81）和「歷史記錄」（173–213）幾乎逐條重複，差別只在表格與條列。

## 4. 百科 or 雷達
| 頁 | 判定 | 理由 |
|---|---|---|
| entities/dario-amodei | 雷達 | 主體是日期流水帳，很多是僅標題可用的新聞；只有批評者表（93–104）像百科 |
| entities/dario-amodei-archive | 雷達（封存） | 原始條目封存 |
| topics/recursive-self-improvement | 雷達（前段百科） | 「目前結論」（49–57）和指標表（61–72）是百科；「技術彙整」佔 230 行，是雷達 |
| topics/anthropic-government-policy | 雷達（前段百科） | 摘要、產品後果節、根本矛盾是百科；攻防紀錄和時序佔 660 行以上，是雷達 |
| topics/anthropic-commitments | 百科 | 承諾狀態表，答「做了嗎」 |

## 5. 內部用語外洩（≤10，都是網站上看得到的）
1. dario-amodei:68 `⟨Q-02⟩`、dario-amodei:89–90 「**懸置細節**」`⟨Q-01⟩`：短標記與懸置用語
2. dario-amodei:200 `🔎 查無官方（標 2026-08-10｜查 Axios、Yahoo Finance｜訊 2026-08-24｜複 2026-09-30）`：標／查／訊／複是維運欄位
3. recursive-self-improvement:85 `❓ 待查證（標 2026-11-03｜查 遞迴自我改進、書面承認｜複 2026-11-17）`
4. dario-amodei:195 「日報僅載逐字稿已公開一事」：「日報」是內部原料
5. recursive-self-improvement:129–130 「日報稱同場有共和黨參議員……」「僅見日報對標題的彙整」
6. anthropic-government-policy:73 「表目前滿載八條……讓位給……下一位最先被頂替的是」：表格維護規則
7. recursive-self-improvement:94 標題裡的「跨頁指標」
8. dario-amodei-archive:37 指路「回主頁『現況』或『公開立場與言論』表」：主頁沒有這張表，實際叫「核心論述」，是斷掉的內部舊名
9. dario-amodei:171 一行裸 `[[news/2026-08-04]]`，沒有說明
10. dario-amodei:50、52、62–64 等處的「（僅標題可用）」重複出現：讀者看得懂，但通篇是查證狀態，不是內容

## 6. 撐不起的句子
- **dario-amodei:43–44、50、62、175：** 「275 萬美元……超過他 1,800 萬美元年薪四倍以上」**算術不成立**，275 萬比 1,800 萬還少。Fortune 的「4 倍」應該是對他的底薪；1,800 萬是 Reuters 報的總薪酬。頁面把兩個口徑混成一句，callout、現況、表格、歷史四處都是同樣的錯。
- **dario-amodei:67、86：** 「Musk、Altman 相繼表態支持」，但 recursive-self-improvement:153 記載 Musk 09-11 稱這波警告是「psyop」。兩處沒有並陳，也沒說明他前後改了立場。
- **dario-amodei:40–41 vs 196：** 頁首 callout 寫 Fortune 評論「內容已查實」並列出論點；歷史記錄 196 仍寫「僅標題可用，具體論點與建議內容未見報導」。兩句互相矛盾。
- **dario-amodei:56：** 「2026 年上半年公開言論集中在……」放在「現況」，但今天是 11 月，下半年的減速呼籲才是主線。
- **dario-amodei:110：** 「同時呼籲政府不應妨礙州級 AI 法律」，沒有日期也沒有來源。
- **dario-amodei:81：** 「多次｜聯署 AI CEO 生物武器防範信（……Suleiman）」，沒有日期，人名拼法也和 index 的 Suleyman 不一致。
- **dario-amodei:40：** 最上方 callout 是 08-24 的舊評論，佔掉「最新」的位置。

## 7. 最想改的三件事
1. **把「現況」改寫成他現在的立場。** 第一段放 09-12〈We Must Pace the Frontier〉的三步驟和 6–12 個月時間窗，附原文連結。保鑣費、薪酬這類僅標題可用的周邊新聞降到表格。同時修正 275 萬／1,800 萬的口徑錯誤。
2. **新增「說過 vs 後來」一節。** 列出他的歷史預測與時間點（90% 程式碼、壓縮 21 世紀、6–12 個月 swarm），每條配上本庫已有的對照：S-1 的逾 90% 是 Anthropic 自家程式碼、STAT 專訪自承還做不到。RSI 頁不判應驗可以維持，但要指路到這一節。
3. **把「在 Anthropic 的角色與影響」改成「他的立場改到了你什麼」。** 三四列就好：速率翻倍（05-12）、減速呼籲 → 第三方評估而非暫停（連 commitments:51）、安全論述 → 政府干預 → Fable 分類器改派與地區限制（連 government-policy#政府動作對你的產品做了什麼、#根本矛盾）。各條明說「會／不會改到你用的 Claude」。
