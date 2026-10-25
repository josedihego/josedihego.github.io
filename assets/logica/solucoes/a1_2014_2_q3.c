// A1-2014.2 – Questão III: Três valores formam um triângulo?
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    double a, b, c;                                     // os três comprimentos
    printf("Três lados: ");                             // pede os lados
    scanf("%lf %lf %lf", &a, &b, &c);                   // lê os três valores
    if (a < b + c && b < a + c && c < a + b) {          // cada lado menor que a soma dos outros dois
        printf("Os valores podem ser lados de um triângulo\n"); // desigualdade triangular satisfeita
    } else {                                            // basta uma condição falhar
        printf("Os valores não podem ser lados de um triângulo\n"); // algum lado é grande demais
    }
    return 0;                                           // fim sem erro
}
