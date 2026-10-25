// Aula 30 – Experimento: custo por operação de conjuntos disjuntos
// Tabelas CSV: ponteiros seguidos por operação (n uniões e 4n buscas)
#include <stdio.h>
#include <stdlib.h>

int *pai, *posto;
long passos;

unsigned long long estado = 0xC2B2AE3D27D4EB4FULL;
unsigned sorteia(unsigned limite) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)((estado >> 11) % limite);
}

int acha_ingenuo(int x) {                      // sobe até a raiz, sem comprimir
    while (pai[x] != x) { x = pai[x]; passos++; }
    return x;
}
void une_ingenuo(int x, int y) {               // pendura a raiz de x na de y, sem posto
    x = acha_ingenuo(x); y = acha_ingenuo(y);
    if (x != y) pai[x] = y;
}

int acha(int x) {                              // compressão de caminho (iterativa)
    int r = x;
    while (pai[r] != r) { r = pai[r]; passos++; }
    while (pai[x] != r) { int p = pai[x]; pai[x] = r; x = p; }
    return r;
}
void une(int x, int y) {                       // união por posto
    x = acha(x); y = acha(y);
    if (x == y) return;
    if (posto[x] > posto[y]) pai[y] = x;
    else { pai[x] = y; if (posto[x] == posto[y]) posto[y]++; }
}

/* m = 5n operações: as uniões ligam 0-1, 1-2, 2-3, ... (pior caso do ingênuo,
   que forma uma corrente); as demais são buscas de elementos sorteados. */
double custo_por_operacao(int n, int heur) {
    int m = 5 * n;
    for (int x = 0; x < n; x++) { pai[x] = x; posto[x] = 0; }
    passos = 0;
    for (int k = 0; k < m; k++) {
        if (k % 5 == 0) {
            int x = k / 5, y = (k / 5 + 1) % n;
            if (heur) une(x, y); else une_ingenuo(x, y);
        } else {
            int x = (int)sorteia(n);
            if (heur) acha(x); else acha_ingenuo(x);
        }
    }
    return (double)passos / m;
}

int main(void) {
    int N = 1 << 21;
    pai = malloc(N * sizeof(int));
    posto = malloc(N * sizeof(int));
    printf("n,ingenuo,heuristicas\n");            // o ingênuo é quadrático: n pequeno
    for (int n = 1000; n <= 16000; n += 1000)
        printf("%d,%.4f,%.4f\n", n, custo_por_operacao(n, 0), custo_por_operacao(n, 1));
    printf("\nn,heuristicas_grande\n");
    for (int n = 1 << 12; n <= N; n *= 2)
        printf("%d,%.4f\n", n, custo_por_operacao(n, 1));
    free(pai); free(posto);
    return 0;
}
