// Aula 12 – Nível 2: Revisão: faixa segura
// teste: 4.8
#include <stdio.h>                                         // printf e scanf

int main(void) {                                           // início do programa
    float v;                                               // tensão medida
    printf("Tensão (V): ");                                // pergunta ao usuário
    scanf("%f", &v);                                       // lê o valor digitado e guarda em v
    if (v >= 4.75 && v <= 5.25) printf("Dentro dos 5%%\n");   // && exige as duas condições
    else printf("Fora da tolerância\n");                   // abaixo de 4,75 V ou acima de 5,25 V
    return 0;                                              // termina com sucesso
}
