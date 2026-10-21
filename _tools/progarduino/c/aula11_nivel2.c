// Aula 11 – Nível 2: Simulado: classificar a corrente
// teste: 0.35
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    float corrente;                                      // em ampères
    printf("Corrente (A): ");                            // pergunta ao usuário
    scanf("%f", &corrente);                              // lê o valor digitado e guarda em corrente
    if (corrente < 0.02) printf("Baixa (LED)\n");        // até 20 mA
    else if (corrente < 0.5) printf("Média (motor pequeno)\n");   // de 20 a 500 mA
    else printf("Alta: use um transistor ou relé\n");    // 500 mA ou mais
    return 0;                                            // termina com sucesso
}
