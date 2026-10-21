// Aula 35 – Nível 3: Simulado: struct e ponteiro
#include <stdio.h>                                      // printf

typedef struct { int pino; int estado; } Led;           // um LED: pino e estado

void inverter(Led *l) {                                 // ponteiro para struct: -> acessa o campo
    l->estado = !l->estado;                             // inverte o estado no struct original
}

int main(void) {                                        // início do programa
    Led verde = {8, 0};                                 // pino 8, apagado
    inverter(&verde);                                   // passa o endereço do struct
    printf("LED do pino %d: %s\n", verde.pino, verde.estado ? "aceso" : "apagado");   // mostra os valores formatados
    return 0;                                           // termina com sucesso
}
