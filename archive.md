---
layout: default
title: Archive
---

<h2 style="margin-bottom:20px; color:#1a3a5c;">&#128193; All News Digests</h2>

{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
<div style="margin-bottom:24px;">
  <h3 style="color:#718096; font-size:0.9rem; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin-bottom:10px; border-bottom:1px solid #dde3ec; padding-bottom:6px;">
    {{ year.name }}
  </h3>
  {% assign postsByMonth = year.items | group_by_exp: "post", "post.date | date: '%B'" %}
  {% for month in postsByMonth %}
  <div style="margin-bottom:16px; padding-left:16px;">
    <div style="font-size:0.82rem; color:#2b6cb0; font-weight:600; margin-bottom:8px;">{{ month.name }}</div>
    {% for post in month.items %}
    <div style="padding:8px 0; border-bottom:1px solid #f0f0f0; display:flex; justify-content:space-between; align-items:center;">
      <a href="{{ post.url | relative_url }}" style="color:#1a3a5c; text-decoration:none; font-size:0.9rem;">
        {{ post.title }}
      </a>
      <span style="font-size:0.78rem; color:#718096; margin-left:12px; white-space:nowrap;">
        {{ post.date | date: "%d %b" }} &middot; {{ post.articles_count | default: 0 }} articles
      </span>
    </div>
    {% endfor %}
  </div>
  {% endfor %}
</div>
{% endfor %}
