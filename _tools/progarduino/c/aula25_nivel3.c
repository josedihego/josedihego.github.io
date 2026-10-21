// Aula 25 – Nível 3: Decimal para binário com vetor
// teste: 37
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    int decimal, bits[32], n = 0;                        // vetor guarda os restos
    printf("Decimal positivo: ");                        // pergunta ao usuário
    scanf("%d", &decimal);                               // lê o valor digitado e guarda em decimal
    int original = decimal;                              // guarda o valor para mostrar no fim
    do {                                                 // executa o bloco pelo menos uma vez
        bits[n] = decimal % 2;                           // resto: próximo bit (do menos significativo)
        decimal /= 2;                                    // divide por 2 (divisão inteira)
        n++;                                             // conta mais um
    } while (decimal > 0);                               // repete até o quociente ser zero
    printf("%d em binário: ", original);                 // mostra original formatados
    for (int i = n - 1; i >= 0; i--) printf("%d", bits[i]);   // mostra de trás para frente
    printf("\n");                                        // quebra a linha
    return 0;                                            // termina com sucesso
}
