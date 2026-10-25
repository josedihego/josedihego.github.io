// Aula 19 – Experimento: custo da busca no encadeamento em função do fator de carga
// Saída CSV: alfa, sem_sucesso, com_sucesso (elementos examinados por busca, em média)
#include <stdio.h>
#include <stdlib.h>

typedef struct No { unsigned chave; struct No *prox; } No;

unsigned long long estado = 88172645463325252ULL;
unsigned long long aleatorio(void) {           // xorshift64: rápido e de boa qualidade
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return estado;
}

int main(void) {
    int m = 1 << 16;                           // posições da tabela
    printf("alfa,sem_sucesso,com_sucesso\n");
    for (int q = 1; q <= 16; q++) {
        double alfa = q * 0.25;
        int n = (int)(alfa * m);
        No **T = calloc(m, sizeof(No *));
        No *nos = malloc(n * sizeof(No));
        unsigned *chaves = malloc(n * sizeof(unsigned));
        for (int i = 0; i < n; i++) {          // chaves aleatórias distintas o bastante
            chaves[i] = (unsigned)aleatorio();
            // hash uniforme: os bits já são aleatórios
            int pos = chaves[i] % m;
            nos[i].chave = chaves[i];
            nos[i].prox = T[pos];
            T[pos] = &nos[i];
        }
        long examinados = 0;
        for (int i = 0; i < n; i++)            // busca com sucesso por cada chave
            for (No *x = T[chaves[i] % m]; x; x = x->prox) {
                examinados++;
                if (x->chave == chaves[i]) break;
            }
        double com = (double)examinados / n;
        examinados = 0;
        int buscas = 200000;
        // busca sem sucesso: percorre a lista toda
        for (int b = 0; b < buscas; b++) {
            unsigned k = (unsigned)aleatorio();
            for (No *x = T[k % m]; x; x = x->prox) examinados++;
        }
        printf("%.2f,%.4f,%.4f\n", alfa, (double)examinados / buscas, com);
        free(T); free(nos); free(chaves);
    }
    return 0;
}
