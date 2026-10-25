// Aula 24 – Experimento: altura da AVL contra a ABB comum, com chaves em ordem
// Saída CSV: n, avl_ordenada, avl_aleatoria, rotacoes (por inserção, chaves aleatórias)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { unsigned chave; int h; struct No *esq, *dir; } No;

long rotacoes;
No *pool;
int livre;

unsigned long long estado = 0xDA942042E4DD58B5ULL;
unsigned aleatorio(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)(estado >> 16);
}

int h(No *x) { return x ? x->h : -1; }
void atualiza(No *x) { int a = h(x->esq), b = h(x->dir); x->h = 1 + (a > b ? a : b); }

No *gira_direita(No *y) {
    No *x = y->esq; y->esq = x->dir; x->dir = y;
    atualiza(y); atualiza(x); rotacoes++;
    return x;
}
No *gira_esquerda(No *x) {
    No *y = x->dir; x->dir = y->esq; y->esq = x;
    atualiza(x); atualiza(y); rotacoes++;
    return y;
}

No *balanceia(No *x) {
    atualiza(x);
    int b = h(x->esq) - h(x->dir);
    if (b > 1) {
        if (h(x->esq->esq) < h(x->esq->dir)) x->esq = gira_esquerda(x->esq);
        return gira_direita(x);
    }
    if (b < -1) {
        if (h(x->dir->dir) < h(x->dir->esq)) x->dir = gira_direita(x->dir);
        return gira_esquerda(x);
    }
    return x;
}

No *insere(No *x, unsigned k) {
    if (!x) {
        x = &pool[livre++];
        x->chave = k; x->h = 0; x->esq = x->dir = NULL;
        return x;
    }
    if (k < x->chave) x->esq = insere(x->esq, k);
    else x->dir = insere(x->dir, k);
    return balanceia(x);
}

// devolve a altura; aborta se não for AVL
int confere(No *x) {
    if (!x) return -1;
    int a = confere(x->esq), b = confere(x->dir);
    if (a - b > 1 || b - a > 1) { fprintf(stderr, "não é AVL!\n"); exit(1); }
    return 1 + (a > b ? a : b);
}

int main(void) {
    pool = malloc((1 << 21) * sizeof(No));
    printf("n,avl_ordenada,avl_aleatoria,rotacoes\n");
    for (int n = 1 << 10; n <= 1 << 21; n *= 2) {
        No *raiz = NULL;
        livre = 0;
        // ABB comum: altura n-1
        for (int i = 0; i < n; i++) raiz = insere(raiz, (unsigned)i);
        int h1 = confere(raiz);
        raiz = NULL; livre = 0; rotacoes = 0;
        for (int i = 0; i < n; i++) raiz = insere(raiz, aleatorio());
        int h2 = confere(raiz);
        printf("%d,%d,%d,%.4f\n", n, h1, h2, (double)rotacoes / n);
    }
    free(pool);
    return 0;
}
