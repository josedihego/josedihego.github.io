// Base 2 – Experimento: percorrer uma matriz por linhas ou por colunas
// Saída CSV: n, linhas_ns, colunas_ns (tempo por elemento, matriz n x n de int)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

volatile long ralo;

int main(void) {
    printf("n,linhas_ns,colunas_ns\n");
    for (int n = 256; n <= 4096; n *= 2) {
        int **m = malloc(n * sizeof *m);
        m[0] = malloc((size_t)n * n * sizeof **m);
        for (int i = 1; i < n; i++) m[i] = m[0] + (size_t)i * n;
        for (long k = 0; k < (long)n * n; k++) m[0][k] = (int)k;
        double melhor[2] = {1e30, 1e30};
        for (int rep = 0; rep < 3; rep++) {
            long s = 0;
            double t0 = agora();
            // linha por linha: endereços vizinhos
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) s += m[i][j];
            double t1 = agora();
            // coluna por coluna: saltos de n inteiros
            for (int j = 0; j < n; j++)
                for (int i = 0; i < n; i++) s += m[i][j];
            double t2 = agora();
            ralo = s;
            if (t1 - t0 < melhor[0]) melhor[0] = t1 - t0;
            if (t2 - t1 < melhor[1]) melhor[1] = t2 - t1;
        }
        double elems = (double)n * n;
        printf("%d,%.4f,%.4f\n", n, melhor[0] / elems * 1e9, melhor[1] / elems * 1e9);
        free(m[0]); free(m);
    }
    return 0;
}
