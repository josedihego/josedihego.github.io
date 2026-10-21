// Aula 15 – Nível 2: Treino para a maratona
#include <stdio.h>                                            // printf
#define MARATONA 42195                                        // metros

int main(void) {                                              // início do programa
    float distancia = 5000;                                   // primeiro treino: 5 km
    int dia = 1;                                              // contador de dias
    while (distancia < MARATONA) {                            // número de repetições desconhecido: while
        distancia = distancia * 1.10;                         // cada treino é 10% maior
        dia = dia + 3;                                        // treina a cada 3 dias
    }
    printf("Primeira maratona no dia %d (%.0f m)\n", dia, distancia);   // mostra dia e distancia formatados
    return 0;                                                 // termina com sucesso
}
