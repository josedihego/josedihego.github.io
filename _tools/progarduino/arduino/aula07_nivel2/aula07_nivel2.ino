// Aula 7 – Nível 2: Barra de 5 LEDs
// pecas: pot A0; led 2 verde; led 3 verde; led 4 amarelo; led 5 amarelo; led 6 vermelho
// Quanto maior a leitura, mais LEDs acesos (gráfico de barras)
#include <Arduino.h>                                // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                      // roda uma vez, quando a placa liga
  for (int pino = 2; pino <= 6; pino++) pinMode(pino, OUTPUT);   // pinos 2 a 6 como saída
}

void loop() {                                       // repete para sempre
  int nivel = map(analogRead(A0), 0, 1023, 0, 5);   // 0 a 5 LEDs
  digitalWrite(2, nivel >= 1);                      // cada LED acende a partir de um nível
  digitalWrite(3, nivel >= 2);                      // 3 recebe nivel >= 2 (verdadeiro acende, falso apaga)
  digitalWrite(4, nivel >= 3);                      // 4 recebe nivel >= 3 (verdadeiro acende, falso apaga)
  digitalWrite(5, nivel >= 4);                      // 5 recebe nivel >= 4 (verdadeiro acende, falso apaga)
  digitalWrite(6, nivel >= 5);                      // 6 recebe nivel >= 5 (verdadeiro acende, falso apaga)
}
