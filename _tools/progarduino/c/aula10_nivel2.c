// Aula 10 – Nível 2: Divisor de tensão
// teste: 9; 10000; 4700
#include <stdio.h>                                          // printf e scanf

int main(void) {                                            // início do programa
    float vin, r1, r2;                                      // entrada e resistores
    printf("Vin (V), R1 e R2 (ohms): ");                    // pergunta ao usuário
    scanf("%f %f %f", &vin, &r1, &r2);                      // lê o valor digitado e guarda em vin, r1, r2
    float vout = vin * r2 / (r1 + r2);                      // Vout = Vin · R2 / (R1 + R2)
    printf("Vout = %.2f V\n", vout);                        // mostra vout formatados
    if (vout > 5.0) {                                       // o Arduino aceita no máximo 5 V
        printf("Atenção: acima de 5 V, não ligue no Arduino!\n");   // mostra "Atenção: acima de 5 V, não ligue no Arduino!"
    } else {
        printf("Seguro para uma entrada analógica do Arduino.\n");   // mostra "Seguro para uma entrada analógica do Arduino."
    }
    return 0;                                               // termina com sucesso
}
