// Aula 11 – Nível 1: Simulado: conversão de unidades
// teste: 2.2
#include <stdio.h>                                   // printf e scanf

int main(void) {                                     // início do programa
    float kohms;                                     // valor em quilo-ohms
    printf("Resistência (kohms): ");                 // pergunta ao usuário
    scanf("%f", &kohms);                             // lê o valor digitado e guarda em kohms
    printf("%.1f kohms = %.0f ohms\n", kohms, kohms * 1000);   // mostra kohms e kohms * 1000 formatados
    return 0;                                        // termina com sucesso
}
