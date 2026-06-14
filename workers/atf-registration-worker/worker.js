/**
 * ATF Registration Worker
 * POST /register  — saves lead to D1, returns {success:true} or {error:"..."}
 * GET  /health    — liveness check
 * GET  /admin     — password-protected CSV export (set ADMIN_SECRET in Worker env vars)
 */

const ALLOWED_ORIGIN = 'https://asiatechfeed.com';

// ── CORS helpers ───────────────────────────────────────────────────────────────
function corsHeaders(origin) {
  const allowed = [ALLOWED_ORIGIN, 'http://localhost:4000', 'http://127.0.0.1:4000'];
  const o = allowed.includes(origin) ? origin : ALLOWED_ORIGIN;
  return {
    'Access-Control-Allow-Origin':  o,
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age':       '86400',
  };
}

function json(data, status = 200, origin = '') {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) },
  });
}

// ── IP hashing (SHA-256, hex) ──────────────────────────────────────────────────
async function hashIP(ip) {
  const buf  = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(ip + 'atf-salt-2026'));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

// ── Validation ─────────────────────────────────────────────────────────────────
function validateEmail(e) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e); }
function validateName(n)  { return typeof n === 'string' && n.trim().length >= 2; }

// ── Main handler ───────────────────────────────────────────────────────────────
export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const url    = new URL(request.url);

    // Pre-flight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    // Health
    if (url.pathname === '/health' && request.method === 'GET') {
      return json({ status: 'ok', ts: new Date().toISOString() }, 200, origin);
    }

    // Admin export (simple secret-header auth)
    if (url.pathname === '/admin' && request.method === 'GET') {
      const secret = request.headers.get('X-Admin-Secret');
      if (!env.ADMIN_SECRET || secret !== env.ADMIN_SECRET) {
        return new Response('Unauthorized', { status: 401 });
      }
      const { results } = await env.DB.prepare(
        'SELECT id, name, email, country, interests, report, created_at FROM registrations ORDER BY created_at DESC'
      ).all();
      const header = 'id,name,email,country,interests,report,registered_at\n';
      const rows   = results.map(r =>
        [r.id, `"${r.name}"`, r.email, `"${r.country}"`, `"${r.interests}"`, r.report, r.created_at].join(',')
      ).join('\n');
      return new Response(header + rows, {
        headers: { 'Content-Type': 'text/csv', 'Content-Disposition': 'attachment; filename="registrations.csv"' },
      });
    }

    // Registration
    if (url.pathname === '/register' && request.method === 'POST') {
      let body;
      try { body = await request.json(); }
      catch { return json({ error: 'Invalid JSON' }, 400, origin); }

      const { name, email, country, interests = [], website, report = '' } = body;

      // Honeypot
      if (website) return json({ success: true }, 200, origin); // silent drop

      // Validate
      if (!validateName(name))    return json({ error: 'Invalid name' },    422, origin);
      if (!validateEmail(email))  return json({ error: 'Invalid email' },   422, origin);
      if (!country)               return json({ error: 'Country required' }, 422, origin);

      const ip     = request.headers.get('CF-Connecting-IP') || 'unknown';
      const ipHash = await hashIP(ip);
      const interestsJson = JSON.stringify(Array.isArray(interests) ? interests : []);

      try {
        await env.DB.prepare(
          'INSERT INTO registrations (name, email, country, interests, report, ip_hash) VALUES (?, ?, ?, ?, ?, ?)'
        ).bind(name.trim(), email.toLowerCase().trim(), country, interestsJson, report, ipHash).run();

        return json({ success: true }, 200, origin);

      } catch (err) {
        // UNIQUE constraint on (email, report) — already registered
        if (err.message && err.message.includes('UNIQUE')) {
          return json({ success: true, already: true }, 409, origin);
        }
        console.error('DB error:', err.message);
        return json({ error: 'Server error. Please try again.' }, 500, origin);
      }
    }

    return json({ error: 'Not found' }, 404, origin);
  },
};
