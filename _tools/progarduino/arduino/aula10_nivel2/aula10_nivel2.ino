// Aula 10 – Nível 2: Alarme com botão
// pecas: botao 2; buzzer 8; led 9 vermelho
// Botão apertado: LED vermelho e sirene de duas notas
#include <Arduino.h>                        // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                        // botão no pino 2
#define PINO_BUZZER 8                       // buzzer no pino 8
#define PINO_LED 9                          // LED no pino 9

void setup() {                              // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);        // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);                // PINO_LED como saída
}

void loop() {                               // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {     // alarme disparado
    digitalWrite(PINO_LED, HIGH);           // acende/liga PINO_LED
    tone(PINO_BUZZER, 880, 200);            // nota aguda
    delay(250);                             // espera 250 ms
    tone(PINO_BUZZER, 660, 200);            // nota grave
    delay(250);                             // espera 250 ms
  } else {
    digitalWrite(PINO_LED, LOW);            // apaga/desliga PINO_LED
    noTone(PINO_BUZZER);                    // silêncio
  }
}
