// Base 1 – Memória: pilha, heap, malloc, calloc, realloc e free
#include <stdio.h>
#include <stdlib.h>

/* Variáveis locais ficam na PILHA e somem quando a função retorna; o que vem de
   malloc fica no HEAP até alguém chamar free. Devolver o endereço de uma local
   é um erro clássico: a memória já não é sua. */
int *vetor_na_pilha_errado(void) {
    int v[4] = {1, 2, 3, 4};
    (void)v;                                     // não faça: return v;
    return NULL;
}

int *vetor_no_heap(int n) {                      // certo: quem chama dá free
    int *v = malloc(n * sizeof *v);              // sizeof *v: segue o tipo de v
    if (!v) { perror("malloc"); exit(1); }       // malloc pode falhar
    for (int i = 0; i < n; i++) v[i] = i + 1;
    return v;
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    vetor_na_pilha_errado();
    int *v = vetor_no_heap(n);
    long soma = 0;
    for (int i = 0; i < n; i++) soma += v[i];
    printf("soma = %ld\n", soma);
    int *zeros = calloc(n, sizeof *zeros);       // calloc: aloca e zera
    printf("calloc zera: zeros[0] = %d\n", zeros[0]);
    // realloc: cresce preservando o conteúdo
    int cap = 1, tam = 0;
    int *w = malloc(cap * sizeof *w);
    for (int i = 0; i < n; i++) {
        if (tam == cap) {
            int *novo = realloc(w, 2 * cap * sizeof *w);
            if (!novo) { free(w); return 1; }    // nunca w = realloc(w, ...) direto
            w = novo;
            cap *= 2;
        }
        w[tam++] = v[i];
    }
    printf("capacidade final %d\n", cap);
    free(v);                                     // cada malloc/calloc/realloc: um free
    free(zeros);
    free(w);
    v = NULL;                                    // evita usar um ponteiro solto
    printf("tudo liberado\n");
    return 0;
}
