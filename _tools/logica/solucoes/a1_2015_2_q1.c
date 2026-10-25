// A1-2015.2 – Questão I: Soma dos dígitos centrais de um número de 4 dígitos
// teste: 4326 => 5
// teste: 1090 => 9
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número menor que 9999
    printf("Número: ");                                 // pede o número
    scanf("%d", &n);                                    // lê o número
    int segundo = (n / 100) % 10;                       // 4326 / 100 = 43; 43 % 10 = 3
    int terceiro = (n / 10) % 10;                       // 4326 / 10 = 432; 432 % 10 = 2
    printf("Soma dos dígitos centrais: %d\n", segundo + terceiro);   // 3 + 2 = 5
    return 0;                                           // fim sem erro
}
