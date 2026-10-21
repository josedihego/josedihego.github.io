// Aula 29 – Nível 2: Média e maior em funções
// teste: 
#include <stdio.h>                                        // printf

float media(float v[], int n) {                           // média de um vetor de n floats
    float s = 0;                                          // acumulador
    for (int i = 0; i < n; i++) s += v[i];                // soma todos
    return s / n;                                         // devolve a média
}

float maior(float v[], int n) {                           // maior elemento de um vetor
    float m = v[0];                                       // começa supondo que o primeiro é o maior
    for (int i = 1; i < n; i++) if (v[i] > m) m = v[i];   // troca quando achar um maior
    return m;                                             // devolve o maior
}

int main(void) {                                          // início do programa
    float tensoes[] = {4.98, 5.02, 4.91, 5.10, 4.95};     // medições de exemplo (V)
    int n = 5;                                            // quantidade de medições
    printf("Média: %.3f V | Maior: %.2f V\n", media(tensoes, n), maior(tensoes, n));   // mostra os valores formatados
    return 0;                                             // termina com sucesso
}
