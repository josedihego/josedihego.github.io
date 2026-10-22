// Aula 1 – Nível 3: SOS em código Morse
// pecas: led 8 vermelho
// Pisca S-O-S (· · ·  — — —  · · ·) no LED do pino 8
#include <Arduino.h>                  // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINO_LED = 8;               // LED com resistor
const int PONTO = 200;                // duração do ponto (ms)
const int TRACO = 600;                // traço = 3 pontos

void setup() {                        // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);          // pino como saída
}

void sinal(int duracao) {             // acende o LED pelo tempo pedido e faz uma pausa curta
  digitalWrite(PINO_LED, HIGH);       // acende
  delay(duracao);                     // ponto ou traço
  digitalWrite(PINO_LED, LOW);        // apaga
  delay(PONTO);                       // pausa entre sinais
}

void loop() {                         // repete para sempre
  sinal(PONTO); sinal(PONTO); sinal(PONTO);   // S
  sinal(TRACO); sinal(TRACO); sinal(TRACO);   // O
  sinal(PONTO); sinal(PONTO); sinal(PONTO);   // S
  delay(2000);                                // pausa antes de repetir
}
