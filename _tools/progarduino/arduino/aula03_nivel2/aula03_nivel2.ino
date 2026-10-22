// Aula 3 – Nível 2: Piscar N vezes
// pecas: led 8 verde
// Digite quantas vezes o LED do pino 8 deve piscar
#include <Arduino.h>                          // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINO_LED = 8;                       // pino do LED (com resistor de 220 ohms)

void setup() {                                // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);                  // PINO_LED como saída
  Serial.begin(9600);                         // abre o Monitor Serial a 9600 baud
  Serial.println("Quantas piscadas?");        // envia o texto ao Monitor Serial e quebra a linha
}

void loop() {                                 // repete para sempre
  if (Serial.available() > 0) {               // chegou um número?
    int vezes = Serial.parseInt();            // lê o número
    while (Serial.available() > 0) Serial.read();   // limpa o Enter
    for (int i = 0; i < vezes; i++) {         // repete 'vezes' vezes
      digitalWrite(PINO_LED, HIGH);           // acende/liga PINO_LED
      delay(250);                             // espera 250 ms
      digitalWrite(PINO_LED, LOW);            // apaga/desliga PINO_LED
      delay(250);                             // espera 250 ms
    }
    Serial.println("Pronto! Quantas piscadas?");   // envia o texto ao Monitor Serial e quebra a linha
  }
}
