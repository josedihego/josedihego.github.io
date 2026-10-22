---
title: "Programação aplicada com C e Arduino – Plano de Aulas"
layout: single
permalink: /progarduino/
author_profile: true
classes: course-page
---
[← Cursos](/courses/){: .back-link}

Plano de Aula da disciplina Programação aplicada com C e Arduino (Automação e Eletrônica).

## Kit portátil: VS Code + C + Arduino

<div class="kit-card">
  <p><strong>Instalado nos computadores do laboratório (Linux), sem precisar de administrador.</strong> O kit traz o VS Code em português, o seu próprio compilador C (gcc) e o arduino-cli com a placa Arduino Uno, além de todos os exemplos das aulas. O professor instala a partir de um pendrive com <code>bash instalar.sh</code>.</p>
  <ol>
    <li>Abra <strong>Kit C e Arduino</strong> no menu de aplicativos. O VS Code abre a pasta <code>C-e-Arduino</code>, com <code>exemplos</code> (todas as aulas) e <code>trabalhos</code>.</li>
    <li>Em <code>trabalhos</code>, crie uma pasta com <strong>o seu nome</strong> e salve nela os seus programas. A conta do laboratório é compartilhada: no fim da aula, copie a sua pasta para o seu pendrive.</li>
    <li>Arquivos <code>.c</code> (C no computador): clique em ▶ ou F5 para compilar e rodar. Arquivos <code>.ino</code> (Arduino): ▶ compila e, com a placa conectada pelo USB, envia e abre o Monitor Serial. Comece seus sketches com <code>#include &lt;Arduino.h&gt;</code> para o editor reconhecer as funções do Arduino.</li>
  </ol>
  <p class="files-hint">Enviar para a placa exige que o usuário do laboratório esteja no grupo <code>dialout</code> (vale também para a Arduino IDE): a tarefa <em>Arduino: verificar placa e permissão</em> mostra se está liberado. Enquanto não estiver, teste os sketches no Wokwi.</p>
</div>

## Ferramentas

<ul class="tool-legend">
  <li><span class="tool tool--c">C</span> programas no computador, compilados com o gcc do kit</li>
  <li><span class="tool tool--arduino">Arduino</span> sketches para o Arduino Uno, enviados pelo kit (arduino-cli)</li>
  <li><span class="tool">Wokwi</span> simulador on-line do Arduino, para quem estiver sem placa (<a href="https://wokwi.com/projects/new/arduino-uno">wokwi.com</a>)</li>
  <li><span class="tool">Monitor Serial</span> conversa com a placa; o Plotter Serial mostra gráficos das leituras</li>
</ul>

<p class="files-hint"><strong>Exemplos das aulas</strong> (três níveis cada: 1 Básico, 2 Intermediário, 3 Avançado): já estão na pasta <code>exemplos</code> do kit, ou em <a href="/assets/progarduino/exemplos-progarduino.zip">exemplos-progarduino.zip</a>. <strong>No Wokwi</strong>: abra um projeto Arduino Uno novo, cole o sketch no <code>sketch.ino</code> e o conteúdo do <code>diagram.json</code> na aba <code>diagram.json</code>: o circuito aparece montado.</p>

{% assign niveis = "basico:Básico,intermediario:Intermediário,avancado:Avançado" | split: "," %}
{% assign repo = "https://github.com/josedihego/josedihego.github.io/blob/master/assets/progarduino/" %}
{% for u in site.data.progarduino %}
<h2 class="unit-title" id="unidade-{{ u.unidade }}"><span class="unit-num">Unidade {{ u.unidade }}</span> {{ u.titulo }}</h2>
<p class="unit-summary">{{ u.resumo | markdownify | remove: '<p>' | remove: '</p>' }}</p>
<div class="lesson-list">
  {% for a in u.aulas %}
  {% assign nn = a.n | prepend: "0" | slice: -2, 2 %}{% capture aula %}aula{{ nn }}{% endcapture %}{% assign ex = site.data.progarduino_exemplos[aula] %}
  <details class="lesson" id="aula-{{ a.n }}">
    <summary>
      <span class="lesson-num">{{ a.n }}</span>
      <span class="lesson-head">
        <strong>{{ a.tema | markdownify | remove: '<p>' | remove: '</p>' | strip }}</strong>
        <span class="lesson-tools"><span class="tool tool--c">C</span><span class="tool tool--arduino">Arduino</span></span>
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
      <h4>Código em C</h4>
      <ol class="level-list">
        {% for t in ex.c %}{% capture arq %}{{ aula }}_nivel{{ forloop.index }}{% endcapture %}<li><span class="level-tag">Nível {{ forloop.index }}</span> {{ t }} <a class="file-link" href="{{ repo }}c/{{ arq }}.c" target="_blank" rel="noopener">ver código</a> <a class="file-link file-link--alt" href="/assets/progarduino/c/{{ arq }}.c" download>baixar .c</a></li>
        {% endfor %}
      </ol>
      <h4>Arduino <a class="file-link file-link--alt" href="https://wokwi.com/projects/new/arduino-uno" target="_blank" rel="noopener">abrir o Wokwi</a></h4>
      <ol class="level-list">
        {% for t in ex.arduino %}{% capture arq %}{{ aula }}_nivel{{ forloop.index }}{% endcapture %}{% assign i = forloop.index0 %}<li><span class="level-tag">Nível {{ forloop.index }}</span> {{ t }} <span class="parts">({{ ex.pecas[i] }})</span> <a class="file-link" href="{{ repo }}arduino/{{ arq }}/{{ arq }}.ino" target="_blank" rel="noopener">ver sketch</a> <a class="file-link file-link--alt" href="{{ repo }}arduino/{{ arq }}/diagram.json" target="_blank" rel="noopener">circuito (diagram.json)</a></li>
        {% endfor %}
      </ol>
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
