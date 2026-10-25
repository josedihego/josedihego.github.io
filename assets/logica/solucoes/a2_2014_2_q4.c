// A2-2014.2 – Questão IV: Lista de presença com números repetidos (na prova, 50 números)
#include <stdio.h>                                      // printf e scanf
#define MAX 50                                          // tamanho da lista na prova

int main(void) {                                        // início do programa
    int n, lista[MAX];                                  // quantos números e a lista lida
    int presentes[MAX], total = 0;                      // números sem repetição e quantos são
    scanf("%d", &n);                                    // lê N (50 na prova; ler N deixa testar com o exemplo)
    for (int i = 0; i < n; i++) scanf("%d", &lista[i]); // lê a lista de presença
    for (int i = 0; i < n; i++) {                       // cada número da lista
        int repetido = 0;                               // já está entre os presentes?
        for (int j = 0; j < total; j++)                 // procura nos que já foram guardados
            if (presentes[j] == lista[i]) repetido = 1; // achou: é repetição
        if (!repetido) presentes[total++] = lista[i];   // primeira vez: guarda na próxima posição livre
    }
    printf("%d Alunos\n", total);                       // quantos receberam presença
    for (int j = 0; j < total; j++)                     // na ordem em que apareceram
        printf("%d - %d\n", j + 1, presentes[j]);       // posição e número de registro
    return 0;                                           // fim sem erro
}
