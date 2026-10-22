// Aula 18 – Nível 3: Contagem regressiva na barra de LEDs
// Barra cheia que vai esvaziando: um LED apaga a cada segundo
#include <Arduino.h>                                        // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                              // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 6; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 6 como saída
}

void loop() {                                               // repete para sempre
  for (int restantes = 5; restantes >= 0; restantes--) {    // de 5 a 0 LEDs
    for (int i = 0; i < 5; i++) {                           // atualiza os 5 LEDs
      digitalWrite(2 + i, i < restantes);                   // 2 + i recebe i < restantes (verdadeiro acende, falso apaga)
    }
    delay(1000);                                            // espera 1000 ms
  }
  for (int i = 0; i < 3; i++) {                             // fim: pisca tudo
    for (int p = 2; p <= 6; p++) digitalWrite(p, HIGH);     // acende todos
    delay(150);                                             // espera 150 ms
    for (int p = 2; p <= 6; p++) digitalWrite(p, LOW);      // apaga todos
    delay(150);                                             // espera 150 ms
  }
}
