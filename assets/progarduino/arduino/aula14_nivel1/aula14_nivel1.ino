// Aula 14 – Nível 1: Média de 10 leituras
// Soma 10 leituras e mostra a média: o valor fica mais estável
#include <Arduino.h>                            // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                  // roda uma vez, quando a placa liga
  Serial.begin(9600);                           // abre o Monitor Serial a 9600 baud
}

void loop() {                                   // repete para sempre
  long soma = 0;                                // long: 10 × 1023 não cabe com folga em int
  for (int i = 0; i < 10; i++) {                // 10 voltas
    soma += analogRead(A0);                     // acumula
    delay(5);                                   // espera 5 ms
  }
  Serial.println(soma / 10);                    // média
  delay(200);                                   // espera 200 ms
}
