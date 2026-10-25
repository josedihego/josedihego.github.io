# Ferramentas do curso /estruturas/ (Estruturas de dados e seus algoritmos – Superior)

Pasta ignorada pelo Jekyll (começa com `_`), não é publicada.

| O quê | Fonte (edite aqui) | Gerado em |
|---|---|---|
| Blocos e as 36 aulas (texto dos slides, em LaTeX) | `plano.py`, `plano_b1.py` … `plano_b4.py` | `assets/estruturas/slides/aulaNN.pdf`, `_data/estruturas.yml` |
| Implementações e experimentos em C (64 arquivos) | `c/aulaNN_*.c` | `assets/estruturas/codigo/*.c` |
| Figuras do Cormen (3ª ed.) | recortadas do PDF local por `cormen_fig.py` | cache em `~/.cache/estruturas-cormen` (fora do repositório) |

Cada deck tem quatro partes: Teoria (Cormen, figuras e pseudocódigo em português), Prática em C, Experimento e
Conexões. Os slides usam xelatex, a fonte Inter e os pacotes tcolorbox, pgfplots, algpseudocode e fontawesome5.

## Experimentos

`c/aulaNN_experimento.c` imprime um CSV (tabelas separadas por linha em branco). Em `plano_bK.py`, cada gráfico diz
as séries e as curvas teóricas (`f` é uma expressão em `n`, que é o valor do eixo x):

- `ajustar=False`: a teoria dá a constante; o gerador compara direto.
- sem `ajustar`: o gerador ajusta `c·f(n)` por mínimos quadrados.
- `limite='inferior'` ou `'superior'`: o medido tem de ficar sempre acima (ou abaixo) de `f(n)`.

Se o medido se afastar da teoria mais que `tolerancia` (na metade superior de `n`), a geração **falha**: o slide
nunca mostra um experimento que não confirma o que diz.

## Comandos (na raiz do site)

```bash
# testa os programas: compilam sem avisos, linhas <= 88 colunas, casos '// teste:' e experimentos rodam
python3 _tools/estruturas/testar.py
python3 _tools/estruturas/encurta.py _tools/estruturas/c/arquivo.c   # move comentários longos

# gera slides (rodando todos os experimentos), código publicado e _data/estruturas.yml
python3 _tools/estruturas/gerar.py . ~/Documents/Books/algoritmos/Cormen_Introduction_to_Algorithms_3rd_edition.pdf
python3 _tools/estruturas/gerar.py . <pdf> --aulas 4,8        # só essas aulas
python3 _tools/estruturas/gerar.py . <pdf> --sem-slides       # só dados e código
```
