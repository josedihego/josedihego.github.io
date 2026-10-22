// Aula 12 – Nível 2: Revisão: liga e desliga com um toque
// pecas: botao 2; led 8 vermelho
// Revisão: cada toque no botão inverte o LED (com espera para o botão ser solto)
#include <Arduino.h>                             // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                             // botão no pino 2
#define PINO_LED 8                               // LED no pino 8
bool aceso = false;                              // estado do LED

void setup() {                                   // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);             // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);                     // PINO_LED como saída
}

void loop() {                                    // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {          // apertou
    aceso = !aceso;                              // inverte o estado
    digitalWrite(PINO_LED, aceso);               // PINO_LED recebe aceso (verdadeiro acende, falso apaga)
    delay(50);                                   // ignora o ruído do contato
    while (digitalRead(PINO_BOTAO) == LOW) {     // espera soltar
    }
  }
}
