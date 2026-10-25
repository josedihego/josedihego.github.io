// A2-2014.2 – Questão II: Os N primeiros pares de primos gêmeos
// teste: 3 => (11, 13)
// teste: 6 => (41, 43)
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int n;                                              // quantos pares mostrar
    printf("N: ");                                      // pede N
    scanf("%d", &n);                                    // lê N
    int achados = 0;                                    // pares já mostrados
    for (int p = 3; achados < n; p += 2) {              // candidatos ímpares 3, 5, 7...
        int p_primo = 1, q_primo = 1;                   // supõe que p e p + 2 são primos
        for (int d = 3; d * d <= p + 2; d += 2) {       // testa divisores ímpares até a raiz
            if (p % d == 0 && d < p) p_primo = 0;       // d divide p (e não é o próprio p)
            if ((p + 2) % d == 0 && d < p + 2) q_primo = 0;   // d divide p + 2
        }
        if (p_primo && q_primo) {                       // os dois primos: é um par de gêmeos
            printf("(%d, %d)\n", p, p + 2);             // mostra o par
            achados++;                                  // conta o par
        }
    }
    return 0;                                           // fim sem erro
}
