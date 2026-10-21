// Aula 32 – Nível 2: Leituras de 3 sensores por 4 horas
#include <stdio.h>                                                 // printf

int main(void) {                                                  // início do programa
    float t[3][4] = {{21.5, 22.0, 23.1, 22.8},                    // sensor 1, horas 1 a 4
                     {19.8, 20.4, 21.0, 20.7},                    // sensor 2
                     {24.2, 25.0, 25.9, 25.1}};                   // sensor 3
    for (int s = 0; s < 3; s++) {                                 // média de cada linha
        float soma = 0;                                           // acumulador
        for (int h = 0; h < 4; h++) soma += t[s][h];              // soma a linha do sensor s
        printf("Sensor %d: média %.2f\n", s + 1, soma / 4);       // mostra s + 1 e soma / 4 formatados
    }
    for (int h = 0; h < 4; h++) {                                 // média de cada coluna
        float soma = 0;                                           // acumulador
        for (int s = 0; s < 3; s++) soma += t[s][h];              // soma a coluna da hora h
        printf("Hora %d: média %.2f\n", h + 1, soma / 3);         // mostra h + 1 e soma / 3 formatados
    }
    return 0;                                                     // termina com sucesso
}
