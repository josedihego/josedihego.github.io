// A2-2025.2 – Questão II: Maior sequência de valores consecutivos iguais
#include <stdio.h>                                      // printf e scanf
#define N 11                                            // quantidade de números sorteados

int main(void) {                                        // início do programa
    int v[N];                                           // vetor com os 11 números
    for (int i = 0; i < N; i++) scanf("%d", &v[i]);     // lê os 11 valores
    int atual = 1, maior = 1;                           // tamanho da sequência atual e da maior até agora
    for (int i = 1; i < N; i++) {                       // compara cada valor com o anterior
        if (v[i] == v[i - 1]) atual++;                  // igual ao anterior: a sequência cresce
        else atual = 1;                                 // diferente: começa uma nova sequência
        if (atual > maior) maior = atual;               // guarda o recorde
    }
    printf("%d pontos\n", maior);                       // tamanho da maior sequência
    return 0;                                           // fim sem erro
}
