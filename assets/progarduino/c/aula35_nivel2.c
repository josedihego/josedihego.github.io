// Aula 35 – Nível 2: Simulado: função que conta
#include <stdio.h>                                     // printf

int conta_acima(int v[], int n, int limite) {          // quantos valores passam do limite
    int c = 0;                                         // contador
    for (int i = 0; i < n; i++) if (v[i] > limite) c++;   // conta os que passam do limite
    return c;                                          // devolve a contagem
}

int main(void) {                                       // início do programa
    int leituras[] = {610, 480, 720, 300, 655, 590};   // leituras de exemplo
    printf("Acima de 600: %d\n", conta_acima(leituras, 6, 600));   // mostra conta_acima(leituras e 6 e 600) formatados
    return 0;                                          // termina com sucesso
}
