// Aula 21 – Nível 3: Servo segue o potenciômetro
// pecas: pot A0; servo 9
// O ângulo do servo (0 a 180°) acompanha o potenciômetro
#include <Arduino.h>                       // funções do Arduino (pinMode, digitalWrite, delay...)
#include <Servo.h>                         // biblioteca do servo
Servo motor;                               // objeto que controla o servo

void setup() {                             // roda uma vez, quando a placa liga
  motor.attach(9);                         // sinal do servo no pino 9
  Serial.begin(9600);                      // abre o Monitor Serial a 9600 baud
}

void loop() {                              // repete para sempre
  int angulo = map(analogRead(A0), 0, 1023, 0, 180);   // leitura → ângulo
  motor.write(angulo);                     // gira até o ângulo pedido
  Serial.println(angulo);                  // envia angulo ao Monitor Serial e quebra a linha
  delay(15);                               // tempo para o servo se mover
}
