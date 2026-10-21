// Aula 19 – Nível 2: Contagem regressiva com sleep
// teste: 
#include <stdio.h>                                 // printf e fflush
#include <unistd.h>                                // sleep (Linux)

int main(void) {                                   // início do programa
    for (int s = 5; s > 0; s--) {                  // de 5 até 1
        printf("%d...\n", s);                      // mostra s formatados
        fflush(stdout);                            // mostra já, sem esperar o buffer
        sleep(1);                                  // pausa de 1 segundo
    }
    printf("Lançar!\n");                           // mostra "Lançar!"
    return 0;                                      // termina com sucesso
}
