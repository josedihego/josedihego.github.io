// Aula 16 – Experimento: busca com e sem sentinela
// Saída CSV: n, sem_sentinela, com_sentinela, sem_ns, com_ns
// (testes feitos numa busca sem sucesso; tempo por elemento visitado)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

long testes;

/* Sem sentinela: cada passo testa "acabou?" e "é a chave?". */
int busca_sem(const int v[], int n, int k) {
    int i = 0;
    while ((testes++, i < n) && (testes++, v[i] != k)) i++;
    return i < n ? i : -1;
}

/* Com sentinela: a chave é copiada para v[n]; o laço não precisa testar o fim. */
int busca_com(int v[], int n, int k) {
    v[n] = k;
    int i = 0;
    while (testes++, v[i] != k) i++;
    return i < n ? i : -1;
}

int main(void) {
    printf("n,sem_sentinela,com_sentinela,sem_ns,com_ns\n");
    for (int n = 1 << 10; n <= 1 << 20; n *= 2) {
        int *v = malloc((n + 1) * sizeof(int));
        for (int i = 0; i < n; i++) v[i] = 2 * i;      // só pares: buscar 1 falha
        testes = 0; busca_sem(v, n, 1); long a = testes;
        testes = 0; busca_com(v, n, 1); long b = testes;
        int voltas = (1 << 26) / n;
        double t0 = agora();
        for (int r = 0; r < voltas; r++) busca_sem(v, n, 1);
        double t1 = agora();
        for (int r = 0; r < voltas; r++) busca_com(v, n, 1);
        double t2 = agora();
        double visitas = (double)n * voltas;
        printf("%d,%ld,%ld,%.4f,%.4f\n", n, a, b, (t1 - t0) / visitas * 1e9,
               (t2 - t1) / visitas * 1e9);
        free(v);
    }
    return 0;
}
