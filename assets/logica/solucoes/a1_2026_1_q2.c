// A1-2026.1 – Questão II: Números n-binariamente distintos
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n, a, b;                                        // limiar n e os dois números (menores que 16)
    printf("n, a e b: ");                               // pede os dados
    scanf("%d %d %d", &n, &a, &b);                      // lê os três inteiros
    int x = a ^ b;                                      // OU exclusivo: bit 1 onde a e b diferem
    int diferentes = (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1) + ((x >> 3) & 1);   // conta os 4 bits
    if (diferentes >= n) printf("%d e %d são %d-binariamente distintos\n", a, b, n); // bits diferentes suficientes
    else printf("%d e %d não são %d-binariamente distintos\n", a, b, n);   // menos bits diferentes que n
    return 0;                                           // fim sem erro
}
