// Aula 2 – Nível 3: Tamanho e limites dos tipos
// teste: 
#include <stdio.h>                                              // printf
#include <limits.h>                                             // INT_MAX, CHAR_MAX...

int main(void) {                                                // início do programa
    printf("char:   %zu byte(s)\n", sizeof(char));              // sizeof dá o tamanho em bytes (%zu)
    printf("int:    %zu bytes, máximo %d\n", sizeof(int), INT_MAX);   // mostra sizeof(int) e INT_MAX formatados
    printf("long:   %zu bytes, máximo %ld\n", sizeof(long), LONG_MAX);   // mostra sizeof(long) e LONG_MAX formatados
    printf("float:  %zu bytes\n", sizeof(float));               // mostra sizeof(float) formatados
    printf("double: %zu bytes\n", sizeof(double));              // mostra sizeof(double) formatados
    int limite = INT_MAX;                                       // maior int possível
    printf("INT_MAX + 1 = %u (como sem sinal)\n", (unsigned)limite + 1u);   // passa do limite
    return 0;                                                   // termina com sucesso
}
