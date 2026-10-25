// Aula 35 – Experimento: comparações do algoritmo ingênuo e do KMP
// Saída CSV: n, ingenuo, kmp (texto a^n, padrão a^99 b: o pior caso do ingênuo)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long comp;

void ingenuo(const char *T, int n, const char *P, int m) {
    for (int s = 0; s <= n - m; s++) {
        int j = 0;
        while (j < m && (comp++, T[s + j] == P[j])) j++;
    }
}

void kmp(const char *T, int n, const char *P, int m) {
    int *pi = malloc(m * sizeof(int));
    pi[0] = 0;
    for (int q = 1, k = 0; q < m; q++) {
        while (k > 0 && P[k] != P[q]) k = pi[k - 1];
        if (P[k] == P[q]) k++;
        pi[q] = k;
    }
    for (int i = 0, q = 0; i < n; i++) {
        while (q > 0 && (comp++, P[q] != T[i])) q = pi[q - 1];
        if (comp++, P[q] == T[i]) q++;
        if (q == m) q = pi[q - 1];
    }
    free(pi);
}

int main(void) {
    int m = 100;
    char *P = malloc(m + 1);
    memset(P, 'a', m - 1);
    P[m - 1] = 'b';
    P[m] = '\0';
    printf("n,ingenuo,kmp\n");
    for (int n = 10000; n <= 160000; n += 10000) {
        char *T = malloc(n + 1);
        memset(T, 'a', n);
        T[n] = '\0';
        long r[2];
        comp = 0; ingenuo(T, n, P, m); r[0] = comp;
        comp = 0; kmp(T, n, P, m); r[1] = comp;
        printf("%d,%ld,%ld\n", n, r[0], r[1]);
        free(T);
    }
    free(P);
    return 0;
}
