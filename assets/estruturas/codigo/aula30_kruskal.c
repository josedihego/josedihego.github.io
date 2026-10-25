// Aula 30 – Conjuntos disjuntos e a árvore geradora mínima de Kruskal (Cormen, 21 e 23)
#include <stdio.h>
#include <stdlib.h>

/* Floresta de conjuntos disjuntos com união por posto e compressão de caminho. */
int pai[16], posto[16];

void cria(int x) { pai[x] = x; posto[x] = 0; }      // MAKE-SET

// FIND-SET com compressão de caminho
int acha(int x) {
    if (pai[x] != x) pai[x] = acha(pai[x]);
    return pai[x];
}

void une(int x, int y) {                            // UNION por posto
    x = acha(x); y = acha(y);
    if (posto[x] > posto[y]) pai[y] = x;
    else {
        pai[x] = y;
        if (posto[x] == posto[y]) posto[y]++;
    }
}

typedef struct { int u, v, w; } Aresta;

int compara(const void *a, const void *b) {
    return ((const Aresta *)a)->w - ((const Aresta *)b)->w;
}

int main(void) {
    int qualquer;
    if (scanf("%d", &qualquer) != 1) return 1;
    /* O grafo da Figura 23.1: vértices a..i. */
    Aresta E[] = {{0, 1, 4}, {0, 7, 8}, {1, 2, 8}, {1, 7, 11}, {2, 3, 7}, {2, 8, 2},
                  {2, 5, 4}, {3, 4, 9}, {3, 5, 14}, {4, 5, 10}, {5, 6, 2}, {6, 7, 1},
                  {6, 8, 6}, {7, 8, 7}};
    int m = sizeof E / sizeof E[0], total = 0;
    for (int x = 0; x < 9; x++) cria(x);
    qsort(E, m, sizeof(Aresta), compara);           // arestas em ordem de peso
    printf("arestas escolhidas:");
    for (int k = 0; k < m; k++)
        if (acha(E[k].u) != acha(E[k].v)) {         // não forma ciclo: entra na árvore
            une(E[k].u, E[k].v);
            total += E[k].w;
            printf(" %c-%c", 'a' + E[k].u, 'a' + E[k].v);
        }
    printf("\npeso total %d\n", total);
    return 0;
}
