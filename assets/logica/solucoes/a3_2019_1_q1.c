// A3-2019.1 – Questão I: Faixas de letras
#include <stdio.h>                                      // printf e fgets

int main(void) {                                        // início do programa
    char s[1001];                                       // texto com letras minúsculas e espaços
    printf("Texto: ");                                  // pede o texto
    fgets(s, sizeof s, stdin);                          // lê a linha
    int tem[26] = {0};                                  // tem[k] = 1 se a letra 'a' + k aparece
    for (int i = 0; s[i] != '\0'; i++)                  // marca as letras presentes
        if (s[i] >= 'a' && s[i] <= 'z') tem[s[i] - 'a'] = 1;   // ignora espaços e duplicadas
    for (int k = 0; k < 26; k++) {                      // percorre o alfabeto
        if (tem[k] && (k == 0 || !tem[k - 1])) {        // começo de faixa: tem a letra, mas não a anterior
            int fim = k;                                // estende enquanto as próximas letras existirem
            while (fim + 1 < 26 && tem[fim + 1]) fim++; // anda até o fim da faixa
            printf("%c:%c ", 'a' + k, 'a' + fim);       // imprime a faixa
        }
    }
    printf("\n");                                       // termina a linha
    return 0;                                           // fim sem erro
}
