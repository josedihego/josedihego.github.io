// Aula 23 – Experimento: altura de árvores de busca construídas aleatoriamente
// Tabela 1 (n, altura_media): média de 10 árvores com chaves aleatórias
// Tabela 2 (n, ordenada): altura quando as chaves chegam em ordem crescente
#include <stdio.h>
#include <stdlib.h>

typedef struct No { unsigned chave; struct No *esq, *dir; } No;

unsigned long long estado = 0x853C49E6748FEA9BULL;
unsigned aleatorio(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)(estado >> 16);
}

int altura_apos_inserir(No nos[], int n, int ordenada) {
    No *raiz = NULL;
    int h = 0;
    for (int i = 0; i < n; i++) {
        nos[i].chave = ordenada ? (unsigned)i : aleatorio();
        nos[i].esq = nos[i].dir = NULL;
        No **lugar = &raiz;
        int prof = 0;                          // profundidade em que o nó vai entrar
        while (*lugar) {
            No *x = *lugar;
            lugar = nos[i].chave < x->chave ? &x->esq : &x->dir;
            prof++;
        }
        *lugar = &nos[i];
        if (prof > h) h = prof;
    }
    return h;
}

int main(void) {
    No *nos = malloc((1 << 21) * sizeof(No));
    printf("n,altura_media\n");
    for (int n = 1 << 10; n <= 1 << 21; n *= 2) {
        double soma = 0;
        for (int r = 0; r < 10; r++) soma += altura_apos_inserir(nos, n, 0);
        printf("%d,%.2f\n", n, soma / 10);
    }
    printf("\nn,ordenada\n");
    for (int n = 500; n <= 8000; n += 500)
        printf("%d,%d\n", n, altura_apos_inserir(nos, n, 1));
    free(nos);
    return 0;
}
