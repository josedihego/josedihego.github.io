// Aula 23 – Nível 1: Simulado: N piscadas pelo potenciômetro
// pecas: pot A0; botao 2; led 8 vermelho
// Simulado: ao apertar o botão, pisca de 1 a 10 vezes conforme o potenciômetro
#define PINO_BOTAO 2                    // botão no pino 2
#define PINO_LED 8                      // LED no pino 8

void setup() {                          // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);    // PINO_BOTAO como entrada com pull-up interno
  pinMode(PINO_LED, OUTPUT);            // PINO_LED como saída
}

void loop() {                           // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {   // botão apertado?
    int vezes = map(analogRead(A0), 0, 1023, 1, 10);   // potenciômetro escolhe 1 a 10
    for (int i = 0; i < vezes; i++) {   // repete 'vezes' vezes
      digitalWrite(PINO_LED, HIGH); delay(200);   // acende/liga PINO_LED e espera 200 ms
      digitalWrite(PINO_LED, LOW);  delay(200);   // apaga/desliga PINO_LED e espera 200 ms
    }
  }
}
