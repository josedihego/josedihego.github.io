// Aula 30 – Nível 3: Função com duas respostas
// teste: 
#include <stdio.h>                                                    // printf

void min_max(int v[], int n, int *menor, int *maior) {                // as respostas voltam pelos ponteiros
    *menor = *maior = v[0];                                           // os dois começam com o primeiro elemento
    for (int i = 1; i < n; i++) {                                     // começa no 1: o 0 já é o valor inicial
        if (v[i] < *menor) *menor = v[i];                             // atualiza o menor pelo ponteiro
        if (v[i] > *maior) *maior = v[i];                             // atualiza o maior pelo ponteiro
    }
}

int main(void) {                                                      // início do programa
    int leituras[] = {612, 598, 640, 575, 633};                       // leituras de exemplo
    int mn, mx;                                                       // vão receber as respostas
    min_max(leituras, 5, &mn, &mx);                                   // passa os endereços de mn e mx
    printf("Menor %d, maior %d, variação %d\n", mn, mx, mx - mn);     // mostra mn e mx e mx - mn formatados
    return 0;                                                         // termina com sucesso
}
