// Aula 28 – Experimento: a BFS é linear em V + E; distâncias num grafo aleatório
// Tabela 1 (n, operacoes): vértices retirados da fila + entradas de adjacência vistas
// Tabela 2 (n, distancia_media): distância média da origem, grau médio 10
#include <stdio.h>
#include <stdlib.h>

unsigned long long estado = 0x5DEECE66DULL;
unsigned sorteia(unsigned limite) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)((estado >> 11) % limite);
}

int *ini_adj, *adj;                            // listas de adjacência compactas (CSR)

void monta(int n, int m, int *origem, int *destino) {
    int *grau = calloc(n + 1, sizeof(int));
    for (int k = 0; k < m; k++) { grau[origem[k]]++; grau[destino[k]]++; }
    ini_adj = malloc((n + 1) * sizeof(int));
    ini_adj[0] = 0;
    for (int u = 0; u < n; u++) ini_adj[u + 1] = ini_adj[u] + grau[u];
    adj = malloc(2 * m * sizeof(int));
    for (int u = 0; u < n; u++) grau[u] = ini_adj[u];
    for (int k = 0; k < m; k++) {
        adj[grau[origem[k]]++] = destino[k];
        adj[grau[destino[k]]++] = origem[k];
    }
    free(grau);
}

long bfs(int n, int s, int *d) {               // devolve o número de operações
    int *fila = malloc(n * sizeof(int)), ini = 0, fim = 0;
    long ops = 0;
    for (int u = 0; u < n; u++) d[u] = -1;
    d[s] = 0;
    fila[fim++] = s;
    while (ini < fim) {
        int u = fila[ini++];
        ops++;                                 // cada vértice sai da fila uma vez
        for (int k = ini_adj[u]; k < ini_adj[u + 1]; k++) {
            // cada entrada de adjacência é vista uma vez
            ops++;
            if (d[adj[k]] < 0) { d[adj[k]] = d[u] + 1; fila[fim++] = adj[k]; }
        }
    }
    free(fila);
    return ops;
}

int main(void) {
    printf("n,operacoes\n");
    int N = 1 << 21;
    int *origem = malloc(5L * N * sizeof(int)), *destino = malloc(5L * N * sizeof(int));
    int *d = malloc(N * sizeof(int));
    for (int n = 1 << 12; n <= N; n *= 2) {
        int m = 4 * n;                         // E = 4V: grau médio 8
        for (int k = 0; k < m; k++) {
            // n-1 arestas formam um caminho:
            origem[k] = k < n - 1 ? k : (int)sorteia(n);
            destino[k] = k < n - 1 ? k + 1 : (int)sorteia(n);   // o grafo é conexo
        }
        monta(n, m, origem, destino);
        printf("%d,%ld\n", n, bfs(n, 0, d));
        free(ini_adj); free(adj);
    }
    printf("\nn,distancia_media\n");
    for (int n = 1 << 10; n <= N; n *= 2) {
        // grau médio 10, sem o caminho artificial
        int m = 5 * n;
        for (int k = 0; k < m; k++) { origem[k] = sorteia(n); destino[k] = sorteia(n); }
        monta(n, m, origem, destino);
        bfs(n, 0, d);
        double soma = 0;
        int alcancados = 0;
        for (int u = 0; u < n; u++) if (d[u] > 0) { soma += d[u]; alcancados++; }
        printf("%d,%.4f\n", n, soma / alcancados);
        free(ini_adj); free(adj);
    }
    free(origem); free(destino); free(d);
    return 0;
}
