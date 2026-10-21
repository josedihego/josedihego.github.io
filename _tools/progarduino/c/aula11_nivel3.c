// Aula 11 – Nível 3: Simulado: potência no resistor
// teste: 12; 100; 0.25
#include <stdio.h>                                                   // printf e scanf

int main(void) {                                                     // início do programa
    float v, r, p_max;                                               // tensão, resistência e potência máxima do resistor
    printf("Tensão (V), resistência (ohms) e potência do resistor (W): ");   // pergunta ao usuário
    scanf("%f %f %f", &v, &r, &p_max);                               // lê o valor digitado e guarda em v, r, p_max
    float p = v * v / r;                                             // P = V² / R
    printf("Dissipa %.3f W: %s\n", p, p <= p_max ? "OK" : "vai queimar!");   // ?: escolhe o texto
    return 0;                                                        // termina com sucesso
}
