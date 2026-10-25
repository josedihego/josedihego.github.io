// Aula 25 – Experimento: altura da rubro-negra e custo do conserto
// Saída CSV: n, altura_ordenada, altura_aleatoria, rotacoes (por inserção, aleatórias)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { unsigned chave; int vermelho; struct No *esq, *dir, *pai; } No;
No NIL_NO, *NIL = &NIL_NO, *raiz;
No *pool;
int livre;
long rotacoes;

unsigned long long estado = 0x1234567887654321ULL;
unsigned aleatorio(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)(estado >> 16);
}

// LEFT-ROTATE (esquerda = 1) ou RIGHT-ROTATE
void gira(No *x, int esquerda) {
    No *y = esquerda ? x->dir : x->esq;
    No *meio = esquerda ? y->esq : y->dir;
    if (esquerda) x->dir = meio; else x->esq = meio;
    if (meio != NIL) meio->pai = x;
    y->pai = x->pai;
    if (x->pai == NIL) raiz = y;
    else if (x == x->pai->esq) x->pai->esq = y;
    else x->pai->dir = y;
    if (esquerda) y->esq = x; else y->dir = x;
    x->pai = y;
    rotacoes++;
}

void insere(unsigned k) {                      // RB-INSERT + RB-INSERT-FIXUP
    No *z = &pool[livre++], *y = NIL, *x = raiz;
    z->chave = k;
    while (x != NIL) { y = x; x = k < x->chave ? x->esq : x->dir; }
    z->pai = y;
    if (y == NIL) raiz = z; else if (k < y->chave) y->esq = z; else y->dir = z;
    z->esq = z->dir = NIL;
    z->vermelho = 1;
    while (z->pai->vermelho) {
        No *p = z->pai, *a = p->pai;
        int pai_esq = (p == a->esq);
        No *tio = pai_esq ? a->dir : a->esq;
        if (tio->vermelho) {                   // caso 1
            p->vermelho = tio->vermelho = 0;
            a->vermelho = 1;
            z = a;
        } else {
            // caso 2
            if (z == (pai_esq ? p->dir : p->esq)) { z = p; gira(z, pai_esq); }
            z->pai->vermelho = 0;              // caso 3
            z->pai->pai->vermelho = 1;
            gira(z->pai->pai, !pai_esq);
        }
    }
    raiz->vermelho = 0;
}

int confere(No *x, int *altura) {              // devolve bh; aborta se violar as regras
    if (x == NIL) { *altura = -1; return 1; }
    int ha, hb;
    int a = confere(x->esq, &ha), b = confere(x->dir, &hb);
    if (a != b) { fprintf(stderr, "alturas negras diferentes!\n"); exit(1); }
    if (x->vermelho && (x->esq->vermelho || x->dir->vermelho)) {
        fprintf(stderr, "vermelho com filho vermelho!\n");
        exit(1);
    }
    *altura = 1 + (ha > hb ? ha : hb);
    return a + !x->vermelho;
}

int main(void) {
    NIL->vermelho = 0;
    pool = malloc((1 << 21) * sizeof(No));
    printf("n,altura_ordenada,altura_aleatoria,rotacoes\n");
    for (int n = 1 << 10; n <= 1 << 21; n *= 2) {
        int h1, h2;
        raiz = NIL; livre = 0;
        for (int i = 0; i < n; i++) insere((unsigned)i);
        confere(raiz, &h1);
        raiz = NIL; livre = 0; rotacoes = 0;
        for (int i = 0; i < n; i++) insere(aleatorio());
        confere(raiz, &h2);
        printf("%d,%d,%d,%.4f\n", n, h1, h2, (double)rotacoes / n);
    }
    free(pool);
    return 0;
}
