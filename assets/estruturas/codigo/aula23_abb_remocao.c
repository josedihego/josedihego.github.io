// Aula 23 – Inserção e remoção em árvore binária de busca (Cormen, seção 12.3)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { int chave; struct No *esq, *dir, *pai; } No;
typedef struct { No *raiz; } Arvore;

void insere(Arvore *T, int k) {                 // TREE-INSERT
    No *z = calloc(1, sizeof(No)), *y = NULL, *x = T->raiz;
    z->chave = k;
    while (x) { y = x; x = k < x->chave ? x->esq : x->dir; }
    z->pai = y;
    if (!y) T->raiz = z;
    else if (k < y->chave) y->esq = z;
    else y->dir = z;
}

/* TRANSPLANT: põe a subárvore v no lugar da subárvore u. */
void transplanta(Arvore *T, No *u, No *v) {
    if (!u->pai) T->raiz = v;
    else if (u == u->pai->esq) u->pai->esq = v;
    else u->pai->dir = v;
    if (v) v->pai = u->pai;
}

No *minimo(No *x) { while (x->esq) x = x->esq; return x; }

void remove_no(Arvore *T, No *z) {              // TREE-DELETE: três casos
    if (!z->esq) transplanta(T, z, z->dir);     // (a) sem filho esquerdo
    else if (!z->dir) transplanta(T, z, z->esq); // (b) sem filho direito
    // (c)/(d) dois filhos: entra o sucessor y
    else {
        No *y = minimo(z->dir);
        if (y->pai != z) {
            transplanta(T, y, y->dir);
            y->dir = z->dir;
            y->dir->pai = y;
        }
        transplanta(T, z, y);
        y->esq = z->esq;
        y->esq->pai = y;
    }
    free(z);
}

No *busca(No *x, int k) {
    while (x && k != x->chave) x = k < x->chave ? x->esq : x->dir;
    return x;
}

void em_ordem(No *x) {
    if (!x) return;
    em_ordem(x->esq);
    printf(" %d", x->chave);
    em_ordem(x->dir);
}
void libera(No *x) { if (x) { libera(x->esq); libera(x->dir); free(x); } }

int main(void) {
    Arvore T = {NULL};
    char s[16];
    while (scanf("%15s", s) == 1) {
        if (s[0] == 'r') {                      // "r k" remove a chave k
            int k;
            if (scanf("%d", &k) != 1) break;
            No *z = busca(T.raiz, k);
            if (z) remove_no(&T, z);
        } else insere(&T, atoi(s));
    }
    printf("em ordem:");
    em_ordem(T.raiz);
    printf("\n");
    if (T.raiz) printf("raiz %d\n", T.raiz->chave);
    libera(T.raiz);
    return 0;
}
