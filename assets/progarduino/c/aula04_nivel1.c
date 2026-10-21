// Aula 4 – Nível 1: Os operadores
#include <stdio.h>                                // printf

int main(void) {                                  // início do programa
    int a = 17, b = 5;                            // dois inteiros
    printf("a + b = %d\n", a + b);                // 22
    printf("a - b = %d\n", a - b);                // 12
    printf("a * b = %d\n", a * b);                // 85
    printf("a / b = %d\n", a / b);                // 3: divisão entre inteiros descarta a parte decimal
    printf("a %% b = %d\n", a % b);               // 2: resto da divisão
    printf("a / 5.0 = %.1f\n", a / 5.0);          // 3.4: com um float na conta o resultado é float
    return 0;                                     // termina com sucesso
}
