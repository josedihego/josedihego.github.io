// A2-2025.1 – Questão II: Robô-espantalho – quantas vezes parou na estação devastada
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n, c, alvo;                                     // estações, comandos, estação mais próxima da área devastada
    scanf("%d %d %d", &n, &c, &alvo);                   // lê os três inteiros
    int estacao = 1;                                    // o robô começa o dia na estação 1
    int vezes = (estacao == alvo);                      // conta a estação inicial, se for o alvo
    for (int i = 0; i < c; i++) {                       // executa os c comandos
        int cmd;                                        // 1 = horário, -1 = anti-horário
        scanf("%d", &cmd);                              // lê o comando
        estacao = (estacao - 1 + cmd + n) % n + 1;      // anda no círculo 1..n (o + n evita resto negativo)
        if (estacao == alvo) vezes++;                   // parou no alvo
    }
    printf("%d\n", vezes);                              // 2 no exemplo
    return 0;                                           // fim sem erro
}
