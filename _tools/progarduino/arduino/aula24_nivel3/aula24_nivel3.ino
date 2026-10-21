// Aula 24 – Nível 3: Revisão: servo pelo ultrassom
// pecas: ultrassom 9 10; servo 6
// Revisão: 5 a 50 cm de distância viram 0 a 180° no servo
#include <Servo.h>
#define TRIG 9                          // TRIG do HC-SR04 no pino 9
#define ECHO 10                         // ECHO do HC-SR04 no pino 10
Servo motor;                            // objeto que controla o servo

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(TRIG, OUTPUT);                // TRIG como saída
  pinMode(ECHO, INPUT);                 // ECHO como entrada
  motor.attach(6);                      // sinal do servo no pino 6
}

void loop() {                           // repete para sempre
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);   // garante o TRIG em nível baixo
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);   // pulso de 10 µs dispara a medição
  digitalWrite(TRIG, LOW);              // fim do pulso
  int cm = pulseIn(ECHO, HIGH) * 0.0343 / 2;   // distância em cm (inteira)
  motor.write(map(constrain(cm, 5, 50), 5, 50, 0, 180));   // 5 a 50 cm → 0 a 180°
  delay(60);                            // espera 60 ms
}
