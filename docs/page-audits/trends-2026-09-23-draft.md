# 第 17 波設計者逐字稿：topics/community-pattern-trends

三大欄：**A 進頁面**（可直接貼上）、**B 進規則檔**（檔名＋節名＋取代哪幾行）、**C 轉知**（`pending_handoffs.py open` 完整參數）。
行號＝對象頁**檔案原始行號**（含 frontmatter），與健檢卡 `trends-2026-09-23.md` 同一套。官方事實只取 `trends-2026-09-23-verified.md` 已錨的句子（§一-1／-3／-4／-5、§二、§三）；趨勢六的官方句只轉述 `official-community-gap` L60 既有內容，趨勢三／五／九的官方零件只指 `community-large-codebase-workflow`，不另引官方原文。
`<實作當天>` 由實作者填當日日期。A-1 整份套進 scratchpad 副本的實測：**338 → 322 行**；本頁 `check_cell_limits` 0 命中（原基線內 5 筆全數改寫到 ≤200）、`check_reader_language` 0 命中；九條標題日期＝各條演進最後節點日期 9/9；帶 HN 分數節點 14 個全數照圖例分級、其餘 57 個皆標「（估）」。**實作者只看末節「# 實作單（最終版）」。**

**保命條款**
- **懸置標記**：本頁改前改後 `iter_pending()` 皆 0 筆；新稿不含 `pending_markers.py:60–61` `LEGACY_RE` 任何字樣（原 L136「未經官方證實」也不在清單內，已改寫）。全庫 **119 → 119**（基線 106）、舊字樣 **40 → 40**（基線 42）——scratchpad 副本 `check_pending_markers.check()` 實測。
- **字元上限基線**：`data/cell-limit-baseline.json` 本頁 5 個指紋（原 L98、L99、L203、L238、L259）改寫後不再命中，成為孤兒指紋；`split_hits()` 只看「命中是否在基線內」，孤兒不會轉紅，**不跑 `--rebuild`**（`check_cell_limits.py:253–255` 要求全庫重建且需人工確認，不屬本波）。
- **錨點與腳本**：全庫無 `[[topics/community-pattern-trends#…]]` 錨點；`scripts/`、`web_reader/assets/`、`src/tests/` 無人 grep 本頁節名（`page-lifecycle.md:16` 查法實跑）；`review-registry.json` 對本頁只有 `bare_name_search_dirs`（L91），節名與標題可改。LCW L74「趨勢六」、llm-wiki L69「趨勢九」按編號引用——**九條編號與順序不動**。
- **agent-channels 不補**：主 session 列的五則之一，但 patterns 本體沒有它的節點（只在模式概覽表 L65 與類別細節 L86 列名，最早見 `news/2026-06-27.md:64`），不是 09-19 那窗漏收的節點；改記進頁尾 `%%`。實補四則：spec-kit（趨勢七）、hcom（趨勢二）、Skillsync、hister（趨勢九）。

---

# A. 進頁面

## A-1 對象頁正文（取代 L27–L338 全部；L1–L26 frontmatter 不手改，實作單第 10 步由腳本重產）

九條趨勢的編號、順序、名稱不動；只換狀態標、熱度標與下列內容。整段貼上：

````markdown
# 社群趨勢觀察（週更）

**狀態：** ongoing
**領域：** 🌐 社群
**更新頻率：** 🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）
**開始日期：** 2026-06-29
**最後更新：** <實作當天>
**最後新聞更新：** <實作當天>

> **最新趨勢觀察**（<實作當天>）
> - **Hook 要回 exit 2 才擋得住**：官方 hooks 文件寫明 exit 2 才會攔下工具呼叫，exit 1 只算非阻擋錯誤、動作照跑；本頁趨勢一先前寫成「exit 1 硬攔截」，已更正。
> - **三條方向官方已有對應**：模型路由（`opusplan`）、手機遠端控制、跨 session 記憶（auto memory），各條先看官方給了什麼；模型路由 8/14 之後社群沒有新做法進來。
> - **新做法**：規格驅動多了 GitHub 的 spec-kit（9/12），跨 session 記憶多了 Skillsync、hister（9/17–9/18），多 agent 互通多了 hcom（9/16）。

---

## 摘要

9 月中，社群做法收斂成的九個方向裡，模型路由、手機遠端控制、跨 session 記憶三條官方已有對應零件；模型路由 8/14 之後社群沒有新做法進來，標為淡出。本頁按時間排出每個方向怎麼走到今天，並列出看到這條線，你現有的設計可以回頭檢查什麼。

- **和 [[topics/community-tech-patterns]] 差在哪**：那頁是每一種做法的原始證據型錄，模式概覽表標出每一類的成熟度與最後動態；本頁只挑已經收斂成方向的，按時間排、講回頭檢查什麼。
- **其他鄰居**：大 repo 四面牆現在該怎麼做、官方零件在哪，見 [[topics/community-large-codebase-workflow]]；觀念爭論見 [[topics/community-tech-discussions]]；7 月以前的最早出處見 [[topics/community-tech-patterns-archive]]。
- **兩把尺**：標題的「方向已收斂」量的是做法有沒有收斂成一個方向，不是用的人多不多；採用量看 patterns 模式概覽表的成熟度（✅⚡⏳），兩者可以不同——例如規格驅動方向已收斂，採用仍屬新興。
- **最近一次動靜**：標題上的日期是最後一個做法進來的那天；近 30 天本頁與 patterns 都沒有新做法進來，標「↘ 淡出」——淡出不代表做法失效。
- **🔥 熱度（注意力，非技術力）**：寫了 HN 分數的條目照分數分級——🔥🔥🔥🔥 ≥100、🔥🔥🔥 30–99、🔥🔥 10–29、🔥 <10（2026-09-23 判定）；標「估」的沒有 HN 分數，是收錄當時依來源數與互動量的估計。

---

## 已收斂的方向

### 趨勢一：強制層取代建議層　`方向已收斂`　最近一次動靜 2026-09-06

**演進：**
- 🔥🔥（估） **Hooks 強制執行機制**（5/06）：用 Hooks 在工具呼叫前後攔截行為，而非只在 CLAUDE.md 寫「請不要…」
- 🔥🔥（估） **每新規則必刪一條**（6/20）：發現 CLAUDE.md 規則一多反而降低遵守率，提出規則總量硬上限
- 🔥🔥🔥（估） **Hooks 取代 CLAUDE.md 規則**（6/23）：正式定調——「必須 100% 執行」的規則搬進 Hooks，CLAUDE.md 只留偏好與風格
- 🔥🔥（估） **Pre-completion Hook**（6/25）：用 Hook 偵測模型「讓我知道如果…」式的模糊收尾，攔下來強制它真正做完
- 🔥🔥🔥🔥 **環境感知條件觸發（Adrafinil）**（6/28，HN 124）：hooks 不再只是業務邏輯觸發器，而是升格為「感知 agent 活躍狀態 → 決定環境副作用是否觸發」的條件控制器；可延伸至 Slack DND、資源分配等場景
- 🔥（估） **氛圍狀態燈**（7/2）：同一「hooks 感知 agent 活躍狀態」機制的第二個獨立實作——驅動實體 LED 燈號提示 agent 執行狀態，確認此條件觸發模式非單一作者的個案巧思，而是可複製的機制
- 🔥（估） **規則遵循率變 100% 新實例**（8/25，dev.to）：將原寫在 prompt 裡的規則改用 hooks 強制執行，遵循率從「機率性」變成 100%；附帶效益是規則確定性提升後，改用較便宜的 Haiku 當 builder 也不再顯得冒險，補上「強制執行降低模型成本門檻」這個先前未明說的連結
- 🔥（估） **claude-code-hooks 外掛市集**（9/6，525★）：把多個 hook 打包成可安裝的市集，從「單一 hook 各自維護」進到「市集化分享」，延伸 Hooks 強制執行路線的散布方式

**代表模式：**
- **Hooks 強制執行取代 CLAUDE.md 規則**：把 deploy 保護、formatter、migration 防寫等「必做」遷到 PreToolUse / PostToolUse hook，以 exit 2 攔截（見下方「Hook 怎麼擋」）
- **ANMA 架構邊界合約**：用 YAML 合約定義架構邊界 + Hook 強制驗證，讓便宜模型也守得住規則（實測 0/20 vs 無約束時 13/19 違規）
- **Pre-completion Hook**：Stop Hook 掃描最後一輪輸出，偵測到模糊結束語句就以 exit 2 結束——官方語意是阻止 Claude 停下、繼續對話，逼模型把事做完

**對現有設計的啟示：** 你 CLAUDE.md 裡任何「必須 100% 遵守」的規則都放錯位置了——LLM 是機率性遵守，規則越多遵守率越低。把它們分成兩類：偏好留 CLAUDE.md，邊界搬 Hooks。

判斷標準只有一個：**「這條規則被遺漏一次，我會生氣嗎？」** 生氣 → Hook，無所謂 → CLAUDE.md。

| 規則 | 放哪裡 | 原因 |
|------|--------|------|
| 「用繁體中文回答」 | CLAUDE.md | 偶爾漏了只是語言問題，不影響系統正確性 |
| 「不加多餘注釋」 | CLAUDE.md | 風格偏好，判斷空間大，偶爾多一行無傷大雅 |
| 「不可 `git push --force` 到 main」 | PreToolUse Hook | 一次失誤就是事故，不能靠機率 |
| 「commit 前跑測試」 | PreToolUse Hook | 緊急狀態下 LLM 最容易「忘記」這條 |
| 「不可讀 `.env` 檔」 | PreToolUse Hook | 安全邊界，一次洩漏就是問題 |
| 「.ts 檔寫完後跑 prettier」 | PostToolUse Hook | 格式一致性是死規定不是建議 |

**Hook 怎麼擋：** PreToolUse hook 以 exit 2 結束，這次工具呼叫就不會發生；exit 1 只算非阻擋錯誤、動作照跑——照 Unix 習慣回 1，會寫出以為在擋、其實不擋的閘。也可以在 stdout 回 JSON `permissionDecision: "deny"`（[官方 hooks 文件](https://code.claude.com/docs/en/hooks)）。各層該放什麼、`deny` 連 bypass 模式都擋得住，見 [[topics/coding-workflow-guide]]。

---

### 趨勢二：Multi-agent 隔離工程化　`方向已收斂`　最近一次動靜 2026-09-16

**演進：**
- 🔥（估） **零星嘗試**（4/26）：多 agent 概念出現，但還沒解決「互相踩到彼此檔案」的問題
- 🔥🔥🔥（估） **Git Worktrees 作為隔離原語**（5/23）：找到關鍵解法——每個 agent 配一個 git worktree，檔案系統完全隔離
- 🔥🔥（估） **並行工作流轉型指南**（6/24）：從「單一 prompt 反覆調整」的線性做法，轉為「任務分解 → 並行派發 → 彙整驗證」
- 🔥🔥（估） **20-instance 崩潰分析**（6/26）：實測從 4 個擴到 20 個並行時的崩潰原因（git lock 競爭、context 洩漏到鄰近 agent）與對策
- 🔥（估） **套件化／伺服器化部署**（7/11、7/15）：ccteams（7/11）將驗證良好的 builder+reviewer subagent 組合打包為可跨專案安裝的 npm 套件；OtoDock（7/15，多家報導）將 Claude Code + Codex 團隊部署至自有伺服器；隔離原語確立後，趨勢重心轉向「配置可重用性」與「常駐化部署」
- 🔥🔥🔥 **本地合併佇列**（7/30，HN 42，多家報導）：隔離原語（worktree）與並行派發問題已收斂後，新缺口浮現在下游——多個平行 agent 產出的 commit 若各自即時觸發建置測試，會拖垮低規格機器並推高 CI 帳單；Claude Code Merge Queue 讓提交排隊依序落地、逐一完整測試後才合併，補上「執行後如何序列化整合」這個先前未被觸及的環節
- 🔥🔥🔥 **常駐雲端運算基礎設施（machine0）**（8/18，Launch HN 83）：YC S26 新創把常駐部署從自架伺服器延伸到商用雲端 VM（含 GPU、CLI／MCP 可操作），鎖定 6–8 小時起跳的長時間 agent 工作；作者也點名常駐拉長 `--yolo` 曝露時間的安全代價，見 [[topics/ai-agent-safety]]
- 🔥🔥（估） **跨代理統一容器第三波（opencodex／metaharness／claw-orchestrator）**（8/27）：繼 8/5 omnigent、8/9 loopx＋HarnessFlow 之後第三批同類專案，「可換底層 agent」成了持續方向；同日 Concord（Show HN，MCP）走互補路線——不統一容器，讓各自獨立的 agent 共享任務脈絡
- 🔥🔥（估） **統一容器路線第四波（avibe／ccteam／agent-orchestrator／OtoDock）**（9/9–9/10）：avibe（本機常駐 Agent OS）、ccteam（跨廠商團隊整編）、agent-orchestrator（全流程平台，11,149★）三種取向湧現；OtoDock 同期定位為「公司作業系統」，統一容器路線分化出 OS／團隊／平台三層
- 🔥（估） **proliferate：統一容器再添「IDE 化」取向**（9/13）：把多 agent 平行執行包進開源 AI IDE 介面，OS／團隊／平台三層之外的第四種取向；僅星數佐證，尚無採用回饋
- 🔥（估） **hcom：任務脈絡互通第二例**（9/16）：跨終端機讓 8 種 coding agent CLI 互相傳訊、監看、生成彼此，走 Concord 那條「不統一容器、只互通脈絡」的路；僅星數佐證

**代表模式：**
- **Git Worktrees 隔離原語**：多 agent 各持獨立 worktree，根除共享目錄的覆蓋衝突
- **20-instance 崩潰分析**：超過 10 個並行就需要 orchestrator 協調層，且要從小規模漸進擴展
- **Personas vs Tool-scoping**：用「每個 agent 只掛載其職責所需的工具」當邊界，比「你是 QA」這種角色描述可靠——模型能無視身份，但無法呼叫沒掛載的工具
- **套件化 Subagent 團隊（ccteams）／伺服器化團隊部署（OtoDock）**：把已驗證的 subagent 組合封裝成可安裝套件或常駐服務，降低每個新專案重新手寫協作邏輯的重複勞動
- **本地合併佇列（Claude Code Merge Queue）**：多平行 agent 的 commit 依序落地並完整測試後才合併，取代各分支即時觸發 CI 的做法，緩解資源競爭與費用暴增
- **跨代理統一容器 / 任務脈絡互通**：omnigent／loopx／claw-orchestrator 讓單一 orchestration 層可替換底層 agent（Claude Code／Codex／Cursor 等）；Concord、hcom 走互補路線，不統一底層卻讓各自獨立的 agent 共享任務脈絡

**對現有設計的啟示：** 回頭檢查三件事：多個 agent 是不是共用同一個工作目錄（10 個 agent 同時改 `utils.py`，後寫的蓋掉前寫的，錯誤還不可復現）；「只能看不能改」是寫在角色描述裡，還是真的沒掛 Edit／Write 工具（模型能無視身份，但叫不動沒掛載的工具）；平行產出的 commit 是各自觸發 CI，還是排隊依序落地。現在該怎麼做、官方已內建哪些零件，見 [[topics/community-large-codebase-workflow]]。

---

### 趨勢三：Context 主權爭奪　`方向已收斂`　最近一次動靜 2026-09-10

**演進：**
- 🔥🔥🔥（估） **Context 是核心瓶頸**（5/12）：確認大型專案的真正天花板是 context 管理，而非程式碼生成品質
- 🔥🔥🔥（估） **Context Rot 修復五法**（6/20）：「Claude 越用越笨」幾乎都是 context 腐蝕；五種具體修復策略成社群共識
- 🔥🔥🔥（估） **三連發：Just-in-Time / Repo-as-Memory / 避免預加載**（6/26）：同期三篇互補，把「context 精準性優於完整性」推成新原則
- 🔥🔥（估） **Context 上限主動截斷**（6/29）：agent 讀取上限設計——56KB 問題揭示 agent 為「確保完整性」反而讀入噪音；明確設定讀取上限（行數/字元數）是 context 管理的防禦性基礎設施
- 🔥（估） **使用者可視化分支/合併對話**（7/15，多家報導）：從工具層自動裁剪延伸出使用者互動層的手動控制——從任一歷史訊息分支出新對話、可合併多個對話串，讓使用者自行精準決定 Claude 後續看到的 context 範圍
- 🔥（估） **pxpipe：圖片化 context**（8/5）：反其道而行的新技巧——把文字 context 渲染成圖片再傳遞，以此降低 token 用量，補上「context 精簡」家族中「改變媒介」而非「裁剪/摘要」的第三條路徑
- 🔥（估） **已否決方案的隱形重工成本**（8/7）：為 Repo-as-Memory 補上「記什麼不該再做」子類別——已否決的架構方案若未結構化索引，agent 會重新實作團隊已經殺掉的做法；「repo 即記憶體」的外化對象從「已決定的事」擴大到「已否決的事」
- 🔥（估） **headless 呼叫冷啟動固定成本**（8/7）：量化實測——`claude -p` 未加 `--bare` 時冷啟動約先耗 15 萬 token，補上「多 agent pipeline 大量發起 headless 呼叫」這個此前未被量化的 context 成本來源
- 🔥🔥🔥 **grep 輸出裁剪（Graft）**（8/15，HN 39，多家報導）：「context 精簡」家族補上第四條路徑——不裁剪檔案內容或轉換媒介，而是直接攔截並精簡 grep 搜尋本身的輸出，宣稱降幅 42%；但 HN 討論質疑其 benchmark 段落疑似 AI 代寫，是本頁少見「機制方向成立、量化宣稱本身未經第三方驗證」的案例
- 🔥（估） **子代理歷史重送疑慮**（8/27，Reddit）：「裁剪什麼」四條路徑之外的新警訊——四個平行 fork 子代理共耗約 200 萬 token；官方證實 fork 會繼承父對話，每次重送、累積多快只有這則單一回報（見 [[topics/community-large-codebase-workflow]]）
- 🔥（估） **nightshift：DAG 調度＋三層 context 管理疊加**（9/10，Show HN）：不限廠商 Rust CLI，以任務相依圖調度協調 GitHub Issues，疊 PCC 記憶＋本地向量 RAG＋滑動視窗三層因應多 issue 工作流的 context rot；作者具名指出官方 `/goal` 有相同架構缺陷改自製，屬單一開發者對官方功能的負向對照，未經獨立覆核

**代表模式：**
- **Context 裁剪 Tool Output**：主動截斷或摘要化工具回應，而非全量塞入 context
- **Just-in-Time @-file Retrieval**：不預先 @ 一堆檔案，只在需要時才即時取回
- **Repo-as-Memory**：模型是工作者、repo 才是記憶體；已決定（與已否決）的事外化成檔案，不寄望模型跨 session 記住
- **Compact Memory**：以語意摘要取代每輪重送完整 transcript，把 O(N²) context 開銷壓回接近 O(N)（附可跑 benchmark）
- **對話分支/合併**：使用者可視化操作介面取代工具層自動裁剪，適合需要精準人工掌控 context 範圍的場景
- **pxpipe（圖片化 context）**：把文字轉成圖片傳遞以降低 token 用量，是「裁剪/摘要」以外的第三種瘦身路徑

**對現有設計的啟示：** 回頭檢查：CLAUDE.md 開頭是不是預先 @ 了一堆檔案；團隊已定的決策是寄望模型記得，還是寫成 repo 裡的檔案；腳本與排程呼叫的冷啟動成本算進去了沒。對話後期它開始「忘記」前面說的事，先懷疑 context 被早期塞入的文件稀釋，不是模型變笨。現在該怎麼做、官方零件在哪，見 [[topics/community-large-codebase-workflow]]。

演進裡的「讀取上限」（6/29）與「已否決方案索引」（8/7）是社群走過的路，不是現在的建議：官方已內建讀取上限、對應的官方 issue 已關閉，見 [[topics/coding-workflow-guide]]。

---

### 趨勢四：模型路由自動化　`方向已收斂`　↘ 淡出・最近一次動靜 2026-08-14

**演進：**
- 🔥（估） **Dragoman 多模型路由**（5/13）：早期單一分享，用顯式規則手動指定哪個任務走哪個模型
- 🔥🔥（估） **三角色分工 Pipeline**（6/25）：Claude 規劃 / Codex 建功能 / ChatGPT 查詢，各司其職並定義交接協定
- 🔥🔥🔥🔥 **Workweave Router**（6/27，HN 216）：**引爆點**，嵌入式自動路由依請求難度選模型，無需手動規則
- 🔥（估） **本地小模型分流（Fast Context Task Router）**（7/5，**原專案已下架，不要照著找**）：把程式碼探索分流給本地 Ollama 小模型，聲稱省 50–60% context token（代價是執行時間增加）
  - 2026-09-13 複查：原專案 07-05 起下架、原因未公開。替代：官方最接近的是 `CLAUDE_CODE_SUBAGENT_MODEL` 把 subagent 指到便宜模型；本地模型的混合做法見 [[topics/community-tech-discussions]]，可路由到 Ollama 的 Dragoman 見 [[topics/community-tech-tools]]
- 🔥🔥🔥（估） **社群轉載量化數字（Fable 5 Orchestrates, Cheap Models Execute）**（7/14）：編排者-執行者分工宣稱 46% 成本下達 96% 效能；社群分層路由思路首次有具體數字佐證。09-07 更正：原始官方連結未見，改列社群轉載，見 [[entities/fable-5]]
- 🔥（估） **只在需要頂尖判斷力任務用 Fable 5**（7/26）：上述社群轉載數字出現後的社群實踐案例——把「編排者-執行者」思路收斂為個人可執行的簡單守則：只有真正需要頂尖判斷力的任務交給 Fable 5，其餘交給便宜 subagent 執行以控制成本
- 🔥（估） **分層 Opus「大腦」＋Sonnet「工人」提案**（8/14，GitHub Issue #56913）：把模型分層從成本路由延伸到長時間自主運行——Opus 決策監督、Sonnet 執行、持久化狀態記進度；官方已於 2026-09-15 關閉，標為不做

**代表模式：**
- **Workweave Router**：嵌入 Claude Code / Codex / Cursor 的成本感知路由，依難度自動降階（裝哪個見 [[topics/community-tech-tools]]）
- **Multi-model Pipeline**：三模型明確分工 + 結構化交接，控制跨平台 token 成本
- **Dragoman**：~800 行 CLI，顯式規則路由至 Perplexity / Gemini / Ollama 並由 Claude 統整
- **分層模型策略**：Sonnet 主力 + Opus 諮詢，社群單一案例稱依任務複雜度節省約 60% 用量
- **Fable 5 Orchestrator-Executor（社群轉載）**：Fable 5 負責協調、便宜模型負責執行，社群流傳 46% 成本／96% 效能數字（原始官方連結未見）；在 Claude Code 裡可用 `opusplan` 或 `CLAUDE_CODE_SUBAGENT_MODEL` 做類似分工

**對現有設計的啟示：** 先看官方給了什麼：`opusplan` 讓規劃用 Opus、開始執行自動換 Sonnet，`CLAUDE_CODE_SUBAGENT_MODEL` 可替 subagent 指定預設模型；依難度自動選模型的路由，官方文件沒有（[官方文件](https://code.claude.com/docs/en/model-config)；官方與社群的差距見 [[topics/official-community-gap]]）。回頭檢查：你是不是所有任務都走最強模型；路由規則是自己寫的，還是交給一個看不到判斷邏輯的路由器。按難度降階可省 60% 以上只是社群單一案例，46%／96% 也只是社群轉載（見 [[entities/fable-5]]）。本地小模型分流只留在上方演進：生態只驗證了省錢、沒驗證省 context，官方做法頁已不再推薦（見 [[topics/coding-workflow-guide]]）。

**哪些任務可以降階：**

| 任務 | 適合模型 | 理由 |
|------|---------|------|
| 格式轉換、JSON 整理、標籤提取 | Haiku | 規則明確，不需要 reasoning |
| 一般 feature 開發、重構、已知類型 bug | Sonnet | 大部分日常工作的最佳 CP 值點 |
| 跨系統架構決策、複雜 bug 調查、不確定性高的問題 | Opus | 真正需要深度 reasoning 的任務 |
| 「幫我 review 這段 migration SQL 的安全性」| **Opus，不可降階** | 看起來簡單但降階後後果嚴重 |

**黑盒路由的隱患：** Workweave Router 自己決定「這個請求夠難嗎」——如果判斷邏輯不透明，某些關鍵任務可能被靜默降階，你不知道為什麼結果不可靠。顯式規則路由（自己定義哪類任務走哪個模型）更容易 debug，代價是維護成本。另一個風險不在路由器：你指定的模型本身不一定釘得住，見 [[topics/code-quality-decline]]。

---

### 趨勢五：對抗性設計　`方向已收斂`　最近一次動靜 2026-09-05

**演進：**
- 🔥（估） **零星出現**（4/26）：對抗性審查概念初現，尚未系統化
- 🔥🔥（估） **6 月系統化**（6/25）：對抗性審查（計畫前 + 程式碼後對照）、Read-Only Reviewer 同期出現，形成設計分層
- 🔥🔥（估） **Verity 自癒式 review gate**（6/27）：每次 agent 執行後自動修復不安全代碼並記憶學習；「reviewer 記憶讓下次起點更優」是對抗性設計的持久化延伸（HN Show HN）
- 🔥🔥（估） **Agent-plan-review-loop**（7/10）：對抗性設計從「程式碼完成後審查」延伸至「計畫階段逐步挑戰」——對抗式 reviewer 在實作前逐條質疑計畫假設，補足計畫前審查的具體實作案例
- 🔥🔥（估） **量化證據：Claude 審 Codex 通過率 71.6%→89.7%**（8/4，Reddit 週熱門）：這條線第一個量化數字，跨模型交叉審查從「機制上合理」進到有通過率可看；同一組數字見 7/22 的論文 [arXiv 2607.21656](https://arxiv.org/abs/2607.21656)（116 則 LiveCodeBench 解題，不是 PR review）
- 🔥🔥 **對抗式審查的「降階」變體（interns-review-plugin）**（9/5，HN 12）：與既有唯讀審查者、跨模型交叉審查不同角度——刻意把審查者意見包裝成「沒經驗實習生」等級，藉此降低使用者對審查意見的過度採信，屬對抗性設計延伸至「怎麼呈現審查結果」的社會工程變體

**代表模式：**
- **對抗性審查設計**：引入對立角色打破 LLM 樂觀偏差；計畫前審查讓審查者讀真實 codebase，程式碼後審查在草稿階段挑模糊假設
- **Read-Only Reviewer Agent**：reviewer 不持有編輯工具，用權限約束強制其只批評不動手，維持對立性可持續
- **多代理 PR Review**：平行子代理 + 多階段驗證，跨廠商模型交叉審查；71.6%→89.7% 與論文 arXiv 2607.21656 的解題測試是同一組數字，不是 PR review 實測
- **Agent-plan-review-loop**：計畫階段對抗式逐步挑戰，在動手實作前先攻破薄弱假設，降低方向錯誤後才發現的成本

**對現有設計的啟示：** 回頭檢查：你的 review agent 能不能編輯（能編輯就會傾向直接改而不是批評）；審查者和作者是不是同一個模型、同一個 session（同一個模型審自己剛做的決定，會傾向確認它）。下表三個層次，看你在哪一層；現在該怎麼做、跨模型數字的測法與限制，見 [[topics/community-large-codebase-workflow]]。

**對抗性設計三個層次：**

| 層次 | 做法 | 效果 |
|------|------|------|
| 最低限度 | 同一個 Claude，先寫再開新 session 審查 | 消除「剛剛做了這個決定」的即時偏差 |
| 中等 | 兩個 agent：writer 掛 Edit/Write，reviewer 只掛 Read | 物理上無法修改 → reviewer 被迫只能批評，不會「幫你改好它」 |
| 最強 | Claude 寫 → GPT 或 Gemini 審 | 不共享訓練偏差，reviewer 不會「順著」原始模型的思路走 |

---

### 趨勢六：多 Agent 可觀測性儀表板化　`方向已收斂`　最近一次動靜 2026-09-10

**演進：**
- 🔥（估） **live-log-viewer-next**（7/6）：讀取本機 JSONL transcript，呈現多個平行 agent 即時對話地圖，此線最早的獨立實作
- 🔥（估） **Topsoil**（7/13）：把 macOS 筆電瀏海變成監看 Claude Code / Codex 等編碼 agent 的即時終端機面板
- 🔥（估） **Fleet Deck**（7/14）：單一看板掌握機器上每個 Claude Code session 狀態（排隊中／執行中／待輸入／閒置）
- 🔥🔥 **Cockpit（現名 episko）**（8/2，HN 11，多家報導）：Rust 打造，將多個 agent／session／專案的執行狀態彙整於單一介面，取代開多視窗追蹤
- 🔥🔥🔥 **Wallfacer**（8/7，HN 35，多家報導）：Claude Code 專用終端機 session 管理工具
- 🔥🔥 **HUD**（8/7，HN 25，多家報導）：開源極簡終端 UI，同時支援 Claude Code／Codex／OpenCode，透過官方 CLI JSON event stream 運作，UserPromptSubmit hook 取狀態不額外耗 token
- 🔥🔥（估） **Clinch／Voidleap Code／DocStash／Csift 同日亮相**（8/19，Hacker News）：管理多 repo session（Clinch）、對話中途換模型的 IDE（Voidleap Code）、agent 產出直接發布成網頁（DocStash）、整理 JSONL session 檔（Csift），「怎麼管理與觀察 session」成了穩定賽道
- 🔥（估） **dsh-TUI／better-agent-terminal**（9/10）：介面元件化的延伸——dsh-TUI（中國社群「DSH」官方收錄的 Claude Code 風格 TUI 元件市集）、better-agent-terminal（多工作區終端聚合），從獨立看板再細分出「可複用介面元件」

**代表模式：**
- **JSONL Transcript 讀取型**（live-log-viewer-next）：解析本機 session 逐字稿檔案重建對話地圖，不需官方額外介面支援
- **官方 Event Stream 型**（HUD）：透過官方 CLI 既有的 JSON event stream + hook 取得狀態，不額外消耗 token，是目前技術上最乾淨的實作路徑
- **獨立看板/主控台型**（Fleet Deck、episko（原名 Cockpit）、Wallfacer、Topsoil）：以獨立 App／TUI 彙整多 session 狀態，各自在「一覽性」與「所在平台」（終端、瀏海面板、獨立視窗）上做不同取捨

**對現有設計的啟示：** 先看官方給了什麼：Agent view（研究預覽）每個 session 一列，標出在跑、在等你還是做完了，但看不到 agent 之間誰在等誰（見 [[topics/official-community-gap]]）。回頭檢查：你的並行 agent 數是不是已經超過眼睛盯得住的終端機視窗數——超過了，可觀測性就該是一層獨立基礎設施，不是事後加的附加功能。自己做這類工具，先看官方 CLI 有沒有事件流介面：讀官方 event stream（如 HUD）比自己解析 transcript 檔案穩，不容易隨版本更新失效。與趨勢二互補——隔離解決「不互相踩到」，這條線解決「知道每個 agent 現在在幹嘛」。

---

### 趨勢七：規格驅動開發（Spec-Driven Development）　`方向已收斂`　最近一次動靜 2026-09-12

**演進：**
- 🔥（估） **opsx spec-driven-development-toolkit**（6/19）：CLI 工具強制要求先寫規格文件才能執行 AI 代碼生成，早期單一嘗試，已被 HN flagged，社群接受度尚待觀察
- 🔥 **ANMA 架構邊界合約**（6/22，HN 3）：YAML 合約定義架構邊界 + Hook 強制驗證，這條線第一個量化數據——有 ANMA 時 0/20 違規，無 ANMA 時 13/19 測試案例違反架構規則
- 🔥（估） **ISO/IEC/IEEE 29148 SRS 格式引入**（6/22，Reddit r/ClaudeAI）：與 ANMA 同日獨立出現的第二種規格化路徑，以工業標準需求規格格式（The system shall...）作為 Interview 收集需求後的書面化框架
- 🔥🔥（估） **ospec／smart-ralph 批次亮相**（8/11）：時隔近兩個月的第三、四個獨立實作——ospec 是「規劃—執行—驗證」可驗證目標迴圈，smart-ralph 把 Ralph Wiggum loop 接上結構化規格流程；兩者星數 8/13 查過非刷星
- 🔥🔥（估） **spec-kit**（9/12）：GitHub 官方帳號釋出規格驅動入門工具包，固定走 spec → plan → tasks → implement，中間產物（規格、計畫）可審查；一週新增兩千多星，尚無使用心得

**代表模式：**
- **ANMA YAML 合約**：架構邊界寫成合約 + Hook 強制驗證，讓便宜模型也能守規（0/20 vs 13/19 實測）
- **ospec 可驗證目標迴圈**：規劃—執行—驗證三階段，相容 Claude Code、Codex、Gemini、OpenCode
- **smart-ralph**：Ralph Wiggum loop + 結構化規格流程，主打規格驅動與智慧壓縮
- **spec-kit**：GitHub 官方帳號的入門工具包，spec → plan → tasks → implement 四段固定流程

**對現有設計的啟示：** 回頭檢查：你的工作流是不是「直接 prompt、邊做邊改」。先寫規格再讓 agent 動手，是社群 6 月到 9 月反覆獨立走到的做法，能把 ANMA 實測的「AI 為求速度繞過架構約束」問題前移到動手前攔截。但有效的證據仍集中在 ANMA 一次實測（0/20 vs 13/19）；ospec、smart-ralph、spec-kit 都還沒有第一手使用心得或獨立複現。

---

### 趨勢八：行動裝置遠端控制　`方向已收斂`　最近一次動靜 2026-09-10

**演進：**
- 🔥（估） **ccgram**（6/28）：Telegram bot 遠端控制本機 Claude Code session，早期單一嘗試
- 🔥（估） **Android Remote Control MCP**（7/8 前後）：MCP-based 方案，讓 Android 裝置可操作本機 Claude Code
- 🔥🔥🔥 **Shellular**（7/8，HN 32）：專屬 web-app，從手機遠端操作本機 Claude Code / Codex session
- 🔥（估） **Relay**（8/19，Hacker News）：讓家用主機上已裝的 Claude Code／Codex／OpenCode 可從任何裝置遠端操作，這條線第 4 個獨立實作
- 🔥（估） **Orchestrator**（9/10，Show HN）：這條線第 5 個獨立實作——手機遠端生成、下指令、終止並管理多個 Claude Code 實例，關閉 App 後任務仍在背景執行

**代表模式：**
- **行動裝置作為控制介面**（ccgram、Shellular、Orchestrator 等）：手機／任意裝置透過 bot、MCP 或專屬 web-app，遠端下達指令或監看本機 Claude Code session 狀態

**對現有設計的啟示：** 先看官方給了什麼：Claude Desktop 可以遠端控制 Claude Code session，官方已確認可用（2026-08-17 關閉對應功能請求），怎麼開見 [[entities/claude-code]]——先試官方。回頭檢查：你的工作流是不是綁死在單一終端機前；「本機常駐、行動裝置遙控」已是社群反覆走過的形態。社群五個實作走 bot、MCP、web-app 三種路徑，本頁沒有它們與官方的逐項比較。與趨勢六互補——趨勢六解決「怎麼看」，這條線解決「不在電腦前時怎麼看、怎麼下指令」。

---

### 趨勢九：跨 Session 記憶層／知識庫　`方向已收斂`　最近一次動靜 2026-09-18

**演進：**
- 🔥（估） **跨環境 Agent 記憶協定（ltm）**（5/12）：Core Memory Packet JSON 協定，主張跨編輯器／跨機器／跨模型的供應商中立記憶格式，早期單一嘗試
- 🔥（估） **OKF 物件鍵格式**（6/28）：第二個獨立標準化嘗試，聚焦跨 session agent 記憶的團隊共用格式，與 ltm 同屬「格式標準化」路線但各走各的協定
- 🔥🔥🔥 **CodeAlmanac**（7/22，YC S26，Show HN score 54）：從「記格式」轉向「記文件」——隨對話自動更新 codebase wiki，取代手動維護的 MANUAL.md／DESIGN.md；30 天內無後續採用回饋，2026-08-29 已自 [[topics/community-tech-tools]] 移除追蹤
- 🔥🔥🔥 **OzBrain**（8/21，HN 69，多家報導）：從「單一使用者跨 session」延伸到「team 共享」——主張 agent 與團隊共用知識庫，取代傳統筆記/任務管理工具
- 🔥（估） **手動 Obsidian vault 取代官方自動記憶**（8/24，Reddit）：與前三者「補充記憶層」方向相反的第一個「取代」案例——使用者主張自己策展的 LLM Wiki 比官方自動記憶更可控、更可信賴
- 🔥（估） **mindmuxai/brain.md**（8/25，504★）：第三種格式路線——零依賴、檔案式 CLI，鎖定決策／需求／限制三類專案層級資訊，補上「輕量、無外部服務依賴」這個此前未見的實作取向
- 🔥（估） **否決記錄需可驗證、防竄改**（8/31，dev.to）：把記憶範疇從「記住怎麼做」延伸到「記住這條路已被否決」，並要求紀錄本身防竄改；與 8/7「已否決方案的隱形重工成本」是同一個問題的第二則訊號
- 🔥（估） **gentle-ai／cpr-compress-preserve-resume**（9/6）：格式標準化再添兩例——gentle-ai（6,304★）打包記憶／規格驅動／skill 為跨 4 種 agent CLI 的單一設定層；cpr（508★）走「壓縮—保存—還原」三段式跨 session 記憶；皆僅星數佐證
- 🔥🔥🔥 **Skillsync**（9/17，Launch HN 59）：YC W26 新創把整段 session（訊息、推理、工具呼叫）在不同 coding agent 之間搬遷延續，訴求不被單一供應商鎖住；機制細節未見完整技術文件
- 🔥🔥🔥（估） **hister**（9/18）：把瀏覽紀錄、書籤、本機檔案建成離線個人搜尋索引，另附 MCP 端點給 agent 查；作者在 Hacker News 現身回答提問，記憶對象從專案延伸到個人知識

**代表模式：**
- **格式標準化**（ltm、OKF）：定義可攜的記憶資料格式，目標是跨工具/跨模型可讀，但兩個協定互不相容，尚未收斂到單一標準
- **codebase 文件自動化**（CodeAlmanac）：記憶對象從「agent 決策」擴大到「專案文件本身」，但 30 天無後續已顯示此路線目前僅一例、缺乏採用驗證
- **團隊共享知識庫**（OzBrain）：記憶範疇從單一使用者延伸到團隊，主張取代而非補充現有筆記工具
- **零依賴檔案式**（mindmuxai/brain.md）：不依賴外部服務或資料庫，直接以檔案存決策/需求/限制

**這條路線怎麼設計：** Karpathy 式 LLM wiki 的三層模式、外面幾種公開實作的並排對照見 [[topics/llm-wiki-pattern]]。

**對現有設計的啟示：** 先看官方給了什麼：auto memory 讓 Claude Code 跨 session 自己記筆記，每個 session 載入前 200 行或 25KB。回頭檢查：你跨 session 要保留的架構決策，是交給內建記憶，還是外化成你自己讀得到的檔案（Markdown／JSON）。社群 5 月起用協定、文件自動化、團隊共享、手動策展、零依賴檔案、跨 agent 搬遷幾種路線在解同一件事，至今沒有一個經第二方採用驗證或有量化數據，選型前先問「這個格式會不會只有我一個人在用」。官方與社群做法現在怎麼接，見 [[topics/community-large-codebase-workflow]]。

---

## 還在醞釀的方向

目前沒有。

---

## 目前結論

- **你的選項**：拿自己的設計對各條「對現有設計的啟示」逐條檢查；撞到的是大 repo 的四面牆，照 [[topics/community-large-codebase-workflow]] 的現在答案做；模型路由、手機遠端、跨 session 記憶三條先開官方零件，再看社群工具。
- **接下來看什麼**：官方把「Opus 大腦＋Sonnet 工人」提案標為不做（9/15）之後，模型路由還有沒有新做法；spec-kit 之後規格驅動有沒有第一手使用心得；官方遠端控制可用之後，社群的手機遙控工具還有沒有新的。

---

## 怎樣算「方向已收斂」

三個以上互不相干的作者、前後隔兩週以上反覆走到同一個做法，且至少一個做法帶量化數據或講得出完整機制，才標「方向已收斂」；還沒到的列在「還在醞釀的方向」。

---

## 相關實體

- [[topics/community-tech-patterns]]（每種做法的原始證據、成熟度與最後動態；本頁的素材來源）
- [[topics/community-tech-patterns-archive]]（4–6 月歷史流水帳，演進起點考據）
- [[topics/community-large-codebase-workflow]]（大 repo 四面牆現在怎麼做、官方零件在哪）
- [[topics/community-tech-discussions]]（思想辯論，趨勢背後的社群共識）
- [[topics/coding-workflow-guide]]（官方流程；hook 強制層、讀取上限、本地模型分流的官方立場）
- [[topics/official-community-gap]]（同一個痛點官方補了沒）
- [[topics/community-tech-tools]]（卡在某個症狀，社群首選裝哪個）
- [[entities/claude-code]]（多數趨勢圍繞的官方產品）
- [[entities/boris-cherny]]（Loops 哲學影響多條趨勢的設計取向）

%% 週更撈料水位：週更已收至 2026-09-19（規則：.claude/reporter-rules/community/weekly.md「community-pattern-trends 趨勢頁週更」）。2026-09-23 健檢：趨勢一曾於 07-02→08-15 44 天無新節點，08-25、09-06 又有新進展；agent-channels 在 patterns 無節點（只在概覽表列名，最早見 06-27 日報），不補進趨勢二；趨勢四 30 天檢查：patterns「模型使用策略」09-06 的 MaskShift（工具呼叫相容層）、magnitude（本地推論後端）不推進路由方向，故標淡出。 %%
````

> 逐行去向見 `trends-2026-09-23-proposal-map.md`。重點：
> - 標題狀態標統一為 `方向已收斂`，熱度詞（▬ 穩定延燒／📈 加溫中／↗ 新升格…六種）換成「最近一次動靜 YYYY-MM-DD」；趨勢四照 B-1 第 4 步跑出「↘ 淡出」。
> - 🔥：14 個帶 HN 分數的節點照 L47 圖例重打（Adrafinil 124、Merge Queue 42、machine0 83、Workweave 216 取 verified §二 即時值；其餘 10 個用頁面原記分數），判定日 2026-09-23；57 個無 HN 分數的節點標「（估）」。Fable 5 由 🔥🔥🔥🔥 降為 🔥🔥🔥（估）：單平台轉載（健檢卡 7(1)）。
> - 四段與 LCW 重疊的啟示（趨勢二／三／五／九）只留回頭檢查，可執行零件一句指 LCW；趨勢二「失敗場景／怎麼修」、趨勢三反模式表與直覺句、趨勢五「為什麼自我審查失效」與 Verity 延伸併入各自啟示或演進。
> - guide L287 撤回的三條：讀取上限（L130）、已否決方案索引（L133）、本地小模型分流（L166）留在演進，啟示段各一句分界（趨勢三 1 句、趨勢四 1 句）。

## A-2 patterns 入口句（`wiki/topics/community-tech-patterns.md` L44，只換第一句，其餘不動）

原：`想知道哪個方向在加溫、熱度往哪走，見 [[topics/community-pattern-trends]]（那頁有每條趨勢的時間軸）。`

```markdown
本頁是每一種做法的原始證據，模式概覽表標每一類的成熟度與最後動態；已經收斂成方向的做法怎麼一步步走到今天、你現有設計可以回頭檢查什麼，見 [[topics/community-pattern-trends]]。
```

## A-3 discussions 入口句（`wiki/topics/community-tech-discussions.md` L43，只換中段）

原：`哪個方向在加溫、熱度往哪走，見 [[topics/community-pattern-trends]]；`

```markdown
社群做法收斂成哪幾個方向、各自怎麼走到今天，見 [[topics/community-pattern-trends]]；
```

## A-4 archive 兩處加註（`wiki/topics/community-tech-patterns-archive.md`，原文一字不刪，只在行尾接括號）

L279 行尾接：

```markdown
（2026-09-23 註：官方語意是 Stop hook 要 exit 2 才會阻止停下，其他非零不擋，見 [[topics/community-pattern-trends]] 趨勢一）
```

L526 行尾（「…影響攔截、允許、修改等場景的設計決策」之後）接：

```markdown
（2026-09-23 註：官方文件的 exit code 只有 exit 2 會擋；Block／Allow 這類是 JSON 回傳的決策欄位 `permissionDecision`，不是 exit code，見 [[topics/community-pattern-trends]] 趨勢一）
```

## A-5 LCW 互指句（`wiki/topics/community-large-codebase-workflow.md` L187 整行換）

```markdown
- [[topics/community-pattern-trends]]（社群做法收斂成的方向、各自怎麼走到今天）
```

---

# B. 進規則檔

## B-1 `.claude/reporter-rules/community/weekly.md`「## community-pattern-trends 趨勢頁週更」（L135–L157 整段換掉；L133 標題、L158 空行、L159 `---` 不動）

`review-registry.json:250–258` 要求本檔含「每日 ingest 不」——那句在 L3，本段不碰。對照表第一列不寫出管理規則檔那一類的全名：`check_rules.py:102–157` 把規則檔裡任何沒有路徑前綴的那個檔名（連反引號內）判為裸露引用，實測寫出即紅（`review-registry.json:3–13`）。

````markdown
每次 `/wiki-lint` 時更新 `wiki/topics/community-pattern-trends.md`（週更，非每日）。本頁回答「社群做法往哪幾個方向收斂、每個方向怎麼走到今天、你現有設計可以回頭檢查什麼」；每種做法的證據與採用成熟度（✅⚡⏳）住 `community-tech-patterns`，本頁不另判採用量、不寫 ✅⚡⏳。

**方向成立門檻（同時滿足，才列入「已收斂的方向」）：**
- ≥ 3 個獨立來源（不同社群帳號、不同媒體、不同工具）
- 最早與最晚的節點相隔 ≥ 14 天（反覆出現，不是單日爆紅）
- 至少 1 個節點帶量化數據，或講得出完整、可照做的機制
頁面只在「怎樣算方向已收斂」節留一句讀者語言；正文與節點不複述本條（不寫「已符合認定標準」「A 層／B 層」「子軸線」）。未達門檻但已有 ≥ 2 個來源的方向列「還在醞釀的方向」，一方向一條：名稱＋已有哪些來源＋還缺哪一條；沒有就寫「目前沒有。」

**趨勢 ↔ patterns 模式概覽類別（撈料與淡出檢查都用這張；新增趨勢或 patterns 類別改名時同步）：**

| 趨勢 | patterns 類別（逐字，比對時去掉反引號） |
|---|---|
| 一 強制層取代建議層 | `Hooks 與自動化`；另含管理規則檔那一類（逐字名見 patterns 模式概覽表；本檔寫出該檔名會被 `check_rules.py` 判為裸露引用） |
| 二 Multi-agent 隔離工程化 | `Multi-agent 架構`、`Agent 規模化` |
| 三 Context 主權爭奪 | `Context 管理`、`Token / 成本優化` |
| 四 模型路由自動化 | `模型使用策略` |
| 五 對抗性設計 | `多代理 PR Review` |
| 六 多 Agent 可觀測性 | `Agent 規模化`、`介面元件複用` |
| 七 規格驅動開發 | `規格驅動開發`、`架構邊界合約` |
| 八 行動裝置遠端控制 | `行動裝置遠端控制` |
| 九 跨 Session 記憶層 | `記憶與知識管理` |

**更新步驟：**
1. **撈料**：`Grep "\*\*與既有模式的關係：\*\*" wiki/topics/community-tech-patterns.md`，挑逐字含上表類別名、且節點日期不早於本頁 `%%`「週更已收至 YYYY-MM-DD」前 3 天者為候選（日報晚 26–30 小時，節點會晚到；名字已在本頁的跳過）。推進該方向的（新取向、新證據、第 N 個獨立實作）才寫成節點；只是同類再多一個工具的不寫。
2. **節點格式**：`- 🔥…（估） **名稱**（M/D，來源平台）：一句推進了什麼`。有 HN 分數的寫 `HN nn`、照頁面摘要的 🔥 圖例分級、不加「（估）」；沒有的加「（估）」。每條 ≤ 200 字元；不寫「本線」「節點」「本週」「GitHub Search」這類維運字眼。
3. **標題**：``### 趨勢N：名稱　`方向已收斂`　最近一次動靜 YYYY-MM-DD``，日期＝該條演進最後一個節點的日期，每次週更重算。
4. **淡出檢查（每條每週都跑）**：「最近一次動靜」距今逾 30 天 → 先看上表對應類別在 patterns 模式概覽表的「最後動態」：30 天內有 → 打開那幾則節點，推進本方向的照第 2 步補進演進（屬漏收），不推進的在本頁 `%%` 記一句為何不收；補完仍逾 30 天 → 標題日期前加「↘ 淡出・」。重新有節點進來即拿掉。淡出只是標記，不移出頁面；整條移除屬使用者裁決。
5. **啟示**：每條 `**對現有設計的啟示：**` 只寫「回頭檢查什麼」。官方已有對應零件的，第一句先寫官方給了什麼——只轉述 `coding-workflow-guide`／`official-community-gap`／`entities/claude-code`／`community-large-codebase-workflow` 已寫的，連頁不連錨；庫內沒有時才直連官方文件並開轉知請功能記者收，收進後改回指頁。與 `community-large-codebase-workflow` 四線重疊的（趨勢二／三／五／九），可執行做法與官方零件以那頁為家，本頁一句指過去。官方做法頁已撤回、或與官方文件相反的做法，只留在演進，不進啟示。
6. **啟示段的表**：只在回頭檢查需要跨列比時用（`page-templates.md`「表格只在有得比時才用」）；靜態，不隨節點改；表內做法被官方文件推翻或被官方做法頁撤回時當週改。
7. **上限**：演進條列累積、不覆寫；單條超過 12 個節點時在回報標 `⚠️ 趨勢N 演進 >12`，怎麼精簡屬使用者裁決。
8. **callout 與目前結論**：callout ≤ 3 條，寫哪條方向有新做法、哪條淡出、官方對應有沒有變，不得含「節點」「本輪」「本週」；`## 目前結論` 只留「你的選項」「接下來看什麼」兩條，每次週更重寫。
9. 更新 `**最後更新：**`、`**最後新聞更新：**`，並把 `%%`「週更已收至」改成本次看過的最新節點日期。

**不更新情況：** 撈料沒有推進任何方向、標題日期與淡出狀態也不必改 → 正文不動（不改最後更新日期），只把 `%%` 水位往前推。
````

> 舊條文三處與頁面對不上、一處從未執行（健檢卡第 5 節）：門檻「首次出現距今 ≥14 天」→ 改「最早與最晚節點相隔 ≥14 天」（頁面 L325 的嚴格版，才擋得住單日爆紅）；新節點 `#### YYYY-MM-DD`＋三級 🔥 → 改成頁面實際的條列＋四級；熱度詞「📈 → stable／plateau」→ 刪，改「最近一次動靜」；「沉寂 30 天 → ↘ 淡出」→ 第 4 步先對 patterns 同類「最後動態」核一次（健檢卡 5：照原條文硬跑會把 patterns 判為活躍的趨勢七判死）。撈料由「近 14 天 news」改為 patterns 關係行＋`%%` 水位（09-19 漏收四則的根因：原步驟讀 news 而非 patterns 節點，且無水位，推論——log 無該輪撈料紀錄可證）。

---

# C. 轉知（3 筆，實作者照抄執行；類別用中文）

C-1（功能：guide 缺 hook exit code 語意）

```
python scripts/pending_handoffs.py open --from 社群 --to 功能 --page topics/coding-workflow-guide --note "L210『強制層是 hooks 或 permissions……回 deny』沒寫 exit code 語意，全庫無家。官方 hooks 文件（2026-09-23 查）：『Exit 2 means a blocking error… exit 2 blocks whether or not you print JSON』；『Without valid JSON on stdout, Claude Code treats exit code 1 as a non-blocking error and proceeds with the action』；Stop hook 的 exit 2『Prevents Claude from stopping, continues the conversation』。community-pattern-trends 趨勢一原寫『exit 1 = 硬攔截』（相反），已改 exit 2 並暫以官方文件直連；archive L279／L526 已加註。若收進 L210，趨勢頁改為只指 guide。"
```

C-2（功能：OCG L59 缺 `CLAUDE_CODE_SUBAGENT_MODEL`、與 L187 互斥）

```
python scripts/pending_handoffs.py open --from 社群 --to 功能 --page topics/official-community-gap --note "①L59『想自己決定哪段用哪個模型』列只寫 opusplan，缺 CLAUDE_CODE_SUBAGENT_MODEL——官方 model-config 文件（2026-09-23 查）：給 subagent／teammate／workflow agent 預設模型；除此之外 no automatic difficulty-based model routing。②同頁 L187『社群工具……填補的是後者，官方目前無對應方向』與 L59 opusplan『開始執行自動換 Sonnet』被第 17 波冷讀者讀成互斥（Q2）。community-pattern-trends 趨勢四暫以官方文件直連 CLAUDE_CODE_SUBAGENT_MODEL；若收進 L59，趨勢頁改為只指本頁。"
```

C-3（模型：官方文件的預設模型字樣）

```
python scripts/pending_handoffs.py open --from 社群 --to 模型 --page entities/opus-5 --note "第 17 波主編查證（2026-09-23）時，官方 model-config 文件寫 Pro／Max／Team／Enterprise／API 的預設模型為『Opus 5.5』；請對官方一手核對，確認庫內預設模型敘述要不要更新。community-pattern-trends 本波未引用此句。"
```

**不開轉知、只記 `wiki/log.md`**：🔥 重打 14 筆與 57 筆標估；四則漏收補進（agent-channels 不補的理由）；趨勢四跑淡出檢查的結果（MaskShift、magnitude 不推進路由方向）；guide L287 三條留演進、出啟示；#56913 not_planned；L190 $100／$18 刪（verified §二：無 token 假設）。guide L287 前兩條的前提已由第 16 波 H-c63724 轉知在案，本波不重開。

**同維護者、本波不改、下次該頁策展處理**（只記 log）：`community-tech-tools` L63 把 Workweave 歸在「不想被單一供應商綁死」、決策表沒有「想依難度降階省錢」症狀（冷讀者 CR:37）；`community-tech-patterns` L1653「現在收斂到哪」與本頁同題兩家（併頁屬使用者裁決）；patterns L1655「CLAUDE.md 管理已定案」vs discussions L54「還在吵」（CR:115）；patterns 09-15 pizza-bot、09-16 TokenEater（歸「Agent 規模化」）是否屬趨勢六，下次週更照 B-1 第 1 步判；09-20～09-22 的 Chief of Staff、aoci-code、Foremerge、pstack-claude 是下次週更的正常料，不是漏收。

**主編自理**：
- `wiki/index.md:103` 本頁那列（「7 條成形趨勢的熱度曲線」已過期）換成：`🗓️ 週更 社群做法收斂成的九個方向：各自怎麼走到今天、你現有設計可以回頭檢查什麼；每種做法的原始證據與成熟度見 [[topics/community-tech-patterns]]`（91 字元，≤120）。
- `wiki/overview.md` L118（趨勢七 🔥🔥🔥🔥「已站穩」）、L119（「第三波…本輪」）過期，下次 overview 改寫時處理。
- 趨勢四 L168 Fable 5 節點日期 7/14 vs `entities/fable-5` L112 來源貼文 07-08（健檢卡第 6 節「需主編定」），本波不動。

---

# 實作單（最終版）

**實作者只看這張。** 行號＝對象頁與規則檔的**原始**行號。所有逐字稿都在本檔上方 A／B／C 區；scratchpad 產物 `new_trends.md` 與 A-1 逐字相同（round-trip 已驗）。

0. **改規則檔** `.claude/reporter-rules/community/weekly.md`：L135–L157 整段換成 B-1（L133 標題、L158 空行、L159 `---` 不動）。驗：`grep -c "週更已收至" .claude/reporter-rules/community/weekly.md` ＝ **4**（原 2，LCW 節兩處；B-1 第 1、9 步各一）；`grep -c "#### YYYY-MM-DD" …weekly.md` ＝ 0；`grep -c "plateau" …weekly.md` ＝ 0；`grep -c "每日 ingest 不" …weekly.md` ≥ 1；`grep -c "CLAUDE\.md" …weekly.md` 與改前相同；`python scripts/check_rules.py` 綠。
1. **對象頁** `wiki/topics/community-pattern-trends.md`：L27–L338 整段換成 A-1 fence 內文字，`<實作當天>` 三處填當日日期（L33、L34、callout 首行）。L1–L26 不手改。
2. **驗對象頁**（L27 以下、`%%` 行除外）：`wc -l` ＝ 322；`grep -c "^### 趨勢"` ＝ 9 且每行都含「`方向已收斂`」與「最近一次動靜 2026-」；`grep -c "（估）"` ＝ **57**；`grep -c "exit 1 = 硬攔截"` ＝ 0；`grep -c "exit 2"` ≥ 4；grep「本週」「本輪」「本次」「本線」「GitHub Search」「A 層」「47 👍」「\$100」「105 天」「121 天」皆 ＝ 0；「節點」只出現在 `%%` 行。
3. **patterns** L44：換 A-2（只換第一句）。
4. **discussions** L43：換 A-3（只換中段）。
5. **archive** L279、L526：行尾各接 A-4 一段（原文不刪字）。
6. **LCW** L187：整行換 A-5。驗：`grep -c "community-pattern-trends" wiki/topics/community-large-codebase-workflow.md` 仍 ＝ 2。
7. **轉知 3 筆**：照抄 C-1～C-3。驗：`python scripts/pending_handoffs.py list --to 功能` 比改前多 2 筆、`--to 模型` 多 1 筆。
8. **`wiki/log.md` 一筆本波條目**：列 C 區「不開轉知、只記 log」與「同維護者、本波不改」兩段全部內容。
9. **主編自理**：`wiki/index.md:103` 換成 C 區那句。
10. **跑閘（依序，每支 exit 0，最後一行原樣抄進回報）**：`python scripts/check_cell_limits.py --page topics/community-pattern-trends` → `python scripts/check_reader_language.py --page topics/community-pattern-trends` → `python scripts/check_cell_limits.py --page topics/community-tech` → `python scripts/check_reader_language.py --page topics/community-` → `python scripts/check_pending_markers.py`（119 筆、基線 106）→ `python scripts/gen_wiki_frontmatter.py`（之後驗 frontmatter L8 `update_freq` 不含「節點」「趨勢層」）→ `python scripts/check_hierarchy.py` → `python scripts/check_rules.py` → `python scripts/build_web.py` → `python scripts/run_tests.py`。

設計者對「A-1＋A-2～A-5 套進 wiki 副本」跑前兩支與懸置閘等價函式的預期（本頁 `--page` 輸出）：
```
WARN: 存量基線內 0 筆／0 頁（前 5 頁：無）
OK: 字元上限機械閘 — 無新增超限
WARN: 存量基線內 0 筆／0 頁（前 5 頁：無）
OK: 讀者語言閘 — 無新增命中
狀態：✅ 懸置標記語法檢查通過
```
