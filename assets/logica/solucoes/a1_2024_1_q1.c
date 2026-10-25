// A1-2024.1 – Questão I: Acelerador de partículas – qual sensor foi atingido?
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int d;                                              // distância total percorrida (km)
    printf("Distância total (km): ");                   // pede a distância
    scanf("%d", &d);                                    // lê a distância
    // pela figura: os trechos fixos do emissor ao acelerador e da saída ao sensor somam 5 km,
    // e cada volta completa tem 8 km; o que sobra das voltas indica a saída (1, 2 ou 3)
    int sensor = (d - 5) % 8;                           // resto depois de tirar os trechos fixos e as voltas
    if (sensor >= 1 && sensor <= 3) printf("A partícula atinge o sensor %d\n", sensor); // só existem os sensores 1, 2 e 3
    else printf("Distância incompatível com o acelerador\n");   // não corresponde a nenhuma saída
    return 0;                                           // fim sem erro
}
