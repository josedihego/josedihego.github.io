// Aula 34 – Experimento: Huffman contra a entropia de Shannon e o código fixo
// Saída CSV: n, huffman, entropia, fixo (bits por símbolo; n símbolos com lei de Zipf)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Frequências de Zipf: o símbolo i aparece proporcionalmente a 1/i (palavras, letras,
   bytes de arquivos seguem leis parecidas). Huffman com heap: O(n lg n). */
double *f;
int *heap, tam;

void sobe(int i) {
    while (i > 0 && f[heap[(i - 1) / 2]] > f[heap[i]]) {
        int p = (i - 1) / 2, t = heap[i];
        heap[i] = heap[p];
        heap[p] = t;
        i = p;
    }
}
int extrai(void) {
    int r = heap[0];
    heap[0] = heap[--tam];
    for (int i = 0;;) {
        int e = 2 * i + 1, d = e + 1, m = i;
        if (e < tam && f[heap[e]] < f[heap[m]]) m = e;
        if (d < tam && f[heap[d]] < f[heap[m]]) m = d;
        if (m == i) break;
        int t = heap[i]; heap[i] = heap[m]; heap[m] = t;
        i = m;
    }
    return r;
}

int main(void) {
    printf("n,huffman,entropia,fixo\n");
    for (int n = 2; n <= 4096; n *= 2) {
        f = malloc(2 * n * sizeof(double));
        int *pai = malloc(2 * n * sizeof(int));
        heap = malloc(2 * n * sizeof(int));
        double soma = 0, H = 0;
        for (int i = 0; i < n; i++) { f[i] = 1.0 / (i + 1); soma += f[i]; }
        for (int i = 0; i < n; i++) { f[i] /= soma; H -= f[i] * log2(f[i]); }
        tam = 0;
        for (int i = 0; i < n; i++) { heap[tam] = i; sobe(tam++); }
        int prox = n;
        for (int k = 1; k < n; k++) {           // junta os dois menos frequentes
            int x = extrai(), y = extrai();
            f[prox] = f[x] + f[y];
            pai[x] = pai[y] = prox;
            heap[tam] = prox; sobe(tam++);
            prox++;
        }
        // comprimento médio = soma f_i · profundidade
        double L = 0;
        for (int i = 0; i < n; i++) {
            int prof = 0;
            for (int x = i; x != prox - 1; x = pai[x]) prof++;
            L += f[i] * prof;
        }
        if (L < H - 1e-9 || L >= H + 1) {      // teorema de Shannon: H <= L < H + 1
            fprintf(stderr, "fora de [H, H+1)!\n");
            return 1;
        }
        printf("%d,%.4f,%.4f,%d\n", n, L, H, (int)ceil(log2(n)));
        free(f); free(pai); free(heap);
    }
    return 0;
}
