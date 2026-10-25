// A3-2026.1 – Questão II: Assinatura de frequência (2N3A1B aceita BANANA)
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    char formula[60], palavra[33];                      // fórmula (ex.: 2N3A1B) e palavra-passe (até 32 letras)
    printf("Fórmula e palavra: ");                      // pede as duas strings
    scanf("%59s %32s", formula, palavra);               // lê as duas palavras
    int exigido[26] = {0}, contado[26] = {0};           // quantidade exigida e encontrada de cada letra
    for (int i = 0; formula[i] != '\0'; i += 2)         // a fórmula vem em pares: dígito + letra
        exigido[formula[i + 1] - 'A'] = formula[i] - '0';   // '3' - '0' = 3; 'A' - 'A' = 0
    for (int i = 0; palavra[i] != '\0'; i++)            // conta as letras da palavra
        contado[palavra[i] - 'A']++;                    // a letra vira índice
    int aceita = 1;                                     // supõe aceita
    for (int k = 0; k < 26; k++)                        // compara letra por letra
        if (exigido[k] != contado[k]) aceita = 0;       // letra a mais, a menos ou fora da fórmula
    printf(aceita ? "ACEITO\n" : "RECUSADO\n");         // resultado
    return 0;                                           // fim sem erro
}
