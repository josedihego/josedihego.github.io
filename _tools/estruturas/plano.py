"""Plan of /estruturas/ (Estruturas de dados e seus algoritmos – Superior): 4 blocks with 36 classes (4 of them project
presentations), a C annex before block 1 (modules B1–B5) and an optional complementary block (advanced sorting, modules C1–C5). Texts are LaTeX (they go straight
to the slides). Each content class has:
  teoria       frames from Cormen et al. (3rd ed.): text, figure (cropped from the book) and/or pseudocode in Portuguese
  pratica      C files in c/ shown on the slides and published on the page
  experimento  c/<id>_experimento.c prints a CSV; the theory curves are checked against it (tolerância)
  conexoes     the concept in other areas of computing"""
from plano_b1 import AULAS_B1
from plano_b2 import AULAS_B2
from plano_b3 import AULAS_B3
from plano_b4 import AULAS_B4
from plano_compl import AULAS_COMPL
from plano_base import AULAS_BASE

BLOCOS = [
    {'n': 0, 'rotulo': 'Anexo', 'tag': 'Anexo', 'titulo': 'Base Prática em C',
     'resumo': 'Cinco módulos de apoio, antes do bloco 1, com o C que as estruturas de dados exigem além do básico: memória e alocação dinâmica, ponteiros (simples, duplos, para funções e para structs), structs, funções genéricas e arquivos.'},
    {'n': 1, 'titulo': 'Fundamentos, ordenação e custo', 'resumo': 'Análise de algoritmos, ordenação por inserção, merge sort, notação assintótica, recorrências, dividir e conquistar e heaps. Termina com o Projeto 1.'},
    {'n': 2, 'titulo': 'Dicionários e estruturas lineares', 'resumo': 'Dicionários, pilhas, filas, vetores dinâmicos e listas: simplesmente e duplamente ligadas, circulares, com sentinela e em vetores; filas de prioridade. Termina com o Projeto 2.'},
    {'n': 3, 'titulo': 'Tabelas hash e árvores', 'resumo': 'Tabelas hash (encadeamento, funções hash, endereçamento aberto), árvores binárias de busca, AVL, rubro-negras e árvores B. Termina com o Projeto 3.'},
    {'n': 4, 'titulo': 'Grafos', 'resumo': 'Buscas em largura e em profundidade, ordenação topológica, árvores geradoras mínimas e caminhos mínimos; programação dinâmica, algoritmos gulosos e casamento de cadeias. Termina com o Projeto 4.'},
    {'n': 5, 'rotulo': 'Bloco complementar', 'opcional': True, 'tag': 'Opcional', 'titulo': 'Ordenação avançada (opcional)',
     'resumo': 'Cinco módulos opcionais, fora das 36 aulas, para quem quer ir além do bloco 1: quicksort, quicksort aleatorizado, limite inferior, ordenação em tempo linear e seleção.'},
]

AULAS = AULAS_BASE + AULAS_B1 + AULAS_B2 + AULAS_B3 + AULAS_B4 + AULAS_COMPL
