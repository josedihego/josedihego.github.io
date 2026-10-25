// A2-2016.2 – Questão II: Os 20 primeiros termos da sequência de Recamán
// teste:  => 0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62
#include <stdio.h>                                      // printf
#define TAM 20                                          // trocar aqui muda o tamanho do vetor (mínimo impacto)

int main(void) {                                        // início do programa
    int a[TAM];                                         // os termos da sequência
    a[0] = 0;                                           // A0 = 0
    for (int n = 1; n < TAM; n++) {                     // calcula A1, A2, ...
        int candidato = a[n - 1] - n;                   // tenta voltar n posições
        int repetido = 0;                               // o candidato já está na sequência?
        for (int k = 0; k < n; k++)                     // procura entre os termos anteriores
            if (a[k] == candidato) repetido = 1;        // achou: não pode usar
        if (candidato > 0 && !repetido) a[n] = candidato;   // positivo e novo: usa a subtração
        else a[n] = a[n - 1] + n;                       // senão, avança n posições
    }
    for (int n = 0; n < TAM; n++) printf("%d%s", a[n], n < TAM - 1 ? ", " : "\n");   // mostra o vetor
    return 0;                                           // fim sem erro
}
