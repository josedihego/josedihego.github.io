// Aula 8 – Nível 1: Decimal para 4 bits
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int n;                                               // número de 0 a 15
    printf("Número (0 a 15): ");                         // pergunta ao usuário
    scanf("%d", &n);                                     // lê o valor digitado e guarda em n
    int b3 = n / 8 % 2;                                  // bit de peso 8
    int b2 = n / 4 % 2;                                  // bit de peso 4
    int b1 = n / 2 % 2;                                  // bit de peso 2
    int b0 = n % 2;                                      // bit de peso 1
    printf("%d em binário: %d%d%d%d\n", n, b3, b2, b1, b0);   // mostra os valores formatados
    return 0;                                            // termina com sucesso
}
