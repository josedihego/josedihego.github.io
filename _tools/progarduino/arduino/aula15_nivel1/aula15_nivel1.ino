// Aula 15 – Nível 1: Enquanto o botão estiver apertado
// pecas: botao 2; led 8 vermelho
// O while prende o programa enquanto o botão está apertado
#include <Arduino.h>                          // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                          // botão no pino 2
#define PINO_LED 8                            // LED no pino 8

void setup() {                                // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);          // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);                  // PINO_LED como saída
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
}

void loop() {                                 // repete para sempre
  while (digitalRead(PINO_BOTAO) == LOW) {    // repete enquanto apertado
    digitalWrite(PINO_LED, HIGH);             // acende/liga PINO_LED
  }
  digitalWrite(PINO_LED, LOW);                // soltou: sai do while
}
