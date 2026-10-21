// Aula 22 – Nível 3: Bomba com histerese
// teste: 
#include <stdio.h>                                                    // printf

int main(void) {                                                      // início do programa
    float nivel = 300;                                                // litros
    int bomba = 0;                                                    // 0 = desligada, 1 = ligada
    for (int minuto = 1; minuto <= 40; minuto++) {                    // simula 40 minutos
        if (nivel < 150) bomba = 1;                                   // liga abaixo de 30%
        else if (nivel > 450) bomba = 0;                              // desliga acima de 90%
        nivel += bomba * 40 - 20;                                     // bomba: +40 L/min; consumo: 20 L/min
        printf("min %2d: %5.0f L  bomba %s\n", minuto, nivel, bomba ? "LIGADA" : "desligada");   // mostra os valores formatados
    }
    return 0;                                                         // termina com sucesso
}
