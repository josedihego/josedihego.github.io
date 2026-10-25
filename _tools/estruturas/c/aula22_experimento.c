// Aula 22 – Experimento: custo médio de busca numa árvore com chaves aleatórias
// Saída CSV: n, busca_media (nós visitados numa busca com sucesso, em média)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { unsigned chave; struct No *esq, *dir; } No;

unsigned long long estado = 0x2545F4914F6CDD1DULL;
unsigned aleatorio(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)(estado >> 16);
}

double media_busca(No nos[], int n) {          // uma árvore com n chaves aleatórias
    No *raiz = NULL;
    double soma = 0;
    for (int i = 0; i < n; i++) {              // a profundidade do novo nó + 1 é
        nos[i].chave = aleatorio();            // exatamente o custo de buscá-lo depois
        nos[i].esq = nos[i].dir = NULL;
        No **lugar = &raiz;
        int visitados = 1;
        while (*lugar) {
            No *x = *lugar;
            lugar = nos[i].chave < x->chave ? &x->esq : &x->dir;
            visitados++;
        }
        *lugar = &nos[i];
        soma += visitados;
    }
    return soma / n;
}

int main(void) {
    No *nos = malloc((1 << 21) * sizeof(No));
    printf("n,busca_media\n");
    for (int n = 1 << 10; n <= 1 << 21; n *= 2) {
        int arvores = n <= (1 << 17) ? 10 : 3;  // uma árvore só varia bastante
        double soma = 0;
        for (int r = 0; r < arvores; r++) soma += media_busca(nos, n);
        printf("%d,%.4f\n", n, soma / arvores);
    }
    free(nos);
    return 0;
}
