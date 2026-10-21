// Aula 7 – Nível 3: Valor do resistor pelas faixas
// teste: 4; 7; 2
#include <stdio.h>                                                  // printf e scanf

int main(void) {                                                    // início do programa
    int f1, f2, mult;                                               // 1ª, 2ª faixa e multiplicador (0 a 9)
    printf("Faixas (0=preto 1=marrom 2=vermelho ... 9=branco): ");   // pergunta ao usuário
    scanf("%d %d %d", &f1, &f2, &mult);                             // lê o valor digitado e guarda em f1, f2, mult
    if (f1 < 0 || f1 > 9 || f2 < 0 || f2 > 9 || mult < 0 || mult > 6) {   // valida as entradas
        printf("Faixa inválida\n");                                 // mostra "Faixa inválida"
        return 1;                                                   // termina com código de erro
    }
    long valor = (f1 * 10 + f2);                                    // dois primeiros dígitos
    for (int i = 0; i < mult; i++) valor = valor * 10;              // multiplica por 10 'mult' vezes
    if (valor >= 1000000) printf("%.1f Mohms\n", valor / 1000000.0);   // escolhe a unidade
    else if (valor >= 1000) printf("%.1f kohms\n", valor / 1000.0);   // milhares: mostra em kohms
    else printf("%ld ohms\n", valor);                               // valores pequenos: em ohms
    return 0;                                                       // termina com sucesso
}
