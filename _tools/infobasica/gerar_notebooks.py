"""Builds one Colab notebook per class and level from _tools/infobasica/python/aulaNN_nivelK.py.
Uso: python3 _tools/infobasica/gerar_notebooks.py <raiz do site>"""
import sys, os, json, glob, yaml

NIVEIS = {1: 'Básico', 2: 'Intermediário', 3: 'Avançado'}
raiz = sys.argv[1]
temas = {a['n']: a for u in yaml.safe_load(open(os.path.join(raiz, '_data/infobasica.yml'))) for a in u['aulas']}
destino = os.path.join(raiz, 'assets/infobasica/python')
os.makedirs(destino, exist_ok=True)
for antigo in glob.glob(os.path.join(destino, '*.ipynb')):
    os.remove(antigo)

def celula(tipo, texto):
    c = {'cell_type': tipo, 'metadata': {}, 'source': texto.splitlines(keepends=True)}
    if tipo == 'code':
        c.update(execution_count=None, outputs=[])
    return c

for fonte in sorted(glob.glob(os.path.join(raiz, '_tools/infobasica/python/*.py'))):
    linhas = open(fonte).read().split('\n')
    titulo = linhas[0].split(': ', 1)[1]                 # "# Aula 6 – Nível 2: Preço com desconto"
    codigo = '\n'.join(linhas[2:]).rstrip('\n')          # linha 2 em diante (a linha 1 é o teste)
    nome = os.path.basename(fonte)[:-3]
    n, k = int(nome[4:6]), int(nome[-1])
    aula = temas[n]
    cabecalho = (f"# Aula {n} – {aula['tema']}\n\n"
                 f"## Nível {k} ({NIVEIS[k]}): {titulo}\n\n"
                 f"**Objetivo da aula:** {aula['objetivo']}\n\n"
                 "Leia os comentários (depois do `#`) e execute a célula abaixo clicando em ▶. "
                 "Depois altere os valores e execute de novo.")
    notebook = {'nbformat': 4, 'nbformat_minor': 0,
                'metadata': {'colab': {'provenance': []}, 'language_info': {'name': 'python'},
                             'kernelspec': {'name': 'python3', 'display_name': 'Python 3'}},
                'cells': [celula('markdown', cabecalho), celula('code', codigo)]}
    json.dump(notebook, open(os.path.join(destino, nome + '.ipynb'), 'w'), ensure_ascii=False, indent=1)
print(len(glob.glob(os.path.join(destino, '*.ipynb'))), 'notebooks')
