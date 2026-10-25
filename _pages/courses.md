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
  <a class="course-card{% if c.nivel %} course-card--{{ c.nivel | downcase }}{% endif %}" href="{{ c.url }}">
    <strong>{{ c.title }}</strong>
    <span class="course-tags">{% if c.nivel %}<span class="course-level">{% if c.nivel == "Integrado" %}<i class="fas fa-school" aria-hidden="true"></i>{% else %}<i class="fas fa-building-columns" aria-hidden="true"></i>{% endif %} {{ c.nivel }}</span>{% endif %}{% if c.code %}<span class="course-code">{{ c.code }}</span>{% endif %}</span>
  </a>
  {% endfor %}
</div>
{% endfor %}
