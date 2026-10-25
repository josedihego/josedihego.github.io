// A1-2026.1 – Questão I: Teleférico – número mínimo de viagens
// teste: 10 20 => 3
// teste: 2 5 => 5
// teste: 10 18 => 2
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int capacidade, alunos;                             // pessoas por viagem (>= 2) e total de alunos
    printf("Capacidade da cabine e número de alunos: ");   // pede os dados
    scanf("%d %d", &capacidade, &alunos);               // lê os dois inteiros
    int por_viagem = capacidade - 1;                    // uma vaga é sempre do monitor
    int viagens = (alunos + por_viagem - 1) / por_viagem;   // divisão arredondada para cima, só com inteiros
    printf("Mínimo de viagens: %d\n", viagens);         // 20 alunos, 9 por viagem → 3
    return 0;                                           // fim sem erro
}
