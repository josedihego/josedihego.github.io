// Aula 24 – Árvore AVL: inserção com rotações (Cormen, problema 13-3)
#include <stdio.h>
#include <stdlib.h>

/* Cada nó guarda a altura da sua subárvore (folha = 0; vazio = -1).
   Balanceamento de x = altura(esq) - altura(dir), sempre em {-1, 0, 1}. */
typedef struct No { int chave, h; struct No *esq, *dir; } No;

int h(No *x) { return x ? x->h : -1; }
int maior(int a, int b) { return a > b ? a : b; }
void atualiza(No *x) { x->h = 1 + maior(h(x->esq), h(x->dir)); }

// RIGHT-ROTATE: x sobe, y desce à direita
No *gira_direita(No *y) {
    No *x = y->esq;
    y->esq = x->dir;
    x->dir = y;
    atualiza(y);
    atualiza(x);
    return x;
}

No *gira_esquerda(No *x) {                     // LEFT-ROTATE: o espelho
    No *y = x->dir;
    x->dir = y->esq;
    y->esq = x;
    atualiza(x);
    atualiza(y);
    return y;
}

No *balanceia(No *x) {
    atualiza(x);
    int b = h(x->esq) - h(x->dir);
    if (b > 1) {                               // pesado à esquerda
        if (h(x->esq->esq) < h(x->esq->dir))   // caso esquerda-direita: rotação dupla
            x->esq = gira_esquerda(x->esq);
        return gira_direita(x);
    }
    if (b < -1) {                              // pesado à direita
        if (h(x->dir->dir) < h(x->dir->esq))   // caso direita-esquerda: rotação dupla
            x->dir = gira_direita(x->dir);
        return gira_esquerda(x);
    }
    return x;
}

// insere como na ABB e rebalanceia na volta
No *insere(No *x, int k) {
    if (!x) {
        x = calloc(1, sizeof(No));
        x->chave = k;
        return x;
    }
    if (k < x->chave) x->esq = insere(x->esq, k);
    else x->dir = insere(x->dir, k);
    return balanceia(x);
}

void libera(No *x) { if (x) { libera(x->esq); libera(x->dir); free(x); } }

int main(void) {
    No *raiz = NULL;
    int k;
    while (scanf("%d", &k) == 1) raiz = insere(raiz, k);
    if (!raiz) return 1;
    printf("raiz %d, altura %d\n", raiz->chave, raiz->h);
    libera(raiz);
    return 0;
}
