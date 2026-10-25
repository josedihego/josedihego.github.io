// A1-2025.2 – Questão II: Luiza – em que ponto descer e quanto andar
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int m, p, d;                                        // tamanho da avenida, distância entre pontos, distância da escola
    printf("M, P e D (metros): ");                      // pede os dados
    scanf("%d %d %d", &m, &p, &d);                      // lê os três inteiros
    if (d < 0 || d > m || p <= 0 || m % p != 0) {       // dados fora do que o enunciado garante
        printf("Dados inválidos\n");                    // avisa
        return 1;                                       // fim com erro
    }
    int antes = d / p;                                  // índice do ponto anterior à escola (0 = primeiro)
    int resto = d % p;                                  // metros entre esse ponto e a escola
    if (resto * 2 <= p) {                               // a escola está mais perto do ponto anterior
        printf("Descer no ponto %d e andar %d metros em direção ao Fim da Avenida\n", antes + 1, resto); // mais perto do ponto anterior: anda para a frente
    } else {                                            // mais perto do ponto seguinte
        printf("Descer no ponto %d e andar %d metros em direção ao Início da Avenida\n", antes + 2, p - resto); // mais perto do próximo ponto: anda de volta
    }
    return 0;                                           // fim sem erro
}
