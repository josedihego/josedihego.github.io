// Aula 33 – Nível 3: Cadastro de componentes
#include <stdio.h>                                                   // printf e scanf

typedef struct {                                                     // novo tipo que agrupa campos
    char codigo[10];                                                 // declara codigo[10] (char)
    int ohms;                                                        // 0 quando não é resistor
    int quantidade;                                                  // declara quantidade (int)
} Componente;                                                        // nome do novo tipo

void mostrar(Componente c) {                                         // recebe um struct inteiro
    printf("%-4s %6d ohms  qtd %3d\n", c.codigo, c.ohms, c.quantidade);   // mostra c.codigo e c.ohms e c.quantidade formatados
}

int main(void) {                                                     // início do programa
    Componente lista[10];                                            // até 10 componentes
    int n;                                                           // declara n (int)
    printf("Quantos componentes (até 10)? ");                        // pergunta ao usuário
    scanf("%d", &n);                                                 // lê o valor digitado e guarda em n
    for (int i = 0; i < n; i++) scanf("%9s %d %d", lista[i].codigo, &lista[i].ohms, &lista[i].quantidade);   // lê os 3 campos de cada componente
    int total = 0;                                                   // acumulador
    for (int i = 0; i < n; i++) {                                    // percorre os n elementos (i de 0 a n-1)
        mostrar(lista[i]);                                           // mostra um componente
        total += lista[i].quantidade;                                // soma as quantidades
    }
    printf("Total de peças: %d\n", total);                           // mostra total formatados
    return 0;                                                        // termina com sucesso
}
