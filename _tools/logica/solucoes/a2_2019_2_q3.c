// A2-2019.2 – Questão III: sigma(n), a soma dos divisores, para n de 1 a N
// teste: 10 => 1, 3, 4, 7, 6, 12, 8, 15, 13, 18
// teste: 1 => 1
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // limite N
    printf("N: ");                                      // pede N
    scanf("%d", &n);                                    // lê N
    for (int k = 1; k <= n; k++) {                      // laço de fora: cada k da lista
        int sigma = 0;                                  // soma dos divisores de k
        for (int d = 1; d <= k; d++) {                  // laço de dentro: candidatos a divisor
            if (k % d == 0) sigma += d;                 // d divide k: soma
        }
        printf("%d%s", sigma, k < n ? ", " : "\n");     // vírgula entre os termos, quebra no fim
    }
    return 0;                                           // fim sem erro
}
