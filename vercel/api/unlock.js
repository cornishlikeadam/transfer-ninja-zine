const crypto = require('crypto');
const gated = require('../gated.json');

function same(a, b) {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.status(405).json({ ok: false }); return; }
  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  const code = String((body && body.code) || '').trim();
  const expected = String(process.env.TUTOR_CODE || '');
  await new Promise((r) => setTimeout(r, 600));
  if (expected && same(code, expected)) { res.status(200).json({ ok: true, data: gated }); }
  else { res.status(401).json({ ok: false }); }
};
