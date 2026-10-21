// Aula 36 – Nível 3: Revisão: malloc e ordenação
// teste: 5; 9; 1; 6; 3; 7
#include <stdio.h>                                       // printf e scanf
#include <stdlib.h>                                      // malloc, free, qsort

int compara(const void *a, const void *b) {              // usada pelo qsort da biblioteca
    return *(const int *)a - *(const int *)b;            // negativo: a vem antes; positivo: b vem antes
}

int main(void) {                                         // início do programa
    int n;                                               // declara n (int)
    printf("Quantos números? ");                         // pergunta ao usuário
    scanf("%d", &n);                                     // lê o valor digitado e guarda em n
    int *v = malloc(n * sizeof(int));                    // vetor de n inteiros alocado em tempo de execução
    for (int i = 0; i < n; i++) scanf("%d", &v[i]);      // lê os n números
    qsort(v, n, sizeof(int), compara);                   // ordenação pronta da biblioteca padrão
    for (int i = 0; i < n; i++) printf("%d ", v[i]);     // mostra o vetor
    printf("\n");                                        // quebra a linha
    free(v);                                             // devolve a memória
    return 0;                                            // termina com sucesso
}
