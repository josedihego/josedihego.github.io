// Aula 32 – Nível 2: Padrões de LEDs numa matriz
// pecas: led 2 vermelho; led 3 vermelho; led 4 vermelho; led 5 vermelho
// Cada linha é um quadro da animação: 1 = aceso
#include <Arduino.h>                              // funções do Arduino (pinMode, digitalWrite, delay...)
const byte QUADROS[][4] = {                       // byte ocupa 1 byte: economiza a RAM do Uno
  {1, 0, 0, 1},                                   // quadro 1: pontas
  {0, 1, 1, 0},                                   // quadro 2: meio
  {1, 1, 1, 1},                                   // quadro 3: todos
  {0, 0, 0, 0},                                   // quadro 4: nenhum
  {1, 0, 1, 0},                                   // quadro 5: alternados
  {0, 1, 0, 1}};                                  // quadro 6: alternados invertidos
const int NQ = sizeof(QUADROS) / sizeof(QUADROS[0]);   // quantidade de quadros

void setup() {                                    // roda uma vez, quando a placa liga
  for (int p = 2; p <= 5; p++) pinMode(p, OUTPUT);   // pinos 2 a 5 como saída
}

void loop() {                                     // repete para sempre
  for (int q = 0; q < NQ; q++) {                  // linhas: quadros
    for (int l = 0; l < 4; l++) {                 // colunas: LEDs
      digitalWrite(2 + l, QUADROS[q][l]);         // 2 + l recebe QUADROS[q][l] (verdadeiro acende, falso apaga)
    }
    delay(300);                                   // espera 300 ms
  }
}
