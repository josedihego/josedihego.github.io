// Aula 2 – Ordenação por inserção (Cormen, seção 2.1)
#include <stdio.h>
#include <stdlib.h>

/* INSERTION-SORT(A): o livro indexa de 1 a n; em C, de 0 a n-1.
   Invariante: no início de cada volta, A[0..j-1] contém os elementos
   originais de A[0..j-1], em ordem. */
void ordena_insercao(int A[], int n) {
    for (int j = 1; j < n; j++) {          // linha 1 do livro: j = 2 até n
        int chave = A[j];                  // a "carta" que será inserida
        int i = j - 1;
        while (i >= 0 && A[i] > chave) {   // desloca os maiores uma posição à direita
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = chave;                  // a chave cai no buraco aberto
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));      // vetor do tamanho pedido
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    ordena_insercao(A, n);
    for (int k = 0; k < n; k++) printf("%d%c", A[k], k < n - 1 ? ' ' : '\n');
    free(A);
    return 0;
}
