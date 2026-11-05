# Wave 27 冷讀者複驗：Dario Amodei（2026-11-05）

> **誠實聲明：** 本次作答時，系統自動把 `/home/user/claude-news/CLAUDE.md`（專案說明）與 `wiki/CLAUDE.md`（wiki 規則，讀完 Dario 主頁後自動注入）載入 context。兩檔我都沒有主動去讀，也沒有用裡面的搜尋路徑（`wiki_search.py`、log、grep 全庫）來答題；不過 wiki/CLAUDE.md 讓我事先知道「`%% %%` 是維運備忘」「子故事頁」這些詞，第 5 節判斷內部用語時可能因此偏寬。
>
> **走訪範圍：** `wiki/index.md` → `entities/dario-amodei` → `entities/dario-amodei-archive`、`topics/recursive-self-improvement`、`topics/anthropic-government-policy`、`entities/yann-lecun`。全程只在單頁內列標題、找字。

---

## 1. 四題作答

### Q1 最近一兩個月說了哪些重要的話（風險、時間表、減速）？——**拿到**

- **路徑：** index:72 → `entities/dario-amodei`（#現況、#核心論述）→（深入）`topics/recursive-self-improvement#Dario Amodei 親自呼籲…`
- **跳數：** 主答案 1 跳（從 index 點 1 次就到）；要看三步驟細節共 2 跳
- **答案在哪：**
  - dario-amodei:49：現況段一句話說完：09-12〈We Must Pace the Frontier〉三步驟減速，6–12 個月 AI 群體可能接管網路，09-23 聯合國安理會，十月只有兩則轉述
  - dario-amodei:57–66：核心論述表，每項主張都標了「最近一次」和「本人原文或僅媒體轉述」，對冷讀者非常好用
  - recursive-self-improvement:273–278：三步驟原文細節；:54 只有第 ① 步已落地
- **卡住的地方：** 「一兩個月」指的是 09-05～11-05。主頁 :49 說「十月本站所見只有兩則媒體轉述」，可是 anthropic-government-policy:326 另有 10-21 Fox News「Amodei 同時為公司安全紀錄與對中銷售紀錄辯護」，主頁沒收這則，兩頁不一致。另外，11-02～03 修訂版 S-1/A 自評「可能迫近」RSI 門檻（recursive-self-improvement:30、:80）是公司聲音、不是他本人說的，但讀者會想知道。主頁沒提，也沒有指路過去。

### Q2 以前的預測（「AI 寫 90% 程式碼」、各種時間點）準不準？——**半拿到（偏弱）**

- **路徑：** index:72 → dario-amodei（頁內找「90%」「預測」，零命中）→ dario-amodei-archive（零命中）→ recursive-self-improvement（#目前結論、#自我改進量化指標）
- **跳數：** 3 跳，中間有 1 跳白走（archive）
- **答案在哪：**
  - recursive-self-improvement:72：S-1 稱 Claude 寫 Anthropic 逾 90% 程式碼（只限 Anthropic 內部，媒體轉述）
  - recursive-self-improvement:56：「兩個時間窗說法（只記原句與起算日，**不判應驗**）」，明說不做準不準的判斷
  - dario-amodei:65：他自己承認「壓縮 21 世紀」願景目前還做不到。這是全站唯一接近「預測自評」的一句
- **卡住的原句：** recursive-self-improvement:56「只記原句與起算日，不判應驗」。整個 wiki 沒有記錄他過去講「90% 程式碼」的原話、時間和對象，所以讀者拿不到「他說過 X → 後來 Y」的對照。:72 的 90% 是 Anthropic 自家數字，沒有說和他當年的預測有關。我可以自己猜兩者相關，但這頁撐不起「他說準了」的結論。主頁 #核心論述 也沒有「預測與兌現」欄。

### Q3 誰在公開批評他？重點是什麼？——**拿到**

- **路徑：** index:72 → dario-amodei#公開批評者對照 →（深入）entities/yann-lecun
- **跳數：** 1 跳；看原話 2 跳
- **答案在哪：** dario-amodei:72–86。九列，每列有「誰、何時、批評什麼、利益關係」，「利益關係」欄特別有用。按論點（動機、可行性、獨立性）整理的質疑在 recursive-self-improvement:55。LeCun 原話在 yann-lecun:54
- **卡住的地方：**
  - 批評表只收「具名的人或政治陣營」（:72）。所以 Techdirt 的「反對禁令、實質要禁」矛盾框架（anthropic-government-policy:280）、HN 社群「募資話術」質疑（recursive-self-improvement:280）都要自己挖
  - 08-24 Fortune 航空業評論被明文排除，只能去 archive 看
  - :79 Zuckerberg 那列寫「批評內容未見報導」，等於只告訴讀者「他批了」

### Q4 他的立場怎麼影響產品或政策（會不會改到我用的 Claude）？——**半拿到**

- **路徑：** index:72 → dario-amodei#在 Anthropic 的角色與影響（:88–93，空泛）→ dario-amodei:51 的連結 → anthropic-government-policy#🪖 軍事合約 → 同頁往上翻到 #現在有哪幾條線在動、#政府動作對你的產品做了什麼
- **跳數：** 2 跳，外加頁內往回翻；主頁沒有直接連到產品節
- **答案在哪：**
  - anthropic-government-policy:47：八條線裡三條改到你的 Claude，分別是香港與中國不可用、浮水印、Fable 5 高風險請求改由 Opus 4.8 執行。細節在 :191–201
  - anthropic-government-policy:233–237：軍事護欄不可移除 → 被五角大廈黑名單，但不影響商用（:64）
  - dario-amodei:175：05-12 他在大會上宣布 Pro/Max 速率翻倍
- **卡住的原句：** dario-amodei:88–93 只有「企業代言人」「政策倡議」這類職稱式描述，沒有一句寫「他的哪個主張 → 哪個產品行為」。政策頁產品節的三條，因果是「政府動作」，不是「Dario 立場」（:191「上表三條標『會』的線」）。他的減速主張對產品的影響（例如 METR 進駐會不會延後模型發布）全站沒寫。最後我只能自己推：護欄立場 → 被排除在軍方之外 → 對商用無影響。主頁 :51 連到的是軍事合約節，不是產品節，所以「會不會改到我」那一節要自己往上翻才找得到。

---

## 2. 入口

index:72 那一列：「Anthropic CEO：現在公開主張哪幾件事（附本人原文；減速論證在 [[topics/recursive-self-improvement]]）、誰公開批評他、與白宮的關係」。**很直覺**，Q1、Q3、Q4（白宮）三題一看就知道進這頁。缺點有兩個：Q2「預測準不準」在鉤子裡沒有對應字眼；人物區塊有 40 多列、沒有排序，Dario 排在第 72 列，冷讀者得往下捲很久才看到他。

## 3. 分不出差別的兩頁

- **dario-amodei#核心論述／#公開批評者對照 vs recursive-self-improvement#目前結論／#Dario Amodei 親自呼籲…：** 6–12 個月時間窗、三步驟、批評者這三樣，兩頁都有。主頁說「論證在議題頁」，但議題頁 :270–281 又把 Dario 的文章完整寫了一遍。讀者分不出哪頁才是他主張的家。
- **dario-amodei-archive vs dario-amodei#歷史記錄：** 主頁 :165–175 已有月總結，archive 是原始條目，冷讀者點進去只會看到同一件事寫得更囉唆。

## 4. 每頁判定

| 頁 | 判定 | 理由 |
|---|---|---|
| entities/dario-amodei | 百科（偏好） | 現況兩段＋主張表＋批評者表就是結論層；只有 :42 callout 和 :144 以下的歷史是雷達 |
| entities/dario-amodei-archive | 雷達（封存） | 純時序原始條目 |
| topics/recursive-self-improvement | 雷達為主 | :41–73 是百科，:76 之後 250 行「技術彙整」＋時序是新聞流 |
| topics/anthropic-government-policy | 前段百科、後段雷達 | :42–262 是結論層，:308 之後 660 行是攻防紀錄與時序 |
| entities/yann-lecun | 百科 | 短，原話＋來源 |

## 5. 內部用語外洩（網站可見，`%% %%` 內不算）

1. dario-amodei:49「十月**本站所見**只有兩則」：把蒐集範圍的限制寫成事實
2. dario-amodei-archive:58「**人物角度僅記**個人具名立場表態」：編輯分工用語
3. dario-amodei-archive:67「**日報僅載**逐字稿已公開一事」：讀者不知道「日報」是什麼
4. dario-amodei-archive:76「Axios 獨家報導（**news/2026-08-24、2026-08-25 兩則跟進**）」：露出原始檔路徑
5. recursive-self-improvement:85「❓ **待查證**（標 2026-11-03｜查 遞迴自我改進、書面承認｜**複 2026-11-17**）」：懸置標記的內部格式
6. recursive-self-improvement:94 標題「…（2026-10-26 新增…，**跨頁指標**）」
7. recursive-self-improvement:281「**可信度評估**……**訊號強度高**」：評分術語（:112、:195 等同樣有）
8. anthropic-government-policy:73「**表目前滿載八條**……**讓位給新進的**……下一位最先被頂替的是」：維護規則外洩
9. anthropic-government-policy:165「**不入表**（產業論戰）」：收錄判準
10. anthropic-government-policy:278「經 Hacker News 轉載達 972 分（本日全站互動最高，**src_count=2**）」：欄位名

（另有 yann-lecun:41「本站當日最高單則」，和第 1 條同類。）

## 6. 撐不起的句子

- dario-amodei:49「十月本站所見只有兩則媒體轉述」：anthropic-government-policy:326 另有 10-21 Fox News 一則，自相矛盾
- dario-amodei:92「同時呼籲政府不應妨礙州級 AI 法律」：沒有日期、沒有來源，全頁其他地方也找不到
- dario-amodei:93「曾與 Altman、Hassabis、Suleyman 聯署……（Wired；日期與原文連結未見）」：自己承認沒有依據
- dario-amodei:100「[[entities/fable-5]] — 2026 旗艦模型（個人出席大會宣布相關政策）」：看不出指哪項政策
- dario-amodei:68「Musk……與 Altman 隨後表態支持」：只有 ITV 單一標題（:130），而且 Musk 前一天才稱示警是 psyop，「支持」需要原話
- recursive-self-improvement:72「06-04 報告為 80% 至逾 90%」和 :91「≥80%（部分報導稱 80–90%）」、:319「80-90%」：同一數字在同頁有三種寫法

## 7. 最想改的三件事

1. **主頁加「說過的預測 → 現在」小表。** 列他過去的時間點預測（90% 程式碼、壓縮 21 世紀、6–12 個月 swarm），附原話日期、目前可對照的數字和狀態（「已兌現／未到期／自承做不到」）。現在 Q2 在全站無家，recursive-self-improvement:56「不判應驗」又擋住了路。不判應驗可以，但至少要並列原話和現況，讓讀者自己判斷。
2. **主頁「在 Anthropic 的角色與影響」改成「他的主張落到產品上的地方」。** 一條主張一行，寫「主張 → 公司動作 → 會不會改到你」，例如：護欄不可移除 → 五角大廈黑名單 → 商用不受影響；減速 ① → METR／Accenture 進駐 → 目前未見延後發布。連結直接指到 [[topics/anthropic-government-policy#政府動作對你的產品做了什麼]]，不要指軍事合約節。
3. **清內部用語、補漏記。** 第 5 節十處改成讀者語言，或移進 `%% %%`；:49「本站所見」改成具體事實，並補上 10-21 Fox News 那則；主頁現況加一句 S-1/A「可能迫近 RSI 門檻」並指路過去，省得讀者以為公司口徑和他本人口徑是兩回事。
