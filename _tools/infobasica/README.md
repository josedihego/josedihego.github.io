# Ferramentas do plano de aulas (/infobasica/)

Pasta ignorada pelo Jekyll (começa com `_`), não é publicada. Tudo tem três níveis: 1 Básico, 2 Intermediário, 3 Avançado.

| O quê | Fonte (edite aqui) | Gerado em | Gerador |
|---|---|---|---|
| Texto das 36 aulas, exemplos de Planilhas e exercícios | `_data/infobasica.yml` | página `/infobasica/` | Jekyll |
| Python (81 exemplos) | `python/aulaNN_nivelK.py` | `assets/infobasica/python/*.ipynb` (abre no Colab) | `gerar_notebooks.py` |
| Scratch (36 projetos) | funções `aulaNN_K` em `gerar_scratch.py` | `assets/infobasica/scratch/*.sb3` | `gerar_scratch.py` |
| Planilhas (78 arquivos) | funções `aN` em `gerar_planilhas.py` | `assets/infobasica/planilhas/*.xlsx` | `gerar_planilhas.py` |

Cada `python/aulaNN_nivelK.py` começa com duas linhas: o título do nível e `# teste:` com as entradas usadas pelo testador
(separadas por `;`, ou `1..100`).

## Comandos (na raiz do site)

```bash
# Python: testa os 81 exemplos (e aponta linhas sem comentário) e gera os notebooks
python3 _tools/infobasica/testar_python.py _tools/infobasica/python
python3 _tools/infobasica/gerar_notebooks.py .

# Scratch: gera os 36 projetos e testa na máquina virtual oficial do Scratch
python3 _tools/infobasica/gerar_scratch.py .
D=$(mktemp -d) && (cd $D && npm init -y >/dev/null && npm install scratch-vm scratch-storage --silent)
NODE_PATH=$D/node_modules node _tools/infobasica/testar_scratch.js assets/infobasica/scratch

# Planilhas: gera os 78 .xlsx e recalcula no LibreOffice para conferir
python3 _tools/infobasica/gerar_planilhas.py .
D=$(mktemp -d) && soffice --headless --calc --convert-to xlsx --outdir $D assets/infobasica/planilhas/*.xlsx
```

O LibreOffice 24.2 não tem `SEQUÊNCIA` nem `FILTRO` (o Google Planilhas tem): essas células aparecem como erro só no LibreOffice.
