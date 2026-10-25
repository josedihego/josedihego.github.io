// Aula 26 – Árvore B: busca e inserção com divisão preventiva (Cormen, capítulo 18)
// teste: 2 F S Q K C L H T V W M R N P A B X Y D Z E => altura 2
// teste: 2 F S Q K C L H T V W M R N P A B X Y D Z E => raiz: K Q
// teste: 3 1 2 3 4 5 6 7 8 9 10 => altura 1
#include <stdio.h>
#include <stdlib.h>

/* Grau mínimo t: todo nó (menos a raiz) tem de t-1 a 2t-1 chaves.
   Num banco de dados, cada nó é uma página do disco; aqui fica na memória. */
typedef struct No {
    int n, folha;
    char *chave;                               // até 2t-1 chaves
    struct No **filho;                         // até 2t filhos
} No;

int t;

No *novo(int folha) {
    No *x = malloc(sizeof(No));
    x->n = 0;
    x->folha = folha;
    x->chave = malloc(2 * t - 1);
    x->filho = malloc(2 * t * sizeof(No *));
    return x;
}

/* B-TREE-SPLIT-CHILD: o filho i de x está cheio; a chave do meio sobe para x. */
void divide(No *x, int i) {
    No *y = x->filho[i], *z = novo(y->folha);
    z->n = t - 1;
    for (int j = 0; j < t - 1; j++) z->chave[j] = y->chave[j + t];
    if (!y->folha)
        for (int j = 0; j < t; j++) z->filho[j] = y->filho[j + t];
    y->n = t - 1;
    for (int j = x->n; j > i; j--) x->filho[j + 1] = x->filho[j];
    x->filho[i + 1] = z;
    for (int j = x->n - 1; j >= i; j--) x->chave[j + 1] = x->chave[j];
    x->chave[i] = y->chave[t - 1];
    x->n++;
}

void insere_nao_cheio(No *x, char k) {         // B-TREE-INSERT-NONFULL
    int i = x->n - 1;
    if (x->folha) {
        while (i >= 0 && k < x->chave[i]) { x->chave[i + 1] = x->chave[i]; i--; }
        x->chave[i + 1] = k;
        x->n++;
        return;
    }
    while (i >= 0 && k < x->chave[i]) i--;
    i++;
    if (x->filho[i]->n == 2 * t - 1) {         // divide antes de descer: nunca volta
        divide(x, i);
        if (k > x->chave[i]) i++;
    }
    insere_nao_cheio(x->filho[i], k);
}

// B-TREE-INSERT: a árvore cresce pela raiz
No *insere(No *raiz, char k) {
    if (raiz->n == 2 * t - 1) {
        No *s = novo(0);
        s->filho[0] = raiz;
        divide(s, 0);
        insere_nao_cheio(s, k);
        return s;
    }
    insere_nao_cheio(raiz, k);
    return raiz;
}

void libera(No *x) {
    if (!x->folha)
        for (int i = 0; i <= x->n; i++) libera(x->filho[i]);
    free(x->chave); free(x->filho); free(x);
}

int main(void) {
    char s[16];
    if (scanf("%d", &t) != 1 || t < 2) return 1;
    No *raiz = novo(1);
    while (scanf("%15s", s) == 1)                // letras ou números pequenos
        raiz = insere(raiz, s[0] > '9' ? s[0] : (char)atoi(s));
    int altura = 0;
    for (No *x = raiz; !x->folha; x = x->filho[0]) altura++;
    printf("altura %d\nraiz:", altura);
    for (int i = 0; i < raiz->n; i++)
        printf(" %c", raiz->chave[i] > ' ' ? raiz->chave[i] : '0' + raiz->chave[i]);
    printf("\n");
    libera(raiz);
    return 0;
}
