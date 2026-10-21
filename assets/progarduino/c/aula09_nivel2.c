// Aula 9 – Nível 2: Conversões com const
#include <stdio.h>                                        // printf

int main(void) {                                          // início do programa
    const float POLEGADA_MM = 25.4;                       // const: o valor não pode mudar
    const int BITS_ADC = 10;                              // resolução do conversor do Arduino
    int niveis = 1 << BITS_ADC;                           // 2^10 = 1024 níveis
    printf("3 polegadas = %.1f mm\n", 3 * POLEGADA_MM);   // mostra 3 * POLEGADA_MM formatados
    printf("ADC de %d bits: %d níveis (0 a %d)\n", BITS_ADC, niveis, niveis - 1);   // mostra BITS_ADC e niveis e niveis - 1 formatados
    printf("Resolução com 5 V: %.2f mV\n", 5000.0 / (niveis - 1));   // mostra 5000.0 / (niveis - 1) formatados
    return 0;                                             // termina com sucesso
}
