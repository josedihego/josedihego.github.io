// A3-2025.2 – Questão I: A mensagem pode ter sido escrita por alienígenas?
#include <stdio.h>                                      // printf e fgets

void tira_enter(char s[]) {                             // troca o '\n' que o fgets guarda por '\0'
    for (int i = 0; s[i] != '\0'; i++)                  // procura o Enter
        if (s[i] == '\n') s[i] = '\0';                  // achou: a string termina aqui
}

int contem(char s[], char c) {                          // 1 se o caractere c aparece em s
    for (int i = 0; s[i] != '\0'; i++)                  // percorre s
        if (s[i] == c) return 1;                        // achou
    return 0;                                           // chegou ao fim sem achar
}

int main(void) {                                        // início do programa
    char alfabeto[100], msg[1001];                      // símbolos alienígenas e mensagem interceptada
    printf("Alfabeto: ");                               // pede o alfabeto
    fgets(alfabeto, sizeof alfabeto, stdin);            // lê a linha
    tira_enter(alfabeto);                               // remove o Enter do fim
    printf("Mensagem: ");                               // pede a mensagem
    fgets(msg, sizeof msg, stdin);                      // lê a linha
    tira_enter(msg);                                    // remove o Enter
    int pode = 1;                                       // supõe que sim
    for (int i = 0; msg[i] != '\0'; i++)                // cada símbolo da mensagem
        if (!contem(alfabeto, msg[i])) pode = 0;        // símbolo fora do alfabeto
    if (pode) printf("A mensagem pode ter sido escrita por alienígenas\n"); // nenhuma regra foi violada
    else printf("A mensagem não pode ter sido escrita por alienígenas\n"); // alguma regra foi violada
    return 0;                                           // fim sem erro
}
