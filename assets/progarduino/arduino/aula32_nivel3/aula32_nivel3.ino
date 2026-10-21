// Aula 32 – Nível 3: Animações escolhidas pelo botão
// Matriz 3D: animação, quadro, LED. O botão troca a animação
#define PINO_BOTAO 7                                            // botão no pino 7
const byte ANIM[3][4][4] = {                                    // 3 animações × 4 quadros × 4 LEDs
  {{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}},     // corrida
  {{1, 0, 0, 1}, {0, 1, 1, 0}, {1, 0, 0, 1}, {0, 1, 1, 0}},     // vai e vem
  {{1, 1, 1, 1}, {0, 0, 0, 0}, {1, 1, 1, 1}, {0, 0, 0, 0}}};    // pisca tudo
int atual = 0;                                                  // animação escolhida

void setup() {                                                  // roda uma vez, quando a placa liga
  pinMode(PINO_BOTAO, INPUT_PULLUP);                            // PINO_BOTAO como entrada com pull-up interno
  for (int p = 2; p <= 5; p++) pinMode(p, OUTPUT);              // pinos 2 a 5 como saída
}

void loop() {                                                   // repete para sempre
  for (int q = 0; q < 4; q++) {                                 // percorre os 4 quadros
    for (int l = 0; l < 4; l++) digitalWrite(2 + l, ANIM[atual][q][l]);   // mostra o quadro nos 4 LEDs
    delay(200);                                                 // espera 200 ms
    if (digitalRead(PINO_BOTAO) == LOW) {          // troca a animação
      atual = (atual + 1) % 3;                                  // próxima animação (volta à primeira depois da terceira)
      delay(250);                                               // espera 250 ms
    }
  }
}
