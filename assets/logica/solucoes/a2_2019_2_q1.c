// A2-2019.2 – Questão I: Quantas subsequências consecutivas somam exatamente X
#include <stdio.h>                                      // printf e scanf
#define MAX 1000                                        // tamanho máximo da sequência

int main(void) {                                        // início do programa
    int n, x;                                           // tamanho da sequência e soma procurada
    int v[MAX];                                         // a sequência
    scanf("%d", &n);                                    // lê N
    for (int i = 0; i < n; i++) scanf("%d", &v[i]);     // lê os N números
    scanf("%d", &x);                                    // lê X
    int quantas = 0;                                    // contador de subsequências
    for (int ini = 0; ini < n; ini++) {                 // cada ponto de partida
        int soma = 0;                                   // soma de v[ini..fim]
        for (int fim = ini; fim < n; fim++) {           // estende a subsequência um elemento por vez
            soma += v[fim];                             // aproveita a soma anterior
            if (soma == x) quantas++;                   // achou uma
        }
    }
    printf("%d subsequências\n", quantas);              // 5 no exemplo
    return 0;                                           // fim sem erro
}
