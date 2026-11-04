# 主編官方查證 — 第 21 波 entities/claude-code（2026-11-01）

查證工具：`npm view` dist-tags、anthropics/claude-code 淺 clone 的 CHANGELOG.md（最後 commit 2026-10-31）、WebFetch 官方文件（code.claude.com hooks／permissions／sub-agents）與 GitHub issue 頁面（雲端 `gh api` 對 anthropics/claude-code 回「access not enabled」，改走網頁）、WebSearch（二手，標明）。行號為 `wiki/entities/claude-code.md` 2026-11-01 原檔（1,231 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 官方一手 | 判定 |
|---|---|---|---|
| 1 | L703「stable 標籤已到 2.1.308……落差已追上」 | `npm view @anthropic-ai/claude-code dist-tags`（2026-11-01）：`stable: 2.1.309`、`latest: 2.1.316`、`next: 2.1.316` | **過期**：stable 已到 2.1.309，所以 L704「v2.1.309 不在 stable」不再成立。「落差已追上」只對 rm 修正成立；stable 與 latest 仍差 7 個版號（2.1.310–316） |
| 2 | L57、L704 v2.1.309「bypass 模式下危險 rm／rmdir 改直接拒絕」 | CHANGELOG 2.1.309：「Changed the dangerous `rm` and `rmdir` prompt in bypass permissions mode **in the Desktop app and VS Code** to deny the command at once with a rewrite hint」 | 一致，但頁面漏了「Desktop 與 VS Code」適用範圍；終端機 CLI 的同類變更是更早的「等 2 分鐘再拒絕」（CHANGELOG L2487） |
| 3 | L50、L712 v2.1.316 | CHANGELOG 2.1.316 第 1–2 條吻合；同版另有 `CLAUDE_CODE_SUBAGENT_EFFORT`、**Opus 4.8 fast mode 10-30 起棄用、11-30 移除（不 fallback，回錯誤）**、PowerShell hook exit 2 未擋修正 | 頁面「官方原文截斷」說法不成立：全文可得。fast mode 棄用是有期限的破壞性變更，頁面零命中 |
| 4 | 版本表缺 v2.1.289、v2.1.269（健檢卡 §0-2） | CHANGELOG 有兩版完整條目：2.1.289 為 deny／ask 規則對 mod 核准、`Read` deny 經 symlink 失效等修正；2.1.269 新增 `claude plugin eval`、`/output-style` | 可補表；現況兩行與官方一致 |
| 5 | H-1458cf「Cursor 惡意 Claude Code 套件，受影響 2.1.312／2.1.313」 | CHANGELOG **沒有 2.1.313 節**（2.1.312 之後直接 2.1.314）；2.1.312 條目無安全事件字樣；WebSearch 找不到提及這兩個版號的一手或二手報導 | **🔎 查無官方**。是否收、收哪裡交設計者；本頁版本表不得把 2.1.313 寫成官方版本 |
| 6 | 結論表 L215–222 八列皆 🔴 | 抽三列看 issue 頁：#53940（Cowork 截斷）open、無官方回應、最後活動 07-16；#24057（改設定要重啟）open、最後留言 10-23、無官方回應；#4953（OOM）open，07-19 有使用者回報 2.1.181／2.1.214 起安裝程式記憶體下降 | 三列 🔴 一致；#4953 可補「部分版本已改善（社群回報）」 |
| 7 | hooks L1005「`if` 過濾器是盡力比對，要硬性允許或拒絕請用權限系統」 | hooks 文件：「Because the `if` filter is best-effort, use the permission system rather than a hook to enforce a hard allow or deny.」 | 一致 |
| 8 | hooks L1007「hook 是保險絲不是門鎖，硬擋用權限系統」 vs coding-workflow-guide L197「PreToolUse 最硬，deny 連 bypassPermissions 都擋得住」（冷讀者 Q3 衝突） | permissions 文件 §Precedence：「A call that a `PreToolUse` hook blocked stays blocked, whichever settings file the hook comes from.」「A blocking hook also takes precedence over allow rules. A hook that exits with code 2 stops the tool call before permission rules are evaluated」；反向「PreToolUse hook decisions don't bypass permission rules」（hook 的 allow 蓋不過 deny 規則）。例外：無 managed settings 也非 Team／Enterprise 登入時，mod 的 `tool.check` 可放行 hook 擋下的呼叫。bypass 模式與 hook 的關係官方文件沒有逐字句 | **兩頁各對一半**：hook **觸發時**的擋是硬的（先於權限規則）；hook **會不會觸發**（`if` 盡力比對、#6305 未觸發、設定未生效）不可靠。cwg L197「連 bypass 都擋得住」無官方逐字句，應標 🔎 或改寫；本頁 L1007 結論句應改成「擋得硬、但可能沒觸發——要保證一定擋，用 deny 規則或沙箱」 |
| 9 | subagent L1056「預設選擇依序……fork 關且無 `background: true` → 預設 background」 | sub-agents 文件：「With nothing configured, a subagent that Claude spawns from your main conversation starts in the background.」「when 20 subagents are running…`Concurrent subagent limit reached`」「`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`」 | 一致；平行上限 20 與覆寫變數本頁沒寫（agent-stack L91 有 20 路） |
| 10 | L697「stable 缺的權限修正與切換建議見 2026-W40 週報開發實務專文」 | 站內無 wikilink（冷讀者 Q2） | 非官方事實；設計者處理成站內句或刪 |

## 二、考題的官方錨句

- **Q1 額度掉得快官方認了沒**：本波未逐一查 💰 組；pricing 是第 24 波對象。claude-code 端只要確保 K 子頁 💰 組有指向 pricing「事故現在還在發生嗎」的一句，互動數家照 features/pages.md L167 住 K。
- **Q2 升不升、stable 還是 latest**：stable＝2.1.309（含 rm 修正與 bypass rm 拒絕）、latest＝2.1.316。2.1.310–316 之間有兩件會改到既有設定的事：2.1.314 新增 `blockWritesOutsideWorkingDirectories`（預設關，不影響）、**2.1.316 Opus 4.8 fast mode 11-30 移除**（用 fast mode 的人必須遷到 Opus 5.5）。一句答案：「沒用 Opus 4.8 fast mode，stable 已夠；要 Monitor tool、寫入邊界設定等新功能才需要 latest」。
- **Q3 hook 能不能當防線**：官方錨句見上表 #7、#8。一句答案：「hook 一旦觸發就是硬擋（先於 allow 規則），但比對是盡力而為、也有不觸發的已知 bug；要保證，用 deny 規則或沙箱，hook 當第二層」。
- **Q4 平行分派選哪種**：官方預設即 background；同時上限 20（可調）；fork 繼承主對話與工具池。

## 三、懸置

- 本頁新語法 29 筆、逾期 0（健檢卡 §9），本波不處置；搬家時隨群走。
- ⟨Q-14⟩、⟨Q-15⟩ 兩則已寫「查證確認」——設計者核過可結案。

## 四、給設計者三句

1. 版本事實的家只能有一個：R 子頁版本表；母頁「現況」只留最新版＋stable／latest 現值（2.1.309／2.1.316）＋一句該不該升，L48–109 其餘砍；補 v2.1.289、v2.1.269 與 2.1.316 的 Opus 4.8 fast mode 棄用。
2. hooks 結論句照 #8 改寫，cwg L197 屬開發實務記者，走 `pending_handoffs.py`（不在本波改）。
3. 2.1.313 不存在於官方 changelog，惡意套件事件的家在安全子頁 `ai-agent-safety-product-vulns`，K／R 子頁至多一句指路並標 🔎。
