#!/usr/bin/env python3
"""
Asia Tech News Feed — Daily Scraper
Scrapes 12 news sources, filters for SE Asia + keywords,
summarizes via Claude API, generates Jekyll posts + TSV for Google Sheets.
"""

import os
import sys
import json
import time
import hashlib
import re
import csv
import io
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import feedparser
from bs4 import BeautifulSoup
from dateutil import parser as dateparser
import pytz
import anthropic

   except Exception:
        return None


def is_recent(dt: datetime | None) -> bool:
    """Return True if within the lookback window."""
    if not dt:
        return True  # assume recent if no date
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    return dt >= cutoff


def article_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:10]


def is_relevant(text: str) -> tuple[bool, list[str]]:
    """Check if text matches keywords. Returns (matched, matched_keywords)."""
    t = text.lower()
    matched_kw = [k for k in KEYWORDS if k.lower() in t]
    matched_sea = [s for s in SE_ASIA_TERMS if s.lower() in t]
    # Must match at least 1 keyword. SE Asia match is a bonus but not required
    # for sources that are already SE Asia-focused.
    return bool(matched_kw), matched_kwly 60-80 words. Journalist style. No fluff.>",
  "key_point_1": "<First key takeaway — factual, journalist style, unique angle, 1-2 sentences>",
  "key_point_2": "<Second key takeaway — factual, journalist style, unique angle, 1-2 sentences>",
  "key_point_3": "<Third key takeaway — factual, journalist style, unique angle, 1-2 sentences>",
  "tags": ["<tag1>", "<tag2>", "<tag3>"]
}}

Tags must be from: semiconductor, electronics, logistics, pharmaceutical, biotechnology, AI, machine vision, automation, technology
Return ONLY the JSON. No markdown, no explanation."""

        try:
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}]
            )
            raw = message.content[0].text.strip()
            # Strip any markdown code fences
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            data = json.loads(raw)
            article["summary"] = data.get("summary", article["title"])[:400]
            article["key_points"] = [
                data.get("key_point_1", ""),
                data.get("key_point_2", ""),
                data.get("key_point_3", ""),
            ]
            article["tags"] = data.get("tags", [])[:4]
        except Exception as e:
            print(f"    ⚠ Claude error: {e}")
            article["summary"] = (article.get("summary_raw") or article["title"])[:320]
            article["key_points"] = ["", "", ""]
            article["tags"] = article.get("matched_keywords", [])[:3]

        summarized.append(article)
        # Respect API rate limits
        if idx < len(articles) - 1:
            time.sleep(0.5)

    return summarized


# ─────────────────────────────────────────────────────────────────────────────
# DEDUPLICATION
# ─────────────────────────────────────────────────────────────────────────────

def deduplicate(articles: list[dict]) -> list[dict]:
    """Remove near-duplicate articles by URL and title similarity."""
    seen_urls = set()
    seen_titles = set()
    unique = []
    for a in articles:
        url_key = a["url"].split("?")[0].rstrip("/")
        title_key = re.sub(r"[^a-z0-9]", "", a["title"].lower())[:60]
        if url_key in seen_urls or title_key in seen_titles:
            continue
        seen_urls.add(url_key)
        seen_titles.add(title_key)
        unique.append(a)
    return unique


# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT GENERATION
# ─────────────────────────────────────────────────────────────────────────────

TAG_CLASS_MAP = {
    "ai": "ai", "artificial intelligence": "ai",
    "semiconductor": "semi", "electronics": "semi",
    "biotechnology": "bio", "biotech": "bio", "pharmaceutical": "bio",
    "automation": "auto", "machine vision": "auto", "robotics": "auto",
    "logistics": "logis", "supply chain": "logis",
}

def tag_html(tag: str) -> str:
    cls = TAG_CLASS_MAP.get(tag.lower(), "")
    return f'<span class="tag {cls}">{tag}</span>'


def render_news_table(articles: list[dict]) -> str:
    """Render HTML table for Jekyll post body."""
    rows = []
    for i, a in enumerate(articles, 1):
        tags_html = "".join(tag_html(t) for t in (a.get("tags") or []))
        kp = a.get("key_points", ["", "", ""])
        date_str = a["date"].strftime("%d %b %Y") if a.get("date") else "—"
        url = a["url"]

        row = f"""<tr>
  <td class="col-num">{i}</td>
  <td class="col-source"><span class="source-badge">{a['short']}</span></td>
  <td class="col-title"><span class="article-title">{a['title']}</span></td>
  <td class="col-summary">{a.get('summary','')}</td>
  <td class="col-points"><ul class="key-points">
    <li>{kp[0]}</li>
    <li>{kp[1]}</li>
    <li>{kp[2]}</li>
  </ul></td>
  <td class="col-tags">{tags_html}</td>
  <td class="col-date">{date_str}</td>
  <td class="col-link"><a class="btn-link" href="{url}" target="_blank" rel="noopener">Read</a></td>
</tr>"""
        rows.append(row)

    table = """<table class="news-table">
<thead>
<tr>
  <th class="col-num">#</th>
  <th class="col-source">Source</th>
  <th class="col-title">Title</th>
  <th class="col-summary">Summary</th>
  <th class="col-points">Key Points</th>
  <th class="col-tags">Topics</th>
  <th class="col-date">Date</th>
  <th class="col-link">Link</th>
</tr>
</thead>
<tbody>
""" + "\n".join(rows) + "\n</tbody>\n</table>"
    return table


def render_tsv(articles: list[dict]) -> str:
    """Generate TSV string for Google Sheets paste."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter="\t", quoting=csv.QUOTE_ALL)
    writer.writerow([
        "#", "Source", "Title", "Summary (80 words)",
        "Key Point 1", "Key Point 2", "Key Point 3",
        "Topics", "Date", "URL"
    ])
    for i, a in enumerate(articles, 1):
        kp = a.get("key_points", ["", "", ""])
        date_str = a["date"].strftime("%Y-%m-%d") if a.get("date") else ""
        tags = ", ".join(a.get("tags") or [])
        writer.writerow([
            i,
            a.get("source", ""),
            a.get("title", ""),
            a.get("summary", ""),
            kp[0] if len(kp) > 0 else "",
            kp[1] if len(kp) > 1 else "",
            kp[2] if len(kp) > 2 else "",
            tags,
            date_str,
            a.get("url", ""),
        ])
    return output.getvalue()


def write_jekyll_post(articles: list[dict], run_date: datetime) -> Path:
    """Write Jekyll post markdown file."""
    date_str = run_date.strftime("%Y-%m-%d")
    slug = f"{date_str}-asia-tech-news-digest"
    filename = POSTS_DIR / f"{slug}.md"

    # Write TSV to assets
    tsv_filename = f"news-{date_str}.tsv"
    tsv_path = ASSETS_DIR / tsv_filename
    tsv_path.write_text(render_tsv(articles), encoding="utf-8")

    table_html = render_news_table(articles)
    sources_used = sorted(set(a["short"] for a in articles))

    front_matter = f"""---
layout: post
title: "Asia Tech News Digest — {run_date.strftime('%B %d, %Y')}"
date: {run_date.strftime('%Y-%m-%d %H:%M:%S')} +0800
articles_count: {len(articles)}
sources_count: {len(sources_used)}
sources: {json.dumps(sources_used)}
csv_file: /assets/data/{tsv_filename}
---
"""
    filename.write_text(front_matter + "\n" + table_html + "\n", encoding="utf-8")
    print(f"✅ Jekyll post written: {filename}")
    return filename


def build_email_html(articles: list[dict], run_date: datetime) -> str:
    """Build a compact HTML email summary for approval."""
    rows = ""
    for i, a in enumerate(articles, 1):
        kp = a.get("key_points", ["", "", ""])
        tags = " · ".join(a.get("tags") or [])
        date_str = a["date"].strftime("%d %b") if a.get("date") else ""
        rows += f"""
<tr style="border-bottom:1px solid #eee;">
  <td style="padding:10px 8px;font-weight:700;color:#666;width:28px;">{i}</td>
  <td style="padding:10px 8px;width:70px;"><span style="background:#edf2f7;color:#2b6cb0;padding:2px 7px;border-radius:3px;font-size:11px;font-weight:700;">{a['short']}</span></td>
  <td style="padding:10px 8px;">
    <div style="font-weight:600;color:#1a3a5c;margin-bottom:4px;">{a['title']}</div>
    <div style="font-size:12px;color:#555;margin-bottom:6px;">{a.get('summary','')}</div>
    <div style="font-size:11px;color:#888;">• {kp[0]}<br>• {kp[1]}<br>• {kp[2]}</div>
    <div style="margin-top:6px;">
      <span style="font-size:11px;color:#718096;">{tags}</span>
      <span style="font-size:11px;color:#718096;margin-left:10px;">{date_str}</span>
      <a href="{a['url']}" style="font-size:11px;color:#e84545;margin-left:10px;">Read →</a>
    </div>
  </td>
</tr>"""

    return f"""<!DOCTYPE html>
<html>
<body style="font-family:Segoe UI,sans-serif;max-width:800px;margin:0 auto;padding:20px;color:#2d3748;">
  <div style="background:#1a3a5c;color:#fff;padding:20px 24px;border-radius:8px 8px 0 0;">
    <h2 style="margin:0;font-size:1.2rem;">⚡ Asia Tech News Digest — {run_date.strftime('%B %d, %Y')}</h2>
    <p style="margin:6px 0 0;font-size:13px;color:rgba(255,255,255,0.7);">{len(articles)} articles · Filtered for SE Asia + tech keywords · Awaiting your approval</p>
  </div>
  <div style="background:#fff5e6;border:1px solid #f6ad55;border-radius:0 0 8px 8px;padding:14px 20px;margin-bottom:20px;">
    <strong>📋 Action required:</strong> Review the {len(articles)} articles below.
    To <strong>publish</strong>, merge the pull request on GitHub.
    To <strong>skip</strong>, simply close the PR without merging.
  </div>
  <table style="width:100%;border-collapse:collapse;">
    {rows}
  </table>
  <div style="margin-top:20px;padding:14px;background:#f7fafc;border-radius:6px;font-size:12px;color:#718096;text-align:center;">
    Auto-generated by Asia Tech News Feed · GitHub Actions
  </div>
</body>
</html>"""


def write_email_file(html: str, run_date: datetime) -> Path:
    """Write email HTML to file for GitHub Actions to read."""
    email_path = Path(__file__).parent.parent / "_email_preview.html"
    email_path.write_text(html, encoding="utf-8")
    return email_path


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    run_date = datetime.now(SGT)
    print(f"\n🌏 Asia Tech News Feed — {run_date.strftime('%Y-%m-%d %H:%M SGT')}")
    print("=" * 60)

    all_articles = []

    for source in SOURCES:
        print(f"\n📰 [{source['short']}] {source['name']}")
        try:
            if source.get("rss") or source["type"] == "rss":
                raw = fetch_rss(source)
            else:
                raw = fetch_scrape(source)
            print(f"  → {len(raw)} items fetched")
        except Exception as e:
            print(f"  ✖ Error: {e}")
            continue

        for article in raw:
            if not is_recent(article.get("date")):
                continue
            combined = f"{article['title']} {article.get('summary_raw','')}"
            matched, kws = is_relevant(combined)
            if not matched:
                continue
            article["matched_keywords"] = kws
            all_articles.append(article)

    print(f"\n📊 {len(all_articles)} relevant articles found before dedup")
    all_articles = deduplicate(all_articles)
    print(f"📊 {len(all_articles)} after deduplication")

    # Sort by date descending, take top MAX_ARTICLES
    all_articles.sort(key=lambda x: x.get("date") or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    all_articles = all_articles[:MAX_ARTICLES]
    print(f"📊 Top {len(all_articles)} selected")

    if not all_articles:
        print("\n⚠ No articles matched. Exiting without creating post.")
        # Write a signal file for GitHub Actions
        Path("/tmp/no_articles.flag").touch()
        sys.exit(0)

    # Fetch full text for better summaries (optional, best-effort)
    print("\n📖 Fetching article full text...")
    for a in all_articles[:MAX_ARTICLES]:
        a["full_text"] = fetch_full_text(a["url"])
        time.sleep(0.3)

    # Summarize
    print("\n🤖 Summarizing with Claude...")
    all_articles = summarize_with_claude(all_articles)

    # Write outputs
    print("\n📝 Writing outputs...")
    post_path = write_jekyll_post(all_articles, run_date)

    email_html = build_email_html(all_articles, run_date)
    email_path = write_email_file(email_html, run_date)

    # Write JSON for GitHub Actions to read PR description
    summary_json = {
        "date": run_date.strftime("%Y-%m-%d"),
        "count": len(all_articles),
        "sources": sorted(set(a["short"] for a in all_articles)),
        "post_file": str(post_path.name),
        "articles": [
            {"title": a["title"], "source": a["short"], "url": a["url"]}
            for a in all_articles[:5]  # first 5 for PR description
        ],
    }
    json_path = Path(__file__).parent.parent / "_digest_meta.json"
    json_path.write_text(json.dumps(summary_json, indent=2), encoding="utf-8")

    print(f"\n✅ Done! {len(all_articles)} articles → {post_path.name}")
    print(f"📧 Email preview: {email_path}")


if __name__ == "__main__":
    main()
