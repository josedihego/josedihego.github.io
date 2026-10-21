// Aula 4 – Nível 2: Hipotenusa com math.h
#include <stdio.h>                                   // printf e scanf
#include <math.h>                                    // sqrt e pow (compile com -lm)

int main(void) {                                     // início do programa
    float c1, c2;                                    // catetos
    printf("Cateto 1: ");                            // pergunta ao usuário
    scanf("%f", &c1);                                // lê o valor digitado e guarda em c1
    printf("Cateto 2: ");                            // pergunta ao usuário
    scanf("%f", &c2);                                // lê o valor digitado e guarda em c2
    float h = sqrt(pow(c1, 2) + pow(c2, 2));         // h = √(c1² + c2²)
    printf("Hipotenusa: %.3f\n", h);                 // mostra h formatados
    return 0;                                        // termina com sucesso
}
