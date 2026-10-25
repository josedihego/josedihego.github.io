// Aula 3 – Experimento: o caso médio da inserção e a distribuição das comparações
// Tabela 1 (n, melhor, media, pior): média de 300 permutações aleatórias por n
// Tabela 2 (comparacoes, frequencia): histograma para n = 100 e 100.000 permutações
#include <stdio.h>
#include <stdlib.h>

long comparacoes;

void ordena_insercao(int A[], int n) {
    for (int j = 1; j < n; j++) {
        int chave = A[j], i = j - 1;
        while (i >= 0 && (comparacoes++, A[i] > chave)) {
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = chave;
    }
}

void embaralha(int A[], int n) {                 // Fisher–Yates: permutação uniforme
    for (int k = 0; k < n; k++) A[k] = k;
    for (int k = n - 1; k > 0; k--) {
        int r = rand() % (k + 1), t = A[k];
        A[k] = A[r];
        A[r] = t;
    }
}

int main(void) {
    srand(7);
    printf("n,melhor,media,pior\n");
    for (int n = 100; n <= 2000; n += 100) {
        int *A = malloc(n * sizeof(int));
        double soma = 0;
        for (int r = 0; r < 300; r++) {
            embaralha(A, n);
            comparacoes = 0;
            ordena_insercao(A, n);
            soma += comparacoes;
        }
        printf("%d,%d,%.1f,%ld\n", n, n - 1, soma / 300, (long)n * (n - 1) / 2);
        free(A);
    }
    printf("\ncomparacoes,frequencia\n");        // linha em branco separa as tabelas
    int A[100], hist[200] = {0};                 // classes de largura 50 comparações
    for (int r = 0; r < 100000; r++) {
        embaralha(A, 100);
        comparacoes = 0;
        ordena_insercao(A, 100);
        hist[comparacoes / 50]++;
    }
    for (int b = 0; b < 200; b++)
        if (hist[b]) printf("%d,%d\n", b * 50 + 25, hist[b]);
    return 0;
}
