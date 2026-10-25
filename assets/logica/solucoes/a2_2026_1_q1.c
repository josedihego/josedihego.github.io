// A2-2026.1 – Questão I: Meia-vida – quando o paciente fica intoxicado tomando de 6 em 6 horas
#include <stdio.h>                                      // printf
#define DOSE 800.0                                      // mg por comprimido
#define LIMITE 1520.0                                   // acima disso: superdosagem

int main(void) {                                        // início do programa
    double teor = DOSE;                                 // primeira dose na hora 0
    int horas = 0;                                      // relógio do tratamento
    while (teor <= LIMITE) {                            // ainda não intoxicou
        horas += 6;                                     // passam 6 horas (uma meia-vida)
        teor = teor / 2 + DOSE;                         // metade foi metabolizada e entra nova dose
        printf("Hora %2d: %.0f mg\n", horas, teor);     // mostra a evolução: 1200, 1400, 1500, 1550
    }
    printf("Intoxicado em %d horas\n", horas);          // primeira vez acima de 1520 mg
    return 0;                                           // fim sem erro
}
