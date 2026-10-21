// Aula 26 – Nível 1: Maior e menor do vetor
#include <stdio.h>                                         // printf

int main(void) {                                           // início do programa
    float temp[] = {22.5, 19.0, 25.3, 21.8, 18.4, 24.1};   // tamanho calculado pelo compilador
    int n = sizeof temp / sizeof temp[0];                  // nº de elementos = tamanho total ÷ tamanho de um
    int imaior = 0, imenor = 0;                            // guardam as POSIÇÕES
    for (int i = 1; i < n; i++) {                          // começa no 1: o 0 já é o valor inicial
        if (temp[i] > temp[imaior]) imaior = i;            // achou um maior: guarda a posição
        if (temp[i] < temp[imenor]) imenor = i;            // achou um menor: guarda a posição
    }
    printf("Maior: %.1f (posição %d)\n", temp[imaior], imaior);   // mostra temp[imaior] e imaior formatados
    printf("Menor: %.1f (posição %d)\n", temp[imenor], imenor);   // mostra temp[imenor] e imenor formatados
    return 0;                                              // termina com sucesso
}
