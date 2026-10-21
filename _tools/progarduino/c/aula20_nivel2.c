// Aula 20 – Nível 2: Classificar uma série de leituras
// teste: 4; 2900; 1200; 450; 120
#include <stdio.h>                                               // printf e scanf

int main(void) {                                                 // início do programa
    int n;                                                       // declara n (int)
    printf("Quantas leituras? ");                                // pergunta ao usuário
    scanf("%d", &n);                                             // lê o valor digitado e guarda em n
    for (int i = 1; i <= n; i++) {                               // repete n vezes, i de 1 a n
        float eco;                                               // declara eco (float)
        printf("Eco %d (us): ", i);                              // mostra i formatados
        scanf("%f", &eco);                                       // lê o valor digitado e guarda em eco
        float cm = eco * 0.0343 / 2;                             // converte em cm
        if (cm < 10) printf("%.1f cm: PARE\n", cm);              // menos de 10 cm
        else if (cm < 30) printf("%.1f cm: perto\n", cm);        // de 10 a 30 cm
        else printf("%.1f cm: livre\n", cm);                     // 30 cm ou mais
    }
    return 0;                                                    // termina com sucesso
}
