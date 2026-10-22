// Aula 10 – Nível 1: Um bip com o buzzer
// pecas: buzzer 8
// tone(pino, frequência, duração) toca uma nota no buzzer
#include <Arduino.h>                   // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BUZZER 8                  // buzzer no pino 8

void setup() {                         // roda uma vez, quando a placa liga
  tone(PINO_BUZZER, 440, 500);         // lá (440 Hz) por meio segundo
}

void loop() {                          // repete para sempre
}
