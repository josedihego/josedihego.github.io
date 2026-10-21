// Aula 10 – Nível 3: LED: qual resistor usar?
// teste: 5; 2; 20
#include <stdio.h>                                                  // printf e scanf

int main(void) {                                                    // início do programa
    float fonte, v_led, i_ma;                                       // tensões e corrente do LED
    printf("Fonte (V), tensão do LED (V) e corrente (mA): ");       // pergunta ao usuário
    scanf("%f %f %f", &fonte, &v_led, &i_ma);                       // lê o valor digitado e guarda em fonte, v_led, i_ma
    if (fonte <= v_led || i_ma <= 0) {                              // valida
        printf("Valores impossíveis\n");                            // mostra "Valores impossíveis"
        return 1;                                                   // termina com código de erro
    }
    float r = (fonte - v_led) / (i_ma / 1000);                      // R = (Vfonte - Vled) / I
    int comercial;                                                  // valor comercial maior ou igual
    if (r <= 100) comercial = 100;                                  // escolhe o primeiro valor comercial maior ou igual
    else if (r <= 150) comercial = 150;                             // próximo valor da série
    else if (r <= 220) comercial = 220;                             // próximo valor da série
    else if (r <= 330) comercial = 330;                             // próximo valor da série
    else if (r <= 470) comercial = 470;                             // próximo valor da série
    else comercial = 1000;                                          // acima de 470: usa 1 kohm
    printf("Calculado: %.1f ohms -> use %d ohms\n", r, comercial);   // mostra r e comercial formatados
    return 0;                                                       // termina com sucesso
}
