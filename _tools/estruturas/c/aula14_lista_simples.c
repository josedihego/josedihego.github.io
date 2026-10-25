// Aula 14 – Lista simplesmente ligada: inserção, busca, remoção e inversão
// teste: c 1;c 2;c 3;f 9;p;r 2;i;p => lista: 3 2 1 9
// teste: c 1;c 2;c 3;f 9;p;r 2;i;p => lista: 9 1 3
// teste: r 5;p => lista: (vazia)
#include <stdio.h>
#include <stdlib.h>

/* Cada nó só conhece o próximo. Guardamos cabeça e cauda: inserir no início e no
   fim custa O(1); remover exige o nó ANTERIOR, então a remoção por chave é O(n).
   Comandos: c k (insere no começo), f k (no fim), r k (remove), i (inverte), p. */
typedef struct No { int chave; struct No *prox; } No;
typedef struct { No *cabeca, *cauda; } Lista;

void insere_comeco(Lista *L, int k) {
    No *x = malloc(sizeof(No));
    x->chave = k;
    x->prox = L->cabeca;
    L->cabeca = x;
    if (!L->cauda) L->cauda = x;                 // lista estava vazia
}

void insere_fim(Lista *L, int k) {
    No *x = malloc(sizeof(No));
    x->chave = k;
    x->prox = NULL;
    if (L->cauda) L->cauda->prox = x; else L->cabeca = x;
    L->cauda = x;
}

void remove_chave(Lista *L, int k) {             // procura mantendo o anterior
    No *ant = NULL, *x = L->cabeca;
    while (x && x->chave != k) { ant = x; x = x->prox; }
    if (!x) return;                              // não está na lista
    if (ant) ant->prox = x->prox; else L->cabeca = x->prox;   // era a cabeça?
    if (L->cauda == x) L->cauda = ant;                         // era a cauda?
    free(x);
}

// Θ(n), sem memória extra (exercício 10.2-7)
void inverte(Lista *L) {
    No *ant = NULL, *x = L->cabeca;
    L->cauda = x;
    while (x) {
        No *prox = x->prox;
        x->prox = ant;                           // vira o ponteiro para trás
        ant = x;
        x = prox;
    }
    L->cabeca = ant;
}

int main(void) {
    Lista L = {NULL, NULL};
    char c;
    int k;
    while (scanf(" %c", &c) == 1) {
        if (c == 'c' && scanf("%d", &k) == 1) insere_comeco(&L, k);
        else if (c == 'f' && scanf("%d", &k) == 1) insere_fim(&L, k);
        else if (c == 'r' && scanf("%d", &k) == 1) remove_chave(&L, k);
        else if (c == 'i') inverte(&L);
        else if (c == 'p') {
            printf("lista:");
            if (!L.cabeca) printf(" (vazia)");
            for (No *x = L.cabeca; x; x = x->prox) printf(" %d", x->chave);
            printf("\n");
        }
    }
    while (L.cabeca) { No *x = L.cabeca; L.cabeca = x->prox; free(x); }
    return 0;
}
