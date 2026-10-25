// A4-2026.1 – Questão I: Porcentagem de palavras que contêm uma letra
// teste: s;Ser ou nao ser eis a questao => 4/7 = 0.57
// teste: z;abc def => 0/2 = 0.00
#include <stdio.h>                                      // printf e fgets

int minuscula(char c) {                                 // 'A'..'Z' vira 'a'..'z'; o resto fica igual
    if (c >= 'A' && c <= 'Z') return c - 'A' + 'a';     // na tabela ASCII, as letras são consecutivas
    return c;                                           // já é minúscula (ou não é letra)
}

int e_letra(char c) {                                   // 1 se c for uma letra sem acento
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');   // letras são consecutivas na tabela ASCII
}

int main(void) {                                        // início do programa
    char letra;                                         // letra procurada
    char texto[257];                                    // até 256 caracteres
    printf("Letra: ");                                  // pede a letra
    scanf(" %c", &letra);                               // o espaço antes de %c pula espaços e Enters
    getchar();                                          // consome o Enter que sobrou
    printf("Texto: ");                                  // pede o texto
    fgets(texto, sizeof texto, stdin);                  // lê a linha inteira
    letra = minuscula(letra);              // compara sem diferenciar maiúsculas
    int palavras = 0, com_letra = 0;                    // contadores
    int dentro = 0, achou = 0;                          // estou dentro de uma palavra? ela já tem a letra?
    for (int i = 0; ; i++) {                            // percorre até o '\0' (tratado no fim)
        if (e_letra(texto[i])) {         // letra: faz parte de uma palavra
            if (!dentro) { dentro = 1; achou = 0; }     // começou uma palavra nova
            if (minuscula(texto[i]) == letra) achou = 1;   // a palavra contém a letra
        } else {                                        // espaço, Enter ou fim: termina a palavra
            if (dentro) {                               // havia uma palavra aberta
                palavras++;                             // conta a palavra
                if (achou) com_letra++;                 // e se ela tinha a letra
                dentro = 0;                             // fecha a palavra
            }
            if (texto[i] == '\0') break;                // fim do texto
        }
    }
    printf("%d/%d = %.2f\n", com_letra, palavras, palavras ? (double)com_letra / palavras : 0.0); // proporção (evita divisão por zero)
    return 0;                                           // fim sem erro
}
