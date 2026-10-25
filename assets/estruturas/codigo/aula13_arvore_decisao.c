// Aula 13 – Limite inferior: pior caso do merge sort contra ceil(lg n!) para n pequeno
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Percorre TODAS as n! permutações (algoritmo de Heap) e guarda o maior número
   de comparações que o merge sort fez: a altura da sua árvore de decisão. */
long comp;
int aux[16];

void merge_sort(int A[], int p, int r) {
    if (p >= r) return;
    int q = (p + r) / 2;
    merge_sort(A, p, q);
    merge_sort(A, q + 1, r);
    for (int k = p; k <= r; k++) aux[k] = A[k];
    for (int k = p, i = p, j = q + 1; k <= r; k++)
        if (i > q) A[k] = aux[j++];
        else if (j > r) A[k] = aux[i++];
        else A[k] = (comp++, aux[i] <= aux[j]) ? aux[i++] : aux[j++];
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1 || n > 11) return 1;
    int P[16], c[16] = {0}, A[16];
    for (int k = 0; k < n; k++) P[k] = k;
    long pior = 0;
    for (int i = 0;;) {                          // algoritmo de Heap (iterativo)
        for (int k = 0; k < n; k++) A[k] = P[k];
        comp = 0;
        merge_sort(A, 0, n - 1);
        if (comp > pior) pior = comp;
        while (i < n && c[i] >= i) c[i++] = 0;   // próxima permutação
        if (i >= n) break;
        int t, j = i % 2 ? c[i] : 0;
        t = P[j]; P[j] = P[i]; P[i] = t;
        c[i]++;
        i = 0;
    }
    double lg_fat = lgamma(n + 1) / log(2);      // lg n! = ln Γ(n+1) / ln 2
    printf("n = %d: limite %.0f, merge sort %ld\n", n, ceil(lg_fat - 1e-9), pior);
    return 0;
}
