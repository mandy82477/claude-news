# 第 21 波逐字稿：entities/claude-code 拆成母頁＋三子頁（2026-11-01）

> 頁面逐字以 `scratchpad/w21/design/out/wiki/entities/` 為準（`split_cc.py` 輸出；新寫文字的單一來源是 `newtext.py`，本稿「進頁面」由 `make_draft.py` 從它直接產生，不手抄）。frontmatter 由 `gen_wiki_frontmatter.py` 生成，實作者不手填。純搬移的段落只寫原行號。
> 行號：「原 Lnnn」指 `wiki/entities/claude-code.md` 2026-11-01 原檔（1,231 行）。裁決 (3) 砍現況 L48–109 **待使用者確認**；若使用者不准，`split_cc.py` 把 `mark(48, 109, …)` 改回 `take(48, 109, "母")`、刪 `M_VERSION` 即可，母頁約 235 行。

## 行數（正文＝`check_page_thickness.body_lines` 口徑，臨時副本跑過 gen 後實量）

| 頁 | 總行 | 正文 |
|---|---|---|
| `entities/claude-code` | 202 | 173 |
| `entities/claude-code-known-issues` | 461 | 432 |
| `entities/claude-code-releases` | 287 | 260 |
| `entities/claude-code-features` | 266 | 239 |
| `entities/claude-code-archive` | 362 | 337 |

## 自查（交件前）

- **讀者語言**：`newtext.py` 187 段新寫字串逐一對 `check_reader_language.py` TERMS（L51 起 37 組）與 `pending_markers.LEGACY_RE`（去掉懸置標記本體後）比對：0 命中。臨時副本整頁掃描新增 2 筆，皆為搬家原文的產品詞「對話封存」（K 📂 組 10-24 複查句、R 歷史 09-01 列），不是新寫字。
- **儲存格 ≤120／條列 ≤200**：`cmp_hits.py` 以 `check_cell_limits.scan` 掃五頁改前改後，改後 232 筆超限全在改前 243 筆之內（內容指紋），新寫文字 0 筆。第一版 4 筆超限（v2.1.316 列 159 字、v2.1.309 列 131、2.1.313 🔎 條 201、L910 指路 201）已改短；v2.1.316 列因此放不下 `CLAUDE_CODE_SUBAGENT_EFFORT`。
- **錨點**：臨時副本 `build_web.py` 錨點 WARN 0（需同批改 cowork L52／L78、claude-tag L45；不改則 2 筆 WARN＋ERROR）。

# 進頁面

## A. 母頁 `wiki/entities/claude-code.md`

節序：標頭 → callout → 拆頁評估 `%%` → `## 往下鑽` → `## 現在還沒修好的`（自原 L209–226 上移）→ `## 現況` → `### 未歸類` → `## 熱度與試用價值` → `## 版本更新`（殼）→ `## hooks：…`（殼）→ `## 相關議題` → `## 參考來源`。

**callout（取代原 L38–40）**

````markdown
> **最新動態**（2026-10-31）
> - **v2.1.316**：新增 `CLAUDE_CODE_DISABLE_ULTRATHINK`；⚠️ Opus 4.8 fast mode 11-30 移除，用的人要改 Opus 5.5（見 [[entities/claude-code-releases]]）。
> - **遊戲重製限制**：Anthropic 證實以更新引導 Claude Code 不重現他人特定遊戲，使用者回報無害的逆向工程也被擋；Claude in Chrome 自 9/18 起在 reddit.com 全工具被安全限制擋下（#95326）（見 [[entities/claude-code-known-issues]]）。
````

**拆頁評估（取代原 L44）**

````markdown
%% 拆頁評估 2026-11-01：已拆（第 21 波）。母頁留現況、結論表與路由；已知問題、版本、功能用法住 claude-code-known-issues／-releases／-features。落選：兩子頁（功能留母頁，母頁約 333 行超過 300）、功能併進 coding-workflow-guide（它答官方建議、已 688 行）。`## 版本更新`、`## hooks：…` 是同名指路殼：前者有讀者版日報 4 筆錨點、feature-radar 3 筆；後者等 coding-workflow-guide、community-guardrails 改指 features 後可刪。 %%
````

**新節：往下鑽（插在 callout 後）**

````markdown
## 往下鑽

| 你想知道 | 去哪頁 | 最後動態 |
|---|---|---|
| 某個 bug 修了沒、誰會遇到、有沒有繞法（九組逐條） | [[entities/claude-code-known-issues]] | 2026-10-31 |
| 現在到哪一版、stable 還是 latest、哪一版加了什麼 | [[entities/claude-code-releases]] | 2026-10-31 |
| hook 能不能當防線、subagent 派哪種、桌面版能做什麼 | [[entities/claude-code-features]] | 2026-10-30 |
| Claude Mods 是什麼、權限怎麼管 | [[entities/claude-mods]] | 2026-10-20 |
````

**現況開頭「版本」（取代原 L48–109，**砍整節，待使用者確認**）**

````markdown
**版本：**

- 最新 **v2.1.316**（2026-10-31）；npm `stable`＝2.1.309、`latest`＝2.1.316（查證 2026-11-01）。
- **該不該升**：沒用 Opus 4.8 fast mode，留在 stable 就夠；要 Monitor tool 或寫入邊界設定才需要 latest。逐版與通道見 [[entities/claude-code-releases]]。
````

**原 L113**

````markdown
- 桌面版文件異動依主題歸群在 [[entities/claude-code-features#桌面版功能地圖]]，逐條時序在同頁。
````

**原 L186**

````markdown
其餘六則傳聞已於 2026-09-06 查證，結果見 [[entities/claude-code-releases#歷史記錄]]（五則結案、一則改列「已下架，原因未載」）。
````

**原 L188**

````markdown
近期新增已知問題與互動數更新見 [[entities/claude-code-known-issues]] 各組。
````

**原 L190 一處替換（舊→新）**

````markdown
技術細節見下方「核心功能」
→
技術細節見 [[entities/claude-code-features#核心功能]]
````

**新節：未歸類（現況末）**

````markdown
### 未歸類

%% 判不出該歸哪個子頁的條目先寫這裡，週更時分派（.claude/reporter-rules/features/pages.md 母頁路由表） %%
目前沒有。
````

**熱度節下新一行（其後接原 L905 原文）**

````markdown
**反向對照**（替代方案宣稱比 Claude Code 好，證據等級寫在條內）：
````

**原 L211 尾句替換**

````markdown
上限 8 列；完整清單見下方「已知問題」分組。
→
上限 8 列；完整清單見 [[entities/claude-code-known-issues]]。
````

**原 L217 第 4 格替換（查證 #6）**

````markdown
長工作分段、定期重開 session（98 則留言，可重現）
→
長工作分段、定期重開 session（98 則留言，可重現；07-19 社群回報 2.1.181／2.1.214 起安裝程式記憶體下降）
````

**原 L226**

````markdown
**接下來看什麼**：這幾條翻 ✅ 的那一天會寫在 [[entities/claude-code-known-issues]] 對應分組；升版判斷見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]；官方建議的做法見 [[topics/coding-workflow-guide]]。
````

**同名殼：版本更新（取代原 L693 的 h2）**

````markdown
## 版本更新

逐版明細、stable／latest 通道與歷史記錄見 [[entities/claude-code-releases]]；升版前要知道的破壞性變更見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。
````

**同名殼：hooks**

````markdown
## hooks：事件、失效模式與能不能當防線

hook 一觸發就是硬擋（先於 allow 規則），但比對是盡力而為，也有不觸發的回報；要保證一定擋，用 deny 規則或沙箱。事件表、失效模式與官方原句見 [[entities/claude-code-features#hooks：事件、失效模式與能不能當防線]]。
````

**參考來源（取代原 L1100–1111）**

````markdown
## 參考來源（最近 10 則）

- [[news/2026-10-31]]
- [[news/2026-10-30]]
- [[news/2026-10-29]]
- [[news/2026-10-28]]
- [[news/2026-10-27]]
- [[news/2026-10-26]]
- [[news/2026-10-25]]
- [[news/2026-10-24]]
- [[news/2026-10-23]]
- [[news/2026-10-22]]
````

純搬移：原 L28–37、L41–43、L110–112、L121、L133–136、L139、L141、L147–150、L152–154、L155–178、L179–185、L187、L189、L191–195、L196–205、L206–210、L212–216、L218–225、L1086–1099；另搬入原 L274（🛡️ 組 Compliance API 條，接在 L178 後）、L905（反向對照）、L911–912（年齡政策，接在 L154 後）。

## B. 子頁 K `wiki/entities/claude-code-known-issues.md`

**標頭**

````markdown
# Claude Code 已知問題：哪裡壞、修了沒、怎麼繞

某個 bug 修了沒、誰會遇到、有沒有繞法：Claude Code 自身故障的逐條清單，依主題分九組。

**類型：** product
**狀態：** active
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**首次出現：** 2025（正式推出）
**最後更新：** 2026-11-01
**最後新聞更新：** 2026-10-31
%% 2026-11-01 第 21 波自 [[entities/claude-code]] 拆出：九組原文照搬；🛡️ 組與安全子頁重疊的 17 條只留修補狀態一行（事件證據住安全子頁）；已解決的 Anthropic Status 事故 40 條原文移到 [[entities/claude-code-archive]]。拆頁評估 2026-11-01：不拆——九組共用「我這版會不會出事」一題；平台相容性一組最大，日後逾 600 行時先依 Windows／Desktop／Cowork 再切 %%

````

**callout**

````markdown
> **最新動態**（2026-10-31）
> - **遊戲重製被擋**：Anthropic 證實以更新引導 Claude Code 不重現他人特定遊戲，使用者回報無害的逆向工程與移植也被拒（🧠 組）。
> - **Claude in Chrome 在 reddit.com 全工具被擋**：自 9/18 起所有工具都被安全限制擋下（#95326，🔌 平台組）。
````

**摘要**

````markdown
## 摘要

- **先看母頁那張表**：現在還會發生、只發生在特定產品或平台的 8 條在 [[entities/claude-code#現在還沒修好的]]，每列寫了誰會遇到、你能做什麼；本頁是全部的逐條清單。
- **額度掉得快**：💰 組是逐條 issue 與互動數；官方認了沒、事故現在還在不在，見 [[entities/pricing#事故現在還在發生嗎]]。
- **安全漏洞**：🛡️ 組只記 Claude Code 版本上的修補狀態；攻擊手法與事件證據在 [[topics/ai-agent-safety-product-vulns]] 與 [[topics/ai-agent-safety-prompt-injection]]。
- **修在哪一版**：見 [[entities/claude-code-releases]]；issue 的留言數與讚數以本頁為準。
````

**原 L233**

````markdown
%% 母頁「現在還沒修好的」是本頁各組的結論表，條目本身不搬 %%
````

**原 L431 一處替換**

````markdown
見「現在還沒修好的」表列
→
見母頁「現在還沒修好的」表列
````

**🌐 組：取代 40 條已解決 Status 事故（放在第一條原位）**

````markdown
- **已解決的 Anthropic Status 事故 40 起**（2026-07-14～10-27，多在一小時內解決）：逐起時間與影響範圍見 [[entities/claude-code-archive#服務穩定性：已解決的 Status 事故]]；正在發生的以 [Anthropic Status](https://status.claude.com) 為準。
````

**🛡️ 原 L237–238（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**CLAUDE.md／AGENTS.md 指令沒有強制力（#53223，31 則留言、5 讚，2026-10-28）**：官方未回應；與 #2544 同一限制（見「🧠 行為與品質」）。證據見 [[topics/ai-agent-safety-product-vulns#2026-10]]。
````

**🛡️ 原 L239–240（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**使用者 email 被放進 prompt，可能被帶給外部網站（#81138，2026-10-29）**：官方未回應；與 #78431 觸發機制不同。證據見 [[topics/ai-agent-safety-product-vulns#2026-10]]。
````

**🛡️ 原 L241（重疊，縮成一行）**

````markdown
- ❓ **待查證**（標 2026-10-28｜查 v2.1.311、skip permissions｜複 2026-11-11）｜**v2.1.311 疑似移除 skip 模式的 `rm` 阻擋**：changelog 沒寫；2.1.309 的方向相反（改成直接拒絕）。證據見 [[topics/ai-agent-safety-product-vulns#2026-10]]。
````

**🛡️ 原 L242–243（重疊，縮成一行）**

````markdown
- ❓ **待查證**（標 2026-10-26｜查 Downloads、Codex｜複 2026-11-09｜訊 2026-10-27）｜**網站把指令檔丟進 Downloads，Claude Code／Codex 會照做**：兩個來源都只有標題，觸發條件與官方回應未見。證據見 [[topics/ai-agent-safety-prompt-injection#2026-10]]。
````

**🛡️ 原 L246（重疊，縮成一行）**

````markdown
- ❓ **待查證**（標 2026-10-30｜查 Plugin4Shell、v2.1.179｜複 2026-11-13）｜**Plugin4Shell 零點擊 RCE**：媒體稱 2.1.179 已修補，changelog 沒寫。證據見 [[topics/ai-agent-safety-product-vulns#2026-10]]。
````

**🛡️ 原 L247–249（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**GitHub Actions 預設範本傳有三家 agent 通用的 RCE 缺陷（Reddit，2026-09-14）**：claude-code-action 官方 advisory 無對應條目（10-03 查）。證據見 [[topics/ai-agent-safety-product-vulns#2026-09]]。
  - ❓ **待查證**（標 2026-09-14｜查 claude-code-action、預設範本｜複 2026-11-14）｜**範本缺陷是否屬實**：只有 Reddit 轉載，沒有具名研究者、CVE 或官方回應。
````

**🛡️ 原 L250（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**Google 搜尋廣告出現仿冒安裝包（Trojan:Win32/Kepavll!rfn）**：只從 `github.com/anthropics/claude-code` 等官方來源安裝。證據見 [[topics/ai-agent-safety-archive#技術彙整存檔（2026-05-18 以前）]]。
````

**🛡️ 原 L251（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**Opus 5 Auto Mode 被具名研究者繞過，且有在野利用（embracethered 等，2026-08-27～08-31）**：實測注入成功率 60–80%，官方委託評測稱 0%；官方未回應。與 v2.1.216／223 修的不同批。證據見 [[topics/ai-agent-safety-prompt-injection#2026-08]]。
````

**🛡️ 原 L252（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**摘要一個網址就會信任該站 llms.txt 的指令（The Register，2026-08-29）**：官方未回應。證據見 [[topics/ai-agent-safety-prompt-injection#2026-08]]。
````

**🛡️ 原 L253–255（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**惡意 `.git` 設定檔讓多款 agent 執行攻擊者程式碼（2026-09-02）**：v2.1.196 修了 core.fsmonitor 變體；第二變體據轉述至 2.1.252 未修。正常 clone 不受影響。證據見 [[topics/ai-agent-safety-prompt-injection#2026-09]]。
  - ❓ **待查證**（標 2026-09-02｜查 fsmonitor、2.1.252｜複 2026-11-14）｜**第二變體是否仍未修補**：只有轉述，官方沒有證實這個變體。
````

**🛡️ 原 L257–260（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**通過 CVP 審核的組織在 Claude Code 仍被資安防護擋下（#84352，201 則留言、29 讚，10-19 更新）**：官方未回應；CVP 綁 organization ID、可提申訴，條件見 [[topics/ai-agent-safety-cyber#防守方能申請什麼]]。
````

**🛡️ 原 L261（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**User-Agent 字串夾帶使用者 email（#78431，2026-08-11）**：08-22 查 issue 仍 open、官方掛了 `area:security` 但無回覆，changelog 未見修復。證據見 [[topics/ai-agent-safety-product-vulns#2026-10]]。
````

**🛡️ 原 L262（重疊，縮成一行）**

````markdown
- ✅ **已修復 v2.1.163**｜**「Comment and Control」：開一則 GitHub Issue 就能經注入碰到 CI secrets（Novee，2026-08-05）**：受影響 v0.2.54–v2.1.162。證據見 [[topics/ai-agent-safety-prompt-injection#2026-08]]。
````

**🛡️ 原 L263（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**Keyv 關聯 npm 蠕蟲在 repo 寫入 Claude Code hook（2026-08-04）**：至少 353 個套件版本（79 個套件名）受波及；屬 npm 供應鏈，Anthropic 無法單方修補。證據見 [[topics/ai-agent-safety-product-vulns#2026-08]]。
````

**🛡️ 原 L264（重疊，縮成一行）**

````markdown
- ✅ **已修復 v2.1.216（v2.1.223 加固）**｜**Auto Mode 下 Bash 複合重導向、隱形 Unicode 繞過權限**：v2.1.223 再補 4 項權限邊界。證據見 [[topics/ai-agent-safety-archive#2026-07]]。
````

**🛡️ 原 L265（重疊，縮成一行）**

````markdown
- ⛔ **官方拒修**｜**`CLAUDE.md` 的 `@import` 經 symlink 讀 repo 外檔案、不跳核准框（Tego AI，2026-07-18）**：07-20 結案為 Informative，官方說「信任此資料夾」對話框就是邊界。證據見 [[topics/ai-agent-safety-archive#2026-07]]。
````

**🛡️ 原 L269（重疊，縮成一行）**

````markdown
- 🔴 **未修復**｜**偵測到程式化使用時可能要求開攝影機確認真人（2026-05-20 起）**：官方刻意設計，觸發條件與關閉選項未說明。證據見 [[topics/ai-agent-safety-archive#2026-05-20]]。
````

組頭計數由 `split_cc.py` `recount()` 依條目實數重算（🛡️、💰、📂、平台、🌐 五組；🧠、MCP 與實數相符，原字不動），結果見 `accounting.txt` 末段。
純搬移：原 L230–232、L234–689 其餘全部（🛡️ 獨有 10 條 L244、245、256、266、267、268、270–273 原文）。

## C. 子頁 R `wiki/entities/claude-code-releases.md`

**標頭**

````markdown
# Claude Code 版本與發布通道：現在到哪一版、該跟哪條

現在到哪一版、我在 stable 還是 latest、哪一版加了什麼。

**類型：** product
**狀態：** active
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**首次出現：** 2025（正式推出）
**最後更新：** 2026-11-01
**最後新聞更新：** 2026-10-31
%% 2026-11-01 第 21 波自 [[entities/claude-code]] 拆出：發布通道、版本表、歷史記錄原文照搬；發布超過 90 天的 78 列與 2026-08 歷史 24 列移到 [[entities/claude-code-archive]]；母頁現況的逐版副本刪除，只在那裡的 v2.1.289、v2.1.269 補成表列 %%

````

**callout**

````markdown
> **最新動態**（2026-10-31）
> - **v2.1.316**：新增 `CLAUDE_CODE_DISABLE_ULTRATHINK`；Claude apps gateway 加群組共用的每月預算池。
> - **⚠️ Opus 4.8 fast mode 10-30 起棄用、11-30 移除**：移除後不會自動改用別的模型，請求直接回錯誤；用 fast mode 的人要改 Opus 5.5。
````

**新節：現在該跟哪條（取代原 L703–704）**

````markdown
## 現在該跟哪條

- **stable＝2.1.309、latest＝2.1.316**（npm dist-tags，查證 2026-11-01），差 7 個版號。
- **沒用 Opus 4.8 fast mode，stable 已夠**：危險 `rm` 的兩道修正（2.1.287／288）與 bypass 模式改直接拒絕（2.1.309，限 Desktop 與 VS Code）都在 stable 裡。
- **要這些才需要 latest**：Monitor tool（2.1.310）、`blockWritesOutsideWorkingDirectories`（2.1.314，預設關）。
- **升版會改到既有行為的**：破壞性變更與預設值改變見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。
````

**原 L697**

````markdown
官方安裝文件（[setup](https://code.claude.com/docs/en/setup)，2026-10-04 查證）：Claude Code 有 latest 與 stable 兩條通道，stable 約晚一週；現在該跟哪條見上方。
````

**原 L708＋新 🔎 一條**

````markdown
> 本表只收本站報導過的版本。**v2.1.242–244 與 v2.1.253–257 未見報導，不代表未發布。** 發布超過 90 天的版本見 [[entities/claude-code-archive]]；破壞性變更與預設值改變見 [[feature-radar#⚠️ 升級前要知道的預設值與破壞性變更]]。

- 🔎 **查無官方**（標 2026-11-01｜查 2.1.313、Cursor 延伸套件｜複 2026-11-15）｜**「2.1.313」不是官方版本號**：官方 changelog 在 2.1.312 之後是 2.1.314；Cursor 市集 Claude Code 延伸套件遭竄改的事件見 [[topics/ai-agent-safety-product-vulns#2026-10]]。
````

**原 L712（v2.1.316 列）**

````markdown
| **v2.1.316** | 2026-10-31 | 新增 `CLAUDE_CODE_DISABLE_ULTRATHINK`；⚠️ Opus 4.8 fast mode 11-30 移除；修 PowerShell hook exit 2 沒擋（[Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.316)）|
````

**原 L721 一處替換**

````markdown
bypass 模式下危險 `rm`／`rmdir` 改為直接拒絕並給改寫提示
→
Desktop／VS Code 的 bypass 模式危險 `rm`／`rmdir` 直接拒絕
````

**新列（依日期插入）**

````markdown
| **v2.1.289** | 2026-10-03 | 修正巢狀 shell 複合指令中 deny／ask 規則對使用者安裝的 mod 核准不生效；修正短指令造成終端機凍結；純 bug 修復（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.289)）|
| **v2.1.269** | 2026-09-11 | 新增 `claude plugin eval`：對外掛跑 eval 套件，產出可重現的 JSON＋HTML 評分（含不裝外掛的對照組）；同版新增 `/output-style`（見 [Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.269)）|
````

**指路替換（原行：舊→新）**

````markdown
L815：見上方「現況」 → 見已知問題頁「📂 Session」組
L1132：見下方「近期報導」 → 見母頁「近期報導」
L1157：細節見「已知問題」「版本更新」各節 → 細節見已知問題頁與「最新版本」
L1158：細節見上方「已知問題」「服務穩定性」「版本更新」各節 → 細節見已知問題頁與「最新版本」
L1161：見「已知問題」與本表細節區 → 見已知問題頁與本表細節區
L1201：詳見「已知問題」 → 詳見已知問題頁
L1208：詳見「已知問題」 → 詳見已知問題頁
L1209：詳見「已知問題」 → 詳見已知問題頁
L1210：詳見「已知問題」 → 詳見已知問題頁
L1211：詳見「已知問題」 → 詳見已知問題頁
L1213：詳見「版本更新」 → 詳見「最新版本」
L1220：詳見「已知問題」 → 詳見已知問題頁
L1221：詳見「已知問題」 → 詳見已知問題頁
L1223：詳見「已知問題」 → 詳見已知問題頁
````

**新：2026-08 時段總結（取代原 L1165–1188，原文進 archive）**

````markdown
### 2026-08 時段總結
- 08-01～08-05：v2.1.221 VS Code Focus view；v2.1.222 修補 worktree 隔離 session 可對主 checkout 下破壞性 git 指令；Claude API 新增 Inference Hooks（Enterprise beta）。
- 08-07～08-09：v2.1.224 新增 `claude self-hosted-runner`；跨 session 訊息互通（`ListAgents`＋`SendMessage`）經官方文件確認，#24798 轉 ✅。
- 08-10～08-14：官方宣布 08-14 起 auto 模式成為 Pro／Max／Team 新 session 預設、不再對分類器收費；v2.1.231 修 MCP OAuth 登入；v2.1.232 subagent forking 預設開啟。
- 08-17～08-22：v2.1.235 `spellcheck`；v2.1.237 修 gateway 下 prompt caching、新增 Concise 輸出風格；v2.1.238 `keybindingFlavor`；anthropic-sdk-python v1.0.0（⚠️ httpx2）；v2.1.239 成本估算計入資料常駐 1.1 倍。
- 08-23～08-27：Opus 5 簡單任務耗時異常，Claude Code 團隊回應是 effort 顯示方式調整；v2.1.245 修 glibc 2.44 當機；v2.1.247 新增 `SendFeedback` 工具。
- 08-29～08-30：v2.1.251 新增 PreModelSwitch／PostModelSwitch hook；SDK 的 files／skills 改 GA 介面；官方宣布 09-14 起週配額永久調高 25%、取消暫行 +50%。
- 本月 Anthropic Status 多起短暫事故均已解決；新增的已知問題與互動數見已知問題頁各組。
- 原始條目見 [[entities/claude-code-archive#2026-08]]
````

**原 L1217 流浪列 → 04 月總結末一條**

````markdown
- ~2026-03：效能退步開始，社群陸續察覺。
````

**頁尾一句**

````markdown
文中「已知問題頁」指 [[entities/claude-code-known-issues]]。
````

純搬移：原 L695–702（h3→h2）、L705–707、L709–900 中發布日 ≥ 2026-08-03 的 96 列、L901、L909（`## 開發者須知`）、L1112–1164、L1189–1215、L1218–1228。

## D. 子頁 F `wiki/entities/claude-code-features.md`

**標頭**

````markdown
# Claude Code 功能怎麼用：hooks、subagent、桌面版

功能怎麼用：hook 能不能當防線、subagent 派哪種、桌面版能做什麼。

**類型：** product
**狀態：** active
**領域：** 🛠️ 工具/功能
**上層：** [[entities/claude-code]]
**首次出現：** 2025（正式推出）
**最後更新：** 2026-11-01
**最後新聞更新：** 2026-10-30
%% 2026-11-01 第 21 波自 [[entities/claude-code]] 拆出：核心功能、桌面版功能地圖、hooks、subagent 原文照搬；母頁現況的 23 條桌面版文件異動與「開發者須知」中屬用法的 8 條一併搬來；hooks 結論句依官方權限文件改寫、subagent 補平行分派一句（查證 2026-11-01） %%

````

**callout**

````markdown
> **最新動態**（2026-10-30）
> - **桌面版文件 10-26、10-30 兩次大增字**（189,365→203,154 字）：段落太多，沒有逐段差異可看，要知道改了什麼得自己開原文比對。
````

**摘要**

````markdown
## 摘要

- **hook 能不能當防線**：hook 一觸發就是硬擋，但不保證會觸發；要保證一定擋，用 deny 規則或沙箱，hook 當第二層（見 [[#hooks：事件、失效模式與能不能當防線]]）。
- **平行分派派哪種 subagent**：什麼都不設就在背景跑、同時最多 20 個；要共用主對話的 context 與 cache 選 fork（見 [[#Subagent 型別差異對照]]）。
- **桌面版能做什麼**：依主題歸群在 [[#桌面版功能地圖]]，每條日期對到同頁「桌面版文件時序」。
- 官方建議的做法見 [[topics/coding-workflow-guide]]；Mods 見 [[entities/claude-mods]]；文中「已知問題頁」指 [[entities/claude-code-known-issues]]。
````

**原 L934**

````markdown
> 把下方「桌面版文件時序」的桌面版文件（`desktop.md`）異動依主題歸群；每條只收時序條目已記的事實，日期指向時序原條。官方文件 [desktop.md](https://code.claude.com/docs/en/desktop.md)，彙整日 2026-10-25。
````

**新 h3：桌面版文件時序（其下接原 L114–120、122–132、137–138、140、142–146 原文，最新在上）**

````markdown
### 桌面版文件時序

````

**指路替換（原行：舊→新）**

````markdown
L910：（見「已知問題」） → （見已知問題）
L946：（查證標記在近期異動的 10-24 條） → （查證標記在下方時序的 10-24 條）
L951：（細節未載，見歷史記錄） → （細節未載，見 [[entities/claude-code-releases#歷史記錄]]）
L951：相關未修問題見已知問題 #40283、#45937 → 相關未修問題見已知問題頁 #40283、#45937
````

**原 L978**

````markdown
> 本節只彙整與導覽，細節留在原處：版本頁（`onFailure`、`PreModelSwitch`）、已知問題頁各組、本頁「開發者須知」。官方 hooks 文件 2026-10-11 查證，權限優先序 2026-11-01 查證。
````

**原 L1006**

````markdown
- **社群實測**：上表三個 🔴（#6305 未觸發、Stop hooks 被忽略、#24057 改設定要重啟）是 hook 靜默不作用的路徑；#9516、#7075 是功能請求（沒有中斷 hook、不能分情境隔離）。v2.1.294 修的那條是「寫了封鎖卻沒擋住」。
````

**原 L1007（hooks 結論，依查證 #8）**

````markdown
- **結論：hook 一觸發就是硬擋，但不保證會觸發。** 要保證一定擋，用 deny 規則或沙箱，hook 當第二層。
  - 擋得硬：官方 [permissions 文件](https://code.claude.com/docs/en/permissions)寫明 `PreToolUse` hook 擋下的呼叫不會被任何 allow 規則放行，exit 2 在權限規則之前就攔下（查證 2026-11-01）。
  - 不一定觸發：`if` 比對是盡力而為，也有沒觸發（#6305）、設定沒生效（#24057）的回報；`onFailure: "block"` 只補 hook 自己壞掉那一種缺口。
  - 反過來不成立：hook 回 allow 蓋不過 deny 規則。例外：沒有 managed settings、也不是 Team／Enterprise 登入時，mod 的 `tool.check` 可放行 hook 擋下的呼叫（見 [[entities/claude-mods]]）。
````

**新：插在原 L1011 前（平行分派選哪種，依查證 #9）**

````markdown
**平行分派選哪種**：什麼都不設，Claude 從主對話派出的 subagent 就在背景跑，同時最多 20 個（`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 可調）；要共用主對話的 context 與 prompt cache（較便宜）用 fork，要乾淨的隔離 context 用非 fork；要在分割窗格各自協作、互派任務才用 teammate（只能前景）。（[官方 sub-agents 文件](https://code.claude.com/docs/en/sub-agents)，查證 2026-11-01）
````

**原 L1056（拆成五步，原條件逐字保留語意）**

````markdown
- 前景還是背景，依序看第一個成立的：
  1. teammate 派出的 → 前景（teammate 設 `background: true` 會被拒）
  2. 設了 `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` → 前景
  3. fork 模式開著 → 背景
  4. fork 關、沒寫 `background: true` → 背景；但主對話需要結果才能繼續時是前景
  5. fork 關、寫了 `background: true` → 背景
````

**原 L1082**

````markdown
> 本表依官方文件 2026-08-22 查證、2026-10-22 補欄、2026-11-01 補平行分派一句；逾 90 天未回訪時在此標明。
````

純搬移：原 L918–933、L935–975、L976–977、L979–1005、L1008–1081；`## 開發者須知` 收原 L903、904、906、907、908、910、913、914。

## E. archive `wiki/entities/claude-code-archive.md`

**說明句（取代原 archive L34）**

````markdown
> 本頁保存從 [[entities/claude-code]] 與三個子頁移出的原始條目：歷史記錄、發布超過 90 天的版本表列、已解決的 Anthropic Status 事故。條目一字不刪，只是搬離主頁讓主頁讀得動；重點見主頁與 [[entities/claude-code-releases]]。
````

**各月段尾新增的小標與表頭（2026-04／05／06／07 各一次，其下接該月版本列原文）**

````markdown

**版本表（發布超過 90 天的列）**

| 版本 | 發布日 | 重點 |
|------|------|------|
````

**新 h2（檔尾）**

````markdown
## 服務穩定性：已解決的 Status 事故

自 [[entities/claude-code-known-issues]]「🌐 服務穩定性」組移入的已解決事故，原文照搬、最新在上；最後一條原住母頁現況。

````

新 `## 2026-08`：表頭＋原 L1165–1188 原文、08-01／08-02 兩列版本（若有）、原 L1229–1231 懸置細節。`## 服務穩定性：已解決的 Status 事故` 下接 40 條原文（原 L626 起，見 accounting）＋原 L151。「最後更新」→ 2026-11-01，「最後新聞更新」不動。

# 進規則檔

> 條文逐字；「原文」指現行檔該段一字不改搬過來。行號指 2026-11-01 現行檔。

## F1. `.claude/reporter-rules/features/pages.md`：`## entities/claude-code`（原 L126–147）整節換成下列四節

````markdown
## entities/claude-code

母頁回答「Claude Code 現在有什麼毛病、哪些修了、哪些你得繞過去」，並把版本、毛病、功能怎麼用三條線各指往子頁。結論層是 `## 現在還沒修好的`（結論表）與 `## 現況` 開頭的「版本」兩條；逐條已知問題、逐版明細、功能用法住三個子頁，母頁不收。

### 0. 樹的路由表（寫條目前先查）

| 子頁 | 收什麼 |
|---|---|
| `entities/claude-code-known-issues` | GitHub Issues 與社群回報的 Claude Code 故障、功能請求與互動數更新；Anthropic Status 事故；🛡️ 組只收版本號綁定的修補狀態 |
| `entities/claude-code-releases` | 每一版的異動（CLI 與 SDK，含純 bug fix 版）、stable／latest 通道現況、歷史記錄每日一列 |
| `entities/claude-code-features` | 功能機制與用法：核心功能清單、桌面版官方文件異動（時序＋功能地圖）、hooks、subagent、不屬單一版本的用法提醒 |
| `entities/claude-mods` | Claude Mods 的機制、權限與安全 |

- **一則條目只住一頁，依序問，第一個「是」就定案：** ① 是某一版的 release notes／changelog 條目 → releases（該版修了某條已知問題，另在 known-issues 把該條翻 ✅、註明版本，不抄版本內容）；② 是一則會讓使用者出問題的回報（issue、Status 事故、社群實測的故障）→ known-issues；③ 是官方文件對某功能怎麼用的異動，或不屬單一版本的用法提醒 → features；④ 平台級帳號／年齡政策、尚待官方佐證的傳聞、定位與市場 → 母頁 `## 現況`。四問都答不出，寫母頁 `### 未歸類`，週更時分派（不設預設子頁，`.claude/reporter-rules/page-lifecycle.md`「路由」條）。
- 安全事件本身（攻擊手法、證據、受影響範圍）的家是 `topics/ai-agent-safety` 的子頁（`.claude/reporter-rules/safety-policy/pages.md` 第 0 條）；known-issues 🛡️ 組一事一行：狀態＋修補版本＋互動數＋「證據見 [[事件所在子頁#YYYY-MM]]」，不重抄事件證據。
- 上表「收什麼」是四問的摘要，兩者不一致時以四問為準。

### 1. 每日（母頁只准動五樣）

1. callout：覆寫成當天各子頁新事件的一句總覽並連子頁（母頁 callout 日期落後子樹最新新聞，`scripts/check_hierarchy.py` 會紅）。來源歸因的 page 填事件所在的子頁。
2. 路由表「最後動態」欄＝該子頁標頭「最後新聞更新」，照抄。
3. `## 現況` 開頭「版本」兩條：最新版號與日期同步 releases 版本表最新一列；`stable`／`latest` 的值屬主編查證（npm dist-tags，`.claude/skills/wiki-lint-sweeps/references/sweeps.md` 5a），記者不自填。
4. `## 現在還沒修好的` 依下方第 2 條覆寫；`## 現況` 其餘段落依第 0 條 ④ 收條目。
5. 既有懸置標記加 `訊`。母頁「最後新聞更新」不因子頁動（page-lifecycle 母頁契約）。

### 2. 已知問題的結論層

（原文：原 L134–140「已知問題的結論層」整段，兩處改字——「「已知問題」分組上方的**結論層索引**」改為「母頁的**結論層索引**（各條目住 `entities/claude-code-known-issues`）」；「完整清單見…」不在條文內，不動；退場句「並在原條目末加」改為「並在 known-issues 原條目末加」。）

### 3. 兩個同名指路殼

`## 版本更新`、`## hooks：事件、失效模式與能不能當防線` 是指路殼（一到兩句＋連子頁）。`## 版本更新` 有讀者版日報與 [[feature-radar]] 的錨點入邊，**節名凍結**、不得刪。`## hooks：…` 等 `topics/coding-workflow-guide`、`topics/community-guardrails` 的錨點改指 features 後即刪（刪前 `scripts/build_web.py` 錨點 WARN 須為 0）。

### 平台級帳號／年齡政策公告

Anthropic 對全產品（含 Claude Code）的帳號、年齡、身分驗證政策公告 → 本頁 `## 現況`「近期平台與文件異動」，延續 Persona／Yoti 條目；若此類條目累積超過 5 條，依 `.claude/reporter-rules/page-lifecycle.md` 拆分原則評估獨立成消費版產品頁。

---

## entities/claude-code-known-issues

本頁回答「某個 bug 修了沒、誰會遇到、有沒有繞法」。結論表在母頁（上方第 2 條），本頁是九組逐條清單。

### 已知問題狀態維護

（原文：原 L128–132 三條。）

- issue 的留言數與讚數住本頁；別頁只寫 issue 號與開關狀態，要數字就連過來。
- Anthropic Status 事故翻 ✅ 滿 30 天，於 `/wiki-lint` 移到 `entities/claude-code-archive`「服務穩定性：已解決的 Status 事故」（原文照搬、最新在上），🌐 組那一行總數與日期範圍同步改。
- 移條目時同步該組組頭的統計行。

---

## entities/claude-code-releases

本頁回答「現在到哪一版、該跟 stable 還是 latest、哪一版加了什麼」。結論層是 `## 現在該跟哪條`：四條固定為 stable／latest 現值、只跟 stable 夠不夠、什麼才需要 latest、升版會改到行為的去 [[feature-radar]] 階梯表。stable 值改變、或新版出現會改到既有行為的設定時覆寫對應那條；stable 值屬主編查證。

- **`## 最新版本` 退場線：** 保留最近 90 天發布的版本；更舊者於 `/wiki-lint` 移到 `entities/claude-code-archive` 該月 `## YYYY-MM` 段尾的「版本表（發布超過 90 天的列）」，原文照搬。`## 最新版本` 有 [[entities/claude-tag]] 與 [[feature-radar]] 的錨點入邊，改名回掃；母頁同名殼 `## 版本更新` 凍結（見母頁第 3 條）。
- 官方 changelog 沒有的版本號不得寫成表列；媒體報導的版號對不上時，在表上方寫一條 🔎 指向事件所在頁。
- 歷史記錄每日一列；蒸餾照 `.claude/reporter-rules/page-lifecycle.md`「時段蒸餾與封存」，原文進共用 archive 的 `## YYYY-MM`，本頁留時段總結。

---

## entities/claude-code-features

本頁回答「功能怎麼用：hook 能不能當防線、subagent 派哪種、桌面版能做什麼」。結論層是 `## 摘要` 與 hooks 節「三、能不能當安全控制」的結論句。

- 桌面版官方文件（`desktop.md`）異動：新的一條寫在 `### 桌面版文件時序` 最上方，同輪在 `### 桌面版功能地圖` 對應主題補一行（日期指向時序原條）。
- hooks、subagent 兩節只收官方文件與 changelog 寫得出的事實；改結論句要附官方文件查證日。subagent 節逾 90 天未對官方文件回訪時，在節尾那句標明。
- Mods 的機制住 [[entities/claude-mods]]，本頁只互指。
````

## F2. `features/pages.md` 其他指名處（逐行替換）

| 行 | 舊 | 新 |
|---|---|---|
| L110 | `原記錄留在 [[entities/claude-code#版本更新]]` | `原記錄見 [[entities/claude-code-releases#最新版本]]（發布逾 90 天者在 [[entities/claude-code-archive]]）` |
| L116 | `與 \`wiki/entities/claude-code.md\` 版本表最新列同步` | `與 \`wiki/entities/claude-code-releases.md\` 版本表最新列同步` |
| L167 | `issue 的留言數與讚數住 [[entities/claude-code]]` | `issue 的留言數與讚數住 [[entities/claude-code-known-issues]]` |
| L252 | `下沉到時序或 [[entities/claude-code]]` | `下沉到時序或 [[entities/claude-code-releases]]` |
| L118 | 不動（「現在還沒修好的」仍在母頁） | — |

## F3. `.claude/reporter-rules/features/daily.md`

負責頁面表 L15 一列換成四列：

````markdown
| `wiki/entities/claude-code.md` | 母頁：callout、路由表「最後動態」、`## 現況`（帳號／年齡政策、尚待官方佐證的傳聞、定位與市場、版本兩條）、`## 現在還沒修好的`；寫條目前先查 `.claude/reporter-rules/features/pages.md` 第 0 條路由表 |
| `wiki/entities/claude-code-known-issues.md` | GitHub Issues 高互動 bug／功能請求、互動數更新、Anthropic Status 事故 |
| `wiki/entities/claude-code-releases.md` | Claude Code 與 SDK 版本更新、新指令／旗標、Breaking change；歷史記錄每日一列 |
| `wiki/entities/claude-code-features.md` | 官方文件的功能用法異動（桌面版文件、hooks、subagent） |
````

| 行 | 舊 | 新 |
|---|---|---|
| L29 | `記入 claude-code.md 已知問題（含 issue 編號與連結）` | `記入 \`claude-code-known-issues.md\` 對應分組（含 issue 編號與連結）` |
| L80 | `記入 \`entities/claude-code\` 版本表` | `記入 \`entities/claude-code-releases\` 版本表` |

## F4. `.claude/reporter-rules/page-lifecycle.md` L52（母頁契約「每日 ingest」格，N3）

舊：`（現有：\`topics/ai-agent-safety\` 的 \`## 現在還擋不住的攻擊\`）`
新：`（現有：\`topics/ai-agent-safety\` 的 \`## 現在還擋不住的攻擊\`；\`entities/claude-code\` 的 \`## 現在還沒修好的\` 與 \`## 現況\`——後者每日收帳號政策與尚待佐證的傳聞，路由見 \`.claude/reporter-rules/features/pages.md\` 第 0 條）`

## F5. `.claude/skills/wiki-lint-sweeps/references/sweeps.md` 5a 末加一條（N4）

````markdown
4. **Claude Code 通道現值**：同輪跑 `npm view @anthropic-ai/claude-code dist-tags`，把 `stable`／`latest` 寫進 `wiki/entities/claude-code.md`「現況」的「版本」第一條與 `wiki/entities/claude-code-releases.md`「現在該跟哪條」第一條，查證日一併改；stable 跨過某個會改到既有行為的版本時，同步改第二、三條。雲端沒有 npm 時跳過，「本機承接」記一行。這是母頁結論層的週更觸發邊（功能類沒有 `weekly.md`）。
````

## F6. 跨維護者規則檔（主 session 判，逐字建議）

| 檔:行 | 舊 | 新 |
|---|---|---|
| `safety-policy/pages.md` L87 | `2. 版本號與 Claude Code 功能面的已知問題另住 [[entities/claude-code]]；本頁是事件證據與狀態的家，兩頁對同一個洞狀態不同時，以有一手出處、日期較新者為準，並在回報「同步自查」欄寫「請主編轉知功能記者」。` | `2. 版本號綁定的修補狀態一行住 [[entities/claude-code-known-issues]]「🛡️ 安全與隱私」（指回本頁事件所在 \`#YYYY-MM\`）；本頁是事件證據與狀態的家。修補版本有新一手出處時，在回報「同步自查」欄寫「請主編轉知功能記者」改那一行。` |
| `models/pages.md` L155 | `後兩者的家是 [[entities/claude-code]] 與 [[entities/pricing]]` | `後兩者的家是 [[entities/claude-code-known-issues]] 與 [[entities/pricing]]` |
| `commercial/weekly.md` L35 | `完整功能落差屬 [[entities/claude-code]]` | `完整功能落差屬 [[entities/claude-code-known-issues]]（🔌 平台相容性）` |
| `community/pages.md` L134 | `缺陷的家是 [[entities/claude-code]]` | `缺陷的家是 [[entities/claude-code-known-issues]]` |
| `wiki-ingest/references/classification.md` L68 | `` `entities/claude-code` + feature-radar `` | `` `entities/claude-code-releases` + feature-radar `` |
| `shared-when.md` L14 | `` `claude-code.md` 行數只排全庫第四，讀一次卻約 86K token、全庫最貴（長表格列，每行平均 180 字元）；它最常被改的「已知問題」**單節就約 41K** `` | `` 拆頁前的 `claude-code.md`（2026-10）行數只排全庫第四，讀一次卻約 86K token（長表格列，每行平均 180 字元）；拆出來的 `claude-code-known-issues.md` 仍約 137K 字元，是功能類最貴的一頁 ``；後半句「——照節標題讀，等於每天為了改一列 bug 狀態載入 41K」一併刪 |
| `shared-when.md` L16 | `` `claude-code.md`、 `` | `` `claude-code-known-issues.md`、 `` |
| `reader-digest/references/format.md` L49 | 範例，不改 | — |
