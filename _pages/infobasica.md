---
title: "Informática – Plano de Aulas - Integrado"
layout: single
permalink: /infobasica/
author_profile: true
classes: course-page
---
[← Cursos](/courses/){: .back-link}

Plano de Aula da disciplina de Informática.

## Ferramentas

Todas funcionam no navegador, sem instalar nada: basta uma conta Google e uma conta no Scratch.

<ul class="tool-legend">
  <li><span class="tool tool--planilhas">Planilhas</span> a mesma lógica como fórmula do Google Planilhas (nomes em PT-BR: <code>SE</code>, <code>RAIZ</code>, <code>SOMA</code>…)</li>
  <li><span class="tool tool--documentos">Documentos</span> Google Documentos: Diário de Bordo e registro das atividades</li>
  <li><span class="tool tool--python">Python</span> linguagem principal, executada no <a href="https://colab.research.google.com/">Google Colab</a></li>
  <li><span class="tool tool--scratch">Scratch</span> a mesma lógica em blocos, no editor on-line (<a href="https://scratch.mit.edu/projects/editor/">scratch.mit.edu</a>)</li>
  <li><span class="tool">Python Tutor</span> visualiza a execução linha a linha (<a href="https://pythontutor.com/">pythontutor.com</a>)</li>
  <li><span class="tool">Fluxogramas</span> <a href="https://app.diagrams.net/">diagrams.net</a> ou <em>Inserir → Desenho</em> no Google Documentos</li>
  <li><span class="tool">Blockly Games</span> desafios de lógica em blocos (<a href="https://blockly.games/?lang=pt-br">blockly.games</a>)</li>
</ul>

<p class="files-hint"><strong>Arquivos das aulas</strong> (três níveis cada: 1 Básico, 2 Intermediário, 3 Avançado). <strong>Python</strong>: abre direto no Colab. <strong>Scratch</strong>: baixe o <code>.sb3</code> e abra no editor on-line em <em>Arquivo → Carregar do seu computador</em>. <strong>Planilhas</strong>: "Abrir cópia no Google Planilhas" cria uma cópia sua, pronta para editar (é preciso entrar com uma conta Google); o <code>.xlsx</code> fica como alternativa para baixar.</p>

{% assign niveis = "basico:Básico,intermediario:Intermediário,avancado:Avançado" | split: "," %}
{% assign colab = "https://colab.research.google.com/github/josedihego/josedihego.github.io/blob/master/assets/infobasica/python/" %}
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
      {% assign nn = a.n | prepend: "0" | slice: -2, 2 %}
      {% if a.planilhas %}
      <h4>Planilhas</h4>
      <ol class="level-list">
        {% for ex in a.planilhas %}{% capture chave %}aula{{ nn }}_nivel{{ forloop.index }}{% endcapture %}<li><span class="level-tag">Nível {{ forloop.index }}</span> {{ ex | markdownify | remove: '<p>' | remove: '</p>' | strip }} <a class="file-link" href="https://docs.google.com/spreadsheets/d/{{ site.data.infobasica_planilhas[chave] }}/copy" target="_blank" rel="noopener"><i class="fas fa-table" aria-hidden="true"></i> Abrir cópia no Google Planilhas</a> <a class="file-link file-link--alt" href="/assets/infobasica/planilhas/{{ chave }}.xlsx" download>.xlsx</a></li>
        {% endfor %}
      </ol>
      {% endif %}
      {% if a.python %}
      <div class="lesson-files"><span class="files-label"><i class="fab fa-python" aria-hidden="true"></i> Python (Colab)</span>{% for f in a.python %}<a class="file-btn" href="{{ colab }}{{ f }}" target="_blank" rel="noopener">Nível {{ forloop.index }}</a>{% endfor %}</div>
      {% endif %}
      {% if a.scratch %}
      <div class="lesson-files"><span class="files-label"><i class="fas fa-puzzle-piece" aria-hidden="true"></i> Scratch (.sb3)</span>{% for f in a.scratch %}<a class="file-btn" href="/assets/infobasica/scratch/{{ f }}" download>Nível {{ forloop.index }}</a>{% endfor %}</div>
      {% endif %}
      <div class="lesson-activity">
        <h4>Atividade em sala · {{ a.atividade.tempo }}</h4>
        <p>{{ a.atividade.descricao | markdownify | remove: '<p>' | remove: '</p>' | strip }}</p>
      </div>
      <h4>Exercícios propostos</h4>
      {% for nivel in niveis %}{% assign partes = nivel | split: ":" %}{% assign chave = partes[0] %}
      <p class="level-head"><span class="level-tag">Nível {{ forloop.index }}</span> {{ partes[1] }}</p>
      <ol>
        {% for e in a.exercicios[chave] %}<li>{{ e | markdownify | remove: '<p>' | remove: '</p>' | strip }}</li>
        {% endfor %}
      </ol>
      {% endfor %}
    </div>
  </details>
  {% endfor %}
</div>
{% endfor %}
