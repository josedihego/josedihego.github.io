// Aula 2 – Nível 1: Três tipos de variável
#include <stdio.h>                               // printf

int main(void) {                                 // início do programa
    int quantidade = 12;                         // int: número inteiro
    float tensao = 4.75;                         // float: número com casas decimais
    char letra = 'A';                            // char: um caractere, entre aspas simples
    printf("Quantidade: %d\n", quantidade);      // %d mostra um int
    printf("Tensão: %.2f V\n", tensao);          // %.2f mostra um float com 2 casas
    printf("Letra: %c\n", letra);                // %c mostra um char
    return 0;                                    // termina com sucesso
}
