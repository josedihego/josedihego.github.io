// Aula 10 – Nível 1: Lei de Ohm com validação
// teste: 5; 0
#include <stdio.h>                                   // printf e scanf

int main(void) {                                     // início do programa
    float v, r;                                      // tensão e resistência
    printf("Tensão (V) e resistência (ohms): ");     // pergunta ao usuário
    scanf("%f %f", &v, &r);                          // lê o valor digitado e guarda em v, r
    if (r <= 0) {                                    // resistência precisa ser positiva
        printf("Resistência inválida\n");            // mostra "Resistência inválida"
    } else {
        printf("Corrente: %.3f A\n", v / r);         // mostra v / r formatados
    }
    return 0;                                        // termina com sucesso
}
