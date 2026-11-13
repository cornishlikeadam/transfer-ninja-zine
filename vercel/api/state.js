// Saves everything you change after unlocking: ticks, checks, notes, scores, stages, logs,
// GPA picks, Common App writing and the document library.
// Storage: a private Vercel Blob store, encrypted with a key derived from TUTOR_CODE.
// Each section carries its own timestamp, so two devices merge section by section.
const crypto = require('crypto');
const { put, get } = require('@vercel/blob');

const STATE = 'tn/state.enc';
const LIB = 'tn/library.enc';

function same(a, b) {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
}
function key() { return crypto.scryptSync(String(process.env.TUTOR_CODE), 'tn-state-v1', 32); }
function seal(obj) {
  const iv = crypto.randomBytes(12), c = crypto.createCipheriv('aes-256-gcm', key(), iv);
  const body = Buffer.concat([c.update(JSON.stringify(obj), 'utf8'), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), body]);
}
function open(buf) {
  const d = crypto.createDecipheriv('aes-256-gcm', key(), buf.subarray(0, 12));
  d.setAuthTag(buf.subarray(12, 28));
  return JSON.parse(Buffer.concat([d.update(buf.subarray(28)), d.final()]).toString('utf8'));
}
async function read(path) {
  const r = await get(path, { access: 'private', useCache: false });
  if (!r || r.statusCode !== 200) return { data: null, etag: null };
  const buf = Buffer.from(await new Response(r.stream).arrayBuffer());
  return { data: open(buf), etag: r.blob.etag };
}
async function write(path, obj, etag) {
  const opts = { access: 'private', addRandomSuffix: false, contentType: 'application/octet-stream', cacheControlMaxAge: 60 };
  if (etag) opts.ifMatch = etag; else opts.allowOverwrite = true;
  return put(path, seal(obj), opts);
}
// Section-by-section merge: the newer timestamp wins.
function merge(base, incoming) {
  const out = Object.assign({}, base || {});
  let changed = false;
  for (const k of Object.keys(incoming || {})) {
    const a = out[k], b = incoming[k];
    if (!b || typeof b.t !== 'number') continue;
    if (!a || b.t > a.t) { out[k] = { v: b.v, t: b.t }; changed = true; }
  }
  return { out, changed };
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.status(405).json({ ok: false }); return; }
  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  body = body || {};
  const expected = String(process.env.TUTOR_CODE || '');
  if (!expected || !same(String(body.code || '').trim(), expected)) {
    await new Promise((r) => setTimeout(r, 600));
    res.status(401).json({ ok: false });
    return;
  }
  if (!process.env.BLOB_READ_WRITE_TOKEN) { res.status(503).json({ ok: false, reason: 'no-store' }); return; }
  const path = body.part === 'library' ? LIB : STATE;
  try {
    if (body.op === 'get') {
      const cur = await read(path);
      res.status(200).json({ ok: true, keys: (cur.data && cur.data.keys) || {}, savedAt: cur.data && cur.data.savedAt });
      return;
    }
    if (body.op === 'put') {
      for (let attempt = 0; attempt < 3; attempt++) {
        const cur = await read(path);
        const m = merge(cur.data && cur.data.keys, body.keys);
        if (!m.changed && cur.data) { res.status(200).json({ ok: true, keys: m.out, savedAt: cur.data.savedAt }); return; }
        const doc = { keys: m.out, savedAt: Date.now() };
        try {
          await write(path, doc, cur.etag);
          res.status(200).json({ ok: true, keys: m.out, savedAt: doc.savedAt });
          return;
        } catch (e) {
          if (!/precondition|etag|412/i.test(String(e && e.message))) throw e;
        }
      }
      res.status(409).json({ ok: false, reason: 'busy' });
      return;
    }
    res.status(400).json({ ok: false });
  } catch (e) {
    res.status(500).json({ ok: false, reason: 'store-error' });
  }
};
