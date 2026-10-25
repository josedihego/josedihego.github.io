// Aula 13 – Experimento: custo amortizado do vetor dinâmico
// Saída CSV: n, dobra, mais_mil (cópias de elementos para fazer n inserções)
// n = 2^k + 1: logo depois de uma expansão, o pior momento para o vetor que dobra
#include <stdio.h>

int main(void) {
    printf("n,dobra,mais_mil\n");
    for (long n = (1 << 10) + 1; n <= (1 << 20) + 1; n = 2 * (n - 1) + 1) {
        long cap = 1, copias = 0;              // estratégia 1: dobrar a capacidade
        for (long tam = 0; tam < n; tam++)
            if (tam == cap) { copias += tam; cap *= 2; }
        long cap2 = 1000, copias2 = 0;          // estratégia 2: somar 1000 posições
        for (long tam = 0; tam < n; tam++)
            if (tam == cap2) { copias2 += tam; cap2 += 1000; }
        printf("%ld,%ld,%ld\n", n, copias, copias2);
    }
    return 0;
}
