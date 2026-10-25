// Aula 29 – Experimento: DFS e ordenação topológica em grafos acíclicos grandes
// Saída CSV: n, operacoes, tempo_ms (DAG com E = 8V; operações = V + E)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned long long estado = 0xA0761D6478BD642FULL;
unsigned sorteia(unsigned limite) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)((estado >> 11) % limite);
}

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

int *ini_adj, *adj, *cor, *pilha, *pos_pilha, *ordem;
long ops;

/* DFS iterativa (a recursiva estouraria a pilha com milhões de vértices). */
void dfs(int n) {
    int k = n;
    for (int s = 0; s < n; s++) {
        if (cor[s]) continue;
        int topo = 0;
        pilha[topo] = s; pos_pilha[topo++] = ini_adj[s]; cor[s] = 1; ops++;
        while (topo) {
            int u = pilha[topo - 1];
            if (pos_pilha[topo - 1] < ini_adj[u + 1]) {
                int v = adj[pos_pilha[topo - 1]++];
                ops++;                         // aresta examinada
                if (cor[v] == 1) { fprintf(stderr, "ciclo!\n"); exit(1); }
                if (cor[v] == 0) {             // descobre v: empilha
                    cor[v] = 1;
                    ops++;
                    pilha[topo] = v;
                    pos_pilha[topo++] = ini_adj[v];
                }
            } else {
                cor[u] = 2;
                ordem[--k] = u;                // término: entra na frente da ordem
                topo--;
            }
        }
    }
}

int main(void) {
    printf("n,operacoes,tempo_ms\n");
    int N = 1 << 21;
    int *de = malloc(8L * N * sizeof(int)), *para = malloc(8L * N * sizeof(int));
    ini_adj = malloc((N + 1) * sizeof(int)); adj = malloc(8L * N * sizeof(int));
    cor = malloc(N * sizeof(int)); pilha = malloc(N * sizeof(int));
    pos_pilha = malloc(N * sizeof(int)); ordem = malloc(N * sizeof(int));
    int *rotulo = malloc(N * sizeof(int)), *posicao = malloc(N * sizeof(int));
    for (int n = 1 << 14; n <= N; n *= 2) {
        int m = 8 * n;
        for (int u = 0; u < n; u++) rotulo[u] = u;          // ordem escondida: arestas
        for (int u = n - 1; u > 0; u--) {                   // só vão de rótulo menor
            // para maior, então não há ciclo
            int r = sorteia(u + 1), t = rotulo[u];
            rotulo[u] = rotulo[r]; rotulo[r] = t;
        }
        for (int e = 0; e < m; e++) {
            int a = sorteia(n), b = sorteia(n);
            if (a == b) b = (b + 1) % n;
            if (a > b) { int t = a; a = b; b = t; }
            de[e] = rotulo[a]; para[e] = rotulo[b];
        }
        for (int u = 0; u <= n; u++) ini_adj[u] = 0;
        for (int e = 0; e < m; e++) ini_adj[de[e] + 1]++;
        for (int u = 0; u < n; u++) ini_adj[u + 1] += ini_adj[u];
        for (int u = 0; u < n; u++) pos_pilha[u] = ini_adj[u];
        for (int e = 0; e < m; e++) adj[pos_pilha[de[e]]++] = para[e];
        for (int u = 0; u < n; u++) cor[u] = 0;
        ops = 0;
        double t0 = agora();
        dfs(n);
        double t = agora() - t0;
        // confere a ordem topológica
        for (int i = 0; i < n; i++) posicao[ordem[i]] = i;
        for (int e = 0; e < m; e++)
            if (posicao[de[e]] > posicao[para[e]]) {
                fprintf(stderr, "ordem errada!\n");
                return 1;
            }
        printf("%d,%ld,%.3f\n", n, ops, t * 1000);
    }
    return 0;
}
