// A2-2024.2 – Questão I: Tempo para o material radioativo chegar à massa final
// teste: 100 50 => 7 minutos
// teste: 1000 1000 => 0 minutos
// teste: 80 10 => 20 minutos
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    double massa, final;                                // massa inicial e massa final desejada
    printf("Massa inicial e massa final: ");            // pede os dados
    scanf("%lf %lf", &massa, &final);                   // lê os dois valores
    int minutos = 0;                                    // contador de minutos
    while (massa > final) {                             // ainda acima da massa desejada
        massa = massa * 0.9;                            // perde 10% por minuto: sobra 90%
        minutos++;                                      // passou um minuto
    }
    printf("Tempo necessário: %d minutos (massa = %.2f)\n", minutos, massa);   // resultado
    return 0;                                           // fim sem erro
}
