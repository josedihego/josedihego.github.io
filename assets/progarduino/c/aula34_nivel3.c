// Aula 34 – Nível 3: Salvar o registro em CSV
#include <stdio.h>                                                   // printf, scanf, fopen, fprintf

int main(void) {                                                     // início do programa
    int n;                                                           // declara n (int)
    printf("Quantas medições? ");                                    // pergunta ao usuário
    scanf("%d", &n);                                                 // lê o valor digitado e guarda em n
    FILE *arquivo = fopen("medicoes.csv", "w");                      // "w": cria (ou apaga) para escrever
    if (arquivo == NULL) { printf("Não consegui criar o arquivo\n"); return 1; }   // fopen falhou
    fprintf(arquivo, "hora,tensao\n");                               // cabeçalho do CSV
    for (int i = 0; i < n; i++) {                                    // percorre os n elementos (i de 0 a n-1)
        char hora[6];                                                // declara hora[6] (char)
        float v;                                                     // declara v (float)
        scanf("%5s %f", hora, &v);                                   // lê o valor digitado e guarda em hora, v
        fprintf(arquivo, "%s,%.2f\n", hora, v);                      // fprintf escreve no arquivo
    }
    fclose(arquivo);                                                 // fecha e grava no disco
    printf("Salvo em medicoes.csv (abra no Google Planilhas)\n");    // mostra "Salvo em medicoes.csv (abra no Google Planilhas)"
    return 0;                                                        // termina com sucesso
}
