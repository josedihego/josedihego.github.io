// Aula 31 – Experimento: Dijkstra com vetor contra Dijkstra com heap, e Bellman-Ford
// Saída CSV: n, vetor, heap, bellman_ford (operações; grafo esparso com E = 8V)
#include <stdio.h>
#include <stdlib.h>

unsigned long long estado = 0x9FB21C651E98DF25ULL;
unsigned sorteia(unsigned limite) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)((estado >> 11) % limite);
}

int *ini, *dest, *peso, *d, *heap, *pos, tam;
long ops;

void troca(int i, int j) {
    int t = heap[i]; heap[i] = heap[j]; heap[j] = t;
    pos[heap[i]] = i; pos[heap[j]] = j;
}
void sobe(int i) {
    while (i > 0 && (ops++, d[heap[(i - 1) / 2]] > d[heap[i]])) {
        troca(i, (i - 1) / 2);
        i = (i - 1) / 2;
    }
}
int extrai_min(void) {
    int u = heap[0];
    troca(0, --tam);
    for (int i = 0;;) {
        int e = 2 * i + 1, f = e + 1, m = i;
        if (e < tam && (ops++, d[heap[e]] < d[heap[m]])) m = e;
        if (f < tam && (ops++, d[heap[f]] < d[heap[m]])) m = f;
        if (m == i) break;
        troca(i, m); i = m;
    }
    return u;
}

void dijkstra_heap(int n) {
    for (int u = 0; u < n; u++) { d[u] = 1 << 30; heap[u] = u; pos[u] = u; }
    d[0] = 0; tam = n;
    while (tam) {
        int u = extrai_min();
        for (int k = ini[u]; k < ini[u + 1]; k++) {
            ops++;
            if (d[u] + peso[k] < d[dest[k]]) {     // RELAX + DECREASE-KEY
                d[dest[k]] = d[u] + peso[k];
                sobe(pos[dest[k]]);
            }
        }
    }
}

void dijkstra_vetor(int n) {                   // EXTRACT-MIN varre o vetor: O(V) cada
    char *feito = calloc(n, 1);
    for (int u = 0; u < n; u++) d[u] = 1 << 30;
    d[0] = 0;
    for (int it = 0; it < n; it++) {
        int u = -1;
        for (int v = 0; v < n; v++) {
            ops++;
            if (!feito[v] && (u < 0 || d[v] < d[u])) u = v;
        }
        feito[u] = 1;
        for (int k = ini[u]; k < ini[u + 1]; k++) {
            ops++;
            if (d[u] + peso[k] < d[dest[k]]) d[dest[k]] = d[u] + peso[k];
        }
    }
    free(feito);
}

// V-1 passadas relaxando todas as arestas
void bellman_ford(int n) {
    for (int u = 0; u < n; u++) d[u] = 1 << 30;
    d[0] = 0;
    for (int it = 1; it < n; it++)
        for (int u = 0; u < n; u++)
            for (int k = ini[u]; k < ini[u + 1]; k++) {
                ops++;
                if (d[u] < (1 << 30) && d[u] + peso[k] < d[dest[k]])
                    d[dest[k]] = d[u] + peso[k];
            }
}

int main(void) {
    printf("n,vetor,heap,bellman_ford\n");
    for (int n = 250; n <= 4000; n += 250) {
        int m = 8 * n;
        ini = calloc(n + 1, sizeof(int));
        dest = malloc(m * sizeof(int));
        peso = malloc(m * sizeof(int));
        d = malloc(n * sizeof(int));
        heap = malloc(n * sizeof(int));
        pos = malloc(n * sizeof(int));
        // 8 arestas saindo de cada vértice
        for (int u = 0; u < n; u++) ini[u + 1] = ini[u] + 8;
        for (int k = 0; k < m; k++) {
            // inclui um ciclo: conexo
            dest[k] = (k % 8 == 0) ? (k / 8 + 1) % n : (int)sorteia(n);
            peso[k] = 1 + sorteia(100);
        }
        long r[3];
        ops = 0; dijkstra_vetor(n); r[0] = ops;
        ops = 0; dijkstra_heap(n); r[1] = ops;
        ops = 0; bellman_ford(n); r[2] = ops;
        printf("%d,%ld,%ld,%ld\n", n, r[0], r[1], r[2]);
        free(ini); free(dest); free(peso); free(d); free(heap); free(pos);
    }
    return 0;
}
