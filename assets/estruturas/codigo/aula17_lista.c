// Aula 17 – Lista duplamente ligada com sentinela (Cormen, seções 10.2)
#include <stdio.h>
#include <stdlib.h>

/* A sentinela L->nil é um nó falso: nil->prox é a cabeça e nil->ant é a cauda.
   Com ela, inserir e remover não têm casos especiais (lista vazia, extremos). */
typedef struct No { int chave; struct No *ant, *prox; } No;
typedef struct { No nil; } Lista;

void inicia(Lista *L) { L->nil.prox = L->nil.ant = &L->nil; }

void insere(Lista *L, int k) {                  // LIST-INSERT': na cabeça, O(1)
    No *x = malloc(sizeof(No));
    x->chave = k;
    x->prox = L->nil.prox;
    L->nil.prox->ant = x;
    L->nil.prox = x;
    x->ant = &L->nil;
}

No *busca(Lista *L, int k) {                    // LIST-SEARCH': Θ(n) no pior caso
    No *x = L->nil.prox;
    while (x != &L->nil && x->chave != k) x = x->prox;
    return x == &L->nil ? NULL : x;
}

void remove_no(No *x) {                         // LIST-DELETE': O(1) dado o nó
    x->ant->prox = x->prox;
    x->prox->ant = x->ant;
    free(x);
}

int main(void) {
    Lista L;
    inicia(&L);
    char cmd[4];
    int k;
    while (scanf("%3s", cmd) == 1) {
        if (cmd[0] == 'i' && scanf("%d", &k) == 1) insere(&L, k);
        else if (cmd[0] == 'b' && scanf("%d", &k) == 1)
            printf(busca(&L, k) ? "achou %d\n" : "não achou %d\n", k);
        else if (cmd[0] == 'r' && scanf("%d", &k) == 1) {
            No *x = busca(&L, k);
            if (x) remove_no(x);
        } else if (cmd[0] == 'p') {
            printf("lista:");
            for (No *x = L.nil.prox; x != &L.nil; x = x->prox) printf(" %d", x->chave);
            printf("\n");
        }
    }
    while (L.nil.prox != &L.nil) remove_no(L.nil.prox);
    return 0;
}
