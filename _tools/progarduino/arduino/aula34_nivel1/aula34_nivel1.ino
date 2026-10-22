// Aula 34 – Nível 1: Estação: leituras em CSV
// pecas: ldr A0; pot A1
// Uma linha CSV por segundo: tempo, luz, temperatura simulada (cole no Google Planilhas)
#include <Arduino.h>                               // funções do Arduino (pinMode, digitalWrite, delay...)
void setup() {                                     // roda uma vez, quando a placa liga
  Serial.begin(9600);                              // abre o Monitor Serial a 9600 baud
  Serial.println("segundos,luz,temperatura");      // cabeçalho
}

void loop() {                                      // repete para sempre
  int luz = analogRead(A0);                        // lê o sensor de luz (0 a 1023)
  float temperatura = analogRead(A1) * 50.0 / 1023;  // potenciômetro simula 0 a 50 °C
  Serial.print(millis() / 1000);                   // envia millis() / 1000 ao Monitor Serial
  Serial.print(",");                               // envia o texto ao Monitor Serial
  Serial.print(luz);                               // envia luz ao Monitor Serial
  Serial.print(",");                               // envia o texto ao Monitor Serial
  Serial.println(temperatura, 1);                  // envia temperatura ao Monitor Serial e quebra a linha
  delay(1000);                                     // espera 1000 ms
}
