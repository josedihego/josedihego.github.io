// Aula 17 – Nível 1: Dado no Monitor Serial
// pecas: botao 2
// Cada toque no botão joga um dado de 6 faces
#define PINO_BOTAO 2                           // botão no pino 2

void setup() {                                 // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);           // PINO_BOTAO como entrada com pull-up interno
  Serial.begin(9600);                          // abre o Monitor Serial a 9600 baud
  randomSeed(analogRead(A5));                  // pino solto gera ruído: semente diferente
}

void loop() {                                  // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {        // botão apertado?
    Serial.print("Saiu ");                     // envia o texto ao Monitor Serial
    Serial.println(random(1, 7));              // random(1, 7) sorteia de 1 a 6
    delay(300);                                // evita várias jogadas num toque
  }
}
