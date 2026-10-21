// Aula 27 – Nível 3: Quantas vezes a palavra aparece?
// teste: o led acende e o led apaga; led
#include <stdio.h>                                            // printf, fgets
#include <string.h>                                           // strlen, strncmp, strcspn

int main(void) {                                              // início do programa
    char texto[200], palavra[30];                             // duas strings
    printf("Texto: ");                                        // pergunta ao usuário
    fgets(texto, sizeof texto, stdin);                        // lê a linha inteira (com espaços) em texto
    printf("Palavra: ");                                      // pergunta ao usuário
    fgets(palavra, sizeof palavra, stdin);                    // lê a linha inteira (com espaços) em palavra
    texto[strcspn(texto, "\n")] = '\0';                       // remove os Enters
    palavra[strcspn(palavra, "\n")] = '\0';                   // troca o Enter pelo fim da string
    int tamanho = strlen(palavra), vezes = 0;                 // tamanho da palavra e contador
    for (int i = 0; texto[i] != '\0'; i++) {                  // percorre o texto até o '\0'
        if (strncmp(&texto[i], palavra, tamanho) == 0) vezes++;   // compara a partir da posição i
    }
    printf("\"%s\" aparece %d vez(es)\n", palavra, vezes);    // mostra palavra e vezes formatados
    return 0;                                                 // termina com sucesso
}
