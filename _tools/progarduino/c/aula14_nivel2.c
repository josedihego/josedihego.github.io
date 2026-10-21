// Aula 14 – Nível 2: Juros compostos
// teste: 1000; 1; 12
#include <stdio.h>                                         // printf e scanf

int main(void) {                                           // início do programa
    float valor, taxa;                                     // capital e taxa mensal (%)
    int meses;                                             // período
    printf("Valor, taxa ao mês (%%) e meses: ");           // pergunta ao usuário (%% escreve %)
    scanf("%f %f %d", &valor, &taxa, &meses);              // lê o valor digitado e guarda em valor, taxa, meses
    for (int m = 1; m <= meses; m++) {                     // um passo por mês
        valor = valor * (1 + taxa / 100);                  // o juro incide sobre o valor acumulado
        printf("Mês %2d: R$ %.2f\n", m, valor);            // mostra m e valor formatados
    }
    return 0;                                              // termina com sucesso
}
