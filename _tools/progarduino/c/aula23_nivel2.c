// Aula 23 – Nível 2: Simulado: média até digitar negativo
// teste: 8; 6.5; 9; -1
#include <stdio.h>                                       // printf e scanf

int main(void) {                                         // início do programa
    float nota, soma = 0;                                // nota lida e acumulador
    int n = 0;                                           // contador começa em zero
    printf("Notas (negativo para terminar): ");          // pergunta ao usuário
    scanf("%f", &nota);                                  // lê o valor digitado e guarda em nota
    while (nota >= 0) {                                  // lê até aparecer um negativo
        soma += nota;                                    // acumula a nota
        n++;                                             // conta mais um
        scanf("%f", &nota);                              // lê o valor digitado e guarda em nota
    }
    if (n > 0) printf("Média de %d notas: %.2f\n", n, soma / n);   // só calcula se houver notas
    return 0;                                            // termina com sucesso
}
