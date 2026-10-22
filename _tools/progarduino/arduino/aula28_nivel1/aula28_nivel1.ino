// Aula 28 – Nível 1: Função piscar(pino, vezes)
// pecas: led 8 vermelho; led 9 verde
// Uma função com parâmetros evita repetir código
#include <Arduino.h>                        // funções do Arduino (pinMode, digitalWrite, delay...)
void piscar(int pino, int vezes) {          // dois parâmetros
  for (int i = 0; i < vezes; i++) {         // repete 'vezes' vezes
    digitalWrite(pino, HIGH); delay(200);   // acende/liga pino e espera 200 ms
    digitalWrite(pino, LOW);  delay(200);   // apaga/desliga pino e espera 200 ms
  }
}

void setup() {                              // roda uma vez, quando a placa liga
  pinMode(8, OUTPUT);                       // 8 como saída
  pinMode(9, OUTPUT);                       // 9 como saída
}

void loop() {                               // repete para sempre
  piscar(8, 3);                             // vermelho 3 vezes
  piscar(9, 2);                             // verde 2 vezes
  delay(1000);                              // espera 1000 ms
}
