// Aula 29 – Busca em profundidade e ordenação topológica (Cormen, seções 22.3 e 22.4)
// teste: 9 => meias cuecas calças sapatos relógio camisa cinto gravata paletó
// teste: 9 => cuecas 11/16
// teste: 3 => meias cuecas calças
#include <stdio.h>
#include <stdlib.h>

/* O grafo da Figura 22.7: o que vestir antes de quê. Uma aresta u -> v diz
   "u antes de v". A DFS numera o fim de cada vértice; em ordem decrescente de
   término, os vértices formam uma ordenação topológica. */
#define V 9
/* Numeração escolhida para a DFS (vértices em ordem, vizinhos em ordem) repetir
   os tempos d/f da Figura 22.7: camisa 1/8, gravata 2/5, paletó 3/4, ... */
const char *nome[V] = {"camisa", "gravata", "paletó", "cinto", "relógio",
                       "cuecas", "calças", "sapatos", "meias"};
int adj[V][V];                                 // matriz de adjacência (grafo pequeno)
int cor[V], d[V], f[V], tempo;                 // 0 branco, 1 cinza, 2 preto
int ordem[V], k_ordem = V;

void visita(int u) {                           // DFS-VISIT
    cor[u] = 1;
    d[u] = ++tempo;                            // descoberta
    for (int v = 0; v < V; v++)
        if (adj[u][v] && cor[v] == 0) visita(v);
    cor[u] = 2;
    f[u] = ++tempo;                            // término
    ordem[--k_ordem] = u;                      // insere na frente da lista
}

int main(void) {
    int arestas[][2] = {{0, 1}, {0, 3}, {1, 2}, {3, 2}, {5, 6}, {5, 7},
                        {6, 3}, {6, 7}, {8, 7}};       // u -> v: vista u antes de v
    for (int k = 0; k < 9; k++) adj[arestas[k][0]][arestas[k][1]] = 1;
    int mostrar;
    if (scanf("%d", &mostrar) != 1 || mostrar < 1 || mostrar > V) return 1;
    for (int u = 0; u < V; u++)                    // DFS: inicia em todo vértice branco
        if (cor[u] == 0) visita(u);
    for (int i = 0; i < mostrar; i++)
        printf("%s%s", nome[ordem[i]], i < mostrar - 1 ? " " : "\n");
    for (int u = 0; u < V; u++) printf("%s %d/%d\n", nome[u], d[u], f[u]);
    return 0;
}
