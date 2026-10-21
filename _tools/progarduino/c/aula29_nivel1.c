// Aula 29 – Nível 1: Soma de um vetor numa função
// teste: 
#include <stdio.h>                                       // printf

int soma(int v[], int n) {                               // o vetor e o tamanho vão como parâmetros
    int total = 0;                                       // acumulador
    for (int i = 0; i < n; i++) total += v[i];           // soma todos os elementos
    return total;                                        // devolve a soma
}

int main(void) {                                         // início do programa
    int leituras[] = {512, 498, 530, 505, 520};          // leituras de exemplo
    printf("Soma: %d\n", soma(leituras, 5));             // mostra soma(leituras e 5) formatados
    return 0;                                            // termina com sucesso
}
