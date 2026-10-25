// Base 4 – Funções: ponteiros para funções, qsort genérico, recursão e void *
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Comparadores no formato que o qsort espera: recebem void * (qualquer tipo)
   e devolvem negativo, zero ou positivo. */
int crescente(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);                  // evita o estouro de x - y
}
int decrescente(const void *a, const void *b) { return crescente(b, a); }

/* Ponteiro para função: uma variável que guarda "qual função chamar". */
typedef int (*Comparador)(const void *, const void *);

/* Troca genérica: funciona para qualquer tipo, dado o tamanho em bytes. */
void troca(void *a, void *b, size_t tam) {
    unsigned char tmp[64];
    memcpy(tmp, a, tam);
    memcpy(a, b, tam);
    memcpy(b, tmp, tam);
}

// recursão: cada chamada tem seu quadro na pilha
long fatorial(int n) {
    return n <= 1 ? 1 : n * fatorial(n - 1);
}

void imprime(const char *nome, const int v[], int n) {
    printf("%s:", nome);
    for (int i = 0; i < n; i++) printf(" %d", v[i]);
    printf("\n");
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1 || n > 20) return 1;
    int v[20];
    for (int i = 0; i < n; i++)
        if (scanf("%d", &v[i]) != 1) return 1;
    Comparador ordens[2] = {crescente, decrescente};          // tabela de funções
    const char *nomes[2] = {"crescente", "decrescente"};
    for (int k = 0; k < 2; k++) {
        qsort(v, n, sizeof v[0], ordens[k]);                   // qsort chama de volta
        imprime(nomes[k], v, n);
    }
    double x = 1.5, y = 2.5;
    troca(&x, &y, sizeof x);
    printf("troca genérica: x = %.1f, y = %.1f\n", x, y);
    printf("fatorial de %d = %ld\n", n, fatorial(n));
    return 0;
}
