// Aula 6 – Nível 3: Luz automática com histerese
// Dois limiares evitam que o LED fique piscando quando a luz está perto do limite
#include <Arduino.h>                      // funções do Arduino (pinMode, digitalWrite, delay...)
const int PINO_LED = 8;                   // pino do LED (com resistor de 220 ohms)
const int LIGA = 600;                     // liga acima deste valor (escuro)
const int DESLIGA = 450;                  // desliga abaixo deste valor (claro)
bool aceso = false;                       // estado atual do LED

void setup() {                            // roda uma vez, quando a placa liga
  pinMode(PINO_LED, OUTPUT);              // PINO_LED como saída
  Serial.begin(9600);                     // abre o Monitor Serial a 9600 baud
}

void loop() {                             // repete para sempre
  int luz = analogRead(A0);               // lê o sensor de luz (0 a 1023)
  if (!aceso && luz > LIGA) {             // estava apagado e escureceu bem
    aceso = true;                         // passa a acender
  } else if (aceso && luz < DESLIGA) {    // estava aceso e clareou bem
    aceso = false;                        // passa a apagar
  }                                       // entre os limiares: mantém como está
  digitalWrite(PINO_LED, aceso);          // PINO_LED recebe aceso (verdadeiro acende, falso apaga)
  Serial.print(luz);                      // envia luz ao Monitor Serial
  Serial.println(aceso ? "  LED aceso" : "  LED apagado");   // envia aceso ? "  LED aceso" : "  LED apagado" ao Monitor Serial e quebra a linha
  delay(100);                             // espera 100 ms
}
