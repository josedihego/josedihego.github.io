// A1-2015.2 (B) – Questão III: Número de lâmpadas de 60 W para um cômodo
// teste: 1 3 4 => 3 lâmpada
// teste: 3 2 3 => 2 lâmpada
// teste: 2 5 4 => 5 lâmpada
#include <stdio.h>                                      // printf e scanf
#include <math.h>                                       // ceil (compile com -lm)

int main(void) {                                        // início do programa
    int classe;                                         // 1 (I), 2 (II) ou 3 (III)
    double largura, comprimento;                        // dimensões do cômodo em metros
    printf("Classe (1, 2 ou 3), largura e comprimento: ");   // pede os dados
    scanf("%d %lf %lf", &classe, &largura, &comprimento);    // lê os três valores
    int watts_m2;                                       // potência mínima por m² da classe
    if (classe == 1) watts_m2 = 12;                     // quarto, sala de TV
    else if (classe == 2) watts_m2 = 15;                // sala, cozinha, varanda
    else if (classe == 3) watts_m2 = 20;                // banheiro, escritório
    else { printf("Classe inválida\n"); return 1; }     // qualquer outro valor é erro
    double potencia = largura * comprimento * watts_m2; // potência total exigida
    int lampadas = (int)ceil(potencia / 60);            // ceil arredonda para cima: 2,4 lâmpadas viram 3
    printf("%d lâmpada(s) de 60 W\n", lampadas);        // resultado
    return 0;                                           // fim sem erro
}
