// Aula 19 – Nível 1: Piscar sem delay
// millis() no lugar de delay(): o loop nunca fica parado
#include <Arduino.h>                 // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 8                   // LED no pino 8
unsigned long anterior = 0;          // última troca
bool aceso = false;                  // estado do LED

void setup() {                       // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);         // PINO_LED como saída
}

void loop() {                        // repete para sempre
  if (millis() - anterior >= 500) {  // passaram 500 ms?
    anterior = millis();             // marca o instante da última troca
    aceso = !aceso;                  // inverte
    digitalWrite(PINO_LED, aceso);   // PINO_LED recebe aceso (verdadeiro acende, falso apaga)
  }
  // aqui o programa pode fazer outras coisas ao mesmo tempo
}
