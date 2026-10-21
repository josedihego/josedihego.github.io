// Aula 32 – Nível 3: Jogo da velha
#include <stdio.h>                                                     // printf e scanf

char t[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};      // tabuleiro

void mostrar(void) {                                                   // desenha o tabuleiro
    for (int l = 0; l < 3; l++) printf(" %c | %c | %c \n%s", t[l][0], t[l][1], t[l][2], l < 2 ? "---+---+---\n" : "");   // uma linha do tabuleiro e o separador
}

int venceu(char j) {                                                   // 3 iguais numa linha, coluna ou diagonal
    for (int i = 0; i < 3; i++) {                                      // 3 voltas
        if (t[i][0] == j && t[i][1] == j && t[i][2] == j) return 1;    // linha i completa
        if (t[0][i] == j && t[1][i] == j && t[2][i] == j) return 1;    // coluna i completa
    }
    return (t[0][0] == j && t[1][1] == j && t[2][2] == j) || (t[0][2] == j && t[1][1] == j && t[2][0] == j);   // uma das duas diagonais
}

int main(void) {                                                       // início do programa
    char jogador = 'X';                                                // X começa
    for (int jogada = 0; jogada < 9; jogada++) {                       // no máximo 9 jogadas
        int l, c;                                                      // linha e coluna escolhidas
        printf("Vez de %c (linha coluna, 0 a 2): ", jogador);          // mostra jogador formatados
        if (scanf("%d %d", &l, &c) != 2) return 1;                     // entrada inválida encerra
        if (l < 0 || l > 2 || c < 0 || c > 2 || t[l][c] != ' ') { printf("Inválida\n"); jogada--; continue; }   // fora do tabuleiro ou ocupada: repete a vez
        t[l][c] = jogador;                                             // marca a casa
        mostrar();                                                     // atualiza a exibição
        if (venceu(jogador)) { printf("%c venceu!\n", jogador); return 0; }   // fim de jogo
        jogador = jogador == 'X' ? 'O' : 'X';                          // troca a vez
    }
    printf("Empate\n");                                                // mostra "Empate"
    return 0;                                                          // termina com sucesso
}
