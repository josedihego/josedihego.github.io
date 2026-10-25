// A3-2023.1 – Questão I: Caça-palavras (horizontal e vertical) – pontuação
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // maior grade aceita

int main(void) {                                        // início do programa
    int m, n;                                           // linhas e colunas da grade
    char g[MAX][MAX + 1], palavra[MAX + 1];             // grade e palavra procurada
    scanf("%d %d", &m, &n);                             // lê as dimensões
    for (int i = 0; i < m; i++) scanf("%s", g[i]);      // lê as linhas da grade
    scanf("%s", palavra);                               // lê a palavra
    int t = 0, achou = 0;                               // tamanho da palavra e resultado
    while (palavra[t] != '\0') t++;                     // conta as letras até o '\0'
    for (int i = 0; i < m && !achou; i++) {             // cada posição inicial
        for (int j = 0; j < n && !achou; j++) {         // (para assim que achar)
            int h = j + t <= n, v = i + t <= m;         // cabe na horizontal? na vertical?
            for (int k = 0; k < t; k++) {               // compara letra a letra
                if (h && g[i][j + k] != palavra[k]) h = 0;   // falhou na horizontal (anda pela coluna)
                if (v && g[i + k][j] != palavra[k]) v = 0;   // falhou na vertical (anda pela linha)
            }
            if (h || v) achou = 1;                      // encontrou em alguma direção
        }
    }
    printf("%d pontos\n", achou ? t : -5);              // tamanho da palavra ou -5
    return 0;                                           // fim sem erro
}
