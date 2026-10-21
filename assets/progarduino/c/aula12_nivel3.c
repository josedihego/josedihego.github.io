// Aula 12 – Nível 3: Revisão: byte em binário
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int n;                                               // valor de 0 a 255
    printf("Valor (0 a 255): ");                         // pergunta ao usuário
    scanf("%d", &n);                                     // lê o valor digitado e guarda em n
    printf("%d = ", n);                                  // mostra n formatados
    printf("%d%d%d%d ", n >> 7 & 1, n >> 6 & 1, n >> 5 & 1, n >> 4 & 1);   // 4 bits mais altos
    printf("%d%d%d%d\n", n >> 3 & 1, n >> 2 & 1, n >> 1 & 1, n & 1);       // 4 bits mais baixos
    return 0;                                            // termina com sucesso
}
