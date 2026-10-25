"""Tests the C files of /estruturas/ (c/):
  - every file compiles with gcc -Wall -Wextra -std=c17 -O2 without warnings;
  - lines have at most 88 characters (they are shown on the slides);
  - '// teste: entrada => trecho' lines run the program with that input (';' separates lines) and look for the
    text in the output; the experiments (aulaNN_experimento.c) only need to run and print a CSV header.
Uso: python3 _tools/estruturas/testar.py [arquivos .c]"""
import sys, os, re, glob, subprocess, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
MAX_COLUNAS = 88
arquivos = sys.argv[1:] or sorted(glob.glob(os.path.join(AQUI, 'c', '*.c')))
falhas = testes = 0
with tempfile.TemporaryDirectory() as tmp:
    for fonte in arquivos:
        nome = os.path.basename(fonte)
        linhas = open(fonte).read().split('\n')
        longas = [i + 1 for i, l in enumerate(linhas) if len(l) > MAX_COLUNAS]
        if longas:
            falhas += 1
            print(f'LINHAS LONGAS {nome}: {longas}')
        exe = os.path.join(tmp, nome[:-2])
        c = subprocess.run(['gcc', '-Wall', '-Wextra', '-std=c17', '-O2', fonte, '-o', exe, '-lm'], capture_output=True, text=True)
        if c.returncode or c.stderr.strip():
            falhas += 1
            print(f'COMPILAÇÃO {nome}:\n{c.stderr.strip()[:800]}')
            continue
        if nome.endswith('_experimento.c'):
            r = subprocess.run([exe], capture_output=True, text=True, timeout=600)
            testes += 1
            if r.returncode or not re.match(r'^[a-z_]+(,[a-z_0-9]+)+\n', r.stdout):
                falhas += 1
                print(f'EXPERIMENTO {nome}: código {r.returncode}, saída {r.stdout[:80]!r}')
            continue
        for entrada, esperado in (re.match(r'// teste: (.*?) => (.*)', l).groups() for l in linhas if l.startswith('// teste:')):
            testes += 1
            r = subprocess.run([exe], input=entrada.replace(';', '\n') + '\n', capture_output=True, text=True, timeout=20)
            if esperado.lower() not in r.stdout.lower():
                falhas += 1
                print(f'FALHOU {nome}: entrada [{entrada}] esperava "{esperado}" | obtido: {r.stdout.strip()[:200]}')
print(f'{len(arquivos)} arquivos, {testes} testes, falhas: {falhas}')
sys.exit(1 if falhas else 0)
