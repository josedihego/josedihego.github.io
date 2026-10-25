// A1-2017.1 – Questão III: Gangorra – equilibrada ou pende para qual lado?
// teste: 30 100 60 50 => equilibrada
// teste: 30 100 30 50 => lado 1
// teste: 20 100 30 80 => lado 2
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int p1, c1, p2, c2;                                 // pesos e comprimentos dos lados 1 e 2
    printf("P1 C1 P2 C2: ");                            // pede os quatro valores
    scanf("%d %d %d %d", &p1, &c1, &p2, &c2);           // lê os quatro valores
    int lado1 = p1 * c1;                                // momento do lado 1
    int lado2 = p2 * c2;                                // momento do lado 2
    if (lado1 == lado2) printf("A gangorra fica equilibrada\n");   // P1 x C1 = P2 x C2
    else if (lado1 > lado2) printf("A gangorra pende para o lado 1\n");   // lado 1 mais "pesado"
    else printf("A gangorra pende para o lado 2\n");    // senão, pende para o lado 2
    return 0;                                           // fim sem erro
}
