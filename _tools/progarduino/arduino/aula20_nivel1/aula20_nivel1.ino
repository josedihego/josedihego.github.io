// Aula 20 – Nível 1: Distância com o HC-SR04
// pecas: ultrassom 9 10
// Mede a distância com o sensor ultrassônico (TRIG no 9, ECHO no 10)
#include <Arduino.h>                           // funções do Arduino (pinMode, digitalWrite, delay...)
#define TRIG 9                                 // TRIG do HC-SR04 no pino 9
#define ECHO 10                                // ECHO do HC-SR04 no pino 10

void setup() {                                 // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                       // TRIG como saída
  pinMode(ECHO, INPUT);                        // ECHO como entrada
  Serial.begin(9600);                          // abre o Monitor Serial a 9600 baud
}

void loop() {                                  // repete para sempre
  digitalWrite(TRIG, LOW);                     // fim do pulso
  delayMicroseconds(2);                        // espera 2 µs
  digitalWrite(TRIG, HIGH);                    // pulso de 10 µs dispara a medição
  delayMicroseconds(10);                       // pulso de 10 µs
  digitalWrite(TRIG, LOW);                     // fim do pulso
  long eco = pulseIn(ECHO, HIGH);              // duração do eco em µs
  float cm = eco * 0.0343 / 2;                 // ida e volta
  Serial.print(cm, 1);                         // envia cm ao Monitor Serial
  Serial.println(" cm");                       // envia o texto ao Monitor Serial e quebra a linha
  delay(200);                                  // espera 200 ms
}
