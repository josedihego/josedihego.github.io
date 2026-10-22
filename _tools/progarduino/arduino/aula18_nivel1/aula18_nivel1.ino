// Aula 18 – Nível 1: Padrão com laços aninhados
// pecas: led 8 vermelho
// 3 séries de 2 piscadas rápidas, separadas por uma pausa
#include <Arduino.h>                               // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 8                                 // LED no pino 8

void setup() {                                     // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                       // PINO_LED como saída
}

void loop() {                                      // repete para sempre
  for (int serie = 0; serie < 3; serie++) {        // laço de fora: séries
    for (int p = 0; p < 2; p++) {                  // laço de dentro: piscadas
      digitalWrite(PINO_LED, HIGH); delay(100);    // acende/liga PINO_LED e espera 100 ms
      digitalWrite(PINO_LED, LOW);  delay(100);    // apaga/desliga PINO_LED e espera 100 ms
    }
    delay(600);                                    // pausa entre séries
  }
  delay(2000);                                     // pausa maior antes de repetir
}
