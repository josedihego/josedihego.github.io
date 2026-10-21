// Aula 16 – Nível 1: Contar pares de 1 a 50
#include <stdio.h>                         // printf

int main(void) {                           // início do programa
    int pares = 0;                         // contador
    for (int n = 1; n <= 50; n++) {        // n de 1 a 50
        if (n % 2 == 0) pares++;           // ++ soma 1
    }
    printf("Pares entre 1 e 50: %d\n", pares);   // mostra pares formatados
    return 0;                              // termina com sucesso
}
