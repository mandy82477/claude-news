"""Build Flags 來源：出貨二進位裡的旗標差異，一個版本最多一則，首跑只記基線。

2026-09-15 探針：CLAUDE_CODE_ENABLE_FUNCTION_HOOKS 在 09-04 的 2.1.261 就在 build 裡，
比 issue 本文的官方承諾（09-09）早五天，changelog 到 09-14 仍未提。
2026-09-16 review 六個 P1：黏字（`..._MINUTES0`）當成真旗標、子字串過濾誤殺
`EXPERIMENTAL_AGENT_TEAMS`、狀態檔壞掉被當首跑、例外全吞讓 ok=false 永不出現、
對帳腳本欄序寫死、第 3 階證據數字錯。每一項各釘一個測試。
"""
import io
import json
import sys
import tarfile
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from news_aggregator.sources import build_flags_watch as bf  # noqa: E402

NOW = datetime(2026, 9, 15, tzinfo=timezone.utc)


def fake_tgz(flags: list[str], junk_size: int = 4096) -> bytes:
    """像 npm 套件的 tgz：小的 package.json ＋ 一個大的『二進位』，旗標散在裡面，每個以引號收尾。"""
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        pj = json.dumps({"name": bf.PACKAGE}).encode()
        info = tarfile.TarInfo("package/package.json"); info.size = len(pj)
        t.addfile(info, io.BytesIO(pj))
        body = b'"\x00garbage\x01'.join(f.encode() for f in flags) + b'"' + b"\x00" * junk_size
        info = tarfile.TarInfo("package/claude"); info.size = len(body)
        t.addfile(info, io.BytesIO(body))
    return buf.getvalue()


BASE = [f"CLAUDE_CODE_FLAG_{i:03d}" for i in range(60)]  # 真 build 有數百個；門檻 50


class TestCleanFlags(unittest.TestCase):
    def test_extract_flags_from_binary_bytes(self):
        data = b"\x00CLAUDE_CODE_ENABLE_FUNCTION_HOOKS\x00xx CLAUDE_CODE_POST_TURN_MEMORY_SYNC\x01CLAUDE_CODE_AB"
        self.assertEqual(bf.extract_flags(data),
                         {"CLAUDE_CODE_ENABLE_FUNCTION_HOOKS", "CLAUDE_CODE_POST_TURN_MEMORY_SYNC"})

    def test_byte_glue_is_dropped_but_real_subflags_survive(self):
        """P1-1：`MINUTES0`、`BASE_URLI`、`SESSION_` 是黏字（各只出現 1 次）；
        `POST_TURN_MEMORY_SYNC` 是真子旗標（以 `_` 起頭）；`BASE_REFS` 出現 4 次是真旗標
        （第二輪 review 用真二進位證實，不可因 `BASE_REF` 存在就刪）。"""
        counts = {"CLAUDE_CODE_GOAL_CHECKIN_MINUTES": 5, "CLAUDE_CODE_GOAL_CHECKIN_MINUTES0": 1,
                  "CLAUDE_CODE_ASSUME_FIRST_PARTY_BASE_URL": 3, "CLAUDE_CODE_ASSUME_FIRST_PARTY_BASE_URLI": 1,
                  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": 6, "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMSV": 1,
                  "CLAUDE_CODE_SESSION_": 115, "CLAUDE_CODE_SESSION_ID": 9,
                  "CLAUDE_CODE_POST_TURN_MEMORY": 4, "CLAUDE_CODE_POST_TURN_MEMORY_SYNC": 2,
                  "CLAUDE_CODE_BASE_REF": 4, "CLAUDE_CODE_BASE_REFS": 4}
        self.assertEqual(bf.clean_flags(counts), {
            "CLAUDE_CODE_GOAL_CHECKIN_MINUTES", "CLAUDE_CODE_ASSUME_FIRST_PARTY_BASE_URL",
            "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS", "CLAUDE_CODE_SESSION_ID",
            "CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_POST_TURN_MEMORY_SYNC",
            "CLAUDE_CODE_BASE_REF", "CLAUDE_CODE_BASE_REFS"})

    def test_glue_shape_with_multiple_occurrences_is_a_real_flag(self):
        """出現 ≥2 次就不是黏字，即使形狀像。"""
        self.assertEqual(bf.clean_flags({"CLAUDE_CODE_BASE_REF": 4, "CLAUDE_CODE_BASE_REFS": 2}),
                         {"CLAUDE_CODE_BASE_REF", "CLAUDE_CODE_BASE_REFS"})

    def test_glue_only_when_the_base_exists(self):
        self.assertEqual(bf.clean_flags({"CLAUDE_CODE_ARTIFACT_MCP6": 1}), {"CLAUDE_CODE_ARTIFACT_MCP6"})

    def test_extract_counts_occurrences_from_bytes(self):
        data = b'"CLAUDE_CODE_BASE_REF"\x00a.CLAUDE_CODE_BASE_REFS\x00"CLAUDE_CODE_BASE_REFS"\x00CLAUDE_CODE_BASE_REFX\x01'
        self.assertEqual(bf.extract_flags(data), {"CLAUDE_CODE_BASE_REF", "CLAUDE_CODE_BASE_REFS"})


class TestPlumbing(unittest.TestCase):
    def test_token_based_never_matches_substrings(self):
        """P1-2：TEAMS 不是 MS、IDLE 不是 ID、TRANSCRIPT 不是 SCRIPT。"""
        for f in ("CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS", "CLAUDE_CODE_DISABLE_AWAITING_USER_IDLE",
                  "CLAUDE_CODE_AUTO_MODE_SEGMENTED_TRANSCRIPT", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST",
                  "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS", "CLAUDE_CODE_POST_TURN_MEMORY",
                  "CLAUDE_CODE_POLISHED_DEWDROP"):
            self.assertFalse(bf.is_plumbing(f), f)

    def test_real_plumbing_still_filtered(self):
        for f in ("CLAUDE_CODE_CONNECT_TIMEOUT_MS", "CLAUDE_CODE_ARTIFACT_FD", "CLAUDE_CODE_TOOL_USE_ID",
                  "CLAUDE_CODE_GATEWAY_TOKEN", "CLAUDE_CODE_DESKTOP_APP_VERSION",
                  "CLAUDE_CODE_INSTALLED_VIA_NPM_WRAPPER", "CLAUDE_CODE_SHELL_LAUNCHER_SCRIPT",
                  "CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS", "CLAUDE_CODE_ACCOUNT_UUID"):
            self.assertTrue(bf.is_plumbing(f), f)


class TestBuildItem(unittest.TestCase):
    def test_one_line_with_candidates_and_counts(self):
        added = {"CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_CONNECT_TIMEOUT_MS", "CLAUDE_CODE_ARTIFACT_REPL"}
        item = bf.build_item("2.1.261", "2.1.272", added, {"CLAUDE_CODE_CARVED_SLATE"}, now=NOW)
        self.assertIn("2 個功能候選", item.title)
        self.assertIn("`CLAUDE_CODE_ARTIFACT_REPL`", item.summary)
        self.assertIn("1 個設定類旗標", item.summary)
        self.assertIn("消失 1 個：`CLAUDE_CODE_CARVED_SLATE`", item.summary)
        self.assertEqual((item.source, item.score), ("Build Flags", 0))
        self.assertEqual(item.dedup_key, f"{bf.PACKAGE_PAGE}2.1.272#2.1.272")

    def test_none_when_only_plumbing_changed(self):
        self.assertIsNone(bf.build_item("a", "b", {"CLAUDE_CODE_X_TIMEOUT_MS"}, set(), now=NOW))

    def test_truncation_is_stated_for_both_lists(self):
        """P2-6：超過 MAX_LISTED 要說「只列前 N 個」，消失清單也一樣。"""
        many = {f"CLAUDE_CODE_FEATURE_{i:03d}" for i in range(bf.MAX_LISTED + 5)}
        gone = {f"CLAUDE_CODE_GONE_{i:03d}" for i in range(bf.MAX_LISTED + 2)}
        s = bf.build_item("a", "b", many, gone, now=NOW).summary
        self.assertEqual(s.count(f"（只列前 {bf.MAX_LISTED} 個）"), 2)
        self.assertIn(f"功能候選 {bf.MAX_LISTED + 5} 個", s)
        self.assertIn(f"消失 {bf.MAX_LISTED + 2} 個", s)

    def test_two_versions_get_two_cache_keys(self):
        a = bf.build_item("1", "2", {"CLAUDE_CODE_A"}, set(), now=NOW)
        b = bf.build_item("2", "3", {"CLAUDE_CODE_B"}, set(), now=NOW)
        self.assertNotEqual(a.dedup_key, b.dedup_key)


class TestFetch(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.state = self.tmp / "state.json"
        self.ledger = self.tmp / "ledger.jsonl"
        self.patches = [mock.patch.object(bf, "STATE_PATH", self.state),
                        mock.patch.object(bf, "LEDGER_PATH", self.ledger)]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()

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

    def _state(self):
        return json.loads(self.state.read_text(encoding="utf-8"))

    def test_first_run_baselines_silently(self):
        self.assertEqual(self._run("2.1.261", BASE), [])
        self.assertEqual((self._state()["version"], len(self._state()["flags"])), ("2.1.261", 60))
        self.assertFalse(self.ledger.exists())

    def test_new_version_emits_one_item_and_appends_ledger(self):
        self._run("2.1.261", BASE)
        items = self._run("2.1.272", BASE + ["CLAUDE_CODE_POST_TURN_MEMORY", "CLAUDE_CODE_X_TIMEOUT_MS"])
        self.assertEqual(len(items), 1)
        self.assertIn("1 個功能候選", items[0].title)
        rows = [json.loads(l) for l in self.ledger.read_text(encoding="utf-8").splitlines()]
        self.assertEqual((rows[0]["candidates"], rows[0]["plumbing"], rows[0]["from"], rows[0]["to"]),
                         (["CLAUDE_CODE_POST_TURN_MEMORY"], ["CLAUDE_CODE_X_TIMEOUT_MS"], "2.1.261", "2.1.272"))
        self.assertEqual(self._state()["version"], "2.1.272")

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

    def test_suspiciously_few_flags_raises_and_keeps_state(self):
        self._run("2.1.271", BASE)
        with self.assertRaises(ValueError):
            self._run("2.1.272", ["CLAUDE_CODE_ONLY_ONE"])  # 抓錯檔
        self.assertEqual(self._state()["version"], "2.1.271")

    def test_network_failure_raises_so_main_records_ok_false(self):
        """P1-4：不吞例外——main.py 才記得到 ok=false，來源健檢才看得見。"""
        self._run("2.1.271", BASE)
        with mock.patch.object(bf.requests, "get", side_effect=OSError("boom")):
            with self.assertRaises(OSError):
                bf.BuildFlagsWatch().fetch()
        self.assertEqual(self._state()["version"], "2.1.271")

    def test_corrupt_state_is_not_a_first_run(self):
        """P1-3：狀態檔截斷 → 拒絕當首跑、不覆寫、不發。"""
        self._run("2.1.271", BASE)
        self.state.write_text('{"version": "2.1.271", "flags": ["CLAUDE_CODE_FL', encoding="utf-8")
        with self.assertRaises(bf.StateError):
            self._run("2.1.272", BASE + ["CLAUDE_CODE_NEW_THING"])
        self.assertTrue(self.state.read_text(encoding="utf-8").endswith('"CLAUDE_CODE_FL'))
        self.assertFalse(self.ledger.exists())

    def test_state_with_too_few_flags_raises(self):
        """P2-1：上一版集合異常小，差集會把整個 build 當新增——拒絕。"""
        self.state.write_text(json.dumps({"version": "2.1.271", "flags": []}), encoding="utf-8")
        with self.assertRaises(bf.StateError):
            self._run("2.1.272", BASE + ["CLAUDE_CODE_NEW_THING"])

    def test_implausibly_large_diff_raises(self):
        self._run("2.1.271", BASE)
        huge = BASE + [f"CLAUDE_CODE_NEW_{i:04d}" for i in range(bf.MAX_ADDED + 1)]
        with self.assertRaises(ValueError):
            self._run("2.1.272", huge)
        self.assertEqual(self._state()["version"], "2.1.271")

    def test_download_total_deadline(self):
        """P2-2：requests 的 timeout 是單次讀取，總時長要自己管。"""
        r = mock.Mock(); r.raise_for_status.return_value = None
        r.iter_content = lambda chunk_size: iter([b"x"] * 5)
        r.__enter__ = lambda s: s; r.__exit__ = lambda s, *a: False
        clock = iter([0.0, 0.0, 1.0, 700.0, 701.0, 702.0, 703.0])
        with mock.patch.object(bf.requests, "get", return_value=r), \
             mock.patch.object(bf.time, "monotonic", side_effect=lambda: next(clock)):
            with self.assertRaises(TimeoutError):
                bf._download_flags("https://x/t.tgz", deadline=600)


if __name__ == "__main__":
    unittest.main()
