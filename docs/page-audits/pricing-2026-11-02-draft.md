# 第 24 波 draft：逐字稿（2026-11-02）

> 單一來源：`<scratchpad>/w24/design/newtext.py`（頁面）、`rules_patch.py`（規則檔與測試）；本檔由 `make_draft.py` 生成，改字請改那兩支再重生。行號指設計 commit `933a34d` 原檔（P＝pricing，A＝pricing-archive）。實作者跑 `split.py <repo>` 產全文，不手抄本檔。

# 進頁面

## A. 母頁 entities/pricing

使命句（標題下）：

```markdown
Claude 現在怎麼收你的錢，以及最近哪幾件事改變了這個答案——帳單出錯在 [[entities/pricing-incidents]]、價格沿革在 [[entities/pricing-history]]，各往下鑽。
```

拆頁評估（取代 P35）：
```markdown
%% 拆頁評估 2026-11-02：已拆（第 24 波，`docs/page-audits/ledger.md` 裁決紀錄）。事故＋配額與速率＋灰色市場 → entities/pricing-incidents；定價與促銷＋成本案例 → entities/pricing-history；計費切割風波死案歸檔 entities/pricing-archive。母頁留方案、牌價、還沒確定、生效規則、通路與乘數、三路分流；正文上限 300 行，逾線時下一刀是 API 塊（一小時、模型 API 定價、通路與乘數連續三節，整塊切出）。 %%
```

callout（取代 P37–39）：
```markdown
> **最新計費政策異動**（2026-11-01）
> - [Reddit 回報](https://www.reddit.com/r/ClaudeAI/comments/1xjlvlc/anthropic_renames_max5_and_max20_and_removes_5h/)的方案改名，2026-11-02 對[官方方案頁](https://claude.com/pricing)查證屬實：$200 一檔現名 **Ultra**（Pro 的 10 倍用量），$100 的 Max 是 5 倍；Max／Ultra／Team 每月附 API credits，Enterprise 已公開 $20／席。下方方案表已整表更新。
> - 最近三個月改了什麼，見 [[entities/pricing-history#最近三個月變了什麼]]；額度掉得快、帳單出錯，先看 [[#事故現在還在發生嗎]]。
```

`## 現況`（取代 P43–51 五段）：
```markdown
**所有付費方案仍是訂閱配額制；週配額 09-14 換軌後約為加成期間的 83%**：同樣的工作，`Settings > Usage` 的用量百分比多跑約 20%（1 ÷ 0.83），5 小時上限的計算方式不變（[官方說明中心](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)，09-14 確認）。旗艦 Fable 在訂閱裡分兩層：Max、Ultra 與 Team premium 標配、上限為週用量的 50%（Ultra 改名後官方未重述，沿用屬推論）；Pro 與 Team standard 走 usage credits 按 API 費率付費。Agent SDK、`claude -p` 照計訂閱配額——原定 06-15 的計費切割已於 06-16 暫停、重推時間未定（經過見 [[entities/pricing-archive#計費切割風波]]）。

**升級能多拿多少、你的選項**：官方不公布週配額的絕對量，方案頁只寫倍數——Max 為 Pro 的 5 倍、Ultra 為 10 倍（2026-11-02 查證）。選項：把重活挪進 5 小時窗／升 Max 或 Ultra／開 usage credits 補量，但開之前先設月上限（開了之後上限不再是硬停止，見下方警語）。
```

新節「往下鑽」（插在 `## 現況` 之後、P53 `---` 之前）：
```markdown
## 往下鑽：帳單出錯與價格沿革

| 子頁 | 答什麼 | 最後動態 |
|---|---|---|
| [[entities/pricing-incidents]] | 帳單出錯、額度掉得快：官方認了沒、現在還在不在、你能先做什麼 | 2026-11-01 |
| [[entities/pricing-history]] | 價格、方案與促銷什麼時候變的，最近三個月改了什麼 | 2026-10-30 |

2026-04～06 的原始條目與已暫停的計費切割風波在 [[entities/pricing-archive]]。

```

方案表表頭說明（取代 P57）：
```markdown
> **資料截至 2026-11-02**（[claude.com/pricing](https://claude.com/pricing) 查證）。「可領優惠」欄的月度 API credits 只能用在 Claude Platform 自建的 App／Agent，**不付 Claude Code 與 Claude apps 的超量**（[官方文件](https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers)）。「訂閱內含／需另計費」的分界會隨陣容換代改變，模型名以當期實際情形填寫。
```

方案表七列（取代 P61–67；表頭 P59–60 不動）：
```markdown
| Free | $0 | 基本額度；含 Design／Slides／Docs，不含 Opus | — | — | 09-14 起週配額 +25% 不適用本方案 |
| Pro | $20（年繳 $17／月）| 全模型，**Fable 旗艦除外**（免另計費最強為 Opus 5.5）| **Fable 5／5.1** — $10/$50 per Mtok，走 usage credits | 無月度 API credits | 至 `Settings > Usage` 確認 auto-reload 未開 |
| Max | $100 | Pro 的 5 倍用量；**旗艦（Fable 5／5.1）上限為週用量 50%** | 超出後走 usage credits | 每月 $100 API credits | 留意旗艦誤要求購點問題（見 [[entities/pricing-incidents]]）|
| Ultra（原 Max 20x） | $200 | Pro 的 10 倍用量；旗艦上限同 Max（改名後官方未重述，推論） | 同上 | 每月 $200 API credits | 用量上限集體訴訟進行中（訴的是 Max 20x 時期的宣稱） |
| Team standard seat | $20（年繳）／$25（月繳）每席 | 同 Pro | 同 Pro | 每席 $20 計入全隊共用池，上限 $500／月 | 年繳需達最低 20 席（2026-10-15 新增門檻）|
| Team premium seat | $100（年繳）／$125（月繳）每席 | 同 Max | 同 Max | 每席 $100 計入同一池 | — |
| Enterprise | $20／席（年繳，20 席起） | 席位費不含用量；舊制席位制比照 standard／premium 分層 | 用量按 API 費率；舊制同對應層 | — | 07-04 起可用支出控管；可依承諾支出談折扣 |
```

usage credits 警語（取代 P69）：
```markdown
**⚠️ usage credits 一開，方案用量上限就不再是硬停止**：額度用盡後照常回答、從 credits 扣款，體感與額度內無異。靠硬上限控管支出者，開之前先設月上限、確認 auto-reload（每日兌換上限 $2,000）未開；規則本文與來源見 [[#當前生效的計費規則]]。
```

方案細節 Team／Enterprise 月費（取代 P86）：
```markdown
- **Team／Enterprise 月費（2026-11-02 官方查證）**：Team 可混搭席位，standard $20／premium $100（年繳；月繳 $25／$125），年繳 20 席起；Enterprise $20／席年繳、20 席起，用量按 API 費率（[claude.com/pricing](https://claude.com/pricing)）
```

API 表新列（插在 P139 Sonnet 4.6 之後）：
```markdown
| Claude Haiku 5.5 | **$0.10 / $0.50**（≤100K）；$0.50 / $2.50（>100K） | 陣容最低價；依 prompt 長度分兩檔，快取命中 $0.01／$0.05（2026-11-02 官方查證）；細節見 [[entities/haiku-5-5#實付成本]] |
```

還沒確定：導語（取代 P159）、新列（P163 之後）、P165 改寫、表下懸置（P602 原文照搬，置於 P171 之後）：
```markdown
**下列各項尚無官方一手文件可寫進「當前生效的計費規則」；查證屬實就移出、寫進它的家，經過見 [[entities/pricing-history]]。**

| Ultra 是否取消 5 小時用量窗 | 單一 Reddit 貼文（10-30）稱取消；2026-11-02 方案頁查證未涵蓋此點，官方說明未見 | 官方 usage limits 說明改版 |
| Opus 5.5 的「實驗性用量上限重置」 | 單一來源稱有；官方說明中心未見此機制（查證進度見表下） | 2026-11-10 複查 |

**懸置細節**
🔎 **查無官方**（標 2026-09-24｜查 Pasquale Pillitteri、實驗性重置｜複 2026-11-10）｜**Claude 是否新增實驗性用量上限重置機制**：2026-10-10 查官方 [說明中心](https://support.claude.com/)「Usage and limits」與 Pro／Max 方案分類，**未見此機制的任何條目**。⚠️ 並查出一件事：看似多家報導其實是**同一個來源**——pasqualepillitteri.it 以 9 種語言各發一篇（en／de／fr／nl／es／pt／id／tr／zh），仍屬單一來源。該來源稱是 Pro／Max／Team 可保留自用的一次性額度、入口在設定→用量的「Resets」頁籤、10-22 到期；**這些細節一概未經官方佐證，不採信為事實**：Google News／Pasquale Pillitteri 單一來源稱 Opus 5.5 上線同時導入「experimental usage limit resets」，具體機制、適用方案與是否官方確認均未見報導；同一媒體 09-05 曾以「Anthropic Resets Claude Limits」為題報導，09-06 查證結果為價格結構未變（見上方「2026-09-05」條），故本則比照處理，不逕自視為新規則寫入「當前生效的計費規則」。
```

已失效規則（取代 P219）：
```markdown
> **已失效並移除的規則**：Fable 5 免費使用期（2026-07-19 到期，由上方 07-20 分界取代）；Claude Code 週用量 +50% 促銷（2026-09-13 到期，09-14 由上方永久 +25% 接手）。經過見 [[entities/pricing-history]]。
```

可用性第 1 條（取代 P286）：
```markdown
- **升級付款失敗**：Max 5x 升 20x 每次付款皆失敗、客服未回應（#56281，2026-10-24），延續 08-02 的 #55266；升級成功者的額度仍按 5x 速率消耗（#79773，10-21）。事件本文見 [[entities/pricing-incidents#事故與爭議（誤扣費、靜默計費改動、帳號安全）]]。
```

`## 事故現在還在發生嗎` 節下（取代 P295–318；節名不動）：
```markdown
額度掉得快、帳單對不上，先分清楚懷疑的是哪一種，再往對的頁走：

| 你懷疑的是 | 去哪頁 | 那裡答什麼 |
|---|---|---|
| 計費事故：官方認了沒、現在還在不在 | [[entities/pricing-incidents#還在發生的事故]] | 一事故一列的狀態表；每件的後續在同頁 |
| 同樣的工作，token 本身變多了 | [[topics/code-quality-decline#三種解釋，目前各自站在哪]] | 退步、計量、配置三種解釋各自的證據 |
| 自己的設定在吃額度 | [[topics/community-cost#用量去向歸因]] | subagent、背景 agent 各吃掉多少、怎麼擋 |

逐條 issue 的留言數與官方回覆在 [[entities/claude-code-known-issues]] 的「💰 計費與配額」組。

### 事故與爭議（誤扣費、靜默計費改動、帳號安全）

這一段已移到 [[entities/pricing-incidents#事故與爭議（誤扣費、靜默計費改動、帳號安全）]]。

```

相關議題新增兩行（P962 之後）：
```markdown
- [[entities/pricing-incidents]]（計費事故與額度異常：官方認了沒、還在不在）
- [[entities/pricing-history]]（價格、方案與促銷的沿革）
```

行內替換：
- **P33**：「**最後更新：** 2026-11-01」→「**最後更新：** 2026-11-02」
- **P117**：「Opus 5 的 **142 小時**」→「Opus 5.5 的 **172 小時**」
- **P117**：「**80 小時**與 **160 小時**」→「**80 小時**與 **200 小時**」
- **P140**：「陣容中最低價；」→「（刪）」
- **P144**：「Fast mode（僅 Claude API，2026-10-16 查證已不再標記「research preview」）另計 **$10 / $50**」→「Fast mode 另計 **$10 / $50**（可用通路與研究預覽狀態見「通路與乘數」乘數細節）」
- **P202**：「詳見下方「重要政策變動紀錄」10-09 條目」→「見 [[entities/pricing-history]] 10-09 條」
- **P212**：「見事件流 10-02 條」→「見 [[entities/pricing-incidents]] 10-02 條」
- **P279**：「脈絡見下方事件流 10-06／10-10 條目。」→「脈絡見 [[entities/pricing-history|沿革頁]] 10-06／10-10 條。」

砍行逐行理由見 proposal-map 第三節。

## B. 子頁 entities/pricing-incidents（新）

標頭（frontmatter 由 gen 重生）：
```markdown
# Anthropic 計費事故：誤扣、額度異常與帳號停用

帳單出錯、額度掉得快、付了錢卻用不了——官方認了沒、現在還在不在，以及你能先做什麼；現在怎麼計費在 [[entities/pricing]]，逐條 issue 的留言數在 [[entities/claude-code-known-issues]]。

（標頭七欄：類型 policy／狀態 active（持續調整中）／領域 💼 商業／上層 [[entities/pricing]]／首次出現 2026-04-25／最後更新 2026-11-02／最後新聞更新 2026-11-01）

> **最新動態**（2026-11-01）
> - [Reddit 單一貼文](https://www.reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic/)稱當日 Claude Code 用量暴增 8 倍，並稱服務端錯誤也扣付費額度、不補償；未見 Anthropic 說法。
> - [Reddit 單一貼文](https://www.reddit.com/r/ClaudeAI/comments/1xjlvlc/anthropic_renames_max5_and_max20_and_removes_5h/)稱方案改名並取消 5 小時窗：改名 2026-11-02 對官方查證屬實（$200 一檔現名 Ultra），5 小時窗至今只有這一則貼文。
```

`## 還在發生的事故`：表頭說明（取代 P295）與 `%%`（取代 P299）：
```markdown
**一事故一列，只收 🔴、⛔、⚖️ 三種狀態；轉 ✅／⏸ 即移出表，條目留在下方。最多 8 列：官方拒修或官方已承認的在最上，其次司法中，再來其餘未解；同一層最後動態新的在上。** 狀態五值定義（供讀者對號）：🔴 未解＝官方未公開回應、也未載明修復版本；✅ 已修＝官方確認或載明修復版本；⛔ 官方拒修＝官方已明確表態不修；⚖️ 司法中＝已進入訴訟程序；⏸ 無後續＝距最後動態逾 90 天且無新回報。

%% 維運備忘：上限、排序、「單一社群回報型」定義與移出判準見 `.claude/reporter-rules/commercial/pages.md`「pricing 事件流的上限與退場」。表只寫 issue 號，互動數的家是 entities/claude-code-known-issues。 %%
```

表八列順序：P306 → **新列 infostealer** → P304 → P303 → P305（改）→ **新列 #56281** → **新列 #79337** → P308（改）；P307 移表下。三個新列：
```markdown
| infostealer 竊 session cookie，免密碼抽乾訂閱額度 | 🔴 未解 | 2026-09-09，官方 08-30 通知已強制登出、撤銷 token、退誤扣款 | 額度莫名見底先查有無不明登入；攻擊面見 [[topics/ai-agent-safety]] |
| Max 5x 升 Max 20x 付款持續失敗、客服未回應 | 🔴 未解 | 2026-10-24，Issue #56281，延續 #55266、#55982 | 升級前備妥備援付款方式、留錯誤截圖；別反覆重試 |
| Fable 成 Max 標準模型起被誤判要先買 usage credits | 🔴 未解 | 2026-10-24，Issue #79337，07-20 起未修 | 對照 `Settings > Usage` 與帳單，於該 issue 回報佐證 |
```

排序實跑（pages.md 新條文）：第一層〔⛔＋官方已承認〕credit 延遲（10-01，Status）＞infostealer（09-09，官方 08-30 通知）＞7 月帳務錯誤（07-20）＞HERMES（04-25）；第二層〔⚖️〕Max 20x 訴訟（10-21）；第三層〔其餘 🔴〕#56281（10-24，起始 08-02）＞#79337（10-24，起始 07-20）＞#16157（09-17）｜第 9 起截斷：#38335（09-16）、#5088（09-04）；第四層〔單一社群回報型〕10-27 Reddit、10-16 HN、10-11 Reddit、#8327（10-02）、#37394（09-21）、08-04 Reddit、07-02 Reddit。

表下兩行：
```markdown
**還在發生、沒進上表的**（同一排序，新的在前）：#38335 Max session 額度加速耗盡（09-16）、#5088 續訂扣款後帳號停用（09-04）；只有單一社群來源的：Reddit 用量暴增 8 倍（10-27）、Console 小數點多扣 100 倍（10-16）、成本顯示把 Haiku 5.5 算成 Opus 價（10-11）、#8327 設 API key 後組織遭停用（10-02）、#37394 Max 觸頂過快（09-21）、Reddit Max 20x 半小時 0%→100%（08-04）、Reddit Max 升級誤購 credits（07-02）。每件見下方「事故與爭議」同日條目。

表只寫 issue 號；留言數與讚數以 [[entities/claude-code-known-issues]] 為準，下方各條目裡的數字是當日快照。
```

06 時段總結（P535–539 原文照搬進 archive `## 2026-06`；P840–843 同）：
```markdown
**2026-06 事故**：隱私政策新增年齡／身份驗證條款（07-08 生效）、加州用戶帳號遭盜刷產生歐元計費（06-24，⏸ 逾 90 天無後續）。原始條目見 [[entities/pricing-archive#2026-06]]。

**2026-06 配額事故**：社群集體反映 Claude Code 配額再次縮減（06-30，無官方公告、幅度不明）。原始條目見 [[entities/pricing-archive#2026-06]]。
```

P339 標題（證據等級）：
```markdown
#### 🔴 2026-10-27：Reddit 單一貼文回報當日用量暴增 8 倍，並稱服務端錯誤也扣付費額度、不補償（未見 Anthropic 說法）
```

P794（取代）：
```markdown
- **2026-11-02 對官方方案頁查證**：改名屬實——$200 一檔現名 Ultra（Pro 的 10 倍用量），$100 的 Max 為 5 倍；5 小時窗是否取消，官方說明未見，見 [[entities/pricing#還沒確定的計費變動]]。
```

相關：
```markdown
## 相關

- [[entities/pricing]]：母頁，現在怎麼計費、三路分流
- [[entities/pricing-history]]：價格、方案與促銷的沿革
- [[entities/claude-code-known-issues]]：逐條 issue 與互動數
- [[topics/code-quality-decline]]：token 消耗變多的三種解釋
- [[topics/community-cost]]：自己的設定吃掉多少額度、怎麼擋
- [[topics/ai-agent-safety]]：額度被盜用的攻擊面
- [[entities/pricing-archive]]：2026-04～06 的原始條目

```

行內替換：
- **P316**：「下方「事故與爭議」事件流每則」→「下方「事故與爭議」每則」
- **P305**：「2026-10-21，Issue #79773（31 留言）：」→「2026-10-21，Issue #79773：」
- **P308**：「Issue #16157 累積 1,495 則留言、725 👍，本頁互動量最高」→「Issue #16157，官方同日補「用量與長度是兩種限制」說明」
- **P531**：「、6/16 Max 集體訴訟（見「計費切割風波」6/16 條目）之後」→「、6/16 Max 集體訴訟之後」

其餘：P330／P337／P789 由 h3 升 h2（節名不改，錨點 `#事故與爭議（誤扣費、靜默計費改動、帳號安全）` 因此存在）；`%% 未列入總表 %%` 等 17 行舊備忘砍（map 第三節）。

## C. 子頁 entities/pricing-history（新）

標頭：
```markdown
# Anthropic 計費沿革：價格、方案與促銷怎麼變過來

Claude 的價格、方案與促銷是什麼時候、怎麼變的，以及最近三個月哪幾件改到你的帳單——現在生效的規則與牌價在 [[entities/pricing]]。

（標頭七欄同 incidents，最後新聞更新 2026-10-30）

> **最新動態**（2026-10-30）
> - [官方方案頁](https://claude.com/pricing)新增問答：Enterprise 與 API 可依用量與承諾支出談客製折扣，門檻與幅度未公開，需洽業務。
```

`## 最近三個月變了什麼`（新，裁決 (3)；插在 callout 之後、`## 定價與促銷` 之前）：
```markdown
## 最近三個月變了什麼

官方已確認、會改到帳單的，新的在上；每條的現行規則住母頁，這裡只記什麼時候變。⚠️＝不必你操作就會改到帳單。

- **11-02 查證｜方案改名與附帶 API credits**：$200 一檔現名 Ultra（Pro 的 10 倍用量）；Max／Ultra／Team 每月附 $100／$200／最多 $500 API credits，不付 Claude Code。見 [[entities/pricing#我的方案現在有什麼]]
- **10-30｜Opus 4.8 fast mode 宣告淘汰，11-30 移除** ⚠️：之後請求直接回錯誤、不退回標準 Opus 4.8；同批 Opus 5.5 fast mode 不再限第一方 API。見 [[entities/pricing#乘數：會互相疊乘]]
- **10-30｜Enterprise／API 可依承諾支出談客製折扣**（門檻未公開）。見 [[entities/pricing#當前生效的計費規則]]
- **10-15｜Team 年繳 20 席下限**。見 [[entities/pricing#方案可用性與帳務摩擦]]
- **10-11｜經 gateway／proxy 時，server-side classifier 檢查未送達就改計入用量** ⚠️。見 [[entities/pricing#當前生效的計費規則]]
- **10-09～11｜Haiku 5.5 依 prompt 長度分兩檔計價** ⚠️：逾 10 萬 token 改用 $0.50／$2.50，長脈絡不加價的待遇不適用。見 [[entities/pricing#模型 API 定價現況]]
- **10-09｜說明頁拿掉「改走額外計費需你明確同意」** ⚠️：開了 usage credits，額度用完就直接扣款；同日 Dashboards（beta）算進方案用量。條目見下方 10-09
- **10-06→10-24｜Claude for Startups 的免費 Team＋$1,000 額度暫停**，不受理新申請。見 [[entities/pricing#額度與通路的帳務坑]]
- **10-05 查證｜Sonnet 4.5 11-30 退役**（Claude API；夥伴平台另訂時程）。見 [[entities/pricing#模型 API 定價現況]]
- **09-22／09-28｜Opus 5.5 $4／$20、Sonnet 5.5 $2／$10 上線並成為預設**。見 [[entities/pricing#模型 API 定價現況]]
- **09-14｜週配額換軌** ⚠️：+50% 加成到期、永久 +25% 接手，水位約為加成期間的 83%。見 [[entities/pricing#現況]]
- **還沒證實的**：Ultra 取消 5 小時窗（10-30 Reddit）、Opus 5.5 實驗性用量重置。見 [[entities/pricing#還沒確定的計費變動]]

---

```

P602 原位改成一行指路：
```markdown
查證進度與現況見 [[entities/pricing#還沒確定的計費變動]]。
```

相關：
```markdown
## 相關

- [[entities/pricing]]：母頁，現在生效的規則、牌價與方案表
- [[entities/pricing-incidents]]：計費事故與額度異常
- [[topics/model-comparison]]：同一份工作換模型差多少
- [[topics/enterprise-cost-management]]：具名成本案例與省錢方法
- [[entities/pricing-archive]]：2026-04～06 的原始條目

```

P545、P949 由 h3 升 h2。

## D. archive entities/pricing-archive

- **A34**：「**最後更新：** 2026-09-20」→「**最後更新：** 2026-11-02」
- **A37**：「重點層（現行規則、牌價、還在發生的事故）都在主頁。」→「現行規則與牌價在主頁，還在發生的事故在 [[entities/pricing-incidents]]，價格沿革在 [[entities/pricing-history]]。」

- `## 2026-06` 依日期插入：P840–843（06-30，放在 06-26 之前）、P535–539（06-24，放在 06-09 之前）
- 檔尾新節（P847 改寫為下列兩行，P848、P851–948 照搬；P849 凍結 `%%` 砍）：
```markdown
## 計費切割風波

Agent SDK／`claude -p` 用量脫離訂閱、改按 API 費率的計畫：2026-05-14 公告、06-16 暫停，重推時間未定。政策本身已不在進行中，原始條目照搬於此；現行規則見 [[entities/pricing#當前生效的計費規則]]「訂閱配額制維持」。
```

# 進規則檔（`rules_patch.py`，臨時副本實套後 `check_rules.py` ✅）

### `.claude/reporter-rules/commercial/pages.md`：`## entities/pricing` 節整段換（到「骨架紀律」小節之前；sha256 鎖 `540edd8ef34f…`）

```markdown
## entities/pricing（母頁）與兩子頁

**子樹：** 母頁 `entities/pricing`（現在怎麼被計費）＋ 子頁 `entities/pricing-incidents`（計費事故與額度異常）、`entities/pricing-history`（價格、方案與促銷的沿革）；舊時段與死案共用 `entities/pricing-archive`。以下各條寫明表住哪一頁；沒寫的指母頁。

**0. 路由（一則新聞寫進哪頁）：**

| 事件 | 寫進 |
|---|---|
| 計費事故／爭議（誤扣、停用、付款流程故障、用量宣稱訴訟）、額度與速率的異常回報、灰色市場與轉售 | `entities/pricing-incidents` 對應事件流，並同步該頁 `## 還在發生的事故` |
| 價格、方案、促銷什麼時候變的（新模型牌價、方案改名、促銷起訖、方案頁改版） | `entities/pricing-history` `## 定價與促銷`，並同步該頁 `## 最近三個月變了什麼` |
| 變動生效後的現行事實 | 母頁對應表（下方同步動作表） |
| 具名成本個案、省錢方法 | `topics/enterprise-cost-management`；history `## 成本案例與優化` 只留一句價差結論＋wikilink |

母頁每日只動：頂部 callout、`## 往下鑽` 路由表的「最後動態」、`## 現況`（兩段，隨方案表／生效規則同批改寫），以及下方同步動作表列出的表與條列（方案表與 `### 方案細節`、`## 一小時／一個月大概多少`、`## 模型 API 定價現況`、`## 還沒確定的計費變動`、`## 當前生效的計費規則`、`### 額度與通路的帳務坑`、`### 方案可用性與帳務摩擦`；`.claude/reporter-rules/page-lifecycle.md` 母頁契約的登記例外）；`## 通路與乘數` 是主編週更（`.claude/reporter-rules/commercial/weekly.md`）。母頁 callout 日期不得早於子樹最新新聞（`scripts/check_hierarchy.py`）。母頁 `## 事故現在還在發生嗎` 只放「額度掉得快」三路分流（計費事故 → incidents 表；token 變多 → `topics/code-quality-decline` 三種解釋；自己的設定 → `topics/community-cost` 用量去向），不放事故表、不抄互動數；`entities/claude-code-known-issues` 的錨點指這個節名，節名不改。其下 `### 事故與爭議（誤扣費、靜默計費改動、帳號安全）` 是指路殼，`daily/` 讀者版日報錨點指入（不可改的過去），不動。

母頁每次寫入同步彙整表，不可只堆事件流（事件流住兩子頁）：

| 事件類型 | 同步動作 |
|---------|---------|
| 訂閱方案價格/內容變動 | **覆寫** `## 我的方案現在有什麼` 對應列 |
| 模型 API 定價變動（發布/促銷/到期） | 更新 `## 模型 API 定價現況`；深度對照留給 [[topics/model-comparison]] wikilink |
| 計費規則生效/暫停/到期 | 更新 `## 當前生效的計費規則`（一條一規則，註明來源日期；失效規則移除，表下「已失效並移除的規則」點名一句） |
| 通路政策變動、乘數新增或倍率調整 | **不由你維護**——`## 通路與乘數` 吃官方計價文件、非日報，由主編於 `/wiki-lint` 5e 依 `.claude/reporter-rules/commercial/weekly.md` 查證維護。日報出現此類線索時，在「同步自查」欄註明「⚠️ 需主編查證官方計價文件：[議題]」即可 |
| 計費事故／爭議（誤扣、停用、付款流程故障、用量宣稱訴訟） | 寫進 incidents 事件流，最新在上時**小標必帶狀態符號**，並依狀態整表**覆寫** incidents `## 還在發生的事故`（上限 8 列，排序與移出見下方「pricing 事件流的上限與退場」）。**狀態由你填，依據只有兩種**：官方一手來源（說明中心、官方 blog、issue 的官方回覆、Anthropic Status）或訴訟文件；日報的社群回報只能更新「最後動態」欄，不能翻狀態。**改 ✅ 需官方確認或修復版本號；改 ⛔ 需官方明示拒修；改 ⏸ 需距最後動態逾 90 天且本輪無新回報**——三者皆不成立就維持 🔴，並在回報寫「⚠️ 需主編查證官方是否已回應：[議題]」 |
| 牌價變動（新模型發布、費率調整） | **整表覆寫重算** `## 一小時／一個月大概多少` 三列；口徑固定為官方 Managed Agents 算例的 token 量，推算列須標「推算」 |
| 尚無官方一手文件的計費變動（傳聞、單一來源） | 加進 `## 還沒確定的計費變動` 一列；**查證屬實當批移出**，事實寫進它的家（方案表、API 表、生效規則），經過留在 history 事件流；查無官方者照懸置標記語法寫在表下「懸置細節」並帶複查日 |

時效性項目（促銷到期、政策生效日）須標截止日，並回報主編同步 feature-radar「⏰ 倒數中」。

### pricing 事件流的上限與退場（事件流住兩子頁）

每組一條判準，結論一律住表（incidents 的事故表、history 的三個月清單、母頁各表）：

- **灰色市場與轉售**（incidents）：只留一段結論＋[[topics/ai-agent-safety]] wikilink，不開條目。
- **事故與爭議**（incidents）：每個 `####` 小標必帶狀態符號（🔴 未解／✅ 已修／⛔ 官方拒修／⚖️ 司法中／⏸ 無後續），無狀態者不得寫入。🔴 ⛔ ⚖️ 同步上 `## 還在發生的事故` 表；轉 ✅／⏸ 即移出。**兩條不適用 90 天無後續**：⚖️ 在判決或撤訴前一律留表；官方曾公開承認過的事故（如已證實的帳務錯誤、Anthropic Status 通報）不轉 ⏸，改標 ⛔ 或維持 🔴 到官方給出結果。**留表優先序**：⛔ 與官方已公開承認的 🔴 ＞ ⚖️ ＞ 其餘 🔴 ＞ 單一社群回報型 🔴；**同層依最後動態新者在上，同日依事故起始日新者在上；不看留言數**。**單一社群回報型**＝只有一則社群來源（一篇貼文或一個 issue），沒有官方回應、也沒有第二個獨立回報者的 issue 或貼文。**上限 8 列**：滿了依留表優先序截斷，⚖️ 與官方已承認的事故不截。截下的每件寫進表下一行「還在發生、沒進上表的」（同一排序，日期＋一句），讀者看得見；不再寫 `%% 未列入總表 %%`。**若截下者仍為近 30 天內有新回報且非單一社群回報型的 🔴**，回報標「⚠️ 計費事故表全數活躍」交主編。表只寫 issue 號，留言數與讚數的家是 [[entities/claude-code-known-issues]]，事件流條目內的數字是當日快照、不回頭改。⏸ 且距最後動態逾 3 個月者列為蒸餾候選。
- **定價與促銷**（history）：事件流只記「什麼時候變的」；已生效的規則寫在母頁 `## 當前生效的計費規則`，事件流不重複。`## 最近三個月變了什麼` 是本頁自己的結論段：已生效、會改到帳單的變動一則一行（日期｜改了什麼｜指向它在母頁的家），官方確認的在前，未證實的收成最後一行指母頁還沒確定表；不必讀者操作就會改到帳單的標 ⚠️。新條目進事件流時同批加行；行的日期逾 3 個月者於 `/wiki-lint` 移除（條目留在事件流）。callout 只寫最新一則，不重抄這一段。
- **配額與速率**（incidents）：單一社群貼文型條目滿 90 天無官方或第二來源佐證，列為蒸餾候選。
- **計費切割風波**：2026-06-16 暫停，2026-11-02 以死案歸檔進 `entities/pricing-archive` `## 計費切割風波`（使用者 09-06 裁決）。政策若重啟，新事件寫進 history `## 定價與促銷`，archive 不回填。
- **成本案例與優化**（history）：具名個案與省錢方法的家是 [[topics/enterprise-cost-management]]，本組只留一句價差結論＋wikilink。

蒸餾與封存照 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存（全站通用）」，**每頁至多 2 個最舊時段**（incidents、history 各自起算）；兩子頁共用 archive 子頁 `entities/pricing-archive`（掛母頁）。
```

### `.claude/reporter-rules/commercial/daily.md`

原：
```markdown
| `wiki/entities/pricing.md` | 訂閱方案、計費政策、token 成本 |
```
新：
```markdown
| `wiki/entities/pricing.md`（母頁） | 訂閱方案、牌價、生效規則、還沒確定的計費變動等現行事實；子頁路由表「最後動態」。事故與沿革寫進下面兩子頁（路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條） |
| `wiki/entities/pricing-incidents.md`（子頁「計費事故」） | 計費事故與爭議、額度與速率異常回報、灰色市場與轉售；`## 還在發生的事故` 表 |
| `wiki/entities/pricing-history.md`（子頁「計費沿革」） | 價格、方案與促銷什麼時候變的；`## 最近三個月變了什麼` |
```

### `.claude/reporter-rules/page-lifecycle.md`

原：
```markdown
與 `## 時序`（只收公司動態），路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條）；
```
新：
```markdown
與 `## 時序`（只收公司動態），路由見 `.claude/reporter-rules/commercial/pages.md` 該節第 0 條；`entities/pricing` 的現況層——`## 現況`、方案表與 `### 方案細節`、一小時、模型 API 定價、還沒確定、當前生效的計費規則、帳務坑、可用性，以及路由表「最後動態」（`## 通路與乘數` 是主編週更），清單與路由見同檔 pricing 節第 0 條）；
```

### `.claude/reporter-rules/models/pages.md`

原：
```markdown
與 [[entities/pricing]]，本節只留一句指路
```
新：
```markdown
與 [[entities/pricing-incidents]]，本節只留一句指路
```

### `src/tests/test_reader_tags.py`

原：
```markdown
        "pricing": "答的是「要花多少」，不是「怎麼做」",
```
新：
```markdown
        "pricing": "答的是「要花多少」，不是「怎麼做」",
        "pricing-incidents": "同 pricing（第 24 波拆出的子頁）",
        "pricing-history": "同 pricing（第 24 波拆出的子頁）",
```

# 進腳本

**只有一處測試**（上方最後一筆 patch，`src/tests/test_reader_tags.py` EXCLUDED 加兩子頁，比照第 23 波 `7ec4d2b`）。其餘逐支確認不必改：
- `scripts/pending_markers.py` `reporter_of()`／`scripts/pending_handoffs.py` `owner_of()`：臨時副本實測兩子頁都回 `wiki-reporter-commercial`／商業（沿 parent 與領域 💼 商業）；不加覆寫。
- `scripts/check_hierarchy.py`、`gen_wiki_frontmatter.py`：子頁靠標頭「上層」欄接上；gen 後 index L56 投影三個子故事（archive、history、incidents）。
- `scripts/check_wiki_freshness.py`：兩子頁零自身歸因，靠上層歸因網址撐（`ancestor_att`）：incidents 的 11-01 兩個 Reddit 網址在 callout 與條目內；history 的 `claude.com/pricing`（10-30 歸因）在 callout。故 history 宣稱 10-30，不宣稱事件流裡 10-31 的 #47509（該則無歸因）。
- `scripts/scan_expiring_deadlines.py`：只掃 `entities/pricing.md` 的「⏰ … 到期」，母頁現無此字樣（L689–690 隨 history 走，是過去式敘述），不改。
- `web_reader/assets/app.js` `PPL_ISSUE_SHORT`：pricing 不在人物議題清單，不改。
- 不碰 `.claude/hooks/guard_roles.py` `GATE_FILES` 任一檔（`scripts/check_*.py`、`data/*baseline*.json` 等）。

