// Aula 19 – Tabela hash com encadeamento: frequência de palavras (Cormen, seção 11.2)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define M 101                                  // número de posições (primo)

typedef struct No { char *palavra; int cont; struct No *prox; } No;
No *T[M];                                      // T[i] é a lista da posição i

/* Polinômio em base 31 com resto por M: método da divisão aplicado à string. */
unsigned h(const char *s) {
    unsigned long v = 0;
    for (; *s; s++) v = (v * 31 + (unsigned char)*s) % M;
    return v;
}

No *busca(const char *s) {                     // CHAINED-HASH-SEARCH: percorre T[h(s)]
    for (No *x = T[h(s)]; x; x = x->prox)
        if (strcmp(x->palavra, s) == 0) return x;
    return NULL;
}

void insere(const char *s) {                   // CHAINED-HASH-INSERT na cabeça: O(1)
    No *x = busca(s);
    if (x) { x->cont++; return; }              // já existe: só conta
    x = malloc(sizeof(No));
    x->palavra = malloc(strlen(s) + 1);
    strcpy(x->palavra, s);
    x->cont = 1;
    x->prox = T[h(s)];
    T[h(s)] = x;
}

int main(void) {
    char p[100];
    int n = 0;
    while (scanf("%99s", p) == 1) { insere(p); n++; }
    int usadas = 0, maior = 0;
    for (int i = 0; i < M; i++) {
        int tam = 0;
        for (No *x = T[i]; x; x = x->prox) {
            printf("%s: %d\n", x->palavra, x->cont);
            tam++;
        }
        if (tam) usadas++;
        if (tam > maior) maior = tam;
    }
    printf("%d palavras, %d posições usadas de %d, maior lista: %d\n",
           n, usadas, M, maior);
    for (int i = 0; i < M; i++)
        while (T[i]) { No *x = T[i]; T[i] = x->prox; free(x->palavra); free(x); }
    return 0;
}
