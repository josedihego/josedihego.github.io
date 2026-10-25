// Aula 12 – Experimento: o quicksort aleatorizado não tem entrada ruim
// Tabela 1 (n, fixo, aleatorizado): comparações com entrada JÁ ORDENADA
// Tabela 2 (comparacoes, frequencia): 20.000 execuções em n = 1000 ordenado
#include <stdio.h>
#include <stdlib.h>

long comp;

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

int particiona(int A[], int p, int r) {
    int x = A[r], i = p - 1;
    for (int j = p; j < r; j++)
        if (comp++, A[j] <= x) troca(A, ++i, j);
    troca(A, i + 1, r);
    return i + 1;
}

void quick(int A[], int p, int r, int sorteia) {
    while (p < r) {
        if (sorteia) troca(A, p + rand() % (r - p + 1), r);
        int q = particiona(A, p, r);
        if (q - p < r - q) { quick(A, p, q - 1, sorteia); p = q + 1; }
        else { quick(A, q + 1, r, sorteia); r = q - 1; }
    }
}

int main(void) {
    srand(12);
    int *A = malloc(16000 * sizeof(int));
    printf("n,fixo,aleatorizado\n");
    for (int n = 1000; n <= 16000; n += 1000) {
        for (int k = 0; k < n; k++) A[k] = k;
        comp = 0; quick(A, 0, n - 1, 0);
        long fixo = comp;
        double soma = 0;
        for (int rep = 0; rep < 20; rep++) {
            for (int k = 0; k < n; k++) A[k] = k;
            comp = 0; quick(A, 0, n - 1, 1);
            soma += comp;
        }
        printf("%d,%ld,%.0f\n", n, fixo, soma / 20);
    }
    printf("\ncomparacoes,frequencia\n");
    int hist[400] = {0};
    for (int rep = 0; rep < 20000; rep++) {
        for (int k = 0; k < 1000; k++) A[k] = k;
        comp = 0; quick(A, 0, 999, 1);
        int b = comp / 250;
        if (b < 400) hist[b]++;
    }
    for (int b = 0; b < 400; b++)
        if (hist[b]) printf("%d,%d\n", b * 250 + 125, hist[b]);
    free(A);
    return 0;
}
