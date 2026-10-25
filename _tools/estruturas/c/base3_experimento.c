// Base 3 – Experimento: vetor de structs (AoS) contra struct de vetores (SoA)
// Saída CSV: n, aos_ns, soa_ns (somar um campo de n registros; tempo por registro)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 64 bytes
typedef struct { double nota; char nome[48]; int idade; int turma; } Registro;

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

volatile double ralo;

int main(void) {
    printf("n,aos_ns,soa_ns\n");
    for (int n = 1 << 12; n <= 1 << 23; n *= 2) {
        // AoS: registros inteiros
        Registro *aos = malloc((size_t)n * sizeof *aos);
        // SoA: um vetor por campo
        double *notas = malloc((size_t)n * sizeof *notas);
        for (int i = 0; i < n; i++) { aos[i].nota = i % 10; notas[i] = i % 10; }
        int voltas = (1 << 25) / n;
        double t0 = agora(), s = 0;
        for (int r = 0; r < voltas; r++)
            // usa 8 de cada 64 bytes
            for (int i = 0; i < n; i++) s += aos[i].nota;
        double t1 = agora();
        for (int r = 0; r < voltas; r++)
            // usa todos os bytes lidos
            for (int i = 0; i < n; i++) s += notas[i];
        double t2 = agora();
        ralo = s;
        double total = (double)n * voltas;
        printf("%d,%.4f,%.4f\n", n, (t1 - t0) / total * 1e9, (t2 - t1) / total * 1e9);
        free(aos); free(notas);
    }
    return 0;
}
