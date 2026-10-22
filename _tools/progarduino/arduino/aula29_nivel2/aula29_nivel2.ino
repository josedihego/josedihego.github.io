// Aula 29 – Nível 2: Função que acende a barra
// pecas: pot A0; led 2 verde; led 3 verde; led 4 amarelo; led 5 amarelo; led 6 vermelho
// acender_barra(nivel) usa o vetor de pinos
#include <Arduino.h>                         // funções do Arduino (pinMode, digitalWrite, delay...)
const int BARRA[] = {2, 3, 4, 5, 6};         // pinos da barra de LEDs
const int N = 5;                             // quantidade de LEDs

void acender_barra(int nivel) {              // acende os 'nivel' primeiros LEDs
  for (int i = 0; i < N; i++) digitalWrite(BARRA[i], i < nivel);   // acende os primeiros 'nivel' LEDs
}

void setup() {                               // roda uma vez, quando a placa liga
  for (int i = 0; i < N; i++) pinMode(BARRA[i], OUTPUT);   // configura os pinos da barra
}

void loop() {                                // repete para sempre
  acender_barra(map(analogRead(A0), 0, 1023, 0, N));   // potenciômetro → 0 a N LEDs
  delay(30);                                 // espera 30 ms
}
