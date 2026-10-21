// Aula 11 – Nível 2: Simulado: botão e potenciômetro
// Simulado: com o botão apertado, o potenciômetro controla o brilho; solto, o LED apaga
#define PINO_BOTAO 2                             // botão no pino 2
#define PINO_LED 9                               // LED no pino 9

void setup() {                                   // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);             // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);                     // PINO_LED como saída
}

void loop() {                                    // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {          // botão apertado?
    analogWrite(PINO_LED, analogRead(A0) / 4);   // 0..1023 dividido por 4 = 0..255
  } else {
    analogWrite(PINO_LED, 0);                    // apaga
  }
}
