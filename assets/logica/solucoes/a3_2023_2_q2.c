// A3-2023.2 – Questão II: Palavra ordenada (letras em ordem alfabética, sem diferenciar maiúsculas)
#include <stdio.h>                                      // printf e scanf

int minuscula(char c) {                                 // 'A'..'Z' vira 'a'..'z'; o resto fica igual
    if (c >= 'A' && c <= 'Z') return c - 'A' + 'a';     // na tabela ASCII, as letras são consecutivas
    return c;                                           // já é minúscula (ou não é letra)
}

int main(void) {                                        // início do programa
    char p[100];                                        // a palavra (até 99 letras + '\0')
    printf("Palavra: ");                                // pede a palavra
    scanf("%99s", p);                                   // %99s: lê uma palavra sem estourar o vetor
    int ordenada = 1;                                   // supõe ordenada até provar o contrário
    for (int i = 1; p[i] != '\0'; i++) {                // compara cada letra com a anterior
        if (minuscula(p[i - 1]) > minuscula(p[i])) ordenada = 0;   // 'r' > 'o' em "Flro": fora de ordem
    }
    if (ordenada) printf("%s é ordenada\n", p);         // resultado
    else printf("%s não é ordenada\n", p);              // resultado
    return 0;                                           // fim sem erro
}
