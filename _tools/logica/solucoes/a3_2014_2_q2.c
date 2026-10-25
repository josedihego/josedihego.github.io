// A3-2014.2 – Questão II: Encontros consonantais numa frase
// teste: O istmo de Stradun não fica no Brasil => 3
// teste: Atrasada pela chuva no trecho => 4
// teste: aeiou => 0
#include <stdio.h>                                      // printf e fgets

int minuscula(char c) {                                 // 'A'..'Z' vira 'a'..'z'; o resto fica igual
    if (c >= 'A' && c <= 'Z') return c - 'A' + 'a';     // na tabela ASCII, as letras são consecutivas
    return c;                                           // já é minúscula (ou não é letra)
}

int e_letra(char c) {                                   // 1 se c for uma letra sem acento
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');   // letras são consecutivas na tabela ASCII
}

int consoante(char c) {                                 // 1 se c for uma letra sem acento que não é vogal
    char m = minuscula(c);                              // compara sem diferenciar maiúsculas
    return e_letra(c) && m != 'a' && m != 'e' && m != 'i' && m != 'o' && m != 'u';// letra que não é vogal
}

int main(void) {                                        // início do programa
    char s[257];                                        // até 256 caracteres + '\0'
    printf("Frase: ");                                  // pede a frase
    fgets(s, sizeof s, stdin);                          // lê a linha inteira (com espaços)
    int encontros = 0, seguidas = 0;                    // total de encontros e consoantes seguidas agora
    for (int i = 0; s[i] != '\0'; i++) {                // percorre a frase
        if (consoante(s[i])) {                          // mais uma consoante no grupo atual
            seguidas++;                                 // conta
            if (seguidas == 2) encontros++;             // a 2ª consoante seguida forma um encontro (conta uma vez)
        } else {                                        // vogal, espaço, acento ou pontuação
            seguidas = 0;                               // quebra o grupo
        }
    }
    printf("%d encontros consonantais\n", encontros);   // istmo (stm), Stradun (Str), Brasil (Br)
    return 0;                                           // fim sem erro
}
