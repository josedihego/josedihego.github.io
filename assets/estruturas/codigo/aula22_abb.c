// Aula 22 – Árvore binária de busca: percursos e consultas (Cormen, seções 12.1 e 12.2)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { int chave; struct No *esq, *dir, *pai; } No;

No *insere(No *raiz, int k) {                  // TREE-INSERT (detalhado na aula 23)
    No *z = calloc(1, sizeof(No)), *y = NULL, *x = raiz;
    z->chave = k;
    while (x) { y = x; x = k < x->chave ? x->esq : x->dir; }
    z->pai = y;
    if (!y) return z;
    if (k < y->chave) y->esq = z; else y->dir = z;
    return raiz;
}

// INORDER-TREE-WALK: Θ(n), chaves em ordem
void em_ordem(No *x) {
    if (!x) return;
    em_ordem(x->esq);
    printf(" %d", x->chave);
    em_ordem(x->dir);
}

No *busca(No *x, int k) {                      // ITERATIVE-TREE-SEARCH: O(h)
    while (x && k != x->chave) x = k < x->chave ? x->esq : x->dir;
    return x;
}

No *minimo(No *x) { while (x->esq) x = x->esq; return x; }
No *maximo(No *x) { while (x->dir) x = x->dir; return x; }

No *sucessor(No *x) {                          // TREE-SUCCESSOR: O(h)
    if (x->dir) return minimo(x->dir);         // caso 1: menor da subárvore direita
    No *y = x->pai;                            // caso 2: sobe até virar filho esquerdo
    while (y && x == y->dir) { x = y; y = y->pai; }
    return y;
}

void libera(No *x) { if (x) { libera(x->esq); libera(x->dir); free(x); } }

int main(void) {
    No *raiz = NULL;
    int k, ultimo = 0;
    while (scanf("%d", &k) == 1) { raiz = insere(raiz, k); ultimo = k; }
    if (!raiz) return 1;
    printf("em ordem:");
    em_ordem(raiz);
    printf("\nmínimo %d, máximo %d\n", minimo(raiz)->chave, maximo(raiz)->chave);
    No *x = busca(raiz, 13), *s = x ? sucessor(x) : NULL;
    if (s) printf("sucessor de 13: %d\n", s->chave);
    printf("última chave lida (%d) %s\n", ultimo,
           busca(raiz, ultimo) ? "encontrada" : "ausente");
    libera(raiz);
    return 0;
}
