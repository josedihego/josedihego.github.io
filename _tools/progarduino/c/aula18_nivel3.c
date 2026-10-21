// Aula 18 – Nível 3: MDC e MMC
// teste: 48; 36
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int a, b;                                            // os dois números lidos
    printf("Dois números: ");                            // pergunta ao usuário
    scanf("%d %d", &a, &b);                              // lê o valor digitado e guarda em a, b
    int x = a, y = b;                                    // cópias para o algoritmo
    while (y != 0) {                                     // algoritmo de Euclides
        int resto = x % y;                               // resto da divisão
        x = y;                                           // o divisor vira dividendo
        y = resto;                                       // o resto vira divisor
    }
    printf("MDC(%d, %d) = %d\n", a, b, x);               // mostra a e b e x formatados
    printf("MMC(%d, %d) = %d\n", a, b, a / x * b);       // MMC = a × b ÷ MDC
    return 0;                                            // termina com sucesso
}
