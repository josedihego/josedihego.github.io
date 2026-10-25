// Aula 6 – Avaliar T(n) = a T(n/b) + n^k e comparar com o teorema mestre
// teste: 2 2 1 1024 => caso 2
// teste: 4 2 1 1024 => caso 1
// teste: 1 2 2 1024 => caso 3
#include <stdio.h>
#include <math.h>

int a, b;
double k;

/* T(1) = 1; divisão inteira (piso), como em código real. */
double T(long n) {
    if (n <= 1) return 1;
    return a * T(n / b) + pow(n, k);
}

int main(void) {
    long n;
    if (scanf("%d %d %lf %ld", &a, &b, &k, &n) != 4) return 1;
    if (a < 1 || b < 2 || n < 1) return 1;
    double e = log(a) / log(b);           // expoente crítico log_b a
    printf("T(%ld) = %.0f\n", n, T(n));
    printf("log_%d %d = %.3f e f(n) = n^%.2f\n", b, a, e, k);
    if (fabs(k - e) < 1e-9)
        printf("caso 2: T(n) = Θ(n^%.3f lg n), previsão %.0f\n", e,
               pow(n, e) * log2(n));
    else if (k < e)
        printf("caso 1: T(n) = Θ(n^%.3f), previsão %.0f\n", e, pow(n, e));
    else
        printf("caso 3: T(n) = Θ(n^%.2f), previsão %.0f\n", k, pow(n, k));
    return 0;
}
