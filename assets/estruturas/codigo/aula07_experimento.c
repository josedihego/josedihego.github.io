// Aula 7 – Experimento: três algoritmos para o subarranjo máximo
// Saída CSV: n, forca_bruta, divisao, kadane (somas realizadas por cada um)
#include <stdio.h>
#include <stdlib.h>

long ops;

long forca_bruta(const int A[], int n) {          // todos os pares (i, j): Θ(n²)
    long melhor = A[0];
    for (int i = 0; i < n; i++) {
        long s = 0;
        for (int j = i; j < n; j++) {
            s += A[j]; ops++;
            if (s > melhor) melhor = s;
        }
    }
    return melhor;
}

long cruzando(const int A[], int lo, int meio, int hi) {
    long s = 0, esq = A[meio], dir = A[meio + 1];
    for (int i = meio; i >= lo; i--) { s += A[i]; ops++; if (s > esq) esq = s; }
    s = 0;
    for (int j = meio + 1; j <= hi; j++) { s += A[j]; ops++; if (s > dir) dir = s; }
    return esq + dir;
}

long divisao(const int A[], int lo, int hi) {     // divisão e conquista: Θ(n lg n)
    if (lo == hi) return A[lo];
    int meio = (lo + hi) / 2;
    long e = divisao(A, lo, meio), d = divisao(A, meio + 1, hi);
    long c = cruzando(A, lo, meio, hi);
    return e > d ? (e > c ? e : c) : (d > c ? d : c);
}

long kadane(const int A[], int n) {               // exercício 4.1-5: Θ(n)
    long melhor = A[0], atual = 0;
    for (int i = 0; i < n; i++) {
        atual = atual > 0 ? atual + A[i] : A[i]; ops++;
        if (atual > melhor) melhor = atual;
    }
    return melhor;
}

int main(void) {
    srand(41);
    printf("n,forca_bruta,divisao,kadane\n");
    for (int n = 256; n <= 16384; n *= 2) {
        int *A = malloc(n * sizeof(int));
        for (int k = 0; k < n; k++) A[k] = rand() % 201 - 100;
        long r[3];
        ops = 0; long m1 = forca_bruta(A, n); r[0] = ops;
        ops = 0; long m2 = divisao(A, 0, n - 1); r[1] = ops;
        ops = 0; long m3 = kadane(A, n); r[2] = ops;
        if (m1 != m2 || m2 != m3) {             // os três têm de concordar
            fprintf(stderr, "respostas diferentes!\n");
            return 1;
        }
        printf("%d,%ld,%ld,%ld\n", n, r[0], r[1], r[2]);
        free(A);
    }
    return 0;
}
