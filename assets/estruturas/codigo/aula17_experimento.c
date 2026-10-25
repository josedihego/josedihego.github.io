// Aula 17 – Experimento: n inserções e depois n extrações em três filas de prioridade
// Saída CSV: n, heap, ordenado, desordenado (comparações entre chaves)
#include <stdio.h>
#include <stdlib.h>

long comp;

/* 1) heap de máximo */
void heap_insere(int A[], int *tam, int x) {
    int i = (*tam)++;
    A[i] = x;
    while (i > 0 && (comp++, A[(i - 1) / 2] < A[i])) {
        int p = (i - 1) / 2, t = A[p]; A[p] = A[i]; A[i] = t; i = p;
    }
}
int heap_extrai(int A[], int *tam) {
    int max = A[0], i = 0;
    A[0] = A[--*tam];
    for (;;) {
        int e = 2 * i + 1, d = e + 1, m = i;
        if (e < *tam && (comp++, A[e] > A[m])) m = e;
        if (d < *tam && (comp++, A[d] > A[m])) m = d;
        if (m == i) return max;
        int t = A[i]; A[i] = A[m]; A[m] = t; i = m;
    }
}

/* 2) vetor ordenado (crescente): inserir desloca; o máximo está no fim */
void ord_insere(int A[], int *tam, int x) {
    int i = (*tam)++ - 1;
    while (i >= 0 && (comp++, A[i] > x)) { A[i + 1] = A[i]; i--; }
    A[i + 1] = x;
}
int ord_extrai(int A[], int *tam) { return A[--*tam]; }

/* 3) vetor desordenado: inserir é O(1); extrair procura o máximo */
void des_insere(int A[], int *tam, int x) { A[(*tam)++] = x; }
int des_extrai(int A[], int *tam) {
    int m = 0;
    for (int i = 1; i < *tam; i++) if (comp++, A[i] > A[m]) m = i;
    int max = A[m];
    A[m] = A[--*tam];
    return max;
}

int main(void) {
    srand(10);
    printf("n,heap,ordenado,desordenado\n");
    for (int n = 1000; n <= 16000; n += 1000) {
        int *dados = malloc(n * sizeof(int)), *A = malloc(n * sizeof(int));
        for (int k = 0; k < n; k++) dados[k] = rand();
        long r[3];
        int tam;
        comp = 0; tam = 0;
        for (int k = 0; k < n; k++) heap_insere(A, &tam, dados[k]);
        while (tam) heap_extrai(A, &tam);
        r[0] = comp;
        comp = 0; tam = 0;
        for (int k = 0; k < n; k++) ord_insere(A, &tam, dados[k]);
        while (tam) ord_extrai(A, &tam);
        r[1] = comp;
        comp = 0; tam = 0;
        for (int k = 0; k < n; k++) des_insere(A, &tam, dados[k]);
        while (tam) des_extrai(A, &tam);
        r[2] = comp;
        printf("%d,%ld,%ld,%ld\n", n, r[0], r[1], r[2]);
        free(dados); free(A);
    }
    return 0;
}
