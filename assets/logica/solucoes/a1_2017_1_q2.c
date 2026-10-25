// A1-2017.1 – Questão II: Jogo do bicho – valor do prêmio
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    double v;                                           // valor apostado
    int n, m;                                           // número apostado e número sorteado
    printf("Valor, número apostado e número sorteado: ");   // pede os dados
    scanf("%lf %d %d", &v, &n, &m);                     // lê os três valores
    int dn = n % 100, dm = m % 100;                     // dois últimos dígitos (dezena e unidade)
    if (dn == 0) dn = 100;                              // 00 pertence ao último grupo (97, 98, 99, 00)
    if (dm == 0) dm = 100;                              // idem
    double premio;                                      // valor a receber
    if (n % 10000 == m % 10000) premio = v * 3000;      // milhar: quatro últimos dígitos iguais
    else if (n % 1000 == m % 1000) premio = v * 500;    // centena: três últimos
    else if (n % 100 == m % 100) premio = v * 50;       // dezena: dois últimos
    else if ((dn - 1) / 4 == (dm - 1) / 4) premio = v * 16;   // mesmo grupo: 01-04 → 0, 05-08 → 1...
    else premio = 0;                                    // nenhum critério
    printf("Prêmio: R$ %.2f\n", premio);                // o else if garante só o maior prêmio
    return 0;                                           // fim sem erro
}
