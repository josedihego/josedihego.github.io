// Aula 33 – Experimento: recursão ingênua contra memoização no corte de hastes
// Saída CSV: n, ingenua, memoizada (chamadas recursivas)
#include <stdio.h>

long chamadas;
int p[41];

int ingenua(int n) {                          // CUT-ROD: refaz os mesmos subproblemas
    chamadas++;
    if (n == 0) return 0;
    int q = -1;
    for (int i = 1; i <= n; i++) {
        int v = p[i] + ingenua(n - i);
        if (v > q) q = v;
    }
    return q;
}

int memo[41];

int memoizada(int n) {                        // MEMOIZED-CUT-ROD: cada n uma vez
    chamadas++;
    if (memo[n] >= 0) return memo[n];
    int q = 0;
    for (int i = 1; i <= n; i++) {
        int v = p[i] + memoizada(n - i);
        if (v > q) q = v;
    }
    return memo[n] = q;
}

int main(void) {
    for (int i = 1; i <= 40; i++) p[i] = 3 * i + (i * 7) % 5;   // preços quaisquer
    printf("n,ingenua,memoizada\n");
    for (int n = 2; n <= 26; n += 2) {
        chamadas = 0;
        int a = ingenua(n);
        long c1 = chamadas;
        for (int i = 0; i <= n; i++) memo[i] = -1;
        chamadas = 0;
        int b = memoizada(n);
        if (a != b) { fprintf(stderr, "respostas diferentes!\n"); return 1; }
        printf("%d,%ld,%ld\n", n, c1, chamadas);
    }
    return 0;
}
