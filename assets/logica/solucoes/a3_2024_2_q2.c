// A3-2024.2 – Questão II: Posição da primeira ocorrência de cada letra
#include <stdio.h>                                      // printf e fgets

int main(void) {                                        // início do programa
    char s[1001];                                       // a string lida
    printf("Texto: ");                                  // pede o texto
    fgets(s, sizeof s, stdin);                          // lê a linha inteira
    int primeira[26];                                   // primeira[k]: posição da 1ª ocorrência da letra 'A' + k
    for (int k = 0; k < 26; k++) primeira[k] = -1;      // -1 = ainda não apareceu
    for (int i = 0; s[i] != '\0'; i++) {                // percorre o texto
        int k = -1;                                     // índice da letra (−1: não é letra)
        if (s[i] >= 'A' && s[i] <= 'Z') k = s[i] - 'A'; // maiúscula: 'O' - 'A' = 14
        if (s[i] >= 'a' && s[i] <= 'z') k = s[i] - 'a'; // minúscula: 'o' - 'a' = 14
        if (k != -1) {                                  // só letras (sem acento)
            if (primeira[k] == -1) primeira[k] = i;     // guarda só a primeira vez
        }
    }
    for (int k = 0; k < 26; k++)                        // de A a Z, em ordem
        if (primeira[k] != -1) printf("%c(%d) ", 'A' + k, primeira[k]);   // só as letras que apareceram
    printf("\n");                                       // termina a linha
    return 0;                                           // fim sem erro
}
