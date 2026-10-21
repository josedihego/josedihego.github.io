// Aula 16 – Nível 2: Monitoramento de tensão
#include <stdio.h>                                               // printf e scanf

int main(void) {                                                 // início do programa
    int leituras, dentro = 0;                                    // total e contador dentro da faixa
    printf("Quantas leituras? ");                                // pergunta ao usuário
    scanf("%d", &leituras);                                      // lê o valor digitado e guarda em leituras
    for (int i = 0; i < leituras; i++) {                         // uma volta por leitura
        int tensao;                                              // declara tensao (int)
        printf("Tensão %d (V): ", i + 1);                        // mostra i + 1 formatados
        scanf("%d", &tensao);                                    // lê o valor digitado e guarda em tensao
        if (tensao >= 200 && tensao <= 240) dentro++;            // faixa aceitável
    }
    printf("Dentro da faixa: %.1f%%\n", 100.0 * dentro / leituras);   // 100.0 força a divisão com decimais
    return 0;                                                    // termina com sucesso
}
