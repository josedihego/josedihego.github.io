// A2-2025.2 – Questão I: Maior e menor média de temperatura em janelas de tamanho dado
// teste: 8 20 30 50 40 20 -10 -30 60 15 -20 -50 6 => maior média: 28.00
// teste: 8 20 30 50 40 20 -10 -30 60 15 -20 -50 6 => menor média: -5.83
// teste: 8 20 30 50 40 20 -10 0 0 0 0 0 4 => maior média: 35.00
#include <stdio.h>                                      // printf e scanf
#define N 12                                            // quantidade de temperaturas

int main(void) {                                        // início do programa
    int t[N];                                           // temperaturas medidas
    int janela;                                         // tamanho do intervalo
    for (int i = 0; i < N; i++) scanf("%d", &t[i]);     // lê as 12 temperaturas
    scanf("%d", &janela);                               // lê o tamanho do intervalo
    double maior = -500, menor = 500;                   // o enunciado garante valores entre -500 e 500
    for (int ini = 0; ini + janela <= N; ini++) {       // cada janela começa em ini
        int soma = 0;                                   // soma da janela atual
        for (int k = ini; k < ini + janela; k++) soma += t[k];   // soma os 'janela' valores
        double media = (double)soma / janela;           // (double): divisão real
        if (media > maior) maior = media;               // nova maior média
        if (media < menor) menor = media;               // nova menor média
    }
    printf("Maior média: %.2f\n", maior);               // 28.00 no exemplo
    printf("Menor média: %.2f\n", menor);               // -5.83 no exemplo
    return 0;                                           // fim sem erro
}
