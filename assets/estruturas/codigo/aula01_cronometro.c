// Aula 1 – Como medir um algoritmo: tempo de relógio e contagem de operações
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Tempo de relógio em segundos (relógio monotônico: não volta com ajustes de hora). */
double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

long long soma(const int A[], int n) {          // uma passada: cresce como n
    long long s = 0;
    for (int i = 0; i < n; i++) s += A[i];
    return s;
}

long pares_zero(const int A[], int n) {          // todos os pares i < j: cresce como n²
    long cont = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (A[i] + A[j] == 0) cont++;
    return cont;
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    double t0 = agora();
    printf("soma = %lld\n", soma(A, n));
    printf("pares com soma zero = %ld\n", pares_zero(A, n));
    printf("tempo: %.6f s\n", agora() - t0);
    free(A);
    return 0;
}
