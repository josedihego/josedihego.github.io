---
title: "Informática Básica – Plano de Aulas"
layout: single
permalink: /infobasica/
author_profile: true
classes: course-page
---
[← Cursos](/courses/){: .back-link}

Plano de aulas das turmas de **Edificações**, **Química** e **Mecânica**: 36 encontros de 2 horas, em três unidades de 12 aulas. Cada problema é resolvido em **Python** e refeito no **Scratch**, como fórmula no **Google Planilhas**, e registrado no **Google Docs**.

## Ferramentas

<ul class="tool-legend">
  <li><span class="tool tool--python">Python</span> linguagem principal, executada no <a href="https://colab.research.google.com/">Google Colab</a></li>
  <li><span class="tool tool--scratch">Scratch</span> a mesma lógica em blocos (<a href="https://scratch.mit.edu/">scratch.mit.edu</a>)</li>
  <li><span class="tool tool--planilhas">Planilhas</span> a mesma lógica como fórmula do Google Planilhas (nomes em PT-BR: <code>SE</code>, <code>RAIZ</code>, <code>SOMA</code>…)</li>
  <li><span class="tool tool--docs">Docs</span> Diário de Bordo e documentação dos projetos</li>
  <li><span class="tool">Python Tutor</span> visualiza a execução linha a linha (<a href="https://pythontutor.com/">pythontutor.com</a>)</li>
  <li><span class="tool">Fluxogramas</span> <a href="http://www.flowgorithm.org/">Flowgorithm</a> ou <a href="https://app.diagrams.net/">diagrams.net</a></li>
  <li><span class="tool">Blockly Games</span> desafios de lógica em blocos (<a href="https://blockly.games/?lang=pt-br">blockly.games</a>)</li>
</ul>

{% for u in site.data.infobasica %}
<h2 class="unit-title" id="unidade-{{ u.unidade }}"><span class="unit-num">Unidade {{ u.unidade }}</span> {{ u.titulo }}</h2>
<p class="unit-summary">{{ u.resumo | markdownify | remove: '<p>' | remove: '</p>' }}</p>
<div class="lesson-list">
  {% for a in u.aulas %}
  <details class="lesson" id="aula-{{ a.n }}">
    <summary>
      <span class="lesson-num">{{ a.n }}</span>
      <span class="lesson-head">
        <strong>{{ a.tema | markdownify | remove: '<p>' | remove: '</p>' | strip }}</strong>
        <span class="lesson-tools">{% for t in a.ferramentas %}<span class="tool tool--{{ t | slugify }}">{{ t }}</span>{% endfor %}</span>
      </span>
    </summary>
    <div class="lesson-body">
      <h4>Objetivo</h4>
      <p>{{ a.objetivo | markdownify | remove: '<p>' | remove: '</p>' | strip }}</p>
      <h4>Material</h4>
      <ul>
        {% for m in a.material %}<li>{{ m | markdownify | remove: '<p>' | remove: '</p>' | strip }}</li>
        {% endfor %}
      </ul>
      <h4>Exercícios propostos</h4>
      <ol>
        {% for e in a.exercicios %}<li>{{ e | markdownify | remove: '<p>' | remove: '</p>' | strip }}</li>
        {% endfor %}
      </ol>
    </div>
  </details>
  {% endfor %}
</div>
{% endfor %}
