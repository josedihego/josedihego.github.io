// Aula 36 – Nível 2: Revisão: semáforo com vetor de structs
// Revisão: cada fase do semáforo é um struct {pino, duração}
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
struct Fase { int pino; unsigned long duracao; };   // uma fase do semáforo
Fase fases[] = {{8, 3000}, {9, 1000}, {10, 3000}};   // verde, amarelo e vermelho

void setup() {                          // roda uma vez, quando a placa liga
  for (int i = 0; i < 3; i++) pinMode(fases[i].pino, OUTPUT);   // configura o pino de cada fase
}

void loop() {                           // repete para sempre
  for (int i = 0; i < 3; i++) {         // 3 voltas
    digitalWrite(fases[i].pino, HIGH);   // acende/liga fases[i].pino
    delay(fases[i].duracao);            // espera o tempo calculado (ms)
    digitalWrite(fases[i].pino, LOW);   // apaga/desliga fases[i].pino
  }
}
