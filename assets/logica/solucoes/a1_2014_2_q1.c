// A1-2014.2 – Questão I: Probabilidade de dois eventos independentes
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    double pa, pb;                                      // probabilidades lidas (entre 0 e 1)
    printf("P(A) e P(B): ");                            // pede as duas probabilidades
    scanf("%lf %lf", &pa, &pb);                         // %lf lê um double
    double ambos = pa * pb;                             // P(A e B) = P(A) x P(B)
    double algum = pa + pb - ambos;                     // P(A ou B) = P(A) + P(B) - P(A e B)
    printf("P(A e B) = %.4f\n", ambos);                 // os dois eventos acontecem
    printf("P(A ou B) = %.4f\n", algum);                // pelo menos um acontece
    return 0;                                           // fim sem erro
}
