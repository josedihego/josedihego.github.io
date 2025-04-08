---
title: "Course News"
permalink: /news/
layout: single
author_profile: false
---

<h2>📰 Notícias 🗒️</h2>

{% assign sorted_news = site.news | sort: "date" | reverse %}
{% for item in sorted_news %}
  <div class="feed-item">
    <p><strong>{{ item.date | date: "%b %d, %Y – %H:%M" }}</strong></p>
    <p>{{ item.content | markdownify }}</p>
    <hr>
  </div>
{% endfor %}
