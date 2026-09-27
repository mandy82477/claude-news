# -*- coding: utf-8 -*-
"""resolve_append_only.py：白名單契約＋union 合併行為（用臨時 git repo 實測，不碰本庫）。"""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "resolve_append_only.py"
spec = importlib.util.spec_from_file_location("rao", SCRIPT)
rao = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rao)


class TestWhitelist(unittest.TestCase):
    def test_only_append_only_files(self):
        """白名單裡不得出現會被改寫既有行的檔（index/頁面/設定）。"""
        for p in rao.APPEND_ONLY:
            self.assertTrue(p.endswith((".md", ".jsonl", ".log")), p)
            self.assertNotIn("index.md", p)
            self.assertNotIn("topics/", p)
            self.assertNotIn("entities/", p)
        self.assertIn("wiki/log.md", rao.APPEND_ONLY)
        self.assertNotIn("src/news_aggregator/emitted_items.json", rao.APPEND_ONLY)


class TestUnionMerge(unittest.TestCase):
    def _git(self, cwd, *args):
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", check=True)

    def test_union_keeps_both_appends_in_order(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            g = lambda *a: self._git(d, *a)
            g("init", "-q", "-b", "master")
            g("config", "user.email", "t@t"); g("config", "user.name", "t")
            f = d / "log.md"
            f.write_text("## base\n", encoding="utf-8"); g("add", "."); g("commit", "-qm", "base")
            g("checkout", "-qb", "cloud")
            f.write_text("## base\n## cloud-append\n", encoding="utf-8"); g("commit", "-qam", "cloud")
            g("checkout", "-q", "master")
            f.write_text("## base\n## local-append\n", encoding="utf-8"); g("commit", "-qam", "local")
            g("checkout", "-q", "cloud")
            r = subprocess.run(["git", "rebase", "master"], cwd=d, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0, "預期 rebase 衝突")
            # 在臨時 repo 內模擬本腳本的 union 合併
            orig_repo, orig_wl = rao.REPO, rao.APPEND_ONLY
            try:
                rao.REPO = d
                rao.APPEND_ONLY = {"log.md"}
                self.assertEqual(rao.conflicted_paths(), ["log.md"])
                rao.resolve_union("log.md")
            finally:
                rao.REPO, rao.APPEND_ONLY = orig_repo, orig_wl
            merged = f.read_text(encoding="utf-8")
            self.assertIn("## local-append", merged)
            self.assertIn("## cloud-append", merged)
            self.assertNotIn("<<<<<<<", merged)
            self.assertLess(merged.index("## base"), merged.index("## local-append"))
            subprocess.run(["git", "-c", "core.editor=true", "rebase", "--continue"],
                           cwd=d, capture_output=True, text=True, check=True)

    def test_refuses_outside_whitelist(self):
        """白名單外的衝突 → `--check` 模式 exit 1 且不動檔（那是需要人判斷的）。"""
        orig = rao.conflicted_paths
        try:
            rao.conflicted_paths = lambda: ["wiki/index.md", "wiki/log.md"]
            self.assertEqual(rao.main(["--check"]), 1)
        finally:
            rao.conflicted_paths = orig


class TestPartialResolve(unittest.TestCase):
    """2026-09-27 改版：混合衝突時白名單內的照解並 git add，白名單外的列出不動，
    整體仍 exit 1；只有白名單內衝突時維持 exit 0（原行為）。

    立法依據：09-26 一次 35 檔衝突裡只有 2 個 append-only 帳本，舊版「有白名單外
    衝突就整批拒絕」逼主編連這 2 個機械可解的也手工 union。
    """

    def _git(self, cwd, *args):
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", check=True)

    def _make_mixed_conflict_repo(self, d: Path):
        """夾具：一個白名單檔（log.md）append-append 衝突＋一個白名單外檔（index.md）
        真實內容衝突（兩側改同一行），rebase 後兩檔皆停在衝突。"""
        g = lambda *a: self._git(d, *a)
        g("init", "-q", "-b", "master")
        g("config", "user.email", "t@t")
        g("config", "user.name", "t")
        log = d / "log.md"
        idx = d / "index.md"
        log.write_text("## base\n", encoding="utf-8")
        idx.write_text("base line\n", encoding="utf-8")
        g("add", "."); g("commit", "-qm", "base")
        g("checkout", "-qb", "cloud")
        log.write_text("## base\n## cloud-append\n", encoding="utf-8")
        idx.write_text("cloud line\n", encoding="utf-8")
        g("commit", "-qam", "cloud")
        g("checkout", "-q", "master")
        log.write_text("## base\n## local-append\n", encoding="utf-8")
        idx.write_text("local line\n", encoding="utf-8")
        g("commit", "-qam", "local")
        g("checkout", "-q", "cloud")
        r = subprocess.run(["git", "rebase", "master"], cwd=d, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0, "夾具必須真的產生 rebase 衝突")

    def test_mixed_conflict_resolves_whitelisted_and_lists_rest_exit_1(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self._make_mixed_conflict_repo(d)
            orig_repo, orig_wl = rao.REPO, rao.APPEND_ONLY
            try:
                rao.REPO = d
                rao.APPEND_ONLY = {"log.md"}
                self.assertEqual(set(rao.conflicted_paths()), {"log.md", "index.md"})
                rc = rao.main([])
            finally:
                rao.REPO, rao.APPEND_ONLY = orig_repo, orig_wl

            self.assertEqual(rc, 1, "白名單外仍有衝突，整體必須仍是 exit 1")
            status = self._git(d, "status", "--short").stdout
            # log.md（白名單內）應已被解並 staged：不再是未合併狀態（UU）
            self.assertNotIn("UU log.md", status)
            # index.md（白名單外）維持未合併，未被動過
            self.assertIn("UU index.md", status)
            merged_log = (d / "log.md").read_text(encoding="utf-8")
            self.assertIn("## local-append", merged_log)
            self.assertIn("## cloud-append", merged_log)
            self.assertNotIn("<<<<<<<", merged_log)
            self._git(d, "rebase", "--abort")

    def test_only_whitelist_conflict_still_exits_0(self):
        """回歸測試：純白名單內衝突的原行為（exit 0）不得被這次改版動到。"""
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            g = lambda *a: self._git(d, *a)
            g("init", "-q", "-b", "master")
            g("config", "user.email", "t@t"); g("config", "user.name", "t")
            f = d / "log.md"
            f.write_text("## base\n", encoding="utf-8"); g("add", "."); g("commit", "-qm", "base")
            g("checkout", "-qb", "cloud")
            f.write_text("## base\n## cloud-append\n", encoding="utf-8"); g("commit", "-qam", "cloud")
            g("checkout", "-q", "master")
            f.write_text("## base\n## local-append\n", encoding="utf-8"); g("commit", "-qam", "local")
            g("checkout", "-q", "cloud")
            r = subprocess.run(["git", "rebase", "master"], cwd=d, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)

            orig_repo, orig_wl = rao.REPO, rao.APPEND_ONLY
            try:
                rao.REPO = d
                rao.APPEND_ONLY = {"log.md"}
                rc = rao.main([])
            finally:
                rao.REPO, rao.APPEND_ONLY = orig_repo, orig_wl
            self.assertEqual(rc, 0)
            g("-c", "core.editor=true", "rebase", "--continue")

    def test_check_mode_does_not_resolve_even_when_mixed(self):
        """`--check` 只列出，不論白名單內外都不得改動任何檔。"""
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            self._make_mixed_conflict_repo(d)
            orig_repo, orig_wl = rao.REPO, rao.APPEND_ONLY
            try:
                rao.REPO = d
                rao.APPEND_ONLY = {"log.md"}
                rc = rao.main(["--check"])
            finally:
                rao.REPO, rao.APPEND_ONLY = orig_repo, orig_wl
            self.assertEqual(rc, 1)
            status = self._git(d, "status", "--short").stdout
            self.assertIn("UU log.md", status, "--check 不得動白名單內的檔")
            self.assertIn("UU index.md", status)
            self._git(d, "rebase", "--abort")


if __name__ == "__main__":
    unittest.main()
