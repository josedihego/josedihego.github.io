// A1-2024.1 (B) – Questão I: Collatz – quantos números até chegar a 1
// teste: 5 => 6
// teste: 1 => 1
// teste: 27 => 112
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    long n;                                             // long: a sequência sobe bastante antes de descer
    printf("Número: ");                                 // pede o número
    scanf("%ld", &n);                                   // lê o número
    int termos = 1;                                     // o próprio número já conta
    while (n != 1) {                                    // até chegar a 1
        if (n % 2 == 0) n = n / 2;                      // par: divide por 2
        else n = 3 * n + 1;                             // ímpar: 3n + 1
        termos++;                                       // mais um número na sequência
    }
    printf("%d números na sequência\n", termos);        // 5: 5, 16, 8, 4, 2, 1 → 6
    return 0;                                           // fim sem erro
}
