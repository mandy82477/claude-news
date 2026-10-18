# 探針記錄：雲端 routine session 讀 GitHub 公開 repo anthropics/claude-code 的權限（2026-10-18）

> 執行者：CLAUDE_NEWS 一次性雲端探針 agent。全程逐字記錄指令與原始輸出，不推論、不修改探針記錄以外的檔案。
> 背景：10-03／10-17 兩次 weekly lint 的 5m／5n 步驟在雲端都因「repository anthropics/claude-code is not configured for this session」與 GH_TOKEN 失效而跳過。本 routine 的 sources 已刻意加上第二個 git_repository（anthropics/claude-code，只 sparse checkout CHANGELOG.md）。

## 步驟 1：工作目錄與同層 repo 目錄

指令與原始輸出：

```
$ pwd; ls; ls .. ; git -C . remote -v
/home/user
total 16
drwxr-xr-x  4 root root 4096 Oct 18 12:43 .
drwxr-xr-x  5 root root 4096 Oct 18 12:43 ..
drwxr-xr-x  3 root root 4096 Oct 18 12:43 claude-code
drwxr-xr-x 14 root root 4096 Oct 18 12:43 claude-news
total 20
drwxr-xr-x  5 root   root   4096 Oct 18 12:43 .
drwxr-xr-x 22 root   root   4096 Oct 18 12:43 ..
drwxr-xr-x  7 claude claude 4096 Oct 18 12:43 claude
drwxr-x---  2 ubuntu ubuntu 4096 Sep 17 02:29 ubuntu
drwxr-xr-x  4 root   root   4096 Oct 18 12:43 user
fatal: not a git repository (or any of the parent directories): .git
```

（`git -C . remote -v` 在 `/home/user` 執行，該層本身不是 git repo，故報錯；第二個 repo 目錄 `claude-code` 確實存在於 `/home/user` 同層，與 `claude-news` 並列。）

切到 `claude-news` repo 內確認自身 remote：

```
$ cd /home/user/claude-news && pwd && ls -la && git remote -v
/home/user/claude-news
total 88
drwxr-xr-x 14 root root  4096 Oct 18 12:43 .
drwxr-xr-x  4 root root  4096 Oct 18 12:43 ..
drwxr-xr-x  9 root root  4096 Oct 18 12:43 .claude
drwxr-xr-x  8 root root  4096 Oct 18 12:43 .git
drwxr-xr-x  3 root root  4096 Oct 18 12:43 .github
-rw-r--r--  1 root root  1843 Oct 18 12:43 .gitignore
-rw-r--r--  1 root root     1 Oct 18 12:43 .nojekyll
-rw-r--r--  1 root root  3992 Oct 18 12:43 CLAUDE.md
-rw-r--r--  1 root root  8562 Oct 18 12:43 README.md
drwxr-xr-x  2 root root  4096 Oct 18 12:43 daily
drwxr-xr-x  4 root root  4096 Oct 18 12:43 data
drwxr-xr-x  7 root root  4096 Oct 18 12:43 docs
drwxr-xr-x  2 root root 12288 Oct 18 12:43 news
drwxr-xr-x  2 root root  4096 Oct 18 12:43 scripts
drwxr-xr-x  7 root root  4096 Oct 18 12:43 src
drwxr-xr-x  6 root root  4096 Oct 18 12:43 web_reader
drwxr-xr-x  2 root root  4096 Oct 18 12:43 weekly
drwxr-xr-x  5 root root  4096 Oct 18 12:43 wiki
origin	https://github.com/mandy82477/claude-news (fetch)
origin	https://github.com/mandy82477/claude-news (push)
```

## 步驟 2：`gh auth status` 與 token 環境變數

指令與原始輸出：

```
$ gh auth status 2>&1; echo GH_TOKEN_set=${GH_TOKEN:+yes} GITHUB_TOKEN_set=${GITHUB_TOKEN:+yes}
github.com
  X Failed to log in to github.com using token (GH_TOKEN)
  - Active account: true
  - The token in GH_TOKEN is invalid.
GH_TOKEN_set=yes GITHUB_TOKEN_set=yes
```

## 步驟 3：`gh issue view` 讀 anthropics/claude-code#41930

指令與原始輸出：

```
$ gh issue view 41930 -R anthropics/claude-code --json number,state 2>&1
HTTP 403: GitHub GraphQL is not available from Claude Code sessions; use the REST API (gh api repos/{owner}/{repo}/...). For review threads, auto-merge, and draft/ready-for-review use the CCR routes on api.github.com: GET /repos/{owner}/{repo}/pulls/{n}/ccr/review_threads, POST /repos/{owner}/{repo}/pulls/{n}/ccr/comments/{comment_id}/resolve (or /unresolve), PUT or DELETE /repos/{owner}/{repo}/pulls/{n}/ccr/auto_merge, POST /repos/{owner}/{repo}/pulls/{n}/ccr/ready_for_review, POST /repos/{owner}/{repo}/pulls/{n}/ccr/convert_to_draft. (https://api.github.com/graphql)
```

（`gh issue view` 走 GraphQL，被雲端環境擋下，與 `gh auth status` 報的 GH_TOKEN 失效並非同一個錯——這裡是環境層擋 GraphQL，不是認證失敗。）

## 步驟 4：`gh api` 讀 CHANGELOG.md 原文

指令與原始輸出：

```
$ gh api repos/anthropics/claude-code/contents/CHANGELOG.md -H "Accept: application/vnd.github.raw" 2>&1 | head -5
# Changelog

## 2.1.302

- Added `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the model the client-side auto mode classifier uses; it does not change the model for server-side auto mode
```

（`gh api` 走 REST，成功回傳。即便步驟 2 顯示 `GH_TOKEN` 對 `gh auth status` 的登入檢查無效，REST 呼叫本身仍成功——實際認證路徑與 `gh auth status` 檢查的不是同一條。）

## 步驟 5：匿名 REST（curl，無 token）讀 issue

指令與原始輸出：

```
$ curl -sS -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/anthropics/claude-code/issues/41930 2>&1
200
```

## 步驟 6：匿名 raw.githubusercontent.com 讀 CHANGELOG.md

指令與原始輸出：

```
$ curl -sS -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md 2>&1
200
```

## 步驟 7：第二個 source（sparse checkout 的 anthropics/claude-code）

指令與原始輸出：

```
$ ls -la /home/user/claude-code
total 12128
drwxr-xr-x 3 root root     4096 Oct 18 12:43 .
drwxr-xr-x 4 root root     4096 Oct 18 12:43 ..
drwxr-xr-x 8 root root     4096 Oct 18 12:43 .git
-rw-r--r-- 1 root root       35 Oct 18 12:43 .gitattributes
-rw-r--r-- 1 root root       11 Oct 18 12:43 .gitignore
-rw-r--r-- 1 root root  1046331 Oct 18 12:43 CHANGELOG.md
-rw-r--r-- 1 root root     2218 Oct 18 12:43 CLAUDE.md
-rw-r--r-- 1 root root      150 Oct 18 12:43 LICENSE.md
-rw-r--r-- 1 root root     2873 Oct 18 12:43 README.md
-rw-r--r-- 1 root root      674 Oct 18 12:43 SECURITY.md
-rw-r--r-- 1 root root 11002760 Oct 18 12:43 demo.gif
-rw-r--r-- 1 root root   325809 Oct 18 12:43 feed.xml

$ head -3 /home/user/claude-code/CHANGELOG.md
# Changelog

## 2.1.302

$ git -C /home/user/claude-code log -1 --format=%h_%ad
dd6bee3_Sat Oct 17 23:14:49 2026 +0000
```

（第二個 source **已經被 clone 進來**，路徑為 `/home/user/claude-code`，與 `claude-news` 並列於 `/home/user` 之下。注意：目錄裡不只有 `CHANGELOG.md`，還有 `.gitattributes`、`.gitignore`、`CLAUDE.md`、`LICENSE.md`、`README.md`、`SECURITY.md`、`demo.gif`、`feed.xml`——並非純粹只有 sparse checkout 設定要求的 `CHANGELOG.md` 一個檔案。）

## 步驟 8：ToolSearch 查 GitHub MCP 工具，並實際呼叫

指令：`ToolSearch(query="+github issue", max_results=10)`

結果：**命中多個 `mcp__github__*` 工具**，包括 `mcp__github__issue_read`、`mcp__github__add_issue_comment`、`mcp__github__issue_write`、`mcp__github__sub_issue_write`、`mcp__github__list_issue_fields`、`mcp__github__list_issue_types`、`mcp__github__update_issue_comment`、`mcp__github__list_issues`、`mcp__github__search_issues`、`mcp__github__actions_get` 等，schema 完整載入。

實際呼叫其中一個唯讀工具：

```
mcp__github__issue_read({ method: "get", owner: "anthropics", repo: "claude-code", issue_number: 41930 })
```

回傳原文（節錄關鍵欄位，完整 body 過長從略）：

```json
{
  "number": 41930,
  "title": "[BUG] Critical: Widespread abnormal usage limit drain across all paid tiers since March 23, 2026 — multiple root causes identified, no formal communication issued",
  "state": "closed",
  "state_reason": "completed",
  "locked": true,
  "html_url": "https://github.com/anthropics/claude-code/issues/41930",
  "user": {"login": "marcuspuchalla", "id": 89977979},
  "author_association": "NONE",
  "labels": ["bug"],
  "assignees": [],
  "comments": 108,
  "reactions": {"total_count": 97, "+1": 85},
  "created_at": "2026-04-01T09:54:32Z",
  "updated_at": "2026-04-24T00:58:51Z",
  "closed_at": "2026-04-24T00:58:47Z",
  "closed_by": "bcherny"
}
```

呼叫**成功**，無錯誤訊息，回傳完整 issue JSON（含 body、標籤、reactions、closed_by 等）。

## 結論

- (a) `gh` 對 anthropics/claude-code：**部分可用**——`gh auth status` 回報 GH_TOKEN 失效，`gh issue view`（走 GraphQL）被環境擋下回 403；但 `gh api repos/.../contents/...`（走 REST）成功讀到 CHANGELOG.md 內容，顯示失敗點是 GraphQL 路徑與 `gh auth status` 的登入檢查，不是全面無權限。
- (b) 匿名 REST／raw 皆可用：`api.github.com/repos/anthropics/claude-code/issues/41930` → HTTP 200；`raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` → HTTP 200。
- (c) 第二個 source **已 clone 進來**，在 `/home/user/claude-code`（與 `claude-news` 同層），且 `mcp__github__issue_read` 透過 GitHub MCP 工具成功讀到 issue 41930 完整內容，無錯誤。
