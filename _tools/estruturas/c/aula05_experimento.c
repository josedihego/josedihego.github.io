// Aula 5 – Experimento: estimar a ordem de crescimento a partir de contagens
// Saída CSV: n, binaria, linear, mergesort, pares (operações básicas de cada algoritmo)
#include <stdio.h>
#include <stdlib.h>

long ops;

int busca_binaria(const int A[], int n, int x) {     // pior caso: x ausente
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int m = lo + (hi - lo) / 2;
        ops++;
        if (A[m] == x) return m;
        if (A[m] < x) lo = m + 1; else hi = m - 1;
    }
    return -1;
}

int busca_linear(const int A[], int n, int x) {
    for (int i = 0; i < n; i++) { ops++; if (A[i] == x) return i; }
    return -1;
}

void merge_sort(int A[], int aux[], int p, int r) {
    if (p >= r) return;
    int q = (p + r) / 2;
    merge_sort(A, aux, p, q);
    merge_sort(A, aux, q + 1, r);
    for (int k = p; k <= r; k++) aux[k] = A[k];
    for (int k = p, i = p, j = q + 1; k <= r; k++, ops++)   // uma operação por posição
        A[k] = (j > r || (i <= q && aux[i] <= aux[j])) ? aux[i++] : aux[j++];
}

long pares(const int A[], int n) {
    long c = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) { ops++; c += (A[i] + A[j] == 0); }
    return c;
}

int main(void) {
    srand(5);
    printf("n,binaria,linear,mergesort,pares\n");
    for (int n = 256; n <= 32768; n *= 2) {
        int *A = malloc(n * sizeof(int)), *aux = malloc(n * sizeof(int));
        for (int k = 0; k < n; k++) A[k] = 2 * k;    // só pares: buscar 1 falha
        long r[4];
        ops = 0; busca_binaria(A, n, 1); r[0] = ops;
        ops = 0; busca_linear(A, n, 1); r[1] = ops;
        for (int k = 0; k < n; k++) A[k] = rand();
        ops = 0; merge_sort(A, aux, 0, n - 1); r[2] = ops;
        ops = 0; pares(A, n); r[3] = ops;
        printf("%d,%ld,%ld,%ld,%ld\n", n, r[0], r[1], r[2], r[3]);
        free(A); free(aux);
    }
    return 0;
}
