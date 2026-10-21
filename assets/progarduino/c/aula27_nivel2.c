// Aula 27 – Nível 2: Palíndromo
#include <stdio.h>                                          // printf, fgets
#include <string.h>                                         // strlen

int main(void) {                                            // início do programa
    char palavra[50];                                       // declara palavra[50] (char)
    printf("Palavra: ");                                    // pergunta ao usuário
    fgets(palavra, sizeof palavra, stdin);                  // lê a linha inteira (com espaços) em palavra
    palavra[strcspn(palavra, "\n")] = '\0';                 // tira o Enter do fim
    int n = strlen(palavra), palindromo = 1;                // tamanho; começa supondo que é palíndromo
    for (int i = 0; i < n / 2; i++) {                       // compara as pontas indo para o meio
        if (palavra[i] != palavra[n - 1 - i]) palindromo = 0;   // letras espelhadas diferentes: não é
    }
    printf("\"%s\" %s palíndromo\n", palavra, palindromo ? "é" : "não é");   // mostra os valores formatados
    return 0;                                               // termina com sucesso
}
