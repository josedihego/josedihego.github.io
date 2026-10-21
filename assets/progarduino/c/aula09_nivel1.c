// Aula 9 – Nível 1: Constantes com #define
#include <stdio.h>                                // printf e scanf
#define PI 3.14159                                // constante: o pré-processador troca PI pelo valor

int main(void) {                                  // início do programa
    float raio;                                   // raio do fio em mm
    printf("Raio (mm): ");                        // pergunta ao usuário
    scanf("%f", &raio);                           // lê o valor digitado e guarda em raio
    printf("Área da seção: %.3f mm²\n", PI * raio * raio);   // mostra PI * raio * raio formatados
    return 0;                                     // termina com sucesso
}
