// Aula 30 – Nível 1: Endereço e conteúdo
// teste: 
#include <stdio.h>                                           // printf

int main(void) {                                             // início do programa
    int tensao = 5;                                          // variável comum
    int *p = &tensao;                                        // p guarda o ENDEREÇO de tensao
    printf("Valor de tensao: %d\n", tensao);                 // mostra tensao formatados
    printf("Endereço de tensao: %p\n", (void *)&tensao);     // & = endereço de
    printf("p aponta para: %p\n", (void *)p);                // mostra (void *)p formatados
    printf("*p (conteúdo apontado): %d\n", *p);              // * = valor no endereço
    *p = 12;                                                 // muda tensao através do ponteiro
    printf("Agora tensao vale %d\n", tensao);                // mostra tensao formatados
    return 0;                                                // termina com sucesso
}
