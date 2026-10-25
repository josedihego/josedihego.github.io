// Base 4 – Experimento: quanto a recursão gasta da pilha e quantas vezes o qsort chama
// Tabela 1 (n, bytes_pilha): profundidade n da recursão contra bytes de pilha usados
// Tabela 2 (n, chamadas): chamadas do comparador do qsort para n inteiros aleatórios
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

uintptr_t base;
uintptr_t mais_fundo;

/* A cada chamada, guardamos o endereço de uma variável local: a diferença entre o
   primeiro e o último endereço é a pilha usada. noinline impede o compilador de
   transformar a recursão num laço. */
__attribute__((noinline)) long desce(int n) {
    volatile char local[40];                   // um quadro com algum conteúdo
    local[0] = (char)n;
    uintptr_t aqui = (uintptr_t)&local[0];
    if (aqui < mais_fundo) mais_fundo = aqui;
    if (n == 0) return local[0];
    return desce(n - 1) + local[0];
}

long chamadas;
int compara(const void *a, const void *b) {
    chamadas++;
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int main(void) {
    printf("n,bytes_pilha\n");
    volatile char marca;
    for (int n = 1000; n <= 16000; n += 1000) {
        base = mais_fundo = (uintptr_t)&marca;
        desce(n);
        printf("%d,%lu\n", n, (unsigned long)(base - mais_fundo));
    }
    printf("\nn,chamadas\n");
    srand(4);
    int *v = malloc((1 << 20) * sizeof *v);
    for (int n = 1 << 10; n <= 1 << 20; n *= 2) {
        for (int i = 0; i < n; i++) v[i] = rand();
        chamadas = 0;
        qsort(v, n, sizeof *v, compara);
        printf("%d,%ld\n", n, chamadas);
    }
    free(v);
    return 0;
}
