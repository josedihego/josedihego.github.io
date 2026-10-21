// Aula 9 – Nível 3: Estouro de capacidade
#include <stdio.h>                                              // printf

int main(void) {                                                // início do programa
    unsigned char byte = 250;                                   // 1 byte: 0 a 255
    byte = byte + 10;                                           // passa de 255 e "dá a volta"
    printf("250 + 10 em 1 byte = %d\n", byte);                  // 4
    short curto = 32767;                                        // 2 bytes: até 32767 (como o int do Arduino Uno)
    curto = (short)(curto + 1);                                 // estoura
    printf("32767 + 1 em 2 bytes = %d\n", curto);               // -32768
    long longo = 32767L + 1;                                    // long tem espaço de sobra
    printf("32767 + 1 em long = %ld\n", longo);                 // mostra longo formatados
    return 0;                                                   // termina com sucesso
}
