// A3-2025.1 – Questão II: Imagem RGB para tons de cinza (na prova, 100 x 100 x 3)
// teste: 1 1 200 150 100 => 159
// teste: 1 2 255 255 255 0 0 0 => 255 0
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // dimensão da prova

int img[MAX][MAX][3];                                   // global: 100 x 100 x 3 inteiros não cabem bem na pilha

int main(void) {                                        // início do programa
    int linhas, colunas;                                // dimensões (100 e 100 na prova)
    scanf("%d %d", &linhas, &colunas);                  // lê as dimensões
    for (int i = 0; i < linhas; i++)                    // cada pixel
        for (int j = 0; j < colunas; j++)               // cada coluna
            for (int c = 0; c < 3; c++) scanf("%d", &img[i][j][c]);   // canais R, G e B
    for (int i = 0; i < linhas; i++) {                  // imprime a imagem cinza
        for (int j = 0; j < colunas; j++) {             // cada coluna
            double cinza = 0.299 * img[i][j][0] + 0.587 * img[i][j][1] + 0.114 * img[i][j][2];   // luminância
            printf("%d ", (int)(cinza + 0.5));          // + 0.5 e truncar = arredondar
        }
        printf("\n");                                   // fim da linha
    }
    return 0;                                           // fim sem erro
}
