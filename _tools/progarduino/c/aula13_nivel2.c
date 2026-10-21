// Aula 13 – Nível 2: Soma dos ímpares
// teste: 
#include <stdio.h>                         // printf

int main(void) {                           // início do programa
    int soma = 0;                          // acumulador começa em zero
    for (int i = 1; i < 200; i = i + 2) {  // 1, 3, 5, ..., 199
        soma = soma + i;                   // acrescenta o ímpar
    }
    printf("Soma dos ímpares até 199 = %d\n", soma);   // 10000
    return 0;                              // termina com sucesso
}
