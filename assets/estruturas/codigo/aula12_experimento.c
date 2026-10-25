// Aula 12 – Experimento: simulação de uma fila de atendimento (M/M/1)
// Saída CSV: rho, espera (tempo médio na fila; atendimento médio = 1)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Clientes chegam com intervalos exponenciais de média 1/rho e são atendidos em
   ordem de chegada (FIFO) com tempos exponenciais de média 1. A fila guarda os
   instantes de chegada; a teoria das filas prevê espera média rho/(1 - rho). */
unsigned long long estado = 0x452821E638D01377ULL;
double uniforme(void) {
    estado ^= estado << 13; estado ^= estado >> 7; estado ^= estado << 17;
    return ((estado >> 11) + 0.5) / 9007199254740992.0;
}
double exponencial(double media) { return -media * log(uniforme()); }

int main(void) {
    int N = 2000000, cap = 1 << 22;
    double *fila = malloc(cap * sizeof(double));   // fila circular de chegadas
    printf("rho,espera\n");
    for (int q = 1; q <= 17; q++) {
        double rho = q * 0.05;
        int cabeca = 0, cauda = 0, tam = 0;
        double t_chegada = exponencial(1 / rho), t_fim = INFINITY, soma = 0;
        int atendidos = 0;
        while (atendidos < N) {
            if (t_chegada < t_fim) {               // evento: chegada
                if (tam == 0 && t_fim == INFINITY) t_fim = t_chegada + exponencial(1);
                else { fila[cauda] = t_chegada; cauda = (cauda + 1) % cap; tam++; }
                t_chegada += exponencial(1 / rho);
            } else {                               // evento: fim de um atendimento
                atendidos++;
                if (tam == 0) { t_fim = INFINITY; continue; }
                double chegou = fila[cabeca];      // DEQUEUE: o mais antigo
                cabeca = (cabeca + 1) % cap; tam--;
                soma += t_fim - chegou;            // quanto ele esperou na fila
                t_fim += exponencial(1);
            }
        }
        printf("%.2f,%.4f\n", rho, soma / N);
    }
    free(fila);
    return 0;
}
