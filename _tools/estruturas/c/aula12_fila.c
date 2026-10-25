// Aula 12 – Filas: vetor circular e lista ligada (Cormen, seção 10.1)
// teste: e 1;e 2;e 3;d;e 4;d;d;d;d => saiu 1
// teste: e 1;e 2;e 3;d;e 4;d;d;d;d => saiu 4
// teste: e 1;e 2;e 3;d;e 4;d;d;d;d => fila vazia
#include <stdio.h>
#include <stdlib.h>

/* Fila circular (Figura 10.2): cabeca é o próximo a sair, cauda a próxima posição
   livre; os índices dão a volta com %. Guardamos n para separar cheia de vazia. */
#define TAM 4
typedef struct { int v[TAM], cabeca, cauda, n; } FilaCircular;

int fc_enfileira(FilaCircular *Q, int x) {       // ENQUEUE
    // cheia: na lista ligada isso não ocorre
    if (Q->n == TAM) return 0;
    Q->v[Q->cauda] = x;
    Q->cauda = (Q->cauda + 1) % TAM;
    Q->n++;
    return 1;
}
int fc_desenfileira(FilaCircular *Q) {           // DEQUEUE (supõe não vazia)
    int x = Q->v[Q->cabeca];
    Q->cabeca = (Q->cabeca + 1) % TAM;
    Q->n--;
    return x;
}

/* Fila em lista simplesmente ligada: entra na cauda, sai da cabeça, ambos O(1). */
typedef struct No { int x; struct No *prox; } No;
typedef struct { No *cabeca, *cauda; } FilaLista;

void fl_enfileira(FilaLista *Q, int x) {
    No *n = malloc(sizeof(No));
    n->x = x;
    n->prox = NULL;
    if (Q->cauda) Q->cauda->prox = n; else Q->cabeca = n;   // fila vazia: caso especial
    Q->cauda = n;
}
int fl_desenfileira(FilaLista *Q) {
    No *n = Q->cabeca;
    int x = n->x;
    Q->cabeca = n->prox;
    if (!Q->cabeca) Q->cauda = NULL;
    free(n);
    return x;
}

int main(void) {
    FilaCircular C = {{0}, 0, 0, 0};
    FilaLista L = {NULL, NULL};
    char op;
    int x;
    while (scanf(" %c", &op) == 1) {
        if (op == 'e' && scanf("%d", &x) == 1) {
            if (!fc_enfileira(&C, x)) printf("fila circular cheia\n");
            fl_enfileira(&L, x);
        } else if (op == 'd') {
            if (!L.cabeca) { printf("fila vazia\n"); continue; }
            int a = fl_desenfileira(&L);
            if (C.n) fc_desenfileira(&C);
            printf("saiu %d\n", a);
        }
    }
    while (L.cabeca) fl_desenfileira(&L);
    return 0;
}
