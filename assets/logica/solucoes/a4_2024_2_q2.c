// A4-2024.2 – Questão II: Plano de construção da pirâmide
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // dimensão máxima

int main(void) {                                        // início do programa
    int n, plano[MAX][MAX];                             // dimensão e plano de construção
    scanf("%d", &n);                                    // lê a dimensão
    for (int i = 0; i < n; i++) {                       // cada posição da base
        for (int j = 0; j < n; j++) {                   // cada coluna
            int borda = i;                              // distância até a borda mais próxima
            if (j < borda) borda = j;                   // borda esquerda
            if (n - 1 - i < borda) borda = n - 1 - i;   // borda de baixo
            if (n - 1 - j < borda) borda = n - 1 - j;   // borda direita
            plano[i][j] = borda + 1;                    // cada camada recua uma casa: altura = distância + 1
        }
    }
    for (int i = 0; i < n; i++) {                       // imprime o plano
        for (int j = 0; j < n; j++) printf("%d ", plano[i][j]); // valores separados por espaço
        printf("\n");                                   // fim da linha
    }
    return 0;                                           // fim sem erro
}
