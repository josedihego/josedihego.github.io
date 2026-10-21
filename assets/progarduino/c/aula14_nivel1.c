// Aula 14 – Nível 1: Soma de 1 a 100
#include <stdio.h>                         // printf

int main(void) {                           // início do programa
    int soma = 0;                          // acumulador
    for (int n = 1; n <= 100; n++) {       // de 1 a 100
        soma += n;                         // += é o mesmo que soma = soma + n
    }
    printf("Soma = %d\n", soma);           // 5050
    return 0;                              // termina com sucesso
}
