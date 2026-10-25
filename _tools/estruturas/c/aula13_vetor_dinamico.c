// Aula 13 – Vetor dinâmico: dobra ao encher, encolhe com 1/4 (Cormen, seção 17.4)
// teste: 9 => capacidade 16 com 9 elementos
// teste: 9 => depois de remover 7: capacidade 4 com 2 elementos
// teste: 1 => capacidade 1 com 1 elementos
#include <stdio.h>
#include <stdlib.h>

/* TABLE-INSERT e TABLE-DELETE: o vetor dobra quando enche e cai pela metade quando
   fica com 1/4. Encolher só em 1/2 faria inserções e remoções alternadas copiarem
   tudo a cada operação; com 1/4, toda operação custa O(1) amortizado. */
typedef struct { int *v; int n, cap; long copias; } Vetor;

void redimensiona(Vetor *T, int nova) {
    int *w = malloc(nova * sizeof(int));
    for (int i = 0; i < T->n; i++) w[i] = T->v[i];   // a cópia: o custo real
    T->copias += T->n;
    free(T->v);
    T->v = w;
    T->cap = nova;
}

void insere(Vetor *T, int x) {
    if (T->cap == 0) redimensiona(T, 1);
    else if (T->n == T->cap) redimensiona(T, 2 * T->cap);
    T->v[T->n++] = x;
}

void remove_ultimo(Vetor *T) {
    T->n--;
    if (T->cap > 1 && T->n <= T->cap / 4) redimensiona(T, T->cap / 2);
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    Vetor T = {NULL, 0, 0, 0};
    for (int i = 0; i < n; i++) insere(&T, i);
    printf("capacidade %d com %d elementos (%ld cópias)\n", T.cap, T.n, T.copias);
    if (n > 7) {
        for (int i = 0; i < 7; i++) remove_ultimo(&T);
        printf("depois de remover 7: capacidade %d com %d elementos\n", T.cap, T.n);
    }
    free(T.v);
    return 0;
}
