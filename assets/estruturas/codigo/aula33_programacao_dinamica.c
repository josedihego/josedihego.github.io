// Aula 33 – Programação dinâmica: corte de hastes e LCS (Cormen, capítulo 15)
#include <stdio.h>
#include <string.h>

/* Preços da Figura 15.1: p[i] = preço de uma haste de comprimento i. */
int p[11] = {0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30};

int corte(int n) {                            // BOTTOM-UP-CUT-ROD: Θ(n²)
    int r[11] = {0};                          // r[j]: melhor receita para comprimento j
    for (int j = 1; j <= n; j++) {
        int q = -1;
        for (int i = 1; i <= j; i++)          // primeiro pedaço de comprimento i
            if (p[i] + r[j - i] > q) q = p[i] + r[j - i];
        r[j] = q;
    }
    return r[n];
}

/* LCS-LENGTH: c[i][j] = tamanho da LCS de X[1..i] e Y[1..j]. Θ(m n). */
int c[101][101];

void lcs(const char *X, const char *Y, char *saida) {
    int m = strlen(X), n = strlen(Y);
    for (int i = 0; i <= m; i++) c[i][0] = 0;
    for (int j = 0; j <= n; j++) c[0][j] = 0;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (X[i - 1] == Y[j - 1]) c[i][j] = c[i - 1][j - 1] + 1;   // estende
            else c[i][j] = c[i - 1][j] >= c[i][j - 1] ? c[i - 1][j] : c[i][j - 1];
    int k = c[m][n];                          // PRINT-LCS, de trás para frente
    saida[k] = '\0';
    for (int i = m, j = n; i > 0 && j > 0;)
        if (X[i - 1] == Y[j - 1]) { saida[--k] = X[i - 1]; i--; j--; }
        else if (c[i - 1][j] >= c[i][j - 1]) i--;
        else j--;
}

int main(void) {
    int n;
    char X[101], Y[101], z[101];
    if (scanf("%d %100s %100s", &n, X, Y) != 3 || n < 1 || n > 10) return 1;
    printf("receita %d\n", corte(n));
    lcs(X, Y, z);
    printf("LCS de tamanho %d: %s\n", (int)strlen(z), z);
    return 0;
}
