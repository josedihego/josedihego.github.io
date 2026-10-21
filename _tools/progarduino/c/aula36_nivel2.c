// Aula 36 – Nível 2: Revisão: matriz identidade
// teste: 4
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // declara n (int)
    printf("Tamanho: ");                                // pergunta ao usuário
    scanf("%d", &n);                                    // lê o valor digitado e guarda em n
    for (int l = 0; l < n; l++) {                       // percorre as linhas
        for (int c = 0; c < n; c++) printf("%d ", l == c);   // 1 na diagonal, 0 fora dela
        printf("\n");                                   // quebra a linha
    }
    return 0;                                           // termina com sucesso
}
