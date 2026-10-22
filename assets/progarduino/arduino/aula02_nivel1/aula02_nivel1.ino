// Aula 2 – Nível 1: Variáveis no Monitor Serial
// Mostra variáveis no Monitor Serial (9600 baud)
#include <Arduino.h>                  // funções do Arduino (pinMode, digitalWrite, delay...)
int quantidade = 12;                  // inteiro
float tensao = 4.75;                  // decimal
char letra = 'A';                     // caractere

void setup() {                        // roda uma vez, quando a placa liga
  Serial.begin(9600);                 // abre a comunicação serial com o computador
  Serial.print("Quantidade: ");       // print escreve sem quebrar a linha
  Serial.println(quantidade);         // println escreve e quebra a linha
  Serial.print("Tensão: ");           // envia o texto ao Monitor Serial
  Serial.println(tensao, 2);          // 2 casas decimais
  Serial.print("Letra: ");            // envia o texto ao Monitor Serial
  Serial.println(letra);              // envia letra ao Monitor Serial e quebra a linha
}

void loop() {                         // nada para repetir
}
