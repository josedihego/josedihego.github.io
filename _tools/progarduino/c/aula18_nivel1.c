// Aula 18 – Nível 1: Tabuada completa (laço aninhado)
// teste: 
#include <stdio.h>                                     // printf

int main(void) {                                       // início do programa
    for (int linha = 1; linha <= 10; linha++) {        // laço de fora: linhas
        for (int coluna = 1; coluna <= 10; coluna++) { // laço de dentro: colunas
            printf("%4d", linha * coluna);             // %4d alinha em 4 posições
        }
        printf("\n");                                  // fim da linha
    }
    return 0;                                          // termina com sucesso
}
