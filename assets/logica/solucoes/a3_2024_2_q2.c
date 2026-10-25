// A3-2024.2 – Questão II: Posição da primeira ocorrência de cada letra
#include <stdio.h>                                      // printf e fgets
#include <ctype.h>                                      // isalpha e toupper

int main(void) {                                        // início do programa
    char s[1001];                                       // a string lida
    printf("Texto: ");                                  // pede o texto
    fgets(s, sizeof s, stdin);                          // lê a linha inteira
    int primeira[26];                                   // primeira[k]: posição da 1ª ocorrência da letra 'A' + k
    for (int k = 0; k < 26; k++) primeira[k] = -1;      // -1 = ainda não apareceu
    for (int i = 0; s[i] != '\0'; i++) {                // percorre o texto
        if (isalpha((unsigned char)s[i])) {             // só letras (sem acento)
            int k = toupper((unsigned char)s[i]) - 'A'; // 'O' - 'A' = 14: a letra vira índice
            if (primeira[k] == -1) primeira[k] = i;     // guarda só a primeira vez
        }
    }
    for (int k = 0; k < 26; k++)                        // de A a Z, em ordem
        if (primeira[k] != -1) printf("%c(%d) ", 'A' + k, primeira[k]);   // só as letras que apareceram
    printf("\n");                                       // termina a linha
    return 0;                                           // fim sem erro
}
