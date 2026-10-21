// Aula 24 – Nível 3: Revisão: tabela de eco
// teste: 
#include <stdio.h>                                         // printf

int main(void) {                                           // início do programa
    printf("Eco (us) | Distância (cm)\n");                 // mostra "Eco (us) | Distância (cm)"
    for (int eco = 500; eco <= 3000; eco += 500) {         // ecos de 500 a 3000 µs, de 500 em 500
        printf("%8d | %14.1f\n", eco, eco * 0.0343 / 2);   // mostra eco e eco * 0.0343 / 2 formatados
    }
    return 0;                                              // termina com sucesso
}
