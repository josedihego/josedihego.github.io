---
title: "Cursos"
layout: single
permalink: /courses/
author_profile: true
---

{% for g in site.data.courses %}
<h2 class="group-title"><i class="fas {{ g.icon }}" aria-hidden="true"></i> {{ g.group }}</h2>
<div class="course-grid">
  {% for c in g.courses %}
  <a class="course-card" href="{{ c.url }}">
    <strong>{{ c.title }}</strong>
    {% if c.code %}<span class="course-code">{{ c.code }}</span>{% endif %}
  </a>
  {% endfor %}
</div>
{% endfor %}
