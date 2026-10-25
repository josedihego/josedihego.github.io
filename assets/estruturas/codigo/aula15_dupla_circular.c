// Aula 15 – Lista duplamente ligada sem sentinela e lista circular (Josefo)
#include <stdio.h>
#include <stdlib.h>

/* Lista duplamente ligada SEM sentinela: cabeça e cauda podem ser NULL, então
   inserir e remover têm casos especiais (compare com a sentinela da aula 16). */
typedef struct No { int chave; struct No *ant, *prox; } No;

No *insere_fim(No **cabeca, No **cauda, int k) {
    No *x = malloc(sizeof(No));
    x->chave = k;
    x->prox = NULL;
    x->ant = *cauda;
    if (*cauda) (*cauda)->prox = x;              // caso geral
    else *cabeca = x;                            // caso especial: lista vazia
    *cauda = x;
    return x;
}

void remove_no(No **cabeca, No **cauda, No *x) {
    if (x->ant) x->ant->prox = x->prox; else *cabeca = x->prox;   // x era a cabeça
    if (x->prox) x->prox->ant = x->ant; else *cauda = x->ant;     // x era a cauda
    free(x);
}

int main(void) {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2 || n < 1 || k < 1) return 1;
    No *cabeca = NULL, *cauda = NULL;
    for (int i = 1; i <= n; i++) insere_fim(&cabeca, &cauda, i);
    /* Problema de Josefo: n pessoas em roda, cada k-ésima sai. Fechamos a lista
       num CÍRCULO (cauda->prox = cabeça): andar é só seguir prox, sem testar o fim. */
    cauda->prox = cabeca;
    cabeca->ant = cauda;
    No *x = cauda;                               // começa "antes" da pessoa 1
    printf("ordem de saída:");
    for (int restam = n; restam > 1; restam--) {
        for (int passo = 0; passo < k; passo++) x = x->prox;
        printf(" %d", x->chave);
        No *sai = x;
        x = x->ant;                              // continua a partir do anterior
        sai->ant->prox = sai->prox;              // na lista circular não há extremos:
        sai->prox->ant = sai->ant;               // a remoção não tem casos especiais
        free(sai);
    }
    printf("\nsobrevivente: %d\n", x->prox->chave);
    free(x->prox == x ? x : x->prox);
    return 0;
}
