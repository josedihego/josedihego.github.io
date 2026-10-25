// A1-2024.2 – Questão I: Área sombreada entre o quadrado e o círculo inscrito
// teste: 1 => 0.86
// teste: 2.5 => 5.38
#include <stdio.h>                                      // printf e scanf
#define PI 3.14                                         // o enunciado manda usar 3.14

int main(void) {                                        // início do programa
    double r;                                           // raio do círculo
    printf("r: ");                                      // pede o raio
    scanf("%lf", &r);                                   // lê o raio
    double lado = 2 * r;                                // o círculo inscrito toca os 4 lados: lado = diâmetro
    double quadrado = lado * lado;                      // área do quadrado = lado²
    double circulo = PI * r * r;                        // área do círculo = π r²
    printf("Área sombreada: %.2f\n", quadrado - circulo);   // o que sobra do quadrado
    return 0;                                           // fim sem erro
}
