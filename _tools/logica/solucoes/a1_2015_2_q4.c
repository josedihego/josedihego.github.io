// A1-2015.2 – Questão IV: Quem é mais velho? (anos, meses e dias)
// teste: 8 4 2 8 3 15 => A primeira pessoa é mais velha
// teste: 8 3 15 8 4 2 => A segunda pessoa é mais velha
// teste: 5 1 1 5 1 1 => mesma idade
#include <stdio.h>                                      // printf e scanf

int main(void) {                                        // início do programa
    int a1, m1, d1, a2, m2, d2;                         // idade de cada pessoa: anos, meses, dias
    printf("Idade da 1ª pessoa (anos meses dias): ");   // pede a primeira idade
    scanf("%d %d %d", &a1, &m1, &d1);                   // lê os três valores
    printf("Idade da 2ª pessoa (anos meses dias): ");   // pede a segunda idade
    scanf("%d %d %d", &a2, &m2, &d2);                   // lê os três valores
    int dif = a1 - a2;                                  // compara primeiro os anos
    if (dif == 0) dif = m1 - m2;                        // anos iguais: desempata pelos meses
    if (dif == 0) dif = d1 - d2;                        // meses iguais: desempata pelos dias
    if (dif > 0) printf("A primeira pessoa é mais velha\n");     // mais tempo de vida = mais velha
    else if (dif < 0) printf("A segunda pessoa é mais velha\n"); // idem para a segunda
    else printf("As duas pessoas têm a mesma idade\n"); // tudo igual
    return 0;                                           // fim sem erro
}
