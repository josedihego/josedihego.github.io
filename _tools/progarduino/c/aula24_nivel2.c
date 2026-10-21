// Aula 24 – Nível 2: Revisão: dados até sair 6
// teste: 
#include <stdio.h>                                  // printf
#include <stdlib.h>                                 // rand e srand
#include <time.h>                                   // time

int main(void) {                                    // início do programa
    srand(time(NULL));                              // semente diferente a cada execução
    int jogadas = 0, dado;                          // contador e valor do dado
    do {                                            // executa o bloco pelo menos uma vez
        dado = rand() % 6 + 1;                      // sorteia de 1 a 6
        jogadas++;                                  // conta a jogada
        printf("%d ", dado);                        // mostra dado formatados
    } while (dado != 6);                            // para no 6
    printf("\nSaiu 6 na jogada %d\n", jogadas);     // mostra jogadas formatados
    return 0;                                       // termina com sucesso
}
