// A3-2023.2 – Questão I: Gotejamento na parede com prateleiras
// teste: 9 14;.......o......;.###...####.#.;..............;..######......;..............;.#.####....##.;..............;.....####.....;.............. => ......oooooo..
// teste: 9 14;.......o......;.###...####.#.;..............;..######......;..............;.#.####....##.;..............;.....####.....;.............. => o.o.o####oo..o
// teste: 9 14;.......o......;.###...####.#.;..............;..######......;..............;.#.####....##.;..............;.....####.....;.............. => o.o.o....oo..o
#include <stdio.h>                                      // printf e scanf
#define MAX 100                                         // maior parede aceita

int main(void) {                                        // início do programa
    int n, m;                                           // linhas e colunas
    char p[MAX][MAX + 1];                               // a parede: '.', '#' e 'o'
    scanf("%d %d", &n, &m);                             // lê as dimensões
    for (int i = 0; i < n; i++) scanf("%s", p[i]);      // lê cada linha
    int mudou = 1;                                      // repete enquanto alguma casa virar 'o'
    while (mudou) {                                     // aplica as regras até estabilizar
        mudou = 0;                                      // nesta passada, ainda nada mudou
        for (int i = 0; i < n; i++) {                   // cada linha
            for (int j = 0; j < m; j++) {               // cada coluna
                if (p[i][j] != '.') continue;           // só a parede vazia pode molhar
                int cai = i > 0 && p[i - 1][j] == 'o';                                   // água logo acima
                int esq = j > 0 && i + 1 < n && p[i][j - 1] == 'o' && p[i + 1][j - 1] == '#';   // escorre da esquerda sobre prateleira
                int dir = j + 1 < m && i + 1 < n && p[i][j + 1] == 'o' && p[i + 1][j + 1] == '#'; // escorre da direita
                if (cai || esq || dir) { p[i][j] = 'o'; mudou = 1; }   // molhou: talvez molhe vizinhos na próxima passada
            }
        }
    }
    for (int i = 0; i < n; i++) printf("%s\n", p[i]);   // padrão final
    return 0;                                           // fim sem erro
}
