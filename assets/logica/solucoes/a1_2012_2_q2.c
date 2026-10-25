// A1-2012.2 – Questão II: Duração de uma aula (hora:minuto)
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int h1, m1, h2, m2;                                 // entrada (h1:m1) e saída (h2:m2)
    printf("Entrada (h m) e saída (h m): ");            // pede os dois horários
    scanf("%d %d %d %d", &h1, &m1, &h2, &m2);           // lê os quatro inteiros
    int inicio = h1 * 60 + m1;                          // tudo em minutos desde 00:00
    int fim = h2 * 60 + m2;                             // idem para a saída
    if (fim < inicio) fim = fim + 24 * 60;              // saiu depois da meia-noite: soma um dia
    int duracao = fim - inicio;                         // duração em minutos
    printf("Duração: %d:%02d\n", duracao / 60, duracao % 60);   // / dá as horas, % os minutos restantes
    return 0;                                           // fim sem erro
}
