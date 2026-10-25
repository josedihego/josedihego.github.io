// Aula 5 – Quanto cabe em 1 segundo? Tabela de crescimento das funções (problema 1-1)
#include <stdio.h>
#include <math.h>

/* Supondo `ops` operações por segundo, qual o maior n resolvido em 1 s para cada f(n)?
   Busca binária sobre n: f é crescente, basta achar o último n com f(n) <= ops. */
double f(int qual, double n) {
    switch (qual) {
        case 0: return log2(n);
        case 1: return sqrt(n);
        case 2: return n;
        case 3: return n * log2(n);
        case 4: return n * n;
        case 5: return n * n * n;
        case 6: return pow(2, n);
        default: return tgamma(n + 1);          // n! = Γ(n + 1)
    }
}

int main(void) {
    double ops;
    if (scanf("%lf", &ops) != 1 || ops < 1) return 1;
    const char *nome[8] = {"lg n", "raiz de n", "n", "n lg n",
                           "n^2", "n^3", "2^n", "n!"};
    printf("%-10s  maior n em 1 s com %.0e operações/s\n", "f(n)", ops);
    for (int q = 0; q < 8; q++) {
        double lo = 1, hi = 2;
        while (hi < 1e300 && f(q, hi) <= ops) hi *= 2;   // dobra até passar
        for (int it = 0; it < 200; it++) {              // depois, busca binária
            double meio = (lo + hi) / 2;
            if (f(q, meio) <= ops) lo = meio; else hi = meio;
        }
        if (lo > 1e15) printf("%-10s  %.2e\n", nome[q], lo);
        else printf("%-10s  %.0f\n", nome[q], floor(lo));
    }
    return 0;
}
