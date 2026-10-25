// A1-2015.2 (B) – Questão I: Desconto previdenciário com teto
// teste: 2000 => 220.00
// teste: 10000 => 570.88
#include <stdio.h>                                      // printf e scanf
#define TETO 570.88                                     // desconto máximo

int main(void) {                                        // início do programa
    double salario;                                     // salário lido
    printf("Salário: ");                                // pede o salário
    scanf("%lf", &salario);                             // lê o salário
    double desconto = salario * 0.11;                   // 11% do salário
    if (desconto > TETO) desconto = TETO;               // passou do teto: fica no teto
    printf("Desconto: R$ %.2f\n", desconto);            // valor final do desconto
    return 0;                                           // fim sem erro
}
