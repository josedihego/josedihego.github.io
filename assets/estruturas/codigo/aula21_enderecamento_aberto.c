// Aula 21 – Endereçamento aberto: hash duplo e remoção por marca (Cormen, 11.4)
#include <stdio.h>

#define M 13                                   // tamanho primo, como na Figura 11.5
#define VAZIA -1
// marca: a sondagem continua por cima dela
#define REMOVIDA -2

int T[M];

int h1(int k) { return k % M; }
int h2(int k) { return 1 + k % (M - 2); }      // nunca 0 e primo com M: visita tudo

int sonda(int k, int i) { return (h1(k) + i * h2(k)) % M; }

int insere(int k) {                            // HASH-INSERT
    for (int i = 0; i < M; i++) {
        int j = sonda(k, i);
        if (T[j] == VAZIA || T[j] == REMOVIDA) { T[j] = k; return j; }
    }
    return -1;                                 // tabela cheia
}

int busca(int k) {                             // HASH-SEARCH: para numa posição VAZIA
    for (int i = 0; i < M; i++) {
        int j = sonda(k, i);
        if (T[j] == VAZIA) return -1;
        if (T[j] == k) return j;
    }
    return -1;
}

void remove_chave(int k) {
    int j = busca(k);
    if (j >= 0) T[j] = REMOVIDA;               // não pode virar VAZIA: quebraria buscas
}

int main(void) {
    for (int j = 0; j < M; j++) T[j] = VAZIA;
    char c;
    int k;
    while (scanf(" %c %d", &c, &k) == 2) {
        if (c == 'i') printf("%d na posição %d\n", k, insere(k));
        else if (c == 'b')
            printf(busca(k) >= 0 ? "%d encontrado\n" : "%d ausente\n", k);
        else if (c == 'r') remove_chave(k);
    }
    return 0;
}
