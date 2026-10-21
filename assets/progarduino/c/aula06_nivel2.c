// Aula 6 – Nível 2: Série ou paralelo à escolha
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    float r1 = 100.0, r2 = 220.0;                        // resistores fixos (ohms)
    int opcao;                                           // escolha do usuário
    float resultado;                                     // resistência equivalente
    printf("1. Paralelo  2. Série: ");                   // pergunta ao usuário
    scanf("%d", &opcao);                                 // lê o valor digitado e guarda em opcao
    if (opcao == 1) {                                    // escolheu paralelo
        resultado = (r1 * r2) / (r1 + r2);               // paralelo: produto ÷ soma
    } else {                                             // qualquer outro valor: série
        resultado = r1 + r2;                             // série: soma
    }
    printf("Resistência equivalente: %.2f ohms\n", resultado);   // mostra resultado formatados
    return 0;                                            // termina com sucesso
}
