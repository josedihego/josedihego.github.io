// Aula 1 – Nível 2: Várias linhas, \n e \t
#include <stdio.h>                       // printf

int main(void) {                         // início do programa
    printf("Curso:\tEletrônica\n");      // \t insere uma tabulação
    printf("Turma:\t2º ano\n");          // cada \n começa uma linha nova
    printf("Disciplina:\tC e Arduino\n");   // mostra "Disciplina:\tC e Arduino"
    printf("\n");                        // linha em branco
    printf("Fim do programa.\n");        // última linha
    return 0;                            // sucesso
}
