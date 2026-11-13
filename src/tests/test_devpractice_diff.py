# -*- coding: utf-8 -*-
"""devpractice_diff.py 的迴歸測試。

真實踩過的坑（2026-09-02 首跑）：
- repo root 在 CLAUDE_NEWS 上一層，diff 標頭是 `CLAUDE_NEWS/wiki/log.md`，
  EXCLUDE 用相等比對永遠不命中 → 編輯部日誌混進候選訊號。
- 基準線退回不可用 reflog（HEAD@{...}）——雲端 fresh clone 的 reflog 是空的。
"""
import importlib.util
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "devpractice_diff.py"

spec = importlib.util.spec_from_file_location("devpractice_diff", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TestExclude(unittest.TestCase):
    def test_exclude_matches_prefixed_paths(self):
        """log.md / index.md 即使帶 repo 前綴也要被排除。"""
        for e in mod.EXCLUDE:
            self.assertTrue(f"CLAUDE_NEWS/{e}".endswith(e))
        src = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("endswith", src, "排除比對必須用 endswith（diff 路徑帶 repo 前綴）")

    def test_no_reflog_syntax(self):
        """雲端 fresh clone 的 reflog 是空的，禁用 HEAD@{...} 語法。"""
        src = SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn("HEAD@{", src)


class TestStateRoundtrip(unittest.TestCase):
    def test_base_sha_fallback_on_bad_state(self):
        """狀態檔壞掉（非 JSON／sha 不存在）→ 退回 fallback，不炸。
        固定視為完整 clone：本測試驗壞狀態檔的處理，淺 clone 分支由 TestShallowClone 驗；
        不固定的話雲端淺 clone 會走 fallback-shallow-*，結果隨執行環境而變。"""
        orig = mod.STATE
        orig_shallow = mod._is_shallow
        mod._is_shallow = lambda: False
        try:
            mod.STATE = ROOT / "data" / "_devpractice_state_test.json"
            mod.STATE.write_text("not json", encoding="utf-8")
            sha, origin = mod._base_sha()
            self.assertEqual(origin, "fallback-48h")
            mod.STATE.write_text(json.dumps({"last_sha": "0" * 40}), encoding="utf-8")
            sha, origin = mod._base_sha()
            self.assertEqual(origin, "fallback-48h")
        finally:
            if mod.STATE.exists():
                mod.STATE.unlink()
            mod.STATE = orig
            mod._is_shallow = orig_shallow

    def test_cli_show_runs(self):
        """show 在真 repo 上跑得動且 exit 0（有無新增皆為正常結果）。"""
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "show"], cwd=ROOT,
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("基準線：", r.stdout)
        # 編輯部日誌不得出現在輸出的檔案分組標題裡
        self.assertNotRegex(r.stdout, re.compile(r"^## .*wiki/log\.md", re.M))


def _run(cwd, *args, env=None):
    return subprocess.run(
        list(args), cwd=cwd, capture_output=True, text=True, encoding="utf-8",
        errors="replace", env=env,
    )


class TestShallowClone(unittest.TestCase):
    """雲端容器淺 clone：狀態檔 sha 不在本地時不得 exit 1、不得靜默換基準。"""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="dpdiff_"))
        cls.origin = cls.tmp / "origin"
        cls.origin.mkdir()
        git = lambda *a, **k: _run(cls.origin, "git", *a, **k)
        git("init", "-q")
        git("config", "user.email", "t@t")
        git("config", "user.name", "t")
        (cls.origin / "wiki").mkdir()
        cls.shas, cls.dates = [], []
        base = 1_700_000_000
        for i in range(6):
            (cls.origin / "wiki" / "a.md").write_text(
                "".join(f"line {j}\n" for j in range(i + 1)), encoding="utf-8")
            git("add", "-A")
            ts = base + i * 5 * 86400  # 每個 commit 相隔 5 天
            env = dict(os.environ, GIT_AUTHOR_DATE=f"{ts} +0000", GIT_COMMITTER_DATE=f"{ts} +0000")
            git("commit", "-q", "-m", f"c{i}", env=env)
            cls.shas.append(git("rev-parse", "HEAD").stdout.strip())
            cls.dates.append(ts)

    @classmethod
    def tearDownClass(cls):
        def _rm(f, p, e):
            os.chmod(p, 0o700)
            f(p)
        shutil.rmtree(cls.tmp, onerror=_rm)

    def _clone(self, name):
        dst = self.tmp / name
        _run(self.tmp, "git", "clone", "-q", "--depth=1", self.origin.as_uri(), str(dst))
        (dst / "scripts").mkdir()
        shutil.copy(SCRIPT, dst / "scripts" / "devpractice_diff.py")
        return dst

    def _state(self, clone, sha, ts):
        (clone / "data").mkdir(exist_ok=True)
        upd = datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        (clone / "data" / "devpractice_state.json").write_text(
            json.dumps({"last_sha": sha, "updated": upd}), encoding="utf-8")

    def _show(self, clone):
        return _run(clone, sys.executable, "scripts/devpractice_diff.py", "show")

    def test_state_sha_recovered_by_deepening(self):
        """sha 在 origin 歷史裡 → 補歷史取回，基準仍是狀態檔那顆，無降級警告。"""
        clone = self._clone("c1")
        self._state(clone, self.shas[2], self.dates[2])
        r = self._show(clone)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"基準線：{self.shas[2][:10]}（state-fetched）", r.stdout)
        self.assertNotIn("降級", r.stdout)
        self.assertIn("line 5", r.stdout)  # c2..HEAD 的新增行都在

    def test_unrecoverable_sha_degrades_loudly(self):
        """sha 補不到 → 不 exit 1；退到本 clone 可用的基準並印明確警告。"""
        clone = self._clone("c2")
        self._state(clone, "0" * 40, self.dates[3])
        r = self._show(clone)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("基準線被降級", r.stdout)
        self.assertIn("fallback-shallow", r.stdout)
        self.assertNotIn("找不到基準", r.stdout)

    def test_missing_state_file_in_shallow(self):
        """狀態檔不存在（全新雲端）→ 同樣不 exit 1。"""
        clone = self._clone("c3")
        r = self._show(clone)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("基準線被降級", r.stdout)


if __name__ == "__main__":
    unittest.main()
