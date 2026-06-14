/**
 * ATF Registration Worker — with Email OTP verification
 *
 * Flow:
 *   1. POST /send-otp   → validate fields → generate 6-digit OTP → store in KV (10 min TTL)
 *                         → send OTP email via Resend → return {sent: true}
 *   2. POST /verify-otp → check OTP in KV → on match: insert D1 row, delete KV key
 *                         → return {success: true} → frontend unlocks PDF download
 *
 * Other endpoints:
 *   GET  /health  — liveness check
 *   GET  /admin   — CSV export (requires X-Admin-Secret header)
 *
 * Secrets (set via `wrangler secret put`):
 *   RESEND_API_KEY  — from resend.com
 *   ADMIN_SECRET    — protects /admin
 *
 * Bindings (wrangler.toml):
 *   DB         — D1 database (registrations table)
 *   OTP_STORE  — KV namespace (temporary OTP storage)
 */

const ALLOWED_ORIGINS = ['https://asiatechfeed.com', 'http://localhost:4000', 'http://127.0.0.1:4000'];
const FROM_EMAIL      = 'reports@asiatechfeed.com';
const OTP_TTL_SEC     = 600;   // 10 minutes
const MAX_ATTEMPTS    = 5;     // wrong guesses before lockout
const MAX_SENDS       = 3;     // resend limit per email per hour

// ── CORS ───────────────────────────────────────────────────────────────────────
function corsHeaders(origin) {
  const o = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
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

// ── Helpers ────────────────────────────────────────────────────────────────────
function validateEmail(e) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e); }
function validateName(n)  { return typeof n === 'string' && n.trim().length >= 2; }

function randomOTP() {
  const arr = new Uint32Array(1);
  crypto.getRandomValues(arr);
  return String(arr[0] % 1000000).padStart(6, '0');
}

async function hashIP(ip) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(ip + 'atf-salt-2026'));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

// ── Resend email sender ────────────────────────────────────────────────────────
async function sendOTPEmail(to, otp, apiKey) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type':  'application/json',
    },
    body: JSON.stringify({
      from:    `Asia Tech Feed <${FROM_EMAIL}>`,
      to:      [to],
      subject: `Your download code: ${otp}`,
      html: `
        <div style="font-family:'Segoe UI',system-ui,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px;background:#f5f7fa;">
          <div style="background:#1a3a5c;padding:20px 24px;border-radius:6px 6px 0 0;">
            <p style="margin:0;color:rgba(255,255,255,0.7);font-size:12px;letter-spacing:0.15em;text-transform:uppercase;">Asia Tech Feed · Special Report</p>
          </div>
          <div style="background:#ffffff;padding:32px 24px;border-radius:0 0 6px 6px;border:1px solid #dde3ec;border-top:none;">
            <h2 style="margin:0 0 8px;color:#1a3a5c;font-size:20px;font-weight:600;">Your verification code</h2>
            <p style="margin:0 0 28px;color:#718096;font-size:14px;">Enter this code on the download page. It expires in 10 minutes.</p>
            <div style="background:#f5f7fa;border:1px solid #dde3ec;border-radius:6px;padding:20px;text-align:center;margin-bottom:28px;">
              <span style="font-size:36px;font-weight:700;letter-spacing:0.2em;color:#1a3a5c;font-family:'Courier New',monospace;">${otp}</span>
            </div>
            <p style="margin:0;color:#a0aec0;font-size:12px;">If you didn't request this, ignore this email. No account was created.</p>
          </div>
          <p style="margin:16px 0 0;text-align:center;color:#a0aec0;font-size:11px;">
            Asia Tech Feed · <a href="https://asiatechfeed.com" style="color:#a0aec0;">asiatechfeed.com</a>
          </p>
        </div>`,
      text: `Your Asia Tech Feed download code is: ${otp}\n\nEnter this on the download page. It expires in 10 minutes.\n\nIf you didn't request this, ignore this email.`,
    }),
  });
  return res.ok;
}

// ── Main handler ───────────────────────────────────────────────────────────────
export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const url    = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    // Health
    if (url.pathname === '/health' && request.method === 'GET') {
      return json({ status: 'ok', ts: new Date().toISOString() }, 200, origin);
    }

    // ── Admin CSV export ───────────────────────────────────────────────────────
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

    // ── POST /send-otp ─────────────────────────────────────────────────────────
    if (url.pathname === '/send-otp' && request.method === 'POST') {
      let body;
      try { body = await request.json(); }
      catch { return json({ error: 'Invalid JSON' }, 400, origin); }

      const { name, email, country, interests = [], website, report = '' } = body;

      // Honeypot
      if (website) return json({ sent: true }, 200, origin);

      // Validate
      if (!validateName(name))   return json({ error: 'Invalid name' },    422, origin);
      if (!validateEmail(email)) return json({ error: 'Invalid email' },   422, origin);
      if (!country)              return json({ error: 'Country required' }, 422, origin);

      if (!env.RESEND_API_KEY) {
        return json({ error: 'Email service not configured. Contact site admin.' }, 500, origin);
      }

      // Rate limit: max MAX_SENDS per email per hour
      const rateKey   = `rate:${email.toLowerCase()}`;
      const rateRaw   = await env.OTP_STORE.get(rateKey);
      const sendCount = rateRaw ? parseInt(rateRaw, 10) : 0;
      if (sendCount >= MAX_SENDS) {
        return json({ error: 'Too many codes requested. Please wait an hour and try again.' }, 429, origin);
      }

      // Generate OTP and store with form data
      const otp    = randomOTP();
      const stored = JSON.stringify({
        otp,
        name,
        email: email.toLowerCase().trim(),
        country,
        interests,
        report,
        attempts: 0,
      });
      const otpKey = `otp:${email.toLowerCase().trim()}`;

      await Promise.all([
        env.OTP_STORE.put(otpKey, stored, { expirationTtl: OTP_TTL_SEC }),
        env.OTP_STORE.put(rateKey, String(sendCount + 1), { expirationTtl: 3600 }),
      ]);

      const sent = await sendOTPEmail(email.trim(), otp, env.RESEND_API_KEY);
      if (!sent) {
        return json({ error: 'Failed to send email. Please try again.' }, 502, origin);
      }

      return json({ sent: true }, 200, origin);
    }

    // ── POST /verify-otp ───────────────────────────────────────────────────────
    if (url.pathname === '/verify-otp' && request.method === 'POST') {
      let body;
      try { body = await request.json(); }
      catch { return json({ error: 'Invalid JSON' }, 400, origin); }

      const { email, code } = body;
      if (!email || !code) return json({ error: 'Missing email or code' }, 400, origin);

      const otpKey = `otp:${email.toLowerCase().trim()}`;
      const raw    = await env.OTP_STORE.get(otpKey);

      if (!raw) {
        return json({ error: 'Code expired or not found. Please request a new one.' }, 410, origin);
      }

      const stored = JSON.parse(raw);

      // Attempt limit
      if (stored.attempts >= MAX_ATTEMPTS) {
        await env.OTP_STORE.delete(otpKey);
        return json({ error: 'Too many incorrect attempts. Please request a new code.' }, 429, origin);
      }

      // Wrong code — increment attempt counter and re-save
      if (code.trim() !== stored.otp) {
        stored.attempts += 1;
        await env.OTP_STORE.put(otpKey, JSON.stringify(stored), { expirationTtl: OTP_TTL_SEC });
        const left = MAX_ATTEMPTS - stored.attempts;
        return json({ error: `Incorrect code. ${left} attempt${left === 1 ? '' : 's'} remaining.` }, 422, origin);
      }

      // ✅ Correct — delete OTP, insert registration into D1
      await env.OTP_STORE.delete(otpKey);

      const ip     = request.headers.get('CF-Connecting-IP') || 'unknown';
      const ipHash = await hashIP(ip);
      const interestsJson = JSON.stringify(Array.isArray(stored.interests) ? stored.interests : []);

      try {
        await env.DB.prepare(
          'INSERT INTO registrations (name, email, country, interests, report, ip_hash) VALUES (?, ?, ?, ?, ?, ?)'
        ).bind(stored.name.trim(), stored.email, stored.country, interestsJson, stored.report, ipHash).run();

        return json({ success: true }, 200, origin);

      } catch (err) {
        // Already registered — still allow download
        if (err.message && err.message.includes('UNIQUE')) {
          return json({ success: true, already: true }, 200, origin);
        }
        console.error('DB error:', err.message);
        return json({ error: 'Server error. Please try again.' }, 500, origin);
      }
    }

    return json({ error: 'Not found' }, 404, origin);
  },
};
