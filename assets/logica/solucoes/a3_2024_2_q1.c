// A3-2024.2 – Questão I: Max pooling com filtro F x F e passo F
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // maior imagem aceita

int main(void) {                                        // início do programa
    int n, f, img[MAX][MAX];                            // dimensão da imagem, do filtro e a imagem
    scanf("%d %d", &n, &f);                             // lê N e F (N múltiplo de F)
    for (int i = 0; i < n; i++)                         // lê a imagem
        for (int j = 0; j < n; j++) scanf("%d", &img[i][j]); // cada coluna
    for (int bi = 0; bi < n; bi += f) {                 // linha de início de cada bloco (passo F)
        for (int bj = 0; bj < n; bj += f) {             // coluna de início de cada bloco
            int maior = img[bi][bj];                    // começa com o canto do bloco
            for (int i = bi; i < bi + f; i++)           // percorre o bloco F x F
                for (int j = bj; j < bj + f; j++)       // colunas do bloco
                    if (img[i][j] > maior) maior = img[i][j];   // guarda o máximo
            printf("%d ", maior);                       // um valor por bloco
        }
        printf("\n");                                   // fim de uma linha de blocos
    }
    return 0;                                           // fim sem erro
}
