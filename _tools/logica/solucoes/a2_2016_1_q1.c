// A2-2016.1 – Questão I: Em quantos anos Zé fica maior que Chico?
// teste:  => 41 anos
#include <stdio.h>                                      // printf

int main(void) {                                        // início do programa
    int chico = 150, ze = 110;                          // alturas em centímetros (inteiros evitam erro de arredondamento)
    int anos = 0;                                       // contador de anos
    while (ze <= chico) {                               // repete ENQUANTO Zé ainda não passou Chico
        chico += 2;                                     // Chico cresce 2 cm por ano
        ze += 3;                                        // Zé cresce 3 cm por ano
        anos++;                                         // passou mais um ano
    }
    printf("Zé fica maior que Chico em %d anos (%d cm x %d cm)\n", anos, ze, chico);   // resultado
    return 0;                                           // fim sem erro
}
