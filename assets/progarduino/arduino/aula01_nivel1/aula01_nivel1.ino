// Aula 1 – Nível 1: Pisca o LED da placa
// O LED da própria placa (pino 13) acende e apaga a cada meio segundo
#include <Arduino.h>                  // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                        // setup roda uma vez, quando a placa liga
  pinMode(LED_BUILTIN, OUTPUT);       // o pino do LED interno vira saída
}

void loop() {                         // loop repete para sempre
  digitalWrite(LED_BUILTIN, HIGH);    // HIGH = 5 V: acende
  delay(500);                         // espera 500 ms
  digitalWrite(LED_BUILTIN, LOW);     // LOW = 0 V: apaga
  delay(500);                         // espera 500 ms
}
