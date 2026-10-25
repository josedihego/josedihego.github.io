// Base 3 – Structs: typedef, ->, vetores de structs, autorreferência e alinhamento
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct {                               // typedef: dispensa escrever "struct"
    char nome[32];
    double nota;
} Aluno;

typedef struct No {                            // autorreferente: o nó de uma lista
    Aluno dado;                                // struct dentro de struct
    struct No *prox;                           // aqui ainda não existe o nome No
} No;

/* Alinhamento: o compilador insere preenchimento para cada campo começar num
   endereço múltiplo do seu tamanho. A ordem dos campos muda o sizeof. */
typedef struct { char a; int b; char c; } Mal;    // 1 + 3 (buraco) + 4 + 1 + 3 = 12
typedef struct { int b; char a; char c; } Bem;    // 4 + 1 + 1 + 2 = 8

void imprime(const Aluno *x) {                 // passar o endereço: não copia a struct
    printf("%s (%.1f)\n", x->nome, x->nota);   // x->nota é (*x).nota
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    Aluno *turma = malloc(n * sizeof *turma);  // vetor de structs no heap
    No *lista = NULL;
    for (int i = 0; i < n; i++) {
        if (scanf("%31s %lf", turma[i].nome, &turma[i].nota) != 2) return 1;
        No *no = malloc(sizeof *no);
        no->dado = turma[i];                   // atribuição copia a struct inteira
        no->prox = lista;
        lista = no;
    }
    int melhor = 0;
    for (int i = 1; i < n; i++)
        if (turma[i].nota > turma[melhor].nota) melhor = i;
    printf("melhor: ");
    imprime(&turma[melhor]);
    printf("sizeof(Mal) = %zu, sizeof(Bem) = %zu; b começa no byte %zu de Mal\n",
           sizeof(Mal), sizeof(Bem), offsetof(Mal, b));
    printf("lista:");
    while (lista) {
        No *x = lista;
        printf(" %s", x->dado.nome);
        lista = x->prox;
        free(x);
    }
    printf("\n");
    free(turma);
    return 0;
}
