// Base 2 – Ponteiros: endereços, aritmética, passagem por referência e ponteiro duplo
// teste: 3 4 => troca: a = 4, b = 3
// teste: 3 4 => matriz 3 x 4: m[2][3] = 23
// teste: 3 4 => vetor via ponteiro duplo: 0 10 20
#include <stdio.h>
#include <stdlib.h>

// passagem por referência: recebe endereços
void troca(int *a, int *b) {
    int t = *a;                                 // *a: o valor guardado no endereço a
    *a = *b;
    *b = t;
}

/* Para que uma função ALTERE um ponteiro do chamador, ela recebe o endereço do
   ponteiro: um ponteiro para ponteiro (int **). */
void aloca_vetor(int **p, int n) {
    *p = malloc(n * sizeof **p);
    for (int i = 0; i < n; i++) (*p)[i] = 10 * i;
}

/* Matriz dinâmica: um vetor de ponteiros para linhas (int **). Uma alocação para
   os ponteiros e outra, contígua, para todos os elementos. */
int **cria_matriz(int lin, int col) {
    int **m = malloc(lin * sizeof *m);
    m[0] = malloc((size_t)lin * col * sizeof **m);
    for (int i = 1; i < lin; i++) m[i] = m[0] + i * col;   // aritmética de ponteiros
    return m;
}

void libera_matriz(int **m) { free(m[0]); free(m); }

int main(void) {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2 || a < 1 || b < 1) return 1;
    int lin = a, col = b;
    troca(&a, &b);                              // &a: o endereço de a
    printf("troca: a = %d, b = %d\n", a, b);
    int v[3] = {7, 8, 9}, *q = v;               // o nome do vetor é o endereço do 1º
    printf("v[1] = %d = *(v + 1) = %d = q[1] = %d\n", v[1], *(v + 1), q[1]);
    int **m = cria_matriz(lin, col);
    for (int i = 0; i < lin; i++)
        for (int j = 0; j < col; j++) m[i][j] = 10 * i + j;
    printf("matriz %d x %d: m[%d][%d] = %d\n", lin, col, lin - 1, col - 1,
           m[lin - 1][col - 1]);
    libera_matriz(m);
    int *w = NULL;
    aloca_vetor(&w, 3);                         // w muda dentro da função
    printf("vetor via ponteiro duplo: %d %d %d\n", w[0], w[1], w[2]);
    free(w);
    return 0;
}
