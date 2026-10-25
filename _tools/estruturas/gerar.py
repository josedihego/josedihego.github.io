"""Builds the /estruturas/ course (Estruturas de dados e seus algoritmos – Superior) from plano.py and c/:
  assets/estruturas/slides/aulaNN.pdf   one deck per content class: Teoria (Cormen), Prática (C), Experimento, Conexões
  assets/estruturas/codigo/*.c          implementations and experiments (without the '// teste:' lines)
  _data/estruturas.yml                  blocks and classes, for _pages/estruturas.md
Figures are cropped from the local PDF of Cormen et al. (3rd ed.) into a cache outside the repository (cormen_fig.py).
Experiments: each c/aulaNN_experimento.c prints a CSV; the generator fits the theoretical curve, checks how far the
measurements stray from it and plots both.
Uso: python3 _tools/estruturas/gerar.py <raiz do site> <pdf do Cormen> [--aulas 2,3] [--sem-slides]"""
import sys, os, re, json, math, glob, shutil, subprocess, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from plano import BLOCOS, AULAS
import cormen_fig

SITE = 'https://josedihego.net'
CACHE = os.path.join(os.path.expanduser('~'), '.cache', 'estruturas-cormen')   # figuras recortadas (não versionadas)
LINHAS_POR_SLIDE = 16
COLUNAS = 88
SEGMENTOS = {                                                  # nome, cor, ícone (fontawesome5)
    'teoria': ('Teoria', 'cteoria', '\\faBook'),
    'pratica': ('Prática em C', 'cpratica', '\\faCode'),
    'experimento': ('Experimento', 'cexperimento', '\\faFlask'),
    'conexoes': ('Conexões', 'cconexoes', '\\faProjectDiagram'),
    'fechamento': ('Para casa', 'cink', '\\faHome'),
}

PREAMBULO = r'''\documentclass[aspectratio=169,11pt]{beamer}
\usefonttheme{professionalfonts}
\usepackage{fontspec}
\setsansfont{Inter}[Scale=0.92]
\setmonofont{DejaVu Sans Mono}[Scale=0.80]
\hyphenpenalty=10000\exhyphenpenalty=10000   % sem padrões de hifenização em português nesta instalação
\usepackage{amsmath,amssymb,booktabs,array,tikz,pgfplots,listings,fontawesome5,hyperref}
\usepackage[most]{tcolorbox}
\usepackage[noend]{algpseudocode}
\pgfplotsset{compat=1.18}
\usetikzlibrary{calc}
% ---------- cores
\definecolor{cink}{HTML}{1E1B4B}\definecolor{cmuted}{HTML}{64748B}\definecolor{csurface}{HTML}{F1F5F9}
\definecolor{cteoria}{HTML}{4F46E5}\definecolor{cpratica}{HTML}{0D9488}\definecolor{cexperimento}{HTML}{D97706}
\definecolor{cconexoes}{HTML}{DB2777}\definecolor{cok}{HTML}{16A34A}
\colorlet{cseg}{cteoria}\newcommand{\segnome}{Teoria}\newcommand{\segicone}{\faBook}
% ---------- tema
\setbeamertemplate{navigation symbols}{}
\setbeamercolor{normal text}{fg=cink}\setbeamercolor{structure}{fg=cteoria}
\setbeamercolor{alerted text}{fg=cconexoes}
\setbeamertemplate{itemize item}{\textcolor{cseg}{\raisebox{0.15ex}{\scriptsize$\blacktriangleright$}}}
\setbeamertemplate{itemize subitem}{\textcolor{cmuted}{--}}
\setbeamertemplate{enumerate item}{\textcolor{cseg}{\bfseries\insertenumlabel.}}
\setbeamerfont{frametitle}{size=\Large,series=\bfseries}
\setbeamertemplate{frametitle}{%
  \vspace{0.55cm}\hspace*{0.15cm}{\color{cseg}\scriptsize\bfseries\segicone\enspace\MakeUppercase{\segnome}}\par
  \vspace{0.05cm}\hspace*{0.15cm}{\color{cink}\usebeamerfont{frametitle}\insertframetitle}\par\vspace{-0.1cm}}
\setbeamersize{text margin left=0.9cm,text margin right=0.9cm}
\setbeamertemplate{footline}{%
  \begin{tikzpicture}[remember picture,overlay]
    \fill[csurface] (current page.south west) rectangle ($(current page.south east)+(0,0.5)$);
    \fill[cseg] (current page.south west) rectangle ($(current page.south west)+({\paperwidth*\insertframenumber/\inserttotalframenumber},0.06)$);
    \node[anchor=west,text=cmuted,font=\tiny] at ($(current page.south west)+(0.9,0.27)$) {\insertshorttitle};
    \node[anchor=east,text=cmuted,font=\tiny\bfseries] at ($(current page.south east)+(-0.9,0.27)$) {\insertframenumber\,/\,\inserttotalframenumber};
  \end{tikzpicture}}
\newcommand{\segmento}[3]{\colorlet{cseg}{#1}\renewcommand{\segnome}{#2}\renewcommand{\segicone}{#3}}
% ---------- caixas
\newtcolorbox{cartao}[2][]{enhanced,colback=white,colframe=#2,boxrule=0pt,leftrule=3pt,arc=3pt,
  left=8pt,right=8pt,top=5pt,bottom=5pt,fontupper=\small,#1}
\newtcolorbox{destaque}[1][cseg]{enhanced,colback=#1!7,colframe=#1,boxrule=0pt,leftrule=3pt,arc=3pt,
  left=8pt,right=8pt,top=5pt,bottom=5pt,fontupper=\small}
\newcommand{\etiqueta}[2]{\tikz[baseline=(t.base)]\node[fill=#1,text=white,rounded corners=2pt,inner sep=2.5pt,font=\tiny\bfseries](t){#2};}
% ---------- pseudocódigo em português
\algrenewcommand\algorithmicfor{\textbf{para}}\algrenewcommand\algorithmicdo{\textbf{faça}}
\algrenewcommand\algorithmicwhile{\textbf{enquanto}}\algrenewcommand\algorithmicif{\textbf{se}}
\algrenewcommand\algorithmicthen{\textbf{então}}\algrenewcommand\algorithmicelse{\textbf{senão}}
\algrenewcommand\algorithmicreturn{\textbf{retorne}}
\algrenewcommand\algorithmicrepeat{\textbf{repita}}\algrenewcommand\algorithmicuntil{\textbf{até que}}
\algrenewcommand\algorithmicprocedure{}\algrenewcommand\algorithmicfunction{}
\algrenewcommand{\algorithmiccomment}[1]{\hfill{\color{cmuted}\footnotesize// #1}}
\algrenewcommand\alglinenumber[1]{{\color{cmuted}\scriptsize#1}}
\newcommand{\Nome}[1]{\textsc{#1}}
\newcommand{\atrib}{\leftarrow}
\newenvironment{pseudo}[1]{\begin{tcolorbox}[enhanced,colback=csurface,colframe=csurface,arc=4pt,left=6pt,right=6pt,top=4pt,bottom=4pt,fontupper=\footnotesize]
  {\color{cteoria}\bfseries\textsc{#1}}\vspace{-2pt}\begin{algorithmic}[1]}{\end{algorithmic}\end{tcolorbox}}
% ---------- código
\lstset{language=C,basicstyle=\ttfamily\footnotesize,keywordstyle=\color{cteoria}\bfseries,
  commentstyle=\color{cmuted}\itshape,stringstyle=\color{cconexoes},columns=fullflexible,keepspaces=true,
  showstringspaces=false,breaklines=true,breakindent=3em,numbers=left,numberstyle=\tiny\color{cmuted},
  numbersep=8pt,xleftmargin=1.6em,backgroundcolor=\color{csurface},frame=none}
% ---------- gráficos
\pgfplotsset{moderno/.style={width=0.92\linewidth,height=5.6cm,axis lines=left,grid=major,
  grid style={draw=black!8},tick label style={font=\tiny,text=cmuted},label style={font=\scriptsize,text=cmuted},
  legend style={draw=none,fill=white,fill opacity=0.85,text opacity=1,font=\tiny,at={(0.02,0.98)},anchor=north west},
  every axis plot/.append style={thick},scaled ticks=false,
  yticklabel style={/pgf/number format/fixed,/pgf/number format/1000 sep={.},/pgf/number format/use comma},
  xticklabel style={/pgf/number format/fixed,/pgf/number format/1000 sep={.},/pgf/number format/use comma}}}
\pgfplotscreateplotcyclelist{serie}{{cteoria,mark=*,mark size=1.4pt,only marks},{cpratica,mark=square*,mark size=1.4pt,only marks},
  {cexperimento,mark=triangle*,mark size=1.8pt,only marks},{cconexoes,mark=diamond*,mark size=1.8pt,only marks}}
'''


def esc(s):
    return (s.replace('\\', '\\textbackslash{}').replace('&', '\\&').replace('%', '\\%').replace('#', '\\#')
             .replace('_', '\\_').replace('{', '\\{').replace('}', '\\}').replace('$', '\\$'))


def seg(nome):
    rot, cor, ic = SEGMENTOS[nome]
    return f'\\segmento{{{cor}}}{{{rot}}}{{{ic}}}'


def figura(fig, pdf_cormen, tmp):
    """Cropped figure (cached) copied into the build folder; returns its file name."""
    nome = f"fig_{fig.replace('.', '_')}.png"
    os.makedirs(CACHE, exist_ok=True)
    cache = os.path.join(CACHE, nome)
    if not os.path.exists(cache):
        cormen_fig.recortar(pdf_cormen, fig, cache)
    shutil.copy2(cache, os.path.join(tmp, nome))
    return nome


def legenda_fig(fig, texto):
    return (f"{{\\color{{cmuted}}\\scriptsize\\textbf{{Figura {fig}}} de Cormen et al. (2009)"
            + (f" — {texto}" if texto else '') + '}')


def quadro_teoria(q, pdf_cormen, tmp):
    """One theory frame: text, figure, pseudocode or a combination (two columns when text and visual coexist).
    Pseudocode and figure together do not fit one slide: the figure goes to a second frame with the same title."""
    if q.get('pseudo') and q.get('fig'):
        primeiro = {k: v for k, v in q.items() if k not in ('fig', 'legenda', 'altura')}
        segundo = {'titulo': q['titulo'] + ' (exemplo)', 'fig': q['fig'], 'legenda': q.get('legenda', ''), 'altura': 0.66}
        return quadro_teoria(primeiro, pdf_cormen, tmp) + '\n' + quadro_teoria(segundo, pdf_cormen, tmp)
    out = [f"\\begin{{frame}}{{{q['titulo']}}}"]
    visual = []
    if q.get('pseudo'):
        visual.append(f"\\begin{{pseudo}}{{{q['nome']}}}\n{q['pseudo'].strip()}\n\\end{{pseudo}}")
    if q.get('fig'):
        arq = figura(q['fig'], pdf_cormen, tmp)
        alt = q.get('altura', 0.62 if not q.get('texto') else 0.55)
        visual.append(f"\\centering\\includegraphics[width=\\linewidth,height={alt}\\textheight,keepaspectratio]{{{arq}}}\\par\\smallskip\n"
                      + legenda_fig(q['fig'], q.get('legenda', '')))
    texto = q.get('texto', '').strip()
    if texto and visual and not q.get('empilhar'):
        lt = q.get('largura_texto', 0.44)
        fonte = '\\footnotesize' if len(texto) > 520 else '\\small'     # texto longo ao lado da figura
        out += [f"\\begin{{columns}}[T,onlytextwidth]\\begin{{column}}{{{lt}\\textwidth}}{fonte}", texto,
                f"\\end{{column}}\\begin{{column}}{{{0.96 - lt:.2f}\\textwidth}}", '\n'.join(visual), '\\end{column}\\end{columns}']
    else:
        if texto:
            out.append(('\\footnotesize ' if len(texto) > 900 else '\\small ') + texto)
        out += visual
    if q.get('rodape'):
        out.append(f"\\vfill\\begin{{destaque}}{q['rodape']}\\end{{destaque}}")
    out.append('\\end{frame}')
    return '\n'.join(out)


def codigo_slide(caminho):
    """Code for the slides: without the header lines ('// Aula' and '// teste:')."""
    linhas = open(caminho).read().rstrip('\n').split('\n')
    while linhas and linhas[0].startswith('//'):
        linhas.pop(0)
    while linhas and not linhas[0].strip():
        linhas.pop(0)
    return linhas


def pedacos(linhas):
    """Same-height chunks of code (visual lines, wrapping counted), cut preferably at blank lines or closing braces."""
    total = len(linhas)
    peso = [max(1, -(-len(l) // COLUNAS)) for l in linhas]
    acum = [0]
    for p in peso:
        acum.append(acum[-1] + p)
    k = -(-acum[-1] // LINHAS_POR_SLIDE)
    while True:
        res, ini = [], 0
        for parte in range(1, k):
            alvo = acum[-1] * parte / k
            def nota(c):
                l = linhas[c - 1]
                bonus = 4 if not l.strip() else 3 if l.rstrip() == '}' else 1 if l.rstrip().endswith('}') else 0
                return abs(acum[c] - alvo) - bonus
            cand = [c for c in range(ini + 1, total) if acum[c] - acum[ini] <= LINHAS_POR_SLIDE
                    and acum[-1] - acum[c] <= LINHAS_POR_SLIDE * (k - parte)] or [ini + 1]
            corte = min(cand, key=nota)
            res.append((ini + 1, corte))
            ini = corte
        res.append((ini + 1, total))
        if all(acum[f] - acum[i - 1] <= LINHAS_POR_SLIDE for i, f in res):
            return res
        k += 1


def quadros_codigo(arquivo, titulo, tmp):
    linhas = codigo_slide(os.path.join(AQUI, 'c', arquivo))
    open(os.path.join(tmp, arquivo), 'w').write('\n'.join(linhas) + '\n')
    partes = pedacos(linhas)
    out = []
    for k, (i, f) in enumerate(partes, 1):
        suf = f' ({k}/{len(partes)})' if len(partes) > 1 else ''
        out.append(f"\\begin{{frame}}[fragile]{{{titulo}{suf}}}\n{{\\color{{cmuted}}\\tiny\\ttfamily {esc(arquivo)}}}\\par\\vspace{{2pt}}\n"
                   f"\\lstinputlisting[firstline={i},lastline={f},firstnumber={i}]{{{arquivo}}}\n\\end{{frame}}")
    return out


# ------------------------------------------------------------------ experimentos
FUNCOES = {'log2': math.log2, 'ln': math.log, 'sqrt': math.sqrt, 'log': math.log, 'exp': math.exp,
           'sum': sum, 'range': range, 'int': int, 'min': min, 'max': max, 'lgamma': math.lgamma,
           'ceil': math.ceil}


def num(v, casas=0, sig=False):
    """Number in Brazilian format: 1.234.567 or 0,503 (sig=True: 3 significant digits)."""
    if sig:
        s = f'{v:.3g}'
        return s.replace('.', ',') if 'e' not in s else s
    s = f'{v:,.{casas}f}'
    return s.replace(',', '_').replace('.', ',').replace('_', '.')


def fmt(v):
    """Adaptive pt-BR number for tables and legends: 1.234.567 · 12,3 · 0,503 · 1,58·10^{-7} (LaTeX)."""
    if v == 0:
        return '0'
    a = abs(v)
    if a >= 1000:
        return num(v)
    if a >= 10:
        return num(v, 1)
    if a >= 0.01:
        return num(v, 3)
    e = math.floor(math.log10(a))
    return f'${num(v / 10 ** e, 2)}\\cdot 10^{{{e}}}$'


def pct(v):
    return num(100 * v, 1) + '\\%'


def avalia(expr, n):
    return eval(expr, {'__builtins__': {}}, dict(FUNCOES, n=n))


def rodar_experimento(arquivo, tmp):
    fonte = os.path.join(AQUI, 'c', arquivo)
    exe = os.path.join(tmp, arquivo[:-2])
    c = subprocess.run(['gcc', '-O2', '-std=c17', '-Wall', '-Wextra', fonte, '-o', exe, '-lm'], capture_output=True, text=True)
    if c.returncode or c.stderr.strip():
        raise RuntimeError(f'{arquivo} não compila limpo:\n{c.stderr}')
    r = subprocess.run([exe], capture_output=True, text=True, timeout=600)
    if r.returncode:
        raise RuntimeError(f'{arquivo} terminou com erro {r.returncode}')
    tabelas = []                                               # tabelas separadas por linha em branco
    for bloco in re.split(r'\n\s*\n', r.stdout.strip()):
        linhas = [l.split(',') for l in bloco.strip().split('\n')]
        tabelas.append([dict(zip(linhas[0], map(float, l))) for l in linhas[1:]])
    return tabelas


def ajustar(dados, col, expr, x='n'):
    """Least-squares constant c for col ≈ c·f(n) over the upper half of n (the asymptotic regime). Returns c and the
    largest relative deviation over that half."""
    fs = [avalia(expr, d[x]) for d in dados]
    ys = [d[col] for d in dados]
    metade = len(dados) // 2                                   # ajuste e teste na metade superior de n:
    c = (sum(y * f for y, f in zip(ys[metade:], fs[metade:]))   # é o comportamento assintótico
         / sum(f * f for f in fs[metade:]))
    desvio = max(abs(y - c * f) / (c * f) for y, f in zip(ys[metade:], fs[metade:]) if f > 0)
    return c, desvio


def grafico(g, tabelas, nome, tmp):
    """pgfplots axis with the measured series and the theoretical curves (constant fitted or fixed)."""
    dados = tabelas[g.get('tabela', 0)]
    x = g.get('x', 'n')
    cols = list(dados[0].keys())
    teorias = []
    for t in g.get('teoria', []):
        if t.get('ajustar', True):
            c, desvio = ajustar(dados, t['col'], t['f'], x)
        else:                                                  # a teoria dá a constante exata: compara direto
            c = 1.0
            fs = [avalia(t['f'], d[x]) for d in dados]
            meio = len(dados) // 2
            desvio = max(abs(d[t['col']] - f) / f for d, f in zip(dados[meio:], fs[meio:]) if f > 0)
        if t.get('limite'):                                   # teoria é um limite: medido >= f (inferior) ou <= f (superior)
            fs = [avalia(t['f'], d[x]) for d in dados]
            sinal = 1 if t['limite'] == 'inferior' else -1
            fora = [d[x] for d, f in zip(dados, fs) if sinal * (d[t['col']] - f) < -1e-9]
            if fora:
                raise RuntimeError(f"{nome}: {t['col']} viola o limite {t['limite']} {t['f']} em n = {fora}")
            c, desvio = 1.0, max(abs(d[t['col']] / f - 1) for d, f in zip(dados, fs) if f > 0)
            teorias.append((t, c, desvio))
            continue
        tol = t.get('tolerancia', 0.15)
        if desvio > tol:
            raise RuntimeError(f"{nome}: {t['col']} se afasta {desvio:.1%} de {t['f']} (tolerância {tol:.0%})")
        teorias.append((t, c, desvio))
    arq = f'{nome}.csv'
    with open(os.path.join(tmp, arq), 'w') as f:
        extra = [f'teo{k}' for k in range(len(teorias))]
        f.write(','.join(cols + extra) + '\n')
        for d in dados:
            vals = [d[c] for c in cols] + [c_ * avalia(t['f'], d[x]) for t, c_, _ in teorias]
            f.write(','.join(f'{v:.6g}' for v in vals) + '\n')
    escala = {'log': 'xmode=log,ymode=log,log basis x=2,', 'logy': 'ymode=log,', 'logx': 'xmode=log,log basis x=2,',
              'linear': ''}[g.get('escala', 'linear')]
    out = [f"\\begin{{tikzpicture}}\\begin{{axis}}[moderno,{escala}cycle list name=serie,xlabel={{{g.get('xlabel', '$n$')}}},"
           f"ylabel={{{g.get('ylabel', '')}}}{',' + g['opcoes'] if g.get('opcoes') else ''}]"]
    for s in g['series']:
        estilo = f"+[{s['estilo']}]" if s.get('estilo') else ''
        out.append(f"\\addplot{estilo} table[x={x},y={s['col']},col sep=comma]{{{arq}}};\\addlegendentry{{{s['rotulo']}}}")
    for k, (t, c, _) in enumerate(teorias):
        rot = t['rotulo'] if not t.get('ajustar', True) else f"{fmt(c)} $\\cdot$ {t['rotulo']}"
        out.append(f"\\addplot[{t.get('cor', 'cink')},dashed,no marks,thick] table[x={x},y=teo{k},col sep=comma]{{{arq}}};\\addlegendentry{{{rot}}}")
    out.append('\\end{axis}\\end{tikzpicture}')
    return '\n'.join(out), teorias


def quadros_experimento(a, tmp):
    e = a['experimento']
    tabelas = rodar_experimento(e['programa'], tmp)
    out = [f"{seg('experimento')}"]
    # hipótese e método
    out.append(f"\\begin{{frame}}{{{e['titulo']}}}\n\\begin{{columns}}[T,onlytextwidth]\\begin{{column}}{{0.48\\textwidth}}"
               f"\\begin{{destaque}}[cexperimento]\\textbf{{Hipótese.}} {e['hipotese']}\\end{{destaque}}\\end{{column}}"
               f"\\begin{{column}}{{0.48\\textwidth}}\\small\\textbf{{Método}}\\begin{{enumerate}}\\setlength{{\\itemsep}}{{1pt}}"
               + ''.join(f'\\item {m}' for m in e['metodo']) + "\\end{enumerate}\\end{column}\\end{columns}\\end{frame}")
    resumo = []
    for k, g in enumerate(e['graficos']):
        corpo, teorias = grafico(g, tabelas, f"exp_{ident(a)}_{k}", tmp)
        dados = tabelas[g.get('tabela', 0)]
        tab = ''
        if teorias:
            t, c, desvio = teorias[0]
            x = g.get('x', 'n')
            amostra = dados[::max(1, len(dados) // 5)][:5] + [dados[-1]]
            linhas = '\\\\'.join(f"{fmt(d[x])} & {fmt(d[t['col']])} & {fmt(d[t['col']] / avalia(t['f'], d[x]))}" for d in amostra)
            tab = (f"\\scriptsize\\begin{{tabular}}{{rrr}}\\toprule ${x}$ & medido & razão\\\\\\midrule {linhas}\\\\\\bottomrule\\end{{tabular}}"
                   f"\\par{{\\tiny\\color{{cmuted}} razão = medido $\\div$ {t['rotulo']}}}"
                   f"\\par\\smallskip\\etiqueta{{cok}}{{\\faCheck\\ " + ((f"sempre $\\ge$ o limite" if t['limite'] == 'inferior' else f"sempre $\\le$ o limite") if t.get('limite') else f"desvio máx. {pct(desvio)}") + "}")
            resumo.append(f"{t['col']} ≈ {c:.3g}·{t['f']} (desvio {desvio:.1%})")       # só para o terminal
        out.append(f"\\begin{{frame}}{{{g['titulo']}}}\n\\begin{{columns}}[T,onlytextwidth]\\begin{{column}}{{0.64\\textwidth}}{corpo}\\end{{column}}"
                   f"\\begin{{column}}{{0.34\\textwidth}}\\vspace{{0.3cm}}{tab}\\par\\medskip{{\\scriptsize {g.get('leitura', '')}}}\\end{{column}}\\end{{columns}}\\end{{frame}}")
    out.append(f"\\begin{{frame}}{{O que o experimento mostrou}}\n\\begin{{destaque}}[cok]{e['conclusao']}\\end{{destaque}}"
               + (f"\\medskip\\small {e['extra']}" if e.get('extra') else '')
               + f"\\vfill{{\\scriptsize\\color{{cmuted}}\\faTerminal\\ Reproduza: \\texttt{{gcc -O2 {esc(e['programa'])} -o exp -lm \\&\\& ./exp}}}}\\end{{frame}}")
    return out, resumo


# ------------------------------------------------------------------ deck
def ident(a):
    """File name of the class deck: aula04 (numbered classes) or the explicit id (compl1)."""
    return a['id'] if 'id' in a else f"aula{a['n']:02d}"


def rotulo(a):
    return a.get('rotulo', f"Aula {a['n']}")


def referencia(a):
    """Reference line of a deck: Cormen by default, or the class's own 'fonte' (the C annex)."""
    return a['fonte'] if 'fonte' in a else f"Cormen et al., \\emph{{Algoritmos}}: {a['cormen']}"


def secao(a):
    """Subtitle of the title slide: the section of the book (\"Seção 10.1\"), with no author: Cormen is credited
    only under the figures taken from the book. Annex modules show their own C reference."""
    if 'fonte' in a:
        return a['fonte'].split(';')[0]
    return a['cormen'][:1].upper() + a['cormen'][1:]


def rotulo_bloco(b):
    return b.get('rotulo', f"Bloco {b['n']}")


def titulo_deck(a, bloco):
    barras = '\n'.join(f"\\fill[white,opacity={0.10 + 0.05 * (k % 4):.2f}] ({10.4 + k * 0.36:.2f},0.9) rectangle +(0.24,{0.3 + h * 0.3:.2f});"
                       for k, h in enumerate([1, 3, 2, 5, 4, 7, 6, 9, 8, 10, 11, 12]))
    return f"""\\begin{{frame}}[plain]
\\begin{{tikzpicture}}[remember picture,overlay]
\\fill[cink] (current page.south west) rectangle (current page.north east);
\\begin{{scope}}[shift={{(current page.south west)}}]
{barras}
\\fill[cteoria] (0.9,6.55) rectangle +(1.2,0.08);
\\node[anchor=north west,text=white!70,font=\\small\\bfseries] at (0.9,6.4) {{{rotulo(a).upper()} \\enspace·\\enspace {rotulo_bloco(bloco).upper()}: {bloco['titulo'].upper()}}};
\\node[anchor=north west,text=white,font=\\huge\\bfseries,text width=9.6cm,align=left] at (0.9,5.7) {{{a['tema']}}};
\\node[anchor=north west,text=white!75,font=\\normalsize,text width=9.6cm] at (0.9,3.55) {{{secao(a)}}};
\\node[anchor=south west,text=white!60,font=\\scriptsize] at (0.9,0.9) {{Estruturas de dados e seus algoritmos \\enspace·\\enspace José Dihego \\enspace·\\enspace IFBA}};
\\end{{scope}}
\\end{{tikzpicture}}
\\end{{frame}}"""


def abertura_segmento(nome, itens):
    rot, cor, ic = SEGMENTOS[nome]
    lista = ''.join(f'\\item {i}' for i in itens)
    return f"""{seg(nome)}
\\begin{{frame}}[plain]
\\begin{{tikzpicture}}[remember picture,overlay]
\\fill[{cor}] (current page.south west) rectangle ($(current page.south west)+(0.35,\\paperheight)$);
\\node[anchor=west,text={cor},font=\\fontsize{{44}}{{44}}\\selectfont] at ($(current page.west)+(1.2,0.9)$) {{{ic}}};
\\node[anchor=west,text=cink,font=\\Huge\\bfseries] at ($(current page.west)+(3.0,0.9)$) {{{rot}}};
\\node[anchor=north west,text=cmuted,font=\\small,text width=11cm] at ($(current page.west)+(3.05,0.15)$) {{\\begin{{itemize}}\\setlength{{\\itemsep}}{{2pt}}{lista}\\end{{itemize}}}};
\\end{{tikzpicture}}
\\end{{frame}}"""


def deck(a, bloco, pdf_cormen, tmp):
    out = [PREAMBULO, f"\\title[{rotulo(a)} · {a['curto']}]{{{a['tema']}}}", '\\begin{document}', titulo_deck(a, bloco)]
    # roteiro
    out.append(seg('teoria'))
    out.append("\\begin{frame}{Roteiro da aula}\n\\begin{columns}[T,onlytextwidth]\\begin{column}{0.56\\textwidth}\\small\\textbf{Ao final, você será capaz de}"
               "\\begin{itemize}\\setlength{\\itemsep}{2pt}" + ''.join(f'\\item {o}' for o in a['objetivos'])
               + "\\end{itemize}\\end{column}\\begin{column}{0.40\\textwidth}"
               + ''.join(f"\\begin{{cartao}}[top=2pt,bottom=2pt,before skip=0pt,after skip=3pt]{{{SEGMENTOS[s][1]}}}{{\\color{{{SEGMENTOS[s][1]}}}{SEGMENTOS[s][2]}}}\\enspace\\textbf{{\\footnotesize {SEGMENTOS[s][0]}}}\\par{{\\tiny\\color{{cmuted}} {d}}}\\end{{cartao}}"
                         for s, d in [('teoria', a['roteiro'][0]), ('pratica', a['roteiro'][1]), ('experimento', a['roteiro'][2]), ('conexoes', a['roteiro'][3])])
               + "\\end{column}\\end{columns}\\end{frame}")
    # teoria
    out.append(seg('teoria'))                                  # a teoria começa sem slide de abertura
    out += [quadro_teoria(q, pdf_cormen, tmp) for q in a['teoria']]
    # prática
    p = a['pratica']
    out.append(abertura_segmento('pratica', p['resumo']))
    for nota in p.get('notas', []):
        out.append(f"\\begin{{frame}}{{{nota['titulo']}}}\n\\small {nota['texto']}\n\\end{{frame}}")
    for arq, tit in p['arquivos']:
        out += quadros_codigo(arq, tit, tmp)
    # experimento
    out.append(abertura_segmento('experimento', a['experimento']['resumo']))
    exp, resumo = quadros_experimento(a, tmp)
    out += exp
    # conexões
    out.append(abertura_segmento('conexoes', [c[1] for c in a['conexoes']]))
    cartoes = [f"\\begin{{cartao}}[equal height group=con{k // 4},valign=top]{{cconexoes}}{{\\color{{cconexoes}}{ic}}}\\enspace\\textbf{{{area}}}\\par\\vspace{{2pt}}{{\\scriptsize {txt}}}\\end{{cartao}}"
               for k, (ic, area, txt) in enumerate(a['conexoes'])]
    for k in range(0, len(cartoes), 4):
        grupo = cartoes[k:k + 4]
        linhas = []
        for j in range(0, len(grupo), 2):
            par = grupo[j:j + 2]
            linhas.append('\\begin{columns}[T,onlytextwidth]' + ''.join(f'\\begin{{column}}{{0.485\\textwidth}}{c}\\end{{column}}' for c in par) + '\\end{columns}')
        out.append(f"\\begin{{frame}}{{Onde isso aparece na computação{' (cont.)' if k else ''}}}\n" + '\\vspace{2pt}'.join(linhas) + '\n\\end{frame}')
    # fechamento
    out.append(seg('fechamento'))
    fonte_ex = '\\footnotesize' if sum(len(x) for x in a['exercicios']) > 380 else '\\small'
    out.append("\\begin{frame}{Para casa}\n\\begin{columns}[T,onlytextwidth]\\begin{column}{0.58\\textwidth}" + fonte_ex + "\\textbf{Exercícios}"
               "\\begin{enumerate}\\setlength{\\itemsep}{2pt}" + ''.join(f'\\item {x}' for x in a['exercicios'])
               + "\\end{enumerate}\\end{column}\\begin{column}{0.38\\textwidth}\\begin{destaque}[cink]\\textbf{Leitura}\\par\\footnotesize "
               + a['leitura'] + f"\\end{{destaque}}\\begin{{destaque}}[cpratica]\\textbf{{Código}}\\par\\footnotesize\\href{{{SITE}/estruturas/\\#aula-{a['n']}}}{{josedihego.net/estruturas}}"
               + "\\end{destaque}\\end{column}\\end{columns}\\end{frame}")
    out.append('\\end{document}')
    return '\n'.join(out) + '\n', resumo


def icones(fonte):
    """\\faProjectDiagram -> \\faIcon{project-diagram}: every fontawesome5 icon works this way, not all have a macro."""
    return re.sub(r'\\fa([A-Z][A-Za-z]*)', lambda m: '\\faIcon{' + re.sub(r'(?<!^)(?=[A-Z])', '-', m.group(1)).lower() + '}', fonte)


def compilar(nome, fonte, tmp):
    open(os.path.join(tmp, nome + '.tex'), 'w').write(icones(fonte))
    for _ in range(2):
        c = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', nome + '.tex'], cwd=tmp, capture_output=True, text=True)
        if c.returncode:
            log = open(os.path.join(tmp, nome + '.log'), errors='replace').read()
            i = log.find('\n!')
            raise RuntimeError(f'{nome}: ' + log[i:i + 600])
    log = open(os.path.join(tmp, nome + '.log'), errors='replace').read()
    avisos = re.findall(r'Overfull \\vbox \(([\d.]+)pt', log)
    faltando = sorted(set(re.findall(r'Missing character: There is no (.) ', log)))
    return os.path.join(tmp, nome + '.pdf'), [a for a in avisos if float(a) > 3], faltando


# ------------------------------------------------------------------ dados da página
def yml(valor, nivel=0):
    pad = '  ' * nivel
    if isinstance(valor, dict):
        return ''.join(f'{pad}{k}:' + ('\n' + yml(v, nivel + 1) if isinstance(v, (dict, list)) and v else ' ' + yml(v).strip() + '\n')
                       for k, v in valor.items())
    if isinstance(valor, list):
        if not valor:
            return '[]\n'
        return ''.join(f'{pad}- ' + yml(v, nivel + 1).lstrip() if isinstance(v, (dict, list)) else f'{pad}- {yml(v).strip()}\n' for v in valor)
    return json.dumps(valor, ensure_ascii=False) + '\n'


def sem_latex(s):
    """Text for the page from the LaTeX of plano.py: formatting commands are dropped and $...$ becomes \\(...\\),
    which MathJax renders (the page sets mathjax: true). Output is plain text, escaped by the template."""
    partes = re.split(r'(\$[^$]*\$)', s)
    saida = []
    for p in partes:
        if p.startswith('$') and p.endswith('$') and len(p) > 1:
            m = p[1:-1].replace('\\atrib', '\\leftarrow').replace('\\Nome', '\\textsf')
            saida.append('\\(' + m + '\\)')
        else:
            for _ in range(2):                         # comandos aninhados: duas passadas
                p = re.sub(r'\\(textbf|emph|texttt|textit|textsc|Nome|textsf)\{([^{}]*)\}', r'\2', p)
            p = (p.replace("``", '“').replace("''", '”').replace('\\%', '%').replace('\\&', '&')
                  .replace('\\_', '_').replace('\\,', ' ').replace('~', ' ').replace('--', '–'))
            saida.append(p)
    return ''.join(saida)


def gerar(raiz, pdf_cormen, slides=True, so=None):
    destino = os.path.join(raiz, 'assets', 'estruturas')
    for sub in ('slides', 'codigo'):
        os.makedirs(os.path.join(destino, sub), exist_ok=True)
    for f in glob.glob(os.path.join(destino, 'codigo', '*.c')):
        os.remove(f)
    for f in sorted(glob.glob(os.path.join(AQUI, 'c', '*.c'))):
        linhas = [l for l in open(f).read().split('\n') if not l.startswith('// teste:')]
        open(os.path.join(destino, 'codigo', os.path.basename(f)), 'w').write('\n'.join(linhas))
    blocos = {b['n']: b for b in BLOCOS}
    resumos = {}
    if slides:
        with tempfile.TemporaryDirectory() as tmp:
            for a in AULAS:
                if a.get('tipo') or (so and str(a['n']) not in so):
                    continue
                nome = ident(a)
                fonte, resumo = deck(a, blocos[a['bloco']], pdf_cormen, tmp)
                pdf, avisos, faltando = compilar(nome, fonte, tmp)
                shutil.copy2(pdf, os.path.join(destino, 'slides', nome + '.pdf'))
                resumos[a['n']] = resumo
                print(nome, 'ok', f'overfull {avisos}' if avisos else '', f'sem glifo {faltando}' if faltando else '', '|', '; '.join(resumo))
    saida = []
    for b in BLOCOS:
        aulas = []
        for a in (x for x in AULAS if x['bloco'] == b['n']):
            d = {'n': a['n'], 'tema': sem_latex(a['tema']), 'tipo': a.get('tipo', 'aula')}
            if a.get('tipo'):
                d['descricao'] = sem_latex(a['descricao'])
                d['entregas'] = [sem_latex(e) for e in a['entregas']]
            else:
                d.update({'cormen': sem_latex(a['fonte']) if 'fonte' in a else 'Cormen, ' + a['cormen'], 'slides': ident(a) + '.pdf',
                          'objetivos': [sem_latex(o) for o in a['objetivos']],
                          'codigo': [{'arquivo': f, 'titulo': t} for f, t in a['pratica']['arquivos']],
                          'experimento': {'arquivo': a['experimento']['programa'], 'pergunta': sem_latex(a['experimento']['pergunta']),
                                          'conclusao': sem_latex(re.sub(r'\\s+', ' ', a['experimento']['conclusao']))},
                          'conexoes': [{'area': sem_latex(ar), 'texto': sem_latex(tx)} for _, ar, tx in a['conexoes']]})
            aulas.append(d)
        saida.append({'bloco': b['n'], 'rotulo': rotulo_bloco(b), 'opcional': b.get('opcional', False), 'tag': b.get('tag', ''),
                      'titulo': b['titulo'], 'resumo': b['resumo'], 'aulas': aulas})
    with open(os.path.join(raiz, '_data', 'estruturas.yml'), 'w') as y:
        y.write('# Gerado por _tools/estruturas/gerar.py a partir de plano.py – não edite à mão\n' + yml(saida))


if __name__ == '__main__':
    so = set(sys.argv[sys.argv.index('--aulas') + 1].split(',')) if '--aulas' in sys.argv else None
    gerar(sys.argv[1], sys.argv[2], '--sem-slides' not in sys.argv, so)
