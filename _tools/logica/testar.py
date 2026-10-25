"""Compiles every solution in _tools/logica/solucoes with -Wall -Wextra (warnings count as failures) and runs each
'// teste: entrada => trecho esperado' line: the program gets the input (';' separates lines) and its output must
contain the expected text (case-insensitive). Also lists code lines without a comment and rejects headers other
than stdio.h, stdlib.h and stdbool.h, and struct (not covered in the course).
Uso: python3 _tools/logica/testar.py [arquivo.c ...]"""
import sys, os, glob, subprocess, tempfile, re

pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'solucoes')
arquivos = sys.argv[1:] or sorted(glob.glob(os.path.join(pasta, '*.c')))
saida_dir = tempfile.mkdtemp()
falhas = testes = sem_comentario = 0

def precisa_comentario(linha):
    s = linha.strip()
    return bool(s) and '//' not in s and s not in ('{', '}', '};', '} else {') and not s.startswith('#include') and not re.match(r'case \d+: printf\("[^"]*"\); break;$', s)

for fonte in arquivos:
    nome = os.path.basename(fonte)[:-2]
    linhas = open(fonte).read().split('\n')
    casos = [re.match(r'// teste: (.*?) => (.*)', l).groups() for l in linhas if l.startswith('// teste:')]
    exe = os.path.join(saida_dir, nome)
    c = subprocess.run(['gcc', '-Wall', '-Wextra', '-std=c17', fonte, '-o', exe], capture_output=True, text=True)
    if c.returncode or c.stderr.strip():
        falhas += 1
        print(f'COMPILAÇÃO {nome}:\n{c.stderr.strip()[:800]}')
        continue
    if not casos:
        print(f'SEM TESTES {nome}')
    for entrada, esperado in casos:
        testes += 1
        try:
            r = subprocess.run([exe], input=entrada.replace(';', '\n') + '\n', capture_output=True, text=True, timeout=10)
            ok = esperado.strip().lower() in r.stdout.lower()
        except subprocess.TimeoutExpired:
            ok, r = False, None
        if not ok:
            falhas += 1
            obtido = (r.stdout.strip().replace('\n', ' | ')[-160:] if r else 'TEMPO ESGOTADO')
            print(f'FALHOU {nome}: entrada [{entrada}] esperava "{esperado}" | obtido: {obtido}')
    proibidos = [l.strip() for l in linhas if (l.startswith('#include') and not re.match(r'#include <(stdio|stdlib|stdbool)\.h>', l))
                 or re.search(r'\bstruct\b', l.split('//')[0])]
    if proibidos:                                             # a disciplina só usa stdio, stdlib e stdbool, sem struct
        falhas += 1
        print(f'FORA DO CONTEÚDO {nome}: {proibidos}')
    sem_comentario += sum(precisa_comentario(l) for l in linhas if not l.startswith('//'))
print(f'{len(arquivos)} soluções, {testes} testes, falhas: {falhas}, linhas sem comentário: {sem_comentario}')
sys.exit(1 if falhas else 0)
