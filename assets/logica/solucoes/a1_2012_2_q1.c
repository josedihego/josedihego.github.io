// A1-2012.2 – Questão I: Octal (até 3 dígitos) para decimal
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número octal digitado como inteiro (ex.: 435)
    printf("Número octal: ");                           // pede o número
    scanf("%d", &n);                                    // lê o número
    int d2 = n / 100;                                   // dígito das centenas (4)
    int d1 = (n / 10) % 10;                             // dígito das dezenas (3)
    int d0 = n % 10;                                    // dígito das unidades (5)
    if (n < 0 || n > 777 || d2 > 7 || d1 > 7 || d0 > 7) {   // em octal só existem os dígitos 0 a 7
        printf("Número octal inválido\n");              // avisa e termina
        return 1;                                       // fim com erro
    }
    int decimal = d2 * 64 + d1 * 8 + d0;                // 4*8² + 3*8¹ + 5*8⁰
    printf("(%d)8 = (%d)10\n", n, decimal);             // mostra a conversão
    return 0;                                           // fim sem erro
}
