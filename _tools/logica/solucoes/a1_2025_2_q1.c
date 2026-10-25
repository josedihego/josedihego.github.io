// A1-2025.2 – Questão I: Beach tennis – a bola caiu dentro ou fora?
// teste: 8 -6 6 => dentro
// teste: 8 8 2 => dentro
// teste: 8 -4 10 => fora
// teste: 8 6 -2 => fora
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int k, x, y;                                        // tamanho da quadra e coordenada da bola
    printf("k, x e y: ");                               // pede os dados
    scanf("%d %d %d", &k, &x, &y);                      // lê os três inteiros
    // a quadra 2k x k tem o juiz no meio da linha de base: x vai de -k a k e y de 0 a k
    if (x >= -k && x <= k && y >= 0 && y <= k) {        // em cima da linha conta como dentro (>= e <=)
        printf("dentro\n");                             // bola válida
    } else {                                            // qualquer coordenada fora dos limites
        printf("fora\n");                               // bola fora
    }
    return 0;                                           // fim sem erro
}
