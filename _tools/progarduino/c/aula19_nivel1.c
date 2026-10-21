// Aula 19 – Nível 1: Que horas são?
// teste: 
#include <stdio.h>                                          // printf
#include <time.h>                                           // time, localtime e strftime

int main(void) {                                            // início do programa
    time_t agora = time(NULL);                              // segundos desde 01/01/1970
    struct tm *local = localtime(&agora);                   // converte para data e hora
    char texto[40];                                         // declara texto[40] (char)
    strftime(texto, sizeof texto, "%d/%m/%Y %H:%M:%S", local);   // formata
    printf("Agora: %s\n", texto);                           // mostra texto formatados
    printf("Segundos desde 1970: %ld\n", (long)agora);      // mostra (long)agora formatados
    return 0;                                               // termina com sucesso
}
