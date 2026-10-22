// Aula 23 – Nível 2: Simulado: média de 20 leituras do LDR
// pecas: ldr A0
// Simulado: média de 20 leituras a cada segundo
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                          // roda uma vez, quando a placa liga
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  long soma = 0;                        // long: a soma de muitas leituras passa de 32767
  for (int i = 0; i < 20; i++) {        // 20 leituras
    soma += analogRead(A0);             // acumula a leitura
    delay(10);                          // espera 10 ms
  }
  Serial.println(soma / 20);            // envia soma / 20 ao Monitor Serial e quebra a linha
  delay(800);                           // espera 800 ms
}
