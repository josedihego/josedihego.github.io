// A1-2023.1 – Questão I: Área de reserva (sobreposição de dois terrenos)
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int x1, y1, v1, h1, x2, y2, v2, h2;                 // canto superior esquerdo, dimensão vertical e horizontal
    printf("Terreno 1 (x y vertical horizontal) e terreno 2: ");   // pede os oito valores
    scanf("%d %d %d %d %d %d %d %d", &x1, &y1, &v1, &h1, &x2, &y2, &v2, &h2); // posição, velocidade e direção de cada carro
    // no mapa o y cresce para baixo: o terreno 1 ocupa x de x1 a x1+h1 e y de y1 a y1+v1
    int esq = x1 > x2 ? x1 : x2;                        // borda esquerda da sobreposição: o maior dos x
    int dir = (x1 + h1) < (x2 + h2) ? (x1 + h1) : (x2 + h2);   // borda direita: a menor das direitas
    int topo = y1 > y2 ? y1 : y2;                       // borda de cima: o maior dos y
    int base = (y1 + v1) < (y2 + v2) ? (y1 + v1) : (y2 + v2);  // borda de baixo: a menor das bases
    if (esq < dir && topo < base) {                     // largura e altura positivas: existe área
        printf("%d %d %d %d\n", esq, topo, dir - esq, base - topo);   // x, y, horizontal, vertical
    } else {                                            // só encostam ou nem se tocam
        printf("NÃO EXISTE ÁREA SUGERIDA\n");           // mensagem pedida
    }
    return 0;                                           // fim sem erro
}
