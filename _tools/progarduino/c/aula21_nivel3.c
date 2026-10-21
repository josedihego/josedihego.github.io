// Aula 21 – Nível 3: Sensor LM35: tensão em temperatura
// teste: 3; 50; 61; 75
#include <stdio.h>                                                  // printf e scanf

int main(void) {                                                    // início do programa
    int n;                                                          // declara n (int)
    printf("Quantas leituras do LM35? ");                           // pergunta ao usuário
    scanf("%d", &n);                                                // lê o valor digitado e guarda em n
    for (int i = 0; i < n; i++) {                                   // percorre os n elementos (i de 0 a n-1)
        int leitura;                                                // declara leitura (int)
        scanf("%d", &leitura);                                      // lê o valor digitado e guarda em leitura
        float mv = leitura * 5000.0 / 1023;                         // leitura → milivolts
        float celsius = mv / 10;                                    // LM35: 10 mV por °C
        printf("Leitura %4d = %6.1f mV = %5.1f °C\n", leitura, mv, celsius);   // mostra leitura e mv e celsius formatados
    }
    return 0;                                                       // termina com sucesso
}
