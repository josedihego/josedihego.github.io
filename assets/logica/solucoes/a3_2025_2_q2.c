// A3-2025.2 – Questão II: Areia movediça – tempo até o tesouro ou tipo de derrota
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // maior arena aceita

int main(void) {                                        // início do programa
    int m;                                              // dimensão da arena
    char mapa[MAX][MAX + 1];                            // cada linha é uma string (+1 para o '\0')
    int visitado[MAX][MAX] = {{0}};                     // marca as quadrículas já percorridas
    scanf("%d", &m);                                    // lê M
    for (int i = 0; i < m; i++) scanf("%s", mapa[i]);   // lê as M linhas (ex.: SSOS)
    int l, c;                                           // posição inicial (linha, coluna)
    scanf("%d %d", &l, &c);                             // lê a posição do pouso
    int minutos = 0;                                    // tempo decorrido
    while (1) {                                         // anda até um dos três desfechos
        if (l < 0 || l >= m || c < 0 || c >= m) { printf("Fora dos Limites\n"); break; }   // saiu da arena
        if (mapa[l][c] == 'X') { printf("Tesouro em %d minutos\n", minutos); break; }      // vitória
        if (visitado[l][c]) { printf("Preso na Areia\n"); break; }   // voltou a uma casa: ciclo para sempre
        visitado[l][c] = 1;                             // marca a casa atual
        char d = mapa[l][c];                            // direção do fluxo aqui
        if (d == 'N') l--;                              // norte: sobe uma linha
        else if (d == 'S') l++;                         // sul: desce
        else if (d == 'L') c++;                         // leste: direita
        else c--;                                       // oeste: esquerda
        minutos++;                                      // uma quadrícula por minuto
    }
    return 0;                                           // fim sem erro
}
