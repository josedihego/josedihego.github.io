// Aula 11 – Experimento: custo por operação de pilha em vetor e em lista ligada
// Saída CSV: n, vetor_ns, lista_ns (n PUSH seguidos de n POP; tempo por operação)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

typedef struct No { long x; struct No *prox; } No;
volatile long ralo;

int main(void) {
    printf("n,vetor_ns,lista_ns\n");
    for (long n = 1 << 12; n <= 1 << 22; n *= 2) {
        double tv = 1e30, tl = 1e30;
        for (int rep = 0; rep < 5; rep++) {
            long *v = malloc(n * sizeof(long)), topo = 0, s = 0;
            double t0 = agora();
            for (long i = 0; i < n; i++) v[topo++] = i;           // PUSH
            while (topo) s += v[--topo];                           // POP
            double t1 = agora();
            free(v);
            No *pilha = NULL;
            double t2 = agora();
            // PUSH: um malloc por nó
            for (long i = 0; i < n; i++) {
                No *no = malloc(sizeof(No));
                no->x = i; no->prox = pilha; pilha = no;
            }
            // POP: um free por nó
            while (pilha) {
                No *no = pilha; s += no->x; pilha = no->prox; free(no);
            }
            double t3 = agora();
            ralo = s;
            if (t1 - t0 < tv) tv = t1 - t0;
            if (t3 - t2 < tl) tl = t3 - t2;
        }
        printf("%ld,%.3f,%.3f\n", n, tv / (2 * n) * 1e9, tl / (2 * n) * 1e9);
    }
    return 0;
}
