// Aula 12 – Nível 1: Revisão: média de duas leituras
#include <stdio.h>                               // printf e scanf

int main(void) {                                 // início do programa
    float l1, l2;                                // duas leituras de tensão
    printf("Leituras (V): ");                    // pergunta ao usuário
    scanf("%f %f", &l1, &l2);                    // lê o valor digitado e guarda em l1, l2
    printf("Média: %.2f V\n", (l1 + l2) / 2);    // parênteses: soma antes de dividir
    return 0;                                    // termina com sucesso
}
