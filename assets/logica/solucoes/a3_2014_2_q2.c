// A3-2014.2 – Questão II: Encontros consonantais numa frase
#include <stdio.h>                                      // printf e fgets
#include <ctype.h>                                      // isalpha e tolower
#include <string.h>                                     // strchr

int consoante(char c) {                                 // 1 se c for uma letra sem acento que não é vogal
    return isalpha((unsigned char)c) && strchr("aeiou", tolower((unsigned char)c)) == NULL; // letra que não está em "aeiou"
}

int main(void) {                                        // início do programa
    char s[257];                                        // até 256 caracteres + '\0'
    printf("Frase: ");                                  // pede a frase
    fgets(s, sizeof s, stdin);                          // lê a linha inteira (com espaços)
    int encontros = 0, seguidas = 0;                    // total de encontros e consoantes seguidas agora
    for (int i = 0; s[i] != '\0'; i++) {                // percorre a frase
        if (consoante(s[i])) {                          // mais uma consoante no grupo atual
            seguidas++;                                 // conta
            if (seguidas == 2) encontros++;             // a 2ª consoante seguida forma um encontro (conta uma vez)
        } else {                                        // vogal, espaço, acento ou pontuação
            seguidas = 0;                               // quebra o grupo
        }
    }
    printf("%d encontros consonantais\n", encontros);   // istmo (stm), Stradun (Str), Brasil (Br)
    return 0;                                           // fim sem erro
}
