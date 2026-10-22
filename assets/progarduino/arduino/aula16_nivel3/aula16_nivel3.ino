// Aula 16 – Nível 3: Contador em binário com reset
// Cada toque soma 1 (0 a 15 em binário nos LEDs); segurar 1 s zera
#include <Arduino.h>                               // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_BOTAO 2                               // botão no pino 2
int contagem = 0;                                  // valor mostrado em binário

void mostrar() {                                   // contagem em binário nos pinos 4 a 7
  for (int bit = 0; bit < 4; bit++) digitalWrite(4 + bit, bitRead(contagem, bit));   // bit 0 no pino 4, bit 3 no pino 7
}

void setup() {                                     // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);               // PINO_BOTAO como entrada com pull-up interno
  for (int pino = 4; pino <= 7; pino++) pinMode(pino, OUTPUT);   // pinos 4 a 7 como saída
  mostrar();                                       // atualiza a exibição
}

void loop() {                                      // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {            // botão apertado?
    unsigned long inicio = millis();               // marca o instante inicial
    delay(30);                                     // debounce simples
    while (digitalRead(PINO_BOTAO) == LOW) {       // espera soltar
    }
    if (millis() - inicio > 1000) contagem = 0;    // toque longo: zera
    else contagem = (contagem + 1) % 16;           // toque curto: soma
    mostrar();                                     // atualiza a exibição
  }
}
