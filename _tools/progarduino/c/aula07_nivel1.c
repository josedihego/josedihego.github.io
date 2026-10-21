// Aula 7 – Nível 1: Faixas de temperatura
// teste: 31
#include <stdio.h>                                   // printf e scanf

int main(void) {                                     // início do programa
    float temperatura;                               // em °C
    printf("Temperatura (°C): ");                    // pergunta ao usuário
    scanf("%f", &temperatura);                       // lê o valor digitado e guarda em temperatura
    if (temperatura < 18) {                          // primeira faixa
        printf("Frio\n");                            // mostra "Frio"
    } else if (temperatura < 28) {                   // só é testado se a anterior foi falsa
        printf("Agradável\n");                       // mostra "Agradável"
    } else {                                         // 28 ou mais
        printf("Quente\n");                          // mostra "Quente"
    }
    return 0;                                        // termina com sucesso
}
