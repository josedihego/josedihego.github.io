// Aula 28 – Nível 1: Minha primeira função
// teste: 2.5
#include <stdio.h>                                   // printf e scanf
#define PI 3.14159                                   // constante PI = 3.14159

float perimetro(float raio) {                        // recebe o raio, devolve o perímetro
    return 2 * PI * raio;                            // devolve o perímetro
}

int main(void) {                                     // início do programa
    float r;                                         // declara r (float)
    printf("Raio: ");                                // pergunta ao usuário
    scanf("%f", &r);                                 // lê o valor digitado e guarda em r
    printf("Perímetro: %.2f\n", perimetro(r));       // chamada da função
    return 0;                                        // termina com sucesso
}
