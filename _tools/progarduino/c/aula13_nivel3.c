// Aula 13 – Nível 3: Tabela de resistores em série
// teste: 220
#include <stdio.h>                                              // printf e scanf

int main(void) {                                                // início do programa
    float r;                                                    // valor de cada resistor
    printf("Valor de um resistor (ohms): ");                    // pergunta ao usuário
    scanf("%f", &r);                                            // lê o valor digitado e guarda em r
    printf("Qtd | Série (ohms) | Paralelo (ohms)\n");           // cabeçalho da tabela
    for (int n = 1; n <= 6; n++) {                              // de 1 a 6 resistores iguais
        printf("%3d | %12.1f | %15.2f\n", n, n * r, r / n);     // %3d, %12.1f: largura fixa alinha as colunas
    }
    return 0;                                                   // termina com sucesso
}
