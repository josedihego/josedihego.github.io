// A1-2024.2 (D) – Questão I: Sequência da soma dos quadrados dos dígitos até repetir
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // primeiro número (0 a 99)
    printf("Número (0 a 99): ");                        // pede o número
    scanf("%d", &n);                                    // lê o número
    int visto[200] = {0};                               // visto[x] = 1 se x já apareceu (vetor como memória)
    int seq[200], tam = 0;                              // a sequência gerada, para imprimir no fim
    while (!visto[n]) {                                 // para quando o número se repetir (ciclo)
        visto[n] = 1;                                   // marca como visto
        seq[tam++] = n;                                 // guarda na sequência
        int soma = 0;                                   // soma dos quadrados dos dígitos
        for (int x = n; x > 0; x /= 10) soma += (x % 10) * (x % 10);   // dígito a dígito
        if (soma >= 100) soma /= 2;                     // regra: 100 ou mais é dividido por 2
        n = soma;                                       // próximo termo
    }
    printf("Sequência: ");                              // imprime o resultado
    for (int i = 0; i < tam; i++) printf("%d%s", seq[i], i < tam - 1 ? ", " : "\n"); // vírgula entre os termos, quebra de linha no último
    return 0;                                           // fim sem erro
}
