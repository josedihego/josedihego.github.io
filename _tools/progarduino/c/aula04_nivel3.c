// Aula 4 – Nível 3: int × float, teto e piso
// teste: 
#include <stdio.h>                                         // printf
#include <math.h>                                          // ceil e floor

int main(void) {                                           // início do programa
    int dias = 5;                                          // valor inteiro
    float com_int = dias * (1 + 12 / 100);                 // 12/100 é divisão inteira = 0!
    float com_float = dias * (1 + 12 / 100.0);             // 100.0 força a divisão com decimais
    printf("Com 12/100:   %.2f\n", com_int);               // 5.00 (errado)
    printf("Com 12/100.0: %.2f\n", com_float);             // 5.60 (certo)
    printf("Teto de 5.6: %.0f\n", ceil(com_float));        // ceil arredonda para cima: 6
    printf("Piso de 5.6: %.0f\n", floor(com_float));       // floor arredonda para baixo: 5
    return 0;                                              // termina com sucesso
}
