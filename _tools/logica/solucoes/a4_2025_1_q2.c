// A4-2025.1 – Questão II: Quantos retângulos (blocos consecutivos) somam exatamente K
// teste: 2 0 1 1 0 0 8 4 1 3 4 => 5 retângulos
// teste: 1 1 1 1 1 1 1 1 1 1 3 => 8 retângulos
// teste: 0 0 0 0 0 0 0 0 0 9 9 => 10 retângulos
#include <stdio.h>                                      // printf e scanf
#define N 10                                            // quadrados na prova

int main(void) {                                        // início do programa
    int v[N], k;                                        // números dos quadrados e soma procurada
    for (int i = 0; i < N; i++) scanf("%d", &v[i]);     // lê os N números
    scanf("%d", &k);                                    // lê K
    int quantos = 0;                                    // contador de retângulos
    for (int ini = 0; ini < N; ini++) {                 // primeiro quadrado do retângulo
        int soma = 0;                                   // soma de v[ini..fim]
        for (int fim = ini; fim < N; fim++) {           // último quadrado
            soma += v[fim];                             // inclui mais um quadrado
            if (soma == k) quantos++;                   // achou um retângulo
            if (soma > k) break;                        // naturais: a soma só cresce, pode parar
        }
    }
    printf("%d retângulos\n", quantos);                 // resultado
    return 0;                                           // fim sem erro
}
