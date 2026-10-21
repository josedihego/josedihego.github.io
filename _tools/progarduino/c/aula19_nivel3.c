// Aula 19 – Nível 3: Cronômetro de processamento
// teste: 
#include <stdio.h>                                              // printf
#include <time.h>                                               // clock

int main(void) {                                                // início do programa
    clock_t inicio = clock();                                   // tempo de CPU no início
    double soma = 0;                                            // double: mais precisão que float
    for (long i = 1; i <= 50000000; i++) soma += 1.0 / i;      // trabalho pesado
    clock_t fim = clock();                                      // tempo de CPU no fim
    double segundos = (double)(fim - inicio) / CLOCKS_PER_SEC;  // converte para segundos
    printf("Soma = %.4f\n", soma);                              // mostra soma formatados
    printf("Levou %.3f s de processamento\n", segundos);        // mostra segundos formatados
    return 0;                                                   // termina com sucesso
}
