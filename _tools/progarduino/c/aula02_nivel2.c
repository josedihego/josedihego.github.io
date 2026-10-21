// Aula 2 – Nível 2: Área e perímetro de uma placa
// teste: 
#include <stdio.h>                                         // printf

int main(void) {                                           // início do programa
    float largura = 10.5;                                  // largura da placa em cm
    float altura = 7.2;                                    // altura da placa em cm
    float area = largura * altura;                         // área = largura × altura
    float perimetro = 2 * (largura + altura);              // soma dos quatro lados
    printf("Placa de %.1f x %.1f cm\n", largura, altura);  // vários valores no mesmo printf
    printf("Área: %.2f cm²\n", area);                      // resultado com 2 casas
    printf("Perímetro: %.2f cm\n", perimetro);             // mostra perimetro formatados
    return 0;                                              // termina com sucesso
}
