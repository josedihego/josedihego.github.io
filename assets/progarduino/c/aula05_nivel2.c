// Aula 5 – Nível 2: Tabela-verdade de E e OU
#include <stdio.h>                                          // printf

int main(void) {                                            // início do programa
    printf(" A B | A&&B A||B !A\n");                        // cabeçalho
    printf(" 0 0 |  %d    %d    %d\n", 0 && 0, 0 || 0, !0);  // && é E, || é OU, ! é NÃO
    printf(" 0 1 |  %d    %d    %d\n", 0 && 1, 0 || 1, !0);   // mostra 0 && 1 e 0 || 1 e !0 formatados
    printf(" 1 0 |  %d    %d    %d\n", 1 && 0, 1 || 0, !1);   // mostra 1 && 0 e 1 || 0 e !1 formatados
    printf(" 1 1 |  %d    %d    %d\n", 1 && 1, 1 || 1, !1);   // mostra 1 && 1 e 1 || 1 e !1 formatados
    return 0;                                               // termina com sucesso
}
