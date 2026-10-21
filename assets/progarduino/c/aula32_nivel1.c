// Aula 32 – Nível 1: Matriz 3 × 3
#include <stdio.h>                                          // printf

int main(void) {                                            // início do programa
    int m[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};        // 3 linhas, 3 colunas
    for (int l = 0; l < 3; l++) {                           // percorre as linhas
        for (int c = 0; c < 3; c++) printf("%3d", m[l][c]); // m[linha][coluna]
        printf("\n");                                       // quebra a linha
    }
    printf("Diagonal: %d %d %d\n", m[0][0], m[1][1], m[2][2]);   // mostra m[0][0] e m[1][1] e m[2][2] formatados
    return 0;                                               // termina com sucesso
}
