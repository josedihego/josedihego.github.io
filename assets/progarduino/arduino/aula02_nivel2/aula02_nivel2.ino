// Aula 2 – Nível 2: Contador de segundos
// Conta os segundos desde que a placa ligou
#include <Arduino.h>                  // funções do Arduino (pinMode, digitalWrite, delay...)
int segundos = 0;                     // contador

void setup() {                        // roda uma vez, quando a placa liga
  Serial.begin(9600);                 // serial a 9600 baud
}

void loop() {                         // repete para sempre
  Serial.print("Segundos: ");         // envia o texto ao Monitor Serial
  Serial.println(segundos);           // mostra o valor atual
  segundos = segundos + 1;            // soma 1
  delay(1000);                        // espera 1 segundo
}
