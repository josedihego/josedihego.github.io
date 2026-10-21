// Aula 3 – Nível 1: Ler um número
// teste: 17
#include <stdio.h>                               // printf e scanf

int main(void) {                                 // início do programa
    int idade;                                   // a variável recebe o valor digitado
    printf("Qual é a sua idade? ");              // pergunta
    scanf("%d", &idade);                         // %d lê um int; & indica onde guardar
    printf("Daqui a 10 anos você terá %d anos.\n", idade + 10);   // mostra idade + 10 formatados
    return 0;                                    // termina com sucesso
}
