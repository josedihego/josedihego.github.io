// Aula 9 – Nível 2: Dimmer com potenciômetro
// O potenciômetro controla o brilho do LED
#include <Arduino.h>                             // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 9                               // LED no pino 9

void setup() {                                   // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                     // PINO_LED como saída
}

void loop() {                                    // repete para sempre
  int leitura = analogRead(A0);                  // 0 a 1023
  int brilho = map(leitura, 0, 1023, 0, 255);    // converte para 0 a 255
  analogWrite(PINO_LED, brilho);                 // PWM: brilho de 0 a 255
}
