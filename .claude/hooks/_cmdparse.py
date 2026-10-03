"""
PreToolUse hook 共用的指令切段與 git 呼叫解析（不是 hook，本身不掛 settings）。

為什麼要共用一份：舊版 `block_git_add_all.py` 用一條 regex 看 `git add` 之後的字面，
`git add ./`、`git add "."`、`git -c a=b add .` 全部從縫裡過去（2026-10-03 盤點實測）。
引號、全域旗標、`bash -c "…"` 包一層——這些是「寫法」問題，不是「規則」問題，
每支 hook 各寫一次就會各漏一次。

射程（誠實標明）：這是靜態字面解析，擋得住手寫的變體，擋不住刻意繞道——
git alias、把指令寫進腳本再執行、變數展開（`$CMD`）都看不到。hook 的目標是
「不小心違規時一定被攔」，不是對抗惡意。
"""
from __future__ import annotations

import re
import shlex

# heredoc 本文與 PowerShell here-string 是資料（多半是 commit 訊息），先整段拿掉，
# 否則訊息裡寫「git add ./ 現在會被擋」那一行會被當成指令。
_HEREDOC_RE = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n.*?\n[ \t]*\2[ \t]*(?=\n|$)", re.S)
_HERESTRING_RE = re.compile(r"@(['\"])\r?\n.*?\r?\n\1@", re.S)


def split_segments(command: str) -> list[str]:
    """引號感知的切段：`;` `&&` `||` `|` `&` 換行 `$(` 反引號 `(` `)` 只在引號外才算分隔。

    雙引號內的 `$(…)` 在 bash 裡其實會執行，這裡刻意不展開——換來的是
    `git commit -m "fix; 之後再 git stash"` 這種訊息不會被誤擋。
    """
    command = _HEREDOC_RE.sub("", command)
    command = _HERESTRING_RE.sub("''", command)
    segs, buf, q = [], [], None
    i, n = 0, len(command)
    while i < n:
        c = command[i]
        if q:
            buf.append(c)
            if c == q:
                q = None
            elif c == "\\" and q == '"' and i + 1 < n:
                buf.append(command[i + 1])
                i += 1
            i += 1
            continue
        if c in "'\"":
            q = c
            buf.append(c)
            i += 1
            continue
        two = command[i:i + 2]
        if two in ("&&", "||", "$("):
            segs.append("".join(buf)); buf = []
            i += 2
            continue
        if c == "&" and (command[i - 1:i] in (">",) or command[i + 1:i + 2] == ">"):
            buf.append(c)  # 2>&1、&> 是重導向不是分隔
            i += 1
            continue
        if c in ";|\n`()&":
            segs.append("".join(buf)); buf = []
            i += 1
            continue
        buf.append(c)
        i += 1
    segs.append("".join(buf))
    return [s for s in segs if s.strip()]

# 指令起點可能出現的前綴詞：跳過它們才看得到真正的程式名
_PREFIX_WORDS = {
    "sudo", "env", "command", "exec", "nohup", "time", "then", "do", "else",
    "if", "while", "until", "!", "{", "call", "start", "noglob",
}
_ENV_ASSIGN_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
_PS_ENV_RE = re.compile(r"^\$env:[A-Za-z_][A-Za-z0-9_]*$", re.I)

# 會把後面的字串當指令再執行一次的殼：遞迴掃描
_SHELLS = {"bash", "sh", "zsh", "dash", "powershell", "pwsh", "cmd", "bash.exe",
           "sh.exe", "powershell.exe", "pwsh.exe", "cmd.exe"}
_SHELL_CMD_FLAGS = {"-c", "-command", "/c", "/k", "-encodedcommand"}

# git 全域旗標：吃一個引數的
_GIT_GLOBAL_WITH_ARG = {"-C", "-c", "--git-dir", "--work-tree", "--namespace",
                        "--exec-path", "--super-prefix", "--config-env"}


_LONE_BACKSLASH_RE = re.compile(r"\\(?![\"'\\$`\n])")


def _tokenize(segment: str) -> list[str]:
    # Windows 路徑的反斜線（`D:\work\repo`）在 POSIX shlex 會被當跳脫字元吃掉；
    # 只保留它跳脫引號／錢號／反引號的用途，其餘一律當字面。
    segment = _LONE_BACKSLASH_RE.sub(r"\\\\", segment)
    try:
        return shlex.split(segment, posix=True)
    except ValueError:
        # 引號沒閉合（例如字串跨段被切開）：退回空白切分，盡力而為
        return [t.strip("'\"") for t in segment.split()]


def basename(prog: str) -> str:
    p = prog.replace("\\", "/").rsplit("/", 1)[-1].lower()
    return p


def iter_commands(command: str, _depth: int = 0):
    """逐一產出每個簡單指令的 token 列（已跳過前綴詞與環境變數指派）。

    `bash -c "…"`／`powershell -Command "…"`／`cmd /c …` 會遞迴展開，
    裡面的指令同樣產出。
    """
    if not isinstance(command, str) or _depth > 3:
        return
    for seg in split_segments(command):
        toks = _tokenize(seg)
        i = 0
        while i < len(toks):
            t = toks[i]
            if t.lower() in _PREFIX_WORDS or _ENV_ASSIGN_RE.match(t):
                i += 1
                continue
            if _PS_ENV_RE.match(t) and i + 2 < len(toks) and toks[i + 1] == "=":
                i += 3
                continue
            break
        toks = toks[i:]
        if not toks:
            continue
        yield toks
        if basename(toks[0]) in _SHELLS:
            for j, a in enumerate(toks[1:], start=1):
                if a.lower() in _SHELL_CMD_FLAGS and j + 1 < len(toks):
                    yield from iter_commands(" ".join(toks[j + 1:]), _depth + 1)
                    break


class GitCall:
    """一次 git 呼叫：全域 `-c` 設定、子指令、子指令引數。"""

    def __init__(self, configs: list[str], sub: str, args: list[str]):
        self.configs = configs
        self.sub = sub
        self.args = args

    def __repr__(self) -> str:  # 測試失敗時好讀
        return f"GitCall(sub={self.sub!r}, args={self.args!r}, configs={self.configs!r})"

    def flags(self) -> list[str]:
        return [a for a in self.args if a.startswith("-") and a != "--"]

    def has_flag(self, *names: str) -> bool:
        """長旗標精確比對（含 `--x=v`）；單字母旗標也認合併寫法（`-am` 含 `-a`）。"""
        for a in self.args:
            if a == "--":
                break
            for n in names:
                if n.startswith("--"):
                    if a == n or a.startswith(n + "="):
                        return True
                elif len(n) == 2 and a.startswith("-") and not a.startswith("--"):
                    if n[1] in a[1:]:
                        return True
        return False

    def positionals(self) -> list[str]:
        """非旗標引數（`--` 之後全部算）。吃引數的旗標由呼叫端自行處理。"""
        out, after = [], False
        for a in self.args:
            if after:
                out.append(a)
            elif a == "--":
                after = True
            elif not a.startswith("-"):
                out.append(a)
        return out


def iter_git(command: str):
    for toks in iter_commands(command):
        if basename(toks[0]) not in ("git", "git.exe"):
            continue
        i, configs = 1, []
        while i < len(toks):
            t = toks[i]
            if t in _GIT_GLOBAL_WITH_ARG:
                if t == "-c" and i + 1 < len(toks):
                    configs.append(toks[i + 1])
                i += 2
                continue
            if t.startswith("--") and "=" in t and t.split("=", 1)[0] in _GIT_GLOBAL_WITH_ARG:
                i += 1
                continue
            if t.startswith("-"):
                i += 1
                continue
            break
        if i >= len(toks):
            continue
        yield GitCall(configs, toks[i].lower(), toks[i + 1:])


# 等同「整棵樹」的 pathspec
WHOLE_TREE = {".", "./", ":/", ":/*", "*", ":", ":/.", ".\\", "./*", ":(top)", ":(glob)**"}


def is_whole_tree_spec(spec: str) -> bool:
    s = spec.strip()
    return s in WHOLE_TREE or s in {"..", "../", "..\\"}
