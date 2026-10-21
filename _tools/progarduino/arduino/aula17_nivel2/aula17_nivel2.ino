// Aula 17 – Nível 2: Dado com 6 LEDs
// pecas: botao 2; led 3 vermelho; led 4 vermelho; led 5 vermelho; led 6 vermelho; led 7 vermelho; led 8 vermelho
// Acende de 1 a 6 LEDs conforme o número sorteado
#define PINO_BOTAO 2                           // botão no pino 2

void setup() {                                 // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);           // PINO_BOTAO como entrada com pull-up interno
  for (int pino = 3; pino <= 8; pino++) pinMode(pino, OUTPUT);   // pinos 3 a 8 como saída
  randomSeed(analogRead(A5));                  // pino solto gera ruído: sorteios diferentes a cada vez
}

void loop() {                                  // repete para sempre
  if (digitalRead(PINO_BOTAO) == LOW) {        // botão apertado?
    int dado = random(1, 7);                   // sorteia de 1 a 6
    for (int i = 0; i < 6; i++) {              // percorre os 6 LEDs
      digitalWrite(3 + i, i < dado);           // acende os primeiros 'dado' LEDs
    }
    delay(400);                                // espera 400 ms
  }
}
