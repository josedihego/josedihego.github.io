// Aula 21 – Experimento: sondagens no endereçamento aberto, linear contra hash duplo
// Saída CSV: alfa, linear_sem, duplo_sem, linear_com, duplo_com (sondagens médias)
#include <stdio.h>
#include <stdlib.h>

#define P 20                                   // m = 2^20 posições
#define M (1u << P)

unsigned long long estado = 0x9E3779B97F4A7C15ULL;
unsigned long long aleatorio(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return estado;
}

// 0 = vazia (chaves sorteadas nunca são 0)
unsigned *T;

unsigned h1(unsigned long long k) { return (unsigned)(k & (M - 1)); }
// ímpar: primo com 2^20
unsigned h2(unsigned long long k) { return (unsigned)((k >> 32) | 1); }

long sondas;

unsigned posicao(unsigned long long k, unsigned i, int duplo) {
    return duplo ? (h1(k) + i * h2(k)) & (M - 1) : (h1(k) + i) & (M - 1);
}

void insere(unsigned long long k, int duplo) {
    for (unsigned i = 0;; i++) {
        unsigned j = posicao(k, i, duplo);
        if (T[j] == 0) { T[j] = (unsigned)(k >> 1) | 1; return; }
    }
}

void busca(unsigned long long k, int duplo) {  // conta sondagens até achar ou ver vazia
    unsigned alvo = (unsigned)(k >> 1) | 1;
    for (unsigned i = 0;; i++) {
        unsigned j = posicao(k, i, duplo);
        sondas++;
        if (T[j] == 0 || T[j] == alvo) return;
    }
}

int main(void) {
    T = malloc(M * sizeof(unsigned));
    unsigned long long *chaves = malloc(M * sizeof(unsigned long long));
    printf("alfa,linear_sem,duplo_sem,linear_com,duplo_com\n");
    for (int q = 1; q <= 18; q++) {
        double alfa = q * 0.05;
        unsigned n = (unsigned)(alfa * M);
        double r[2][2];
        for (int duplo = 0; duplo <= 1; duplo++) {
            for (unsigned j = 0; j < M; j++) T[j] = 0;
            for (unsigned i = 0; i < n; i++) {
                chaves[i] = aleatorio();
                insere(chaves[i], duplo);
            }
            sondas = 0;
            for (unsigned i = 0; i < n; i++) busca(chaves[i], duplo);
            r[duplo][1] = (double)sondas / n;
            sondas = 0;
            for (int b = 0; b < 200000; b++) busca(aleatorio(), duplo);
            r[duplo][0] = sondas / 200000.0;
        }
        printf("%.2f,%.4f,%.4f,%.4f,%.4f\n", alfa, r[0][0], r[1][0], r[0][1], r[1][1]);
    }
    free(T); free(chaves);
    return 0;
}
