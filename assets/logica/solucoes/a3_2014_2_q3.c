// A3-2014.2 – Questão III: struct produto – aumentar 10% os abaixo da média (na prova, 100 produtos)
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // a prova pede 100 registros

typedef struct {                                        // um registro: dados de um produto
    char nome[50];                                      // nome do produto (uma palavra)
    double preco;                                       // preço
} Produto;                                              // nome do novo tipo

int main(void) {                                        // início do programa
    Produto p[MAX];                                     // vetor de structs
    int n;                                              // quantidade de produtos
    scanf("%d", &n);                                    // lê N (100 na prova)
    double soma = 0;                                    // soma dos preços
    for (int i = 0; i < n; i++) {                       // lê cada produto
        scanf("%49s %lf", p[i].nome, &p[i].preco);      // . acessa o campo do struct
        soma += p[i].preco;                             // acumula para a média
    }
    double media = soma / n;                            // média dos preços originais
    int barato = 0;                                     // índice do mais barato após o aumento
    for (int i = 0; i < n; i++) {                       // aplica o aumento
        if (p[i].preco < media) p[i].preco *= 1.10;     // abaixo da média: +10%
        if (p[i].preco < p[barato].preco) barato = i;   // acompanha o mais barato
    }
    printf("Mais barato: %s R$ %.2f\n", p[barato].nome, p[barato].preco); // nome e preço já reajustado
    return 0;                                           // fim sem erro
}
