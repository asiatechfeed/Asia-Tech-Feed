#!/usr/bin/env python3
"""
Asia Tech News Feed â Daily Scraper
Scrapes 20 news sources, filters for Asia + keywords,
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

# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# CONFIGURATION
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
POSTS_DIR = Path(__file__).parent.parent / "_posts"
ASSETS_DIR = Path(__file__).parent.parent / "assets" / "data"
POSTS_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

MAX_ARTICLES = 30
MAX_PER_DOMAIN = 3
LOOKBACK_DAYS = 3
SGT = pytz.timezone("Asia/Singapore")

# Domains that are inherently Asia-focused â no additional Asia term required
ASIA_FOCUSED_DOMAINS = {
    "channelnewsasia.com", "businesstimes.com.sg", "thestar.com.my",
    "straitstimes.com", "asiamanufacturingreview.com", "edb.gov.sg",
    "eeco.or.th", "focustaiwan.tw", "techinasia.com",
    "asia.nikkei.com", "kedglobal.com", "eetasia.com",
    "digitimes.com", "ic-pcb.com",
}

KEYWORDS = [
    "semiconductor", "electronics", "logistics", "pharmaceutical",
    "biotechnology", "biotech", "technology", "artificial intelligence",
    " ai ", "machine vision", "automation", "manufacturing",
    "chip", "wafer", "fab", "foundry", "pcb", "circuit board",
    "supply chain", "medtech", "drug", "vaccine", "robot",
]

SE_ASIA_TERMS = [
    "singapore", "malaysia", "thailand", "vietnam", "indonesia",
    "philippines", "myanmar", "cambodia", "laos", "brunei",
    "southeast asia", "se asia", "asean", "asia pacific", "apac",
    "penang", "johor", "selangor", "bangkok", "ho chi minh",
    "jakarta", "manila", "yangon", "phnom penh", "kuala lumpur",
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# NEWS SOURCES â (name, type, url, rss_url or scrape config)
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

SOURCES = [
    {
        "name": "IC-PCB",
        "short": "IC-PCB",
        "url": "https://www.ic-pcb.com/",
        "rss": "https://www.ic-pcb.com/feed/",
        "type": "rss",
    },
    {
        "name": "Channel NewsAsia",
        "short": "CNA",
        "url": "https://www.channelnewsasia.com/",
        "rss": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml",
        "type": "rss",
    },
    {
        "name": "Business Times SG",
        "short": "BT",
        "url": "https://www.businesstimes.com.sg/",
        "rss": "https://www.businesstimes.com.sg/rss/all-news",
        "type": "rss",
    },
    {
        "name": "The Star MY",
        "short": "Star",
        "url": "https://www.thestar.com.my/news/",
        "rss": "https://www.thestar.com.my/rss/News/Nation/",
        "type": "rss",
    },
    {
        "name": "Straits Times",
        "short": "ST",
        "url": "https://www.straitstimes.com/",
        "rss": "https://www.straitstimes.com/news/tech/rss.xml",
        "type": "rss",
    },
    {
        "name": "Asia Manufacturing Review",
        "short": "AMR",
        "url": "https://www.asiamanufacturingreview.com/",
        "rss": "https://www.asiamanufacturingreview.com/rss/news",
        "type": "rss",
    },
    {
        "name": "EDB Corporate News",
        "short": "EDB",
        "url": "https://www.edb.gov.sg/en/about-edb/media-releases-publications.html?tab=corporate-news",
        "type": "scrape",
        "article_selector": "article, .news-item, .media-item",
        "title_selector": "h2, h3, .title",
        "date_selector": ".date, time, .published",
        "link_selector": "a",
    },
    {
        "name": "EDB Industry News",
        "short": "EDB-I",
        "url": "https://www.edb.gov.sg/en/about-edb/media-releases-publications.html?tab=industry-news",
        "type": "scrape",
        "article_selector": "article, .news-item, .media-item",
        "title_selector": "h2, h3, .title",
        "date_selector": ".date, time, .published",
        "link_selector": "a",
    },
    {
        "name": "EECO Thailand",
        "short": "EECO",
        "url": "https://www.eeco.or.th/en",
        "rss": "https://www.eeco.or.th/en/feed/",
        "type": "rss",
    },
    {
        "name": "TrendForce",
        "short": "TrendForce",
        "url": "https://www.trendforce.com/news/",
        "rss": "https://www.trendforce.com/feed/",
        "type": "rss",
    },
    {
        "name": "Electronics Weekly",
        "short": "EW",
        "url": "https://www.electronicsweekly.com/news/",
        "rss": "https://www.electronicsweekly.com/feed/",
        "type": "rss",
    },
    {
        "name": "Vision Systems Design",
        "short": "VSD",
        "url": "https://www.vision-systems.com/",
        "rss": "https://www.vision-systems.com/rss.xml",
        "type": "rss",
    },
    {
        "name": "EE Times Asia",
        "short": "EETAsia",
        "url": "https://www.eetasia.com/",
        "rss": "https://www.eetasia.com/feed/",
        "type": "rss",
    },
    {
        "name": "DigiTimes",
        "short": "DigiTimes",
        "url": "https://www.digitimes.com/news/",
        "type": "scrape",
        "article_selector": "article, .news-item, .story-item",
        "title_selector": "h2, h3, .title",
        "date_selector": ".date, time, .published",
        "link_selector": "a",
    },
    {
        "name": "Nikkei Asia",
        "short": "NikkeiAsia",
        "url": "https://asia.nikkei.com/",
        "rss": "https://asia.nikkei.com/rss/feed/nar",
        "type": "rss",
    },
    {
        "name": "KED Global",
        "short": "KED",
        "url": "https://www.kedglobal.com/",
        "rss": "https://www.kedglobal.com/rss/",
        "type": "rss",
    },
    {
        "name": "Focus Taiwan",
        "short": "FocusTW",
        "url": "https://focustaiwan.tw/",
        "rss": "https://focustaiwan.tw/rss/aall.xml",
        "type": "rss",
    },
    {
        "name": "Tech in Asia",
        "short": "TechAsia",
        "url": "https://www.techinasia.com/",
        "rss": "https://www.techinasia.com/feed",
        "type": "rss",
    },
    {
        "name": "Automation.com",
        "short": "Automate",
        "url": "https://www.automation.com/",
        "rss": "https://www.automation.com/rss-feeds/all-content",
        "type": "rss",
    },
    {
        "name": "Semiconductor Engineering",
        "short": "SemiEng",
        "url": "https://semiengineering.com/",
        "rss": "https://semiengineering.com/feed/",
        "type": "rss",
    },
]


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# HELPERS
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

def normalize_date(raw_date) -> datetime | None:
    """Parse various date formats â timezone-aware UTC datetime."""
    if not raw_date:
        return None
    try:
        if isinstance(raw_date, time.struct_time):
            dt = datetime(*raw_date[:6], tzinfo=timezone.utc)
        else:
            dt = dateparser.parse(str(raw_date), fuzzy=True)
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
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
    # Must match at least 1 keyword. Asia match is a bonus but not required
    # for sources that are already Asia-focused.
    return bool(matched_kw), matched_kw


def clean_text(html_or_text: str) -> str:
    """Strip HTML tags and clean whitespace."""
    soup = BeautifulSoup(html_or_text, "lxml")
    text = soup.get_text(separator=" ", strip=True)
    return re.sub(r"\s+", " ", text).strip()


def fetch_url(url: str, timeout: int = 15) -> requests.Response | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        return resp
    except Exception as e:
        print(f"  â  Failed to fetch {url}: {e}")
        return None


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# FETCHING
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

def fetch_rss(source: dict) -> list[dict]:
    """Parse RSS/Atom feed and return raw articles."""
    rss_url = source.get("rss", source["url"])
    print(f"  ð¡ RSS: {rss_url}")
    try:
        feed = feedparser.parse(rss_url, request_headers=HEADERS)
        articles = []
        for entry in feed.entries:
            url = entry.get("link", "")
            title = entry.get("title", "")
            summary = entry.get("summary", entry.get("description", ""))
            pub_date = normalize_date(entry.get("published_parsed") or entry.get("updated_parsed"))
            articles.append({
                "title": clean_text(title),
                "url": url,
                "summary_raw": clean_text(summary)[:800],
                "date": pub_date,
                "source": source["name"],
                "short": source["short"],
            })
        return articles
    except Exception as e:
        print(f"  â  RSS parse error for {rss_url}: {e}")
        return []


def fetch_scrape(source: dict) -> list[dict]:
    """HTML scrape fallback."""
    print(f"  ð Scraping: {source['url']}")
    resp = fetch_url(source["url"])
    if not resp:
        return []
    soup = BeautifulSoup(resp.text, "lxml")
    articles = []

    # Try common article container patterns
    containers = (
        soup.select("article") or
        soup.select(".news-item") or
        soup.select(".media-item") or
        soup.select(".post") or
        soup.select("li.item")
    )

    for item in containers[:30]:
        link_tag = item.find("a", href=True)
        if not link_tag:
            continue
        url = urljoin(source["url"], link_tag["href"])
        title_tag = item.find(["h1", "h2", "h3", "h4"])
        title = clean_text(title_tag.get_text() if title_tag else link_tag.get_text())
        if not title or len(title) < 10:
            continue
        p_tag = item.find("p")
        summary = clean_text(p_tag.get_text() if p_tag else "")
        time_tag = item.find(["time", "span"], class_=re.compile("date|time|published", re.I))
        raw_date = ""
        if time_tag:
            raw_date = time_tag.get("datetime") or time_tag.get_text()
        pub_date = normalize_date(raw_date)
        articles.append({
            "title": title,
            "url": url,
            "summary_raw": summary[:800],
            "date": pub_date,
            "source": source["name"],
            "short": source["short"],
        })
    return articles


def fetch_full_text(url: str) -> str:
    """Fetch article body for better summarization context."""
    resp = fetch_url(url, timeout=12)
    if not resp:
        return ""
    soup = BeautifulSoup(resp.text, "lxml")
    # Remove nav, header, footer, ads, scripts
    for tag in soup(["script", "style", "nav", "header", "footer", "aside", "iframe", "form"]):
        tag.decompose()
    # Try article body
    body = (
        soup.find("article") or
        soup.find(class_=re.compile("article-body|post-content|entry-content|story-body")) or
        soup.find("main")
    )
    text = clean_text(body.get_text() if body else soup.get_text())
    return text[:3000]


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# CLAUDE SUMMARIZATION
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

def summarize_with_claude(articles: list[dict]) -> list[dict]:
    """Batch summarize articles via Claude API."""
    if not ANTHROPIC_API_KEY:
        print("â  ANTHROPIC_API_KEY not set â using raw summaries.")
        for a in articles:
            a["summary"] = (a["summary_raw"] or a["title"])[:320]
            a["tags"] = a.get("matched_keywords", [])[:3]
        return articles

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    summarized = []

    for idx, article in enumerate(articles):
        print(f"  ð¤ Summarizing {idx+1}/{len(articles)}: {article['title'][:60]}...")
        context = article.get("full_text") or article.get("summary_raw") or article["title"]

        prompt = f"""You are a journalist specializing in Asia technology and industry news.

Article Title: {article['title']}
Source: {article['source']}
URL: {article['url']}
Content:
{context}

Provide ONLY a JSON response with these exact keys:
{{
  "summary": "<Concise factual summary in exactly 60-80 words. Journalist style. No fluff.>",
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
            article["tags"] = data.get("tags", [])[:4]
        except Exception as e:
            print(f"    â  Claude error: {e}")
            article["summary"] = (article.get("summary_raw") or article["title"])[:320]
            article["tags"] = article.get("matched_keywords", [])[:3]

        summarized.append(article)
        # Respect API rate limits
        if idx < len(articles) - 1:
            time.sleep(0.5)

    return summarized


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# DEDUPLICATION
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

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


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# OUTPUT GENERATION
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

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
        url = a["url"]

        row = f"""<tr>
  <td class="col-num">{i}</td>
  <td class="col-source"><span class="source-badge">{a['short']}</span></td>
  <td class="col-title"><span class="article-title">{a['title']}</span></td>
  <td class="col-summary">{a.get('summary','')}</td>
  <td class="col-tags">{tags_html}</td>
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
  <th class="col-tags">Topics</th>
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
        "Topics", "Date", "URL"
    ])
    for i, a in enumerate(articles, 1):
        date_str = a["date"].strftime("%Y-%m-%d") if a.get("date") else ""
        tags = ", ".join(a.get("tags") or [])
        writer.writerow([
            i,
            a.get("source", ""),
            a.get("title", ""),
            a.get("summary", ""),
            tags,
            date_str,
            a.get("url", ""),
        ])
    return output.getvalue()


def update_search_index(articles: list[dict], run_date: datetime) -> None:
    """Append today's articles to the cumulative search index JSON."""
    index_path = ASSETS_DIR / "search-index.json"
    existing = []
    if index_path.exists():
        try:
            existing = json.loads(index_path.read_text(encoding="utf-8"))
        except Exception:
            existing = []

    date_str = run_date.strftime("%Y-%m-%d")
    # Remove any existing entries for today (avoid duplicates on re-run)
    existing = [e for e in existing if e.get("date") != date_str]

    for a in articles:
        existing.append({
            "date": date_str,
            "title": a.get("title", ""),
            "summary": a.get("summary", ""),
            "source": a.get("source", a.get("short", "")),
            "short": a.get("short", ""),
            "tags": a.get("tags") or [],
            "url": a.get("url", ""),
        })

    # Keep newest first
    existing.sort(key=lambda x: x.get("date", ""), reverse=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"ð Search index updated: {len(existing)} total articles")


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
title: "Asia Tech News Digest - {run_date.strftime('%B %d, %Y')}"
date: {run_date.strftime('%Y-%m-%d %H:%M:%S')} +0800
articles_count: {len(articles)}
sources_count: {len(sources_used)}
sources: {json.dumps(sources_used)}
csv_file: /assets/data/{tsv_filename}
---
"""
    filename.write_text(front_matter + "\n" + table_html + "\n", encoding="utf-8")
    print(f"â Jekyll post written: {filename}")
    return filename


def build_email_html(articles: list[dict], run_date: datetime) -> str:
    """Build a compact HTML email summary for approval."""
    rows = ""
    for i, a in enumerate(articles, 1):
        tags = " | ".join(a.get("tags") or [])
        date_str = a["date"].strftime("%d %b") if a.get("date") else ""
        rows += f"""
<tr style="border-bottom:1px solid #eee;">
  <td style="padding:10px 8px;font-weight:700;color:#666;width:28px;">{i}</td>
  <td style="padding:10px 8px;width:70px;"><span style="background:#edf2f7;color:#2b6cb0;padding:2px 7px;border-radius:3px;font-size:11px;font-weight:700;">{a['short']}</span></td>
  <td style="padding:10px 8px;">
    <div style="font-weight:600;color:#1a3a5c;margin-bottom:4px;">{a['title']}</div>
    <div style="font-size:12px;color:#555;margin-bottom:6px;">{a.get('summary','')}</div>
    <div style="margin-top:6px;">
      <span style="font-size:11px;color:#718096;">{tags}</span>
      <span style="font-size:11px;color:#718096;margin-left:10px;">{date_str}</span>
      <a href="{a['url']}" style="font-size:11px;color:#e84545;margin-left:10px;">Read &rarr;</a>
    </div>
  </td>
</tr>"""

    return f"""<!DOCTYPE html>
<html>
<body style="font-family:Segoe UI,sans-serif;max-width:800px;margin:0 auto;padding:20px;color:#2d3748;">
  <div style="background:#1a3a5c;color:#fff;padding:20px 24px;border-radius:8px 8px 0 0;">
    <h2 style="margin:0;font-size:1.2rem;">Asia Tech News Digest - {run_date.strftime('%B %d, %Y')}</h2>
    <p style="margin:6px 0 0;font-size:13px;color:rgba(255,255,255,0.7);">{len(articles)} articles | Filtered for Asia + tech keywords | Awaiting your approval</p>
  </div>
  <div style="background:#fff5e6;border:1px solid #f6ad55;border-radius:0 0 8px 8px;padding:14px 20px;margin-bottom:20px;">
    <strong>ð Action required:</strong> Review the {len(articles)} articles below.
    To <strong>publish</strong>, merge the pull request on GitHub.
    To <strong>skip</strong>, simply close the PR without merging.
  </div>
  <table style="width:100%;border-collapse:collapse;">
    {rows}
  </table>
  <div style="margin-top:20px;padding:14px;background:#f7fafc;border-radius:6px;font-size:12px;color:#718096;text-align:center;">
    Auto-generated by Asia Tech News Feed | GitHub Actions
  </div>
</body>
</html>"""


def write_email_file(html: str, run_date: datetime) -> Path:
    """Write email HTML to file for GitHub Actions to read."""
    email_path = Path(__file__).parent.parent / "_email_preview.html"
    email_path.write_text(html, encoding="utf-8")
    return email_path


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# MAIN
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

def main():
    run_date = datetime.now(SGT)
    print(f"\nð Asia Tech News Feed â {run_date.strftime('%Y-%m-%d %H:%M SGT')}")
    print("=" * 60)

    all_articles = []

    for source in SOURCES:
        print(f"\nð° [{source['short']}] {source['name']}")
        try:
            if source.get("rss") or source["type"] == "rss":
                raw = fetch_rss(source)
            else:
                raw = fetch_scrape(source)
            print(f"  â {len(raw)} items fetched")
        except Exception as e:
            print(f"  â Error: {e}")
            continue

        for article in raw:
            if not is_recent(article.get("date")):
                continue
            combined = f"{article['title']} {article.get('summary_raw','')}"
            matched, kws = is_relevant(combined)
            if not matched:
                continue
            # For global sources, also require an Asia term
            domain = urlparse(article["url"]).netloc.replace("www.", "")
            is_asia_source = any(d in domain for d in ASIA_FOCUSED_DOMAINS)
            if not is_asia_source:
                sea_matched = any(s in combined.lower() for s in SE_ASIA_TERMS)
                if not sea_matched:
                    continue
            article["matched_keywords"] = kws
            all_articles.append(article)

    print(f"\nð {len(all_articles)} relevant articles found before dedup")
    all_articles = deduplicate(all_articles)
    print(f"ð {len(all_articles)} after deduplication")

    # Sort by date descending
    all_articles.sort(key=lambda x: x.get("date") or datetime.min.replace(tzinfo=timezone.utc), reverse=True)

    # Cap at MAX_PER_DOMAIN articles per source domain
    domain_counts: dict[str, int] = {}
    capped = []
    for a in all_articles:
        domain = urlparse(a["url"]).netloc
        if domain_counts.get(domain, 0) < MAX_PER_DOMAIN:
            domain_counts[domain] = domain_counts.get(domain, 0) + 1
            capped.append(a)
    all_articles = capped
    print(f"ð {len(all_articles)} after per-domain cap (max {MAX_PER_DOMAIN} per site)")

    # Take top MAX_ARTICLES
    all_articles = all_articles[:MAX_ARTICLES]
    print(f"ð Top {len(all_articles)} selected")

    if not all_articles:
        print("\nâ  No articles matched. Exiting without creating post.")
        # Write a signal file for GitHub Actions
        Path("/tmp/no_articles.flag").touch()
        sys.exit(0)

    # Fetch full text for better summaries (optional, best-effort)
    print("\nð Fetching article full text...")
    for a in all_articles[:MAX_ARTICLES]:
        a["full_text"] = fetch_full_text(a["url"])
        time.sleep(0.3)

    # Summarize
    print("\nð¤ Summarizing with Claude...")
    all_articles = summarize_with_claude(all_articles)

    # Write outputs
    print("\nð Writing outputs...")
    post_path = write_jekyll_post(all_articles, run_date)
    update_search_index(all_articles, run_date)

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

    print(f"\nâ Done! {len(all_articles)} articles â {post_path.name}")
    print(f"ð§ Email preview: {email_path}")


if __name__ == "__main__":
    main()
