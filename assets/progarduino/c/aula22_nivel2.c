// Aula 22 – Nível 2: Tanque com consumo
#include <stdio.h>                                              // printf

int main(void) {                                                // início do programa
    float nivel = 200;                                          // começa com 200 L
    for (int minuto = 1; minuto <= 30; minuto++) {              // simula 30 minutos
        nivel += 35;                                            // entra 35 L/min
        nivel -= (minuto % 10 < 5) ? 50 : 10;                   // consumo alto 5 min, baixo 5 min
        if (nivel > 500) nivel = 500;                           // não passa da capacidade
        if (nivel < 0) nivel = 0;                               // nem fica negativo
        printf("min %2d: %5.0f L\n", minuto, nivel);            // mostra minuto e nivel formatados
    }
    return 0;                                                   // termina com sucesso
}
