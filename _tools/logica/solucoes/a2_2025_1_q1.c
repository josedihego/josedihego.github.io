// A2-2025.1 – Questão I: Cofre – quantas vezes cada dígito passa pelo controle
// teste: 1 9 4 11 13 0 => 1 6 3 1 4 3 0 1 0 4
// teste: 1 0 => 0 0 0 0 0 0 0 0 0 1
// teste: 1 14 0 => 1 3 1 1 2 2 0 1 0 3
#include <stdio.h>                                      // printf e scanf
#define T 14                                            // tamanho da barra: troque aqui (e os valores) para outra barra

int main(void) {                                        // início do programa
    int barra[T] = {9, 4, 3, 9, 1, 2, 4, 5, 1, 1, 9, 7, 0, 5};   // números da figura da prova
    int conta[10] = {0};                                // conta[d]: vezes que o dígito d apareceu no controle
    int atual;                                          // posição atual (de 1 a T)
    scanf("%d", &atual);                                // a primeira é sempre 1
    conta[barra[atual - 1]]++;                          // o número da posição inicial conta
    int prox;                                           // próxima parada
    scanf("%d", &prox);                                 // lê a próxima posição
    while (prox > 0) {                                  // zero ou negativo encerra
        int passo = prox > atual ? 1 : -1;              // para a direita (+1) ou para a esquerda (-1)
        for (int p = atual + passo; p != prox + passo; p += passo)   // cada posição percorrida, sem repetir a atual
            conta[barra[p - 1]]++;                      // posição p da barra é o índice p - 1 do vetor
        atual = prox;                                   // agora o controle está na nova parada
        scanf("%d", &prox);                             // próxima parada
    }
    for (int d = 0; d < 10; d++) printf("%d%s", conta[d], d < 9 ? " " : "\n");   // as 10 contagens
    return 0;                                           // fim sem erro
}
