---
title: "Notícias"
permalink: /news/
layout: single
author_profile: false
---
{% assign sorted_news = site.news | sort: "date" | reverse %}
{% for item in sorted_news %}
  <div class="feed-item">
  {% assign monthNames = "janeiro,fevereiro,março,abril,maio,junho,julho,agosto,setembro,outubro,novembro,dezembro" | split: "," %}
{% assign m = item.date | date: "%-m" | minus: 1 %}
<p><strong>{{ item.date | date: "%d" }} de {{ monthNames[m] }} de {{ item.date | date: "%Y" }} – {{ item.date | date: "%H:%M" }}</strong></p>

    <p>{{ item.content | markdownify }}</p>
    <hr>
  </div>
{% endfor %}
