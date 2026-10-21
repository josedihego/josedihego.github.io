// Aula 29 – Nível 3: Ordenar e imprimir com funções
#include <stdio.h>                                               // printf

void imprimir(int v[], int n) {                                  // void: não devolve nada
    for (int i = 0; i < n; i++) printf("%d ", v[i]);             // mostra o vetor
    printf("\n");                                                // quebra a linha
}

void ordenar(int v[], int n) {                                   // altera o vetor original!
    for (int p = 0; p < n - 1; p++)                              // passadas do bubble sort
        for (int i = 0; i < n - 1 - p; i++)                      // compara vizinhos na parte ainda desordenada
            if (v[i] > v[i + 1]) { int aux = v[i]; v[i] = v[i + 1]; v[i + 1] = aux; }   // fora de ordem: troca os vizinhos
}

int main(void) {                                                 // início do programa
    int dados[] = {9, 2, 7, 4, 5, 1};                            // vetor desordenado
    imprimir(dados, 6);                                          // mostra antes de ordenar
    ordenar(dados, 6);                                           // a função altera o próprio vetor
    imprimir(dados, 6);                                          // mostra ordenado: o vetor foi alterado
    return 0;                                                    // termina com sucesso
}
