// Aula 22 – Nível 1: Tanque enchendo
#include <stdio.h>                                       // printf

int main(void) {                                         // início do programa
    float nivel = 0;                                     // litros
    int minuto = 0;                                      // contador de minutos
    while (nivel < 500) {                                // capacidade: 500 L
        nivel += 35;                                     // bomba: 35 L/min
        minuto++;                                        // passou um minuto
        printf("min %2d: %5.0f L\n", minuto, nivel);     // mostra minuto e nivel formatados
    }
    printf("Cheio em %d minutos\n", minuto);             // mostra minuto formatados
    return 0;                                            // termina com sucesso
}
