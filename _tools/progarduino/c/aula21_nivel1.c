// Aula 21 – Nível 1: A conta do map
// teste: 512
#include <stdio.h>                                                     // printf e scanf

int main(void) {                                                       // início do programa
    long leitura;                                                      // valor do conversor (0 a 1023)
    printf("Leitura (0 a 1023): ");                                    // pergunta ao usuário
    scanf("%ld", &leitura);                                            // lê o valor digitado e guarda em leitura
    long porcento = (leitura - 0) * (100 - 0) / (1023 - 0) + 0;        // a mesma fórmula do map() do Arduino
    printf("%ld -> %ld%%\n", leitura, porcento);                       // mostra leitura e porcento formatados
    return 0;                                                          // termina com sucesso
}
