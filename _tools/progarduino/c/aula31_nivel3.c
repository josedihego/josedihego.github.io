// Aula 31 – Nível 3: Contar vogais com ponteiro
// teste: Programação aplicada
#include <stdio.h>                                         // printf, fgets
#include <ctype.h>                                         // tolower

int main(void) {                                           // início do programa
    char texto[100];                                       // declara texto[100] (char)
    printf("Texto: ");                                     // pergunta ao usuário
    fgets(texto, sizeof texto, stdin);                     // lê a linha inteira (com espaços) em texto
    int vogais = 0;                                        // contador
    for (char *c = texto; *c != '\0'; c++) {               // o ponteiro anda de caractere em caractere
        char l = tolower((unsigned char)*c);               // letra apontada, em minúscula
        if (l == 'a' || l == 'e' || l == 'i' || l == 'o' || l == 'u') vogais++;   // é vogal: conta
    }
    printf("Vogais (sem acento): %d\n", vogais);           // mostra vogais formatados
    return 0;                                              // termina com sucesso
}
