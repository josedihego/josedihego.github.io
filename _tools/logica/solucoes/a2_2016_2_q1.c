// A2-2016.2 – Questão I: Primo de Chen (com funções)
// teste: 2 => é primo de Chen
// teste: 7 => é primo de Chen
// teste: 43 => não é primo de Chen
// teste: 9 => não é primo
#include <stdio.h>                                      // printf e scanf

int e_primo(int n) {                                    // devolve 1 se n for primo, 0 se não
    if (n < 2) return 0;                                // 0 e 1 não são primos
    for (int d = 2; d * d <= n; d++)                    // basta testar até a raiz
        if (n % d == 0) return 0;                       // achou divisor: não é primo
    return 1;                                           // nenhum divisor: primo
}

int e_semiprimo(int n) {                                // 1 se n for o produto de dois primos
    for (int d = 2; d * d <= n; d++)                    // menor fator possível
        if (n % d == 0) return e_primo(d) && e_primo(n / d);   // primeiro divisor: os dois fatores são primos?
    return 0;                                           // sem divisores: é primo, não semiprimo
}

int main(void) {                                        // início do programa
    int p;                                              // número lido
    printf("Número: ");                                 // pede o número
    scanf("%d", &p);                                    // lê o número
    if (!e_primo(p)) printf("%d não é primo\n", p);     // primo de Chen precisa ser primo
    else if (e_primo(p + 2) || e_semiprimo(p + 2)) printf("%d é primo de Chen\n", p); // p + 2 primo ou semiprimo: definição de Chen
    else printf("%d não é primo de Chen\n", p);         // p + 2 tem 3 ou mais fatores primos
    return 0;                                           // fim sem erro
}
