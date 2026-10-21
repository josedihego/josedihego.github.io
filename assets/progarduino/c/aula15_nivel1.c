// Aula 15 – Nível 1: Somar até chegar a 42
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int soma = 0, valor;                                 // acumulador e valor lido
    while (soma < 42) {                                  // repete ENQUANTO a soma for menor que 42
        printf("Valor: ");                               // pergunta ao usuário
        scanf("%d", &valor);                             // lê o valor digitado e guarda em valor
        soma += valor;                                   // acumula o valor lido
    }
    printf("Soma = %d (chegou a 42 ou passou)\n", soma);   // mostra soma formatados
    return 0;                                            // termina com sucesso
}
