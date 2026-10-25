// Aula 15 – Seleção em tempo esperado linear: o i-ésimo menor (Cormen, seção 9.2)
// teste: 9 7 1 9 3 5 2 8 6 4 5 => 5º menor: 5
// teste: 5 10 40 30 20 50 1 => 1º menor: 10
#include <stdio.h>
#include <stdlib.h>

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

int particiona_aleatorio(int A[], int p, int r) {
    troca(A, p + rand() % (r - p + 1), r);
    int x = A[r], i = p - 1;
    for (int j = p; j < r; j++)
        if (A[j] <= x) troca(A, ++i, j);
    troca(A, i + 1, r);
    return i + 1;
}

/* RANDOMIZED-SELECT: como o quicksort, mas desce só no lado que contém a resposta. */
int seleciona(int A[], int p, int r, int i) {
    while (p < r) {
        int q = particiona_aleatorio(A, p, r);
        int k = q - p + 1;                       // o pivô é o k-ésimo menor de A[p..r]
        if (i == k) return A[q];
        if (i < k) r = q - 1;
        else { p = q + 1; i -= k; }
    }
    return A[p];
}

int main(void) {
    srand(15);
    int n, i;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    if (scanf("%d", &i) != 1 || i < 1 || i > n) return 1;
    printf("%dº menor: %d\n", i, seleciona(A, 0, n - 1, i));
    free(A);
    return 0;
}
