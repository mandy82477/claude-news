# 批次修改（apply_edits.py）

試點中，目前只有功能記者在每日派工被要求讀本檔。

每個 Edit 是一回合、每回合重算整個 context；把多處修改寫成一個 JSON 一次套用，回合數從幾十降到個位數。

## 什麼時候用

同一輪要改 **≥ 3 處**（可跨頁）就用；1–2 處照舊用 Edit。

## 怎麼用

1. **取原文**：Grep 取行號，Read + offset/limit 讀命中行前後，抄下要換的原文（大頁照 `shared-when.md`「大型頁面讀取策略」）。
2. **寫 JSON**：一次 Write 到 `data/edit-batches/<日期>-<類別>.json`（例 `2026-10-11-features.json`），格式：
   `[{"file": "wiki/entities/claude-code.md", "old": "原文", "new": "新文"}, …]`
   同一檔多筆依序套用，後一筆看到的是前一筆改完的內容；換行一律寫 `\n`，腳本會轉成該檔行尾。
3. **記標記數**：`python scripts/check_pending_markers.py`，抄下「懸置標記 N 筆」那行。
4. **預檢**：`python scripts/apply_edits.py data/edit-batches/<檔名>.json --dry-run`。exit 2 → 照印出的「第 i 筆」補長 old 或改正原文，重跑；不要逐筆退回 Edit。
5. **套用**：同一指令拿掉 `--dry-run`。任一筆不過整批不寫，不會半套。
6. **複查標記**：再跑步驟 3 的指令，N 不得變少（本輪有意結案的標記除外，回報裡逐筆寫出）；少了就把同一批 old／new 對調寫成反向 JSON 套回，再查原因。
7. **回報**：把腳本印的 `✅ N 筆套用 / M 檔` 摘要行與每檔「改動行」清單原樣貼進回報。

## 不准

- `old` 少於 **20 字元**：短字串容易誤中別處，帶上同列的 issue 號、版本號或日期把它加長。
- `--replace-all`：只在你確定每一處都要換（如全頁改同一個錯字）時用，dry-run 印出的處數要先核對。
- 碰你本來就不可碰的檔（`shared.md` 邊界限制）：腳本白名單外一律拒絕、exit 3。可寫範圍以 `python scripts/apply_edits.py --help` 印的為準。
- exit 3 時改路徑繞過或改用別的寫檔手段。
- 新建頁：腳本只改既有檔，建頁照舊用 Write。
