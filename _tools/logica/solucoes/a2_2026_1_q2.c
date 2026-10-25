// A2-2026.1 – Questão II: Rotina de Kaprekar até 6174
// teste: 8991 => 9981 - 1899 = 8082
// teste: 8991 => 8532 - 2358 = 6174
// teste: 3524 => 6174
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número de 4 dígitos (com dígitos distintos)
    printf("Número de 4 dígitos: ");                    // pede o número
    scanf("%d", &n);                                    // lê o número
    do {                                                // pelo menos uma vez (6174 → 7641 - 1467 = 6174)
        int d[4];                                       // os quatro dígitos
        for (int i = 0, x = n; i < 4; i++, x /= 10) d[i] = x % 10;   // separa (com zeros à esquerda)
        for (int p = 0; p < 3; p++)                     // ordena crescente (bubble sort)
            for (int i = 0; i < 3 - p; i++)             // bubble sort: a cada passada, o maior vai para o fim
                if (d[i] > d[i + 1]) { int aux = d[i]; d[i] = d[i + 1]; d[i + 1] = aux; } // fora de ordem: troca os vizinhos
        int menor = d[0] * 1000 + d[1] * 100 + d[2] * 10 + d[3];   // dígitos em ordem crescente
        int maior = d[3] * 1000 + d[2] * 100 + d[1] * 10 + d[0];   // em ordem decrescente
        n = maior - menor;                              // próximo número da rotina
        printf("%d - %d = %d\n", maior, menor, n);      // mostra a transição
    } while (n != 6174);                                // até atingir a constante
    return 0;                                           // fim sem erro
}
