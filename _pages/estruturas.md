---
title: "Estruturas de dados e seus algoritmos – Superior"
layout: single
permalink: /estruturas/
author_profile: true
classes: course-page
mathjax: true
---
[← Cursos](/courses/){: .back-link}

Plano de aulas da disciplina de Estruturas de Dados e Algoritmos (ADS, INF006). São 36 encontros em quatro blocos: 32 aulas e 4 apresentações de projeto (aulas 9, 18, 27 e 36). Fora dos 36 encontros há um anexo, <strong>Base Prática em C</strong> (módulos B1 a B5, para estudar antes do bloco 1), e um bloco complementar opcional que aprofunda a ordenação (C1 a C5).

<div class="kit-card">
<strong>Como é cada aula</strong>: um conjunto de slides em quatro partes.
<ol>
  <li><strong>Teoria</strong>, a partir de Cormen et al., <em>Algoritmos: teoria e prática</em> (3ª edição), com as figuras do livro e o pseudocódigo em português.</li>
  <li><strong>Prática em C</strong>: implementação comentada, testada, para baixar e rodar.</li>
  <li><strong>Experimento</strong>: uma hipótese tirada da teoria, um programa em C que mede, e o gráfico do medido contra a curva teórica. Rode na sua máquina: <code>gcc -O2 arquivo.c -o exp -lm &amp;&amp; ./exp</code>.</li>
  <li><strong>Conexões</strong>: onde o conceito aparece em outras áreas da computação.</li>
</ol>
As figuras dos slides são reproduzidas de Cormen, Leiserson, Rivest e Stein (MIT Press, 2009) para fins didáticos, com a indicação da figura original.
</div>

{% for b in site.data.estruturas %}
<h2 class="unit-title{% if b.tag != "" %} unit-title--opcional{% endif %}" id="bloco-{{ b.bloco }}"><span class="unit-num">{{ b.rotulo }}</span> {{ b.titulo }}</h2>
<p class="unit-summary">{{ b.resumo }}</p>
<div class="lesson-list">
  {% for a in b.aulas %}
  <details class="lesson{% if a.tipo != 'aula' %} lesson--prova{% endif %}" id="aula-{{ a.n }}">
    <summary>
      <span class="lesson-num">{{ a.n }}</span>
      <span class="lesson-head">
        <strong>{{ a.tema | escape }}</strong>
        <span class="lesson-tools">{% if a.tipo == 'aula' %}{% if b.tag != "" %}<span class="tool tool--opcional">{{ b.tag }}</span>{% endif %}<span class="tool">{{ a.cormen }}</span>{% else %}<span class="tool tool--prova">Projeto</span>{% endif %}</span>
      </span>
    </summary>
    <div class="lesson-body">
      {% if a.tipo == 'aula' %}
      <div class="lesson-files">
        <a class="file-btn" href="/assets/estruturas/slides/{{ a.slides }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf" aria-hidden="true"></i> Slides{% if b.tag != "" %} do módulo{% else %} da aula{% endif %} {{ a.n }}</a>
        {% for c in a.codigo %}<a class="file-btn" href="/assets/estruturas/codigo/{{ c.arquivo }}" download><i class="fas fa-code" aria-hidden="true"></i> {{ c.arquivo }}</a>{% endfor %}
        <a class="file-btn" href="/assets/estruturas/codigo/{{ a.experimento.arquivo }}" download><i class="fas fa-flask" aria-hidden="true"></i> {{ a.experimento.arquivo }}</a>
      </div>
      <h4>Objetivos</h4>
      <ul>
        {% for o in a.objetivos %}<li>{{ o | escape }}</li>
        {% endfor %}
      </ul>
      <div class="q-card">
        <h4>Experimento</h4>
        <p><strong>{{ a.experimento.pergunta | escape }}</strong></p>
        <p>{{ a.experimento.conclusao | escape }}</p>
      </div>
      <h4>Conexões</h4>
      <ul class="conexoes">
        {% for c in a.conexoes %}<li><strong>{{ c.area | escape }}:</strong> {{ c.texto | escape }}</li>
        {% endfor %}
      </ul>
      {% else %}
      <p>{{ a.descricao | escape }}</p>
      <h4>Entregas</h4>
      <ul>
        {% for e in a.entregas %}<li>{{ e | escape }}</li>
        {% endfor %}
      </ul>
      {% endif %}
    </div>
  </details>
  {% endfor %}
</div>
{% endfor %}
