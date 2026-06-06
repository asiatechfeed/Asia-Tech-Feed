# ⚡ Asia Tech News Feed

Automated daily news digest for Asia covering semiconductors, electronics, logistics, pharmaceutical, biotechnology, AI, machine vision, and automation.

---

## How It Works

1. **GitHub Actions runs daily at 10am SGT** — scrapes 12 news sources
2. **Claude AI summarizes** each article (80-word summary + 3 journalist-style key points)
3. **A Pull Request is created** with the staged content
4. **You receive an email** with the full digest preview
5. **Merge the PR** to publish to your GitHub Pages site
6. **TSV file included** in each digest — paste directly into Google Sheets

---

## Setup Instructions

### Step 1 — Create GitHub repository

1. Go to [github.com/new](https://github.com/new)
2. Name: `asia-news-feed`
3. Visibility: **Public** (required for free GitHub Pages)
4. Initialize with a README: **No**
5. Click **Create repository**

### Step 2 — Push this code

```bash
cd path/to/asia-news-feed
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/asia-news-feed.git
git push -u origin main
```

### Step 3 — Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **`gh-pages`** / root
4. Click **Save**

Your site will be live at: `https://YOUR_USERNAME.github.io/asia-news-feed`

> Note: The `gh-pages` branch is created automatically on first deploy. Set it after the first GitHub Actions run.

### Step 4 — Configure GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these secrets:

| Secret Name | Value | How to get it |
|---|---|---|
| `ANTHROPIC_API_KEY` | Your Claude API key | [console.anthropic.com](https://console.anthropic.com) |
| `GMAIL_USERNAME` | Your Gmail address | e.g. `you@gmail.com` |
| `GMAIL_APP_PASSWORD` | Gmail App Password | See below |
| `APPROVAL_EMAIL` | Email to send digest to | e.g. `you@gmail.com` |

#### Getting a Gmail App Password

1. Go to your Google Account → **Security**
2. Under "How you sign in to Google", enable **2-Step Verification** if not already
3. Search for **"App passwords"** in the search bar
4. Select app: **Mail** / device: **Other** → type "GitHub Actions"
5. Copy the 16-character password → use as `GMAIL_APP_PASSWORD`

### Step 5 — Update `_config.yml`

Edit `_config.yml` and replace:
```yaml
url: "https://YOUR_GITHUB_USERNAME.github.io"
```
with your actual GitHub username.

### Step 6 — Test the workflow

1. Go to **Actions** tab in your repo
2. Click **Daily Asia Tech News Digest**
3. Click **Run workflow** → select `force_publish: false`
4. Watch it run — you'll receive an email with the digest
5. Review and merge the PR to publish

---

## Daily Workflow (After Setup)

```
10:00 AM SGT   GitHub Actions runs automatically
               ↓
               Scrapes 12 news sources
               ↓
               Filters: SE Asia + keywords
               ↓
               Claude AI summarizes top 20 articles
               ↓
               Creates a PR + sends you an email
               ↓
You review    → Merge PR to publish
               OR close PR to skip
               ↓
               Site auto-deploys to GitHub Pages
```

---

## Sources Monitored

| Source | Focus |
|---|---|
| IC-PCB | PCB & semiconductor industry |
| Channel NewsAsia | SE Asia general news |
| Business Times SG | Singapore business |
| The Star MY | Malaysia news |
| Straits Times | Singapore news |
| Asia Manufacturing Review | Manufacturing |
| EDB Corporate News | Singapore investment news |
| EDB Industry News | Industry updates |
| EECO Thailand | Eastern Economic Corridor |
| TrendForce | Semiconductor & tech market data |
| Electronics Weekly | Electronics industry |
| Vision Systems Design | Machine vision & automation |

---

## Google Sheets Integration

Each digest includes a `.tsv` file. To import:
1. Open Google Sheets
2. **File** → **Import** → **Upload** the `.tsv` file
3. Or copy the table content and paste directly

---

## Customisation

**Change keywords** — Edit `KEYWORDS` list in `scripts/fetch_news.py`

**Change region filter** — Edit `SE_ASIA_TERMS` list

**Change article count** — Edit `MAX_ARTICLES = 20`

**Change schedule** — Edit the cron in `.github/workflows/daily_news.yml`:
- `"0 2 * * *"` = 10am SGT daily
- `"0 2 * * 1-5"` = weekdays only
- `"0 2 * * 1"` = Mondays only

**Add a new source** — Add a dict to the `SOURCES` list in `fetch_news.py`

---

## Cost Estimate

- **GitHub Actions**: Free (2,000 min/month on free tier; this job uses ~3 min/day)
- **GitHub Pages**: Free
- **Claude API (Haiku)**: ~$0.002–0.005 per day (20 articles × summarization)

---

## Troubleshooting

**No email received** → Check `GMAIL_APP_PASSWORD` secret; ensure 2FA is enabled on Gmail

**No articles found** → Some RSS feeds may be temporarily down; try manual trigger next day

**Jekyll build fails** → Run `bundle exec jekyll serve` locally to check for errors

**Rate limited by a news site** → The scraper has built-in delays; most sources use RSS which is always allowed
