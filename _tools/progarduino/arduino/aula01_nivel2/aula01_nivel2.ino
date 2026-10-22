// Aula 1 – Nível 2: LED externo com tempos diferentes
// pecas: led 8 vermelho
// LED no pino 8 (com resistor de 220 ohms): aceso 1 s, apagado 0,2 s
#include <Arduino.h>                  // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINO_LED = 8;               // número do pino num nome fácil de ler

void setup() {                        // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);          // pino como saída
}

void loop() {                         // repete para sempre
  digitalWrite(PINO_LED, HIGH);       // acende
  delay(1000);                        // 1 segundo aceso
  digitalWrite(PINO_LED, LOW);        // apaga
  delay(200);                         // 0,2 segundo apagado
}
