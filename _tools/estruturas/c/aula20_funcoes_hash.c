// Aula 20 – Comparando funções hash: divisão, multiplicação e hashing universal
// teste: 64 1024 => divisão por 1024: 16 posições usadas
// teste: 64 1024 => divisão por 1021: 1021 posições usadas
#include <stdio.h>
#include <stdlib.h>

/* Lê o passo s e m; insere as chaves s, 2s, 3s, ..., m*s (um padrão comum: endereços
   alinhados, IDs múltiplos de 10) e conta quantas posições cada função usa. */
unsigned divisao(unsigned k, unsigned m) { return k % m; }

unsigned multiplicacao(unsigned k, int p) {     // m = 2^p; A = (√5 - 1)/2 em 32 bits
    unsigned s = 2654435769u;                   // ⌊A · 2^32⌋, sugestão de Knuth
    return (k * s) >> (32 - p);                 // os p bits mais altos de k·s mod 2^32
}

typedef unsigned (*Hash)(unsigned, unsigned);

int usadas(Hash f, unsigned passo, unsigned m, unsigned param) {
    char *ocupada = calloc(m, 1);
    int cont = 0;
    for (unsigned i = 1; i <= m; i++) {
        unsigned pos = f(i * passo, param);
        if (!ocupada[pos]) { ocupada[pos] = 1; cont++; }
    }
    free(ocupada);
    return cont;
}

unsigned mult_aux(unsigned k, unsigned p) { return multiplicacao(k, (int)p); }

int main(void) {
    unsigned passo, m;
    if (scanf("%u %u", &passo, &m) != 2 || m < 2) return 1;
    unsigned primo = m - 1;                     // maior primo menor que m
    for (;; primo--) {
        int ok = 1;
        for (unsigned d = 2; d * d <= primo; d++) if (primo % d == 0) { ok = 0; break; }
        if (ok) break;
    }
    int p = 0;
    while ((1u << p) < m) p++;
    printf("divisão por %u: %d posições usadas\n", m, usadas(divisao, passo, m, m));
    printf("divisão por %u: %d posições usadas\n", primo,
           usadas(divisao, passo, primo, primo));
    printf("multiplicação (m = 2^%d): %d posições usadas\n", p,
           usadas(mult_aux, passo, 1u << p, (unsigned)p));
    return 0;
}
