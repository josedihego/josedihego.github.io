// Aula 20 – Nível 2: Alarme de aproximação
// Acende o LED quando algo chega a menos de 20 cm
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
#define TRIG 9                          // TRIG do HC-SR04 no pino 9
#define ECHO 10                         // ECHO do HC-SR04 no pino 10
#define PINO_LED 8                      // LED no pino 8

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                // TRIG como saída
  pinMode(ECHO, INPUT);                 // ECHO como entrada
  pinMode(PINO_LED, OUTPUT);            // PINO_LED como saída
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);   // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);   // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);              // fim do pulso
  float cm = pulseIn(ECHO, HIGH) * 0.0343 / 2;   // tempo de eco → distância em cm
  digitalWrite(PINO_LED, cm < 20);      // PINO_LED recebe cm < 20 (verdadeiro acende, falso apaga)
  Serial.println(cm, 1);                // envia cm ao Monitor Serial e quebra a linha
  delay(100);                           // espera 100 ms
}
