// Aula 7 – Subarranjo máximo por divisão e conquista (Cormen, seção 4.1)
// teste: 16 13 -3 -25 20 -3 -16 -23 18 20 -7 12 -5 -22 15 -4 7 => soma 43 de A[8..11]
// teste: 3 -1 -2 -3 => soma -1 de A[1..1]
#include <stdio.h>
#include <stdlib.h>

typedef struct { int ini, fim; long soma; } Faixa;

/* FIND-MAX-CROSSING-SUBARRAY: o melhor subarranjo que cruza o meio. */
Faixa cruzando(const int A[], int lo, int meio, int hi) {
    long s = 0, esq = -__LONG_MAX__, dir = -__LONG_MAX__;
    int i_max = meio, j_max = meio + 1;
    for (int i = meio; i >= lo; i--) {          // melhor sufixo de A[lo..meio]
        s += A[i];
        if (s > esq) { esq = s; i_max = i; }
    }
    s = 0;
    for (int j = meio + 1; j <= hi; j++) {      // melhor prefixo de A[meio+1..hi]
        s += A[j];
        if (s > dir) { dir = s; j_max = j; }
    }
    return (Faixa){i_max, j_max, esq + dir};
}

Faixa maximo(const int A[], int lo, int hi) {
    if (lo == hi) return (Faixa){lo, hi, A[lo]};   // caso base: um elemento
    int meio = (lo + hi) / 2;
    Faixa e = maximo(A, lo, meio), d = maximo(A, meio + 1, hi);
    Faixa c = cruzando(A, lo, meio, hi);
    if (e.soma >= d.soma && e.soma >= c.soma) return e;
    if (d.soma >= e.soma && d.soma >= c.soma) return d;
    return c;
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int *A = malloc(n * sizeof(int));
    for (int k = 0; k < n; k++)
        if (scanf("%d", &A[k]) != 1) return 1;
    Faixa f = maximo(A, 0, n - 1);
    // + 1: índices como no livro (1..n)
    printf("soma %ld de A[%d..%d]\n", f.soma, f.ini + 1, f.fim + 1);
    free(A);
    return 0;
}
