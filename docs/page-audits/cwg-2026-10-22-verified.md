# 第 19 波主編查證：topics/coding-workflow-guide（2026-10-22）

> 方法：官方文件以 `.md` 原文直取（`https://code.claude.com/docs/en/<頁>.md`），全部 2026-10-22 取得；原檔存 scratchpad `w19v/`。行號：頁面＝現檔；官方＝原文 `.md` 行號。

## 給設計者三句

1. **頁面有一條結論已被官方推翻**：「skill 描述清單 compact 後不重載」（L218、L541、L631「目前結論」第三條）——官方 context-window 表現寫 **Rebuilt … and re-injected. Requires Claude Code v2.1.304 or later**。結論層要改，不只是改一句。
2. **「官方文件 185 頁、llms.txt 原文已失效」兩處都錯**：llms.txt 現可取得，`docs/en/` 頁 264 條。這種會一直變的數字不該進正文。
3. Q1–Q4 四題的官方錨句都找得到且頁面引用大致逐字正確；Code Review 官方已拆成 7 頁（含 `code-review-costs`、`code-review-local`、`code-review-customize`），頁面第 5 段引用的「Length has a cost」「round seven」兩句**現行官方頁查無**。

## 頁面數字／斷言對官方

| 頁面行 | 頁面說法 | 官方原文（逐字） | 出處 | 判定 |
|---|---|---|---|---|
| L218、L541、L631 | skill 描述清單 compact 後不重載 | 「Skill descriptions \| Rebuilt from your current skills and re-injected. Requires Claude Code v2.1.304 or later」 | context-window.md L29 | ❌ 過期（v2.1.304 起改變） |
| L214 | `paths:` 規則 compact 後消失；要跨 compact 就拿掉 `paths:` | 「Rules with `paths:` frontmatter \| Claude Code reloads them on demand」；「If a rule must persist across compaction, drop the `paths:` frontmatter」 | context-window.md L32、L42 | ⚠️ 半對：會「依需重載」（碰到檔就回來），不是永久消失；拿掉 `paths:` 的建議仍在 |
| L599、L663 | 官方文件共 185 頁；llms.txt 原文已失效 | llms.txt 可取得，`code.claude.com/docs/en/` 條目 264 | llms.txt | ❌ 兩處皆錯 |
| L173 | `features-overview` 與 `claude-directory` 給「200 行以內」，引「Longer files still load in full but may reduce adherence」 | features-overview：「Keep CLAUDE.md under 200 lines」；memory：「target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence」 | features-overview.md L110、L251；memory.md L88 | ⚠️ 數字對；出處錯（claude-directory 查無，應為 memory）；引句非逐字 |
| L174 | 「Would removing this cause Claude to make mistakes?」「Bloated CLAUDE.md files cause Claude to ignore your actual instructions!」 | 同左逐字 | best-practices.md L170 | ✅ |
| L180–189 | Build your setup over time：錯兩次→CLAUDE.md、貼第三次→skill、「A repeated mistake or a recurring review comment is a CLAUDE.md edit…」 | 同左逐字 | features-overview.md L53、L59、L62、L69 | ✅ |
| L131 | v2.1.277 起無 CLAUDE.md 時原生讀 AGENTS.md；`/config`「Project instructions」可調；**尚未支援 Bedrock、Vertex、Foundry** | 「Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later」；不支援情形列三種：v2.1.277 前、停用內建 plugin、升級後第一個 session | memory.md L350–369、L411–417 | ⚠️ 版本與設定對；「Bedrock／Vertex／Foundry 不支援」現行官方查無 |
| L200 | auto memory `MEMORY.md` 前 200 行／25KB | 「Every session (first 200 lines or 25KB)」 | memory.md L31 | ✅ |
| L257 | Explore：模型繼承主對話、在 Claude API 上以 Opus 為上限 | 「Model: the main conversation's model. When the main conversation runs Fable, … Explore runs on the Opus model that the `opus` alias resolves to」 | sub-agents.md L39–41 | ⚠️ 「Opus 上限」只在主對話是 Fable 時成立；Bedrock 等平台仍跟主對話 |
| L257 | thoroughness 三段 quick／medium／very thorough | 同左 | sub-agents.md L49 | ✅ |
| L355、L357、L359 | 「If you could describe the diff in one sentence, skip the plan.」等三句 | 同左逐字 | best-practices.md L103、L107 | ✅ |
| L367、L369 | 規格 self-contained 判準、「Time spent making the spec precise pays off…」 | 同左逐字 | best-practices.md L351 | ✅ |
| L397、L400 | security-guidance 三層、≤30 檔、連續 3 次、每小時 ≤20、預設 Opus 4.7、8KB、「None of the layers block writes or commits」 | 同左 | security-guidance.md L61、L96、L102、L108、L166、L172 | ✅（≤50 條未逐條核） |
| L421 | `/review` 是 `/code-review` 別名；v2.1.147 前叫 `/simplify` | 「`/review` is an alias of `/code-review`. Before v2.1.223, `/review` was a separate command…」 | code-review-local.md L17 | ⚠️ 別名對；改名史官方現行頁只講 v2.1.223，v2.1.147／154 那段查無 |
| L426、L432 | ultrareview Pro/Max 各 3 次免費、一次性不 refresh、之後 $5–25 | 「3 free runs」「one-time allotment per account and don't refresh」「typically $5 to $25 in usage credits」 | ultrareview.md L119–125 | ✅ |
| L427 | Code Review 按 token 走 usage credits、無固定單價 | 「has no flat per-review price」「billed on token usage through usage credits」 | code-review-costs.md L9、L16 | ✅ |
| L427（缺） | 頁面沒寫 Code Review 限方案 | 「For Team and Enterprise plans」 | code-review.md L7 | ⚠️ 缺：冷讀者 Q3 卡點 |
| L432 | $13／開發者／活躍日、$150–250／月 | 「around $13 per developer per active day and $150-250 per developer per month」 | costs.md L11 | ✅ |
| L434 | 觸發模式 Manual／Once、「Reviewing on every push runs the most reviews and costs the most」 | 三種 Review runs；「After every push: runs on each push, multiplying cost by the number of pushes」 | code-review-costs.md L22–27 | ⚠️ 事實對、引句非現行逐字 |
| L434、L436 | 「stops a one-line fix from reaching round seven…」「Length has a cost: a long REVIEW.md dilutes…」 | 現行 7 頁 code-review 系列全文 grep 零命中 | code-review*.md | ❓ 查無（可能已改寫）；不可再標逐字引用 |
| L440 | 本機 `/code-review` 不讀 REVIEW.md，只跟 CLAUDE.md | 「the review follows your `CLAUDE.md` … It doesn't read `REVIEW.md`」 | code-review-local.md L65；customize.md L47 | ✅（官方現已明寫，「官方沒標的坑」措辭過期） |
| L438 | `--max-findings <n>\|all` 自 v2.1.288 | 「`--max-findings <n>`, `--max-findings all`, or `--max-findings default`」 | code-review-local.md L83 | ✅（多一個 `default`） |
| L460 | 「Claude stops when the work looks done…」 | 同左逐字 | best-practices.md L33 | ✅ |
| L466 | Stop hook 連續擋 8 次後強制結束、查 `stop_hook_active` | 「8-consecutive-continuation cap … ends the turn」 | hooks.md L2718–2720 | ✅ |
| L469 | `/goal` 條件上限 4,000 字元、「or stop after 20 turns」 | 同左 | goal.md L64、L66 | ✅ |
| L502 | `SessionEnd` 所有 hook 共用 1.5 秒（可拉到 60 秒） | 「default timeout of 1.5 seconds」；per-hook `timeout` 使整體預算上調「up to 60 seconds」；或 env var | hooks.md L3555–3566 | ✅ |
| L547 | 「Have Claude show evidence rather than asserting success…」 | 同左逐字 | best-practices.md L52 | ✅ |
| L543 | trust-then-verify gap、「If you can't verify it, don't ship it.」 | 同左 | best-practices.md L556–557 | ✅ |

## 考題的官方錨句

| 題 | 錨句 | 出處 |
|---|---|---|
| Q1 CLAUDE.md 放什麼、多長、何時加 | include／exclude 表；「target under 200 lines per CLAUDE.md file」；「Claude gets a convention or command wrong twice → Add it to CLAUDE.md」 | best-practices.md L170–179；memory.md L88；features-overview.md L59 |
| Q2 怎麼讓它自己驗證 | 「Without a check it can run, "looks done" is the only signal available」；「Have Claude show evidence rather than asserting success」；`/goal`、Stop hook | best-practices.md L33、L52；goal.md；hooks.md L2720 |
| Q3 review 入口與價錢 | 本機 `/code-review` 算一般用量；ultrareview 3 次免費後 $5–25；Code Review（GitHub）**限 Team／Enterprise**、無單價、按 token、可設月上限 | code-review-local.md；ultrareview.md L119–125；code-review.md L7；code-review-costs.md |
| Q4 先規劃還是直接做 | 「If you could describe the diff in one sentence, skip the plan.」「when the change modifies multiple files」；大功能先 interview 寫 spec | best-practices.md L107、L315、L351 |

## 逾期懸置

頁面 frontmatter `pending_count: 0`；`check_pending_markers.py` exit 0。無逾期懸置。
