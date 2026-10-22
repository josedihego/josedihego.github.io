// Aula 5 – Nível 2: Porta E com dois botões
// pecas: botao 2; botao 3; led 8 vermelho
// O LED só acende com os DOIS botões apertados (E lógico)
#include <Arduino.h>                              // funções do Arduino (pinMode, digitalWrite, delay...)
const int BOTAO_A = 2, BOTAO_B = 3, PINO_LED = 8;   // pinos dos dois botões e do LED

void setup() {                                    // roda uma vez, quando a placa liga
  pinMode(BOTAO_A, INPUT_PULLUP);                 // botões com pull-up interno
  pinMode(BOTAO_B, INPUT_PULLUP);                 // BOTAO_B como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);                      // PINO_LED como saída
}

void loop() {                                     // repete para sempre
  bool a = digitalRead(BOTAO_A) == LOW;           // apertado = LOW, por isso o == LOW
  bool b = digitalRead(BOTAO_B) == LOW;           // true quando o botão B está apertado
  digitalWrite(PINO_LED, a && b);                 // && = E: true (1) acende
}
