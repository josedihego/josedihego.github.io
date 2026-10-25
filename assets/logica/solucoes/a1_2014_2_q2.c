// A1-2014.2 – Questão II: Graus, minutos e segundos para graus decimais
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int graus, minutos, segundos;                       // coordenada lida
    printf("Graus minutos segundos: ");                 // pede os três valores
    scanf("%d %d %d", &graus, &minutos, &segundos);     // lê os três inteiros
    double decimal = graus + minutos / 60.0 + segundos / 3600.0;   // 60.0 e 3600.0: divisão real, não inteira
    printf("%.5f graus decimais\n", decimal);           // 5 casas, como no exemplo da prova
    return 0;                                           // fim sem erro
}
