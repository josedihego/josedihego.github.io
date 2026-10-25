// A3-2025.1 – Questão I: Grace Hopper – COBOL ou BUG?
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    char s[200];                                        // cinco palavras separadas por hífen
    printf("Texto: ");                                  // pede o texto
    scanf("%199s", s);                                  // lê sem espaços
    const char *alvo = "cobol";                         // a i-ésima palavra deve começar ou terminar com alvo[i]
    int palavra = 0, ok = 1;                            // índice da palavra atual e resultado
    int ini = 0;                                        // posição do início da palavra atual
    for (int i = 0; ; i++) {                            // percorre até o '\0'
        if (s[i] == '-' || s[i] == '\0') {              // terminou uma palavra: s[ini .. i-1]
            if (palavra >= 5 || (s[ini] != alvo[palavra] && s[i - 1] != alvo[palavra])) ok = 0; // letra fora do início e do fim da palavra
            palavra++;                                  // próxima palavra
            ini = i + 1;                                // ela começa depois do hífen
            if (s[i] == '\0') break;                    // fim do texto
        }
    }
    if (palavra != 5) ok = 0;                           // precisam ser exatamente cinco palavras
    printf(ok ? "COBOL\n" : "BUG\n");                   // resultado
    return 0;                                           // fim sem erro
}
