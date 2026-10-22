// Aula 5 – Nível 3: Portas OU e OU exclusivo
// LED vermelho = A OU B; LED verde = A XOR B (um ou outro, não os dois)
#include <Arduino.h>                              // funções do Arduino (pinMode, digitalWrite, delay...)
const int BOTAO_A = 2, BOTAO_B = 3, LED_OU = 8, LED_XOR = 9;   // pinos dos botões e dos LEDs

void setup() {                                    // roda uma vez, quando a placa liga
  pinMode(BOTAO_A, INPUT_PULLUP);                 // BOTAO_A como entrada com pull-up interno
  pinMode(BOTAO_B, INPUT_PULLUP);                 // BOTAO_B como entrada com pull-up interno
  pinMode(LED_OU, OUTPUT);                        // LED_OU como saída
  pinMode(LED_XOR, OUTPUT);                       // LED_XOR como saída
}

void loop() {                                     // repete para sempre
  bool a = digitalRead(BOTAO_A) == LOW;           // true quando apertado
  bool b = digitalRead(BOTAO_B) == LOW;           // true quando o botão B está apertado
  digitalWrite(LED_OU, a || b);                   // || = OU
  digitalWrite(LED_XOR, a != b);                  // diferentes = OU exclusivo
}
