// Aula 33 – Nível 2: Vetor de leituras de sensores
#include <stdio.h>                                              // printf

typedef struct {                                                // typedef: dispensa escrever struct
    char nome[12];                                              // declara nome[12] (char)
    float valor;                                                // declara valor (float)
    char unidade[4];                                            // declara unidade[4] (char)
} Leitura;                                                      // nome do novo tipo

int main(void) {                                                // início do programa
    Leitura dados[] = {{"LDR", 612, ""}, {"Temp", 24.5, "C"}, {"Dist", 37.2, "cm"}};   // vetor de structs
    int n = sizeof dados / sizeof dados[0];                     // quantidade de leituras
    for (int i = 0; i < n; i++) {                               // percorre os n elementos (i de 0 a n-1)
        printf("%-5s %7.1f %s\n", dados[i].nome, dados[i].valor, dados[i].unidade);   // %-5s alinha à esquerda
    }
    return 0;                                                   // termina com sucesso
}
