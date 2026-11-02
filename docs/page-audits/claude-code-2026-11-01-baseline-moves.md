# 第 21–23 波拆頁：基線搬家清單（2026-11-02）

> 本檔原為第 21 波；第 23 波 anthropic-business 拆頁另有 46 筆同性質搬家（清單在 `anthropic-business-2026-11-02-proposal-map.md` 第六節），本機一次 `--rebuild --allow-grow` 一併收；第 22 波貢獻 0 筆。

雲端 session 的 `guard_roles.py` H6 擋 `--rebuild`／`--allow-grow`／`--write-baseline` 與 `data/*-allow.json`，所以這兩道閘在 `claude/stoic-edison-ewvmcx` 上刻意是紅的（使用者 2026-11-02 裁決）。紅的每一筆都是原文隨拆頁從 `entities/claude-code` 搬到子頁，內容與長度不變。**併 master 前，在本機做下面兩件事：**

1. **cell 基線**（配不回 0；預期 added 153（第 21 波 107＋第 23 波 46）；removed 以輸出為準，都在舊頁名 `entities/claude-code`、`topics/anthropic-business` 下）：

   ```bash
   python scripts/check_cell_limits.py --rebuild --allow-grow --reason "第 21 波 claude-code 拆頁：107 筆存量超限隨原文搬到三子頁（內容與長度不變，清單見 docs/page-audits/claude-code-2026-11-01-baseline-moves.md）；舊頁名下失效存量一併收緊；第 23 波 anthropic-business 拆頁 46 筆同性質，清單見 docs/page-audits/anthropic-business-2026-11-02-proposal-map.md 第六節"
   ```

2. **reader-language 白名單**（不要跑 `--write-baseline`：存量基線已是 0，跑了會把兩筆產品詞種回去）：`data/reader-language-allow.json` 把 #22、#23（`line_contains`「只談封存」，兩筆重複，#23 可刪）的 `page` 改為 `entities/claude-code-known-issues`；#24（「對話封存後完全消失」）改為 `entities/claude-code-releases`；reason 原樣。之後 `python scripts/check_reader_language.py` 應印 `OK`。

兩件做完 `python scripts/run_tests.py` 應 exit 0，再併 master。

## cell 搬家逐筆（`moves.py` 輸出原樣）

cell：改後新增 107 筆；能配回 entities/claude-code 舊基線 107；配不回 0
| # | 新頁 | 行 | 類型 | 錨點 | 長度 | 舊頁基線上限 |
|---|---|---|---|---|---|---|
| 1 | entities/claude-code-features | 64 | list_item | 1Password 整合已確認（查證日 2026 | 353 | 353 |
| 2 | entities/claude-code-features | 137 | list_item | 官方文件更新（2026-08-29） | 204 | 204 |
| 3 | entities/claude-code-features | 192 | list_item | 自訂 agent 支援的 frontmatter | 295 | 295 |
| 4 | entities/claude-code-features | 223 | list_item | background 白名單 | 236 | 236 |
| 5 | entities/claude-code-features | 262 | list_item | 桌面版官方文件：Auto Mode 模型門檻與 | 331 | 331 |
| 6 | entities/claude-code-features | 265 | list_item | CLI 權限客製化避免手動確認（2026-06- | 238 | 238 |
| 7 | entities/claude-code-known-issues | 82 | list_item | ✅ 已修復 v2.1.197（2026-07-0 | 601 | 601 |
| 8 | entities/claude-code-known-issues | 83 | list_item | ✅ 已修復 v2.1.118｜Claude Co | 508 | 508 |
| 9 | entities/claude-code-known-issues | 84 | list_item | API 金鑰外洩風險 | 359 | 359 |
| 10 | entities/claude-code-known-issues | 85 | list_item | Claude Code 攝影機存取請求——官方確 | 363 | 363 |
| 11 | entities/claude-code-known-issues | 86 | list_item | 撤銷授權後 session 紀錄持續出現（202 | 233 | 233 |
| 12 | entities/claude-code-known-issues | 88 | list_item | Gmail MCP connector 黑暗設計 | 250 | 250 |
| 13 | entities/claude-code-known-issues | 103 | list_item | 使用者實測：輸入第一個提示前即已耗用約 51,0 | 628 | 628 |
| 14 | entities/claude-code-known-issues | 104 | list_item | Pro 方案新開 session 預設開啟 1M | 527 | 527 |
| 15 | entities/claude-code-known-issues | 105 | list_item | Max 20（$200/月）方案升級至 v2.1 | 312 | 312 |
| 16 | entities/claude-code-known-issues | 107 | list_item | Max 5x 升級至 Max 20x 失敗，顯示 | 479 | 479 |
| 17 | entities/claude-code-known-issues | 108 | list_item | Fable 5 於 Max 方案自 2026-0 | 542 | 542 |
| 18 | entities/claude-code-known-issues | 109 | list_item | API Error: Rate limit re | 284 | 284 |
| 19 | entities/claude-code-known-issues | 110 | list_item | 方案 5 小時用量限額在不到 1 小時 30 分 | 252 | 252 |
| 20 | entities/claude-code-known-issues | 115 | list_item | 功能請求：印度地區專屬定價方案（INR 計價）（ | 231 | 231 |
| 21 | entities/claude-code-known-issues | 118 | list_item | HERMES.md 計費路由 bug（GitHu | 313 | 313 |
| 22 | entities/claude-code-known-issues | 122 | list_item | Session 額度上限時無法順暢接續／功能請求 | 595 | 595 |
| 23 | entities/claude-code-known-issues | 127 | list_item | 升級方案付款失敗，PaymentIntent 於 | 231 | 231 |
| 24 | entities/claude-code-known-issues | 128 | list_item | 一般開發操作在數分鐘內即異常耗盡 token／配 | 219 | 219 |
| 25 | entities/claude-code-known-issues | 129 | list_item | 選用 opus-plan 模型時，即使已達成 1 | 303 | 303 |
| 26 | entities/claude-code-known-issues | 171 | list_item | 恢復曾用延伸思考的 session 永久失敗，A | 438 | 438 |
| 27 | entities/claude-code-known-issues | 173 | list_item | Output styles 帶 YAML fro | 246 | 246 |
| 28 | entities/claude-code-known-issues | 174 | list_item | 功能請求：優先訊息通道，可在執行途中即時導正 C | 290 | 290 |
| 29 | entities/claude-code-known-issues | 175 | list_item | Claude Code 回傳空白思考區塊，推理 | 280 | 280 |
| 30 | entities/claude-code-known-issues | 176 | list_item | 「Prompt is too long」錯誤導致 | 324 | 324 |
| 31 | entities/claude-code-known-issues | 179 | list_item | 功能請求：允許自訂 .claude/agents | 327 | 327 |
| 32 | entities/claude-code-known-issues | 184 | list_item | v2.1.150 起滑鼠滾輪失效，滾動動作誤判為 | 222 | 222 |
| 33 | entities/claude-code-known-issues | 187 | list_item | 功能請求：訊息佇列模式——排入佇列而非中斷進行中 | 220 | 220 |
| 34 | entities/claude-code-known-issues | 188 | list_item | Opus 5 xhigh 推理強度於 Claud | 310 | 310 |
| 35 | entities/claude-code-known-issues | 194 | list_item | autoMemoryEnabled=false | 318 | 318 |
| 36 | entities/claude-code-known-issues | 197 | list_item | 「The model's tool call c | 342 | 342 |
| 37 | entities/claude-code-known-issues | 198 | list_item | --dangerously-skip-permi | 229 | 229 |
| 38 | entities/claude-code-known-issues | 199 | list_item | 回應超過 32000 output token | 215 | 215 |
| 39 | entities/claude-code-known-issues | 202 | list_item | 畫面/終端機閃爍（GitHub issue #7 | 210 | 210 |
| 40 | entities/claude-code-known-issues | 203 | list_item | Thinking summaries 在 Opu | 434 | 434 |
| 41 | entities/claude-code-known-issues | 210 | list_item | 功能請求：送出前檢視並編輯「已貼上文字」區塊內容 | 479 | 479 |
| 42 | entities/claude-code-known-issues | 211 | list_item | Post/PreToolUse Hooks 未如 | 493 | 493 |
| 43 | entities/claude-code-known-issues | 214 | list_item | 升級至 v2.1.1 後 token 消耗異常暴 | 283 | 283 |
| 44 | entities/claude-code-known-issues | 215 | list_item | Extended Thinking「思考內容」實 | 301 | 301 |
| 45 | entities/claude-code-known-issues | 216 | list_item | Explore subagent 固定使用 Ha | 255 | 255 |
| 46 | entities/claude-code-known-issues | 217 | list_item | 記憶過多導致品質退步（2026-06-22 指控 | 205 | 205 |
| 47 | entities/claude-code-known-issues | 230 | list_item | CLAUDE.md 作為 candidate-c | 264 | 264 |
| 48 | entities/claude-code-known-issues | 236 | list_item | Fable 5 advisor（Opus 4.8 | 289 | 289 |
| 49 | entities/claude-code-known-issues | 263 | list_item | 功能請求：跨 session 持久記憶（GitH | 229 | 229 |
| 50 | entities/claude-code-known-issues | 264 | list_item | 提案：開放 compact／session 生命 | 261 | 261 |
| 51 | entities/claude-code-known-issues | 269 | list_item | 對話壓縮（compaction）間歇性失敗或卡死 | 244 | 244 |
| 52 | entities/claude-code-known-issues | 270 | list_item | ✅ 已修復 v2.1.224｜功能請求 | 543 | 543 |
| 53 | entities/claude-code-known-issues | 276 | list_item | Session 歷史 30 天自動刪除（Anth | 548 | 566 |
| 54 | entities/claude-code-known-issues | 283 | list_item | Checkpoint Commits 污染 gi | 231 | 231 |
| 55 | entities/claude-code-known-issues | 291 | list_item | 已付費 Max 帳號登入成功卻因 has_fin | 352 | 352 |
| 56 | entities/claude-code-known-issues | 292 | list_item | Claude Code 要求使用者幾乎每天都須重 | 269 | 269 |
| 57 | entities/claude-code-known-issues | 293 | list_item | 功能請求：多帳號設定檔支援（Multi-Acco | 257 | 257 |
| 58 | entities/claude-code-known-issues | 309 | list_item | MCP OAuth 於 resource 參數尾 | 290 | 290 |
| 59 | entities/claude-code-known-issues | 310 | list_item | Microsoft 365 Connector | 241 | 241 |
| 60 | entities/claude-code-known-issues | 312 | list_item | 排程 routine 對 custom conn | 306 | 306 |
| 61 | entities/claude-code-known-issues | 314 | list_item | 自建 OAuth 2.1 認證 MCP Serv | 242 | 242 |
| 62 | entities/claude-code-known-issues | 354 | list_item | context window 狀態列對 Clau | 236 | 236 |
| 63 | entities/claude-code-known-issues | 355 | list_item | 功能請求：Claude Desktop／Cowo | 382 | 382 |
| 64 | entities/claude-code-known-issues | 357 | list_item | v2.1.113 起原生二進位改依賴 glibc | 295 | 295 |
| 65 | entities/claude-code-known-issues | 364 | list_item | Bedrock：Claude Opus 4.7 | 303 | 303 |
| 66 | entities/claude-code-known-issues | 367 | list_item | Dispatch 主對話持續顯示離線，儘管 Co | 212 | 212 |
| 67 | entities/claude-code-known-issues | 373 | list_item | 工作目錄追蹤暫存檔從未清理，/tmp/claud | 215 | 215 |
| 68 | entities/claude-code-known-issues | 375 | list_item | Cowork Edit/Write 工具因緩衝區 | 253 | 253 |
| 69 | entities/claude-code-known-issues | 381 | list_item | 功能請求：跨機器多 agent 協作（Agent | 288 | 288 |
| 70 | entities/claude-code-known-issues | 382 | list_item | 功能請求：GitLab 整合（儲存庫連接、Mer | 216 | 216 |
| 71 | entities/claude-code-known-issues | 383 | list_item | 功能請求：Linear 整合——指派 issue | 325 | 325 |
| 72 | entities/claude-code-known-issues | 391 | list_item | VSCode 擴充套件 ide_selectio | 206 | 206 |
| 73 | entities/claude-code-known-issues | 394 | list_item | Claude Desktop/Cowork 缺 | 221 | 221 |
| 74 | entities/claude-code-known-issues | 395 | list_item | Windows 11 Pro | 278 | 278 |
| 75 | entities/claude-code-known-issues | 400 | list_item | 功能請求：Claude Code Web 支援從 | 290 | 290 |
| 76 | entities/claude-code-known-issues | 401 | list_item | Cowork VM 在 Windows ARM6 | 299 | 299 |
| 77 | entities/claude-code-known-issues | 403 | list_item | 多起 API 連線錯誤彙整回報（API Erro | 234 | 234 |
| 78 | entities/claude-code-known-issues | 404 | list_item | Cowork 工作區啟動失敗「Failed to | 327 | 327 |
| 79 | entities/claude-code-known-issues | 408 | list_item | claude.exe 列出目錄時（NtQuery | 283 | 283 |
| 80 | entities/claude-code-known-issues | 410 | list_item | Windows Desktop app | 406 | 406 |
| 81 | entities/claude-code-known-issues | 415 | list_item | Linux 上持續產生 Windows 換行（C | 215 | 215 |
| 82 | entities/claude-code-known-issues | 433 | list_item | Cowork 分頁在 Windows 11 de | 214 | 214 |
| 83 | entities/claude-code-known-issues | 436 | list_item | 功能請求聚集：跨平台支援需求未滿足：多項高反應數 | 352 | 352 |
| 84 | entities/claude-code-known-issues | 447 | list_item | Anthropic Status | 391 | 391 |
| 85 | entities/claude-code-known-issues | 449 | list_item | Anthropic Status | 245 | 289 |
| 86 | entities/claude-code-known-issues | 450 | list_item | Anthropic Status | 233 | 261 |
| 87 | entities/claude-code-known-issues | 451 | list_item | OAuth 登入逾時失敗，auth.anthro | 217 | 217 |
| 88 | entities/claude-code-known-issues | 452 | list_item | claude.ai visualize 功能故障 | 242 | 242 |
| 89 | entities/claude-code-known-issues | 454 | list_item | API Error: Connection cl | 316 | 316 |
| 90 | entities/claude-code-known-issues | 455 | list_item | Claude API / Claude Code | 317 | 317 |
| 91 | entities/claude-code-known-issues | 456 | list_item | Anthropic API 大規模 500 In | 217 | 217 |
| 92 | entities/claude-code-known-issues | 463 | list_item | ✅ 已修復 v2.1.64｜CVE-2026-3 | 208 | 208 |
| 93 | entities/claude-code-releases | 144 | table_cell | v2.1.258#c3 | 122 | 122 |
| 94 | entities/claude-code-releases | 147 | table_cell | v2.1.252#c3 | 150 | 150 |
| 95 | entities/claude-code-releases | 148 | table_cell | v2.1.251#c3 | 125 | 125 |
| 96 | entities/claude-code-releases | 153 | table_cell | v2.1.246#c3 | 129 | 129 |
| 97 | entities/claude-code-releases | 156 | table_cell | v2.1.239#c3 | 146 | 146 |
| 98 | entities/claude-code-releases | 162 | table_cell | v2.1.235#c3 | 139 | 139 |
| 99 | entities/claude-code-releases | 163 | table_cell | v2.1.234#c3 | 140 | 140 |
| 100 | entities/claude-code-releases | 165 | table_cell | v2.1.232#c3 | 166 | 166 |
| 101 | entities/claude-code-releases | 167 | table_cell | anthropic-sdk-python v0.#c3 | 122 | 122 |
| 102 | entities/claude-code-releases | 172 | table_cell | anthropic-sdk-python v0.#c3 | 222 | 222 |
| 103 | entities/claude-code-releases | 176 | table_cell | v2.1.223#c3 | 201 | 201 |
| 104 | entities/claude-code-releases | 177 | table_cell | v2.1.222#c3 | 154 | 154 |
| 105 | entities/claude-code-releases | 182 | list_item | 底層 runtime 確認改用 Rust 版 B | 285 | 285 |
| 106 | entities/claude-code-releases | 235 | table_cell | 2026-09-04#c2 | 954 | 954 |
| 107 | entities/claude-code-releases | 236 | table_cell | 2026-09-01#c2 | 681 | 681 |
