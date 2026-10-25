// A2-2016.1 – Questão III: Corredor de salas – máximo de vidas
// teste: -2 5 -1 8 -11 7 3 0 0 0 => 12 vidas
// teste: 1 2 3 4 5 6 7 8 9 10 => 55 vidas
// teste: -5 -5 4 -1 -1 3 -9 2 -8 -1 => 5 vidas
#include <stdio.h>                                      // printf e scanf
#define N 10                                            // salas do corredor

int main(void) {                                        // início do programa
    int v[N];                                           // vidas ganhas em cada sala
    for (int i = 0; i < N; i++) scanf("%d", &v[i]);     // lê as 10 salas
    int melhor = v[0];                                  // melhor soma encontrada
    for (int ini = 0; ini < N; ini++) {                 // sala de entrada
        int soma = 0;                                   // vidas de ini até fim
        for (int fim = ini; fim < N; fim++) {           // sala de saída
            soma += v[fim];                             // entra em mais uma sala
            if (soma > melhor) melhor = soma;           // guarda o recorde
        }
    }
    printf("Máximo: %d vidas\n", melhor);               // 5 - 1 + 8 = 12 no exemplo
    return 0;                                           // fim sem erro
}
