// Aula 31 – Nível 1: Ponteiro andando pelo vetor
// teste: 
#include <stdio.h>                                      // printf

int main(void) {                                        // início do programa
    int v[] = {10, 20, 30, 40};                         // vetor de exemplo
    int *p = v;                                         // o nome do vetor é o endereço do 1º elemento
    for (int i = 0; i < 4; i++) {                       // percorre os 4 elementos
        printf("*(p + %d) = %d  em %p\n", i, *(p + i), (void *)(p + i));   // p + i avança i inteiros
    }
    return 0;                                           // termina com sucesso
}
