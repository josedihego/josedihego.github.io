// Aula 11 – Nível 1: Simulado: pisca com dois tempos
// Simulado: LED aceso 300 ms e apagado 700 ms
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 8                      // LED no pino 8

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);            // PINO_LED como saída
}

void loop() {                           // repete para sempre
  digitalWrite(PINO_LED, HIGH);         // acende/liga PINO_LED
  delay(300);                           // espera 300 ms
  digitalWrite(PINO_LED, LOW);          // apaga/desliga PINO_LED
  delay(700);                           // espera 700 ms
}
