// Aula 6 – Nível 3: Bhaskara com teste do delta
#include <stdio.h>                                              // printf e scanf
#include <math.h>                                               // sqrt

int main(void) {                                                // início do programa
    float a, b, c;                                              // coeficientes
    printf("a b c: ");                                          // pergunta ao usuário
    scanf("%f %f %f", &a, &b, &c);                              // lê os três de uma vez
    float delta = b * b - 4 * a * c;                            // discriminante
    if (delta < 0) {                                            // sem raízes reais
        printf("Delta = %.2f: não há raízes reais\n", delta);   // mostra delta formatados
    } else {                                                    // delta >= 0
        float x1 = (-b + sqrt(delta)) / (2 * a);                // primeira raiz
        float x2 = (-b - sqrt(delta)) / (2 * a);                // segunda raiz
        printf("x1 = %.3f e x2 = %.3f\n", x1, x2);              // mostra x1 e x2 formatados
    }
    return 0;                                                   // termina com sucesso
}
