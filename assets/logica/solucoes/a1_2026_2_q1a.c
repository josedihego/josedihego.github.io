// A1-2026.2 – Questão I: Ponto de término na pista circular
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    long c, n;                                          // distância do treino e comprimento da pista (metros)
    printf("C (metros do treino) e N (comprimento da pista): ");   // pede os dados
    scanf("%ld %ld", &c, &n);                           // %ld lê long (treinos longos cabem)
    printf("Deixe a garrafa a %ld metros da partida\n", c % n);    // voltas completas não importam: só o resto
    return 0;                                           // fim sem erro
}
