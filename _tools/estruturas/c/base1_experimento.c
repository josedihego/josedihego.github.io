// Base 1 – Experimento: quanto custa, em bytes e em tempo, um malloc pequeno?
// Saída CSV: n, bytes_por_bloco, ns_por_malloc (n blocos de 16 bytes)
#define _GNU_SOURCE                   // mallinfo2 e clock_gettime
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

int main(void) {
    printf("n,bytes_por_bloco,ns_por_malloc\n");
    void **p = malloc((1 << 22) * sizeof(void *));
    for (int n = 1 << 12; n <= 1 << 22; n *= 2) {
        size_t antes = mallinfo2().uordblks;      // bytes do heap em uso
        double t0 = agora();
        for (int i = 0; i < n; i++) p[i] = malloc(16);
        double t1 = agora();
        size_t depois = mallinfo2().uordblks;
        for (int i = 0; i < n; i++) free(p[i]);
        printf("%d,%.3f,%.3f\n", n, (double)(depois - antes) / n, (t1 - t0) / n * 1e9);
    }
    free(p);
    return 0;
}
