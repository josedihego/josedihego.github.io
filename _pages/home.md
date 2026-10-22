---
title: "Prof. José Dihego"
layout: single
permalink: /
author_profile: true
classes: home-page
---

<p class="home-intro">Full Professor at the Federal Institute of Bahia (<a href="https://portal.ifba.edu.br/">IFBA</a>), Campus Salvador, since 2010. PhD in Computer Science from <a href="https://www.cin.ufpe.br">CIn-UFPE</a>.</p>

<ul class="chips" aria-label="Interests">
  <li>Formal Methods</li>
  <li>Programming Languages</li>
  <li>Mobile Development</li>
</ul>

## Apps on Google Play

<div class="app-list">
{% for app in site.data.apps %}
  <a class="app-card" href="{{ app.url }}" target="_blank" rel="noopener noreferrer">
    <img src="{{ app.icon | relative_url }}" alt="" width="64" height="64">
    <div>
      <strong>{{ app.name }}</strong>
      <span>{{ app.description }}</span>
      <span class="app-store"><i class="fab fa-google-play" aria-hidden="true"></i> Google Play</span>
    </div>
  </a>
{% endfor %}
</div>

## Selected publications

<ul class="pub-list">
{% assign pubs = site.data.publications | sort: "year" | reverse %}
{% for p in pubs %}
  <li>
    <span class="pub-year">{{ p.year }}</span>
    <div>
      <a class="pub-title" href="https://doi.org/{{ p.doi }}">{{ p.title }}</a>
      <span class="pub-authors">{{ p.authors }}</span>
    </div>
  </li>
{% endfor %}
</ul>

## Education

<ul class="edu-list">
  <li><strong>PhD in Computer Science</strong>, UFPE, 2016
    <a class="tag" href="https://drive.google.com/file/d/1o2ebNJ8OmKo23rNcTv-97Jzzs-rEPqhE/view?usp=drive_link">PDF</a>
    <a class="tag" href="https://www.repositorio.ufpe.br/handle/123456789/19522">Repository</a></li>
  <li><strong>MSc in Computer Science</strong>, UFPE, 2010
    <a class="tag" href="https://drive.google.com/file/d/1EOZVxCfB_jia1Dx-MPKoAqs8_z4HtRxN/view?usp=drive_link">PDF</a>
    <a class="tag" href="https://www.repositorio.ufpe.br/handle/123456789/2660">Repository</a></li>
  <li><strong>BSc in Computer Science</strong>, UFPE, 2008
    <a class="tag" href="https://drive.google.com/file/d/1MFuxt_-J5zLWGaxqcb2p9GfOUZSzICLa/view?usp=drive_link">PDF</a>
    <a class="tag" href="https://www.cin.ufpe.br/~tg/2008-2/">Repository</a></li>
</ul>

<!-- Store links disabled: apps no longer listed on Google Play / App Store (Oct 2026)
#### Mobile Apps

<a href="https://play.google.com/store/apps/developer?id=José+Dihego+da+Silva+Oliveira" target="_blank" rel="noopener noreferrer">
  <i class="fab fa-google-play" style="font-size:24px;"></i>
 Android apps on Google Play
</a>

<a href="https://apps.apple.com/us/developer/jose-dihego-da-silva-oliveira/id1234567890" target="_blank" rel="noopener noreferrer">
  <i class="fab fa-app-store-ios" style="font-size:24px;"></i>
  iOS apps on Apple Store
</a>
-->

## Professional address

Federal Institute of Education, Science and Technology of Bahia (IFBA)<br>
R. Emídio dos Santos, s/n – Barbalho, Salvador – BA, 40301-015<br>
<a class="tag" href="https://www.google.com/maps/search/?api=1&query=IFBA+Campus+Salvador"><i class="fas fa-location-dot" aria-hidden="true"></i> Open in Google Maps</a>
