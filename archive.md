---
layout: default
title: Archive
---

<h2 style="margin-bottom:20px; color:#1a3a5c;">📁 All News Digests</h2>

{% assign explainer_items = site.explainers | sort: "date" | reverse %}
{% if explainer_items.size > 0 %}
<details class="archive-folder">
  <summary class="archive-folder-title">
    <span class="folder-icon">📖</span>
    <span class="folder-name">Explainers</span>
    <span class="folder-count">{{ explainer_items.size }} explainer{% if explainer_items.size != 1 %}s{% endif %}</span>
  </summary>
  <div class="archive-folder-body">
    {% for item in explainer_items %}
    <div class="archive-row">
      <a href="{{ item.url | relative_url }}" class="archive-link">{{ item.title }}</a>
      <span class="archive-meta">
        {{ item.date | date: "%d %b %Y" }}
        {% if item.tags and item.tags.size > 0 %}&middot; {{ item.tags | join: ", " }}{% endif %}
      </span>
    </div>
    {% endfor %}
  </div>
</details>
{% endif %}

{% assign postsByYear = site.posts | group_by_exp: "post", "post.archive_date | default: post.date | date: '%Y'" %}
{% for year in postsByYear %}

{% assign postsByMonth = year.items | group_by_exp: "post", "post.archive_date | default: post.date | date: '%B %Y'" %}
{% for month in postsByMonth %}
<details class="archive-folder" {% if forloop.first and forloop.parentloop.first %}open{% endif %}>
  <summary class="archive-folder-title">
    <span class="folder-icon">📂</span>
    <span class="folder-name">{{ month.name }}</span>
    <span class="folder-count">{{ month.items | size }} digest{% if month.items.size != 1 %}s{% endif %}</span>
  </summary>
  <div class="archive-folder-body">
    {% for post in month.items %}
    <div class="archive-row">
      <a href="{{ post.url | relative_url }}" class="archive-link">{{ post.title }}</a>
      <span class="archive-meta">
        {{ post.date | date: "%d %b" }}
        {% if post.layout == "editorial" %}&middot; Editor's Review{% else %}&middot; {{ post.articles_count | default: 0 }} articles{% endif %}
      </span>
    </div>
    {% endfor %}
  </div>
</details>
{% endfor %}

{% endfor %}

<style>
.archive-folder {
  background: var(--card-bg, #fff);
  border: 1px solid var(--border, #dde3ec);
  border-radius: 10px;
  margin-bottom: 12px;
  overflow: hidden;
}
.archive-folder-title {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  cursor: pointer;
  list-style: none;
  user-select: none;
  font-weight: 600;
  color: var(--text, #1a3a5c);
  font-size: 0.95rem;
}
.archive-folder-title::-webkit-details-marker { display: none; }
.archive-folder-title::before {
  content: '▶';
  font-size: 0.65rem;
  color: #718096;
  transition: transform 0.2s;
  flex-shrink: 0;
}
details[open] > .archive-folder-title::before { transform: rotate(90deg); }
.folder-icon { font-size: 1.1rem; }
.folder-name { flex: 1; }
.folder-count {
  font-size: 0.78rem;
  color: #718096;
  font-weight: 400;
  background: var(--bg, #f7f9fc);
  border: 1px solid var(--border, #dde3ec);
  border-radius: 12px;
  padding: 2px 10px;
}
.archive-folder-body {
  border-top: 1px solid var(--border, #dde3ec);
  padding: 4px 0;
}
.archive-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 18px 10px 42px;
  border-bottom: 1px solid var(--border, #f0f4f8);
}
.archive-row:last-child { border-bottom: none; }
.archive-link {
  color: var(--text, #1a3a5c);
  text-decoration: none;
  font-size: 0.9rem;
}
.archive-link:hover { color: #2b6cb0; text-decoration: underline; }
.archive-meta {
  font-size: 0.78rem;
  color: #718096;
  white-space: nowrap;
  margin-left: 12px;
}
html.dark .archive-folder { background: var(--card-bg); border-color: #334; }
html.dark .archive-folder-title { color: var(--text); }
html.dark .folder-count { background: #1a2035; border-color: #334; }
html.dark .archive-folder-body { border-top-color: #334; }
html.dark .archive-row { border-bottom-color: #2a3045; }
html.dark .archive-link { color: var(--text); }
</style>
