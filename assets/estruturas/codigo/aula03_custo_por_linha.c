// Aula 3 – Custo linha a linha da ordenação por inserção (a tabela da seção 2.2)
#include <stdio.h>
#include <stdlib.h>

/* vezes[k] = quantas vezes a linha k do pseudocódigo do livro executou (k = 1..8). */
long vezes[9];

void ordena_insercao(int A[], int n) {
    int j;
    for (j = 1; vezes[1]++, j < n; j++) {   // linha 1: o teste roda n vezes
        int chave = A[j];          vezes[2]++;
        int i = j - 1;             vezes[4]++;
        while (vezes[5]++, i >= 0 && A[i] > chave) {   // linha 5: t_j testes
            A[i + 1] = A[i];       vezes[6]++;
            i--;                   vezes[7]++;
        }
        A[i + 1] = chave;          vezes[8]++;
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    ordena_insercao(A, n);
    const char *nome[9] = {"", "para", "chave = A[j]", "comentário",
                           "i = j - 1",
                           "teste do enquanto", "A[i+1] = A[i]", "i = i - 1",
                           "A[i+1] = chave"};
    for (int k = 1; k <= 8; k++)
        if (k != 3) printf("linha %d (%s): %ld vezes\n", k, nome[k], vezes[k]);
    free(A);
    return 0;
}
