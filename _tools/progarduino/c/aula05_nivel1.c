// Aula 5 – Nível 1: Comparações valem 0 ou 1
// teste: 
#include <stdio.h>                         // printf

int main(void) {                                  // início do programa
    int tensao = 5;                        // valor de exemplo
    printf("tensao > 3  -> %d\n", tensao > 3);    // 1 = verdadeiro
    printf("tensao == 3 -> %d\n", tensao == 3);   // 0 = falso; == compara
    printf("tensao != 3 -> %d\n", tensao != 3);   // 1: != significa diferente
    printf("tensao <= 5 -> %d\n", tensao <= 5);   // 1
    return 0;                                     // termina com sucesso
}
