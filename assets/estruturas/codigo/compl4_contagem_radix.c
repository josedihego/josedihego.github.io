// Complemento 4 – Ordenação por contagem e radix sort (Cormen, seções 8.2 e 8.3)
#include <stdio.h>
#include <stdlib.h>

/* COUNTING-SORT: chaves em 0..k. C[v] conta; depois vira "quantos são <= v".
   Percorrer A de trás para frente torna o algoritmo estável. */
void contagem(const int A[], int B[], int n, int k) {
    int *C = calloc(k + 1, sizeof(int));
    for (int j = 0; j < n; j++) C[A[j]]++;
    for (int v = 1; v <= k; v++) C[v] += C[v - 1];
    for (int j = n - 1; j >= 0; j--) B[--C[A[j]]] = A[j];
    free(C);
}

/* RADIX-SORT (LSD) em base 10: contagem estável dígito a dígito, do menos
   significativo para o mais significativo. */
void radix(int A[], int n, int digitos) {
    int *B = malloc(n * sizeof(int));
    for (int d = 0, pot = 1; d < digitos; d++, pot *= 10) {
        int C[10] = {0};
        for (int j = 0; j < n; j++) C[A[j] / pot % 10]++;
        for (int v = 1; v < 10; v++) C[v] += C[v - 1];
        for (int j = n - 1; j >= 0; j--) B[--C[A[j] / pot % 10]] = A[j];
        for (int j = 0; j < n; j++) A[j] = B[j];
    }
    free(B);
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int)), *B = malloc(n * sizeof(int)), max = 0;
    for (int k = 0; k < n; k++) {
        if (scanf("%d", &A[k]) != 1 || A[k] < 0) return 1;
        if (A[k] > max) max = A[k];
    }
    if (max < 100) {                          // chaves pequenas: contagem direta
        contagem(A, B, n, max);
        printf("contagem:");
    } else {                                  // chaves maiores: radix nos dígitos
        int digitos = 0;
        for (int m = max; m > 0; m /= 10) digitos++;
        radix(A, n, digitos);
        for (int k = 0; k < n; k++) B[k] = A[k];
        printf("radix:");
    }
    for (int k = 0; k < n; k++) printf(" %d", B[k]);
    printf("\n");
    free(A); free(B);
    return 0;
}
