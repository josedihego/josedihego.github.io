// Aula 8 – Heaps e heapsort (Cormen, capítulo 6)
#include <stdio.h>
#include <stdlib.h>

/* Heap em vetor com índices 0..n-1: filhos de i em 2i+1 e 2i+2
   (no livro, com índices 1..n: 2i e 2i+1). */
#define ESQ(i) (2 * (i) + 1)
#define DIR(i) (2 * (i) + 2)

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

/* MAX-HEAPIFY: supõe que as subárvores de i já são heaps e faz i "descer". */
void max_heapify(int A[], int tam, int i) {
    int maior = i;
    if (ESQ(i) < tam && A[ESQ(i)] > A[maior]) maior = ESQ(i);
    if (DIR(i) < tam && A[DIR(i)] > A[maior]) maior = DIR(i);
    if (maior != i) {
        troca(A, i, maior);
        max_heapify(A, tam, maior);
    }
}

void constroi_heap(int A[], int n) {          // BUILD-MAX-HEAP: das folhas para a raiz
    for (int i = n / 2 - 1; i >= 0; i--) max_heapify(A, n, i);
}

void heapsort(int A[], int n) {
    constroi_heap(A, n);
    for (int fim = n - 1; fim > 0; fim--) {
        troca(A, 0, fim);                     // o máximo vai para o fim
        max_heapify(A, fim, 0);               // o heap encolhe uma posição
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    heapsort(A, n);
    for (int k = 0; k < n; k++) printf("%d%c", A[k], k < n - 1 ? ' ' : '\n');
    free(A);
    return 0;
}
