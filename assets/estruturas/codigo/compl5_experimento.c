// Complemento 5 – Experimento: seleção aleatorizada e bucket sort
// Tabela 1 (n, mediana): comparações para achar a mediana (média de muitas execuções)
// Tabela 2 (n, uniforme, concentrada): deslocamentos do bucket sort
#include <stdio.h>
#include <stdlib.h>

long comp;

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

int seleciona(int A[], int p, int r, int i) {
    while (p < r) {
        troca(A, p + rand() % (r - p + 1), r);
        int x = A[r], m = p - 1;
        for (int j = p; j < r; j++)
            if (comp++, A[j] <= x) troca(A, ++m, j);
        troca(A, m + 1, r);
        int q = m + 1, k = q - p + 1;
        if (i == k) return A[q];
        if (i < k) r = q - 1;
        else { p = q + 1; i -= k; }
    }
    return A[p];
}

/* Bucket sort de n valores em [0, 1): n baldes, inserção em cada balde.
   Conta os deslocamentos da inserção (o trabalho que depende da distribuição). */
long bucket(double v[], int n) {
    int *tam = calloc(n, sizeof(int)), *ini = calloc(n + 1, sizeof(int));
    double *B = malloc(n * sizeof(double));
    for (int k = 0; k < n; k++) tam[(int)(v[k] * n)]++;
    for (int b = 0; b < n; b++) ini[b + 1] = ini[b] + tam[b];
    int *pos = calloc(n, sizeof(int));
    long desloc = 0;
    for (int k = 0; k < n; k++) {               // insere v[k] no seu balde, em ordem
        int b = (int)(v[k] * n), j = ini[b] + pos[b]++ - 1;
        while (j >= ini[b] && B[j] > v[k]) { B[j + 1] = B[j]; j--; desloc++; }
        B[j + 1] = v[k];
    }
    free(tam); free(ini); free(pos); free(B);
    return desloc;
}

int main(void) {
    srand(16);
    int N = 1 << 18;
    int *A = malloc(N * sizeof(int));
    printf("n,mediana\n");
    for (int n = 1 << 10; n <= N; n *= 2) {
        double soma = 0;
        // uma execução isolada varia muito: média de pelo menos 200
        int reps = (1 << 25) / n > 200 ? (1 << 25) / n : 200;
        for (int rep = 0; rep < reps; rep++) {
            for (int k = 0; k < n; k++) A[k] = rand();
            comp = 0;
            seleciona(A, 0, n - 1, (n + 1) / 2);
            soma += comp;
        }
        printf("%d,%.0f\n", n, soma / reps);
    }
    printf("\nn,uniforme,concentrada\n");
    double *v = malloc(16000 * sizeof(double));
    for (int n = 1000; n <= 16000; n += 1000) {
        for (int k = 0; k < n; k++) v[k] = rand() / (RAND_MAX + 1.0);
        long u = bucket(v, n);
        for (int k = 0; k < n; k++)                  // tudo no balde 0
            v[k] = rand() / (RAND_MAX + 1.0) / n;
        long c = bucket(v, n);
        printf("%d,%ld,%ld\n", n, u, c);
    }
    free(A); free(v);
    return 0;
}
