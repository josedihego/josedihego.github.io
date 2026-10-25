"""Builds the /logica/ course from plano.py, questoes.json and solucoes/:
  assets/logica/solucoes/*.c        solutions without the '// teste:' lines
  assets/logica/slides/aulaNN.pdf   one Beamer deck per content class (xelatex, theme metropolis)
  _data/logica.yml                  blocks, classes, questions and question bank, for _pages/logica.md
The exam PDFs are not copied: every question links to its PDF in the public repository PROVAS.
Uso: python3 _tools/logica/gerar.py <raiz do site> [--sem-slides] [--aulas 1,2]"""
import sys, os, re, json, glob, shutil, subprocess, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from plano import BLOCOS, AULAS

SITE = 'https://josedihego.net'
PROVAS = 'https://github.com/josedihego/programacaoC/blob/main/INF027_listas_provas_PDF/'
ROMANOS = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
LINHAS_POR_SLIDE = 18
COLUNAS = 92                                                  # caracteres por linha de código no slide (footnotesize)


def arquivo_solucao(qid):
    """'A1-2015.2-QI-B' -> 'a1_2015_2_b_q1.c'; 'A1-2026.2-QIa' -> 'a1_2026_2_q1a.c'."""
    m = re.match(r'A(\d)-(\d{4})\.(\d)-Q([IV]+)([ab]?)(?:-([A-Z]))?$', qid)
    av, ano, sem, rom, sub, ver = m.groups()
    return f'a{av}_{ano}_{sem}_' + (ver.lower() + '_' if ver else '') + f'q{ROMANOS[rom]}{sub}.c'


def rotulo(q):
    """Human label: 'Avaliação 1 – 2014.2 (versão B), Questão I'."""
    nome = 'Avaliação Final' if q['avaliacao'] == 4 else f"Avaliação {q['avaliacao']}"
    ver = re.search(r'_([A-Z])\.pdf$', q['pdf'])
    return f"{nome} – {q['periodo']}" + (f' (versão {ver.group(1)})' if ver else '') + f", Questão {q['questao']}"


def limpar(texto):
    """Statement text for the page: fixes the 'posiçõ es' spacing of some PDFs and drops the exam instructions."""
    if re.search(r'çã o|õ es|ú mero|á ria|ô nia', texto):
        texto = re.sub(r'(?<=\w)([ãõáéíóúçâêô]) (?=(o|os|es|ão|rias?|rios?|meros?|ncias?|vel|veis|ticas?|ticos?|gicas?|ximos?|nimos?|lidos?|lidas?|ssaros|ximas?|ximos?|nias?)\b)',
                       r'\1', texto)
        texto = re.sub(r'\bá rea', 'área', texto)
    texto = re.split(r'\n\s*(Orientações|Instruções)', texto)[0]
    return re.sub(r'\n{3,}', '\n\n', texto).strip()


def tex(s):
    """Escapes LaTeX and converts the markup `code` and **bold**."""
    def esc(x):
        return (x.replace('\\', '\x00').replace('{', '\\{').replace('}', '\\}').replace('$', '\\$')
                 .replace('&', '\\&').replace('#', '\\#').replace('_', '\\_').replace('%', '\\%')
                 .replace('^', '\\^{}').replace('~', '\\~{}').replace('\x00', '\\textbackslash{}'))
    partes = re.split(r'(`[^`]*`)', s)
    saida = ''
    for p in partes:
        if p.startswith('`') and p.endswith('`') and len(p) > 1:
            saida += '\\texttt{' + esc(p[1:-1]).replace("'", "\\textquotesingle{}") + '}'
        else:
            saida += re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', esc(p))
    for c, m in SIMBOLOS.items():                             # símbolos fora da fonte do texto
        saida = saida.replace(c, m)
    return saida


SIMBOLOS = {'π': '$\\pi$', 'σ': '$\\sigma$', 'Δ': '$\\Delta$', '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '√': '$\\sqrt{\\ }$',
            '≤': '$\\le$', '−': '$-$', '⏎': '$\\hookleftarrow$', '→': '$\\to$'}


def md(s):
    """Markup of plano.py for the page (markdownify understands `code` and **bold** already)."""
    return s


MESA_C = r'''#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#define MESA(...) (printf(__VA_ARGS__), printf(" \\\\\n"))
int main(void) {
%s
return 0;
}
'''


def rodar_mesa(codigo, tmp):
    fonte, exe = os.path.join(tmp, 'mesa.c'), os.path.join(tmp, 'mesa')
    open(fonte, 'w').write(MESA_C % codigo)
    c = subprocess.run(['gcc', '-std=c17', '-w', fonte, '-o', exe, '-lm'], capture_output=True, text=True)
    if c.returncode:
        raise RuntimeError('teste de mesa não compila:\n' + c.stderr + codigo)
    return subprocess.run([exe], capture_output=True, text=True, timeout=5).stdout


def codigo_sem_testes(caminho):
    """Solution for the slides: without the header lines (title and '// teste:') and with the comments moved left, to
    the column after the longest short line of code (long lines keep two spaces before the comment)."""
    linhas = open(caminho).read().rstrip('\n').split('\n')
    while linhas and linhas[0].startswith('//'):
        linhas.pop(0)
    partes = [re.match(r'^(.*?\S)\s{2,}(// .*)$', l) for l in linhas]
    curtas = [len(m.group(1)) for m in partes if m and len(m.group(1)) <= 44]
    coluna = max(curtas, default=0) + 2
    return [m.group(1).ljust(coluna if len(m.group(1)) < coluna else len(m.group(1)) + 2) + m.group(2) if m else l
            for m, l in zip(partes, linhas)]


def pedacos(linhas):
    """Splits the code into slides of about the same height. Height is counted in visual lines (a line longer than
    COLUNAS wraps), at most LINHAS_POR_SLIDE per slide; cuts prefer a blank line or a closing brace near the ideal point."""
    total = len(linhas)
    peso = [max(1, -(-len(l) // COLUNAS)) for l in linhas]
    acum = [0]
    for p in peso:
        acum.append(acum[-1] + p)
    k = -(-acum[-1] // LINHAS_POR_SLIDE)                      # número de slides (arredonda para cima)
    while True:
        res, ini = [], 0
        for parte in range(1, k):
            alvo = acum[-1] * parte / k                       # altura ideal acumulada até o corte
            def nota(c):                                      # menor é melhor: distância do alvo, com bônus
                l = linhas[c - 1]
                bonus = 4 if not l.strip() else 3 if l.rstrip() in ('}', '    }') else 0
                return abs(acum[c] - alvo) - bonus
            candidatos = [c for c in range(ini + 1, total) if acum[c] - acum[ini] <= LINHAS_POR_SLIDE
                          and acum[-1] - acum[c] <= LINHAS_POR_SLIDE * (k - parte)] or [ini + 1]
            corte = min(candidatos, key=nota)
            res.append((ini + 1, corte))
            ini = corte
        res.append((ini + 1, total))
        if all(acum[f] - acum[i - 1] <= LINHAS_POR_SLIDE for i, f in res):
            return res
        k += 1                                                # não coube: um slide a mais


PREAMBULO = r'''\documentclass[aspectratio=169,10pt]{beamer}
\usetheme[progressbar=frametitle,numbering=fraction]{metropolis}
\usepackage{fontspec}
\setmonofont{DejaVu Sans Mono}[Scale=0.84]
\usepackage{listings,xcolor,booktabs,array,hyperref}
\definecolor{azul}{HTML}{1F4E79}\definecolor{verde}{HTML}{2E7D32}\definecolor{vermelho}{HTML}{C62828}
\setbeamercolor{frametitle}{bg=azul}\setbeamercolor{progress bar}{fg=orange}
\setbeamercolor{alerted text}{fg=vermelho}
\hypersetup{colorlinks,urlcolor=azul,linkcolor=azul}
\lstset{language=C,basicstyle=\ttfamily\footnotesize,keywordstyle=\color{azul}\bfseries,
  commentstyle=\color{verde!80!black}\itshape,stringstyle=\color{vermelho!80!black},columns=fullflexible,
  keepspaces=true,showstringspaces=false,breaklines=true,breakindent=3em,
  numbers=left,numberstyle=\tiny\color{gray},numbersep=6pt,xleftmargin=1.5em}
\lstdefinestyle{curto}{numbers=none,xleftmargin=0pt,basicstyle=\ttfamily\small}
\newcommand{\errado}[1]{\textcolor{vermelho}{\texttt{#1}}}
\newcommand{\certo}[1]{\textcolor{verde}{\texttt{#1}}}
'''


def fonte_tex(q):
    url = PROVAS + q['pdf']
    return f"\\href{{{url}}}{{\\textbf{{{tex(rotulo(q))}}}}}\\\\[-2pt]{{\\scriptsize\\ttfamily {tex(q['pdf'])}}}"


def deck(a, Q, sol_dir, tmp, bloco):
    """LaTeX source of a class deck; code files are written to tmp."""
    r, p = Q[a['resolvida']], Q[a['proposta']]
    nn = f"{a['n']:02d}"
    out = [PREAMBULO,
           f"\\title{{Aula {a['n']}: {tex(a['tema'])}}}",
           f"\\subtitle{{Lógica de Programação – Superior · Bloco {bloco['n']}}}",
           '\\author{José Dihego · IFBA}\\date{}',
           '\\begin{document}', '\\maketitle']
    # 1. objetivo e conceitos
    out.append('\\begin{frame}{O que você precisa saber hoje}')
    out.append(f"\\alert{{Objetivo:}} {tex(a['objetivo'])}\\par\\medskip")
    out.append('\\begin{itemize}\\setlength{\\itemsep}{3pt}')
    out += [f'\\item {tex(c)}' for c in a['conceitos']]
    out.append('\\end{itemize}\\end{frame}')
    # 2. padrão
    open(os.path.join(tmp, f'padrao{nn}.c'), 'w').write(a['padrao'] + '\n')
    out.append('\\begin{frame}[fragile]{O padrão em C}')
    out.append(f'\\lstinputlisting[style=curto]{{padrao{nn}.c}}')
    out.append('\\end{frame}')
    # 3. erros
    out.append('\\begin{frame}{Erros que custam pontos}')
    out.append('\\renewcommand{\\arraystretch}{1.5}\\footnotesize')
    out.append('\\begin{tabular}{>{\\raggedright}p{0.31\\textwidth}>{\\raggedright}p{0.31\\textwidth}>{\\raggedright\\arraybackslash}p{0.30\\textwidth}}')
    out.append('\\toprule \\textbf{Errado} & \\textbf{Certo} & \\textbf{Por quê}\\\\ \\midrule')
    for e, c, pq in a['erros']:
        out.append(f'\\errado{{{tex(e)}}} & \\certo{{{tex(c)}}} & {tex(pq)}\\\\')
    out.append('\\bottomrule\\end{tabular}\\end{frame}')
    # 4. teste de mesa
    m = a['mesa']
    linhas = rodar_mesa(m['codigo'], tmp).strip().split('\n')
    tabela = ['\\begin{tabular}{' + 'c' * len(m['cab']) + '}', '\\toprule ' + ' & '.join(m['cab']) + '\\\\ \\midrule']
    tabela += linhas + ['\\bottomrule\\end{tabular}']
    tamanho = '\\footnotesize' if len(linhas) <= 9 else '\\scriptsize' if len(linhas) <= 14 else '\\tiny'
    out.append('\\begin{frame}[fragile]{Teste de mesa}')
    if m.get('oculto'):
        out.append(f"{tex(m.get('legenda', 'Execute à mão e confira com a tabela:'))}\\par\\medskip")
        out.append('\\centering' + tamanho)
        out += tabela
    else:
        visivel = '\n'.join(l for l in m['codigo'].split('\n') if not l.strip().startswith('MESA('))
        open(os.path.join(tmp, f'mesa{nn}.c'), 'w').write(visivel + '\n')
        out.append('\\begin{columns}[T]\\begin{column}{0.5\\textwidth}')
        out.append(f'\\lstinputlisting[style=curto,basicstyle=\\ttfamily\\footnotesize]{{mesa{nn}.c}}')
        out.append('\\end{column}\\begin{column}{0.48\\textwidth}\\centering' + tamanho)
        out += tabela
        out.append('\\end{column}\\end{columns}')
    out.append('\\end{frame}')
    # 5. questão resolvida
    out.append(f"\\begin{{frame}}{{Questão resolvida em sala}}")
    out.append(f"{fonte_tex(r)}\\par\\medskip")
    out.append(f"\\textbf{{{tex(titulo_q(r, sol_dir))}}}\\par\\medskip")
    out.append('Estratégia:\\begin{enumerate}\\setlength{\\itemsep}{3pt}')
    out += [f'\\item {tex(s)}' for s in a['passos']]
    out.append('\\end{enumerate}')
    out.append(f"\\vfill{{\\scriptsize Enunciado completo (com figuras e exemplos) no PDF da prova.}}")
    out.append('\\end{frame}')
    # 6. código da solução
    sol = arquivo_solucao(a['resolvida'])
    codigo = codigo_sem_testes(os.path.join(sol_dir, sol))
    open(os.path.join(tmp, sol), 'w').write('\n'.join(codigo) + '\n')
    partes = pedacos(codigo)
    for k, (ini, fim) in enumerate(partes, 1):
        sufixo = f' ({k}/{len(partes)})' if len(partes) > 1 else ''
        out.append(f"\\begin{{frame}}[fragile]{{Solução{sufixo}}}")
        out.append(f'\\lstinputlisting[firstline={ini},lastline={fim},firstnumber={ini}]{{{sol}}}')
        out.append('\\end{frame}')
    # 7. sua vez
    teste = re.search(r'^// teste: (.*?) => (.*)$', open(os.path.join(sol_dir, arquivo_solucao(a['proposta']))).read(), re.M)
    out.append('\\begin{frame}{Sua vez: questão proposta}')
    out.append(f"{fonte_tex(p)}\\par\\medskip")
    out.append(f"\\textbf{{{tex(titulo_q(p, sol_dir))}}}\\par\\medskip")
    out.append('Dicas:\\begin{itemize}\\setlength{\\itemsep}{3pt}')
    out += [f'\\item {tex(d)}' for d in a['dica']]
    out.append('\\end{itemize}')
    if teste and len(teste.group(1)) <= 70:                  # exemplo curto; os longos ficam no enunciado
        entrada = teste.group(1).replace(';', ' ⏎ ')
        out.append(f"\\medskip{{\\small Para conferir: entrada \\texttt{{{tex(entrada)}}} → a saída deve conter \\texttt{{{tex(teste.group(2))}}}}}")
    out.append(f"\\vfill{{\\scriptsize A solução comentada está na página do curso: {SITE}/logica/\\#aula-{a['n']}}}")
    out.append('\\end{frame}')
    out.append('\\end{document}')
    return '\n'.join(out) + '\n'


def titulo_q(q, sol_dir):
    """Short title from the solution header ('// A1-2014.2 – Questão I: title')."""
    caminho = os.path.join(sol_dir, arquivo_solucao(q['id']))
    if os.path.exists(caminho):
        return open(caminho).readline().split(': ', 1)[1].strip()
    return ''                                                 # sem solução (banco): só o link para o PDF


def compilar(nome, fonte, tmp):
    open(os.path.join(tmp, nome + '.tex'), 'w').write(fonte)
    for _ in range(2):                                        # 2 passadas: barra de progresso e numeração
        c = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', nome + '.tex'],
                           cwd=tmp, capture_output=True, text=True)
        if c.returncode:
            erro = [l for l in open(os.path.join(tmp, nome + '.log'), errors='replace') if l.startswith('!')]
            raise RuntimeError(f'{nome}: ' + ''.join(erro[:3]))
    avisos = [l.strip() for l in open(os.path.join(tmp, nome + '.log'), errors='replace') if 'Overfull \\vbox' in l or 'Missing character' in l]
    return os.path.join(tmp, nome + '.pdf'), avisos


def questao_yml(q, sol_dir):
    sol = arquivo_solucao(q['id'])
    d = {'id': q['id'], 'rotulo': rotulo(q), 'titulo': titulo_q(q, sol_dir), 'pdf': q['pdf'], 'url': PROVAS + q['pdf']}
    if os.path.exists(os.path.join(sol_dir, sol)):
        d['solucao'] = sol
        d['codigo'] = '\n'.join(l for l in open(os.path.join(sol_dir, sol)).read().rstrip('\n').split('\n')
                                if not l.startswith('// teste:'))
    return d


def yml(valor, nivel=0):
    """Minimal YAML writer (strings as JSON, which YAML accepts)."""
    pad = '  ' * nivel
    if isinstance(valor, dict):
        return ''.join(f'{pad}{k}:' + ('\n' + yml(v, nivel + 1) if isinstance(v, (dict, list)) and v else ' ' + yml(v).strip() + '\n')
                       for k, v in valor.items())
    if isinstance(valor, list):
        if not valor:
            return '[]\n'
        s = ''
        for v in valor:
            corpo = yml(v, nivel + 1)
            s += f'{pad}- ' + corpo.lstrip() if isinstance(v, (dict, list)) else f'{pad}- {yml(v).strip()}\n'
        return s
    return json.dumps(valor, ensure_ascii=False) + '\n'


def gerar(raiz, slides=True, so_aulas=None):
    Q = {q['id']: q for q in json.load(open(os.path.join(AQUI, 'questoes.json')))}
    sol_dir = os.path.join(AQUI, 'solucoes')
    destino = os.path.join(raiz, 'assets', 'logica')
    for sub in ('solucoes', 'slides'):
        os.makedirs(os.path.join(destino, sub), exist_ok=True)
    # soluções publicadas: sem as linhas de teste
    for f in glob.glob(os.path.join(destino, 'solucoes', '*.c')):
        os.remove(f)
    for f in sorted(glob.glob(os.path.join(sol_dir, '*.c'))):
        linhas = [l for l in open(f).read().split('\n') if not l.startswith('// teste:')]
        open(os.path.join(destino, 'solucoes', os.path.basename(f)), 'w').write('\n'.join(linhas))
    # slides
    blocos = {b['n']: b for b in BLOCOS}
    bloco_de = lambda n: 1 if n <= 12 else 2 if n <= 24 else 3
    if slides:
        with tempfile.TemporaryDirectory() as tmp:
            for a in AULAS:
                if a.get('tipo') or (so_aulas and a['n'] not in so_aulas):
                    continue
                nome = f"aula{a['n']:02d}"
                pdf, avisos = compilar(nome, deck(a, Q, sol_dir, tmp, blocos[bloco_de(a['n'])]), tmp)
                shutil.copy2(pdf, os.path.join(destino, 'slides', nome + '.pdf'))
                print(nome, 'ok' + (f' – {len(avisos)} overfull vbox' if avisos else ''))
    # dados da página
    usadas = set()
    saida = []
    for b in BLOCOS:
        aulas = []
        for a in (x for x in AULAS if bloco_de(x['n']) == b['n']):
            d = {'n': a['n'], 'tema': md(a['tema']), 'tipo': a.get('tipo', 'aula'), 'objetivo': md(a['objetivo'])}
            if a.get('tipo'):
                d['questoes'] = [questao_yml(Q[i], sol_dir) for i in a['questoes']]
                usadas.update(a['questoes'])
            else:
                d['slides'] = f"aula{a['n']:02d}.pdf"
                d['conceitos'] = [md(c) for c in a['conceitos']]
                d['resolvida'] = questao_yml(Q[a['resolvida']], sol_dir)
                d['proposta'] = questao_yml(Q[a['proposta']], sol_dir)
                usadas.update([a['resolvida'], a['proposta']])
            aulas.append(d)
        saida.append({'bloco': b['n'], 'titulo': b['titulo'], 'resumo': b['resumo'], 'aulas': aulas})
    # banco: questões não usadas, pela avaliação de origem (A1 → bloco 1, A2 → bloco 2, A3/Final → bloco 3)
    for b in saida:
        resto = [q for q in Q.values() if q['id'] not in usadas and min(q['avaliacao'], 3) == b['bloco']]
        b['banco'] = [questao_yml(q, sol_dir) for q in sorted(resto, key=lambda q: (q['periodo'], q['pdf'], q['questao']))]
    with open(os.path.join(raiz, '_data', 'logica.yml'), 'w') as y:
        y.write('# Gerado por _tools/logica/gerar.py a partir de plano.py e questoes.json – não edite à mão\n')
        y.write(yml(saida))
    return len(usadas), sum(len(b['banco']) for b in saida)


if __name__ == '__main__':
    so = {int(x) for x in sys.argv[sys.argv.index('--aulas') + 1].split(',')} if '--aulas' in sys.argv else None
    usadas, banco = gerar(sys.argv[1], '--sem-slides' not in sys.argv, so)
    print(f'{usadas} questões nas aulas, {banco} no banco')
