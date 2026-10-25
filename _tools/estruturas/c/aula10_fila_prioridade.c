// Aula 10 – Fila de prioridade com heap de máximo (Cormen, seção 6.5)
// teste: i 5;i 9;i 2;m;x;x;i 7;x;x;f => maior 9
// teste: i 5;i 9;i 2;m;x;x;i 7;x;x;f => extraído 7
// teste: i 5;i 2;x;x;f => extraído 2
// teste: i 1;i 3;a 0 10;x;f => extraído 10
#include <stdio.h>
#include <stdlib.h>

/* Heap de máximo com índices 0..tam-1. Comandos lidos da entrada:
   i x (insere x), m (mostra o máximo), x (extrai o máximo),
   a k v (aumenta a chave da posição k para v), f (fim). */
typedef struct { int *A; int tam, cap; } Fila;

void troca(int A[], int i, int j) { int t = A[i]; A[i] = A[j]; A[j] = t; }

void desce(Fila *f, int i) {                     // MAX-HEAPIFY
    for (;;) {
        int e = 2 * i + 1, d = e + 1, maior = i;
        if (e < f->tam && f->A[e] > f->A[maior]) maior = e;
        if (d < f->tam && f->A[d] > f->A[maior]) maior = d;
        if (maior == i) return;
        troca(f->A, i, maior);
        i = maior;
    }
}

void sobe(Fila *f, int i) {                      // laço de HEAP-INCREASE-KEY
    while (i > 0 && f->A[(i - 1) / 2] < f->A[i]) {
        troca(f->A, i, (i - 1) / 2);
        i = (i - 1) / 2;
    }
}

void insere(Fila *f, int x) {                    // MAX-HEAP-INSERT
    if (f->tam == f->cap) {                      // vetor cheio: dobra a capacidade
        f->cap = f->cap ? 2 * f->cap : 4;
        f->A = realloc(f->A, f->cap * sizeof(int));
    }
    f->A[f->tam++] = x;
    sobe(f, f->tam - 1);
}

int extrai_max(Fila *f) {                        // HEAP-EXTRACT-MAX
    int max = f->A[0];
    f->A[0] = f->A[--f->tam];
    desce(f, 0);
    return max;
}

void aumenta(Fila *f, int k, int v) {            // HEAP-INCREASE-KEY
    if (v < f->A[k]) { printf("nova chave é menor\n"); return; }
    f->A[k] = v;
    sobe(f, k);
}

int main(void) {
    Fila f = {NULL, 0, 0};
    char cmd[4];
    int x, k;
    while (scanf("%3s", cmd) == 1 && cmd[0] != 'f') {
        if (cmd[0] == 'i' && scanf("%d", &x) == 1) insere(&f, x);
        else if (cmd[0] == 'm' && f.tam) printf("maior %d\n", f.A[0]);
        else if (cmd[0] == 'x' && f.tam) printf("extraído %d\n", extrai_max(&f));
        else if (cmd[0] == 'a' && scanf("%d %d", &k, &x) == 2 && k < f.tam)
            aumenta(&f, k, x);
    }
    free(f.A);
    return 0;
}
