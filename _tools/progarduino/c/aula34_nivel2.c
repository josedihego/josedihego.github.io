// Aula 34 – Nível 2: Estatísticas do registro
// teste: 4; 08:00 4.98; 09:00 5.03; 10:00 4.71; 11:00 5.30
#include <stdio.h>                                                    // printf e scanf

typedef struct {                                                      // novo tipo que agrupa campos
    char hora[6];                                                     // declara hora[6] (char)
    float tensao;                                                     // declara tensao (float)
} Medicao;                                                            // nome do novo tipo

int main(void) {                                                      // início do programa
    Medicao m[24];                                                    // até 24 medições (uma por hora)
    int n, fora = 0;                                                  // quantidade e contador de medições fora da faixa
    float soma = 0;                                                   // acumulador
    printf("Quantas medições? ");                                     // pergunta ao usuário
    scanf("%d", &n);                                                  // lê o valor digitado e guarda em n
    for (int i = 0; i < n; i++) {                                     // percorre os n elementos (i de 0 a n-1)
        scanf("%5s %f", m[i].hora, &m[i].tensao);                     // lê o valor digitado e guarda em m[i].hora, m[i].tensao
        soma += m[i].tensao;                                          // acumula para a média
        if (m[i].tensao < 4.75 || m[i].tensao > 5.25) {               // fora dos 5%
            printf("Alerta às %s: %.2f V\n", m[i].hora, m[i].tensao);   // mostra m[i].hora e m[i].tensao formatados
            fora++;                                                   // conta mais uma fora da faixa
        }
    }
    printf("Média %.3f V; %d fora da faixa\n", soma / n, fora);       // mostra soma / n e fora formatados
    return 0;                                                         // termina com sucesso
}
