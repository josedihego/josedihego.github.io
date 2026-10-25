// A3-2026.1 – Questão I: Rotação de 90 graus no sentido horário (na prova, N = 50)
// teste: 2 1 2 3 4 => 3 1
// teste: 2 1 2 3 4 => 4 2
// teste: 3 1 2 3 4 5 6 7 8 9 => 7 4 1
#include <stdio.h>                                      // printf e scanf
#define MAX 50                                          // dimensão da prova

int main(void) {                                        // início do programa
    int n, img[MAX][MAX];                               // dimensão e imagem em tons de cinza
    scanf("%d", &n);                                    // lê N
    for (int i = 0; i < n; i++)                         // lê a imagem linha a linha
        for (int j = 0; j < n; j++) scanf("%d", &img[i][j]); // cada coluna
    for (int i = 0; i < n; i++) {                       // linha i da imagem girada
        for (int j = 0; j < n; j++)                     // coluna j da imagem girada
            printf("%d ", img[n - 1 - j][i]);           // vem da coluna i, lida de baixo para cima
        printf("\n");                                   // fim da linha
    }
    return 0;                                           // fim sem erro
}
