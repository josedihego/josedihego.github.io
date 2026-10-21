// Aula 25 – Nível 1: Ler e mostrar um vetor
// teste: 5; 3; 9; 1; 7
#include <stdio.h>                                   // printf e scanf
#define TAM 5                                        // tamanho do vetor

int main(void) {                                     // início do programa
    int valores[TAM];                                // 5 inteiros: valores[0] a valores[4]
    for (int i = 0; i < TAM; i++) {                  // percorre as TAM posições
        printf("Valor %d: ", i + 1);                 // mostra i + 1 formatados
        scanf("%d", &valores[i]);                    // guarda na posição i
    }
    printf("[");                                     // mostra "["
    for (int i = 0; i < TAM; i++) {                  // percorre as TAM posições
        printf("%d%s", valores[i], i < TAM - 1 ? ", " : "]\n");   // vírgula entre os elementos
    }
    return 0;                                        // termina com sucesso
}
