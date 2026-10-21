// Aula 6 – Nível 1: Par ou ímpar
// teste: 7
#include <stdio.h>                         // printf e scanf

int main(void) {                           // início do programa
    int numero;                            // número lido
    printf("Número inteiro: ");            // pergunta ao usuário
    scanf("%d", &numero);                  // lê o valor digitado e guarda em numero
    if (numero % 2 == 0) {                 // resto zero na divisão por 2?
        printf("%d é par\n", numero);      // bloco do if
    } else {                               // caso contrário
        printf("%d é ímpar\n", numero);    // bloco do else
    }
    return 0;                              // termina com sucesso
}
