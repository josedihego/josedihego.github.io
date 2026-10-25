// Aula 4 – Merge sort (Cormen, seção 2.3)
// teste: 8 5 2 4 7 1 3 2 6 => 1 2 2 3 4 5 6 7
// teste: 1 9 => 9
// teste: 5 3 3 1 1 2 => 1 1 2 3 3
#include <stdio.h>
#include <stdlib.h>

/* MERGE(A, p, q, r): intercala A[p..q] e A[q+1..r], ambos ordenados.
   No livro, sentinelas ∞ marcam o fim de L e R; aqui testamos os limites. */
void intercala(int A[], int p, int q, int r) {
    int n1 = q - p + 1, n2 = r - q;
    int *L = malloc(n1 * sizeof(int)), *R = malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++) L[i] = A[p + i];
    for (int j = 0; j < n2; j++) R[j] = A[q + 1 + j];
    int i = 0, j = 0;
    for (int k = p; k <= r; k++) {
        if (j >= n2 || (i < n1 && L[i] <= R[j]))   // <= mantém a ordem dos iguais
            A[k] = L[i++];
        else
            A[k] = R[j++];
    }
    free(L);
    free(R);
}

void merge_sort(int A[], int p, int r) {
    if (p < r) {
        int q = (p + r) / 2;            // dividir
        merge_sort(A, p, q);            // conquistar a metade esquerda
        merge_sort(A, q + 1, r);        // conquistar a metade direita
        intercala(A, p, q, r);          // combinar
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    merge_sort(A, 0, n - 1);
    for (int k = 0; k < n; k++) printf("%d%c", A[k], k < n - 1 ? ' ' : '\n');
    free(A);
    return 0;
}
