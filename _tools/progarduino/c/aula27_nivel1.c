// Aula 27 – Nível 1: Ler uma frase e contar letras
// teste: Arduino Uno
#include <stdio.h>                                       // printf, fgets

int main(void) {                                         // início do programa
    char frase[100];                                     // até 99 caracteres + '\0'
    printf("Frase: ");                                   // pergunta ao usuário
    fgets(frase, sizeof frase, stdin);                   // lê a linha inteira, com espaços
    int n = 0;                                           // contador começa em zero
    while (frase[n] != '\0' && frase[n] != '\n') n++;    // conta até o fim do texto
    printf("A frase tem %d caracteres\n", n);            // mostra n formatados
    return 0;                                            // termina com sucesso
}
