// Aula 23 – Nível 3: Simulado: quantos primos?
// teste: 100
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int limite, quantos = 0;                             // limite lido e contador de primos
    printf("Até: ");                                     // pergunta ao usuário
    scanf("%d", &limite);                                // lê o valor digitado e guarda em limite
    for (int n = 2; n <= limite; n++) {                  // candidatos de 2 até o limite
        int divisores = 0;                               // contador de divisores de n
        for (int d = 1; d <= n; d++) if (n % d == 0) divisores++;   // conta todos os divisores
        if (divisores == 2) quantos++;                   // primo tem exatamente 2 divisores
    }
    printf("%d primos até %d\n", quantos, limite);       // mostra quantos e limite formatados
    return 0;                                            // termina com sucesso
}
