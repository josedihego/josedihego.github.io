// Aula 3 – Nível 2: Resistores em série e em paralelo
#include <stdio.h>                                          // printf e scanf

int main(void) {                                            // início do programa
    float r1, r2;                                           // duas resistências em ohms
    printf("Valor de R1 (ohms): ");                         // pergunta ao usuário
    scanf("%f", &r1);                                       // %f lê um float
    printf("Valor de R2 (ohms): ");                         // pergunta ao usuário
    scanf("%f", &r2);                                       // lê o valor digitado e guarda em r2
    float serie = r1 + r2;                                  // série: soma
    float paralelo = (r1 * r2) / (r1 + r2);                 // paralelo: produto ÷ soma
    printf("Série: %.2f ohms\n", serie);                    // mostra serie formatados
    printf("Paralelo: %.2f ohms\n", paralelo);              // mostra paralelo formatados
    return 0;                                               // termina com sucesso
}
