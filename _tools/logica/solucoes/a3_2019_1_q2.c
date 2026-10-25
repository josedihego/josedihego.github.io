// A3-2019.1 – Questão II: Expressão em letras para número de telefone
// teste: 1-LAR-DOCE-LAR => 1-527-3623-527
// teste: MY-LOVE => 69-5683
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    char s[101];                                        // expressão (A-Z, hífens, 1 e 0)
    printf("Expressão: ");                              // pede a expressão
    scanf("%100s", s);                                  // lê sem espaços
    //                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    const char *tabela = "22233344455566677778889999";  // tabela[letra - 'A'] dá o dígito da tecla
    for (int i = 0; s[i] != '\0'; i++) {                // percorre a expressão
        if (s[i] >= 'A' && s[i] <= 'Z') s[i] = tabela[s[i] - 'A'];   // letra vira dígito
    }                                                   // hífen, 1 e 0 ficam como estão
    printf("%s\n", s);                                  // 1-527-3623-527
    return 0;                                           // fim sem erro
}
