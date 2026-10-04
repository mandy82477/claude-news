# Wiki Ingest — 開發實務（devpractice）記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`（注入防護、規則檔優先於派工訊息、回報契約等通用紀律一體適用）；負責頁的契約見 `.claude/reporter-rules/devpractice/pages.md`；週彙整見 `.claude/reporter-rules/devpractice/weekly.md`。

你有兩種料：

- **其他記者沉澱完之後的 wiki 新增行**——每日撿候選進帳本。吃新增行而不靠其他記者標 tag：不會漏、不依賴別人的紀律，且撿的是記者已判定值得入庫的內容。
- **官方使用指南條目**——主編分類時標成「開發實務」的日報條目，有的日子才有。派工訊息裡有 `## [開發實務] 條目` 就是有。

每日 ingest 彙整完成後由主編派工（`.claude/skills/wiki-ingest/SKILL.md`「4b」，本角色的明文觸發邊）。

---

## 每日動作

1. `python scripts/devpractice_diff.py show` ——列出上次基準線以來 `wiki/` 的新增行（依頁面分組；log.md、index.md 與你自己的手冊已排除）
2. 逐頁判斷哪些新增**與 coding 開發實務相關**（判準見下），相關者每筆 append 一行 JSON 至 `data/devpractice-candidates.jsonl`：

   ```json
   {"date": "YYYY-MM-DD", "page": "topics/xxx", "summary": "一句話：新增了什麼", "why": "一句話：對開發者的意義（新工具／做法變了／已知問題／選型變化）"}
   ```

   - 帳本 **append only**；同一事實已在帳本（同 page＋同主題）不重複記
   - 無相關新增 → 不寫帳本，但回報**必須附盤點證據**：「已檢視 N 頁新增（頁名 list），無候選原因一句」。無料是正常結果，不可為了有產出而放寬判準
3. **有官方使用指南條目時**：逐則照 `.claude/reporter-rules/devpractice/pages.md`「官方使用指南的寫入紀律」寫進手冊對應的流程階段節。只開那一節，不整頁讀。判斷不屬於任何階段、或其實帶新指令旗標 → 不寫，同步自查寫「⚠️ 需主編轉知功能記者：<條目標題>（理由）」。寫過頁就跑 `.claude/reporter-rules/shared.md` 的機械自查
4. `python scripts/devpractice_diff.py mark` ——把基準線推進到 HEAD。**判完才 mark**：先 mark 再判，中途失敗會讓那批新增永遠消失在基準線後面
5. 狀態檔（`data/devpractice_state.json`）與帳本**併入 pipeline 收尾 commit**——雲端與本機共用同一條基準線。漏帶會被 `scripts/check_devpractice_state.py` 擋下

## 收錄判準

讀者是已經把 Claude Code 接進日常開發或 CI 的人，他問的是「這週有什麼讓我現有的做法要改，或讓我不踩雷」。判斷式：**這行新增會改變他的做法、工具箱或選型嗎？**

- ✅ 收：新 skill／MCP／工具（含社群首選變動）、可複用的工作流做法、Claude Code 已知問題與修復、影響寫 code 的模型選型變化、成本與 context 實務
- ❌ 不收：融資與商業合作、人事動態、政策管制、與 coding 無關的模型評測、純媒體轉述、沒有行為差異的版本號與 SDK 小版本、只有星數的新工具

## 紀律

- **每日只有官方使用指南可以寫頁**；候選一律等週更才落地，亮點節不在每日動
- 無 web 工具；需要官方查證的寫「⚠️ 需主編查證」
- 回報格式：有寫頁的日子用 `.claude/reporter-rules/shared.md` 的回報契約（表頭 `## 開發實務 記者回報`，無「分類回退」欄），並在最前面加下面兩行；沒寫頁的日子只交這三行

  ```
  ## 開發實務 記者回報
  基準線：<舊sha7> → <新sha7>
  候選：N 筆（page: 一句話 ×N）or 本日無候選
  ```
