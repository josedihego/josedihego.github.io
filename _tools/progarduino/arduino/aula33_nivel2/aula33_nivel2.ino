// Aula 33 – Nível 2: Vetor de structs: vários LEDs
// pecas: led 8 vermelho; led 9 amarelo; led 10 verde
// Cada LED pisca no seu ritmo; uma função atualiza qualquer LED
struct Led {                                   // tudo o que descreve um LED que pisca sozinho
  int pino;                                    // declara pino (int)
  unsigned long periodo;                       // declara periodo (unsigned long)
  unsigned long ultimo;                        // declara ultimo (unsigned long)
  bool aceso;                                  // declara aceso (bool)
};

Led leds[] = {{8, 250, 0, false}, {9, 600, 0, false}, {10, 1300, 0, false}};   // 3 LEDs com períodos diferentes
const int N = sizeof(leds) / sizeof(leds[0]);   // quantidade de LEDs

void atualizar(Led &l) {                       // & no C++ do Arduino: altera o original
  if (millis() - l.ultimo >= l.periodo) {      // passou o período deste LED?
    l.ultimo = millis();                       // marca a troca
    l.aceso = !l.aceso;                        // inverte
    digitalWrite(l.pino, l.aceso);             // l.pino recebe l.aceso (verdadeiro acende, falso apaga)
  }
}

void setup() {                                 // roda uma vez, quando a placa liga
  for (int i = 0; i < N; i++) pinMode(leds[i].pino, OUTPUT);   // configura o pino de cada LED
}

void loop() {                                  // repete para sempre
  for (int i = 0; i < N; i++) atualizar(leds[i]);   // cada LED cuida do seu ritmo
}
