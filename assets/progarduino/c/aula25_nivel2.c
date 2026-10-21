// Aula 25 – Nível 2: Ordem inversa e soma
#include <stdio.h>                                   // printf e scanf
#define TAM 10                                       // constante TAM = 10

int main(void) {                                     // início do programa
    int v[TAM], soma = 0;                            // vetor de TAM inteiros e acumulador
    printf("10 valores: ");                          // pergunta ao usuário
    for (int i = 0; i < TAM; i++) {                  // percorre as TAM posições
        scanf("%d", &v[i]);                          // lê o valor digitado e guarda em v[i]
        soma += v[i];                                // soma enquanto lê
    }
    printf("Ao contrário: ");                        // pergunta ao usuário
    for (int i = TAM - 1; i >= 0; i--) printf("%d ", v[i]);   // do último ao primeiro
    printf("\nSoma: %d\n", soma);                    // mostra soma formatados
    return 0;                                        // termina com sucesso
}
