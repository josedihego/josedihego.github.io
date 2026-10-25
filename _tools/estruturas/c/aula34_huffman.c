// Aula 34 – Códigos de Huffman (Cormen, seção 16.3)
// teste: 45 13 12 16 9 5 => a:0 b:101 c:100 d:111 e:1101 f:1100
// teste: 45 13 12 16 9 5 => 224 mil bits
#include <stdio.h>

/* Frequências (em milhares) de a..f, como na Figura 16.3. A fila de prioridade é
   um vetor simples: com 6 símbolos, achar o mínimo por varredura basta. */
#define MAX 64
int freq[2 * MAX], esq[2 * MAX], dir[2 * MAX], vivo[2 * MAX], n_nos;
char codigo[MAX][MAX];

int extrai_min(void) {
    int m = -1;
    for (int i = 0; i < n_nos; i++)
        if (vivo[i] && (m < 0 || freq[i] < freq[m])) m = i;
    vivo[m] = 0;
    return m;
}

void gera(int x, char *prefixo, int prof, int n) {   // percorre a árvore: 0 esq, 1 dir
    if (x < n) { prefixo[prof] = '\0'; sprintf(codigo[x], "%s", prefixo); return; }
    prefixo[prof] = '0'; gera(esq[x], prefixo, prof + 1, n);
    prefixo[prof] = '1'; gera(dir[x], prefixo, prof + 1, n);
}

int main(void) {
    int n = 0;
    while (n < MAX && scanf("%d", &freq[n]) == 1) { vivo[n] = 1; n++; }
    if (n < 2) return 1;
    n_nos = n;
    for (int k = 1; k < n; k++) {             // HUFFMAN: n - 1 junções
        int x = extrai_min(), y = extrai_min();
        freq[n_nos] = freq[x] + freq[y];       // novo nó z com filhos x e y
        esq[n_nos] = x;
        dir[n_nos] = y;
        vivo[n_nos++] = 1;
    }
    char prefixo[MAX];
    gera(n_nos - 1, prefixo, 0, n);
    long bits = 0;
    for (int i = 0; i < n; i++) {
        printf("%c:%s ", 'a' + i, codigo[i]);
        for (int j = 0; codigo[i][j]; j++) bits += freq[i];
    }
    printf("\n%ld mil bits\n", bits);
    return 0;
}
