// A1-2023.2 – Questão II: Mutação por swap (inverter um bit)
// teste: 28 3 => 20
// teste: 20 3 => 28
// teste: 5 0 => 4
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int individuo, bit;                                 // número entre 0 e 35 e bit entre 0 e 4
    printf("Indivíduo (0 a 35) e bit (0 a 4): ");       // pede os dados
    scanf("%d %d", &individuo, &bit);                   // lê os dois inteiros
    if (individuo < 0 || individuo > 35 || bit < 0 || bit > 4) {   // fora dos limites do enunciado
        printf("Valores inválidos\n");                  // avisa
        return 1;                                       // fim com erro
    }
    int mascara = 1 << bit;                             // 1 deslocado: só o bit escolhido ligado (bit 3 → 01000)
    int mutante = individuo ^ mascara;                  // XOR inverte exatamente esse bit
    printf("Novo indivíduo: %d\n", mutante);            // 28 (11100) → 20 (10100)
    return 0;                                           // fim sem erro
}
