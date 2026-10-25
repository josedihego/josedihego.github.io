// Aula 10 – Experimento: dicionário em vetor ordenado contra vetor desordenado
// Saída CSV: n, ord_insercao, ord_busca, des_insercao, des_busca
// (elementos movidos nas n inserções; comparações nas n buscas com sucesso)
#include <stdio.h>
#include <stdlib.h>

unsigned long long estado = 0x243F6A8885A308D3ULL;
unsigned sorteia(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return (unsigned)(estado >> 16);
}

int main(void) {
    printf("n,ord_insercao,ord_busca,des_insercao,des_busca\n");
    for (int n = 1000; n <= 16000; n += 1000) {
        unsigned *chaves = malloc(n * sizeof(unsigned));
        unsigned *v = malloc(n * sizeof(unsigned));
        for (int i = 0; i < n; i++) chaves[i] = sorteia();
        long mov = 0, comp = 0;
        int tam = 0;
        // vetor ordenado: busca a posição e desloca
        for (int i = 0; i < n; i++) {
            int lo = 0, hi = tam;
            while (lo < hi) {
                int m = (lo + hi) / 2;
                if (v[m] < chaves[i]) lo = m + 1; else hi = m;
            }
            for (int j = tam; j > lo; j--) { v[j] = v[j - 1]; mov++; }
            v[lo] = chaves[i];
            tam++;
        }
        for (int i = 0; i < n; i++) {            // n buscas binárias com sucesso
            int lo = 0, hi = n;
            while (lo < hi) {
                int m = (lo + hi) / 2;
                comp++;
                if (v[m] < chaves[i]) lo = m + 1; else hi = m;
            }
        }
        long mov_ord = mov, comp_ord = comp;
        // vetor desordenado: insere no fim (0 movimentos)
        comp = 0;
        for (int i = 0; i < n; i++) v[i] = chaves[i];
        for (int i = 0; i < n; i++)             // busca linear com sucesso
            for (int j = 0; j < n; j++) { comp++; if (v[j] == chaves[i]) break; }
        printf("%d,%ld,%ld,%d,%ld\n", n, mov_ord, comp_ord, 0, comp);
        free(chaves); free(v);
    }
    return 0;
}
