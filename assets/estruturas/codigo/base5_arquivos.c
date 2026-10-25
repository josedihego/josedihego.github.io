// Base 5 – Arquivos, argumentos e erros: texto, binário, argc/argv, perror e assert
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* Lê n e n inteiros; grava-os num arquivo texto e num binário; lê de volta.
   Opcionalmente, o nome-base dos arquivos vem da linha de comando (argv[1]). */
int main(int argc, char *argv[]) {
    const char *base = argc > 1 ? argv[1] : "dados";   // argv[0] é o nome do programa
    char nome_txt[256], nome_bin[256];
    snprintf(nome_txt, sizeof nome_txt, "%s.txt", base);
    snprintf(nome_bin, sizeof nome_bin, "%s.bin", base);
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int *v = malloc(n * sizeof *v);
    for (int i = 0; i < n; i++)
        if (scanf("%d", &v[i]) != 1) return 1;
    FILE *f = fopen(nome_txt, "w");
    if (!f) { perror(nome_txt); return 1; }   // perror explica o motivo (errno)
    for (int i = 0; i < n; i++) fprintf(f, "%d\n", v[i]);
    fclose(f);
    FILE *g = fopen(nome_bin, "wb");
    if (!g) { perror(nome_bin); return 1; }
    size_t escritos = fwrite(v, sizeof *v, n, g);  // os bytes da memória, como estão
    assert(escritos == (size_t)n);             // falha aqui = erro de programação
    fclose(g);
    f = fopen(nome_txt, "r");
    long soma = 0;
    int x, lidos = 0;
    while (fscanf(f, "%d", &x) == 1) { soma += x; lidos++; }
    fclose(f);
    printf("média lida do arquivo texto: %.2f\n", (double)soma / lidos);
    g = fopen(nome_bin, "rb");
    fseek(g, 0, SEEK_END);                     // tamanho = posição do fim
    printf("arquivo binário: %ld bytes\n", ftell(g));
    fclose(g);
    remove(nome_txt);
    remove(nome_bin);
    free(v);
    return 0;
}
