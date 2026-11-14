---
title: "Atendimento e Calendários"
layout: single
permalink: /schedule/
author_profile: true
---

<div class="info-grid">
  <div class="info-card">
    <h2><i class="fas fa-clock" aria-hidden="true"></i> Horário de atendimento</h2>
    <p>Segundas-feiras, das 18:40h às 20:20h</p>
  </div>
  <div class="info-card">
    <h2><i class="fas fa-location-dot" aria-hidden="true"></i> Locais</h2>
    <ol>
      <li>BLOCO E (LAB 1, LAB 2, LAB 3 ou LAB 4, primeiro andar)</li>
      <li>BLOCO L (LAB 5, primeiro andar)</li>
      <li>BLOCO D (em uma sala de aula no primeiro andar)</li>
    </ol>
  </div>
</div>

## Calendários acadêmicos

{% assign calendarios = "2026|integrado|Integrado|2ª Retificação;2026|superior|Superior|5ª Retificação;2027|integrado|Integrado|Resolução 01/2026;2027|superior|Superior|Resolução 01/2026" | split: ";" %}
{% assign ano_atual = "" %}
<div class="cal-list">
{% for c in calendarios %}{% assign f = c | split: "|" %}{% assign pdf = "/assets/pdfs/" | append: f[1] | append: "-" | append: f[0] | append: ".pdf" %}
  {% if f[0] != ano_atual %}<h3 class="cal-year">{{ f[0] }}</h3>{% assign ano_atual = f[0] %}{% endif %}
  <details class="cal-item">
    <summary>
      <i class="fas fa-calendar-days" aria-hidden="true"></i>
      <span class="cal-title">Calendário {{ f[2] }} {{ f[0] }}</span>
      <span class="cal-note">{{ f[3] }}</span>
      <i class="fas fa-chevron-down cal-chevron" aria-hidden="true"></i>
    </summary>
    <div class="cal-body">
      <a class="download-btn" href="{{ pdf }}"><i class="fas fa-file-pdf" aria-hidden="true"></i> Baixar PDF</a>
      <object class="pdf-embed" data-src="{{ pdf }}#page=1&view=Fit&zoom=page-fit" type="application/pdf" width="100%" height="600"></object>
    </div>
  </details>
{% endfor %}
</div>

<script>
  // Load each PDF only when its calendar is opened
  document.querySelectorAll('.cal-item').forEach(function (d) {
    d.addEventListener('toggle', function () {
      var o = d.querySelector('object[data-src]');
      if (d.open && o) {
        var n = o.cloneNode(false);
        n.removeAttribute('data-src');
        n.setAttribute('data', o.dataset.src);
        o.replaceWith(n);
      }
    });
  });
</script>
