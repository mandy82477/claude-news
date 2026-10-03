// 小編輯部介紹動畫的劇本與播放器。PALETTE／CHARS／PROPS 由 make-story.mts 從 mod 實際程式產生後注入。
// 畫布固定 1920×1080；字級下限：字幕標題 52px、副標 36px、標籤 30px（縮到 1280 寬約 20px）。
// 每幕的劇情對應規則檔出處，見同資料夾 README.md 的分鏡表。

const cv = document.getElementById('cv')
const ctx = cv.getContext('2d')
const W = 1920, H = 1080
const FONT = '"Noto Sans TC","Microsoft JhengHei","PingFang TC",sans-serif'
const EMOJI = '"Segoe UI Emoji","Apple Color Emoji","Noto Color Emoji"'
const COL = {
  stage: '#f7f3e8', floor: '#e6dfcd', ink: '#1f1e1d', mut: '#5f5e5a', paper: '#fffdf7', line: '#cfc9b9',
  clay: '#D85A30', red: '#E24B4A', redInk: '#A32D2D', green: '#3B6D11', greenFill: '#639922', amber: '#854F0B',
  amberFill: '#FAC775', blue: '#185FA5', blueFill: '#378ADD', gray: '#888780', sticky: '#FAC775',
}

// ── 小工具 ──────────────────────────────────────────────────────
const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v))
const seg = (t, a, b) => clamp((t - a) / (b - a))
const ease = (x) => (x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2)
const lerp = (a, b, p) => a + (b - a) * p

function grid(g, x, y, s) {
  for (let r = 0; r < g.length; r++) {
    const row = g[r]
    for (let c = 0; c < row.length; c++) {
      const ch = row[c]
      if (ch === '.') continue
      ctx.fillStyle = PALETTE[ch.charCodeAt(0) - 65]
      ctx.fillRect(Math.round(x + c * s), Math.round(y + r * s), Math.ceil(s), Math.ceil(s))
    }
  }
}
// 角色：mode = wave｜still｜glasses｜sleep；x,y 為左上角，s 為每像素邊長
function char(key, mode, x, y, s, tick) {
  const frames = CHARS[key][mode]
  grid(frames[tick % frames.length], x, y, s)
}
function prop(name, x, y, s, tick) {
  const f = PROPS[name]
  grid(f[tick % f.length], x, y, s)
}
function text(str, x, y, o = {}) {
  ctx.save()
  ctx.globalAlpha *= o.alpha ?? 1
  ctx.font = `${o.weight ?? 500} ${o.size ?? 34}px ${FONT},${EMOJI}`
  ctx.fillStyle = o.color ?? COL.ink
  ctx.textAlign = o.align ?? 'left'
  ctx.textBaseline = o.base ?? 'alphabetic'
  if (o.rot) { ctx.translate(x, y); ctx.rotate(o.rot); ctx.fillText(str, 0, 0) } else ctx.fillText(str, x, y)
  ctx.restore()
}
function rr(x, y, w, h, r) {
  ctx.beginPath()
  ctx.moveTo(x + r, y)
  ctx.arcTo(x + w, y, x + w, y + h, r)
  ctx.arcTo(x + w, y + h, x, y + h, r)
  ctx.arcTo(x, y + h, x, y, r)
  ctx.arcTo(x, y, x + w, y, r)
  ctx.closePath()
}
function box(x, y, w, h, o = {}) {
  ctx.save()
  ctx.globalAlpha *= o.alpha ?? 1
  rr(x, y, w, h, o.r ?? 14)
  if (o.fill !== null) { ctx.fillStyle = o.fill ?? COL.paper; ctx.fill() }
  if (o.stroke !== null) { ctx.lineWidth = o.lw ?? 3; ctx.strokeStyle = o.stroke ?? COL.line; ctx.stroke() }
  ctx.restore()
}
// 卡片：主標＋可選副標，文字置中
function card(x, y, w, h, title, sub, o = {}) {
  box(x, y, w, h, o)
  const cy = sub ? y + h / 2 - 6 : y + h / 2 + (o.size ?? 34) * 0.35
  text(title, x + w / 2, cy, { size: o.size ?? 34, weight: 700, align: 'center', color: o.color ?? COL.ink, alpha: o.alpha })
  if (sub) text(sub, x + w / 2, cy + 42, { size: o.subSize ?? 30, align: 'center', color: o.subColor ?? COL.mut, alpha: o.alpha })
}
// 印章：圓角框＋旋轉的字，pop 進場
function stamp(x, y, str, p, color = COL.red, size = 46) {
  if (p <= 0) return
  const k = 1 + (1 - ease(clamp(p * 3))) * 0.6
  ctx.save()
  ctx.translate(x, y)
  ctx.rotate(-0.12)
  ctx.scale(k, k)
  ctx.globalAlpha = clamp(p * 3)
  ctx.font = `800 ${size}px ${FONT},${EMOJI}`
  const w = ctx.measureText(str).width + 40
  rr(-w / 2, -size * 0.85, w, size * 1.4, 10)
  ctx.lineWidth = 6
  ctx.strokeStyle = color
  ctx.stroke()
  ctx.fillStyle = color
  ctx.textAlign = 'center'
  ctx.fillText(str, 0, size * 0.2)
  ctx.restore()
}
function sticky(x, y, w, h, lines, p, color = COL.sticky) {
  if (p <= 0) return
  const dy = (1 - ease(p)) * -60
  ctx.save()
  ctx.globalAlpha = clamp(p * 2)
  ctx.translate(x + w / 2, y + h / 2 + dy)
  ctx.rotate(0.03)
  ctx.fillStyle = color
  ctx.fillRect(-w / 2, -h / 2, w, h)
  ctx.fillStyle = 'rgba(0,0,0,0.08)'
  ctx.fillRect(-w / 2, -h / 2, w, 14)
  ctx.restore()
  lines.forEach((ln, i) => text(ln.t, x + 28, y + 64 + dy + i * 48, { size: ln.size ?? 34, weight: ln.weight ?? 600, color: ln.color ?? COL.ink, alpha: clamp(p * 2) }))
}
function newspaper(x, y, w, h, title, alpha = 1) {
  box(x, y, w, h, { fill: COL.paper, stroke: COL.gray, lw: 4, r: 8, alpha })
  text(title, x + 26, y + 56, { size: 34, weight: 700, alpha })
  ctx.save()
  ctx.globalAlpha = alpha
  ctx.fillStyle = '#b4b2a9'
  for (let i = 0; i < 6; i++) {
    const ly = y + 92 + i * ((h - 120) / 6)
    ctx.fillRect(x + 26, ly, (w - 52) * (i % 3 === 2 ? 0.6 : 1) / 2 - 10, 10)
    ctx.fillRect(x + w / 2 + 6, ly, (w - 52) * (i % 2 ? 0.7 : 1) / 2 - 10, 10)
  }
  ctx.restore()
}
function arrow(x1, y1, x2, y2, color = COL.gray, lw = 6) {
  ctx.save()
  ctx.strokeStyle = color
  ctx.fillStyle = color
  ctx.lineWidth = lw
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke()
  const a = Math.atan2(y2 - y1, x2 - x1)
  ctx.beginPath()
  ctx.moveTo(x2, y2)
  ctx.lineTo(x2 - 26 * Math.cos(a - 0.45), y2 - 26 * Math.sin(a - 0.45))
  ctx.lineTo(x2 - 26 * Math.cos(a + 0.45), y2 - 26 * Math.sin(a + 0.45))
  ctx.closePath(); ctx.fill()
  ctx.restore()
}
function nameTag(key, cx, y, size = 30) {
  text(CHARS[key].badge + ' ' + CHARS[key].name, cx, y, { size, weight: 700, align: 'center' })
}
function floor(y = 780, bottom = 900) {
  ctx.fillStyle = COL.floor
  ctx.fillRect(0, y, W, bottom - y)
}
function chapter(label, alpha = 1) {
  ctx.save()
  ctx.globalAlpha = alpha
  ctx.font = `800 34px ${FONT}`
  const w = ctx.measureText(label).width + 44
  rr(36, 30, w, 62, 31)
  ctx.fillStyle = COL.clay; ctx.fill()
  ctx.fillStyle = '#fff'; ctx.textBaseline = 'middle'
  ctx.fillText(label, 58, 62)
  ctx.restore()
}
function caption(title, sub, alpha = 1) {
  ctx.save()
  ctx.globalAlpha = alpha
  ctx.fillStyle = 'rgba(255,253,247,0.97)'
  ctx.fillRect(0, 900, W, 180)
  ctx.fillStyle = COL.line
  ctx.fillRect(0, 900, W, 3)
  ctx.restore()
  text(title, 80, 972, { size: 52, weight: 800, alpha })
  if (sub) text(sub, 80, 1036, { size: 36, color: COL.mut, alpha })
}
function lock(x, y, s, alpha) {
  ctx.save()
  ctx.globalAlpha = alpha
  ctx.strokeStyle = COL.ink; ctx.lineWidth = s * 0.16
  ctx.beginPath(); ctx.arc(x + s / 2, y + s * 0.42, s * 0.28, Math.PI, 0); ctx.stroke()
  ctx.fillStyle = COL.amber
  rr(x + s * 0.12, y + s * 0.42, s * 0.76, s * 0.56, s * 0.08); ctx.fill()
  ctx.fillStyle = COL.amberFill
  ctx.fillRect(x + s * 0.46, y + s * 0.58, s * 0.08, s * 0.22)
  ctx.restore()
}
function dice(x, y, s, face, rot = 0) {
  const pips = { 1: [[0.5, 0.5]], 2: [[0.28, 0.28], [0.72, 0.72]], 3: [[0.25, 0.25], [0.5, 0.5], [0.75, 0.75]], 4: [[0.28, 0.28], [0.72, 0.28], [0.28, 0.72], [0.72, 0.72]], 5: [[0.25, 0.25], [0.75, 0.25], [0.5, 0.5], [0.25, 0.75], [0.75, 0.75]], 6: [[0.28, 0.22], [0.72, 0.22], [0.28, 0.5], [0.72, 0.5], [0.28, 0.78], [0.72, 0.78]] }
  ctx.save()
  ctx.translate(x + s / 2, y + s / 2); ctx.rotate(rot); ctx.translate(-s / 2, -s / 2)
  rr(0, 0, s, s, s * 0.16); ctx.fillStyle = '#fff'; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = COL.ink; ctx.stroke()
  ctx.fillStyle = COL.ink
  for (const [px, py] of pips[face]) { ctx.beginPath(); ctx.arc(px * s, py * s, s * 0.08, 0, Math.PI * 2); ctx.fill() }
  ctx.restore()
}

// ── 劇本 ────────────────────────────────────────────────────────
const REPORTERS = ['features', 'models', 'commercial', 'policy', 'community', 'people', 'market', 'devpractice', 'classify']
const SLEEPERS = ['editor', ...REPORTERS]

const SCENES = [
  { label: '開場', start: 0, end: 8, draw(t, tick) {
    floor(700, H)
    SLEEPERS.forEach((k, i) => char(k, 'sleep', 100 + i * 175, 640, 16, tick + i))
    text('Claude News 小編輯部', W / 2, 300, { size: 96, weight: 800, align: 'center', alpha: ease(seg(t, 0.8, 2)) })
    text('一份每天的新聞日報，怎麼變成一座會查證的知識庫', W / 2, 400, { size: 44, align: 'center', color: COL.mut, alpha: ease(seg(t, 1.6, 2.8)) })
    if (t > 4.6) {
      const sh = Math.sin(t * 40) * 8 * (1 - seg(t, 6.6, 7.6))
      text('⏰', 1700 + sh, 200, { size: 96, align: 'center' })
      text('早上了，開工！', 1700, 290, { size: 40, weight: 700, align: 'center', color: COL.clay, alpha: seg(t, 5, 5.6) })
    }
  } },

  { label: '01 抓料', start: 8, end: 20, draw(t, tick) {
    floor()
    chapter('01 抓料')
    const srcs = [['Anthropic 官方', 'Blog・Status'], ['GitHub', 'Releases・Issues'], ['社群', 'HN・Reddit・RSS']]
    srcs.forEach(([a, b], i) => card(70, 150 + i * 200, 420, 160, a, b, { size: 40 }))
    for (let k = 0; k < 9; k++) {
      const t0 = 0.6 + k * 0.7
      const p = ease(seg(t, t0, t0 + 1.6))
      if (p <= 0 || p >= 1) continue
      const sy = 230 + (k % 3) * 200
      box(lerp(500, 660, p), lerp(sy, 420, p) - 34, 56, 70, { fill: COL.paper, stroke: COL.gray, lw: 3, r: 4 })
    }
    char('helper', 'wave', 700, 300, 22, tick)
    prop('press', 700 + 220, 300, 22, tick)
    nameTag('helper', 810, 540, 34)
    const np = ease(seg(t, 4.5, 6.2))
    newspaper(1320, 180 + (1 - np) * 40, 520, 460, '今日日報 news/10-03.md', np)
    caption('抓料：每天自動抓新聞，小幫手寫成繁體中文日報', '刻意延遲 26–30 小時：要的是穩定與深度，不追秒級快訊', ease(seg(t, 0.2, 0.8)))
  } },

  { label: '02 派工', start: 20, end: 35, draw(t, tick) {
    floor()
    chapter('02 派工')
    const ex = 700, ey = 110, s = 20
    if (t < 6) { char('editor', 'glasses', ex, ey, s, tick); prop('read', ex + 200, ey, s, tick) }
    else if (t < 9.5) {
      char('editor', 'wave', ex, ey, s, tick); prop('whistle', ex + 200, ey, s, tick)
      text('嗶——集合！', ex + 380, ey + 60, { size: 52, weight: 800, color: COL.clay, alpha: seg(t, 6.2, 6.8) })
    } else char('editor', 'still', ex, ey, s, tick)
    nameTag('editor', ex + 100, ey + 8 * s + 48, 34)
    REPORTERS.forEach((k, i) => {
      const p = ease(seg(t, 7 + i * 0.55, 7.6 + i * 0.55))
      if (p <= 0) return
      const x = 40 + i * 206, y = 470 + (1 - p) * 60
      ctx.save(); ctx.globalAlpha = p
      char(k, 'wave', x + 38, y, 13, tick + i)
      ctx.restore()
      text(CHARS[k].name, x + 103, y + 150, { size: 30, weight: 700, align: 'center', alpha: p })
      text(CHARS[k].badge, x + 103, y + 196, { size: 36, align: 'center', alpha: p })
    })
    caption('派工：主編讀完日報、逐則分類，吹哨派記者', '九類記者各管一塊領域，帽子就是他們的名牌', ease(seg(t, 0.2, 0.8)))
  } },

  { label: '03 寫 wiki', start: 35, end: 50, draw(t, tick) {
    floor()
    chapter('03 寫 wiki')
    const s = 16
    const desks = [['features', t > 9 ? 'radar' : 'write', t > 9 ? '功能雷達' : 'Claude Code 頁'], ['models', 'write', 'Opus 5.5 頁'], ['community', 'write', '社群工具頁'], ['commercial', 'write', '定價頁']]
    desks.forEach(([k, a, label], i) => {
      const x = 50 + i * 375
      char(k, 'wave', x, 150, s, tick + i)
      prop(a, x + 10 * s, 150, s, tick + i)
      nameTag(k, x + 9 * s, 150 + 8 * s + 46)
      text('✎ ' + label, x + 9 * s, 150 + 8 * s + 92, { size: 30, align: 'center', color: COL.mut })
    })
    const ea = t < 8 ? 'log' : 'shelf'
    char('editor', 'wave', 1560, 150, s, tick)
    prop(ea, 1560 + 10 * s, 150, s, tick)
    nameTag('editor', 1560 + 9 * s, 150 + 8 * s + 46)
    text(t < 8 ? '✎ 操作日誌' : '✎ 整理索引', 1560 + 9 * s, 150 + 8 * s + 92, { size: 30, align: 'center', color: COL.mut })
    const pages = ['Claude Code', 'Opus 5.5', '社群工具', '定價', '功能雷達', '操作日誌', '索引']
    pages.forEach((pg, i) => {
      const p = ease(seg(t, 2 + i * 1.4, 2.8 + i * 1.4))
      if (p <= 0) return
      const x = 100 + i * 250, y = 560 + (1 - p) * 30
      box(x, y, 225, 160, { fill: COL.paper, stroke: COL.greenFill, lw: 4, alpha: p })
      text('wiki', x + 20, y + 44, { size: 30, color: COL.green, weight: 700, alpha: p })
      text(pg, x + 112, y + 112, { size: 34, weight: 700, align: 'center', alpha: p })
    })
    caption('寫 wiki：每位記者只寫自己負責的頁', '每個事實只有一個家；主編整理索引、寫下不會遺忘的操作日誌', ease(seg(t, 0.2, 0.8)))
  } },

  { label: '04 查證', start: 50, end: 88, draw(t, tick) {
    floor()
    chapter('04 查證')
    if (t < 10) {
      // ① 記者不能自己上網：電話被鎖住，只能貼條子
      const s = 22, x = 120, y = 170
      if (t < 4.5) {
        char('features', 'still', x, y, s, tick)
        prop('phone', x + 10 * s, y, s, tick)
        lock(x + 10 * s, y + 10, 8 * s, ease(seg(t, 2, 2.6)))
      } else {
        char('features', 'wave', x, y, s, tick)
        prop('write', x + 10 * s, y, s, tick)
      }
      nameTag('features', x + 5 * s, y + 8 * s + 50, 34)
      if (t < 4.5) text('🚫 記者沒有 web 工具', x + 9 * s, y + 8 * s + 120, { size: 42, weight: 800, color: COL.redInk, align: 'center', alpha: seg(t, 2.4, 3) })
      sticky(760, 190, 680, 270, [{ t: '⚠️ 需主編查證', size: 48, weight: 800 }, { t: '議題：新功能的正式上線範圍', size: 36 }, { t: '建議查：官方說明中心', size: 36, color: COL.mut }], ease(seg(t, 5.2, 6.4)))
      if (t > 6.6) arrow(1470, 330, 1660, 330, COL.clay)
      text('交給主編', 1690, 344, { size: 40, weight: 800, color: COL.clay, alpha: seg(t, 6.8, 7.4) })
      caption('查證①：記者不能自己上網', '需要官方說明的事實不准用猜的，貼條子請主編查', ease(seg(t, 0.2, 0.8)))
    } else if (t < 21) {
      // ② 懸置標記上輸送帶；探針掃日報，命中就蓋「訊」通知記者；逾期的分兩條路
      const u = t - 10
      newspaper(70, 130, 440, 300, '今日日報')
      for (let i = 0; i < 2; i++) {
        const cx = 190 + i * 200, cy = 290
        const hit = u > 3
        ctx.save()
        ctx.strokeStyle = hit ? COL.amber : COL.greenFill
        ctx.lineWidth = 9
        ctx.globalAlpha = hit ? 0.95 : 0.6
        ctx.beginPath(); ctx.arc(cx, cy, 56 + (hit ? Math.sin(u * 10) * 6 : (u * 30 + i * 20) % 30), 0, Math.PI * 2); ctx.stroke()
        ctx.restore()
        text('探針', cx, cy + 12, { size: 32, weight: 700, align: 'center', color: hit ? COL.amber : COL.green })
      }
      text('兩個探針同時命中！', 290, 490, { size: 38, weight: 800, align: 'center', color: COL.amber, alpha: seg(u, 3, 3.5) })
      // 輸送帶
      ctx.fillStyle = '#5f5e5a'; ctx.fillRect(580, 640, 680, 26)
      ctx.fillStyle = '#888780'
      for (let k = 0; k < 14; k++) ctx.fillRect(580 + ((k * 50 + u * 90) % 680), 644, 22, 18)
      // 兩條 Lane（右側框）
      box(1290, 130, 590, 290, { fill: '#FAEEDA', stroke: COL.amber, lw: 4, alpha: seg(u, 5.8, 6.4) })
      text('Lane A：日報有新線索', 1320, 180, { size: 32, weight: 800, color: COL.amber, alpha: seg(u, 5.8, 6.4) })
      text('→ 記者用日報更新頁面', 1320, 224, { size: 30, color: COL.amber, alpha: seg(u, 5.8, 6.4) })
      box(1290, 450, 590, 320, { fill: '#E6F1FB', stroke: COL.blueFill, lw: 4, alpha: seg(u, 6.4, 7) })
      text('Lane B：逾期沒線索', 1320, 490, { size: 32, weight: 800, color: COL.blue, alpha: seg(u, 6.4, 7) })
      text('→ 主編上網查官方', 1320, 534, { size: 30, color: COL.blue, alpha: seg(u, 6.4, 7) })
      const qs = ['上線範圍', '定價生效日', '合作細節']
      const dest = [[1320, 290], [1320, 590], [1590, 590]]
      qs.forEach((q, i) => {
        const x0 = 600 + i * 230, y0 = 520
        const p = ease(seg(u, 6.6 + i * 1.1, 7.8 + i * 1.1))
        const x = lerp(x0, dest[i][0], p), y = lerp(y0, dest[i][1], p) - Math.sin(p * Math.PI) * 80
        card(x, y, 210, 110, q, null, { size: 30, fill: '#FAEEDA', stroke: COL.amber })
        text('❓', x + 14, y + 36, { size: 30 })
        if (i === 0) stamp(x + 170, y + 6, '訊 10-03', seg(u, 5, 5.6), COL.red, 30)
      })
      if (u > 3.6 && u < 5.2) {
        const p = ease(seg(u, 3.6, 5.1))
        ctx.fillStyle = COL.red
        ctx.beginPath(); ctx.arc(lerp(290, 700, p), lerp(420, 510, p) - Math.sin(p * Math.PI) * 140, 20, 0, Math.PI * 2); ctx.fill()
      }
      caption('查證②：沒查清楚的事先掛上 ❓，排隊等複查', '探針每天掃新日報，命中就蓋「訊」通知負責記者；逾期的分兩條路清', ease(seg(u, 0.2, 0.8)))
    } else if (t < 33) {
      // ③ 主編照優先序查一手來源
      const u = t - 21, s = 18
      char('editor', 'glasses', 60, 200, s, tick)
      prop('phone', 60 + 10 * s, 200, s, tick)
      nameTag('editor', 60 + 5 * s, 200 + 8 * s + 50, 34)
      const steps = ['① 官方說明中心', '② 官方文件 docs', '③ anthropic.com', '④ 官方帳號', '⑤ 具名媒體（只能寫「媒體稱」）']
      text('查證優先序', 560, 160, { size: 38, weight: 800, color: COL.clay })
      steps.forEach((sname, i) => {
        const on = u > 1 + i * 0.9
        box(560 + i * 28, 190 + i * 100, 620, 80, { fill: on ? '#E6F1FB' : COL.paper, stroke: on ? COL.blueFill : COL.line, lw: on ? 5 : 3 })
        text(sname, 588 + i * 28, 243 + i * 100, { size: 33, weight: on ? 700 : 500, color: on ? COL.blue : COL.mut })
      })
      const results = [
        [6.4, '✅ 改寫成事實', '附來源連結與查證日', '#EAF3DE', COL.greenFill, COL.green],
        [8, '🔎 查無官方說明', '改成 🔎，之後再看', '#F1EFE8', COL.gray, COL.mut],
        [9.6, '📰 只寫「媒體稱」', '不把媒體數字當官方', '#FAEEDA', COL.amber, COL.amber],
      ]
      results.forEach(([at, title, sub, fill, stroke, color], i) => {
        const y = 190 + i * 180
        const flipping = u > at - 0.3 && u < at + 0.3
        const sx = flipping ? Math.abs(Math.cos(clamp((u - at + 0.3) / 0.6) * Math.PI)) : 1
        ctx.save()
        ctx.translate(1470, y + 75); ctx.scale(sx, 1); ctx.translate(-1470, -(y + 75))
        if (u > at) card(1250, y, 440, 150, title, sub, { fill, stroke, color, lw: 5, size: 36 })
        else card(1250, y, 440, 150, '❓ 待查證', null, { fill: '#FAEEDA', stroke: COL.amber, size: 36 })
        ctx.restore()
      })
      caption('查證③：主編照優先序查一手來源', '查到就改寫成事實並附來源；只有媒體說法的數字，就老實寫「媒體稱」', ease(seg(u, 0.2, 0.8)))
    } else {
      // ④ 每週擲骰抽題
      const u = t - 33
      const rolling = u < 1.8
      dice(150, 240, 220, rolling ? 1 + (Math.floor(u * 12) % 6) : 4, rolling ? Math.sin(u * 14) * 0.5 : 0.08)
      dice(410, 290, 190, rolling ? 1 + (Math.floor(u * 9 + 3) % 6) : 6, rolling ? -Math.sin(u * 12) * 0.5 : -0.1)
      text('每週擲骰（種子綁週次）', 350, 570, { size: 36, weight: 700, align: 'center' })
      const qs = [['Q7　這個生效日期對嗎？', '證據：頁面第 102 行 ↔ 官方公告'], ['Q8　這個「首選」還成立嗎？', '證據：決策表 ↔ 本週日報']]
      qs.forEach(([q, ev], i) => {
        const p = ease(seg(u, 1.8 + i * 0.6, 2.4 + i * 0.6))
        if (p <= 0) return
        const y = 200 + i * 250
        box(760, y, 1000, 210, { fill: COL.paper, stroke: COL.line, alpha: p })
        text(q, 800, y + 80, { size: 40, weight: 700, alpha: p })
        const ok = u > 3 + i * 0.6
        text(ok ? '✅ ' + ev : '…翻頁面找證據', 800, y + 156, { size: 34, color: ok ? COL.green : COL.mut, alpha: p })
      })
      caption('查證④：每週擲骰抽題，自己質疑自己', '每一題都要帶回一行證據才算過；答不出來就變成待辦，回報使用者', ease(seg(u, 0.2, 0.8)))
    }
  } },

  { label: '05 退案', start: 88, end: 124, draw(t, tick) {
    floor()
    chapter('05 退案')
    if (t < 9) {
      // ① 複核記者翻垃圾桶：誤排除的撈回來改派，最多回退一次
      const u = t
      text('今天排除的新聞', 270, 330, { size: 34, weight: 700, align: 'center' })
      ctx.fillStyle = '#888780'; rr(130, 360, 280, 360, 16); ctx.fill()
      ctx.fillStyle = '#5f5e5a'; ctx.fillRect(110, 348, 320, 32)
      for (let k = 0; k < 4; k++) { ctx.fillStyle = '#b4b2a9'; ctx.fillRect(165 + k * 60, 410, 32, 270) }
      const s = 18
      char('classify', 'glasses', 470, 230, s, tick)
      prop('search', 470 + 10 * s, 230, s, tick)
      nameTag('classify', 470 + 5 * s, 230 + 8 * s + 50, 32)
      box(1320, 270, 520, 300, { fill: '#FBEAF0', stroke: '#D4537E', lw: 4 })
      text('🌐 社群記者收件匣', 1580, 320, { size: 34, weight: 700, align: 'center', color: '#72243E' })
      let cx = 220, cy = 340
      if (u > 1) { const p = ease(seg(u, 1, 2.6)); cx = lerp(220, 860, p); cy = lerp(340, 180, p) }
      if (u > 4) { const p = ease(seg(u, 4, 5.5)); cx = lerp(860, 1430, p); cy = lerp(180, 430, p) }
      if (u > 6.2) { const p = Math.sin(seg(u, 6.2, 7.2) * Math.PI); cx = 1430 - p * 170 }
      if (u > 0.5) card(cx, cy, 310, 100, 'Reddit 實測心得', null, { size: 32 })
      stamp(cx + 230, cy + 64, '誤排除', seg(u, 3, 3.6))
      if (u > 6.6) {
        ctx.fillStyle = COL.red; ctx.fillRect(1230, 270, 18, 300)
        sticky(1020, 610, 820, 170, [{ t: '一則最多回退一次', size: 40, weight: 800 }, { t: '再彈回來 → 待使用者裁示', size: 34 }], ease(seg(u, 6.8, 7.6)))
      }
      caption('退案①：複核記者翻垃圾桶', '主編排除錯的撈回來，改派給正確的記者；同一則最多回退一次', ease(seg(u, 0.2, 0.8)))
    } else if (t < 16) {
      // ② 規則檔比派工訊息大
      const u = t - 9, s = 20
      char('models', 'still', 160, 230, s, tick)
      nameTag('models', 160 + 5 * s, 230 + 8 * s + 50, 34)
      box(400, 190, 250, 320, { fill: '#185FA5', stroke: '#0C447C', lw: 6, r: 10 })
      text('規則檔', 525, 350, { size: 48, weight: 800, align: 'center', color: '#fff' })
      text('版控・單一來源', 525, 404, { size: 30, align: 'center', color: '#B5D4F4' })
      const p = ease(seg(u, 0.5, 2.2))
      const bounce = u > 2.2 ? Math.sin(seg(u, 2.2, 2.8) * Math.PI) * 40 : 0
      const sx = lerp(1500, 690, p) + bounce
      box(sx, 240, 560, 220, { fill: COL.paper, stroke: COL.gray, lw: 4 })
      text('派工單', sx + 30, 304, { size: 32, weight: 700, color: COL.mut })
      text('「今天順手改寫主線頁」', sx + 30, 384, { size: 38, weight: 700 })
      sticky(690, 560, 1100, 200, [{ t: '⚠️ 派工與規則牴觸', size: 44, weight: 800, color: COL.redInk }, { t: '照規則做（主線改寫已改成週更），回報主編', size: 34 }], ease(seg(u, 3.4, 4.4)), '#FCEBEB')
      caption('退案②：規則檔比派工訊息大', '派工要求違反規則時，記者照規則做，並在回報寫明牴觸與做法', ease(seg(u, 0.2, 0.8)))
    } else if (t < 24) {
      // ③ 主編抽驗回報，不符就退回補做
      const u = t - 16, s = 18
      char('editor', 'glasses', 80, 220, s, tick)
      prop('check', 80 + 10 * s, 220, s, tick)
      nameTag('editor', 80 + 5 * s, 220 + 8 * s + 50, 34)
      dice(250, 500, 130, u < 1.2 ? 1 + (Math.floor(u * 12) % 6) : 3, u < 1.2 ? Math.sin(u * 14) * 0.5 : 0)
      text('抽驗一項宣稱', 315, 690, { size: 32, weight: 700, align: 'center' })
      const back = u > 2.2 && u < 5.8
      const fx = back ? lerp(700, 1000, ease(seg(u, 2.4, 3.4))) : u >= 5.8 ? lerp(1000, 700, ease(seg(u, 5.8, 6.6))) : 700
      box(fx, 250, 420, 300, { fill: '#FAEEDA', stroke: COL.amber, lw: 5, r: 8 })
      ctx.fillStyle = COL.amber; ctx.fillRect(fx, 224, 160, 32)
      text('社群記者的回報', fx + 210, 326, { size: 34, weight: 700, align: 'center', color: COL.amber })
      text('宣稱：「已更新決策表」', fx + 210, 390, { size: 30, align: 'center' })
      if (u > 2 && u < 6) stamp(fx + 210, 480, '退回補做', seg(u, 2, 2.5))
      if (u > 6.6) stamp(fx + 210, 480, '✅ 通過', seg(u, 6.6, 7.1), COL.green)
      const ca = u < 2.2 ? 'write' : u < 4 ? 'sweat' : u < 6 ? 'write' : 'thumbs'
      char('community', ca === 'write' ? 'wave' : 'still', 1480, 220, s, tick)
      prop(ca, 1480 + 10 * s, 220, s, tick)
      nameTag('community', 1480 + 5 * s, 220 + 8 * s + 50, 34)
      caption('退案③：主編抽驗回報，不符就退回補做', '一次過還是退回、退回的原因，都記進操作日誌', ease(seg(u, 0.2, 0.8)))
    } else {
      // ④ 內容閘紅：wiki 進不了 master；不准改閘，修不好就停泊
      const u = t - 24, s = 16
      const green = u > 8.4
      text('內容閘', 290, 180, { size: 40, weight: 800, align: 'center' })
      ctx.fillStyle = '#2C2C2A'; rr(200, 200, 180, 440, 26); ctx.fill()
      const lights = [[COL.red, !green], ['#EF9F27', false], ['#97C459', green]]
      lights.forEach(([c, on], i) => {
        ctx.fillStyle = on ? c : '#444441'
        ctx.beginPath(); ctx.arc(290, 280 + i * 140, 56, 0, Math.PI * 2); ctx.fill()
      })
      const loop = u < 1 ? 0 : u < 4.4 ? 1 : 2
      card(460, 190, 460, 130, `修復迴圈 ${loop} / 2`, '只修內容本身', { size: 42 })
      char('editor', green ? 'still' : 'wave', 500, 380, s, tick)
      prop(green ? 'thumbs' : 'write', 500 + 10 * s, 380, s, tick)
      nameTag('editor', 500 + 5 * s, 380 + 8 * s + 46, 32)
      box(1130, 190, 650, 130, { fill: COL.paper, stroke: COL.gray, lw: 4 })
      text('閘腳本 check_*.py・基線檔', 1455, 270, { size: 36, weight: 700, align: 'center', color: COL.mut })
      if (u > 2.4 && u < 7.5) {
        const p = ease(seg(u, 2.4, 3.6))
        arrow(960, 420, lerp(960, 1110, p), lerp(420, 300, p), COL.mut, 8)
        if (u > 3.6) card(1130, 360, 650, 150, '🚫 hook：不准改閘來放行', '靠改閘變綠＝把閘拆掉', { fill: '#FCEBEB', stroke: COL.red, color: COL.redInk, size: 38, lw: 5 })
      }
      if (green) stamp(960, 700, '✅ 轉綠・commit', seg(u, 8.6, 9.2), COL.green, 46)
      box(1130, 560, 650, 170, { fill: '#F1EFE8', stroke: COL.line })
      text('如果兩圈還是紅：', 1160, 622, { size: 32, weight: 700, color: COL.mut })
      text('貼封條，wiki 停到 unmerged 分支', 1160, 682, { size: 32, color: COL.mut })
      caption('退案④：內容閘紅燈時，wiki 進不了 master', '只准修內容、不准改閘；修不好就先停在旁邊的分支，不會弄丟', ease(seg(u, 0.2, 0.8)))
    }
  } },

  { label: '06 上線', start: 124, end: 136, draw(t, tick) {
    floor()
    chapter('06 上線')
    const s = 20
    const a = t < 3.6 ? 'check' : t < 5.6 ? 'thumbs' : t < 8 ? 'press' : 'plane'
    char('editor', a === 'thumbs' ? 'still' : 'wave', 100, 200, s, tick)
    prop(a, 100 + 10 * s, 200, s, tick)
    nameTag('editor', 100 + 5 * s, 200 + 8 * s + 50, 34)
    const steps = [['測試全綠', 3.6], ['建網站', 5.6], ['一次 push', 8]]
    steps.forEach(([sname, at], i) => {
      const on = t > at
      card(90 + i * 320, 580, 290, 110, (on ? '✅ ' : '') + sname, null, { size: 36, fill: on ? '#EAF3DE' : COL.paper, stroke: on ? COL.greenFill : COL.line })
    })
    if (t > 8 && t < 10.4) {
      const p = ease(seg(t, 8, 10.2))
      const x = lerp(560, 1160, p), y = lerp(320, 300, p) - Math.sin(p * Math.PI) * 120
      ctx.save(); ctx.translate(x, y); ctx.rotate(-0.2)
      ctx.fillStyle = '#378ADD'
      ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(110, 36); ctx.lineTo(0, 72); ctx.lineTo(24, 36); ctx.closePath(); ctx.fill()
      ctx.restore()
    }
    box(1100, 140, 740, 560, { fill: COL.paper, stroke: COL.ink, lw: 5 })
    ctx.fillStyle = '#e6dfcd'; ctx.fillRect(1103, 143, 734, 58)
    text('GitHub Pages', 1470, 184, { size: 32, weight: 700, align: 'center', color: COL.mut })
    if (t > 10.2) {
      const p = ease(seg(t, 10.2, 11))
      text('Claude News', 1150, 276, { size: 50, weight: 800, color: COL.clay, alpha: p })
      ;[['今日日報', '#FAEEDA'], ['wiki 知識庫', '#EAF3DE'], ['每週週報', '#E6F1FB']].forEach(([n, f], i) => card(1150, 320 + i * 120, 640, 100, n, null, { size: 36, fill: f, stroke: COL.line, alpha: p }))
    }
    caption('上線：測試全綠、建網站，一次 push', '雲端每天排三班；本機和雲端走同一套規則與閘', ease(seg(t, 0.2, 0.8)))
  } },

  { label: '收尾', start: 136, end: 146, draw(t, tick) {
    floor(700, H)
    const fade = ease(seg(t, 4.5, 6.5))
    ;['editor', ...REPORTERS].forEach((k, i) => {
      ctx.save(); ctx.globalAlpha = 1 - fade
      char(k, 'wave', 50 + i * 185, 500, 13, tick + i)
      ctx.restore()
    })
    if (fade > 0) { ctx.save(); ctx.globalAlpha = fade; char('editor', 'sleep', 860, 600, 20, tick); ctx.restore() }
    text('查得到的寫進去，查不到的誠實標出來', W / 2, 250, { size: 64, weight: 800, align: 'center', alpha: ease(seg(t, 0.5, 1.6)) })
    text('Claude News・給需要深度與穩定資訊的工程師', W / 2, 340, { size: 40, align: 'center', color: COL.mut, alpha: ease(seg(t, 1.4, 2.4)) })
  } },
]
// ── 配時：劇本照原本的時間軸寫（約 2 分半），這裡壓成約 1 分鐘 ─────────
// 查證與退案是重點：四個橋段各自用折線對應，每段字幕至少停留約 3 秒。
const RETIME = {
  '開場': { dur: 4 }, '01 抓料': { dur: 5 }, '02 派工': { dur: 5.5 }, '03 寫 wiki': { dur: 5 },
  '04 查證': { dur: 18, knots: [[0, 0], [4.5, 10], [9, 21], [15, 33], [18, 38]] },
  '05 退案': { dur: 16, knots: [[0, 0], [4.5, 9], [8, 16], [12, 24], [16, 36]] },
  '06 上線': { dur: 4 }, '收尾': { dur: 3.5 },
}
// SHORT 由產生器注入：精簡版（約 1 分鐘）才重新配時，完整版照原劇本時間軸
if (SHORT) {
  let acc = 0
  for (const sc of SCENES) {
    const od = sc.end - sc.start
    const r = RETIME[sc.label]
    sc.knots = r.knots ?? [[0, 0], [r.dur, od]]
    sc.start = acc
    acc += r.dur
    sc.end = acc
  }
}
// 新時間軸的場內時間 → 劇本原本的場內時間（折線內插）
function scriptTime(sc, u) {
  if (!sc.knots) return u
  const k = sc.knots
  for (let i = 1; i < k.length; i++) {
    if (u <= k[i][0]) return lerp(k[i - 1][1], k[i][1], (u - k[i - 1][0]) / (k[i][0] - k[i - 1][0]))
  }
  return k[k.length - 1][1]
}
const TOTAL = SCENES[SCENES.length - 1].end

// ── 播放器 ──────────────────────────────────────────────────────
let T = 0, playing = true, last = null
const sl = document.getElementById('sl'), pp = document.getElementById('pp'), clock = document.getElementById('clock'), chEl = document.getElementById('ch')
const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`
SCENES.forEach((sc) => {
  const b = document.createElement('button')
  b.textContent = sc.label
  b.onclick = () => { T = sc.start + 0.01; render() }
  chEl.appendChild(b)
})
function render() {
  const sc = SCENES.find((s) => T >= s.start && T < s.end) ?? SCENES[SCENES.length - 1]
  ctx.fillStyle = COL.stage
  ctx.fillRect(0, 0, W, H)
  const tick = Math.floor(T * 3)
  sc.draw(scriptTime(sc, T - sc.start), tick)
  // 場景交界淡入
  const k = 1 - seg(T - sc.start, 0, 0.35)
  if (k > 0 && sc.start > 0) { ctx.fillStyle = `rgba(247,243,232,${k})`; ctx.fillRect(0, 0, W, H) }
  sl.value = Math.round((T / TOTAL) * 1000)
  clock.textContent = `${fmt(T)} / ${fmt(TOTAL)}`
  ;[...chEl.children].forEach((b, i) => b.classList.toggle('on', SCENES[i] === sc))
}
function loop(now) {
  if (last !== null && playing) {
    T += (now - last) / 1000
    if (T >= TOTAL) { T = TOTAL - 0.001; playing = false; pp.textContent = '▶ 重播' }
  }
  last = now
  render()
  requestAnimationFrame(loop)
}
pp.onclick = () => {
  if (!playing && T >= TOTAL - 0.01) T = 0
  playing = !playing
  pp.textContent = playing ? '⏸ 暫停' : '▶ 播放'
}
sl.oninput = () => { T = (sl.value / 1000) * TOTAL; render() }
document.addEventListener('keydown', (e) => {
  if (e.code === 'Space') { e.preventDefault(); pp.click() }
  if (e.code === 'ArrowRight') T = Math.min(TOTAL - 0.01, T + 5)
  if (e.code === 'ArrowLeft') T = Math.max(0, T - 5)
})
// 給驗收用：?t=秒數 直接停在該格
const q = new URLSearchParams(location.search).get('t')
if (q !== null) { T = Number(q); playing = false; pp.textContent = '▶ 播放' }
window.__story = { seek: (s) => { T = s; playing = false; render() }, scenes: SCENES.map((s) => [s.label, s.start, s.end]) }
requestAnimationFrame(loop)
