// Aula 8 – Experimento: construir o heap é linear; o heapsort é n lg n
// Saída CSV: n, construcao, heapsort (comparações entre chaves, média de 3 vetores)
#include <stdio.h>
#include <stdlib.h>

long comparacoes;

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

void max_heapify(int A[], int tam, int i) {
    for (;;) {                                 // versão iterativa (sem recursão)
        int e = 2 * i + 1, d = e + 1, maior = i;
        if (e < tam && (comparacoes++, A[e] > A[maior])) maior = e;
        if (d < tam && (comparacoes++, A[d] > A[maior])) maior = d;
        if (maior == i) return;
        troca(A, i, maior);
        i = maior;
    }
}

int main(void) {
    srand(8);
    printf("n,construcao,heapsort\n");
    for (int n = 1 << 12; n <= 1 << 21; n *= 2) {
        int *A = malloc(n * sizeof(int));
        double c1 = 0, c2 = 0;
        for (int r = 0; r < 3; r++) {
            for (int k = 0; k < n; k++) A[k] = rand();
            comparacoes = 0;
            for (int i = n / 2 - 1; i >= 0; i--) max_heapify(A, n, i);
            c1 += comparacoes;
            for (int fim = n - 1; fim > 0; fim--) {
                troca(A, 0, fim);
                max_heapify(A, fim, 0);
            }
            c2 += comparacoes;                 // total: construção + extrações
        }
        printf("%d,%.0f,%.0f\n", n, c1 / 3, c2 / 3);
        free(A);
    }
    return 0;
}
