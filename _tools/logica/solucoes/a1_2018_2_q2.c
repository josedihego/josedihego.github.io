// A1-2018.2 – Questão II: Dígito verificador da Setelândia (base 7)
// teste: 999 => 9991
// teste: 7 => 71
// teste: 48 => 485
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número de 0 a 999
    printf("Número (0 a 999): ");                       // pede o número
    scanf("%d", &n);                                    // lê o número
    int soma = 0;                                       // soma dos algarismos na base 7
    int resto = n;                                      // cópia que será dividida
    while (resto > 0) {                                 // conversão para base 7, dígito a dígito
        soma += resto % 7;                              // o resto da divisão por 7 é o próximo dígito
        resto = resto / 7;                              // passa para a próxima posição
    }
    int dv = soma % 7;                                  // dígito verificador
    printf("%d%d\n", n, dv);                            // o DV vai à direita do número original
    return 0;                                           // fim sem erro
}
