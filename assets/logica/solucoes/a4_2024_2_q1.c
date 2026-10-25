// A4-2024.2 – Questão I: Hexadecimal (string) para decimal
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    char hex[256];                                      // até 255 caracteres
    printf("Hexadecimal: ");                            // pede o número
    scanf("%255s", hex);                                // lê a string
    unsigned long long valor = 0;                       // maior inteiro sem sinal do C
    for (int i = 0; hex[i] != '\0'; i++) {              // da esquerda para a direita (método de Horner)
        int d;                                          // valor do dígito atual
        if (hex[i] >= '0' && hex[i] <= '9') d = hex[i] - '0';        // '7' - '0' = 7
        else if (hex[i] >= 'A' && hex[i] <= 'F') d = hex[i] - 'A' + 10;   // 'B' - 'A' + 10 = 11
        else { printf("Dígito inválido: %c\n", hex[i]); return 1; }  // qualquer outro caractere
        valor = valor * 16 + d;                         // desloca uma casa hexadecimal e soma o dígito
    }
    printf("%llu\n", valor);                            // %llu imprime unsigned long long
    return 0;                                           // fim sem erro
}
