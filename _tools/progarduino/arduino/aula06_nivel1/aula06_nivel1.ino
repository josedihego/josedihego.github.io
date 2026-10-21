// Aula 6 – Nível 1: Botão acende o LED
// pecas: botao 2; led 8 vermelho
// Enquanto o botão estiver apertado o LED fica aceso
const int PINO_BOTAO = 2, PINO_LED = 8;   // pinos do botão e do LED

void setup() {                            // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);      // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);              // PINO_LED como saída
}

void loop() {                             // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {   // apertado?
    digitalWrite(PINO_LED, HIGH);         // acende
  } else {                                // solto
    digitalWrite(PINO_LED, LOW);          // apaga
  }
}
