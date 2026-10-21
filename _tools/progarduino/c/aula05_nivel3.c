// Aula 5 – Nível 3: Implicação e OU exclusivo
// teste: 1; 0
#include <stdio.h>                                           // printf e scanf

int main(void) {                                             // início do programa
    int p, q;                                                // valores lógicos (0 ou 1)
    printf("p (0 ou 1): ");                                  // pergunta ao usuário
    scanf("%d", &p);                                         // lê o valor digitado e guarda em p
    printf("q (0 ou 1): ");                                  // pergunta ao usuário
    scanf("%d", &q);                                         // lê o valor digitado e guarda em q
    int implica = !p || q;                                   // p → q equivale a (não p) ou q
    int xou = (p || q) && !(p && q);                         // XOR: um ou outro, mas não os dois
    printf("p -> q = %d\n", implica);                        // mostra implica formatados
    printf("p XOR q = %d\n", xou);                           // mostra xou formatados
    return 0;                                                // termina com sucesso
}
