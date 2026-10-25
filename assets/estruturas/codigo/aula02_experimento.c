// Aula 2 – Experimento: comparações da ordenação por inserção em três tipos de entrada
// Saída CSV: n, ordenado, aleatorio, invertido (número de comparações A[i] > chave)
#include <stdio.h>
#include <stdlib.h>

long comparacoes;                // contador global, zerado antes de cada ordenação

void ordena_insercao(int A[], int n) {
    for (int j = 1; j < n; j++) {
        int chave = A[j], i = j - 1;
        // o operador vírgula conta cada teste A[i] > chave antes de fazê-lo
        while (i >= 0 && (comparacoes++, A[i] > chave)) {
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = chave;
    }
}

long mede(int A[], int n) {
    comparacoes = 0;
    ordena_insercao(A, n);
    return comparacoes;
}

int main(void) {
    srand(2026);                           // semente fixa: o experimento é reproduzível
    printf("n,ordenado,aleatorio,invertido\n");
    for (int n = 500; n <= 8000; n += 500) {
        int *A = malloc(n * sizeof(int));
        for (int k = 0; k < n; k++) A[k] = k;        // melhor caso: já ordenado
        long c1 = mede(A, n);
        double soma = 0;                     // caso médio: média de 5 permutações
        for (int r = 0; r < 5; r++) {
            for (int k = 0; k < n; k++) A[k] = rand();
            soma += mede(A, n);
        }
        for (int k = 0; k < n; k++) A[k] = n - k;    // pior caso: decrescente
        long c3 = mede(A, n);
        printf("%d,%ld,%.0f,%ld\n", n, c1, soma / 5, c3);
        free(A);
    }
    return 0;
}
