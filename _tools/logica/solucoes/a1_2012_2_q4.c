// A1-2012.2 – Questão IV: Data por extenso
// teste: 2 6 => dois de junho
// teste: 1 12 => primeiro de dezembro
// teste: 23 9 => vinte e três de setembro
// teste: 16 3 => dezesseis de março
// teste: 30 4 => trinta de abril
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int dia, mes;                                       // data lida
    printf("Dia e mês: ");                              // pede a data
    scanf("%d %d", &dia, &mes);                         // lê os dois inteiros
    if (dia < 1 || dia > 31 || mes < 1 || mes > 12) {   // validação básica
        printf("Data inválida\n");                      // avisa
        return 1;                                       // fim com erro
    }
    if (dia == 1) printf("primeiro");                   // o dia 1 tem nome próprio
    else if (dia >= 10 && dia <= 19) {                  // 10 a 19: nomes especiais
        switch (dia) {                                  // escolhe pelo valor exato
            case 10: printf("dez"); break;              // cada caso imprime e sai do switch
            case 11: printf("onze"); break;
            case 12: printf("doze"); break;
            case 13: printf("treze"); break;
            case 14: printf("quatorze"); break;
            case 15: printf("quinze"); break;
            case 16: printf("dezesseis"); break;
            case 17: printf("dezessete"); break;
            case 18: printf("dezoito"); break;
            default: printf("dezenove"); break;         // sobrou o 19
        }
    } else {                                            // demais: dezena + "e" + unidade
        if (dia / 10 == 2) printf("vinte");             // 20 a 29
        if (dia / 10 == 3) printf("trinta");            // 30 e 31
        if (dia >= 20 && dia % 10 != 0) printf(" e ");  // 21, 22...: "vinte e ..."
        switch (dia % 10) {                             // a unidade
            case 1: printf("um"); break;
            case 2: printf("dois"); break;
            case 3: printf("três"); break;
            case 4: printf("quatro"); break;
            case 5: printf("cinco"); break;
            case 6: printf("seis"); break;
            case 7: printf("sete"); break;
            case 8: printf("oito"); break;
            case 9: printf("nove"); break;
        }                                               // unidade 0 (20, 30): nada a imprimir
    }
    printf(" de ");                                     // ligação entre dia e mês
    switch (mes) {                                      // nome do mês
        case 1: printf("janeiro"); break;
        case 2: printf("fevereiro"); break;
        case 3: printf("março"); break;
        case 4: printf("abril"); break;
        case 5: printf("maio"); break;
        case 6: printf("junho"); break;
        case 7: printf("julho"); break;
        case 8: printf("agosto"); break;
        case 9: printf("setembro"); break;
        case 10: printf("outubro"); break;
        case 11: printf("novembro"); break;
        default: printf("dezembro"); break;             // sobrou o 12
    }
    printf("\n");                                       // termina a linha
    return 0;                                           // fim sem erro
}
