// A4-2025.1 – Questão I: Alcance da lava do vulcão (mapa 8 x 8)
#include <stdio.h>                                      // printf e scanf
#define N 8                                             // mapa da prova

int main(void) {                                        // início do programa
    char mapa[N][N + 1];                                // altitudes '1' a '9' (cada linha é uma string)
    int forca;                                          // força da erupção (0 a 9)
    for (int i = 0; i < N; i++) scanf("%s", mapa[i]);   // lê as 8 linhas
    scanf("%d", &forca);                                // lê a força
    if (mapa[0][0] - '0' <= forca) mapa[0][0] = '*';    // a erupção começa no canto superior esquerdo
    int mudou = 1;                                      // repete enquanto a lava avançar
    while (mudou) {                                     // propagação até estabilizar
        mudou = 0;                                      // nada mudou nesta passada (ainda)
        for (int i = 0; i < N; i++) {                   // cada posição
            for (int j = 0; j < N; j++) {               // cada coluna
                if (mapa[i][j] == '*' || mapa[i][j] - '0' > forca) continue;   // já invadida ou alta demais
                int vizinho = (i > 0 && mapa[i - 1][j] == '*') || (i < N - 1 && mapa[i + 1][j] == '*') || // vizinho invadido acima ou abaixo...
                              (j > 0 && mapa[i][j - 1] == '*') || (j < N - 1 && mapa[i][j + 1] == '*');   // acima, abaixo, esquerda, direita
                if (vizinho) { mapa[i][j] = '*'; mudou = 1; }   // invadida a partir de um vizinho
            }
        }
    }
    for (int i = 0; i < N; i++) printf("%s\n", mapa[i]); // mapa final
    return 0;                                           // fim sem erro
}
