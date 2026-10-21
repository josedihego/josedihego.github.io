// Aula 20 – Nível 3: Velocidade do som e temperatura
// teste: 1166
#include <stdio.h>                                                    // printf e scanf

int main(void) {                                                      // início do programa
    float eco;                                                        // declara eco (float)
    printf("Tempo de eco (us): ");                                    // pergunta ao usuário
    scanf("%f", &eco);                                                // lê o valor digitado e guarda em eco
    printf("Temp (C) | Velocidade (m/s) | Distância (cm)\n");         // mostra "Temp (C) | Velocidade (m/s) | Distância (cm)"
    for (int t = 0; t <= 40; t += 10) {                               // de 0 a 40 °C
        float v = 331.3 + 0.606 * t;                                  // velocidade do som no ar
        float cm = eco * (v / 10000.0) / 2;                           // m/s → cm/µs = ÷ 10000
        printf("%8d | %16.1f | %14.2f\n", t, v, cm);                  // mostra t e v e cm formatados
    }
    return 0;                                                         // termina com sucesso
}
