// Aula 28 – Nível 2: Funções para resistores
// teste: 330; 470
#include <stdio.h>                                         // printf e scanf

float serie(float r1, float r2) {                          // dois parâmetros
    return r1 + r2;                                        // devolve a resistência em série
}

float paralelo(float r1, float r2) {                       // resistência em paralelo de dois resistores
    return r1 * r2 / (r1 + r2);                            // produto ÷ soma
}

int main(void) {                                           // início do programa
    float a, b;                                            // os dois resistores
    printf("R1 e R2: ");                                   // pergunta ao usuário
    scanf("%f %f", &a, &b);                                // lê o valor digitado e guarda em a, b
    printf("Série: %.1f | Paralelo: %.1f\n", serie(a, b), paralelo(a, b));   // mostra os valores formatados
    printf("Paralelo de 3 iguais: %.1f\n", paralelo(paralelo(a, a), a));   // uma chamada dentro da outra
    return 0;                                              // termina com sucesso
}
