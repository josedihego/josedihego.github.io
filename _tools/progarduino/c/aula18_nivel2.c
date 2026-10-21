// Aula 18 – Nível 2: Primos até N
// teste: 50
#include <stdio.h>                                         // printf e scanf

int main(void) {                                           // início do programa
    int limite;                                            // declara limite (int)
    printf("Primos até: ");                                // pergunta ao usuário
    scanf("%d", &limite);                                  // lê o valor digitado e guarda em limite
    for (int n = 2; n <= limite; n++) {                    // candidatos
        int primo = 1;                                     // supõe que é primo
        for (int d = 2; d * d <= n; d++) {                 // basta testar até a raiz
            if (n % d == 0) { primo = 0; break; }          // achou divisor: não é primo
        }
        if (primo) printf("%d ", n);                       // mostra só os primos
    }
    printf("\n");                                          // quebra a linha
    return 0;                                              // termina com sucesso
}
