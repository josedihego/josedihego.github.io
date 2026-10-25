// Aula 11 – Quicksort com a partição de Lomuto (Cormen, seções 7.1 e 7.2)
// teste: 8 2 8 7 1 3 5 6 4 => 1 2 3 4 5 6 7 8
// teste: 5 3 3 3 3 3 => 3 3 3 3 3
// teste: 1 7 => 7
#include <stdio.h>
#include <stdlib.h>

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

/* PARTITION: pivô x = A[r]. Invariante: A[p..i] <= x, A[i+1..j-1] > x. */
int particiona(int A[], int p, int r) {
    int x = A[r], i = p - 1;
    for (int j = p; j < r; j++)
        if (A[j] <= x) troca(A, ++i, j);         // cresce a região dos menores
    troca(A, i + 1, r);                          // o pivô vai para o meio
    return i + 1;
}

void quicksort(int A[], int p, int r) {
    if (p < r) {
        int q = particiona(A, p, r);             // A[p..q-1] <= A[q] < A[q+1..r]
        quicksort(A, p, q - 1);
        quicksort(A, q + 1, r);                  // nada a combinar
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    quicksort(A, 0, n - 1);
    for (int k = 0; k < n; k++) printf("%d%c", A[k], k < n - 1 ? ' ' : '\n');
    free(A);
    return 0;
}
