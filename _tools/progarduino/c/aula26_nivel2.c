// Aula 26 – Nível 2: Busca sequencial
// teste: 220
#include <stdio.h>                                          // printf e scanf

int main(void) {                                            // início do programa
    int estoque[] = {100, 220, 330, 470, 1000, 2200};       // resistores em estoque (ohms)
    int n = sizeof estoque / sizeof estoque[0];             // quantidade de elementos do vetor
    int procurado, pos = -1;                                // -1 = não encontrado
    printf("Resistor procurado (ohms): ");                  // pergunta ao usuário
    scanf("%d", &procurado);                                // lê o valor digitado e guarda em procurado
    for (int i = 0; i < n && pos == -1; i++) {              // para assim que encontrar
        if (estoque[i] == procurado) pos = i;               // achou: guarda a posição (o laço para)
    }
    if (pos >= 0) printf("Tem! Gaveta %d\n", pos + 1);      // posição + 1 para contar a partir de 1
    else printf("Não tem %d ohms\n", procurado);            // pos continua -1: não achou
    return 0;                                               // termina com sucesso
}
