// Aula 26 – Experimento: altura da árvore B para três graus mínimos
// Saída CSV: n, t2, t16, t128 (altura após n inserções de chaves aleatórias)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { int n, folha; unsigned *chave; struct No **filho; } No;
int t;

No *novo(int folha) {
    No *x = malloc(sizeof(No));
    x->n = 0; x->folha = folha;
    x->chave = malloc((2 * t - 1) * sizeof(unsigned));
    x->filho = malloc(2 * t * sizeof(No *));
    return x;
}

void divide(No *x, int i) {
    No *y = x->filho[i], *z = novo(y->folha);
    z->n = t - 1;
    for (int j = 0; j < t - 1; j++) z->chave[j] = y->chave[j + t];
    if (!y->folha) for (int j = 0; j < t; j++) z->filho[j] = y->filho[j + t];
    y->n = t - 1;
    for (int j = x->n; j > i; j--) x->filho[j + 1] = x->filho[j];
    x->filho[i + 1] = z;
    for (int j = x->n - 1; j >= i; j--) x->chave[j + 1] = x->chave[j];
    x->chave[i] = y->chave[t - 1];
    x->n++;
}

void insere_nao_cheio(No *x, unsigned k) {
    while (!x->folha) {                        // versão iterativa
        int i = x->n - 1;
        while (i >= 0 && k < x->chave[i]) i--;
        i++;
        if (x->filho[i]->n == 2 * t - 1) { divide(x, i); if (k > x->chave[i]) i++; }
        x = x->filho[i];
    }
    int i = x->n - 1;
    while (i >= 0 && k < x->chave[i]) { x->chave[i + 1] = x->chave[i]; i--; }
    x->chave[i + 1] = k;
    x->n++;
}

void libera(No *x) {
    if (!x->folha) for (int i = 0; i <= x->n; i++) libera(x->filho[i]);
    free(x->chave); free(x->filho); free(x);
}

int altura_com(int grau, int n) {
    t = grau;
    srand(26);
    No *raiz = novo(1);
    for (int i = 0; i < n; i++) {
        unsigned k = (unsigned)rand() << 1 ^ (unsigned)rand();
        if (raiz->n == 2 * t - 1) {            // raiz cheia: a árvore cresce para cima
            No *s = novo(0);
            s->filho[0] = raiz;
            divide(s, 0);
            raiz = s;
        }
        insere_nao_cheio(raiz, k);
    }
    int h = 0;
    for (No *x = raiz; !x->folha; x = x->filho[0]) h++;
    libera(raiz);
    return h;
}

int main(void) {
    printf("n,t2,t16,t128\n");
    for (int n = 1 << 10; n <= 1 << 22; n *= 2)
        printf("%d,%d,%d,%d\n", n, altura_com(2, n), altura_com(16, n),
               altura_com(128, n));
    return 0;
}
