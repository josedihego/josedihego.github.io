// Aula 15 – Experimento: problema de Josefo com lista circular e com vetor
// Saída CSV: n, lista, vetor (passos na lista; elementos deslocados no vetor; k = 3)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { int chave; struct No *prox; } No;

int main(void) {
    int k = 3;
    printf("n,lista,vetor\n");
    for (int n = 2000; n <= 32000; n += 2000) {
        No *nos = malloc(n * sizeof(No));        // lista circular simples
        for (int i = 0; i < n; i++) {
            nos[i].chave = i + 1;
            nos[i].prox = &nos[(i + 1) % n];      // o último aponta para o primeiro
        }
        No *ant = &nos[n - 1];
        long passos = 0;
        for (int restam = n; restam > 1; restam--) {
            for (int p = 1; p < k; p++) { ant = ant->prox; passos++; }   // anda k - 1
            ant->prox = ant->prox->prox;          // remove o seguinte: O(1)
        }
        int sobra_lista = ant->chave;
        int *v = malloc(n * sizeof(int));        // vetor: acha a posição em O(1),
        for (int i = 0; i < n; i++) v[i] = i + 1;   // mas remover desloca o resto
        long desloc = 0;
        int tam = n, pos = 0;
        while (tam > 1) {
            pos = (pos + k - 1) % tam;
            for (int j = pos; j < tam - 1; j++) { v[j] = v[j + 1]; desloc++; }
            tam--;
            if (pos == tam) pos = 0;
        }
        if (v[0] != sobra_lista) {              // as duas soluções têm de concordar
            fprintf(stderr, "sobreviventes diferentes!\n");
            return 1;
        }
        printf("%d,%ld,%ld\n", n, passos, desloc);
        free(nos); free(v);
    }
    return 0;
}
