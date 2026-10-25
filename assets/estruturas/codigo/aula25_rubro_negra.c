// Aula 25 – Árvore rubro-negra: inserção (Cormen, seções 13.1 a 13.3)
#include <stdio.h>
#include <stdlib.h>

/* Uma sentinela NIL (preta) faz o papel de todas as folhas e do pai da raiz. */
typedef enum { VERMELHO, PRETO } Cor;
typedef struct No { int chave; Cor cor; struct No *esq, *dir, *pai; } No;
typedef struct { No *raiz, *nil; } Arvore;

void gira_esquerda(Arvore *T, No *x) {         // LEFT-ROTATE
    No *y = x->dir;
    x->dir = y->esq;
    if (y->esq != T->nil) y->esq->pai = x;
    y->pai = x->pai;
    if (x->pai == T->nil) T->raiz = y;
    else if (x == x->pai->esq) x->pai->esq = y;
    else x->pai->dir = y;
    y->esq = x;
    x->pai = y;
}

void gira_direita(Arvore *T, No *y) {          // RIGHT-ROTATE (espelho)
    No *x = y->esq;
    y->esq = x->dir;
    if (x->dir != T->nil) x->dir->pai = y;
    x->pai = y->pai;
    if (y->pai == T->nil) T->raiz = x;
    else if (y == y->pai->dir) y->pai->dir = x;
    else y->pai->esq = x;
    x->dir = y;
    y->pai = x;
}

void conserta(Arvore *T, No *z) {              // RB-INSERT-FIXUP
    while (z->pai->cor == VERMELHO) {
        if (z->pai == z->pai->pai->esq) {
            No *y = z->pai->pai->dir;          // tio
            if (y->cor == VERMELHO) {          // caso 1: recolore e sobe
                z->pai->cor = PRETO;
                y->cor = PRETO;
                z->pai->pai->cor = VERMELHO;
                z = z->pai->pai;
            } else {
                if (z == z->pai->dir) {        // caso 2: vira o caso 3
                    z = z->pai;
                    gira_esquerda(T, z);
                }
                z->pai->cor = PRETO;           // caso 3: recolore e gira
                z->pai->pai->cor = VERMELHO;
                gira_direita(T, z->pai->pai);
            }
        } else {                               // espelho: pai é filho direito
            No *y = z->pai->pai->esq;
            if (y->cor == VERMELHO) {
                z->pai->cor = PRETO;
                y->cor = PRETO;
                z->pai->pai->cor = VERMELHO;
                z = z->pai->pai;
            } else {
                if (z == z->pai->esq) {
                    z = z->pai;
                    gira_direita(T, z);
                }
                z->pai->cor = PRETO;
                z->pai->pai->cor = VERMELHO;
                gira_esquerda(T, z->pai->pai);
            }
        }
    }
    T->raiz->cor = PRETO;
}

void insere(Arvore *T, int k) {                // RB-INSERT
    No *z = malloc(sizeof(No)), *y = T->nil, *x = T->raiz;
    z->chave = k;
    while (x != T->nil) { y = x; x = k < x->chave ? x->esq : x->dir; }
    z->pai = y;
    if (y == T->nil) T->raiz = z;
    else if (k < y->chave) y->esq = z;
    else y->dir = z;
    z->esq = z->dir = T->nil;
    z->cor = VERMELHO;
    conserta(T, z);
}

/* bh(raiz): pretos de raiz até NIL, sem contar a raiz e contando o NIL.
   A raiz é preta, então basta contar os pretos de um caminho, raiz incluída. */
int altura_negra(Arvore *T) {
    int bh = 0;
    for (No *x = T->raiz; x != T->nil; x = x->esq)
        if (x->cor == PRETO) bh++;
    return bh;
}

void libera(Arvore *T, No *x) {
    if (x == T->nil) return;
    libera(T, x->esq);
    libera(T, x->dir);
    free(x);
}

int main(void) {
    No nil = {0, PRETO, NULL, NULL, NULL};
    Arvore T = {&nil, &nil};
    int k;
    while (scanf("%d", &k) == 1) insere(&T, k);
    if (T.raiz == T.nil) return 1;
    printf("raiz %d (%s), altura negra %d\n", T.raiz->chave,
           T.raiz->cor == PRETO ? "preta" : "vermelha", altura_negra(&T));
    libera(&T, T.raiz);
    return 0;
}
