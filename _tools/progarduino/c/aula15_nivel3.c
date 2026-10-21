// Aula 15 – Nível 3: Menu com do-while e validação
// teste: 3; 1; 2; 0
#include <stdio.h>                                              // printf e scanf

int main(void) {                                                // início do programa
    int opcao;                                                  // escolha do menu
    do {                                                        // do-while: executa pelo menos uma vez
        printf("1-Ohm  2-Potência  0-Sair: ");                  // pergunta ao usuário
        scanf("%d", &opcao);                                    // lê o valor digitado e guarda em opcao
        if (opcao == 1) printf("V = R x I\n");                  // opção 1
        else if (opcao == 2) printf("P = V x I\n");             // opção 2
        else if (opcao != 0) printf("Opção inválida\n");        // valida a entrada
    } while (opcao != 0);                                       // o teste fica no fim
    printf("Até logo!\n");                                      // mostra "Até logo!"
    return 0;                                                   // termina com sucesso
}
