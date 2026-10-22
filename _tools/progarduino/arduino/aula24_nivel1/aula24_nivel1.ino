// Aula 24 – Nível 1: Revisão: pisca com millis e potenciômetro
// pecas: pot A0; led 8 vermelho
// Revisão: período de 100 a 1000 ms escolhido no potenciômetro, sem delay
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 8                      // LED no pino 8
unsigned long anterior = 0;             // instante da última troca
bool aceso = false;                     // estado do LED

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);            // PINO_LED como saída
}

void loop() {                           // repete para sempre
  unsigned long periodo = map(analogRead(A0), 0, 1023, 100, 1000);   // potenciômetro escolhe 100 a 1000 ms
  if (millis() - anterior >= periodo) {   // passou o período?
    anterior = millis();                // marca o instante da última troca
    aceso = !aceso;                     // inverte o estado
    digitalWrite(PINO_LED, aceso);      // PINO_LED recebe aceso (verdadeiro acende, falso apaga)
  }
}
