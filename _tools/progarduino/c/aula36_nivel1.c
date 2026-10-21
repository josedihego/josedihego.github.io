// Aula 36 – Nível 1: Revisão: inverter uma string
// teste: sensor
#include <stdio.h>                                      // printf, fgets
#include <string.h>                                     // strlen, strcspn

int main(void) {                                        // início do programa
    char s[50];                                         // declara s[50] (char)
    printf("Palavra: ");                                // pergunta ao usuário
    fgets(s, sizeof s, stdin);                          // lê a linha inteira (com espaços) em s
    s[strcspn(s, "\n")] = '\0';                         // tira o Enter do fim
    for (int i = strlen(s) - 1; i >= 0; i--) putchar(s[i]);   // mostra do último caractere ao primeiro
    printf("\n");                                       // quebra a linha
    return 0;                                           // termina com sucesso
}
