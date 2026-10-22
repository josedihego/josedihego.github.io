// Aula 8 – Nível 2: Contador binário
// Conta de 0 a 15 em binário, um número por segundo
#include <Arduino.h>                                  // funções do Arduino (pinMode, digitalWrite, delay...)
int numero = 0;                                       // contador

void setup() {                                        // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 5; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 5 como saída
  Serial.begin(9600);                                 // abre o Monitor Serial a 9600 baud
}

void loop() {                                         // repete para sempre
  for (int bit = 0; bit < 4; bit++) {                 // percorre os 4 bits
    digitalWrite(2 + bit, bitRead(numero, bit));      // bit 0 no pino 2, bit 3 no pino 5
  }
  Serial.println(numero);                             // envia numero ao Monitor Serial e quebra a linha
  numero = (numero + 1) % 16;                         // depois de 15 volta para 0
  delay(1000);                                        // espera 1000 ms
}
