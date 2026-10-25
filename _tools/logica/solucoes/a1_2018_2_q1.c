// A1-2018.2 – Questão I: Quantos dígitos 1 tem o binário de um número entre 0 e 32
// teste: 7 => 3
// teste: 32 => 1
// teste: 31 => 5
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número entre 0 e 32 (cabe em 6 bits)
    printf("Número (0 a 32): ");                        // pede o número
    scanf("%d", &n);                                    // lê o número
    int uns = n % 2                                     // bit de peso 1
            + (n / 2) % 2                               // bit de peso 2
            + (n / 4) % 2                               // bit de peso 4
            + (n / 8) % 2                               // bit de peso 8
            + (n / 16) % 2                              // bit de peso 16
            + (n / 32) % 2;                             // bit de peso 32
    printf("%d dígito(s) 1\n", uns);                    // cada bit vale 0 ou 1: somar conta os uns
    return 0;                                           // fim sem erro
}
