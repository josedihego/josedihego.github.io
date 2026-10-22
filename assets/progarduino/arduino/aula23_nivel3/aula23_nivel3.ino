// Aula 23 – Nível 3: Simulado: distância em 3 faixas
// Simulado: verde acima de 50 cm, amarelo de 20 a 50, vermelho abaixo de 20
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
#define TRIG 9                          // TRIG do HC-SR04 no pino 9
#define ECHO 10                         // ECHO do HC-SR04 no pino 10

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                // TRIG como saída
  pinMode(ECHO, INPUT);                 // ECHO como entrada
  for (int p = 4; p <= 6; p++) pinMode(p, OUTPUT);   // pinos 4 a 6 como saída
}

void loop() {                           // repete para sempre
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);   // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);   // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);              // fim do pulso
  float cm = pulseIn(ECHO, HIGH) * 0.0343 / 2;   // tempo de eco → distância em cm
  digitalWrite(4, cm > 50);             // 4 recebe cm > 50 (verdadeiro acende, falso apaga)
  digitalWrite(5, cm >= 20 && cm <= 50);   // 5 recebe cm >= 20 && cm <= 50 (verdadeiro acende, falso apaga)
  digitalWrite(6, cm < 20);             // 6 recebe cm < 20 (verdadeiro acende, falso apaga)
  delay(150);                           // espera 150 ms
}
