// A1-2026.2 – Questão I: Zip – quem ganhou a partida?
#include <stdio.h>                                      // printf e scanf
#include <stdlib.h>                                     // abs

int main(void) {                                        // início do programa
    int a, b, c, d;                                     // cartas de Lia (a, b) e de Mia (c, d)
    printf("Cartas de Lia e de Mia: ");                 // pede as quatro cartas
    scanf("%d %d %d %d", &a, &b, &c, &d);               // lê as quatro cartas
    int lia = a + b;                                    // pontuação básica: a soma
    if (a == b) lia = lia * 2;                          // cartas iguais: dobra
    else if (abs(a - b) == 1) lia = lia * 3;            // consecutivas (diferença 1): triplica
    int mia = c + d;                                    // a mesma regra para Mia
    if (c == d) mia = mia * 2;                          // cartas iguais
    else if (abs(c - d) == 1) mia = mia * 3;            // consecutivas
    if (lia > mia) printf("Lia\n");                     // maior pontuação vence
    else if (mia > lia) printf("Mia\n");                // idem
    else printf("empate\n");                            // iguais: aposta acumula
    return 0;                                           // fim sem erro
}
