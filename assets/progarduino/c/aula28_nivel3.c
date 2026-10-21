// Aula 28 – Nível 3: Função e_primo
#include <stdio.h>                                          // printf e scanf
#include <stdbool.h>                                        // bool, true, false

bool e_primo(int n) {                                       // devolve verdadeiro ou falso
    if (n < 2) return false;                                // 0 e 1 não são primos
    for (int d = 2; d * d <= n; d++) {                      // testa divisores até a raiz de n
        if (n % d == 0) return false;                       // return sai da função na hora
    }
    return true;                                            // nenhum divisor: é primo
}

int main(void) {                                            // início do programa
    int limite;                                             // declara limite (int)
    printf("Até: ");                                        // pergunta ao usuário
    scanf("%d", &limite);                                   // lê o valor digitado e guarda em limite
    for (int i = 1; i <= limite; i++) {                     // de 1 até o limite
        if (e_primo(i)) printf("%d ", i);                   // a função deixa o main mais limpo
    }
    printf("\n");                                           // quebra a linha
    return 0;                                               // termina com sucesso
}
