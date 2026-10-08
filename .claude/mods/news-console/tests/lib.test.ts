import { expect, test } from 'claude-code/testing'
import {
  classifyShift, explainPullFailure, foreignHits, freshness, gitStageCalls, latestDigest, parseAheadBehind,
  parsePorcelain, relTo, syncSummary, underSpec,
} from '../hooks/lib.ts'

const NOW = Date.UTC(2026, 9, 3, 9, 0, 0) // 2026-10-03T09:00Z

test('ahead/behind and latest digest parse git output', async () => {
  expect(parseAheadBehind('0\t54\n')).toEqual({ ahead: 0, behind: 54 })
  expect(parseAheadBehind('fatal: bad revision')).toBe(null)
  expect(latestDigest('news/2026-09-30.md\nnews/2026-10-02.md\nnews/README.md\n')).toBe('2026-10-02')
})

test('a diverged clone gets no ff-only button, and pull errors say why', async () => {
  expect(syncSummary(0, 1)).toEqual({ text: '本機落後 origin 1 筆', canFastForward: true })
  const diverged = syncSummary(2, 1)
  expect(diverged.canFastForward).toBe(false)
  expect(diverged.text).toContain('分岔')
  // 2026-10-04 實際的 stderr：第一行是 hint，不是原因
  expect(explainPullFailure('hint: Diverging branches can\'t be fast-forwarded\nfatal: Not possible to fast-forward, aborting.'))
    .toBe('本機有未推的 commit，和遠端分岔了，ff-only 拉不了')
  expect(explainPullFailure('error: Your local changes to the following files would be overwritten by merge:\n\tsrc/gathered_items.json'))
    .toContain('未 commit')
  expect(explainPullFailure('hint: something\nfatal: unable to access remote')).toBe('fatal: unable to access remote')
})

test('designed aborts stay quiet', async () => {
  const idem = '[cloud daily-news-pipeline-cloud STARTED 2026-10-02T22:08:16Z]\n' +
    '[cloud daily-news-pipeline-cloud ABORTED 2026-10-02T22:08:16Z] reason=digest already exists (Step 0b 冪等閘)'
  expect(classifyShift(idem, [], NOW).alert).toBe(null)
  const wait12 = '[cloud daily-news-pipeline-cloud STARTED 2026-10-02T12:08:33Z]\n' +
    '[cloud daily-news-pipeline-cloud ABORTED 2026-10-02T12:09:15Z] Step 1a：src/gathered_archive/2026-10-02.json 不存在'
  expect(classifyShift(wait12, [], NOW).alert).toBe(null)
  const locked = '[cloud daily-news-pipeline-cloud STARTED 2026-10-02T17:08:00Z]\n' +
    '[cloud daily-news-pipeline-cloud ABORTED 2026-10-02T17:09:00Z] ABORTED: pipeline lock held by local@pc'
  expect(classifyShift(locked, [], NOW).alert).toBe(null)
  const done = '[cloud daily-news-pipeline-cloud STARTED 2026-10-02T17:07:58Z]\n[x] Single push done\n[x] === Pipeline complete (agent) ==='
  expect(classifyShift(done, [], NOW).alert).toBe(null)
})

test('real failures speak up', async () => {
  const wait22 = '[cloud daily-news-pipeline-cloud STARTED 2026-10-02T22:08:33Z]\n' +
    '[cloud daily-news-pipeline-cloud ABORTED 2026-10-02T22:09:15Z] Step 1a：archive 不存在'
  expect(classifyShift(wait22, [], NOW).alert).toMatch(/缺報/)
  const failed = '[cloud daily-news-pipeline-cloud STARTED 2026-10-02T17:07:58Z]\n[x] Push FAILED - rebase conflict'
  expect(classifyShift(failed, [], NOW).alert).toMatch(/失敗/)
  const dead = '[cloud daily-news-pipeline-cloud STARTED 2026-10-03T03:00:00Z]\n'
  expect(classifyShift(dead, [], NOW).alert).toMatch(/中途死亡/)
  const running = '[cloud daily-news-pipeline-cloud STARTED 2026-10-03T08:00:00Z]\n'
  expect(classifyShift(running, [], NOW).alert).toBe(null)
  expect(classifyShift('', ['origin/cloud-daily-2026-10-02-unmerged'], NOW).alert).toMatch(/停泊分支/)
})

test('freshness reads last_news_update from frontmatter', async () => {
  const page = '---\npage: "topics/x"\nlast_news_update: "2026-09-02"\n---\n# x\n'
  expect(freshness(page, NOW)).toEqual({ date: '2026-09-02', days: 31 })
  expect(freshness('# no frontmatter\n', NOW)).toBe(null)
})

test('paths: relTo, porcelain, pathspecs', async () => {
  expect(relTo('C:/repo', 'C:\\repo\\wiki\\log.md')).toBe('wiki/log.md')
  expect(relTo('C:/repo', 'c:/repo/wiki/a.md')).toBe('wiki/a.md')
  expect(relTo('C:/repo', 'D:/elsewhere/a.md')).toBe(null)
  expect(parsePorcelain(' M wiki/a.md\n?? news/x.md\nR  old.md -> new.md\n')).toEqual(['wiki/a.md', 'news/x.md', 'new.md'])
  expect(underSpec('wiki/a.md', 'wiki/')).toBe(true)
  expect(underSpec('wiki2/a.md', 'wiki')).toBe(false)
})

test('git add/commit calls are found only at command start', async () => {
  expect(gitStageCalls('git add wiki/ data/x.jsonl && git commit -m "x"')).toEqual([
    { sub: 'add', pathspecs: ['wiki/', 'data/x.jsonl'], all: false },
    { sub: 'commit', pathspecs: [], all: false },
  ])
  expect(gitStageCalls('git -C "D:/r" add -- wiki/a.md')).toEqual([{ sub: 'add', pathspecs: ['wiki/a.md'], all: false }])
  expect(gitStageCalls('echo "git add wiki/"; grep "git commit" x')).toEqual([])
  expect(gitStageCalls('git commit -m "fix; git add . later"')).toEqual([{ sub: 'commit', pathspecs: [], all: false }])
  // -a／--all／-am 都會帶走所有改過的追蹤檔
  expect(gitStageCalls('git commit -am "x"')[0].all).toBe(true)
  expect(gitStageCalls('git commit --all -m x')[0].all).toBe(true)
  expect(gitStageCalls('git commit -m x -- wiki/a.md')).toEqual([{ sub: 'commit', pathspecs: ['wiki/a.md'], all: false }])
})

test('foreign hits count files and sessions, never mine', async () => {
  const foreign = new Map([['s2', new Set(['wiki/a.md', 'wiki/b.md'])], ['s3', new Set(['weekly/w.md'])]])
  expect(foreignHits(['wiki/a.md', 'wiki/b.md', 'wiki/c.md'], new Set(['wiki/c.md']), foreign)).toEqual({ files: 2, sessions: 1 })
  expect(foreignHits(['wiki/a.md'], new Set(['wiki/a.md']), foreign)).toEqual({ files: 0, sessions: 0 })
})
