// Aula 12 – Quicksort aleatorizado (Cormen, seção 7.3)
// teste: 8 1 2 3 4 5 6 7 8 => 1 2 3 4 5 6 7 8
// teste: 6 9 9 1 1 5 0 => 0 1 1 5 9 9
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

int particiona(int A[], int p, int r) {
    int x = A[r], i = p - 1;
    for (int j = p; j < r; j++)
        if (A[j] <= x) troca(A, ++i, j);
    troca(A, i + 1, r);
    return i + 1;
}

/* RANDOMIZED-PARTITION: sorteia o pivô em A[p..r] e o leva para o fim. */
int particiona_aleatorio(int A[], int p, int r) {
    int k = p + rand() % (r - p + 1);
    troca(A, k, r);
    return particiona(A, p, r);
}

void quicksort_aleatorio(int A[], int p, int r) {
    if (p < r) {
        int q = particiona_aleatorio(A, p, r);
        quicksort_aleatorio(A, p, q - 1);
        quicksort_aleatorio(A, q + 1, r);
    }
}

int main(void) {
    srand((unsigned)time(NULL));             // cada execução sorteia pivôs diferentes
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    quicksort_aleatorio(A, 0, n - 1);
    for (int k = 0; k < n; k++) printf("%d%c", A[k], k < n - 1 ? ' ' : '\n');
    free(A);
    return 0;
}
