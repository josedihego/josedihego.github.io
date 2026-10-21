// Aula 16 – Nível 3: Maior, menor e média
// teste: 5; 21.5; 23.0; 19.8; 25.1; 22.4
#include <stdio.h>                                            // printf e scanf

int main(void) {                                              // início do programa
    int n;                                                    // declara n (int)
    float valor, soma = 0, maior, menor;                      // maior e menor vêm da primeira leitura
    printf("Quantas temperaturas? ");                         // pergunta ao usuário
    scanf("%d", &n);                                          // lê o valor digitado e guarda em n
    for (int i = 0; i < n; i++) {                             // percorre os n elementos (i de 0 a n-1)
        printf("Temperatura %d: ", i + 1);                    // mostra i + 1 formatados
        scanf("%f", &valor);                                  // lê o valor digitado e guarda em valor
        if (i == 0 || valor > maior) maior = valor;          // na primeira volta, inicializa
        if (i == 0 || valor < menor) menor = valor;           // na primeira volta, ou se for menor, guarda
        soma += valor;                                        // acumula o valor lido
    }
    printf("Maior %.1f | Menor %.1f | Média %.2f\n", maior, menor, soma / n);   // mostra maior e menor e soma / n formatados
    return 0;                                                 // termina com sucesso
}
