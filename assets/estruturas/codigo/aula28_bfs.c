// Aula 28 – Listas de adjacência e busca em largura (Cormen, seções 22.1 e 22.2)
#include <stdio.h>
#include <stdlib.h>

/* Entrada: V E, depois E arestas não direcionadas como pares de letras (a, b, ...),
   depois o índice da origem s (0 = primeira letra). Vértices: 'a' + i, ou as letras
   r s t u v w x y da Figura 22.3 quando V = 8. */
typedef struct Aresta { int v; struct Aresta *prox; } Aresta;

int V;
Aresta **adj;                                  // adj[u]: lista de vizinhos de u

void liga(int u, int v) {                      // insere na cabeça: O(1)
    Aresta *a = malloc(sizeof(Aresta));
    a->v = v;
    a->prox = adj[u];
    adj[u] = a;
}

int letra_para_vertice(char c, const char *nomes) {
    for (int i = 0; i < V; i++) if (nomes[i] == c) return i;
    return -1;
}

int main(void) {
    int E, s;
    if (scanf("%d %d", &V, &E) != 2) return 1;
    const char *nomes = V == 8 ? "rstuvwxy" : "abcdefghijklmnopqrstuvwxyz";
    adj = calloc(V, sizeof(Aresta *));
    for (int k = 0; k < E; k++) {
        char a[2], b[2];
        if (scanf("%1s %1s", a, b) != 2) return 1;
        int u = letra_para_vertice(a[0], nomes), v = letra_para_vertice(b[0], nomes);
        liga(u, v);
        liga(v, u);                            // não direcionado: duas entradas
    }
    if (scanf("%d", &s) != 1) return 1;
    int *d = malloc(V * sizeof(int)), *fila = malloc(V * sizeof(int));
    for (int u = 0; u < V; u++) d[u] = -1;     // -1 = infinito (branco, não descoberto)
    int ini = 0, fim = 0;
    d[s] = 0;
    fila[fim++] = s;
    while (ini < fim) {                        // BFS: fila FIFO
        int u = fila[ini++];
        for (Aresta *a = adj[u]; a; a = a->prox)
            if (d[a->v] < 0) {                 // descobre v: distância de u mais 1
                d[a->v] = d[u] + 1;
                fila[fim++] = a->v;
            }
    }
    for (int u = 0; u < V; u++) {
        if (d[u] < 0) printf("%c:inf ", nomes[u]);
        else printf("%c:%d ", nomes[u], d[u]);
    }
    printf("\n");
    return 0;
}
