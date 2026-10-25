// Aula 16 – Pilha com vetor dinâmico e fila circular (Cormen, seções 10.1 e 17.4)
#include <stdio.h>
#include <stdlib.h>

/* Pilha que dobra a capacidade quando enche: PUSH custa O(1) amortizado. */
typedef struct { char *v; int topo, cap; } Pilha;

void empilha(Pilha *p, char c) {
    if (p->topo == p->cap) {
        p->cap = p->cap ? 2 * p->cap : 4;
        p->v = realloc(p->v, p->cap);
    }
    p->v[p->topo++] = c;
}
int vazia(const Pilha *p) { return p->topo == 0; }
char desempilha(Pilha *p) { return p->v[--p->topo]; }   // supõe não vazia

/* Fila circular de tamanho fixo (Figura 10.2): cabeca e cauda dão a volta. */
#define TAM_FILA 8
typedef struct { int v[TAM_FILA]; int cabeca, cauda, n; } Fila;

int enfileira(Fila *f, int x) {
    if (f->n == TAM_FILA) return 0;                     // transbordamento
    f->v[f->cauda] = x;
    f->cauda = (f->cauda + 1) % TAM_FILA;
    f->n++;
    return 1;
}
int desenfileira(Fila *f) {                             // supõe não vazia
    int x = f->v[f->cabeca];
    f->cabeca = (f->cabeca + 1) % TAM_FILA;
    f->n--;
    return x;
}

int balanceada(const char *s) {                         // aplicação clássica da pilha
    Pilha p = {NULL, 0, 0};
    int ok = 1;
    for (int i = 0; s[i] && ok; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') empilha(&p, c);
        else if (c == ')' || c == ']' || c == '}') {
            char esperado = c == ')' ? '(' : c == ']' ? '[' : '{';
            ok = !vazia(&p) && desempilha(&p) == esperado;
        }
    }
    ok = ok && vazia(&p);
    free(p.v);
    return ok;
}

int main(void) {
    char s[1001];
    if (scanf("%1000s", s) != 1) return 1;
    printf(balanceada(s) ? "balanceada\n" : "não balanceada\n");
    Fila f = {{0}, 0, 0, 0};                            // demonstração da fila circular
    for (int x = 1; x <= 10; x++)
        if (!enfileira(&f, x)) desenfileira(&f), enfileira(&f, x);
    printf("fila (mais antigo primeiro):");
    while (f.n) printf(" %d", desenfileira(&f));
    printf("\n");
    return 0;
}
