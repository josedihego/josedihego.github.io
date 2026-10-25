// A2-2014.2 – Questão III: Soma dos recíprocos dos números triangulares
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // quantidade de termos
    printf("N: ");                                      // pede N
    scanf("%d", &n);                                    // lê N
    long triangular = 0;                                // número triangular atual
    double soma = 0;                                    // acumulador da série (começa em zero)
    for (int k = 1; k <= n; k++) {                      // k-ésimo termo
        triangular += k;                                // o próximo triangular é o anterior + k
        soma += 1.0 / triangular;                       // 1.0: divisão real (1 / 3 inteiro daria 0)
    }
    printf("S = %.6f\n", soma);                         // 1 + 1/3 + 1/6 + ...
    return 0;                                           // fim sem erro
}
