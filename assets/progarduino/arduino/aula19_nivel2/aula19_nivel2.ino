// Aula 19 – Nível 2: Dois LEDs, dois ritmos
// Vermelho troca a cada 300 ms e verde a cada 1100 ms, ao mesmo tempo
#include <Arduino.h>                   // funções do Arduino (pinMode, digitalWrite, delay...)
#define LED_A 8                        // primeiro LED no pino 8
#define LED_B 9                        // segundo LED no pino 9
unsigned long ultimoA = 0, ultimoB = 0;   // última troca de cada LED
bool estadoA = false, estadoB = false;   // estado de cada LED

void setup() {                         // roda uma vez, quando a placa liga
  pinMode(LED_A, OUTPUT);              // LED_A como saída
  pinMode(LED_B, OUTPUT);              // LED_B como saída
}

void loop() {                          // repete para sempre
  unsigned long agora = millis();      // lê o relógio uma vez por volta
  if (agora - ultimoA >= 300) {        // relógio do LED A
    ultimoA = agora;                   // reinicia o relógio do LED A
    estadoA = !estadoA;                // inverte o LED A
    digitalWrite(LED_A, estadoA);      // LED_A recebe estadoA (verdadeiro acende, falso apaga)
  }
  if (agora - ultimoB >= 1100) {       // relógio do LED B
    ultimoB = agora;                   // reinicia o relógio do LED B
    estadoB = !estadoB;                // inverte o LED B
    digitalWrite(LED_B, estadoB);      // LED_B recebe estadoB (verdadeiro acende, falso apaga)
  }
}
