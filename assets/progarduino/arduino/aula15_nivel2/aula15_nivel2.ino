// Aula 15 – Nível 2: Esperar escurecer
// O programa espera (while) até ficar escuro, então pisca o LED 3 vezes
#include <Arduino.h>                          // funções do Arduino (pinMode, digitalWrite, delay...)
#define PINO_LED 8                            // LED no pino 8

void setup() {                                // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                  // PINO_LED como saída
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
}

void loop() {                                 // repete para sempre
  Serial.println("Esperando escurecer...");   // envia o texto ao Monitor Serial e quebra a linha
  while (analogRead(A0) < 600) {              // claro: continua esperando
    delay(50);                                // espera 50 ms
  }
  for (int i = 0; i < 3; i++) {               // escureceu: sinaliza
    digitalWrite(PINO_LED, HIGH); delay(200);   // acende/liga PINO_LED e espera 200 ms
    digitalWrite(PINO_LED, LOW);  delay(200);   // apaga/desliga PINO_LED e espera 200 ms
  }
  while (analogRead(A0) >= 600) {             // espera clarear antes de recomeçar
    delay(50);                                // espera 50 ms
  }
}
