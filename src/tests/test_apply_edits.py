"""Tests for scripts/apply_edits.py — 批次精確字串替換。

每個測試用 TemporaryDirectory 當假 repo 根（--root），不碰真 wiki。
"""
import codecs
import io
import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tests._helpers import SCRIPTS_DIR, load_script_module

mod = load_script_module("apply_edits")

PAGE = "wiki/entities/demo.md"
TOPIC = "wiki/topics/demo-topic.md"


class _RepoCase(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write_bytes(self, rel: str, data: bytes) -> Path:
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        return p

    def write(self, rel: str, text: str) -> Path:
        return self.write_bytes(rel, text.encode("utf-8"))

    def read_bytes(self, rel: str) -> bytes:
        return (self.root / rel).read_bytes()

    def apply(self, edits, *, replace_all=False, dry_run=False):
        buf = io.StringIO()
        code = mod.run(edits, self.root, replace_all, dry_run, out=buf)
        return code, buf.getvalue()


class TestHitAndRollback(_RepoCase):
    def test_hits_apply_and_summary(self):
        self.write(PAGE, "line one\nline two alpha\nline three\nline four beta\n")
        self.write(TOPIC, "topic gamma here\n")
        code, out = self.apply([
            {"file": PAGE, "old": "two alpha", "new": "two ALPHA"},
            {"file": PAGE, "old": "four beta", "new": "four BETA\nadded line"},
            {"file": TOPIC, "old": "gamma", "new": "GAMMA"},
        ])
        self.assertEqual(code, 0, out)
        self.assertEqual(self.read_bytes(PAGE),
                         b"line one\nline two ALPHA\nline three\nline four BETA\nadded line\n")
        self.assertEqual(self.read_bytes(TOPIC), b"topic GAMMA here\n")
        self.assertIn("3 筆套用 / 2 檔", out)
        self.assertIn(f"{PAGE}：改動行 2, 4-5", out)
        self.assertIn(f"{TOPIC}：改動行 1", out)

    def test_sequential_edits_on_same_file(self):
        self.write(PAGE, "aaa bbb\n")
        code, out = self.apply([
            {"file": PAGE, "old": "aaa", "new": "xxx"},
            {"file": PAGE, "old": "xxx bbb", "new": "done"},
        ])
        self.assertEqual(code, 0, out)
        self.assertEqual(self.read_bytes(PAGE), b"done\n")

    def test_miss_rolls_back_whole_batch(self):
        self.write(PAGE, "first target\n")
        self.write(TOPIC, "second file\n")
        code, out = self.apply([
            {"file": PAGE, "old": "first target", "new": "CHANGED"},
            {"file": TOPIC, "old": "not present", "new": "x"},
        ])
        self.assertEqual(code, 2)
        self.assertIn("第 2 筆", out)
        self.assertIn("找不到", out)
        self.assertEqual(self.read_bytes(PAGE), b"first target\n")
        self.assertEqual(self.read_bytes(TOPIC), b"second file\n")

    def test_missing_file_is_preflight_error(self):
        code, out = self.apply([{"file": PAGE, "old": "x", "new": "y"}])
        self.assertEqual(code, 2)
        self.assertIn("檔案不存在", out)


class TestMultipleHits(_RepoCase):
    def test_multiple_hits_blocked(self):
        self.write(PAGE, "dup\nother\ndup\n")
        code, out = self.apply([{"file": PAGE, "old": "dup", "new": "x"}])
        self.assertEqual(code, 2)
        self.assertIn("命中 2 次", out)
        self.assertIn("第 1 筆", out)
        self.assertEqual(self.read_bytes(PAGE), b"dup\nother\ndup\n")

    def test_replace_all(self):
        self.write(PAGE, "dup\nother\ndup\n")
        code, out = self.apply([{"file": PAGE, "old": "dup", "new": "x"}], replace_all=True)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.read_bytes(PAGE), b"x\nother\nx\n")
        self.assertIn("改動行 1, 3", out)


class TestEncodingPreserved(_RepoCase):
    def test_crlf_preserved_and_json_newlines_converted(self):
        self.write_bytes(PAGE, b"| a | b |\r\n| c | d |\r\ntail\r\n")
        code, out = self.apply([
            {"file": PAGE, "old": "| a | b |\n| c | d |", "new": "| a | B |\n| new | row |\n| c | d |"},
        ])
        self.assertEqual(code, 0, out)
        self.assertEqual(self.read_bytes(PAGE),
                         b"| a | B |\r\n| new | row |\r\n| c | d |\r\ntail\r\n")
        self.assertNotIn(b"\n", self.read_bytes(PAGE).replace(b"\r\n", b""))

    def test_lf_preserved(self):
        self.write_bytes(PAGE, b"one\ntwo\nthree\n")
        code, out = self.apply([{"file": PAGE, "old": "two\nthree", "new": "2\r\n3"}])
        self.assertEqual(code, 0, out)
        self.assertEqual(self.read_bytes(PAGE), b"one\n2\n3\n")

    def test_bom_preserved(self):
        self.write_bytes(PAGE, codecs.BOM_UTF8 + "中文標題\n內容\n".encode("utf-8"))
        code, out = self.apply([{"file": PAGE, "old": "內容", "new": "新內容"}])
        self.assertEqual(code, 0, out)
        data = self.read_bytes(PAGE)
        self.assertTrue(data.startswith(codecs.BOM_UTF8))
        self.assertEqual(data[3:].decode("utf-8"), "中文標題\n新內容\n")

    def test_no_bom_not_added(self):
        self.write(PAGE, "abc\n")
        self.apply([{"file": PAGE, "old": "abc", "new": "def"}])
        self.assertFalse(self.read_bytes(PAGE).startswith(codecs.BOM_UTF8))


class TestPathRejection(_RepoCase):
    def assert_rejected(self, rel: str):
        self.write(rel, "target text\n")
        self.write(PAGE, "ok text\n")
        code, out = self.apply([
            {"file": PAGE, "old": "ok text", "new": "changed"},
            {"file": rel, "old": "target text", "new": "x"},
        ])
        self.assertEqual(code, 3, out)
        self.assertEqual(self.read_bytes(rel), b"target text\n")
        self.assertEqual(self.read_bytes(PAGE), b"ok text\n")  # 同批合法的那筆也不寫
        return out

    def test_news_rejected(self):
        self.assert_rejected("news/2026-10-11.md")

    def test_log_rejected(self):
        out = self.assert_rejected("wiki/log.md")
        self.assertIn("append", out)

    def test_scripts_rejected(self):
        self.assert_rejected("scripts/x.py")

    def test_radar_and_index_rejected(self):
        self.assert_rejected("wiki/feature-radar.md")
        self.assert_rejected("wiki/index.md")

    def test_help_and_messages_derive_from_constant(self):
        code, out = self.apply([{"file": "wiki/index.md", "old": "a", "new": "b"}])
        self.assertEqual(code, 3)
        self.assertIn(mod.ALLOWED_TEXT, out)
        self.assertEqual(mod.ALLOWED_PREFIXES, ("wiki/entities/", "wiki/topics/"))

    def test_claude_and_data_rejected(self):
        self.assert_rejected(".claude/reporter-rules/shared.md")
        self.assert_rejected("data/foo.json")

    def test_traversal_and_absolute_rejected(self):
        for raw in ("wiki/entities/../log.md", "wiki/entities/../../scripts/x.py",
                    "C:/Windows/x.md", "/etc/passwd"):
            code, _ = self.apply([{"file": raw, "old": "a", "new": "b"}])
            self.assertEqual(code, 3, raw)

    def test_allowed_paths(self):
        for rel in ("wiki/entities/e.md", "wiki/topics/t.md", "wiki\\topics\\t.md"):
            norm = rel.replace("\\", "/")
            self.write(norm, "hello world\n")
            code, out = self.apply([{"file": rel, "old": "hello", "new": "bye"}])
            self.assertEqual(code, 0, f"{rel}: {out}")
            self.assertEqual(self.read_bytes(norm), b"bye world\n")


class TestDryRun(_RepoCase):
    def test_dry_run_does_not_write(self):
        self.write(PAGE, "l1\nl2 target\nl3\n")
        code, out = self.apply([{"file": PAGE, "old": "target", "new": "x"}], dry_run=True)
        self.assertEqual(code, 0, out)
        self.assertEqual(self.read_bytes(PAGE), b"l1\nl2 target\nl3\n")
        self.assertIn("dry-run", out)
        self.assertIn(f"{PAGE}：第 2 行", out)


class TestCli(_RepoCase):
    def _cli(self, *args, stdin: bytes | None = None):
        return subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "apply_edits.py"), *args],
            input=stdin, capture_output=True, timeout=60,
        )

    def test_help_has_no_side_effects(self):
        r = self._cli("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn(b"--dry-run", r.stdout)

    def test_stdin_and_file_input(self):
        self.write(PAGE, "from cli\n")
        batch = json.dumps([{"file": PAGE, "old": "from cli", "new": "via stdin"}]).encode()
        r = self._cli("--root", str(self.root), stdin=batch)
        self.assertEqual(r.returncode, 0, r.stdout.decode("utf-8", "replace"))
        self.assertEqual(self.read_bytes(PAGE), b"via stdin\n")

        jf = self.root / "batch.json"
        jf.write_text(json.dumps([{"file": PAGE, "old": "via stdin", "new": "via file"}]), encoding="utf-8")
        r = self._cli(str(jf), "--root", str(self.root))
        self.assertEqual(r.returncode, 0)
        self.assertEqual(self.read_bytes(PAGE), b"via file\n")

    def test_bad_json_exit_2(self):
        r = self._cli("--root", str(self.root), stdin=b"{not json")
        self.assertEqual(r.returncode, 2)


if __name__ == "__main__":
    unittest.main()
