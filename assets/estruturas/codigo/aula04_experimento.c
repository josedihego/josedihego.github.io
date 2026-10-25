// Aula 4 – Experimento: comparações do merge sort e o cruzamento com a inserção
// Tabela 1 (n, comparacoes): merge sort em permutações aleatórias, média de 5
// Tabela 2 (n, insercao_us, merge_us): tempo para n pequeno
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long comparacoes;
int *aux;                    // vetor auxiliar único (evita malloc a cada merge)

void intercala(int A[], int p, int q, int r) {
    for (int k = p; k <= r; k++) aux[k] = A[k];
    int i = p, j = q + 1;
    for (int k = p; k <= r; k++) {
        if (i > q) A[k] = aux[j++];
        else if (j > r) A[k] = aux[i++];
        else if (comparacoes++, aux[i] <= aux[j]) A[k] = aux[i++];
        else A[k] = aux[j++];
    }
}

void merge_sort(int A[], int p, int r) {
    if (p < r) {
        int q = (p + r) / 2;
        merge_sort(A, p, q);
        merge_sort(A, q + 1, r);
        intercala(A, p, q, r);
    }
}

void insercao(int A[], int n) {
    for (int j = 1; j < n; j++) {
        int chave = A[j], i = j - 1;
        while (i >= 0 && A[i] > chave) { A[i + 1] = A[i]; i--; }
        A[i + 1] = chave;
    }
}

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

int main(void) {
    srand(42);
    int N = 1 << 20;
    int *A = malloc(N * sizeof(int)), *B = malloc(N * sizeof(int));
    aux = malloc(N * sizeof(int));
    printf("n,comparacoes\n");
    for (int n = 1 << 12; n <= N; n *= 2) {
        double soma = 0;
        for (int r = 0; r < 5; r++) {
            for (int k = 0; k < n; k++) A[k] = rand();
            comparacoes = 0;
            merge_sort(A, 0, n - 1);
            soma += comparacoes;
        }
        printf("%d,%.0f\n", n, soma / 5);
    }
    printf("\nn,insercao_us,merge_us\n");
    for (int n = 10; n <= 500; n += 10) {
        double ti = 1e30, tm = 1e30;
        for (int rep = 0; rep < 5; rep++) {    // melhor de 5 lotes de 2000
            for (int k = 0; k < n * 2000; k++) B[k % N] = rand();
            double t0 = agora();
            for (int s = 0; s < 2000; s++) {
                for (int k = 0; k < n; k++) A[k] = B[k + s % 64];
                insercao(A, n);
            }
            double t1 = agora();
            for (int s = 0; s < 2000; s++) {
                for (int k = 0; k < n; k++) A[k] = B[k + s % 64];
                merge_sort(A, 0, n - 1);
            }
            double t2 = agora();
            if (t1 - t0 < ti) ti = t1 - t0;
            if (t2 - t1 < tm) tm = t2 - t1;
        }
        printf("%d,%.3f,%.3f\n", n, ti / 2000 * 1e6, tm / 2000 * 1e6);
    }
    free(A); free(B); free(aux);
    return 0;
}
