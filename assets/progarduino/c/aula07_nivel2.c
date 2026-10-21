// Aula 7 – Nível 2: Calculadora com switch
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    float a, b;                                          // operandos
    char op;                                             // operador
    printf("Conta (ex.: 8 * 3): ");                      // pergunta ao usuário
    scanf("%f %c %f", &a, &op, &b);                      // lê número, operador e número
    switch (op) {                                        // escolhe o caso pelo valor de op
        case '+': printf("= %.2f\n", a + b); break;      // break sai do switch
        case '-': printf("= %.2f\n", a - b); break;      // subtração
        case '*': printf("= %.2f\n", a * b); break;      // multiplicação
        case '/':                                        // divisão
            if (b != 0) printf("= %.2f\n", a / b);       // evita divisão por zero
            else printf("Divisão por zero!\n");          // divisor zero: avisa em vez de dividir
            break;                                       // sai do switch/laço
        default: printf("Operador inválido\n");          // nenhum caso combinou
    }
    return 0;                                            // termina com sucesso
}
