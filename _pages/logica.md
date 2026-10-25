---
title: "Lógica de Programação – Superior"
layout: single
permalink: /logica/
author_profile: true
classes: course-page
---
[← Cursos](/courses/){: .back-link}

Plano de aulas da disciplina de Lógica de Programação (INF027), em linguagem C. São 36 encontros em três blocos; cada bloco termina com uma avaliação no formato das provas anteriores, e o último encontro é a reavaliação.

<div class="kit-card">
<strong>Como é cada aula</strong>
<ol>
  <li><strong>Slides</strong>: o conceito do dia, o padrão em C, os erros que mais custam pontos e um teste de mesa.</li>
  <li><strong>Resolvida em sala</strong>: uma questão de prova anterior, resolvida passo a passo, com o código comentado.</li>
  <li><strong>Para você</strong>: outra questão de prova anterior, para resolver. A solução comentada fica disponível para conferir depois.</li>
</ol>
Toda questão indica a prova de origem e o número da questão, com link para o PDF original no repositório <a href="https://github.com/josedihego/programacaoC/tree/main/INF027_listas_provas_PDF">programacaoC</a>. Para compilar: <code>gcc -Wall arquivo.c -o programa -lm</code>, ou no navegador em <a href="https://www.onlinegdb.com/online_c_compiler">OnlineGDB</a>.
</div>

{% for b in site.data.logica %}
<h2 class="unit-title" id="bloco-{{ b.bloco }}"><span class="unit-num">Bloco {{ b.bloco }}</span> {{ b.titulo }}</h2>
<p class="unit-summary">{{ b.resumo | markdownify | remove: '<p>' | remove: '</p>' | strip }}</p>
<div class="lesson-list">
  {% for a in b.aulas %}
  <details class="lesson{% if a.tipo != 'aula' %} lesson--prova{% endif %}" id="aula-{{ a.n }}">
    <summary>
      <span class="lesson-num">{{ a.n }}</span>
      <span class="lesson-head">
        <strong>{{ a.tema | markdownify | remove: '<p>' | remove: '</p>' | strip }}</strong>
        <span class="lesson-tools">{% if a.tipo == 'aula' %}<span class="tool">{{ a.resolvida.rotulo | split: "," | first }}</span>{% else %}<span class="tool tool--prova">{% if a.tipo == 'reavaliacao' %}Reavaliação{% else %}Avaliação{% endif %}</span>{% endif %}</span>
      </span>
    </summary>
    <div class="lesson-body">
      <p>{{ a.objetivo | markdownify | remove: '<p>' | remove: '</p>' | strip }}</p>
      {% if a.tipo == 'aula' %}
      <div class="lesson-files"><a class="file-btn" href="/assets/logica/slides/{{ a.slides }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf" aria-hidden="true"></i> Slides da aula {{ a.n }}</a></div>
      <h4>Conceitos</h4>
      <ul>
        {% for c in a.conceitos %}<li>{{ c | markdownify | remove: '<p>' | remove: '</p>' | strip }}</li>
        {% endfor %}
      </ul>
      {% assign blocos_q = "resolvida,proposta" | split: "," %}
      {% for chave in blocos_q %}{% assign q = a[chave] %}
      <div class="q-card{% if chave == 'proposta' %} q-card--proposta{% endif %}">
        <h4>{% if chave == 'resolvida' %}Resolvida em sala{% else %}Para você{% endif %}: {{ q.titulo }}</h4>
        <p class="q-source"><a href="{{ q.url }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf" aria-hidden="true"></i> {{ q.rotulo }}</a> <span class="q-file">{{ q.pdf }}</span></p>
        {% if q.codigo %}<details class="q-more"><summary>Solução comentada{% if chave == 'proposta' %} (tente antes!){% endif %}</summary><pre class="codigo"><code>{{ q.codigo | escape }}</code></pre><a class="file-link" href="/assets/logica/solucoes/{{ q.solucao }}" download>{{ q.solucao }}</a></details>{% endif %}
      </div>
      {% endfor %}
      {% else %}
      <h4>Prova-modelo</h4>
      {% for q in a.questoes %}
      <div class="q-card">
        <h4>Questão {{ forloop.index }}: {{ q.titulo }}</h4>
        <p class="q-source"><a href="{{ q.url }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf" aria-hidden="true"></i> {{ q.rotulo }}</a> <span class="q-file">{{ q.pdf }}</span></p>
        {% if q.codigo %}<details class="q-more"><summary>Solução comentada</summary><pre class="codigo"><code>{{ q.codigo | escape }}</code></pre><a class="file-link" href="/assets/logica/solucoes/{{ q.solucao }}" download>{{ q.solucao }}</a></details>{% endif %}
      </div>
      {% endfor %}
      {% endif %}
    </div>
  </details>
  {% endfor %}
  {% if b.banco.size > 0 %}
  <details class="lesson lesson--banco" id="banco-{{ b.bloco }}">
    <summary>
      <span class="lesson-num"><i class="fas fa-layer-group" aria-hidden="true"></i></span>
      <span class="lesson-head"><strong>Banco de questões do Bloco {{ b.bloco }}</strong><span class="lesson-tools"><span class="tool">{{ b.banco.size }} questões</span></span></span>
    </summary>
    <div class="lesson-body">
      <p>Outras questões de provas anteriores com o conteúdo do bloco, para treinar.</p>
      <ul class="q-bank">
        {% for q in b.banco %}<li><a href="{{ q.url }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf" aria-hidden="true"></i> {{ q.rotulo }}</a> <span class="q-file">{{ q.pdf }}</span></li>
        {% endfor %}
      </ul>
    </div>
  </details>
  {% endif %}
</div>
{% endfor %}
