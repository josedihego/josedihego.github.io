// A3-2014.2 – Questão I: A matriz é de permutação? (na prova, N = 10)
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // maior dimensão aceita

int main(void) {                                        // início do programa
    int n, m[MAX][MAX];                                 // dimensão e matriz
    scanf("%d", &n);                                    // lê N (10 na prova; ler N deixa testar com matrizes pequenas)
    for (int i = 0; i < n; i++)                         // cada linha
        for (int j = 0; j < n; j++) scanf("%d", &m[i][j]);   // cada coluna
    int ok = 1;                                         // supõe que é de permutação
    for (int i = 0; i < n; i++) {                       // para cada índice i: linha i e coluna i
        int uns_linha = 0, uns_coluna = 0;              // quantos 1 na linha i e na coluna i
        for (int j = 0; j < n; j++) {                   // percorre a linha e a coluna ao mesmo tempo
            if (m[i][j] != 0 && m[i][j] != 1) ok = 0;   // só pode ter 0 e 1
            uns_linha += m[i][j];                       // m[i][j]: linha i
            uns_coluna += m[j][i];                      // m[j][i]: coluna i
        }
        if (uns_linha != 1 || uns_coluna != 1) ok = 0;  // exatamente um 1 por linha e por coluna
    }
    printf(ok ? "É uma matriz de permutação\n" : "Não é uma matriz de permutação\n"); // operador ternário escolhe a mensagem
    return 0;                                           // fim sem erro
}
