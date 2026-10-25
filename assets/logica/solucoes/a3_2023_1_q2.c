// A3-2023.1 – Questão II: Consenso de cinco fitas de DNA
#include <stdio.h>                                      // printf e scanf
#include <string.h>                                     // strlen

int main(void) {                                        // início do programa
    char f[5][9];                                       // 5 fitas de até 8 caracteres
    for (int k = 0; k < 5; k++) scanf("%8s", f[k]);     // lê as fitas
    const char *bases = "ACGT";                         // as quatro enzimas
    int t = strlen(f[0]);                               // todas têm o mesmo tamanho
    for (int i = 0; i < t; i++) {                       // cada posição da fita
        int conta[4] = {0};                             // frequência de A, C, G, T nesta posição
        for (int k = 0; k < 5; k++)                     // olha a posição i nas 5 fitas
            for (int b = 0; b < 4; b++)                 // compara com cada uma das 4 bases
                if (f[k][i] == bases[b]) conta[b]++;    // conta a enzima encontrada
        int melhor = 0, empate = 0;                     // índice da mais frequente e se há empate
        for (int b = 1; b < 4; b++) {                   // procura a maior contagem
            if (conta[b] > conta[melhor]) { melhor = b; empate = 0; }   // nova maior: desfaz empate
            else if (conta[b] == conta[melhor]) empate = 1;             // igual à maior: empate
        }
        printf("%c", empate ? '?' : bases[melhor]);     // '?' quando não há consenso
    }
    printf("\n");                                       // fim da fita
    return 0;                                           // fim sem erro
}
