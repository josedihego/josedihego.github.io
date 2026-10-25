// Aula 14 – Experimento: radix sort (linear) contra qsort da biblioteca (n lg n)
// Saída CSV: n, radix_ns, qsort_ns (tempo por elemento, melhor de 3)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

/* Radix LSD em base 256: 4 passadas de contagem sobre os bytes da chave. */
void radix(unsigned A[], unsigned B[], int n) {
    for (int byte = 0; byte < 4; byte++) {
        int C[256] = {0}, sh = 8 * byte;
        for (int j = 0; j < n; j++) C[(A[j] >> sh) & 255]++;
        for (int v = 1; v < 256; v++) C[v] += C[v - 1];
        for (int j = n - 1; j >= 0; j--) B[--C[(A[j] >> sh) & 255]] = A[j];
        memcpy(A, B, n * sizeof(unsigned));
    }
}

int cmp(const void *a, const void *b) {
    unsigned x = *(const unsigned *)a, y = *(const unsigned *)b;
    return (x > y) - (x < y);
}

int main(void) {
    srand(14);
    int N = 1 << 22;
    unsigned *orig = malloc(N * sizeof(unsigned)), *A = malloc(N * sizeof(unsigned));
    unsigned *B = malloc(N * sizeof(unsigned));
    for (int k = 0; k < N; k++) orig[k] = ((unsigned)rand() << 16) ^ (unsigned)rand();
    printf("n,radix_ns,qsort_ns\n");
    for (int n = 1 << 16; n <= N; n *= 2) {
        double tr = 1e30, tq = 1e30;
        for (int rep = 0; rep < 3; rep++) {
            memcpy(A, orig, n * sizeof(unsigned));
            double t0 = agora();
            radix(A, B, n);
            double t1 = agora();
            memcpy(A, orig, n * sizeof(unsigned));
            double t2 = agora();
            qsort(A, n, sizeof(unsigned), cmp);
            double t3 = agora();
            if (t1 - t0 < tr) tr = t1 - t0;
            if (t3 - t2 < tq) tq = t3 - t2;
        }
        printf("%d,%.3f,%.3f\n", n, tr / n * 1e9, tq / n * 1e9);
    }
    free(orig); free(A); free(B);
    return 0;
}
