// Aula 30 – Nível 2: Trocar dois valores
// teste: 3; 8
#include <stdio.h>                                       // printf e scanf

void trocar(int *a, int *b) {                            // recebe endereços
    int aux = *a;                                        // guarda o valor apontado por a
    *a = *b;                                             // o valor apontado por b vai para a
    *b = aux;                                            // o valor guardado vai para b
}

int main(void) {                                         // início do programa
    int x, y;                                            // os dois valores a trocar
    printf("x e y: ");                                   // pergunta ao usuário
    scanf("%d %d", &x, &y);                              // lê o valor digitado e guarda em x, y
    trocar(&x, &y);                                      // passa os endereços: a função altera x e y
    printf("Depois de trocar: x = %d, y = %d\n", x, y);   // mostra x e y formatados
    return 0;                                            // termina com sucesso
}
