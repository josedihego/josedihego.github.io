// Aula 32 – Experimento: Floyd-Warshall (V³) contra V execuções de Dijkstra
// Saída CSV: n, floyd_ms, dijkstra_ms (todos os pares; grafo esparso com E = 8V)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned long long estado = 0x6A09E667F3BCC908ULL;
unsigned sorteia(unsigned limite) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)((estado >> 11) % limite);
}

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

int *ini, *dest, *peso, *d, *heap, *pos, tam;

void troca(int i, int j) {
    int t = heap[i]; heap[i] = heap[j]; heap[j] = t;
    pos[heap[i]] = i; pos[heap[j]] = j;
}

void dijkstra(int n, int s) {                   // heap binário: O((V + E) lg V)
    for (int u = 0; u < n; u++) { d[u] = 1 << 29; heap[u] = u; pos[u] = u; }
    d[s] = 0;
    troca(0, s);
    tam = n;
    while (tam) {
        int u = heap[0];
        troca(0, --tam);
        for (int i = 0;;) {
            int e = 2 * i + 1, f = e + 1, m = i;
            if (e < tam && d[heap[e]] < d[heap[m]]) m = e;
            if (f < tam && d[heap[f]] < d[heap[m]]) m = f;
            if (m == i) break;
            troca(i, m);
            i = m;
        }
        for (int k = ini[u]; k < ini[u + 1]; k++)
            if (d[u] + peso[k] < d[dest[k]]) {
                d[dest[k]] = d[u] + peso[k];
                for (int i = pos[dest[k]]; i > 0 && d[heap[(i - 1) / 2]] > d[heap[i]];
                     i = (i - 1) / 2)
                    troca(i, (i - 1) / 2);
            }
    }
}

int main(void) {
    printf("n,floyd_ms,dijkstra_ms\n");
    for (int n = 200; n <= 1600; n += 200) {
        int m = 8 * n;
        ini = malloc((n + 1) * sizeof(int));
        dest = malloc(m * sizeof(int));
        peso = malloc(m * sizeof(int));
        d = malloc(n * sizeof(int));
        heap = malloc(n * sizeof(int));
        pos = malloc(n * sizeof(int));
        int *D = malloc((long)n * n * sizeof(int));
        for (int u = 0; u <= n; u++) ini[u] = 8 * u;
        for (int k = 0; k < m; k++) {
            dest[k] = k % 8 == 0 ? (k / 8 + 1) % n : (int)sorteia(n);
            peso[k] = 1 + sorteia(100);
        }
        double melhor_f = 1e30, melhor_d = 1e30;
        long soma1 = 0, soma2 = 0;
        for (int rep = 0; rep < 2; rep++) {     // melhor de 2: o relógio tem ruído
            for (long k = 0; k < (long)n * n; k++) D[k] = 1 << 29;
            for (int k = 0; k < m; k++) {
                long pos_uv = (long)(k / 8) * n + dest[k];
                if (peso[k] < D[pos_uv]) D[pos_uv] = peso[k];
            }
            for (int u = 0; u < n; u++) D[(long)u * n + u] = 0;
            double t0 = agora();
            for (int k = 0; k < n; k++)
                for (int i = 0; i < n; i++) {
                    int dik = D[(long)i * n + k];
                    for (int j = 0; j < n; j++)
                        if (dik + D[(long)k * n + j] < D[(long)i * n + j])
                            D[(long)i * n + j] = dik + D[(long)k * n + j];
                }
            double t1 = agora();
            soma1 = soma2 = 0;                  // confere: as duas respostas coincidem
            for (long k = 0; k < (long)n * n; k++) soma1 += D[k];
            double t2 = agora();
            for (int s = 0; s < n; s++) {
                dijkstra(n, s);
                for (int u = 0; u < n; u++) soma2 += d[u];
            }
            double t3 = agora();
            if (t1 - t0 < melhor_f) melhor_f = t1 - t0;
            if (t3 - t2 < melhor_d) melhor_d = t3 - t2;
        }
        if (soma1 != soma2) { fprintf(stderr, "respostas diferentes!\n"); return 1; }
        printf("%d,%.2f,%.2f\n", n, melhor_f * 1000, melhor_d * 1000);
        free(ini); free(dest); free(peso); free(d); free(heap); free(pos); free(D);
    }
    return 0;
}
