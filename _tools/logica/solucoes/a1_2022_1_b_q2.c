// A1-2022.1 (B) – Questão II: Quantas vezes cada dígito aparece de A até B
// teste: 1 9 => 0 1 1 1 1 1 1 1 1 1
// teste: 10 22 => 2 12 5 1 1 1 1 1 1 1
// teste: 1000 1000 => 3 1 0 0 0 0 0 0 0 0
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int a, b;                                           // intervalo [A, B]
    printf("A e B: ");                                  // pede o intervalo
    scanf("%d %d", &a, &b);                             // lê os dois limites
    int conta[10] = {0};                                // conta[d] = quantas vezes o dígito d apareceu (tudo zero)
    for (int n = a; n <= b; n++) {                      // cada número do intervalo
        int x = n;                                      // cópia para desmontar em dígitos
        while (x > 0) {                                 // percorre os dígitos (sem zeros à esquerda)
            conta[x % 10]++;                            // o dígito vira o índice do vetor
            x /= 10;                                    // próximo dígito
        }
    }
    for (int d = 0; d < 10; d++) printf("%d%s", conta[d], d < 9 ? " " : "\n");   // as 10 contagens
    return 0;                                           // fim sem erro
}
