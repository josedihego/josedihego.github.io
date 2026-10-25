// Aula 11 – Pilhas em vetor e em lista ligada; avaliação de expressões pós-fixas
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Duas implementações com a mesma interface: PUSH, POP, STACK-EMPTY. */
#define TAM 100
typedef struct { double v[TAM]; int topo; } PilhaVetor;     // Cormen: S[1..n], S.top

int pv_vazia(const PilhaVetor *S) { return S->topo == 0; }
int pv_empilha(PilhaVetor *S, double x) {
    // transbordamento (overflow)
    if (S->topo == TAM) return 0;
    S->v[S->topo++] = x;
    return 1;
}
double pv_desempilha(PilhaVetor *S) { return S->v[--S->topo]; }   // supõe não vazia

typedef struct No { double x; struct No *prox; } No;         // pilha ligada: sem limite
typedef struct { No *topo; } PilhaLista;

void pl_empilha(PilhaLista *S, double x) {                   // insere na cabeça: O(1)
    No *n = malloc(sizeof(No));
    n->x = x;
    n->prox = S->topo;
    S->topo = n;
}
double pl_desempilha(PilhaLista *S) {                        // remove a cabeça: O(1)
    No *n = S->topo;
    double x = n->x;
    S->topo = n->prox;
    free(n);
    return x;
}

/* Expressão pós-fixa (notação polonesa reversa): operandos são empilhados; um
   operador desempilha dois, calcula e empilha o resultado. */
int main(void) {
    char tok[32];
    PilhaVetor S = {{0}, 0};
    PilhaLista L = {NULL};
    while (scanf("%31s", tok) == 1) {
        if (strchr("+-*/", tok[0]) && tok[1] == '\0') {
            if (S.topo < 2) { printf("expressão inválida\n"); return 1; }
            double b = pv_desempilha(&S), a = pv_desempilha(&S);
            double r = tok[0] == '+' ? a + b : tok[0] == '-' ? a - b
                     : tok[0] == '*' ? a * b : a / b;
            pv_empilha(&S, r);
            pl_desempilha(&L); pl_desempilha(&L);
            pl_empilha(&L, r);
        } else {
            pv_empilha(&S, atof(tok));
            pl_empilha(&L, atof(tok));
        }
    }
    if (S.topo != 1) { printf("expressão inválida\n"); return 1; }
    printf("%g\n", pv_desempilha(&S));
    printf("(a pilha ligada concorda: %g)\n", pl_desempilha(&L));
    return 0;
}
