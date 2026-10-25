// Aula 11 – Experimento: comparações do quicksort em entradas aleatórias e ordenadas
// Tabela 1 (n, aleatorio): média de 5 vetores aleatórios, n até 2^20
// Tabela 2 (n, ordenado): vetor já ordenado (pior caso da partição de Lomuto)
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

void quicksort(int A[], int p, int r) {
    while (p < r) {                         // recursão só no lado menor: pilha O(lg n)
        int q = particiona(A, p, r);
        if (q - p < r - q) { quicksort(A, p, q - 1); p = q + 1; }
        else { quicksort(A, q + 1, r); r = q - 1; }
    }
}

int main(void) {
    srand(11);
    int N = 1 << 20;
    int *A = malloc(N * sizeof(int));
    printf("n,aleatorio\n");
    for (int n = 1 << 12; n <= N; n *= 2) {
        double soma = 0;
        for (int rep = 0; rep < 5; rep++) {
            for (int k = 0; k < n; k++) A[k] = rand();
            comp = 0;
            quicksort(A, 0, n - 1);
            soma += comp;
        }
        printf("%d,%.0f\n", n, soma / 5);
    }
    printf("\nn,ordenado\n");
    for (int n = 1000; n <= 16000; n += 1000) {
        for (int k = 0; k < n; k++) A[k] = k;
        comp = 0;
        quicksort(A, 0, n - 1);
        printf("%d,%ld\n", n, comp);
    }
    free(A);
    return 0;
}
