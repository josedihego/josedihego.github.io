// Aula 17 – Nível 1: Jogar um dado
// teste: 
#include <stdio.h>                                   // printf
#include <stdlib.h>                                  // rand e srand
#include <time.h>                                    // time

int main(void) {                                     // início do programa
    srand(time(NULL));                               // semente diferente a cada execução
    int dado = rand() % 6 + 1;                       // rand() % 6 dá 0..5; +1 dá 1..6
    printf("Saiu %d\n", dado);                       // mostra dado formatados
    return 0;                                        // termina com sucesso
}
