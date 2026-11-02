# 第 24 波冷讀者複驗：計費（2026-11-02）

**聲明**：開工時系統自動把專案根目錄 `CLAUDE.md` 載入了 context（專案說明、wiki 三個動作、環境限制）。我沒有刻意讀它，答題時也沒有引用它；`wiki/CLAUDE.md`、`.claude/`、`docs/`、`news/`、`scripts/`、`log.md` 都沒讀。走過的頁：`index` → `entities/pricing` → `entities/pricing-incidents`、`entities/pricing-history` → `topics/community-cost`、`topics/code-quality-decline`（後兩頁只讀了被連到的段落，加上單頁標題列表）。行號指原始 .md 檔。

---

## 1. 四題結果

### Q1 額度掉得特別快／莫名被扣費，官方認了沒？有沒有繞法？
- **路徑**：index:35 → pricing「事故現在還在發生嗎」(285) → pricing-incidents「還在發生的事故」(45) → 回 pricing:293 → community-cost「用量去向歸因」(58)／「用量窗口與配額守門」(66) → 回 pricing:292 → code-quality-decline「三種解釋」(123)、「怎麼自己量一次」(67)
- **跳數**：4（index→pricing→incidents，再從 pricing 分流表跳兩頁）
- **結果**：**半拿到**
- **答案在哪**：
  - 「官方認了沒」：pricing-incidents:40（這幾天的 8 倍暴增「未見 Anthropic 說法」）、:51–62（事故狀態表）、:157–159（#16157 官方唯一的實質回覆是 2026-01-26，之後沒有新說法）；code-quality-decline:58（token 異常「無官方專文」）。結論是官方沒認，這點拿得到。
  - 「繞法」：散在四處——pricing:74（先關 usage credits 或設上限）、pricing:204（`ANTHROPIC_API_KEY` 會讓呼叫改走 API 計費）、community-cost:72–96（agent-usage-guard hook、resume-on-ratelimit、監控工具，作者全標「⏳ 單一作者」）、code-quality-decline:69–73（自己讀 `~/.claude/projects/` 的 log 量一次）。
- **卡住的原句**：
  - pricing-incidents:47「官方拒修或官方已承認的在最上」，但第一列（:53）是一個 10-01 起就停在「Investigating」的 Status 通報，一個月沒有後續。我分不清它是官方承認了、還是 wiki 沒跟上。
  - pricing-incidents:62「只有單一社群來源的：Reddit 用量暴增 8 倍（10-27）」。我問的「這幾天」正是這件，它卻被放在表外的一長串括號裡。
  - 沒有一個地方用一句話寫出「這幾天的狀況目前沒有官方說法，你可以先做 A、B、C」。繞法得自己從三頁拼起來。

### Q2 Max（或 Pro）現在包含什麼？每月附多少 API 額度？跟 Team 差在哪？
- **路徑**：index:57 → pricing「我的方案現在有什麼」(60)
- **跳數**：1
- **結果**：**拿到**（有一處矛盾）
- **答案在哪**：pricing:62–72（方案表：Pro 沒有 API credits，Max 每月 $100，Ultra 每月 $200，Team 每席 $20／$100 匯入共用池、上限 $500）；pricing:62、:265–266（這些 credits 不能付 Claude Code 的超量）；pricing:46（Fable 在訂閱裡怎麼分層）。
- **卡住的原句**：
  - pricing:69「驗證帳號無 5 小時上限」：「驗證帳號」是什麼、怎麼變成驗證帳號，全頁沒有解釋。
  - pricing:71 寫 Team premium「同 Max」（5 倍），但 pricing-history:69 寫「現有最高為 Premium（6.25x Pro 用量）」。兩個數字對不上。

### Q3 API 跑 Opus 5.5 一百萬 token 多少？批次、快取折扣？Bedrock／Vertex 會不會更貴？
- **路徑**：index:53（Opus 5.5 那列直接寫了 $4/$20）→ pricing「模型 API 定價現況」(126)、「通路與乘數」(215)
- **跳數**：1
- **結果**：**半拿到**（Anthropic 自家的價格拿到；Bedrock／Vertex 沒拿到）
- **答案在哪**：pricing:130（$4 / $20，快取讀取 $0.20，Batch 打 5 折）；:241–243（快取命中 ×0.05、Batch ×0.5、快取寫入 ×1.25／×2.0）；:252（乘數會疊乘）；:246（長脈絡不加價）。算出來：輸入 100 萬 token $4、輸出 100 萬 token $20；走 Batch 是 $2／$10；快取讀取 $0.20。
- **雲端通路**：只拿到「規則」，拿不到「數字」——:225（Bedrock 沒有 Batch 折扣）、:232（Bedrock 也沒有 beta 功能）、:245（regional 端點 ×1.1）。
- **卡住的原句**：pricing:231「partner 通路（Bedrock、Google Cloud）的絕對數字本頁不記」。這個取捨我能理解，但頁面沒有直接回答「會不會比較貴」，只丟兩個外部連結；也沒寫最近一次比對的結果是同價還是不同價。

### Q4 最近一個月哪些計費規則改了、會在我不知情時改到帳單？
- **路徑**：index:57 → pricing:41 → pricing-history「最近三個月變了什麼」(44)
- **跳數**：2
- **結果**：**拿到**
- **答案在哪**：pricing-history:46–61，⚠️ 標的就是「不用你操作就會改到帳單」的條目：10-30 Opus 4.8 fast mode 淘汰（:49）、10-11 gateway／proxy 之下分類器檢查改計入用量（:52）、10-09～11 Haiku 5.5 改兩檔計價（:53）、10-09 拿掉「需你同意」（:54）。
- **卡住的原句**：
  - 清單抓的是三個月，「近一個月」要自己數日期。
  - 10-22 新增的「wrapping up」收尾寬限（pricing:195）會影響用量怎麼算，卻不在這張清單裡。
  - 11-02 那條（:48）把方案改名、拿掉 5 小時上限這兩件不同性質的事寫在同一行，也沒有標 ⚠️。

## 2. 入口
- 帶我進去的是 index:35（「要花多少、怎麼被計費；額度掉得特別快是 bug 還是正常」）和 index:57（pricing 那列，鉤子寫「含月度 API 額度」「額度掉得快先看分流」）。用詞很貼近我的問題，**直覺**。
- 兩個小問題：
  - index:22 說這一塊「只放答『怎麼做』的頁面」，又說「要花多少的頁在各自領域的分頁下」，但 :35 正是一列「要花多少」，自相矛盾。
  - :35 連到的是 pricing 的一個分流段，進去後還要再跳一次才到事故表。直接連 pricing-incidents#還在發生的事故可以省一跳。
- index:57 的鉤子沒提到 Ultra 改名。從 Max 20x 來的讀者在 index 認不出它。

## 3. 分不出差別的兩頁
- **pricing-incidents「配額與速率」(252–304) 和 code-quality-decline「Token 消耗異常訊號群」(87–121)**：兩邊都收「額度掉得快」的社群回報，#38335、#41506、「Max 20x 週額度不到一天用完」三件在兩頁都有。pricing:290–292 的分流表試著用「計費事故」和「token 變多」來分，但從讀者這邊看，症狀根本一樣：額度沒了。我分不清一則新回報該去哪頁找。

## 4. 每頁定性
| 頁 | 判定 | 理由 |
|---|---|---|
| index | 百科（地圖） | 只放路由 |
| entities/pricing | **百科**（頂部一個雷達 callout） | 方案表、牌價、乘數、規則都是「現在是什麼」 |
| entities/pricing-incidents | **雷達** | 頂部是狀態表，下面是一則一則依日期排的流水帳 |
| entities/pricing-history | 雷達＋沿革 | 頂部是三個月清單，下面依日期排 |
| topics/community-cost | **雷達** | 結論段很薄，主體是 50 多則工具條目 |
| topics/code-quality-decline | 雷達（前段百科化） | 「三條線」表與「怎麼量」像百科，後半是時序 |

## 5. 內部用語外洩（10 處）
1. pricing:168「🔎 **查無官方**（標 2026-09-24｜查 Pasquale Pillitteri、實驗性重置｜複 2026-11-10）」：標／查／複這套暗碼
2. pricing:167、pricing-incidents:66「懸置細節」
3. pricing:180、:182、pricing-history:73「diff 偵測」
4. pricing:105、:113、:190「WebFetch 逐字查證」：工具名稱
5. pricing:201「日報 09-28／10-01 偵測到的異動屬實」
6. pricing:197「證實 09-27 MIXED『五類中三類收費』的標題」：引用一則讀者看不到的日報標題
7. pricing-incidents:167「本 session 未取得 `anthropics/claude-code` 讀取授權，依規不擴權」
8. pricing-incidents:311「08-29 `訊` 為探針假命中，已移除」
9. pricing-incidents:139「（Google News/TechCrunch；Startup Fortune）」這類抓取管道標記；:197「Reddit RSS 無讚數非低互動指標」
10. pricing-history:46、pricing-incidents:317「母頁」；pricing:37 的 `%%` 註解寫著「第 24 波」和 `docs/page-audits/ledger.md`（如果網站版沒有隱藏 `%%`，這段就會外洩）

## 6. 撐不起的句子
- pricing:88「Ultra 的差異不只用量：context window、Claude Code 額度、優先排隊等有結構性差異」：沒來源、沒日期、沒數字。
- pricing:203「1M context window 觸發獨立 API 計費通道」：唯一的證據是 05-11 的單一個案，卻列在「當前生效的計費規則」裡，而且跟 :246「長脈絡不加價」打架。
- pricing:204 `ANTHROPIC_API_KEY` 陷阱：「來源：2026-04-30」沒有連結。
- pricing-history:114「Sonnet 5.5…快取讀取低至 $0.20/Mtok」和 pricing:131、:255 的 $0.10 矛盾。
- pricing-history:69「Premium（6.25x Pro 用量）」和 pricing:71「同 Max」（5 倍）矛盾。
- pricing-incidents:54 infostealer 那件標「🔴 未解」，但同列寫官方 08-30 已通知、強制登出、退款。照 :47 自己的定義（🔴＝官方未公開回應），這件不該是 🔴。
- pricing-incidents:57 把 Issue #79773（個人回報）標成「⚖️ 司法中」。打官司的是 06-16 那起集體訴訟，不是這個 issue。
- code-quality-decline:89 寫「表上 10 則，從 06-27 到 10-30」，但表的第一列是 07-01；:121 又寫「既有十一則」，兩處數字自己對不上。

## 7. 最想改的三件事
1. **pricing-incidents 頂部補一段「這週額度掉得快？」三行答案**：官方有沒有說法（附日期）、最常見的三個自查點（usage credits 開關、`ANTHROPIC_API_KEY`、subagent／快取過期）、社群擋法連到 community-cost#用量窗口與配額守門。現在 Q1 要拼三頁。
2. **修掉方案與快取數字的跨頁矛盾**：Team premium 是 5 倍還是 6.25 倍；Sonnet 5.5 快取讀取是 $0.10 還是 $0.20；「驗證帳號」要定義。另外把「1M context 獨立計費」移出現行規則，或補上新的證據。
3. **通路一節回答「會不會比較貴」**：至少寫一句「YYYY-MM-DD 對過 Bedrock／Vertex 的 Opus 5.5 牌價：同價／差 X」，加上 regional ×1.1、沒有 Batch 折扣兩條，讓讀者不用跳出 wiki 就能判斷。順手把 index:35 直接連到 pricing-incidents，省一跳。
