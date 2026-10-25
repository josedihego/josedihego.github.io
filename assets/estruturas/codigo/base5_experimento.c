// Base 5 – Experimento: arquivo texto contra arquivo binário
// Saída CSV: n, bytes_texto, bytes_binario, texto_ns, binario_ns
// (n inteiros de 0 a 999.999: tamanho e tempo de escrita + leitura por número)
#define _POSIX_C_SOURCE 199309L   // clock_gettime com -std=c17
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double agora(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return t.tv_sec + t.tv_nsec / 1e9;
}

long tamanho(const char *nome) {
    FILE *f = fopen(nome, "rb");
    fseek(f, 0, SEEK_END);
    long t = ftell(f);
    fclose(f);
    return t;
}

int main(void) {
    srand(5);
    const char *txt = "/tmp/base5_experimento.txt", *bin = "/tmp/base5_experimento.bin";
    printf("n,bytes_texto,bytes_binario,texto_ns,binario_ns\n");
    for (int n = 1 << 14; n <= 1 << 21; n *= 2) {
        int *v = malloc(n * sizeof *v), *w = malloc(n * sizeof *w);
        for (int i = 0; i < n; i++) v[i] = rand() % 1000000;
        double t0 = agora();
        FILE *f = fopen(txt, "w");
        for (int i = 0; i < n; i++) fprintf(f, "%d\n", v[i]);
        fclose(f);
        f = fopen(txt, "r");
        for (int i = 0; i < n; i++)
            if (fscanf(f, "%d", &w[i]) != 1) return 1;
        fclose(f);
        double t1 = agora();
        f = fopen(bin, "wb");
        fwrite(v, sizeof *v, n, f);
        fclose(f);
        f = fopen(bin, "rb");
        if (fread(w, sizeof *w, n, f) != (size_t)n) return 1;
        fclose(f);
        double t2 = agora();
        printf("%d,%ld,%ld,%.2f,%.2f\n", n, tamanho(txt), tamanho(bin),
               (t1 - t0) / n * 1e9, (t2 - t1) / n * 1e9);
        free(v); free(w);
    }
    remove(txt);
    remove(bin);
    return 0;
}
