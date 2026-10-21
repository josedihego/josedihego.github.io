// Aula 34 – Nível 1: Registro de medições em vetor de struct
// teste: 3; 08:00 4.98; 09:00 5.03; 10:00 4.87
#include <stdio.h>                                               // printf e scanf

typedef struct {                                                 // novo tipo que agrupa campos
    char hora[6];                                                // declara hora[6] (char)
    float tensao;                                                // declara tensao (float)
} Medicao;                                                       // nome do novo tipo

int main(void) {                                                 // início do programa
    Medicao m[24];                                               // até 24 medições (uma por hora)
    int n;                                                       // declara n (int)
    printf("Quantas medições? ");                                // pergunta ao usuário
    scanf("%d", &n);                                             // lê o valor digitado e guarda em n
    for (int i = 0; i < n; i++) scanf("%5s %f", m[i].hora, &m[i].tensao);   // lê hora e tensão
    for (int i = 0; i < n; i++) printf("%s  %.2f V\n", m[i].hora, m[i].tensao);   // mostra o registro
    return 0;                                                    // termina com sucesso
}
