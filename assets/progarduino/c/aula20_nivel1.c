// Aula 20 – Nível 1: Do tempo de eco à distância
#include <stdio.h>                                              // printf e scanf

int main(void) {                                                // início do programa
    float tempo_us;                                             // tempo de ida e volta do som (µs)
    printf("Tempo de eco (microssegundos): ");                  // pergunta ao usuário
    scanf("%f", &tempo_us);                                     // lê o valor digitado e guarda em tempo_us
    float distancia = tempo_us * 0.0343 / 2;                    // som: 0,0343 cm/µs; ida e volta: ÷ 2
    printf("Distância: %.1f cm\n", distancia);                  // mostra distancia formatados
    return 0;                                                   // termina com sucesso
}
