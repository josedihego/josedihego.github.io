// A1-2014.2 – Questão IV: Validação pelo algoritmo de Luhn (até 4 dígitos)
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número de até 4 dígitos
    printf("Número: ");                                 // pede o número
    scanf("%d", &n);                                    // lê o número
    int soma = 0;                                       // somatório de Luhn
    int posicao = 1;                                    // 1 = unidade (o primeiro após inverter)
    while (n > 0) {                                     // percorre os dígitos da direita para a esquerda
        int d = n % 10;                                 // dígito atual
        if (posicao % 2 == 0) {                         // posições pares: dobra
            d = d * 2;                                  // multiplica por 2
            if (d > 9) d = d - 9;                       // "noves fora": 12 → 3, 16 → 7
        }
        soma += d;                                      // acumula
        n = n / 10;                                     // descarta o dígito já tratado
        posicao++;                                      // próxima posição
    }
    if (soma % 10 == 0) printf("Número Válido\n");      // somatório múltiplo de 10
    else printf("Número Inválido\n");                   // senão, inválido
    return 0;                                           // fim sem erro
}
