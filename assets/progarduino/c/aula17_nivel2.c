// Aula 17 – Nível 2: Jogo de contas até errar
#include <stdio.h>                                          // printf e scanf
#include <stdlib.h>                                         // rand e srand
#include <time.h>                                           // time

int main(void) {                                            // início do programa
    srand(time(NULL));                                      // embaralha a sequência
    int acertos = 0, acertou = 1;                           // placar e controle do laço
    while (acertou) {                                       // repete enquanto acertar
        int a = rand() % 10, b = rand() % 10;               // números de 0 a 9
        int resposta;                                       // declara resposta (int)
        printf("%d + %d = ", a, b);                         // mostra a e b formatados
        if (scanf("%d", &resposta) != 1) break;             // entrada inválida encerra
        if (resposta == a + b) acertos++;                   // acertou: soma ponto
        else acertou = 0;                                   // errou: sai do laço
    }
    printf("Você acertou %d contas seguidas\n", acertos);   // mostra acertos formatados
    return 0;                                               // termina com sucesso
}
