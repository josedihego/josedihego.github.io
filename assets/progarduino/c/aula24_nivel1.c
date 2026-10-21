// Aula 24 – Nível 1: Revisão: contagem de 10 em 10
#include <stdio.h>                                  // printf

int main(void) {                                           // início do programa
    for (int i = 100; i >= 0; i -= 10) printf("%d ", i);   // passo negativo
    printf("\n");                                          // quebra a linha
    return 0;                                              // termina com sucesso
}
