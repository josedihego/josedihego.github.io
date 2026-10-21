// Aula 17 – Nível 3: Pedra, papel e tesoura
#include <stdio.h>                                                    // printf e scanf
#include <stdlib.h>                                                   // rand e srand
#include <time.h>                                                     // time
#define PEDRA 0                                                       // constante PEDRA = 0
#define PAPEL 1                                                       // constante PAPEL = 1
#define TESOURA 2                                                     // constante TESOURA = 2

int main(void) {                                                      // início do programa
    srand(time(NULL));                                                // semente diferente a cada execução
    int jogador, computador = rand() % 3;                             // 0, 1 ou 2
    printf("0-Pedra 1-Papel 2-Tesoura: ");                            // pergunta ao usuário
    scanf("%d", &jogador);                                            // lê o valor digitado e guarda em jogador
    printf("Computador jogou %d\n", computador);                      // mostra computador formatados
    if (jogador == computador) printf("Empate\n");                    // jogadas iguais
    else if ((jogador == PEDRA && computador == TESOURA) ||           // regras de vitória
             (jogador == PAPEL && computador == PEDRA) ||             // papel embrulha pedra
             (jogador == TESOURA && computador == PAPEL)) printf("Você ganhou!\n");   // tesoura corta papel
    else printf("Computador ganhou\n");                               // qualquer outro caso
    return 0;                                                         // termina com sucesso
}
