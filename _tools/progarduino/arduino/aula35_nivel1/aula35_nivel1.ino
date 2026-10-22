// Aula 35 – Nível 1: Simulado: vetor de pinos
// pecas: led 2 vermelho; led 3 amarelo; led 4 verde
// Simulado: acende os LEDs do vetor do último para o primeiro
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINOS[] = {2, 3, 4};          // pinos dos LEDs

void setup() {                          // roda uma vez, quando a placa liga
  for (int i = 0; i < 3; i++) pinMode(PINOS[i], OUTPUT);   // configura os 3 pinos
}

void loop() {                           // repete para sempre
  for (int i = 2; i >= 0; i--) {        // do último para o primeiro
    digitalWrite(PINOS[i], HIGH); delay(300);   // acende/liga PINOS[i] e espera 300 ms
    digitalWrite(PINOS[i], LOW);        // apaga/desliga PINOS[i]
  }
}
