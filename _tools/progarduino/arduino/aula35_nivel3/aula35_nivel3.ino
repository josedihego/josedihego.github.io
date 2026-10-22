// Aula 35 – Nível 3: Simulado: comando e struct
// pecas: led 8 vermelho
// Simulado: comando "PERIODO n" muda o ritmo de um LED descrito por um struct
#include <Arduino.h>                    // funções do Arduino (pinMode, digitalWrite, delay...)
struct Led { int pino; unsigned long periodo; unsigned long ultimo; bool aceso; };   // um LED que pisca sozinho
Led led = {8, 500, 0, false};           // pino 8, meio segundo

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(led.pino, OUTPUT);            // led.pino como saída
  Serial.begin(9600);                   // abre o Monitor Serial a 9600 baud
}

void loop() {                           // repete para sempre
  if (Serial.available() > 0) {         // chegou algo pela serial?
    String s = Serial.readStringUntil('\n');   // lê a linha até o Enter
    s.trim();                           // tira espaços e \r
    s.toUpperCase();                    // aceita maiúsculas e minúsculas
    if (s.startsWith("PERIODO ")) led.periodo = s.substring(8).toInt();   // PERIODO n: novo ritmo
  }
  if (millis() - led.ultimo >= led.periodo) {   // passou o período?
    led.ultimo = millis();              // marca a troca
    led.aceso = !led.aceso;             // inverte
    digitalWrite(led.pino, led.aceso);   // led.pino recebe led.aceso (verdadeiro acende, falso apaga)
  }
}
