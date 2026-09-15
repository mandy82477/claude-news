"""Build Flags 來源：出貨二進位裡的旗標差異，一個版本最多一則，首跑只記基線。

2026-09-15 探針：CLAUDE_CODE_ENABLE_FUNCTION_HOOKS 在 09-04 的 2.1.261 就在 build 裡，
比 issue 本文的官方承諾（09-09）早五天，changelog 到 09-14 仍未提。
2.1.261→2.1.272 十天新增 45 個旗標，其中約一半是逾時／識別碼等水管；單日差 1 個。
"""
import io
import json
import sys
import tarfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from news_aggregator.sources import build_flags_watch as bf  # noqa: E402

NOW = datetime(2026, 9, 15, tzinfo=timezone.utc)


def fake_tgz(flags: list[str], junk_size: int = 4096) -> bytes:
    """一個像 npm 套件的 tgz：小的 package.json ＋ 一個大的『二進位』，旗標散在裡面。"""
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        pj = json.dumps({"name": bf.PACKAGE}).encode()
        info = tarfile.TarInfo("package/package.json"); info.size = len(pj)
        t.addfile(info, io.BytesIO(pj))
        body = b"\x00garbage\x01".join(f.encode() for f in flags) + b"\x00" * junk_size
        info = tarfile.TarInfo("package/claude"); info.size = len(body)
        t.addfile(info, io.BytesIO(body))
    return buf.getvalue()


BASE = [f"CLAUDE_CODE_FLAG_{i:03d}" for i in range(60)]  # 真 build 有數百個；門檻 50


class TestPureFunctions(unittest.TestCase):
    def test_extract_flags_from_binary_bytes(self):
        data = b"\x00CLAUDE_CODE_ENABLE_FUNCTION_HOOKS\x00xx CLAUDE_CODE_POST_TURN_MEMORY_SYNC\x01CLAUDE_CODE_AB"
        self.assertEqual(bf.extract_flags(data),
                         {"CLAUDE_CODE_ENABLE_FUNCTION_HOOKS", "CLAUDE_CODE_POST_TURN_MEMORY_SYNC"})

    def test_plumbing_vs_candidate(self):
        plumbing = ["CLAUDE_CODE_CONNECT_TIMEOUT_MS", "CLAUDE_CODE_ARTIFACT_FD", "CLAUDE_CODE_TOOL_USE_ID",
                    "CLAUDE_CODE_GATEWAY_TOKEN", "CLAUDE_CODE_DESKTOP_APP_VERSION",
                    "CLAUDE_CODE_INSTALLED_VIA_NPM_WRAPPER", "CLAUDE_CODE_SHELL_LAUNCHER_SCRIPT"]
        cands = ["CLAUDE_CODE_ENABLE_FUNCTION_HOOKS", "CLAUDE_CODE_POST_TURN_MEMORY",
                 "CLAUDE_CODE_DISABLE_TURN_HANDOFF", "CLAUDE_CODE_AUTO_MODE_SERVER",
                 "CLAUDE_CODE_POLISHED_DEWDROP"]  # 代號也是候選——記者分，機器不猜
        for f in plumbing:
            self.assertTrue(bf.is_plumbing(f), f)
        for f in cands:
            self.assertFalse(bf.is_plumbing(f), f)

    def test_build_item_is_one_line_with_candidates_and_counts(self):
        added = {"CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_CONNECT_TIMEOUT_MS", "CLAUDE_CODE_ARTIFACT_REPL"}
        item = bf.build_item("2.1.261", "2.1.272", added, {"CLAUDE_CODE_CARVED_SLATE"}, now=NOW)
        self.assertIn("2 個功能候選", item.title)
        self.assertIn("`CLAUDE_CODE_ARTIFACT_REPL`", item.summary)
        self.assertIn("1 個設定類旗標", item.summary)
        self.assertIn("消失：`CLAUDE_CODE_CARVED_SLATE`", item.summary)
        self.assertEqual(item.source, "Build Flags")
        self.assertEqual(item.score, 0)
        self.assertEqual(item.dedup_key, f"{bf.PACKAGE_PAGE}2.1.272#2.1.272")

    def test_build_item_none_when_only_plumbing_changed(self):
        self.assertIsNone(bf.build_item("a", "b", {"CLAUDE_CODE_X_TIMEOUT_MS"}, set(), now=NOW))

    def test_two_versions_get_two_cache_keys(self):
        a = bf.build_item("1", "2", {"CLAUDE_CODE_A"}, set(), now=NOW)
        b = bf.build_item("2", "3", {"CLAUDE_CODE_B"}, set(), now=NOW)
        self.assertNotEqual(a.dedup_key, b.dedup_key)


class TestFetch(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(__import__("tempfile").mkdtemp())
        self.state = self.tmp / "state.json"
        self.ledger = self.tmp / "ledger.jsonl"
        self.p_state = mock.patch.object(bf, "STATE_PATH", self.state)
        self.p_ledger = mock.patch.object(bf, "LEDGER_PATH", self.ledger)
        self.p_state.start(); self.p_ledger.start()

    def tearDown(self):
        self.p_state.stop(); self.p_ledger.stop()

    def _run(self, version: str, flags: list[str], downloads: list | None = None):
        tgz = fake_tgz(flags)

        def get(url, **kw):
            r = mock.Mock()
            r.raise_for_status.return_value = None
            if url == bf.REGISTRY_URL:
                r.json.return_value = {"version": version, "dist": {"tarball": f"https://x/{version}.tgz"}}
            else:
                if downloads is not None:
                    downloads.append(url)
                r.iter_content = lambda chunk_size: [tgz]
                r.__enter__ = lambda s: s
                r.__exit__ = lambda s, *a: False
            return r
        with mock.patch.object(bf.requests, "get", side_effect=get):
            return bf.BuildFlagsWatch().fetch()

    def test_first_run_baselines_silently(self):
        items = self._run("2.1.261", BASE)
        self.assertEqual(items, [])
        st = json.loads(self.state.read_text(encoding="utf-8"))
        self.assertEqual(st["version"], "2.1.261")
        self.assertEqual(len(st["flags"]), 60)
        self.assertFalse(self.ledger.exists())

    def test_new_version_emits_one_item_and_appends_ledger(self):
        self._run("2.1.261", BASE)
        items = self._run("2.1.272", BASE + ["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_X_TIMEOUT_MS"])
        self.assertEqual(len(items), 1)
        self.assertIn("1 個功能候選", items[0].title)
        rows = [json.loads(l) for l in self.ledger.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(rows[0]["candidates"], ["CLAUDE_CODE_POST_TURN_MEMORY"])
        self.assertEqual(rows[0]["plumbing"], ["CLAUDE_CODE_X_TIMEOUT_MS"])
        self.assertEqual((rows[0]["from"], rows[0]["to"]), ("2.1.261", "2.1.272"))
        self.assertEqual(json.loads(self.state.read_text(encoding="utf-8"))["version"], "2.1.272")

    def test_same_version_does_not_download(self):
        self._run("2.1.272", BASE)
        dl: list = []
        self.assertEqual(self._run("2.1.272", BASE, downloads=dl), [])
        self.assertEqual(dl, [])

    def test_removed_only_still_emits(self):
        self._run("2.1.271", BASE + ["CLAUDE_CODE_CARVED_SLATE"])
        items = self._run("2.1.272", BASE)
        self.assertEqual(len(items), 1)
        self.assertIn("消失", items[0].summary)

    def test_suspiciously_few_flags_refuses_to_touch_state(self):
        self._run("2.1.271", BASE)
        items = self._run("2.1.272", ["CLAUDE_CODE_ONLY_ONE"])  # 抓錯檔
        self.assertEqual(items, [])
        self.assertEqual(json.loads(self.state.read_text(encoding="utf-8"))["version"], "2.1.271")

    def test_network_failure_returns_empty_and_keeps_state(self):
        self._run("2.1.271", BASE)
        with mock.patch.object(bf.requests, "get", side_effect=OSError("boom")):
            self.assertEqual(bf.BuildFlagsWatch().fetch(), [])
        self.assertEqual(json.loads(self.state.read_text(encoding="utf-8"))["version"], "2.1.271")


if __name__ == "__main__":
    unittest.main()
