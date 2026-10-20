# Ferramentas do plano de aulas (/infobasica/)

Pasta ignorada pelo Jekyll (começa com `_`), não é publicada.

- `../../_data/infobasica.yml`: conteúdo das 36 aulas. Os campos `python` e `scratch` apontam para os arquivos abaixo.
- `../../assets/infobasica/python/aulaNN.ipynb`: exemplos em Python. São a fonte; edite direto (ou no Colab e baixe o `.ipynb`).
- `../../assets/infobasica/scratch/aulaNN.sb3`: projetos Scratch, gerados por `gerar_scratch.py`.

## Comandos (na raiz do site)

```bash
# executa todos os notebooks com entradas de teste
python3 _tools/infobasica/testar_python.py assets/infobasica/python

# regera os projetos Scratch (edite as funções aulaNN em gerar_scratch.py)
python3 _tools/infobasica/gerar_scratch.py .

# testa os projetos na máquina virtual oficial do Scratch (instala numa pasta temporária)
D=$(mktemp -d) && (cd $D && npm init -y >/dev/null && npm install scratch-vm scratch-storage --silent)
NODE_PATH=$D/node_modules node _tools/infobasica/testar_scratch.js assets/infobasica/scratch
```
