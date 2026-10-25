// Aula 6 – Experimento: T(n) pela recorrência contra a previsão do teorema mestre
// Saída CSV: n, dois (2T(n/2)+n), quatro (4T(n/2)+n), um (T(n/2)+1), sete (7T(n/2)+n²)
#include <stdio.h>

double T(int a, int pot, long n) {      // T(1) = 1; f(n) = n^pot (pot = 0, 1 ou 2)
    if (n <= 1) return 1;
    double f = pot == 0 ? 1 : pot == 1 ? (double)n : (double)n * n;
    double sub = T(a, pot, n / 2);       // os a subproblemas são iguais: calcula um só
    return a * sub + f;
}

int main(void) {
    printf("n,dois,quatro,um,sete\n");
    for (long n = 16; n <= (1L << 24); n *= 2)
        printf("%ld,%.0f,%.0f,%.0f,%.0f\n", n,
               T(2, 1, n), T(4, 1, n), T(1, 0, n), T(7, 2, n));
    return 0;
}
