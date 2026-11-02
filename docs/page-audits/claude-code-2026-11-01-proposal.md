> **2026-11-02 註：** 本檔是第一輪提案，行號與數字以 `claude-code-2026-11-01-review.md`（重算後）與 commit `3a96d6b` 實作為準；文中「同 commit 重建 cell／reader-language 基線」已作廢（雲端 H6 擋，改由使用者本機重建，見 `-baseline-moves.md`）。

# 第 21 波設計提案：entities/claude-code 拆成母頁＋三子頁（2026-11-01）

> 上游：健檢卡 `claude-code-2026-11-01.md`、冷讀者 `wave21-cold-reader-2026-11-01.md`、查證 `claude-code-2026-11-01-verified.md`；七個裁決點照 ledger「2026-11-01｜第 21 波」條執行，不重開。裁決 (3)「砍現況 L48–109」**待使用者確認**，本案照預設出。
> 機械產物在 `scratchpad/w21/design/`（下稱 `D/`）：`newtext.py`（所有新寫文字的單一來源）、`split_cc.py`（切頁＋蒸餾，斷言原檔 1–1,231 每行恰消費一次，帳在 `accounting.txt`）、`verify_split.py`（獨立逐字核對＋懸置去 slug 比對）、`shield*.py`（🛡️ 組逐條對安全頁）、`build_tmp.sh`（臨時副本跑 gen 與各閘）、`cmp_hits.py`、`make_draft.py`、`out/wiki/entities/`（五頁改後全文）。行號一律指原檔。

## 1. 推薦案（一個）

先在同一刀蒸餾三批進共用 `claude-code-archive`（版本表發布早於 08-03 的列、歷史記錄 08 月 24 列、已解決 Status 事故 40 條），再把其餘原文一字不改、依問題分三群搬進 K／R／F；母頁留結論表、現況、路由與兩個同名指路殼。

| 頁 | 使命一句 | 節清單 | 正文行（`check_page_thickness` 口徑） |
|---|---|---|---|
| 母 `entities/claude-code` | Claude Code 現在有什麼毛病、哪些修了、哪些你得繞過去；版本、毛病、功能怎麼用，各往下鑽 | callout／往下鑽（路由表）／**現在還沒修好的**（上移到路由表下）／現況（版本兩條、近期平台與文件異動、近期報導、定位與市場、未歸類）／熱度與試用價值（＋反向對照）／版本更新（殼）／hooks（殼）／相關議題／參考來源 | **173**（上限 300） |
| K `entities/claude-code-known-issues` | 某個 bug 修了沒、誰會遇到、有沒有繞法 | callout／摘要（4 條：先看母頁表、💰 去 pricing、🛡️ 去安全子頁、修在哪版）／已知問題九組 | **432** |
| R `entities/claude-code-releases` | 現在到哪一版、我在 stable 還是 latest、哪一版加了什麼 | callout／**現在該跟哪條**（結論 4 條）／發布通道／最新版本（96＋2 列）／開發者須知（1 條）／歷史記錄（09–10 表、08–04 月總結） | **260** |
| F `entities/claude-code-features` | 功能怎麼用：hook 能不能當防線、subagent 派哪種、桌面版能做什麼 | callout／摘要（4 條）／核心功能／桌面版功能地圖／**桌面版文件時序**（新 h3，23 條自母頁現況搬來）／hooks／Subagent 型別差異對照／開發者須知（8 條） | **239** |
| archive（共用） | — | 04–07 各月段尾加「版本表（發布超過 90 天的列）」／新 `## 2026-08`／新 `## 服務穩定性：已解決的 Status 事故` | 337（153→337） |

- 原 1,201 行正文 → 173＋432＋260＋239，四頁皆不逾 600，不需 `拆頁評估` 交代；K 頁 `%%` 仍寫一行「不拆」與日後切法（平台相容性依 Windows／Desktop／Cowork），因為它以每月 17–33 條成長（健檢卡 §13）。
- 子頁三題：照健檢卡 §3 表，本案不改。子頁標頭照第 20 波：H1、使命一句、類型／狀態／領域（＝母頁 🛠️）／**`**上層：** [[entities/claude-code]]`**／首次出現／最後更新／最後新聞更新／`%%` 來歷；不帶「對照角色」（追蹤頁區只看根頁，`build_web.py` L709）。frontmatter 由 gen 生成：臨時副本實跑三子頁 `page_role: "child"`、母頁 `hub`、index L48 投影出四子頁＋mods。
- **與裁決數字的兩處差異**（逐筆核後，主 session 判）：
  - **N1** 版本表 90 天退場是 **82 列**不是 78（`awk` 取第 2 欄前 10 字元 < `2026-08-03`：04 月 2／05 月 20／06 月 30／07 月 30；含 L874 那列日期格帶註解的 v2.1.163）。
  - **N2** 🛡️ 組重疊 **17／獨有 10**，不是 16／11。`shield_home.py` 逐條找安全頁的家：L242 Downloads 在 `prompt-injection#2026-10` 有家（健檢卡判獨有）、L250、L269 在 safety-archive 有家 → 縮一行；L267 deeplink 的技術細節（`claude-cli://`、`--prefill`、`--settings=`、`SessionStart`）安全頁全無（`shield_unique.py`）→ 留全文；L266 隱寫術的 v2.1.197／v2.1.91 安全頁無 → 留全文。L274 Compliance API 不是故障，搬母頁接在 Compliance 條（L175–178）後。
- 🛡️ 一行的寫法：狀態＋修補版本＋互動數（互動數的家在 K，pages.md L167）＋一句「證據見 [[安全子頁#YYYY-MM]]」；原條目獨有的數字（Keyv 353／79、#2544 互參、v2.1.216 批次）收進那一行。有懸置標記的 5 條（L241、242、246、249、255）標記字串原樣保留在一行裡。

## 2. 照查證改的句子（全在 `newtext.py`）

stable＝2.1.309／latest＝2.1.316（母頁現況、R「現在該跟哪條」、R 發布通道；原 L703–704「落差已追上」刪）；2.1.309 rm 拒絕限 Desktop／VS Code（R 結論、R L721 格）；v2.1.316 列刪「原文截斷」、補 fast mode 11-30 移除與 PowerShell hook exit 2（格長 ≤120，`CLAUDE_CODE_SUBAGENT_EFFORT` 放不下，留給下輪）；R、母頁 callout 補 fast mode 棄用；補 v2.1.289、v2.1.269 兩列；2.1.313 不寫成列，改一條 🔎（標 11-01｜查 2.1.313、Cursor 延伸套件｜複 11-15），指 product-vulns；結論表 #4953 格補「07-19 社群回報 2.1.181／2.1.214 起安裝程式記憶體下降」；hooks 結論改「一觸發就是硬擋，但不保證會觸發」三子條（查證 #8 逐字依據）；L1006「五個 🔴 都是靜默不作用」改三個＋兩個是功能請求（冷讀者撐不起句）；subagent 補「平行分派選哪種」（背景、20 個、fork 何時）並把 L1056 斜線串拆成五步（冷讀者 Q4）；L697 刪無連結的 W40 句；L708 與母頁 L226 的斷錨改指 `[[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]`。⟨Q-14⟩、⟨Q-15⟩ 已結案，隨 08-14 列進 archive `## 2026-08`（成對搬，非新語法標記，不計數）。

## 3. 錨點入邊逐筆去向

| 入邊 | 現指 | 拆後 | 誰改 |
|---|---|---|---|
| feature-radar L28、L52、L467 | `#版本更新` | 母頁殼仍活；改指 `entities/claude-code-releases#最新版本` | handoff → 主編 |
| claude-tag L45 | `#版本更新` | `entities/claude-code-releases#最新版本` | 實作者（同維護者） |
| daily/ 4 筆（10-21～10-24） | `#版本更新` | 母頁殼，不動（讀者版日報不回改） | — |
| features/pages.md L110 | `#版本更新` | 改指 releases（見 §5） | 規則檔 |
| cowork L52、L78 | `#已知問題` | `entities/claude-code-known-issues#已知問題`（**不改 build 紅**：臨時副本實測 2 筆錨點 WARN＋ERROR） | 實作者 |
| cowork L78 | `#現在還沒修好的` | 母頁，不動 | — |
| coding-workflow-guide L393、community-guardrails L86 | `#hooks：…` | 母頁同名殼接住；改指 `entities/claude-code-features#hooks：…` 後殼可刪 | handoff → 開發實務、社群 |
| claude-code L113（自指） | `#桌面版功能地圖` | `entities/claude-code-features#桌面版功能地圖` | 本頁 |
| 文字指名 9 筆 | — | cowork L37、L97→K；claude-skills L81「近期平台與文件異動」→F「桌面版文件時序」（實作者）；radar L426「🔌 MCP 整合」、L1212「💰 計費與配額」→K（主編）；radar L50、code-quality-decline L225、pages.md L118 指「現在還沒修好的」不動；三份跨維護者規則檔見 §5 | — |

臨時副本套用本案＋cowork／claude-tag 兩處後：`build_web.py` `wikilink 健檢合計：斷鏈 WARN 23／錨點 WARN 0`（改前同為 23／0），exit 0。

## 4. 懸置與保命

- 原檔新語法 29＋archive 1＝30 → 拆後 母 6／K 20／R 2／F 2／archive 1＝**31**（+1＝2.1.313 🔎）。`verify_split.py` 去 slug 比對 `(標記日, 探針)` 多重集：拆後＝拆前＋那一筆，exit 0。
- **計數閘看不住這次**：`check_pending_markers.py` `_marker_count_gate`（L288）基線是 206、全庫現有 211，靜默少 5 筆以內都不紅。所以保命靠 `verify_split.py`（驗紅：刪 K 的 fsmonitor 標記行＋一條 🔴 → 兩處都抓到、exit 1），實作後主 session 跑 `--rebuild-count --reason "第 21 波 claude-code 拆頁：23 筆換 slug、+1 2.1.313"`。
- 舊字樣棘輪（L396）：全庫 20→18（縮行刪掉 L246「官方未載」、L255「未證實」兩處原句，新寫的一行改用「changelog 沒寫」「官方沒有證實」）；只擋增加，不觸發。
- 砍整節只有一處：**現況 L48–109（待使用者確認）**。它唯一不在版本表的事實是 v2.1.289、v2.1.269 兩版，已補成 R 表列；62 行內無懸置標記（`accounting.txt` L48–109 全標「砍」，`verify_split` 比對標記數不變為證）。

## 5. 規則檔要改的地方（逐字在 draft「進規則檔」）

- **features/pages.md**：`## entities/claude-code`（原 L126–147）拆四節：母頁（使命、路由表＋依序四問、每日准動五樣、結論表條文原文、兩個同名殼）；K（狀態維護原 L128–132、互動數之家、Status 事故翻 ✅ 滿 30 天移 archive）；R（結論層「現在該跟哪條」、90 天退場線改成已生效條文、節名凍結改寫、官方 changelog 沒有的版號不成列）；F（桌面版文件時序＋地圖同輪補、hooks／subagent 只收官方文件寫得出的、90 天回訪）。L110、L116、L167、L252 改指子頁；原 L146 年齡政策改住母頁現況。
- **features/daily.md**：負責頁表 L15 一列變四列；L29 GitHub Issues → K；L80 純 bug fix → R 版本表。
- **page-lifecycle.md** L52 例外清單：加「`entities/claude-code` 的 `## 現在還沒修好的` 與 `## 現況`」（**N3**：現況每天收傳聞、帳號政策，母頁不是唯讀；與 ai-agent-safety 只開一張表不同）。
- **sweeps.md 5a** 加一句（**N4**：功能類沒有 `weekly.md`，母頁週更觸發邊放主編親做的 5a）：同輪查 npm dist-tags，改母頁「版本」與 R「現在該跟哪條」第一條的 stable／latest。
- **跨維護者，主 session 判**：safety-policy/pages.md L87（執行第 20 波裁決 4：K 只留版本號綁定的修補狀態一行，刪「兩頁狀態不同時以新者為準」）；models/pages.md L155、commercial/weekly.md L35、community/pages.md L134 的「家在 [[entities/claude-code]]」→ K；classification.md L68 → R；shared-when.md L14、L16 的 86K token 例改成「拆頁前約 86K；拆後最大的是已知問題子頁約 137K 字元」；reader-digest format.md L49 是範例，不改。

## 6. handoff 清單（由主 session 開帳，先 dry-run）

| # | --to | 頁 | 事項 |
|---|---|---|---|
| 1 | 開發實務 | topics/coding-workflow-guide | L197「PreToolUse 最硬……連 bypassPermissions 都擋得住」無官方逐字句，照查證 #8 改成「觸發即硬擋（先於 allow 規則）、不保證觸發」並附 permissions 文件 11-01；L393 錨點改指 `entities/claude-code-features#hooks：事件、失效模式與能不能當防線` |
| 2 | 社群 | topics/community-guardrails | L86 錨點同上改指 features |
| 3 | 主編 | feature-radar | L28／L52／L467 改指 `entities/claude-code-releases#最新版本`；L426、L1212 文字指路改指 K；冷讀者：L26 核對只到 v2.1.304，L50「沒有東西擋著你升級」撐不起，補核 2.1.305–316（2.1.316 fast mode 移除是破壞性） |
| 4 | 主編 | index | L48 鉤子改寫（現為「功能、已知問題、社群工具」）；開發實務入口補「升版／stable 還是 latest」「用 hook／權限擋危險指令」兩列（冷讀者最想改 1） |
| 5 | 安全政策 | topics/ai-agent-safety-product-vulns | 目前結論「2026-10-30 npm stable 是 2.1.308」→ 11-01 為 2.1.309；Cursor 事件的「2.1.312 與 2.1.313」官方 CLI changelog 無 2.1.313，請寫明是 Cursor 市集延伸套件版本；K 🛡️ 17 條已改為一行指向本頁 |
| 6 | 安全政策 | topics/ai-agent-safety | L78「把 DROP、DELETE、`rm -rf` 設成要顯式確認」補連 `entities/claude-code-features#hooks：…` 與 deny 規則（冷讀者 Q3） |
| 7 | 社群 | topics/code-quality-decline | #38335 互動數（:96 記 791）與 pricing（:307 記 855）不同步；互動數的家是 K，改成只寫 issue 號＋指 K |
| 8 | 商業 | entities/pricing | 冷讀者最想改 3（「額度掉得快」三路分流、上限 6 列造成漏讀）——屬第 24 波對象，登帳即可 |

既有帳：H-7526b2（Downloads，K L242 已有條目＋標記）、H-1458cf（2.1.313，R 🔎 一條）、H-6e641e（128 MB，K 💰 L316 已有標記）三筆可結案；同維護者鄰居 cowork、claude-tag、claude-skills、anthropic-agent-stack（L89 補連 `entities/claude-code-features#Subagent 型別差異對照`，冷讀者 Q4）由實作者直接改入口句。

## 7. 不選的方向

- **兩子頁（F 留母頁）**：母頁約 333 行超過 300（裁決 1）。
- **F 併進 coding-workflow-guide**：它答「官方建議」、已 688 行，且跨維護者（裁決 1）。
- **`#版本更新` 入邊全改指 R、母頁不留殼**：daily/ 4 筆讀者版日報不回改，會永久斷（裁決 2）。
- **R 自開 archive**：第 18、20 波都共用一份（裁決 4）。
- **claude-mods 改掛 F**：只換父節點（裁決 5）。
- **🛡️ 重疊條目原文搬進 archive 留底**：標記會在 archive 多一份（同一事實兩個家），獨有數字已收進一行。
- **hooks 殼改成母頁 h3 結論段**：殼只為接兩筆跨維護者錨點，handoff 1、2 落地即刪，不值得變成母頁長期結論。
- **結論表留在現況之後**：冷讀者 Q1 卡在「表前 150 行現況」，使命句的答案上移到路由表下。

**可行性前提**：wiki 九檔（母＋三子＋archive＋cowork、claude-tag、claude-skills、anthropic-agent-stack）、規則檔 5 份＋sweeps、`gen_wiki_frontmatter.py`、cell 基線 `--rebuild --allow-grow`（107 筆搬家）、reader-language `--write-baseline`（2 筆搬家，見 §8）、pending `--rebuild-count`、handoff 與 `wiki/log.md` Query 條目都在同一個 commit 進去並 push（page-lifecycle 階段 2、4）；cowork 兩錨點沒改，`build_web.py` 當場 ERROR。

## 8. 閘（臨時副本 `/tmp/w21_{before,after}`，`D/build_tmp.sh` 一鍵重跑）

| 閘 | 改前 | 改後（最後一行原樣） | 看守什麼（行號） |
|---|---|---|---|
| `verify_split.py` | — | `結論：OK　照搬行逐字核對、懸置標記 30→31（+1＝2.1.313）` | 驗紅見 §4 |
| `check_hierarchy.py` | ✅ 31 母頁 | `狀態：✅ 通過（31 個母頁）` | L138 hub 不落後；驗紅：母頁 callout 改 10-30 → `❌ hub 落後：entities/claude-code callout 日期 2026-10-30 < 子樹最新新聞 2026-10-31`；L122 領域繼承、L123–129 archive 掛父 |
| `check_pending_markers.py` | 通過 | `狀態：✅ 懸置標記語法檢查通過`（新語法 212、舊字樣 18） | 計數閘 L288 看不住，見 §4 |
| `check_reader_language.py` | OK | `FAIL: 讀者語言閘 — 2 筆新增的內部用語外洩` | 兩筆都是搬家原文的產品詞「對話封存」（K 📂 組 10-24 複查句、R 09-01 列），基線以頁為鍵（L308）；新寫文字 0 筆（`newtext.py` 187 段另以 TERMS 與 LEGACY_RE 自查 0 命中） |
| `check_cell_limits.py` | OK | `FAIL: 字元上限機械閘 — 107 筆新增的超限儲存格／條列` | 全是搬家原文（`cmp_hits.py`：改後 232 筆，不在改前 243 筆內的 0 筆）；新寫文字第一版 4 筆超限（316 列 159、309 列 131、🔎 條 201、L910 201）已改到 0 |
| `check_wiki_freshness.py` | OK 131 頁 | `OK: wiki 新鮮度檢查通過（134 頁；衍生頁 11 頁已宣告觸發邊）` | `ancestor_att` L201–211 |
| `build_web.py` | 斷鏈 23／錨點 0 | `wikilink 健檢合計：斷鏈 WARN 23／錨點 WARN 0`（含 cowork／claude-tag 兩處） | `check_wikilink_anchors` L372 |
| `run_tests.py` | — | 2 FAIL＋1 ERROR：cell（第 8 步後消）、devpractice 兩測試要 git（副本改前即紅） | — |

## 9. 需主 session 裁的新裁決點

- **N1** 退場列 82（非 78）、**N2** 🛡️ 17／10（非 16／11）：見 §1，依據在 `D/accounting.txt` 與 `shield_unique.py` 輸出。
- **N3** page-lifecycle 例外清單納入母頁 `## 現況`（備案：現況的傳聞與帳號政策移到 F，母頁只剩版本兩條＋定位——但傳聞多與產品而非功能用法有關，放 F 是雜物間）。
- **N4** 週更觸發邊放 sweeps 5a（備案：新開 `features/weekly.md`，要改角色檔讀檔清單）。
- **N5** K「Status 事故翻 ✅ 滿 30 天移 archive」是新條文（不寫，40 條三個月後又長回來）。

## 10. 最不確定的一件事

母頁 `## 現況` 仍是每日進料的混合區（傳聞 33 行＋平台 20 行＋定位 5 行）。它守得住 300 行靠的是傳聞查證後結案搬走，目前沒有機械看守；若三個月後母頁回到 250 行以上，該問的是「近期報導」要不要成為第四個子頁。
