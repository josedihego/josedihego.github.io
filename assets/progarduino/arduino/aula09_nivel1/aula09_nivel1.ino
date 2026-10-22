// Aula 9 – Nível 1: Brilho fixo com PWM
// analogWrite gera PWM: 0 (apagado) a 255 (brilho máximo). Use um pino com ~ (3, 5, 6, 9, 10, 11)
#include <Arduino.h>                   // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 9                     // #define também cria constantes
#define BRILHO 40                      // cerca de 16% do tempo ligado

void setup() {                         // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);           // PINO_LED como saída
  analogWrite(PINO_LED, BRILHO);       // brilho fraco
}

void loop() {                          // repete para sempre
}
