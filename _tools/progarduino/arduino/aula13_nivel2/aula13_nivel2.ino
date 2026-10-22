// Aula 13 – Nível 2: Sequência de LEDs
// pecas: led 2 vermelho; led 3 vermelho; led 4 vermelho; led 5 vermelho; led 6 vermelho
// Acende os LEDs dos pinos 2 a 6, um de cada vez
#include <Arduino.h>                                             // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                                   // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 6; pino++) pinMode(pino, OUTPUT);   // configura todos com um laço
}

void loop() {                                                    // repete para sempre
  for (int pino = 2; pino <= 6; pino++) {   // percorre os pinos
    digitalWrite(pino, HIGH);                                    // acende/liga pino
    delay(150);                                                  // espera 150 ms
    digitalWrite(pino, LOW);                                     // apaga/desliga pino
  }
}
