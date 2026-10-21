// Aula 26 – Nível 3: Ordenação (bubble sort)
#include <stdio.h>                                               // printf

int main(void) {                                                 // início do programa
    int v[] = {42, 7, 19, 3, 25, 11, 8};                         // vetor desordenado
    int n = sizeof v / sizeof v[0];                              // quantidade de elementos do vetor
    for (int passada = 0; passada < n - 1; passada++) {          // n-1 passadas
        for (int i = 0; i < n - 1 - passada; i++) {              // o fim já está ordenado
            if (v[i] > v[i + 1]) {                               // fora de ordem: troca
                int aux = v[i];                                  // guarda um dos valores
                v[i] = v[i + 1];                                 // o vizinho vem para a posição i
                v[i + 1] = aux;                                  // o valor guardado vai para a posição seguinte
            }
        }
    }
    for (int i = 0; i < n; i++) printf("%d ", v[i]);             // mostra o vetor
    printf("\n");                                                // quebra a linha
    return 0;                                                    // termina com sucesso
}
