// Aula 32 – Caminhos mínimos entre todos os pares: Floyd-Warshall (Cormen, seção 25.2)
// teste: 1 => 0 1 -3 2 -4
// teste: 1 => 8 5 1 6 0
#include <stdio.h>

/* O grafo da Figura 25.1 (5 vértices, pesos negativos, sem ciclo negativo).
   D^(k)[i][j]: menor caminho de i a j com intermediários só entre os vértices 1..k. */
#define V 5
#define INF 1000000

int main(void) {
    int qualquer;
    if (scanf("%d", &qualquer) != 1) return 1;
    int D[V][V];
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++) D[i][j] = i == j ? 0 : INF;
    int arestas[][3] = {{0, 1, 3}, {0, 2, 8}, {0, 4, -4}, {1, 3, 1}, {1, 4, 7},
                        {2, 1, 4}, {3, 0, 2}, {3, 2, -5}, {4, 3, 6}};
    for (int e = 0; e < 9; e++) D[arestas[e][0]][arestas[e][1]] = arestas[e][2];
    for (int k = 0; k < V; k++)                 // k: novo intermediário permitido
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                if (D[i][k] < INF && D[k][j] < INF && D[i][k] + D[k][j] < D[i][j])
                    D[i][j] = D[i][k] + D[k][j];   // passar por k é melhor
    for (int i = 0; i < V; i++) {               // a matriz D^(5) da Figura 25.4
        for (int j = 0; j < V; j++) printf("%d%c", D[i][j], j < V - 1 ? ' ' : '\n');
    }
    return 0;
}
