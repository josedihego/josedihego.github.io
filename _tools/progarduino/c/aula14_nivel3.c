// Aula 14 – Nível 3: Média de N medições
// teste: 4; 4.9; 5.1; 5.0; 4.8
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int n;                                               // quantidade de medições
    float soma = 0;                                      // acumulador
    printf("Quantas medições? ");                        // pergunta ao usuário
    scanf("%d", &n);                                     // lê o valor digitado e guarda em n
    for (int i = 1; i <= n; i++) {                       // repete n vezes, i de 1 a n
        float medida;                                    // variável local do laço
        printf("Medição %d (V): ", i);                   // mostra i formatados
        scanf("%f", &medida);                            // lê o valor digitado e guarda em medida
        soma += medida;                                  // acumula
    }
    if (n > 0) printf("Média: %.3f V\n", soma / n);      // evita dividir por zero
    return 0;                                            // termina com sucesso
}
