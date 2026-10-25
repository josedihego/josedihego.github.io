// Complemento 3 – Experimento: quão perto do limite lg n! chega o merge sort?
// Tabela 1 (n, pior_merge, limite): pior caso sobre TODAS as n! permutações, n = 2..10
// Tabela 2 (n, media_merge): média em vetores aleatórios, n até 2^20
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long comp;
int *aux;

void merge_sort(int A[], int p, int r) {
    if (p >= r) return;
    int q = (p + r) / 2;
    merge_sort(A, p, q);
    merge_sort(A, q + 1, r);
    for (int k = p; k <= r; k++) aux[k] = A[k];
    for (int k = p, i = p, j = q + 1; k <= r; k++)
        if (i > q) A[k] = aux[j++];
        else if (j > r) A[k] = aux[i++];
        else A[k] = (comp++, aux[i] <= aux[j]) ? aux[i++] : aux[j++];
}

/* Todas as n! permutações (algoritmo de Heap): o maior número de comparações. */
long pior_caso(int n) {
    int P[16], c[16] = {0}, A[16];
    for (int k = 0; k < n; k++) P[k] = k;
    long pior = 0;
    for (int i = 0;;) {
        for (int k = 0; k < n; k++) A[k] = P[k];
        comp = 0;
        merge_sort(A, 0, n - 1);
        if (comp > pior) pior = comp;
        while (i < n && c[i] >= i) c[i++] = 0;
        if (i >= n) return pior;
        int t, j = i % 2 ? c[i] : 0;
        t = P[j]; P[j] = P[i]; P[i] = t;
        c[i]++;
        i = 0;
    }
}

int main(void) {
    srand(13);
    int N = 1 << 20;
    aux = malloc(N * sizeof(int));
    printf("n,pior_merge,limite\n");
    for (int n = 2; n <= 10; n++)
        printf("%d,%ld,%.0f\n", n, pior_caso(n), ceil(lgamma(n + 1) / log(2) - 1e-9));
    printf("\nn,media_merge\n");
    int *A = malloc(N * sizeof(int));
    for (int n = 1 << 10; n <= N; n *= 2) {
        double soma = 0;
        for (int r = 0; r < 3; r++) {
            for (int k = 0; k < n; k++) A[k] = rand();
            comp = 0;
            merge_sort(A, 0, n - 1);
            soma += comp;
        }
        printf("%d,%.0f\n", n, soma / 3);
    }
    free(A); free(aux);
    return 0;
}
