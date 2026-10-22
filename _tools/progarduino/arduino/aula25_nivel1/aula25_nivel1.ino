// Aula 25 – Nível 1: Vetor de pinos
// pecas: led 3 vermelho; led 5 amarelo; led 6 verde; led 9 azul
// Os pinos ficam num vetor: o mesmo código serve para qualquer quantidade de LEDs
#include <Arduino.h>                                    // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINOS[] = {3, 5, 6, 9};                       // pinos fora de ordem, sem problema
const int N = sizeof(PINOS) / sizeof(PINOS[0]);         // quantidade de elementos

void setup() {                                          // roda uma vez, quando a placa liga
  for (int i = 0; i < N; i++) pinMode(PINOS[i], OUTPUT);   // configura cada pino do vetor
}

void loop() {                                           // repete para sempre
  for (int i = 0; i < N; i++) {                         // percorre o vetor
    digitalWrite(PINOS[i], HIGH);                       // acende/liga PINOS[i]
    delay(250);                                         // espera 250 ms
    digitalWrite(PINOS[i], LOW);                        // apaga/desliga PINOS[i]
  }
}
