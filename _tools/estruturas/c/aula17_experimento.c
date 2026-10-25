// Aula 17 – Experimento: lista ligada contra vetor
// Tabela 1 (n, vetor, lista): elementos movidos para n inserções no INÍCIO
// Tabela 2 (n, vetor_ns, lista_ns): tempo por elemento para percorrer tudo
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct No { long chave; struct No *prox; } No;

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

volatile long ralo;

int main(void) {
    srand(17);
    printf("n,vetor,lista\n");
    for (long n = 2000; n <= 32000; n += 2000) {
        long movidos = 0;              // vetor: inserir no início desloca todos
        for (long tam = 0; tam < n; tam++) movidos += tam;
        printf("%ld,%ld,%ld\n", n, movidos, 0L);   // lista: só ajusta ponteiros
    }
    printf("\nn,vetor_ns,lista_ns\n");
    for (long n = 1 << 10; n <= 1 << 24; n *= 4) {
        long *v = malloc(n * sizeof(long));
        No *nos = malloc(n * sizeof(No));
        long *ordem = malloc(n * sizeof(long));
        for (long k = 0; k < n; k++) { v[k] = k; ordem[k] = k; }
        for (long k = n - 1; k > 0; k--) {      // nós espalhados pela memória
            long r = ((long)rand() << 15 ^ rand()) % (k + 1);
            long t = ordem[k];
            ordem[k] = ordem[r]; ordem[r] = t;
        }
        for (long k = 0; k < n; k++) {
            nos[ordem[k]].chave = k;
            nos[ordem[k]].prox = k + 1 < n ? &nos[ordem[k + 1]] : NULL;
        }
        long voltas = (1L << 25) / n;           // ~33 milhões de visitas por medida
        double t0 = agora();
        long s = 0;
        for (long r = 0; r < voltas; r++)
            for (long k = 0; k < n; k++) s += v[k];
        double t1 = agora();
        for (long r = 0; r < voltas; r++)
            for (No *x = &nos[ordem[0]]; x; x = x->prox) s += x->chave;
        double t2 = agora();
        ralo = s;
        double visitas = (double)n * voltas;
        printf("%ld,%.3f,%.3f\n", n, (t1 - t0) / visitas * 1e9,
               (t2 - t1) / visitas * 1e9);
        free(v); free(nos); free(ordem);
    }
    return 0;
}
