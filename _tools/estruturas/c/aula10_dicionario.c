// Aula 10 – Dicionário em vetor ordenado: busca binária e consultas de ordem
// teste: i 30;i 10;i 50;i 20;i 40;b 20;b 25;m;M;s 30;r 30;s 20;p => 20 encontrado
// teste: i 30;i 10;i 50;i 20;i 40;b 20;b 25;m;M;s 30;r 30;s 20;p => 25 ausente
// teste: i 30;i 10;i 50;i 20;i 40;b 20;b 25;m;M;s 30;r 30;s 20;p => sucessor de 30: 40
// teste: i 30;i 10;i 50;i 20;i 40;r 30;p => conjunto: 10 20 40 50
#include <stdio.h>
#include <stdlib.h>

/* Um conjunto dinâmico com as operações do Cormen (introdução da parte III):
   SEARCH, INSERT, DELETE, MINIMUM, MAXIMUM, SUCCESSOR. Comandos da entrada:
   i k, r k, b k (busca), m (mínimo), M (máximo), s k (sucessor), p (imprime). */
typedef struct { int *v; int n, cap; } Dicionario;

// busca binária: primeiro índice com v >= k
int posicao(const Dicionario *D, int k) {
    int lo = 0, hi = D->n;
    while (lo < hi) {
        int meio = lo + (hi - lo) / 2;
        if (D->v[meio] < k) lo = meio + 1; else hi = meio;
    }
    return lo;                                 // O(lg n)
}

int busca(const Dicionario *D, int k) {
    int i = posicao(D, k);
    return i < D->n && D->v[i] == k;
}

void insere(Dicionario *D, int k) {            // abre espaço deslocando: O(n)
    int i = posicao(D, k);
    if (i < D->n && D->v[i] == k) return;      // conjunto: sem repetições
    if (D->n == D->cap) {
        D->cap = D->cap ? 2 * D->cap : 8;
        D->v = realloc(D->v, D->cap * sizeof(int));
    }
    for (int j = D->n; j > i; j--) D->v[j] = D->v[j - 1];
    D->v[i] = k;
    D->n++;
}

void remove_chave(Dicionario *D, int k) {      // fecha o buraco: O(n)
    int i = posicao(D, k);
    if (i == D->n || D->v[i] != k) return;
    for (int j = i; j < D->n - 1; j++) D->v[j] = D->v[j + 1];
    D->n--;
}

int main(void) {
    Dicionario D = {NULL, 0, 0};
    char c;
    int k;
    while (scanf(" %c", &c) == 1) {
        if (c == 'i' && scanf("%d", &k) == 1) insere(&D, k);
        else if (c == 'r' && scanf("%d", &k) == 1) remove_chave(&D, k);
        else if (c == 'b' && scanf("%d", &k) == 1)
            printf(busca(&D, k) ? "%d encontrado\n" : "%d ausente\n", k);
        else if (c == 'm' && D.n) printf("mínimo %d\n", D.v[0]);          // O(1)
        else if (c == 'M' && D.n) printf("máximo %d\n", D.v[D.n - 1]);    // O(1)
        else if (c == 's' && scanf("%d", &k) == 1) {                      // O(lg n)
            int i = posicao(&D, k + 1);
            if (i < D.n) printf("sucessor de %d: %d\n", k, D.v[i]);
        } else if (c == 'p') {
            printf("conjunto:");
            for (int j = 0; j < D.n; j++) printf(" %d", D.v[j]);
            printf("\n");
        }
    }
    free(D.v);
    return 0;
}
