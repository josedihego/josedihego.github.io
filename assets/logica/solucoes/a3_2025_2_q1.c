// A3-2025.2 – Questão I: A mensagem pode ter sido escrita por alienígenas?
#include <stdio.h>                                      // printf e fgets
#include <string.h>                                     // strchr e strcspn

int main(void) {                                        // início do programa
    char alfabeto[100], msg[1001];                      // símbolos alienígenas e mensagem interceptada
    printf("Alfabeto: ");                               // pede o alfabeto
    fgets(alfabeto, sizeof alfabeto, stdin);            // lê a linha
    alfabeto[strcspn(alfabeto, "\n")] = '\0';           // remove o Enter do fim
    printf("Mensagem: ");                               // pede a mensagem
    fgets(msg, sizeof msg, stdin);                      // lê a linha
    msg[strcspn(msg, "\n")] = '\0';                     // remove o Enter
    int pode = 1;                                       // supõe que sim
    for (int i = 0; msg[i] != '\0'; i++)                // cada símbolo da mensagem
        if (strchr(alfabeto, msg[i]) == NULL) pode = 0; // strchr devolve NULL se o símbolo não está no alfabeto
    if (pode) printf("A mensagem pode ter sido escrita por alienígenas\n"); // nenhuma regra foi violada
    else printf("A mensagem não pode ter sido escrita por alienígenas\n"); // alguma regra foi violada
    return 0;                                           // fim sem erro
}
