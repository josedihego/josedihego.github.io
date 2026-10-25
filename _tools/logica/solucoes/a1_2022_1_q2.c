// A1-2022.1 – Questão II: Relógio de Chronos – hora a partir dos ângulos dos ponteiros
// teste: 195 180 => 06:30
// teste: 180 0 => 06:00
// teste: 359 354 => 11:59
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int ang_hora, ang_min;                              // ângulos dos ponteiros de hora e de minutos (graus)
    printf("Ângulos (hora minuto): ");                  // pede os ângulos
    scanf("%d %d", &ang_hora, &ang_min);                // lê os dois inteiros
    int horas = ang_hora / 30;                          // 360 graus / 12 horas = 30 graus por hora
    int minutos = ang_min / 6;                          // 360 graus / 60 minutos = 6 graus por minuto
    printf("%02d:%02d\n", horas, minutos);              // %02d completa com zero à esquerda
    return 0;                                           // fim sem erro
}
