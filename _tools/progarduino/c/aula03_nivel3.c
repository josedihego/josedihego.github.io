// Aula 3 – Nível 3: Lei de Ohm e potência
// teste: 12; 470
#include <stdio.h>                                            // printf e scanf

int main(void) {                                              // início do programa
    float tensao, resistencia;                                // entradas
    printf("Tensão da fonte (V): ");                          // pergunta ao usuário
    scanf("%f", &tensao);                                     // lê o valor digitado e guarda em tensao
    printf("Resistência (ohms): ");                           // pergunta ao usuário
    scanf("%f", &resistencia);                                // lê o valor digitado e guarda em resistencia
    float corrente = tensao / resistencia;                    // I = V / R
    float potencia = tensao * corrente;                       // P = V × I
    printf("Corrente: %.4f A (%.1f mA)\n", corrente, corrente * 1000);   // em ampères e miliampères
    printf("Potência: %.4f W\n", potencia);                   // mostra potencia formatados
    return 0;                                                 // termina com sucesso
}
