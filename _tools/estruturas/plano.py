"""Plan of /estruturas/ (Estruturas de dados e seus algoritmos – Superior): 4 blocks, 36 classes, 4 of them project
presentations. Texts are LaTeX (they go straight to the slides). Each content class has:
  teoria       frames from Cormen et al. (3rd ed.): text, figure (cropped from the book) and/or pseudocode in Portuguese
  pratica      C files in c/ shown on the slides and published on the page
  experimento  c/aulaNN_experimento.c prints a CSV; the theory curves are checked against it (tolerância)
  conexoes     the concept in other areas of computing"""
from plano_b1 import AULAS_B1
from plano_b2 import AULAS_B2
from plano_b3 import AULAS_B3
from plano_b4 import AULAS_B4

BLOCOS = [
    {'n': 1, 'titulo': 'Fundamentos e ordenação', 'resumo': 'Análise de algoritmos, notação assintótica, recorrências, dividir e conquistar e heapsort. Termina com o Projeto 1.'},
    {'n': 2, 'titulo': 'Ordenação avançada e estruturas lineares', 'resumo': 'Filas de prioridade, quicksort, limite inferior, ordenação linear, seleção, pilhas, filas e listas. Termina com o Projeto 2.'},
    {'n': 3, 'titulo': 'Dicionários: hash e árvores', 'resumo': 'Tabelas hash, árvores binárias de busca, AVL, rubro-negras e árvores B. Termina com o Projeto 3.'},
    {'n': 4, 'titulo': 'Grafos e técnicas de projeto', 'resumo': 'Buscas em grafos, árvores geradoras, caminhos mínimos, programação dinâmica, algoritmos gulosos e casamento de cadeias. Termina com o Projeto 4.'},
]

AULAS = AULAS_B1 + AULAS_B2 + AULAS_B3 + AULAS_B4
