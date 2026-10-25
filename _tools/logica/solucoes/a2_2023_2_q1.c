// A2-2023.2 – Questão I: O chefe ao telefone – "zero" apaga o último número
// teste: 1 3 5 4 0 0 7 0 0 6 -1 => 7
// teste: 10 20 30 -1 => 60
// teste: 5 0 -1 => 0
#include <stdio.h>                                      // printf e scanf
#define MAX 1000                                        // vendas que cabem na "pilha"

int main(void) {                                        // início do programa
    int pilha[MAX];                                     // números ainda válidos
    int topo = 0;                                       // quantos números estão na pilha
    int x;                                              // número falado
    scanf("%d", &x);                                    // primeira leitura
    while (x >= 0) {                                    // negativo encerra a lista
        if (x == 0) {                                   // "zero": apaga o último número
            if (topo > 0) topo--;                       // só se houver algum
        } else {                                        // número de venda
            pilha[topo++] = x;                          // empilha
        }
        scanf("%d", &x);                                // próxima leitura
    }
    int soma = 0;                                       // total das vendas
    for (int i = 0; i < topo; i++) soma += pilha[i];    // soma o que sobrou na pilha
    printf("%d\n", soma);                               // 1 + 6 = 7 no exemplo
    return 0;                                           // fim sem erro
}
