// Aula 8 – Nível 2: Binário de 5 bits para decimal
// teste: 1; 0; 1; 1; 0
#include <stdio.h>                                               // printf e scanf

int main(void) {                                                 // início do programa
    int b4, b3, b2, b1, b0;                                      // bits, do mais significativo ao menos
    printf("Bits b4 b3 b2 b1 b0 (separados por espaço): ");      // pergunta ao usuário
    scanf("%d %d %d %d %d", &b4, &b3, &b2, &b1, &b0);            // lê o valor digitado e guarda em b4, b3, b2, b1, b0
    int decimal = b4 * 16 + b3 * 8 + b2 * 4 + b1 * 2 + b0 * 1;   // soma dos pesos
    printf("%d%d%d%d%d = %d em decimal\n", b4, b3, b2, b1, b0, decimal);   // mostra os valores formatados
    return 0;                                                    // termina com sucesso
}
