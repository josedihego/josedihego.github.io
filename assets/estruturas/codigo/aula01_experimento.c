// Aula 1 – Experimento: tempo de um algoritmo linear e de um quadrático ao dobrar n
// Saída CSV: n, linear_ms, quadratico_ms (melhor de 5 execuções de cada)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

volatile long long ralo;                 // impede o compilador de descartar as contas

void linear(const int A[], int n) {
    long long s = 0;
    for (int r = 0; r < 200; r++)        // 200 passadas: tempo mensurável
        for (int i = 0; i < n; i++) s += A[i] ^ r;
    ralo = s;
}

void quadratico(const int A[], int n) {
    long c = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) c += (A[i] + A[j] == 0);
    ralo = c;
}

double melhor_de_5(void (*f)(const int *, int), const int A[], int n) {
    double melhor = 1e30;
    for (int r = 0; r < 5; r++) {        // o mínimo filtra interrupções do sistema
        double t0 = agora();
        f(A, n);
        double t = agora() - t0;
        if (t < melhor) melhor = t;
    }
    return melhor * 1000;
}

int main(void) {
    srand(2026);
    printf("n,linear_ms,quadratico_ms\n");
    for (int n = 2000; n <= 32000; n += 2000) {
        int *A = malloc(n * sizeof(int));
        for (int k = 0; k < n; k++) A[k] = rand() % 2001 - 1000;
        double tl = melhor_de_5(linear, A, n), tq = melhor_de_5(quadratico, A, n);
        printf("%d,%.4f,%.4f\n", n, tl, tq);
        free(A);
    }
    return 0;
}
