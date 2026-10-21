// Aula 35 – Nível 1: Simulado: vetor e média
// teste: 
#include <stdio.h>                                  // printf

int main(void) {                                    // início do programa
    int v[] = {7, 3, 9, 4, 6};                      // vetor de exemplo
    int soma = 0;                                   // acumulador
    for (int i = 0; i < 5; i++) soma += v[i];       // soma os 5 elementos
    printf("Média: %.1f\n", soma / 5.0);            // mostra soma / 5.0 formatados
    return 0;                                       // termina com sucesso
}
