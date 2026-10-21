// Aula 23 – Nível 1: Simulado: tabuada de N
// teste: 7
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int n;                                               // declara n (int)
    printf("Tabuada do: ");                              // pergunta ao usuário
    scanf("%d", &n);                                     // lê o valor digitado e guarda em n
    for (int i = 1; i <= 10; i++) printf("%d x %d = %d\n", n, i, n * i);   // uma linha da tabuada por volta
    return 0;                                            // termina com sucesso
}
