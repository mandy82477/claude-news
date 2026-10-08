"""pipeline_lock 的互斥判準：用真的 git 遠端（bare repo）加兩個 clone 扮演本機與雲端。

守四件事：持有中另一邊搶不到、放了就搶得到、逾時可接手、同時搶時後推的輸（git 快轉檢查）。
另守「搶到鎖後日報已在 origin」要放鎖並回 4，以及沒持有時 release 不動遠端。
"""
import io
import os
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
import pipeline_lock as pl  # noqa: E402

ENV = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
       "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
T0 = datetime(2026, 10, 8, 17, 0, tzinfo=timezone.utc)


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", env=ENV)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr}")
    return r.stdout.strip()


def quiet(fn, *a, **k):
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = fn(*a, **k)
    return rc, buf.getvalue()


class LockTest(unittest.TestCase):
    def setUp(self):
        os.environ.update({k: ENV[k] for k in ("GIT_AUTHOR_NAME", "GIT_AUTHOR_EMAIL", "GIT_COMMITTER_NAME", "GIT_COMMITTER_EMAIL")})
        self.tmp = TemporaryDirectory()
        root = Path(self.tmp.name)
        self.origin = root / "origin.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "master", str(self.origin)], check=True, env=ENV)
        seed = root / "seed"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(seed)], check=True, env=ENV, capture_output=True)
        (seed / "a.txt").write_text("a", encoding="utf-8")
        git(seed, "add", "a.txt")
        git(seed, "commit", "-q", "-m", "seed")
        git(seed, "push", "-q", "origin", "HEAD:master")
        self.local = root / "local"
        self.cloud = root / "cloud"
        for c in (self.local, self.cloud):
            subprocess.run(["git", "clone", "-q", str(self.origin), str(c)], check=True, env=ENV, capture_output=True)
        self.seed = seed

    def tearDown(self):
        self.tmp.cleanup()

    def test_held_lock_blocks_the_other_side_until_released(self):
        rc, _ = quiet(pl.acquire, self.local, "2026-10-08", "local@pc", now=T0)
        self.assertEqual(rc, 0)
        rc, out = quiet(pl.acquire, self.cloud, "2026-10-08", "cloud@box", now=T0 + timedelta(minutes=30))
        self.assertEqual(rc, 1)
        self.assertIn("local@pc", out)
        self.assertIn("30 分鐘前", out)

        quiet(pl.release, self.local, now=T0 + timedelta(hours=1))
        rc, _ = quiet(pl.acquire, self.cloud, "2026-10-08", "cloud@box", now=T0 + timedelta(hours=1, minutes=5))
        self.assertEqual(rc, 0)
        msgs = git(self.origin, "log", "--format=%s", pl.BRANCH).splitlines()
        self.assertEqual([m.split()[0] for m in msgs], ["HELD", "RELEASED", "HELD"])

    def test_same_clone_twice_is_not_reentrant(self):
        # 同一個 clone 上兩個本機 session 共用權杖檔，第二個也要被擋
        self.assertEqual(quiet(pl.acquire, self.local, "2026-10-08", "local@pc", now=T0)[0], 0)
        rc, out = quiet(pl.acquire, self.local, "2026-10-08", "local@pc", now=T0 + timedelta(minutes=5))
        self.assertEqual(rc, 1)
        self.assertIn("release", out)

    def test_stale_lock_can_be_taken_over(self):
        quiet(pl.acquire, self.local, "2026-10-08", "local@pc", now=T0)
        rc, out = quiet(pl.acquire, self.cloud, "2026-10-08", "cloud@box", now=T0 + timedelta(hours=pl.STALE_HOURS, minutes=1))
        self.assertEqual(rc, 0)
        self.assertIn("視為已死", out)
        # 原持有者事後 release：鎖已不是它的，只清權杖、不動遠端
        before = git(self.origin, "rev-parse", pl.BRANCH)
        quiet(pl.release, self.local, now=T0 + timedelta(hours=4))
        self.assertEqual(git(self.origin, "rev-parse", pl.BRANCH), before)
        self.assertFalse(pl._token_file(self.local).exists())

    def test_simultaneous_grab_loser_is_rejected_by_fast_forward_check(self):
        # 兩邊都看到「無鎖」後各自推：先推的贏，後推的不是快轉被拒
        status_a, _ = pl._push_child(self.local, None, f"HELD aaa local@pc 2026-10-08 {pl._iso(T0)}")
        status_b, _ = pl._push_child(self.cloud, None, f"HELD bbb cloud@box 2026-10-08 {pl._iso(T0)}")
        self.assertEqual((status_a, status_b), ("ok", "rejected"))

    def test_digest_already_on_origin_releases_and_returns_4(self):
        (self.seed / "news").mkdir()
        (self.seed / "news" / "2026-10-08.md").write_text("x", encoding="utf-8")
        git(self.seed, "add", "news")
        git(self.seed, "commit", "-q", "-m", "digest")
        git(self.seed, "push", "-q", "origin", "HEAD:master")
        rc, _ = quiet(pl.acquire, self.local, "2026-10-08", "local@pc", require_absent="news/2026-10-08.md", now=T0)
        self.assertEqual(rc, 4)
        self.assertEqual(git(self.origin, "log", "-1", "--format=%s", pl.BRANCH).split()[0], "RELEASED")

    def test_release_without_holding_touches_nothing(self):
        rc, out = quiet(pl.release, self.cloud, now=T0)
        self.assertEqual(rc, 0)
        self.assertIn("未持有", out)
        self.assertEqual(subprocess.run(["git", "-C", str(self.origin), "rev-parse", "--verify", "--quiet", pl.BRANCH],
                                        capture_output=True).returncode, 1)

    def test_parse_rejects_non_lock_messages(self):
        self.assertIsNone(pl.parse("wiki: ingest"))
        self.assertEqual(pl.parse(f"HELD t h 2026-10-08 {pl._iso(T0)}")["holder"], "h")


if __name__ == "__main__":
    unittest.main()
