// Aula 13 – Nível 1: Contar de 0 a 9
// teste: 
#include <stdio.h>                         // printf

int main(void) {                           // início do programa
    for (int i = 0; i < 10; i++) {         // começa em 0, repete enquanto i < 10, soma 1 a cada volta
        printf("%d\n", i);                 // corpo do laço
    }
    printf("Fim\n");                       // fora do laço: executa uma vez
    return 0;                              // termina com sucesso
}
