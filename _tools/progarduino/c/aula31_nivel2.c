// Aula 31 – Nível 2: Vetor do tamanho que o usuário quiser
// teste: 4; 1.5; 2.5; 3.5; 4.5
#include <stdio.h>                                         // printf e scanf
#include <stdlib.h>                                        // malloc e free

int main(void) {                                           // início do programa
    int n;                                                 // declara n (int)
    printf("Quantas leituras? ");                          // pergunta ao usuário
    scanf("%d", &n);                                       // lê o valor digitado e guarda em n
    float *v = malloc(n * sizeof(float));                  // reserva memória para n floats
    if (v == NULL) return 1;                               // sem memória
    float soma = 0;                                        // acumulador
    for (int i = 0; i < n; i++) {                          // percorre os n elementos (i de 0 a n-1)
        scanf("%f", &v[i]);                                // usa como um vetor comum
        soma += v[i];                                      // acumula o elemento
    }
    printf("Média de %d leituras: %.2f\n", n, soma / n);   // mostra n e soma / n formatados
    free(v);                                               // devolve a memória
    return 0;                                              // termina com sucesso
}
