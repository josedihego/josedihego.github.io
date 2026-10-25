// A4-2026.1 – Questão II: Classificador por vizinhança (distância de Manhattan)
// teste: 4 120 80 -1 140 86 1 125 110 1 115 75 -1 25 118 85 => BAIXO RISCO
// teste: 4 120 80 -1 140 86 1 125 110 1 115 75 -1 35 118 85 => INCONCLUSIVO
// teste: 4 120 80 -1 140 86 1 125 110 1 115 75 -1 5 118 85 => INCONCLUSIVO
// teste: 4 120 80 -1 140 86 1 125 110 1 115 75 -1 24 138 90 => ALTO RISCO
#include <stdio.h>                                      // printf e scanf
#include <stdlib.h>                                     // abs
#define MAX 100                                         // a prova usa M = 10

int main(void) {                                        // início do programa
    int m, tab[MAX][3];                                 // pacientes: pressão, glicemia, risco (+1 ou -1)
    scanf("%d", &m);                                    // lê M (10 na prova)
    for (int i = 0; i < m; i++)                         // lê a tabela M x 3
        scanf("%d %d %d", &tab[i][0], &tab[i][1], &tab[i][2]); // pressão, glicemia e risco do paciente i
    int limiar, pressao, glicemia;                      // parâmetro e dados do novo paciente
    scanf("%d %d %d", &limiar, &pressao, &glicemia);    // lê os três valores
    int votos = 0;                                      // soma dos riscos dos vizinhos (+1 alto, -1 baixo)
    for (int i = 0; i < m; i++) {                       // cada paciente anterior
        int d = abs(pressao - tab[i][0]) + abs(glicemia - tab[i][1]);   // distância de Manhattan
        if (d < limiar) votos += tab[i][2];             // vizinho (estritamente menor): vota
    }
    if (votos > 0) printf("ALTO RISCO\n");              // mais vizinhos de alto risco
    else if (votos < 0) printf("BAIXO RISCO\n");        // mais vizinhos de baixo risco
    else printf("INCONCLUSIVO\n");                      // empate (inclusive 0 a 0)
    return 0;                                           // fim sem erro
}
