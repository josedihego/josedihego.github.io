# Ferramentas do curso /logica/ (Lógica de Programação – Superior)

Pasta ignorada pelo Jekyll (começa com `_`), não é publicada.

| O quê | Fonte (edite aqui) | Gerado em |
|---|---|---|
| Blocos, temas, questões de cada aula e conteúdo dos slides | `plano.py` | `_data/logica.yml`, `assets/logica/slides/aulaNN.pdf` |
| Índice das 91 questões das provas (id, PDF; o texto serve só de referência, não é publicado) | `questoes.json` | `_data/logica.yml` |
| Soluções comentadas (72) | `solucoes/*.c` | `assets/logica/solucoes/*.c` e `_data/logica.yml` |
| PDFs das provas | não ficam aqui: cada questão aponta para o PDF no repositório [programacaoC](https://github.com/josedihego/programacaoC/tree/main/INF027_listas_provas_PDF) | links em `_data/logica.yml` e nos slides |

Cada solução começa com `// A1-2014.2 – Questão I: título` e linhas `// teste: entrada => trecho esperado da saída`
(na entrada, `;` separa linhas). O nome do arquivo vem do id da questão: `A1-2015.2-QI-B` → `a1_2015_2_b_q1.c`.

Nos slides, o teste de mesa é um trecho de C executado pelo gerador: cada linha `MESA("...", ...)` imprime uma linha
da tabela e não aparece no slide. As questões não usadas nas aulas vão para o banco do bloco da avaliação de origem.

## Comandos (na raiz do site)

```bash
# testa as soluções (compila com -Wall -Wextra, roda os casos e aponta linhas sem comentário)
python3 _tools/logica/testar.py _tools/logica/solucoes/*.c

# gera PDFs, soluções, slides (xelatex + tema metropolis) e _data/logica.yml
python3 _tools/logica/gerar.py .
python3 _tools/logica/gerar.py . --sem-slides     # só dados e soluções
python3 _tools/logica/gerar.py . --aulas 3,4      # só os slides dessas aulas
```
