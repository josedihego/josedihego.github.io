// Aula 33 – Nível 1: Um struct para um ponto
#include <stdio.h>                                       // printf
#include <math.h>                                        // sqrt

struct Ponto {                                           // agrupa dados relacionados
    float x, y;                                          // coordenadas
};

int main(void) {                                         // início do programa
    struct Ponto a = {0, 0}, b = {3, 4};                 // dois pontos, campos na ordem x, y
    float d = sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y));   // . acessa um campo
    printf("Distância de (%.0f,%.0f) a (%.0f,%.0f): %.1f\n", a.x, a.y, b.x, b.y, d);   // mostra os valores formatados
    return 0;                                            // termina com sucesso
}
