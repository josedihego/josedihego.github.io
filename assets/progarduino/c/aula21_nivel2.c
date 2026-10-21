// Aula 21 – Nível 2: Calibração por mínimo e máximo
#include <stdio.h>                                             // printf e scanf

int main(void) {                                               // início do programa
    int n, minimo = 1023, maximo = 0;                          // começam invertidos de propósito
    int leituras[20];                                          // guarda até 20 leituras
    printf("Quantas leituras de calibração (até 20)? ");       // pergunta ao usuário
    scanf("%d", &n);                                           // lê o valor digitado e guarda em n
    for (int i = 0; i < n; i++) {                              // percorre os n elementos (i de 0 a n-1)
        scanf("%d", &leituras[i]);                             // lê o valor digitado e guarda em leituras[i]
        if (leituras[i] < minimo) minimo = leituras[i];        // registra a menor
        if (leituras[i] > maximo) maximo = leituras[i];        // registra a maior
    }
    printf("Calibrado: %d a %d\n", minimo, maximo);            // mostra minimo e maximo formatados
    for (int i = 0; i < n; i++) {                              // percorre os n elementos (i de 0 a n-1)
        printf("%d -> %d%%\n", leituras[i], (leituras[i] - minimo) * 100 / (maximo - minimo));   // mostra os valores formatados
    }
    return 0;                                                  // termina com sucesso
}
