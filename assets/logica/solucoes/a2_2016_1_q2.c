// A2-2016.1 – Questão II: Números brasileiros
#include <stdio.h>                                      // printf e scanf

int digitos_iguais(int n, int base) {                   // 1 se n escrito na base tiver todos os dígitos iguais
    int ultimo = n % base;                              // dígito menos significativo
    while (n > 0) {                                     // percorre os dígitos na base
        if (n % base != ultimo) return 0;               // achou um dígito diferente
        n = n / base;                                   // próximo dígito
    }
    return 1;                                           // todos iguais
}

int main(void) {                                        // início do programa
    int n;                                              // número lido
    printf("Número: ");                                 // pede o número
    scanf("%d", &n);                                    // lê o número
    for (int b = 2; b < n - 1; b++) {                   // bases possíveis: 1 < b < n - 1
        if (digitos_iguais(n, b)) {                     // achou uma base que funciona
            printf("%d é brasileiro (base %d)\n", n, b);   // ex.: 7 = (111) na base 2
            return 0;                                   // basta uma base
        }
    }
    printf("%d não é brasileiro\n", n);                 // nenhuma base serviu
    return 0;                                           // fim sem erro
}
