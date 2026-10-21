// Aula 8 – Nível 3: Operadores bit a bit
// teste: 
#include <stdio.h>                                         // printf

int main(void) {                                           // início do programa
    unsigned char a = 0x0C;                                // 0000 1100 (12)
    unsigned char b = 0x0A;                                // 0000 1010 (10)
    printf("a & b  = %d\n", a & b);                        // E bit a bit: 0000 1000 = 8
    printf("a | b  = %d\n", a | b);                        // OU bit a bit: 0000 1110 = 14
    printf("a ^ b  = %d\n", a ^ b);                        // OU exclusivo: 0000 0110 = 6
    printf("a << 1 = %d\n", a << 1);                       // desloca para a esquerda: ×2 = 24
    printf("a >> 2 = %d\n", a >> 2);                       // desloca para a direita: ÷4 = 3
    printf("bit 3 de a = %d\n", (a >> 3) & 1);             // lê um bit isolado: 1
    return 0;                                              // termina com sucesso
}
