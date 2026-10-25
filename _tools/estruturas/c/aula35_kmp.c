// Aula 35 – Casamento de cadeias: Knuth-Morris-Pratt (Cormen, seção 32.4)
// teste: bacbababaabcbab ababaca => nenhuma ocorrência
// teste: abababacaba ababaca => ocorrência no deslocamento 2
// teste: aaaaa aa => ocorrência no deslocamento 3
#include <stdio.h>
#include <string.h>

/* pi[q] = tamanho do maior prefixo próprio de P[0..q] que também é sufixo dele.
   Quando um caractere não casa, voltamos para pi[q-1] em vez de recomeçar. */
void prefixo(const char *P, int m, int pi[]) {   // COMPUTE-PREFIX-FUNCTION: Θ(m)
    pi[0] = 0;
    for (int q = 1, k = 0; q < m; q++) {
        while (k > 0 && P[k] != P[q]) k = pi[k - 1];
        if (P[k] == P[q]) k++;
        pi[q] = k;
    }
}

int main(void) {
    char T[1001], P[101];
    if (scanf("%1000s %100s", T, P) != 2) return 1;
    int n = strlen(T), m = strlen(P), pi[101], achou = 0;
    prefixo(P, m, pi);
    for (int i = 0, q = 0; i < n; i++) {        // KMP-MATCHER: Θ(n)
        while (q > 0 && P[q] != T[i]) q = pi[q - 1];
        if (P[q] == T[i]) q++;
        if (q == m) {                           // casou P inteiro terminando em i
            printf("ocorrência no deslocamento %d\n", i - m + 1);
            achou = 1;
            q = pi[q - 1];                      // procura a próxima
        }
    }
    if (!achou) printf("nenhuma ocorrência\n");
    return 0;
}
