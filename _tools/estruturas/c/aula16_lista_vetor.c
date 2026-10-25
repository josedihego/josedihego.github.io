// Aula 16 – Lista em vetores com lista livre (Cormen, seção 10.3)
// teste: i 4;i 1;i 16;i 9;r 16;i 25;p => lista: 25 9 1 4
// teste: i 4;i 1;i 16;i 9;r 16;i 25;p => posições usadas: 4 de 8
#include <stdio.h>

/* Sem ponteiros: prox[], chave[] e ant[] são vetores; um "ponteiro" é um índice e
   -1 faz o papel de NIL. As posições livres formam uma pilha ligada por prox[]:
   ALLOCATE-OBJECT tira do topo e FREE-OBJECT devolve, ambos O(1). */
#define M 8
int prox[M], chave[M], ant[M];
int livre, cabeca = -1;

int aloca(void) {                               // ALLOCATE-OBJECT
    if (livre == -1) return -1;                 // sem espaço
    int x = livre;
    livre = prox[x];
    return x;
}

void libera(int x) {                            // FREE-OBJECT
    prox[x] = livre;
    livre = x;
}

void insere(int k) {                            // na cabeça
    int x = aloca();
    if (x < 0) { printf("sem espaço\n"); return; }
    chave[x] = k;
    prox[x] = cabeca;
    ant[x] = -1;
    if (cabeca >= 0) ant[cabeca] = x;
    cabeca = x;
}

void remove_chave(int k) {
    int x = cabeca;
    while (x >= 0 && chave[x] != k) x = prox[x];
    if (x < 0) return;
    if (ant[x] >= 0) prox[ant[x]] = prox[x]; else cabeca = prox[x];
    if (prox[x] >= 0) ant[prox[x]] = ant[x];
    libera(x);                                  // a posição volta para a lista livre
}

int main(void) {
    for (int i = 0; i < M; i++) prox[i] = i + 1 < M ? i + 1 : -1;   // tudo livre
    livre = 0;
    char c;
    int k;
    while (scanf(" %c", &c) == 1) {
        if (c == 'i' && scanf("%d", &k) == 1) insere(k);
        else if (c == 'r' && scanf("%d", &k) == 1) remove_chave(k);
        else if (c == 'p') {
            int usadas = 0;
            printf("lista:");
            for (int x = cabeca; x >= 0; x = prox[x]) {
                printf(" %d", chave[x]);
                usadas++;
            }
            printf("\nposições usadas: %d de %d\n", usadas, M);
        }
    }
    return 0;
}
