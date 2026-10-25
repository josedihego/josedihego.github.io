// A2-2014.2 – Questão I: Raiz quadrada subtraindo ímpares consecutivos
// teste: 16 => raiz exata de 16 é 4
// teste: 27 => raiz aproximada de 27 é 6
// teste: 1 => raiz exata de 1 é 1
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // número positivo
    printf("Número: ");                                 // pede o número
    scanf("%d", &n);                                    // lê o número
    int resto = n;                                      // vai sendo reduzido pelos ímpares
    int vezes = 0;                                      // quantas subtrações foram feitas
    for (int impar = 1; resto > 0; impar += 2) {        // 1, 3, 5, ... enquanto o resultado for positivo
        resto -= impar;                                 // subtrai o próximo ímpar
        vezes++;                                        // conta a subtração
    }
    if (resto == 0) printf("A raiz exata de %d é %d\n", n, vezes);   // terminou em zero: exata
    else printf("A raiz aproximada de %d é %d\n", n, vezes);         // passou de zero: aproximada
    return 0;                                           // fim sem erro
}
