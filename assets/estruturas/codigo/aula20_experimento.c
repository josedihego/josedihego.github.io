// Aula 20 – Experimento: chaves com padrão (múltiplos de 64) em quatro funções hash
// Saída CSV: n, div_pot2, div_primo, multiplicacao, universal
// (custo médio de busca com sucesso, com n = m chaves: fator de carga 1)
#include <stdio.h>
#include <stdlib.h>

unsigned m_atual, p_atual, primo_atual;
unsigned long long a_univ, b_univ;
const unsigned long long P = 4294967311ULL;    // primo maior que 2^32

unsigned f_pot2(unsigned k) { return k % m_atual; }
unsigned f_primo(unsigned k) { return k % primo_atual; }
unsigned f_mult(unsigned k) { return (k * 2654435769u) >> (32 - p_atual); }
unsigned f_univ(unsigned k) {                  // h_ab(k) = ((a k + b) mod p) mod m
    return (unsigned)(((a_univ * k + b_univ) % P) % m_atual);
}

double custo(unsigned (*h)(unsigned), unsigned tam, unsigned n) {
    int *cont = calloc(tam, sizeof(int));
    for (unsigned i = 1; i <= n; i++) cont[h(64 * i)]++;
    double soma = 0;                            // a chave na posição j de uma lista de
    for (unsigned j = 0; j < tam; j++)          // tamanho L custa j; total L(L+1)/2
        soma += (double)cont[j] * (cont[j] + 1) / 2;
    free(cont);
    return soma / n;
}

int main(void) {
    srand(20);
    printf("n,div_pot2,div_primo,multiplicacao,universal\n");
    for (p_atual = 10; p_atual <= 18; p_atual++) {
        m_atual = 1u << p_atual;
        primo_atual = m_atual + 1;              // menor primo maior que m
        for (;; primo_atual++) {
            int ok = 1;
            for (unsigned d = 2; d * d <= primo_atual; d++)
                if (primo_atual % d == 0) { ok = 0; break; }
            if (ok) break;
        }
        unsigned n = m_atual;
        double univ = 0;
        // a garantia é sobre a média da família:
        int sorteios = (1 << 26) / n;
        for (int s = 0; s < sorteios; s++) {    // sorteamos muitas funções
            a_univ = 1 + ((unsigned long long)rand() << 16 ^ rand()) % (P - 1);
            b_univ = ((unsigned long long)rand() << 16 ^ rand()) % P;
            univ += custo(f_univ, m_atual, n) / sorteios;
        }
        printf("%u,%.4f,%.4f,%.4f,%.4f\n", n, custo(f_pot2, m_atual, n),
               custo(f_primo, primo_atual, n), custo(f_mult, m_atual, n), univ);
    }
    return 0;
}
