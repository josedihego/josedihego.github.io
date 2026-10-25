// Aula 31 – Caminhos mínimos de origem única: Dijkstra com heap (Cormen, seção 24.3)
// teste: 0 => s:0 t:8 x:9 y:5 z:7
// teste: 0 => caminho até x: s y t x
#include <stdio.h>
#include <stdlib.h>

/* O grafo da Figura 24.6 (vértices s, t, x, y, z) com pesos não negativos. */
#define V 5
#define INF 1000000000
const char nome[V] = {'s', 't', 'x', 'y', 'z'};
int w[V][V];                                   // 0 = sem aresta (pesos positivos)
int d[V], pi[V], heap[V], pos[V], tam;

void troca(int i, int j) {
    int t = heap[i]; heap[i] = heap[j]; heap[j] = t;
    pos[heap[i]] = i; pos[heap[j]] = j;
}
void sobe(int i) {                             // DECREASE-KEY: o vértice sobe no heap
    while (i > 0 && d[heap[(i - 1) / 2]] > d[heap[i]]) {
        troca(i, (i - 1) / 2);
        i = (i - 1) / 2;
    }
}
int extrai_min(void) {                         // EXTRACT-MIN
    int u = heap[0];
    troca(0, --tam);
    for (int i = 0;;) {
        int e = 2 * i + 1, dd = e + 1, m = i;
        if (e < tam && d[heap[e]] < d[heap[m]]) m = e;
        if (dd < tam && d[heap[dd]] < d[heap[m]]) m = dd;
        if (m == i) break;
        troca(i, m);
        i = m;
    }
    return u;
}

int main(void) {
    int s;
    if (scanf("%d", &s) != 1 || s < 0 || s >= V) return 1;
    int arestas[][3] = {{0, 1, 10}, {0, 3, 5}, {1, 2, 1}, {1, 3, 2}, {2, 4, 4},
                        {3, 1, 3}, {3, 2, 9}, {3, 4, 2}, {4, 0, 7}, {4, 2, 6}};
    for (int k = 0; k < 10; k++) w[arestas[k][0]][arestas[k][1]] = arestas[k][2];
    for (int u = 0; u < V; u++) { d[u] = INF; pi[u] = -1; heap[u] = u; pos[u] = u; }
    d[s] = 0;                                  // INITIALIZE-SINGLE-SOURCE
    tam = V;
    sobe(pos[s]);
    while (tam > 0) {
        int u = extrai_min();                  // u entra em S: d[u] é definitivo
        for (int v = 0; v < V; v++)
            if (w[u][v] && d[u] + w[u][v] < d[v]) {   // RELAX(u, v, w)
                d[v] = d[u] + w[u][v];
                pi[v] = u;
                sobe(pos[v]);
            }
    }
    for (int u = 0; u < V; u++) printf("%c:%d ", nome[u], d[u]);
    printf("\ncaminho até x:");
    int caminho[V], k = 0;
    for (int u = 2; u != -1; u = pi[u]) caminho[k++] = u;
    while (k) printf(" %c", nome[caminho[--k]]);
    printf("\n");
    return 0;
}
