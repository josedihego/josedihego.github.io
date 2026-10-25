// A1-2024.1 – Questão II: Cadeado de três rodas – menor número de movimentos
// teste: 152 971 => 5
// teste: 000 999 => 3
// teste: 555 555 => 0
#include <stdio.h>                                      // printf e scanf
#include <stdlib.h>                                     // abs

int main(void) {                                        // início do programa
    int atual, segredo;                                 // números de 3 dígitos
    printf("Número atual e segredo: ");                 // pede os dois números
    scanf("%d %d", &atual, &segredo);                   // lê os dois inteiros
    int total = 0;                                      // acumula os movimentos
    int d;                                              // diferença em uma roda
    d = abs(atual / 100 - segredo / 100);               // roda das centenas
    total += d < 10 - d ? d : 10 - d;                   // o menor caminho: para cima (d) ou para baixo (10 - d)
    d = abs((atual / 10) % 10 - (segredo / 10) % 10);   // roda das dezenas
    total += d < 10 - d ? d : 10 - d;                   // mesma regra
    d = abs(atual % 10 - segredo % 10);                 // roda das unidades
    total += d < 10 - d ? d : 10 - d;                   // mesma regra
    printf("Movimentos: %d\n", total);                  // 2 + 2 + 1 = 5 no exemplo
    return 0;                                           // fim sem erro
}
