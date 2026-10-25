// A1-2024.2 (D) – Questão II: Liga do Reizinho – pontos somando min + max de cada janela
#include <stdio.h>                                      // printf e scanf
#define P 5                                             // partidas do campeonato atual
#define J 3                                             // tamanho da janela

int main(void) {                                        // início do programa
    int gols[P];                                        // gols em cada partida
    for (int i = 0; i < P; i++) scanf("%d", &gols[i]);  // lê os gols
    int total = 0;                                      // pontuação acumulada
    for (int ini = 0; ini <= P - J; ini++) {            // P - J + 1 janelas
        int min = gols[ini], max = gols[ini];           // começa com o primeiro jogo da janela
        for (int k = ini + 1; k < ini + J; k++) {       // demais jogos da janela
            if (gols[k] < min) min = gols[k];           // menor da janela
            if (gols[k] > max) max = gols[k];           // maior da janela
        }
        total += min + max;                             // pontos desta janela
    }
    printf("%d pontos\n", total);                       // (1+3) + (1+3) + (1+4) = 13 no exemplo
    return 0;                                           // fim sem erro
}
