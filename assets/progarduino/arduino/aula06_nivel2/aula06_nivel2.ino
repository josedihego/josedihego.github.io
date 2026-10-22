// Aula 6 – Nível 2: Luz automática com LDR
// Acende o LED quando o ambiente fica escuro (sensor de luz LDR no A0)
#include <Arduino.h>                      // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINO_LED = 8;                   // pino do LED (com resistor de 220 ohms)
const int LIMIAR = 500;                   // ajuste olhando os valores no Monitor Serial

void setup() {                            // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);              // PINO_LED como saída
  Serial.begin(9600);                     // abre o Monitor Serial a 9600 baud
}

void loop() {                             // repete para sempre
  int luz = analogRead(A0);               // no módulo do Wokwi: mais luz = valor menor
  Serial.println(luz);                    // envia luz ao Monitor Serial e quebra a linha
  if (luz > LIMIAR) {                     // escuro
    digitalWrite(PINO_LED, HIGH);         // acende/liga PINO_LED
  } else {                                // claro
    digitalWrite(PINO_LED, LOW);          // apaga/desliga PINO_LED
  }
  delay(100);                             // espera 100 ms
}
